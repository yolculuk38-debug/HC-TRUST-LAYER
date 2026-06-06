import importlib.util
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

from hc_runtime.qr_payload_parser import (
    ALLOWED_QR_PAYLOAD_STATUSES,
    RESULT_FIELD_CONTRACT,
    parse_qr_payload,
)

CLI = ROOT / "scripts" / "run_qr_payload_parser.py"

FIXTURE_DIR = ROOT / "docs" / "demo" / "fixtures" / "qr-payload-parser"
EXPECTED_SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}
STABLE_OUTPUT_FIELDS = RESULT_FIELD_CONTRACT

VALID_PAYLOAD = {
    "qr_version": "1",
    "record_id": "HC-EXAMPLE-2026-0001",
    "canonical_url": "https://example.invalid/record/HC-EXAMPLE-2026-0001",
    "payload_hash": "abc",
    "content_hash": "def",
    "issued_at": "2026-01-01T00:00:00Z",
    "issuer_id": "demo",
    "algorithm": "none",
    "key_id": "demo-key",
}


def encode(payload):
    return json.dumps(payload)


def run_cli(raw_payload):
    return subprocess.run(
        [sys.executable, str(CLI), raw_payload],
        check=True,
        capture_output=True,
        text=True,
    )


def load_cli_module():
    spec = importlib.util.spec_from_file_location("run_qr_payload_parser", CLI)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def assert_exact_result_contract(result):
    assert set(result) == set(RESULT_FIELD_CONTRACT)
    assert result["status"] in ALLOWED_QR_PAYLOAD_STATUSES
    assert_safety_markers(result)
    assert_public_safe_list_shape(result)


def test_valid_payload_returns_advisory_valid_payload():
    result = parse_qr_payload(encode(VALID_PAYLOAD))

    assert result["status"] == "valid_payload"
    assert result["warnings"] == []
    assert result["errors"] == []
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True
    assert_exact_result_contract(result)


def test_valid_payload_has_exact_top_level_field_set():
    result = parse_qr_payload(encode(VALID_PAYLOAD))

    assert_exact_result_contract(result)


def test_invalid_payload_has_exact_top_level_field_set():
    payload = dict(VALID_PAYLOAD)
    del payload["payload_hash"]

    result = parse_qr_payload(encode(payload))

    assert result["status"] == "invalid_payload"
    assert_exact_result_contract(result)


def test_malformed_payload_has_exact_top_level_field_set():
    result = parse_qr_payload('{"record_id":')

    assert result["status"] == "malformed_payload"
    assert_exact_result_contract(result)


def test_parser_results_only_use_allowed_statuses():
    malformed = parse_qr_payload('{"record_id":')
    invalid = parse_qr_payload(encode({"record_id": "bad"}))
    valid = parse_qr_payload(encode(VALID_PAYLOAD))

    assert set(ALLOWED_QR_PAYLOAD_STATUSES) == {
        "valid_payload",
        "invalid_payload",
        "malformed_payload",
    }
    assert {valid["status"], invalid["status"], malformed["status"]} == set(
        ALLOWED_QR_PAYLOAD_STATUSES
    )


def test_parser_result_safety_markers_are_fixed_values():
    for raw_payload in [
        encode(VALID_PAYLOAD),
        '{"record_id":',
        encode({"record_id": "bad"}),
    ]:
        result = parse_qr_payload(raw_payload)

        assert {marker: result[marker] for marker in EXPECTED_SAFETY_MARKERS} == (
            EXPECTED_SAFETY_MARKERS
        )


def test_parser_result_warnings_and_errors_are_always_lists():
    for raw_payload in [
        encode(VALID_PAYLOAD),
        '{"record_id":',
        encode({"record_id": "bad"}),
    ]:
        result = parse_qr_payload(raw_payload)

        assert_public_safe_list_shape(result)


def test_missing_field_returns_warning_and_invalid_payload():
    payload = dict(VALID_PAYLOAD)
    del payload["payload_hash"]

    result = parse_qr_payload(encode(payload))

    assert result["status"] == "invalid_payload"
    assert any(
        "Missing required QR payload field(s): payload_hash." == warning
        for warning in result["warnings"]
    )
    assert result["errors"] == ["QR payload is missing required field(s)."]


def test_malformed_json_returns_malformed_payload():
    result = parse_qr_payload('{"record_id":')

    assert result["status"] == "malformed_payload"
    assert result["warnings"] == []
    assert result["errors"]


def test_invalid_record_id_returns_invalid_payload():
    payload = dict(VALID_PAYLOAD, record_id="not-an-hc-record")

    result = parse_qr_payload(encode(payload))

    assert result["status"] == "invalid_payload"
    assert (
        "QR payload record_id does not match HC:// record identifier format."
        in result["errors"]
    )


def test_unknown_field_returns_warning_without_invalidating_payload():
    payload = dict(VALID_PAYLOAD, debug_note="local-only")

    result = parse_qr_payload(encode(payload))

    assert result["status"] == "valid_payload"
    assert result["warnings"] == ["Unknown QR payload field ignored: debug_note."]
    assert result["errors"] == []


def test_safety_markers_always_present():
    for raw_payload in [
        encode(VALID_PAYLOAD),
        '{"record_id":',
        encode({"record_id": "bad"}),
    ]:
        result = parse_qr_payload(raw_payload)

        assert result["advisory_only"] is True
        assert result["public_safe"] is True
        assert result["truth_guarantee"] is False
        assert result["human_review_required"] is True


def test_cli_valid_payload_returns_valid_payload():
    completed = run_cli(encode(VALID_PAYLOAD))
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert result["status"] == "valid_payload"


def test_cli_malformed_json_returns_malformed_payload():
    completed = run_cli('{"record_id":')
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert result["status"] == "malformed_payload"


def test_cli_missing_field_returns_invalid_payload():
    payload = dict(VALID_PAYLOAD)
    del payload["payload_hash"]

    completed = run_cli(encode(payload))
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert result["status"] == "invalid_payload"


def test_cli_output_is_valid_json():
    completed = run_cli(encode(VALID_PAYLOAD))

    result = json.loads(completed.stdout)

    assert isinstance(result, dict)
    assert result["status"] == "valid_payload"


def test_cli_output_preserves_safety_markers():
    completed = run_cli(encode(VALID_PAYLOAD))
    result = json.loads(completed.stdout)

    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True


def test_cli_output_preserves_exact_field_set():
    for raw_payload in [
        encode(VALID_PAYLOAD),
        '{"record_id":',
        encode({"record_id": "bad"}),
    ]:
        completed = run_cli(raw_payload)
        result = json.loads(completed.stdout)

        assert completed.stderr == ""
        assert_exact_result_contract(result)


def test_cli_does_not_fetch_urls_or_call_network(monkeypatch, capsys):
    def fail_network(*args, **kwargs):
        raise AssertionError("QR payload parser CLI must remain local-only")

    monkeypatch.setattr(socket, "create_connection", fail_network)
    monkeypatch.setattr(urllib.request, "urlopen", fail_network)

    module = load_cli_module()

    assert module.main([encode(VALID_PAYLOAD)]) == 0
    result = json.loads(capsys.readouterr().out)

    assert result["status"] == "valid_payload"


def test_cli_does_not_claim_qr_authenticity_or_signature_verification():
    completed = run_cli(encode(VALID_PAYLOAD))
    result = json.loads(completed.stdout)
    output = json.dumps(result, sort_keys=True).lower()

    assert "authentic" not in output
    assert "signature" not in output
    assert "verified" not in output
    assert "signature_verified" not in result
    assert "qr_authenticity_proven" not in result


def load_fixture(name):
    return (FIXTURE_DIR / name).read_text()


def cli_fixture_result(name):
    completed = run_cli(load_fixture(name))
    assert completed.stderr == ""
    return json.loads(completed.stdout)


def stable_output(result):
    return {field: result[field] for field in STABLE_OUTPUT_FIELDS}


def assert_safety_markers(result):
    for marker, expected in EXPECTED_SAFETY_MARKERS.items():
        assert result[marker] is expected


def assert_public_safe_list_shape(result):
    assert isinstance(result["warnings"], list)
    assert isinstance(result["errors"], list)
    assert all(isinstance(warning, str) for warning in result["warnings"])
    assert all(isinstance(error, str) for error in result["errors"])


def test_cli_valid_fixture_matches_stable_golden_output_shape():
    result = cli_fixture_result("valid-payload.json")

    assert stable_output(result) == {
        "status": "valid_payload",
        **EXPECTED_SAFETY_MARKERS,
        "warnings": [],
        "errors": [],
    }
    assert_public_safe_list_shape(result)


def test_cli_missing_field_fixture_matches_stable_golden_output_shape():
    result = cli_fixture_result("missing-field-payload.json")

    assert result["status"] == "invalid_payload"
    assert_safety_markers(result)
    assert_public_safe_list_shape(result)
    assert any(
        "Missing required QR payload field" in warning
        for warning in result["warnings"]
    )
    assert any("key_id" in warning for warning in result["warnings"])
    assert any("missing required field" in error for error in result["errors"])


def test_cli_unknown_field_fixture_matches_stable_golden_output_shape():
    result = cli_fixture_result("unknown-field-payload.json")

    assert result["status"] == "valid_payload"
    assert_safety_markers(result)
    assert_public_safe_list_shape(result)
    assert any(
        "Unknown QR payload field ignored" in warning
        for warning in result["warnings"]
    )
    assert any("review_note" in warning for warning in result["warnings"])
    assert result["errors"] == []


def test_cli_malformed_fixture_matches_stable_golden_output_shape():
    result = cli_fixture_result("malformed-payload.txt")

    assert result["status"] == "malformed_payload"
    assert_safety_markers(result)
    assert_public_safe_list_shape(result)
    assert result["warnings"] == []
    assert result["errors"]
    assert any("malformed JSON" in error for error in result["errors"])

