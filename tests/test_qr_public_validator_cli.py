import hashlib
import json
import socket
import urllib.request
from pathlib import Path

from hc_runtime import qr_public_validator
from hc_trust.cli import main

ROOT = Path(__file__).resolve().parents[1]
MATCHING_PAYLOAD_PATH = (
    ROOT
    / "docs"
    / "demo"
    / "fixtures"
    / "qr-payload-parser"
    / "record-match-payload.json"
)

EXPECTED_SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}


def _load_matching_payload() -> dict[str, str]:
    return json.loads(MATCHING_PAYLOAD_PATH.read_text(encoding="utf-8"))


def _refresh_payload_hash(payload: dict[str, str]) -> None:
    canonical_payload = dict(payload)
    canonical_payload.pop("payload_hash", None)
    payload["payload_hash"] = hashlib.sha256(
        json.dumps(
            canonical_payload,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _run_cli(payload: str | dict[str, str], capsys) -> tuple[int, dict]:
    payload_json = payload if isinstance(payload, str) else json.dumps(payload)
    exit_code = main(["qr-public-validator", payload_json])
    captured = capsys.readouterr()
    result = json.loads(captured.out)

    assert captured.err == ""
    assert (
        captured.out
        == json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    )
    for marker, expected in EXPECTED_SAFETY_MARKERS.items():
        assert result[marker] is expected

    return exit_code, result


def test_qr_public_validator_cli_returns_sorted_json_for_matching_record(capsys):
    exit_code, result = _run_cli(_load_matching_payload(), capsys)

    assert exit_code == 0
    assert result["status"] == "qr_record_validated"
    assert result["qr_payload_status"] == "valid_payload"
    assert result["bridge_status"] == "bridge_match"
    assert result["record_lookup_status"] == "found"
    assert result["content_hash_match"] is True
    assert result["local_validator"]["record_id"] == "HC-RELEASE-2026-0001"
    assert result["local_validator"]["status"] == "found"


def test_qr_public_validator_cli_returns_one_for_content_hash_mismatch(capsys):
    payload = _load_matching_payload()
    payload["content_hash"] = "0" * 64
    _refresh_payload_hash(payload)

    exit_code, result = _run_cli(payload, capsys)

    assert exit_code == 1
    assert result["status"] == "qr_record_mismatch"
    assert result["qr_payload_status"] == "valid_payload"
    assert result["bridge_status"] == "bridge_mismatch"
    assert result["record_lookup_status"] == "found"
    assert result["content_hash_match"] is False
    assert result["local_validator"]["status"] == "found"


def test_qr_public_validator_cli_returns_one_for_malformed_json(capsys):
    exit_code, result = _run_cli('{"record_id":', capsys)

    assert exit_code == 1
    assert result["status"] == "malformed_payload"
    assert result["qr_payload_status"] == "malformed_payload"
    assert result["local_validator"] is None


def test_qr_public_validator_cli_does_not_call_network(monkeypatch, capsys):
    def fail_network(*args, **kwargs):
        raise AssertionError("QR Public Validator CLI must remain local-only")

    monkeypatch.setattr(socket, "create_connection", fail_network)
    monkeypatch.setattr(urllib.request, "urlopen", fail_network)

    exit_code, result = _run_cli(_load_matching_payload(), capsys)

    assert exit_code == 0
    assert result["status"] == "qr_record_validated"


def test_qr_public_validator_cli_uses_current_checkout_root(
    monkeypatch, capsys, tmp_path
):
    monkeypatch.setattr(
        qr_public_validator,
        "ROOT",
        tmp_path / "installed-package-location",
    )
    monkeypatch.chdir(ROOT)

    exit_code, result = _run_cli(_load_matching_payload(), capsys)

    assert exit_code == 0
    assert result["status"] == "qr_record_validated"
    assert result["record_lookup_status"] == "found"
