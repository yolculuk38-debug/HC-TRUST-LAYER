"""Canonical record loader coverage for HC:// advisory runtime behavior."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from hc_runtime.canonical_record_loader import CanonicalRecordLoader
from hc_runtime.runtime import ValidatorPipeline


def _sha256(content: object) -> str:
    if isinstance(content, str):
        payload = content
    else:
        payload = json.dumps(content, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")


def _record(record_id: str, content: object = "canonical loader content") -> dict[str, object]:
    return {"record_id": record_id, "content": content, "content_hash": _sha256(content)}


def _run(root: Path, record_id: str) -> dict[str, Any]:
    return ValidatorPipeline(canonical_loader=CanonicalRecordLoader(root=root)).run(
        record_id=record_id,
        qr_input=f"hc://{record_id} hash:advisory",
    )


def test_valid_canonical_record_loads_from_approved_directory_with_verified_status(tmp_path: Path) -> None:
    record_id = "HC-LOADER-VALID"
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


def test_content_hash_mismatch_returns_explicit_hash_mismatch_status(tmp_path: Path) -> None:
    record_id = "HC-LOADER-HASH-MISMATCH"
    _write_json(
        tmp_path / "records" / "archived" / f"{record_id}.json",
        {"record_id": record_id, "content": "canonical content", "content_hash": _sha256("different content")},
    )

    result = _run(tmp_path, record_id)

    assert result["canonical_bridge"]["lookup_status"] == "hash_mismatch"
    assert result["canonical_bridge"]["schema_valid"] is True
    assert result["hash_result"]["hash_verified"] is False
    assert any("content_hash mismatch" in warning.lower() for warning in result["trust_assignment"]["warnings"])
