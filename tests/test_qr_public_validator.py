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
    ALLOWED_COMBINED_STATUSES,
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


def bridge_payload(record_id, declared_content_hash):
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


def write_record(path, record_id, content="Combined local validator content"):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
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
        "title": "Combined local validator test record",
        "verification_status": "draft",
        "witness_type": "ai",
        "witnesses": ["Human reviewer"],
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def assert_combined_shape(result):
    assert tuple(result) == RESULT_FIELD_CONTRACT
    assert set(result) == set(RESULT_FIELD_CONTRACT)
    assert result["status"] in ALLOWED_COMBINED_STATUSES
    assert isinstance(result["warnings"], list)
    assert isinstance(result["errors"], list)
    assert all(isinstance(warning, str) for warning in result["warnings"])
    assert all(isinstance(error, str) for error in result["errors"])
    for marker, expected in EXPECTED_SAFETY_MARKERS.items():
        assert result[marker] is expected


def test_combined_valid_qr_payload_matching_local_record(tmp_path):
    record_id = "HC-COMBINED-2026-0001"
    record = write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)
    payload = bridge_payload(record_id, record["content_hash"])

    result = run_qr_public_validator(json.dumps(payload), repo_root=tmp_path)

    assert_combined_shape(result)
    assert result["status"] == "qr_record_validated"
    assert result["qr_payload_status"] == "valid_payload"
    assert result["bridge_status"] == "bridge_match"
    assert result["record_lookup_status"] == "found"
    assert result["content_hash_match"] is True
    assert isinstance(result["local_validator"], dict)
    assert result["local_validator"]["status"] == "found"
    assert result["local_validator"]["record_id"] == record_id


def test_combined_payload_content_hash_mismatch(tmp_path):
    record_id = "HC-COMBINED-2026-0002"
    write_record(tmp_path / "records" / "verified" / f"{record_id}.json", record_id)
    payload = bridge_payload(record_id, "0" * 64)

    result = run_qr_public_validator(payload, repo_root=tmp_path)

    assert_combined_shape(result)
    assert result["status"] == "qr_record_mismatch"
    assert result["bridge_status"] == "bridge_mismatch"
    assert result["record_lookup_status"] == "found"
    assert result["content_hash_match"] is False
    assert isinstance(result["local_validator"], dict)
    assert result["local_validator"]["status"] == "found"


def test_combined_record_not_found_does_not_embed_local_validator(tmp_path):
    payload = bridge_payload("HC-COMBINED-NOTFOUND-2026-0001", "1" * 64)

    result = run_qr_public_validator(json.dumps(payload), repo_root=tmp_path)

    assert_combined_shape(result)
    assert result["status"] == "record_not_found"
    assert result["bridge_status"] == "record_not_found"
    assert result["record_lookup_status"] == "not_found"
    assert result["local_validator"] is None


def test_combined_malformed_payload_does_not_embed_local_validator(tmp_path):
    result = run_qr_public_validator('{"record_id":', repo_root=tmp_path)

    assert_combined_shape(result)
    assert result["status"] == "malformed_payload"
    assert result["qr_payload_status"] == "malformed_payload"
    assert result["local_validator"] is None


def test_combined_invalid_payload_does_not_embed_local_validator(tmp_path):
    payload = bridge_payload("not-an-hc-record", "1" * 64)

    result = run_qr_public_validator(json.dumps(payload), repo_root=tmp_path)

    assert_combined_shape(result)
    assert result["status"] == "invalid_payload"
    assert result["qr_payload_status"] == "invalid_payload"
    assert result["local_validator"] is None


def test_combined_duplicate_record_id(tmp_path):
    record_id = "HC-COMBINED-DUP-2026-0001"
    first = write_record(tmp_path / "records" / "pending" / "one.json", record_id, "one")
    write_record(tmp_path / "records" / "archived" / "two.json", record_id, "two")
    payload = bridge_payload(record_id, first["content_hash"])

    result = run_qr_public_validator(payload, repo_root=tmp_path)

    assert_combined_shape(result)
    assert result["status"] == "duplicate_record_id"
    assert result["bridge_status"] == "duplicate_record_id"
    assert result["record_lookup_status"] == "duplicate_record_id"
    assert result["local_validator"] is None


def test_combined_no_network_calls(monkeypatch, tmp_path):
    def fail_network(*args, **kwargs):
        raise AssertionError("Combined QR Public Validator must remain local-only")

    monkeypatch.setattr(socket, "create_connection", fail_network)
    monkeypatch.setattr(urllib.request, "urlopen", fail_network)

    record_id = "HC-COMBINED-NONETWORK-2026-0001"
    record = write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)
    payload = bridge_payload(record_id, record["content_hash"])

    result = run_qr_public_validator(payload, repo_root=tmp_path)

    assert_combined_shape(result)
    assert result["status"] == "qr_record_validated"


def test_combined_output_does_not_claim_qr_authenticity_signature_or_truth(tmp_path):
    result = run_qr_public_validator('{"record_id":', repo_root=tmp_path)
    serialized = json.dumps(result, sort_keys=True).lower()

    assert_combined_shape(result)
    assert result["truth_guarantee"] is False
    assert "authenticity_verified" not in serialized
    assert "qr_authentic" not in serialized
    assert "signature_verified" not in serialized
    assert "truth_verified" not in serialized
    assert '"verified": true' not in serialized
