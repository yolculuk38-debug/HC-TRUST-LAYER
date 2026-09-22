"""Canonical record loader coverage for HC:// advisory runtime behavior."""

from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import pytest

from hc_runtime.canonical_record_loader import CanonicalRecordLoader
from hc_runtime.runtime import ValidatorPipeline
from hc_trust.hashing import HC_CONTENT_HASH_PROFILE, calculate_content_hash


def _sha256(content: object) -> str:
    if isinstance(content, str):
        return calculate_content_hash(content)
    return calculate_content_hash(content, HC_CONTENT_HASH_PROFILE)


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")


def _record(record_id: str, content: object = "canonical loader content") -> dict[str, object]:
    return {
        "schema_version": "hc-record-v1",
        "record_id": record_id,
        "created_at": "2026-08-08T12:00:00Z",
        "title": "Canonical loader test record",
        "record_type": "protocol_note",
        "witness_type": "human",
        "author": "HC-TRUST-LAYER tests",
        "content": content,
        "content_hash": _sha256(content),
        "content_hash_profile": HC_CONTENT_HASH_PROFILE,
        "archive_ref": "pending_archive",
        "verification_status": "draft",
    }


def _run(root: Path, record_id: str) -> dict[str, Any]:
    return ValidatorPipeline(canonical_loader=CanonicalRecordLoader(root=root)).run(
        record_id=record_id,
        qr_input=f"hc://{record_id} hash:advisory",
    )


def test_valid_canonical_record_loads_from_approved_directory_with_verified_status(tmp_path: Path) -> None:
    record_id = "HC-LOADER-2026-0001"
    _write_json(tmp_path / "records" / "pending" / f"{record_id}.json", _record(record_id, {"claim": "HC://"}))

    result = _run(tmp_path, record_id)

    assert result["canonical_bridge"]["lookup_performed"] is True
    assert result["canonical_bridge"]["found"] is True
    assert result["canonical_bridge"]["lookup_status"] == "verified"
    assert result["schema_result"]["valid"] is True
    assert result["hash_result"]["hash_verified"] is True
    assert result["trust_assignment"]["warnings"] == []


def test_missing_canonical_record_returns_explicit_missing_status(tmp_path: Path) -> None:
    result = _run(tmp_path, "HC-LOADER-MISSING")

    assert result["canonical_bridge"]["lookup_status"] == "missing"
    assert result["canonical_bridge"]["found"] is False
    assert result["schema_result"]["valid"] is False
    assert result["hash_result"]["hash_verified"] is False
    assert any("lookup returned no record" in warning.lower() for warning in result["trust_assignment"]["warnings"])


def test_malformed_json_returns_explicit_malformed_status_without_unsafe_parse(tmp_path: Path) -> None:
    record_id = "HC-LOADER-MALFORMED"
    path = tmp_path / "records" / "verified" / f"{record_id}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('{"record_id": "HC-LOADER-MALFORMED",', encoding="utf-8")

    result = _run(tmp_path, record_id)

    assert result["canonical_bridge"]["lookup_status"] == "malformed"
    assert result["canonical_bridge"]["malformed"] is True
    assert result["schema_result"]["valid"] is False
    assert any("malformed" in warning.lower() for warning in result["trust_assignment"]["warnings"])


def test_malformed_filename_hint_takes_precedence_over_valid_record_id_collision(
    tmp_path: Path,
) -> None:
    record_id = "HC-COLLISION-2026-0001"
    _write_json(
        tmp_path / "records" / "pending" / "valid-other-name.json",
        _record(record_id),
    )
    malformed = tmp_path / "records" / "verified" / f"{record_id}.json"
    malformed.parent.mkdir(parents=True, exist_ok=True)
    malformed.write_text(
        f'{{"record_id":"{record_id}","record_id":"attacker"}}',
        encoding="utf-8",
    )

    result = _run(tmp_path, record_id)

    assert result["canonical_bridge"]["lookup_status"] == "malformed"
    assert result["canonical_bridge"]["malformed"] is True
    assert result["schema_result"]["valid"] is False
    assert result["hash_result"]["hash_verified"] is False


def test_generated_index_cache_and_export_files_are_ignored(tmp_path: Path) -> None:
    record_id = "HC-LOADER-IGNORED"
    ignored_record = _record(record_id)
    _write_json(tmp_path / "generated" / f"{record_id}.json", ignored_record)
    _write_json(tmp_path / "records" / "pending" / "explorer_index.json", ignored_record)
    _write_json(tmp_path / "records" / "pending" / f"{record_id}-index.json", ignored_record)
    _write_json(tmp_path / "records" / "pending" / "cache" / f"{record_id}.json", ignored_record)
    _write_json(tmp_path / "records" / "pending" / f"{record_id}-export.json", ignored_record)

    result = _run(tmp_path, record_id)

    assert result["canonical_bridge"]["lookup_status"] == "missing"
    assert result["canonical_bridge"]["found"] is False


@pytest.mark.parametrize("word", ["INDEX", "MANIFEST", "CACHE", "EXPORT", "GENERATED"])
def test_runtime_loads_canonical_ids_containing_artifact_words(tmp_path, word):
    record_id = f"HC-{word}-2026-0001"
    _write_json(tmp_path / "records/pending" / f"{record_id}.json", _record(record_id))
    result = _run(tmp_path, record_id)
    assert result["canonical_bridge"]["lookup_status"] == "verified"
    assert result["schema_result"]["valid"] is True
    assert result["hash_result"]["hash_verified"] is True


def test_runtime_loads_documented_legacy_archive_record(tmp_path):
    record_id = "HC-LEGACY-2026-0001"
    _write_json(tmp_path / "records/archive" / f"{record_id}.json", _record(record_id))
    assert _run(tmp_path, record_id)["canonical_bridge"]["lookup_status"] == "verified"


def test_content_hash_mismatch_returns_explicit_hash_mismatch_status(tmp_path: Path) -> None:
    record_id = "HC-HASHMISMATCH-2026-0001"
    record = _record(record_id, "canonical content")
    record["content_hash"] = _sha256("different content")
    _write_json(
        tmp_path / "records" / "archived" / f"{record_id}.json",
        record,
    )

    result = _run(tmp_path, record_id)

    assert result["canonical_bridge"]["lookup_status"] == "hash_mismatch"
    assert result["canonical_bridge"]["schema_valid"] is True
    assert result["hash_result"]["hash_verified"] is False
    assert any("content_hash mismatch" in warning.lower() for warning in result["trust_assignment"]["warnings"])


@pytest.mark.parametrize("contents", [("same", "same"), ("first", "second"), ("same", "same", "different")])
def test_duplicate_ids_never_select_a_record(tmp_path, contents):
    record_id = "HC-DUPLICATE-2026-0001"
    for group, content in zip(("pending", "verified", "archived"), contents):
        _write_json(tmp_path / "records" / group / f"{record_id}.json", _record(record_id, content))
    result = _run(tmp_path, record_id)
    assert result["canonical_bridge"]["lookup_status"] == "duplicate_record_id"
    assert result["canonical_bridge"]["found"] is False
    assert result["schema_result"]["checked"] is False
    assert result["hash_result"]["checked"] is False
    assert result["hash_result"]["hash_verified"] is False


def test_collision_refresh_recovers_only_after_duplicate_removed(tmp_path):
    from hc_runtime.canonical_record_loader import DUPLICATE_RECORD

    record_id = "HC-DUPLICATE-2026-0002"
    first = tmp_path / "records/pending/one.json"
    second = tmp_path / "records/pending/nested/two.json"
    _write_json(first, _record(record_id))
    loader = CanonicalRecordLoader(root=tmp_path)
    assert isinstance(loader.get(record_id), dict)
    _write_json(second, _record(record_id))
    loader.refresh()
    assert loader.get(record_id) is DUPLICATE_RECORD
    second.unlink()
    assert loader.get(record_id) is DUPLICATE_RECORD
    loader.refresh()
    assert isinstance(loader.get(record_id), dict)


def test_concurrent_cold_start_scans_canonical_records_once(tmp_path, monkeypatch):
    record_id = "HC-CONCURRENT-2026-0001"
    _write_json(tmp_path / "records/pending/one.json", _record(record_id))
    loader = CanonicalRecordLoader(root=tmp_path)
    original_load = CanonicalRecordLoader._load
    scans = 0

    def counted_load(instance):
        nonlocal scans
        scans += 1
        time.sleep(0.05)
        original_load(instance)

    monkeypatch.setattr(CanonicalRecordLoader, "_load", counted_load)
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(loader.get, (record_id, record_id)))

    assert scans == 1
    assert all(isinstance(result, dict) for result in results)


def test_ignored_artifact_does_not_create_collision(tmp_path):
    record_id = "HC-DUPLICATE-2026-0003"
    _write_json(tmp_path / "records/pending/one.json", _record(record_id))
    _write_json(tmp_path / "records/pending/generated_index.json", _record(record_id))
    assert _run(tmp_path, record_id)["canonical_bridge"]["lookup_status"] == "verified"


def test_external_symlink_cannot_supply_a_canonical_record(tmp_path):
    record_id = "HC-SYMLINK-2026-0001"
    target = tmp_path / "outside.json"
    _write_json(target, _record(record_id))
    root = tmp_path / "repo"
    approved = root / "records/pending"
    approved.mkdir(parents=True)
    (approved / "record.json").symlink_to(target)
    assert CanonicalRecordLoader(root=root).get(record_id) is None


def test_symlinked_approved_directory_cannot_escape_root(tmp_path):
    record_id = "HC-SYMLINK-2026-0002"
    outside = tmp_path / "outside"
    _write_json(outside / "record.json", _record(record_id))
    root = tmp_path / "repo"
    (root / "records").mkdir(parents=True)
    (root / "records/pending").symlink_to(outside, target_is_directory=True)
    assert CanonicalRecordLoader(root=root).get(record_id) is None


def test_api_does_not_promote_duplicate_record_ids(tmp_path, monkeypatch):
    from fastapi.testclient import TestClient
    import hc_runtime.routes.verify as route
    from hc_runtime.app import create_app
    from hc_runtime.runtime import RuntimeQueueStore
    from hc_runtime.events import RuntimeEventStore
    from hc_runtime.contracts.abuse_signals import AdvisoryAbuseSignalTracker

    record_id = "HC-DUPLICATE-API-2026"
    for group in ("pending", "verified"):
        _write_json(tmp_path / "records" / group / "one.json", _record(record_id))
    monkeypatch.setattr(route, "PIPELINE", ValidatorPipeline(canonical_loader=CanonicalRecordLoader(root=tmp_path)))
    monkeypatch.setattr(route, "QUEUE_STORE", RuntimeQueueStore())
    monkeypatch.setattr(route, "EVENT_STORE", RuntimeEventStore())
    monkeypatch.setattr(route, "ABUSE_SIGNAL_TRACKER", AdvisoryAbuseSignalTracker())
    with TestClient(create_app()) as client:
        response = client.post(f"/verify/{record_id}", json={"qr_input": f"hc://{record_id}"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["canonical_lookup_status"] == "duplicate_record_id"
    assert payload["schema_valid"] is False
    assert payload["hash_verified"] is False


def test_legacy_archive_id_collision_is_rejected(tmp_path):
    record_id = "HC-DUPLICATE-LEGACY-2026"
    for group in ("pending", "archive"):
        _write_json(tmp_path / "records" / group / "one.json", _record(record_id))
    assert _run(tmp_path, record_id)["canonical_bridge"]["lookup_status"] == "duplicate_record_id"


def test_symlink_to_generated_file_is_not_canonical(tmp_path):
    record_id = "HC-GENERATED-LINK-2026"
    target = tmp_path / "records/pending/generated_index.json"
    _write_json(target, _record(record_id))
    (target.parent / "alias.json").symlink_to(target)
    assert CanonicalRecordLoader(root=tmp_path).get(record_id) is None


def test_artifact_word_in_id_does_not_hide_a_duplicate(tmp_path):
    record_id = "HC-INDEX-2026-0001"
    for group in ("pending", "verified"):
        _write_json(tmp_path / "records" / group / f"{record_id}.json", _record(record_id))
    assert _run(tmp_path, record_id)["canonical_bridge"]["lookup_status"] == "duplicate_record_id"
