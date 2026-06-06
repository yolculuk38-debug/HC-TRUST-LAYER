import hashlib
import json
import socket
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hc_runtime.qr_public_validator import (  # noqa: E402
    ALLOWED_QR_PUBLIC_VALIDATOR_STATUSES,
    RESULT_FIELD_CONTRACT,
    run_qr_public_validator,
)

EXPECTED_SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}


def content_hash(content):
    if isinstance(content, str):
        content_bytes = content.encode("utf-8")
    else:
        content_bytes = json.dumps(content, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(content_bytes).hexdigest()


def advisory_payload_hash(payload):
    canonical_payload = dict(payload)
    canonical_payload.pop("payload_hash", None)
    return hashlib.sha256(
        json.dumps(canonical_payload, sort_keys=True, separators=(",", ":")).encode(
            "utf-8"
        )
    ).hexdigest()


def qr_payload(record_id, declared_content_hash):
    payload = {
        "qr_version": "1",
        "record_id": record_id,
        "canonical_url": f"https://example.invalid/record/{record_id}",
        "payload_hash": "pending",
        "content_hash": declared_content_hash,
        "issued_at": "2026-01-01T00:00:00Z",
        "issuer_id": "demo",
        "algorithm": "none",
        "key_id": "demo-key",
    }
    payload["payload_hash"] = advisory_payload_hash(payload)
    return payload


def write_record(path, record_id, content="Local advisory combined validator content"):
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "archive_ref": "pending_archive",
        "author": "Human reviewer",
        "content": content,
        "content_hash": content_hash(content),
        "created_at": "2026-01-01T00:00:00Z",
        "hash": "",
        "id": record_id,
        "prev_hash": "",
        "record_id": record_id,
        "record_type": "ai_witness",
        "source": "HC-TRUST-LAYER test",
        "status": "pending",
        "timestamp": "2026-01-01T00:00:00Z",
        "title": "Local advisory combined validator test record",
        "verification_status": "draft",
        "witness_type": "ai",
        "witnesses": ["Human reviewer"],
    }
    path.write_text(json.dumps(record, indent=2), encoding="utf-8")
    return record


def assert_result_shape(result):
    assert tuple(result) == RESULT_FIELD_CONTRACT
    assert set(result) == set(RESULT_FIELD_CONTRACT)
    assert result["status"] in ALLOWED_QR_PUBLIC_VALIDATOR_STATUSES
    assert result["warnings"] and isinstance(result["warnings"], list)
    assert isinstance(result["errors"], list)
    for marker, expected in EXPECTED_SAFETY_MARKERS.items():
        assert result[marker] is expected


def test_combined_valid_payload_and_matching_local_record_returns_validated(tmp_path):
    record_id = "HC-QRPUBLIC-2026-0001"
    record = write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)
    payload = qr_payload(record_id, record["content_hash"].upper())

    result = run_qr_public_validator(json.dumps(payload), repo_root=tmp_path)

    assert_result_shape(result)
    assert result["status"] == "qr_record_validated"
    assert result["qr_payload_status"] == "valid_payload"
    assert result["bridge_status"] == "bridge_match"
    assert result["record_lookup_status"] == "found"
    assert result["content_hash_match"] is True
    assert result["local_validator"] is not None
    assert result["local_validator"]["status"] == "found"
    assert result["local_validator"]["source_path"] == f"records/pending/{record_id}.json"


def test_combined_payload_content_hash_mismatch_returns_mismatch(tmp_path):
    record_id = "HC-QRPUBLIC-2026-0002"
    write_record(tmp_path / "records" / "verified" / f"{record_id}.json", record_id)
    payload = qr_payload(record_id, "0" * 64)

    result = run_qr_public_validator(payload, repo_root=tmp_path)

    assert_result_shape(result)
    assert result["status"] == "qr_record_mismatch"
    assert result["bridge_status"] == "bridge_mismatch"
    assert result["record_lookup_status"] == "found"
    assert result["content_hash_match"] is False
    assert result["local_validator"] is not None
    assert result["local_validator"]["status"] == "found"


def test_record_not_found_omits_local_validator(tmp_path):
    payload = qr_payload("HC-QRPUBLIC-NOTFOUND-2026-0001", "1" * 64)

    result = run_qr_public_validator(json.dumps(payload), repo_root=tmp_path)

    assert_result_shape(result)
    assert result["status"] == "record_not_found"
    assert result["record_lookup_status"] == "not_found"
    assert result["content_hash_match"] is None
    assert result["local_validator"] is None


def test_malformed_payload_omits_local_validator(tmp_path):
    result = run_qr_public_validator('{"record_id":', repo_root=tmp_path)

    assert_result_shape(result)
    assert result["status"] == "malformed_payload"
    assert result["qr_payload_status"] == "malformed_payload"
    assert result["bridge_status"] == "malformed_payload"
    assert result["record_lookup_status"] == "not_checked"
    assert result["local_validator"] is None


def test_invalid_payload_omits_local_validator(tmp_path):
    payload = qr_payload("not-an-hc-record", "1" * 64)

    result = run_qr_public_validator(json.dumps(payload), repo_root=tmp_path)

    assert_result_shape(result)
    assert result["status"] == "invalid_payload"
    assert result["qr_payload_status"] == "invalid_payload"
    assert result["bridge_status"] == "invalid_payload"
    assert result["record_lookup_status"] == "not_checked"
    assert result["local_validator"] is None


def test_duplicate_record_id_omits_local_validator(tmp_path):
    record_id = "HC-QRPUBLIC-DUP-2026-0001"
    first = write_record(tmp_path / "records" / "pending" / "one.json", record_id, "one")
    write_record(tmp_path / "records" / "archived" / "two.json", record_id, "two")
    payload = qr_payload(record_id, first["content_hash"])

    result = run_qr_public_validator(payload, repo_root=tmp_path)

    assert_result_shape(result)
    assert result["status"] == "duplicate_record_id"
    assert result["record_lookup_status"] == "duplicate_record_id"
    assert result["content_hash_match"] is None
    assert result["local_validator"] is None


def test_safety_markers_always_present(tmp_path):
    record_id = "HC-QRPUBLIC-SAFE-2026-0001"
    record = write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)
    cases = [
        json.dumps(qr_payload(record_id, record["content_hash"])),
        json.dumps(qr_payload(record_id, "0" * 64)),
        json.dumps(qr_payload("HC-QRPUBLIC-NOTFOUND-2026-0002", "1" * 64)),
        json.dumps(qr_payload("not-an-hc-record", "1" * 64)),
        '{"record_id":',
    ]

    for raw_payload in cases:
        result = run_qr_public_validator(raw_payload, repo_root=tmp_path)
        assert_result_shape(result)
        assert {marker: result[marker] for marker in EXPECTED_SAFETY_MARKERS} == (
            EXPECTED_SAFETY_MARKERS
        )


def test_no_network_calls_or_canonical_url_fetch(monkeypatch, tmp_path):
    def fail_network(*args, **kwargs):
        raise AssertionError("QR Public Validator must remain local-only")

    monkeypatch.setattr(socket, "create_connection", fail_network)
    monkeypatch.setattr(urllib.request, "urlopen", fail_network)
    record_id = "HC-QRPUBLIC-NONETWORK-2026-0001"
    record = write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)
    payload = qr_payload(record_id, record["content_hash"])
    payload["canonical_url"] = "https://example.invalid/must-not-fetch"
    payload["payload_hash"] = advisory_payload_hash(payload)

    result = run_qr_public_validator(json.dumps(payload), repo_root=tmp_path)

    assert_result_shape(result)
    assert result["status"] == "qr_record_validated"
    assert result["content_hash_match"] is True


def test_demo_fixtures_are_not_treated_as_canonical_records(tmp_path):
    record_id = "HC-QRPUBLIC-DEMO-2026-0001"
    record = write_record(
        tmp_path
        / "docs"
        / "demo"
        / "fixtures"
        / "qr-payload-parser"
        / f"{record_id}.json",
        record_id,
    )
    payload = qr_payload(record_id, record["content_hash"])

    result = run_qr_public_validator(payload, repo_root=tmp_path)

    assert_result_shape(result)
    assert result["status"] == "record_not_found"
    assert result["record_lookup_status"] == "not_found"
    assert result["local_validator"] is None


def test_stable_result_shape(tmp_path):
    result = run_qr_public_validator('{"record_id":', repo_root=tmp_path)

    assert tuple(result) == RESULT_FIELD_CONTRACT
    assert set(result) == {
        "status",
        "qr_payload_status",
        "bridge_status",
        "record_lookup_status",
        "content_hash_match",
        "local_validator",
        "warnings",
        "errors",
        "advisory_only",
        "public_safe",
        "truth_guarantee",
        "human_review_required",
    }
