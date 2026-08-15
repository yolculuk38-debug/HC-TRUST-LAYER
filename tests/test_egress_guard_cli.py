"""HC Optical Egress Guard CLI boundary tests."""

from __future__ import annotations

import json
from pathlib import Path

from hc_trust.cli import main
from hc_trust.egress_guard import MAX_JSON_BYTES


REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_ROOT = REPO_ROOT / "examples" / "hc-egress-guard"
POLICY_PATH = EXAMPLE_ROOT / "evidence-only-policy.json"


def test_cli_allows_normal_fixture_and_emits_json(capsys) -> None:
    exit_code = main(
        [
            "egress-evaluate",
            str(EXAMPLE_ROOT / "normal-event.json"),
            "--policy",
            str(POLICY_PATH),
        ]
    )

    output = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert output["decision"] == "ALLOW"
    assert output["assurance"]["hardware_enforcement"] == "NOT_CONNECTED"
    assert output["assurance"]["quantum_security"] == "NOT_CLAIMED"


def test_cli_blocks_trip_fixture(capsys) -> None:
    exit_code = main(
        [
            "egress-evaluate",
            str(EXAMPLE_ROOT / "trip-event.json"),
            "--policy",
            str(POLICY_PATH),
        ]
    )

    output = json.loads(capsys.readouterr().out)
    assert exit_code == 1
    assert output["decision"] == "BLOCK"
    assert output["recommended_action"] == "CLOSE_AND_HOLD"
    assert "DETECTOR_SATURATED" in output["reason_codes"]


def test_cli_rejects_duplicate_json_properties_without_hash_claim(
    tmp_path, capsys
) -> None:
    event_path = tmp_path / "duplicate-event.json"
    event_path.write_text(
        '{"schema_version":"hc-egress-sensor-event-v1",'
        '"schema_version":"hc-egress-sensor-event-v1"}',
        encoding="utf-8",
    )

    exit_code = main(
        [
            "egress-evaluate",
            str(event_path),
            "--policy",
            str(POLICY_PATH),
        ]
    )

    output = json.loads(capsys.readouterr().out)
    assert exit_code == 2
    assert output == {
        "schema_version": "hc-egress-error-v1",
        "engine_version": "0.1.0",
        "status": "INVALID_INPUT",
        "decision": "BLOCK",
        "recommended_action": "CLOSE_AND_HOLD",
        "reason_codes": ["JSON_INVALID"],
        "error_document": "EVENT",
        "assurance": {
            "policy_authentication": "NOT_VERIFIED",
            "telemetry_authentication": "NOT_VERIFIED",
            "decision_authentication": "NOT_SIGNED",
            "hardware_enforcement": "NOT_CONNECTED",
            "replay_protection": "NOT_IMPLEMENTED",
            "quantum_security": "NOT_CLAIMED",
        },
        "hardware_enforcement_performed": False,
        "human_review_required": True,
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
    }
    assert "digest" not in json.dumps(output).lower()


def test_cli_rejects_unreadable_policy_before_event(capsys, tmp_path) -> None:
    missing_policy = tmp_path / "missing-policy.json"

    exit_code = main(
        [
            "egress-evaluate",
            str(EXAMPLE_ROOT / "normal-event.json"),
            "--policy",
            str(missing_policy),
        ]
    )

    output = json.loads(capsys.readouterr().out)
    assert exit_code == 2
    assert output["decision"] == "BLOCK"
    assert output["error_document"] == "POLICY"
    assert output["reason_codes"] == ["JSON_READ_FAILED"]


def test_cli_rejects_oversized_event_without_unbounded_parse(capsys, tmp_path) -> None:
    event_path = tmp_path / "oversized-event.json"
    event_path.write_bytes(b"{" + (b" " * MAX_JSON_BYTES) + b"}")

    exit_code = main(
        [
            "egress-evaluate",
            str(event_path),
            "--policy",
            str(POLICY_PATH),
        ]
    )

    output = json.loads(capsys.readouterr().out)
    assert exit_code == 2
    assert output["decision"] == "BLOCK"
    assert output["error_document"] == "EVENT"
    assert output["reason_codes"] == ["JSON_TOO_LARGE"]


def test_cli_rejects_invalid_utf8_event(capsys, tmp_path) -> None:
    event_path = tmp_path / "invalid-utf8-event.json"
    event_path.write_bytes(b'{"event_id":"\xff"}')

    exit_code = main(
        [
            "egress-evaluate",
            str(event_path),
            "--policy",
            str(POLICY_PATH),
        ]
    )

    output = json.loads(capsys.readouterr().out)
    assert exit_code == 2
    assert output["decision"] == "BLOCK"
    assert output["error_document"] == "EVENT"
    assert output["reason_codes"] == ["JSON_INVALID_UTF8"]
