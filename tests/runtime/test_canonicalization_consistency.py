"""Cross-surface P0-2 canonicalization and fail-closed regressions."""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

import hc_runtime.routes.verify as verify_route
from hc_runtime.app import create_app
from hc_runtime.canonical_record_loader import MALFORMED_RECORD, CanonicalRecordLoader
from hc_runtime.public_validator_lookup import lookup_public_validator_record
from hc_runtime.runtime import ValidatorPipeline
from hc_trust.hashing import HC_CONTENT_HASH_PROFILE, calculate_content_hash
from hc_trust.verification import verify_record_hash


def _write_record(root: Path, record_id: str, record_text: str) -> Path:
    path = root / "records" / "pending" / f"{record_id}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(record_text, encoding="utf-8")
    return path


def test_structured_v2_hash_is_identical_across_core_loader_and_runtime(tmp_path: Path) -> None:
    content = {"z": [{"b": 2, "a": "\u00e9"}], "a": 1.0}
    record_id = "HC-JCS-2026-0001"
    record = {
        "schema_version": "hc-record-v1",
        "record_id": record_id,
        "created_at": "2026-08-08T12:00:00Z",
        "title": "Canonicalization consistency record",
        "record_type": "protocol_note",
        "witness_type": "human",
        "author": "HC-TRUST-LAYER tests",
        "content": content,
        "content_hash": calculate_content_hash(content, HC_CONTENT_HASH_PROFILE),
        "content_hash_profile": HC_CONTENT_HASH_PROFILE,
        "archive_ref": "pending_archive",
        "verification_status": "draft",
    }
    path = _write_record(tmp_path, record_id, json.dumps(record, ensure_ascii=False))

    passed, message = verify_record_hash(path)
    pipeline_result = ValidatorPipeline(
        canonical_loader=CanonicalRecordLoader(root=tmp_path)
    ).run(record_id=record_id, qr_input=f"hc://{record_id}")

    assert passed, message
    assert pipeline_result["canonical_bridge"]["hash_verified"] is True
    assert pipeline_result["canonical_bridge"]["lookup_status"] == "verified"
    assert pipeline_result["hash_result"]["checked"] is True


def test_algorithm_absent_structured_record_is_hash_unverifiable() -> None:
    content = {"evidence": "present"}
    record = {
        "record_id": "ambiguous-record",
        "content": content,
        "content_hash": calculate_content_hash(content, HC_CONTENT_HASH_PROFILE),
    }

    result = ValidatorPipeline(canonical_records={"ambiguous-record": record}).run(
        record_id="ambiguous-record", qr_input="hc://ambiguous-record"
    )

    assert result["canonical_bridge"]["lookup_status"] == "hash_unverifiable"
    assert result["canonical_bridge"]["hash_verified"] is False
    assert result["hash_result"]["checked"] is False
    assert any(
        "legacy_structured_content_algorithm_ambiguous" in warning
        for warning in result["canonical_bridge"]["warnings"]
    )


def test_unknown_profile_is_hash_unverifiable_without_exception() -> None:
    record = {
        "record_id": "unknown-profile",
        "content": "content",
        "content_hash": "0" * 64,
        "content_hash_profile": "sha256",
    }

    result = ValidatorPipeline(canonical_records={"unknown-profile": record}).run(
        record_id="unknown-profile", qr_input="hc://unknown-profile"
    )

    assert result["canonical_bridge"]["lookup_status"] == "hash_unverifiable"
    assert result["hash_result"]["checked"] is False
    assert any("unknown_content_hash_profile" in warning for warning in result["canonical_bridge"]["warnings"])


def test_explicit_null_profile_is_unknown_across_core_and_runtime(tmp_path: Path) -> None:
    record_id = "null-profile"
    content = "legacy-compatible text"
    record = {
        "record_id": record_id,
        "content": content,
        "content_hash": calculate_content_hash(content),
        "content_hash_profile": None,
    }
    path = _write_record(tmp_path, record_id, json.dumps(record))

    passed, message = verify_record_hash(path)
    runtime_result = ValidatorPipeline(canonical_records={record_id: record}).run(
        record_id=record_id,
        qr_input=f"hc://{record_id}",
    )

    assert passed is False
    assert "unknown_content_hash_profile" in message
    assert runtime_result["canonical_bridge"]["lookup_status"] == "hash_unverifiable"
    assert runtime_result["hash_result"]["checked"] is False
    assert runtime_result["hash_result"]["hash_verified"] is False
    assert any(
        "unknown_content_hash_profile" in warning
        for warning in runtime_result["canonical_bridge"]["warnings"]
    )


@pytest.mark.anyio
async def test_public_runtime_keeps_unverifiable_structured_hash_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    content = {"evidence": "present"}
    record_id = "ambiguous-public-record"
    record = {
        "record_id": record_id,
        "content": content,
        "content_hash": calculate_content_hash(content, HC_CONTENT_HASH_PROFILE),
    }
    monkeypatch.setattr(
        verify_route,
        "PIPELINE",
        ValidatorPipeline(canonical_records={record_id: record}),
    )

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.post(
            f"/verify/{record_id}", json={"qr_input": f"hc://{record_id}"}
        )

    assert response.status_code == 200
    payload = response.json()
    assert payload["canonical_lookup_status"] == "hash_unverifiable"
    assert payload["hash_verified"] is False
    assert payload["trust_state"] != "ADVISORY"
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False


def test_duplicate_key_record_is_malformed_in_loader_and_public_lookup(tmp_path: Path) -> None:
    record_id = "duplicate-record"
    _write_record(
        tmp_path,
        record_id,
        '{"record_id":"duplicate-record","record_id":"other","content":"x","content_hash":"0"}',
    )

    loader = CanonicalRecordLoader(root=tmp_path)
    lookup = lookup_public_validator_record(record_id, root=tmp_path)

    assert loader.get(record_id) is MALFORMED_RECORD
    assert lookup["status"] == "lookup_error"
    assert lookup["found"] is False
    assert lookup["public_safe"] is True
    assert lookup["truth_guarantee"] is False
    assert any("duplicate" in error.lower() for error in lookup["errors"])
