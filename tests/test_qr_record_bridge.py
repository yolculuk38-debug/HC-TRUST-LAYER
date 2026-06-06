import contextlib
import hashlib
import importlib.util
import io
import json
import socket
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hc_runtime.qr_record_bridge import (  # noqa: E402
    ALLOWED_BRIDGE_STATUSES,
    RESULT_FIELD_CONTRACT,
    check_qr_payload_record_bridge,
)

CLI = ROOT / "scripts" / "run_qr_record_bridge.py"

EXPECTED_SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}


def run_cli(raw_payload):
    return subprocess.run(
        [sys.executable, str(CLI), raw_payload],
        check=True,
        capture_output=True,
        text=True,
    )


def load_cli_module():
    spec = importlib.util.spec_from_file_location("run_qr_record_bridge", CLI)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def run_cli_main(raw_payload):
    module = load_cli_module()
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        exit_code = module.main([raw_payload])
    return exit_code, stdout.getvalue()


def run_cli_main_with_repo_root(monkeypatch, repo_root, raw_payload):
    module = load_cli_module()
    seen = []

    def bridge_with_repo_root(payload):
        seen.append(payload)
        return check_qr_payload_record_bridge(payload, repo_root=repo_root)

    monkeypatch.setattr(module, "check_qr_payload_record_bridge", bridge_with_repo_root)
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        exit_code = module.main([raw_payload])
    return exit_code, stdout.getvalue(), seen


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


def write_record(path, record_id, content="Local advisory bridge content"):
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
        "title": "Local advisory bridge test record",
        "verification_status": "draft",
        "witness_type": "ai",
        "witnesses": ["Human reviewer"],
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def assert_bridge_shape(result):
    assert tuple(result) == RESULT_FIELD_CONTRACT
    assert_bridge_values(result)


def assert_bridge_values(result):
    assert set(result) == set(RESULT_FIELD_CONTRACT)
    assert result["bridge_status"] in ALLOWED_BRIDGE_STATUSES
    for marker, expected in EXPECTED_SAFETY_MARKERS.items():
        assert result[marker] is expected
    assert isinstance(result["warnings"], list)
    assert isinstance(result["errors"], list)
    assert all(isinstance(warning, str) for warning in result["warnings"])
    assert all(isinstance(error, str) for error in result["errors"])


def test_qr_payload_content_hash_matches_local_record(tmp_path):
    record_id = "HC-BRIDGE-2026-0001"
    record = write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)
    payload = bridge_payload(record_id, record["content_hash"].upper())

    result = check_qr_payload_record_bridge(json.dumps(payload), repo_root=tmp_path)

    assert_bridge_shape(result)
    assert result["qr_payload_status"] == "valid_payload"
    assert result["record_lookup_status"] == "found"
    assert result["content_hash_match"] is True
    assert result["bridge_status"] == "bridge_match"
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False


def test_qr_payload_content_hash_mismatches_local_record(tmp_path):
    record_id = "HC-BRIDGE-2026-0002"
    write_record(tmp_path / "records" / "verified" / f"{record_id}.json", record_id)
    payload = bridge_payload(record_id, "0" * 64)

    result = check_qr_payload_record_bridge(payload, repo_root=tmp_path)

    assert_bridge_shape(result)
    assert result["record_lookup_status"] == "found"
    assert result["content_hash_match"] is False
    assert result["bridge_status"] == "bridge_mismatch"
    assert result["errors"] == [
        "QR payload content_hash mismatch against matched local canonical record."
    ]


def test_record_id_not_found_reports_record_not_found(tmp_path):
    payload = bridge_payload("HC-NOTFOUND-2026-0001", "1" * 64)

    result = check_qr_payload_record_bridge(json.dumps(payload), repo_root=tmp_path)

    assert_bridge_shape(result)
    assert result["record_lookup_status"] == "not_found"
    assert result["content_hash_match"] is None
    assert result["bridge_status"] == "record_not_found"


def test_malformed_payload_does_not_lookup(monkeypatch, tmp_path):
    def fail_lookup(*args, **kwargs):
        raise AssertionError("Malformed QR payload must not trigger record lookup")

    monkeypatch.setattr("hc_runtime.qr_record_bridge.lookup_public_validator_record", fail_lookup)

    result = check_qr_payload_record_bridge('{"record_id":', repo_root=tmp_path)

    assert_bridge_shape(result)
    assert result["qr_payload_status"] == "malformed_payload"
    assert result["record_lookup_status"] == "not_checked"
    assert result["bridge_status"] == "malformed_payload"
    assert result["content_hash_match"] is None


def test_invalid_record_id_does_not_lookup(monkeypatch, tmp_path):
    def fail_lookup(*args, **kwargs):
        raise AssertionError("Invalid QR record_id must not trigger record lookup")

    monkeypatch.setattr("hc_runtime.qr_record_bridge.lookup_public_validator_record", fail_lookup)
    payload = bridge_payload("not-an-hc-record", "1" * 64)

    result = check_qr_payload_record_bridge(json.dumps(payload), repo_root=tmp_path)

    assert_bridge_shape(result)
    assert result["qr_payload_status"] == "invalid_payload"
    assert result["record_lookup_status"] == "not_checked"
    assert result["bridge_status"] == "invalid_payload"
    assert result["content_hash_match"] is None


def test_duplicate_record_id_handling(tmp_path):
    record_id = "HC-DUPBRIDGE-2026-0001"
    first = write_record(tmp_path / "records" / "pending" / "one.json", record_id, "one")
    write_record(tmp_path / "records" / "archived" / "two.json", record_id, "two")
    payload = bridge_payload(record_id, first["content_hash"])

    result = check_qr_payload_record_bridge(payload, repo_root=tmp_path)

    assert_bridge_shape(result)
    assert result["record_lookup_status"] == "duplicate_record_id"
    assert result["content_hash_match"] is None
    assert result["bridge_status"] == "duplicate_record_id"
    assert result["errors"] == [
        "QR payload record bridge requires exactly one local canonical record match."
    ]


def test_safety_markers_always_present(tmp_path):
    cases = [
        '{"record_id":',
        json.dumps(bridge_payload("HC-NOTFOUND-2026-0002", "1" * 64)),
        json.dumps(bridge_payload("not-an-hc-record", "1" * 64)),
    ]

    for raw_payload in cases:
        result = check_qr_payload_record_bridge(raw_payload, repo_root=tmp_path)
        assert_bridge_shape(result)
        assert {marker: result[marker] for marker in EXPECTED_SAFETY_MARKERS} == (
            EXPECTED_SAFETY_MARKERS
        )


def test_no_network_calls(monkeypatch, tmp_path):
    def fail_network(*args, **kwargs):
        raise AssertionError("QR record bridge must remain local-only")

    monkeypatch.setattr(socket, "create_connection", fail_network)
    monkeypatch.setattr(urllib.request, "urlopen", fail_network)
    record_id = "HC-NONETWORK-2026-0001"
    record = write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)
    payload = bridge_payload(record_id, record["content_hash"])

    result = check_qr_payload_record_bridge(payload, repo_root=tmp_path)

    assert_bridge_shape(result)
    assert result["bridge_status"] == "bridge_match"


def test_local_lookup_allowlist_preserved_and_demo_fixtures_not_canonical(tmp_path):
    record_id = "HC-DEMO-BRIDGE-2026-0001"
    record = write_record(
        tmp_path
        / "docs"
        / "demo"
        / "fixtures"
        / "qr-payload-parser"
        / f"{record_id}.json",
        record_id,
    )
    payload = bridge_payload(record_id, record["content_hash"])

    result = check_qr_payload_record_bridge(payload, repo_root=tmp_path)

    assert_bridge_shape(result)
    assert result["record_lookup_status"] == "not_found"
    assert result["bridge_status"] == "record_not_found"
    assert result["content_hash_match"] is None


def test_result_shape_stable(tmp_path):
    result = check_qr_payload_record_bridge('{"record_id":', repo_root=tmp_path)

    assert tuple(result) == RESULT_FIELD_CONTRACT
    assert set(result) == {
        "qr_payload_status",
        "record_lookup_status",
        "content_hash_match",
        "bridge_status",
        "warnings",
        "errors",
        "advisory_only",
        "public_safe",
        "truth_guarantee",
        "human_review_required",
    }


def test_cli_bridge_match_outputs_valid_json_and_safety_markers(monkeypatch, tmp_path):
    record_id = "HC-CLI-BRIDGE-2026-0001"
    record = write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)
    raw_payload = json.dumps(bridge_payload(record_id, record["content_hash"]))

    exit_code, stdout, seen = run_cli_main_with_repo_root(monkeypatch, tmp_path, raw_payload)
    result = json.loads(stdout)

    assert exit_code == 0
    assert seen == [raw_payload]
    assert stdout.strip().startswith("{")
    assert "\n" in stdout
    assert_bridge_values(result)
    assert result["bridge_status"] == "bridge_match"
    assert result["content_hash_match"] is True
    assert {marker: result[marker] for marker in EXPECTED_SAFETY_MARKERS} == (
        EXPECTED_SAFETY_MARKERS
    )


def test_cli_bridge_mismatch_case_outputs_valid_json(monkeypatch, tmp_path):
    record_id = "HC-CLI-BRIDGE-2026-0002"
    write_record(tmp_path / "records" / "verified" / f"{record_id}.json", record_id)
    raw_payload = json.dumps(bridge_payload(record_id, "0" * 64))

    exit_code, stdout, _seen = run_cli_main_with_repo_root(monkeypatch, tmp_path, raw_payload)
    result = json.loads(stdout)

    assert exit_code == 0
    assert_bridge_values(result)
    assert result["bridge_status"] == "bridge_mismatch"
    assert result["content_hash_match"] is False
    assert result["errors"] == [
        "QR payload content_hash mismatch against matched local canonical record."
    ]
    assert {marker: result[marker] for marker in EXPECTED_SAFETY_MARKERS} == (
        EXPECTED_SAFETY_MARKERS
    )


def test_cli_record_not_found_case_outputs_valid_json():
    payload = bridge_payload("HC-CLI-NOTFOUND-2026-0001", "1" * 64)

    completed = run_cli(json.dumps(payload))
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert_bridge_values(result)
    assert result["bridge_status"] == "record_not_found"
    assert result["record_lookup_status"] == "not_found"


def test_cli_malformed_payload_case_outputs_valid_json():
    completed = run_cli('{"record_id":')
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert_bridge_values(result)
    assert result["bridge_status"] == "malformed_payload"
    assert result["qr_payload_status"] == "malformed_payload"


def test_cli_output_uses_sorted_json_keys_for_determinism():
    completed = run_cli('{"record_id":')
    result = json.loads(completed.stdout)

    assert list(result) == sorted(result)
    assert completed.stdout.splitlines()[1].startswith('  "advisory_only"')


def test_cli_does_not_call_network_or_fetch_canonical_url(monkeypatch):
    def fail_network(*args, **kwargs):
        raise AssertionError("QR record bridge CLI must remain local-only")

    monkeypatch.setattr(socket, "create_connection", fail_network)
    monkeypatch.setattr(urllib.request, "urlopen", fail_network)
    payload = bridge_payload("HC-CLI-NONETWORK-2026-0001", "2" * 64)

    exit_code, stdout = run_cli_main(json.dumps(payload))
    result = json.loads(stdout)

    assert exit_code == 0
    assert_bridge_values(result)
    assert result["bridge_status"] == "record_not_found"


def test_cli_output_does_not_claim_qr_authenticity_signature_or_truth():
    completed = run_cli('{"record_id":')
    result = json.loads(completed.stdout)
    serialized = json.dumps(result, sort_keys=True).lower()

    assert result["truth_guarantee"] is False
    assert "authenticity_verified" not in serialized
    assert "qr_authentic" not in serialized
    assert "signature_verified" not in serialized
    assert "truth_verified" not in serialized
    assert '"verified": true' not in serialized
