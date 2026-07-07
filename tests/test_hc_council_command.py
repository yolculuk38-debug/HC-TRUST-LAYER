import json
from pathlib import Path

from scripts.hc_council_command import main, parse_command, parse_fixture


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_PATH = ROOT / "examples" / "hc_council_command.example.json"


EXPECTED_PUBLIC_SAFE_MARKERS = {
    "mode": "report_only",
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
}


def assert_public_safe_markers(payload):
    assert {key: payload[key] for key in EXPECTED_PUBLIC_SAFE_MARKERS} == (
        EXPECTED_PUBLIC_SAFE_MARKERS
    )


def test_parse_pr_review_command_is_report_only_and_public_safe():
    payload = parse_command(
        "/hc council review pr 1199",
        evidence_refs=["docs/project-control/hc-council-command-surface.md"],
    ).to_dict()

    assert_public_safe_markers(payload)
    assert payload["accepted"] is True
    assert payload["action"] == "review"
    assert payload["target_type"] == "pr"
    assert payload["target_number"] == 1199
    assert payload["next_action"] == "build_council_fixture"
    assert payload["stop_reasons"] == []
    assert payload["warnings"] == ["pr_review_requires_live_github_gate_snapshot"]


def test_parse_repo_review_command_requires_gate_snapshot_warning():
    payload = parse_command("/hc council review repo").to_dict()

    assert_public_safe_markers(payload)
    assert payload["accepted"] is True
    assert payload["target_type"] == "repo"
    assert payload["target_number"] is None
    assert payload["warnings"] == ["repo_review_requires_current_gate_snapshot"]


def test_parse_status_like_commands_are_accepted_without_targets():
    for command in [
        "/hc council status",
        "/hc council risks",
        "/hc council evidence",
        "/hc council daily",
    ]:
        payload = parse_command(command).to_dict()

        assert_public_safe_markers(payload)
        assert payload["accepted"] is True
        assert payload["target_type"] is None
        assert payload["target_number"] is None
        assert payload["next_action"] == "run_report_only_status"
        assert payload["stop_reasons"] == []


def test_invalid_commands_fail_closed_with_public_safe_errors():
    cases = {
        "": "command_too_short",
        "/wrong council review repo": "invalid_prefix",
        "/hc council approve pr 1": "unknown_action",
        "/hc council review": "missing_review_target",
        "/hc council review branch main": "unknown_review_target",
        "/hc council review pr abc": "invalid_pr_number",
        "/hc council review pr 0": "invalid_pr_number",
        "/hc council status extra": "unexpected_arguments",
    }

    for command, reason in cases.items():
        payload = parse_command(command).to_dict()

        assert_public_safe_markers(payload)
        assert payload["accepted"] is False
        assert payload["next_action"] == "stop"
        assert payload["stop_reasons"] == [reason]


def test_fixture_parsing_sorts_and_deduplicates_evidence_refs():
    fixture = {
        "command": "/hc council review repo",
        "evidence_refs": ["z-ref", "a-ref", "z-ref", ""],
    }

    payload = parse_fixture(fixture)

    assert payload["accepted"] is True
    assert payload["evidence_refs"] == ["a-ref", "z-ref"]


def test_example_fixture_parses_to_expected_pr_target():
    payload = parse_fixture(json.loads(EXAMPLE_PATH.read_text(encoding="utf-8")))

    assert_public_safe_markers(payload)
    assert payload["accepted"] is True
    assert payload["target_type"] == "pr"
    assert payload["target_number"] == 1199
    assert payload["evidence_refs"] == [
        "docs/project-control/hc-council-command-surface.md",
        "https://github.com/yolculuk38-debug/HC-TRUST-LAYER/pull/1199",
    ]


def write_cli_fixture(path, command="/hc council review pr 1200"):
    path.write_text(
        json.dumps(
            {
                "command": command,
                "evidence_refs": ["docs/project-control/hc-council-command-surface.md"],
            }
        ),
        encoding="utf-8",
    )


def test_cli_outputs_deterministic_public_safe_json(tmp_path, capsys):
    fixture = tmp_path / "fixture.json"
    write_cli_fixture(fixture)

    exit_code = main([str(fixture)])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)
    assert exit_code == 0
    assert_public_safe_markers(payload)
    assert payload["accepted"] is True
    assert payload["target_number"] == 1200
    assert payload["evidence_source"] == "local command text only"


def test_cli_pretty_output_remains_valid_public_safe_json(tmp_path, capsys):
    fixture = tmp_path / "fixture.json"
    write_cli_fixture(fixture, command="/hc council review repo")

    exit_code = main([str(fixture), "--pretty"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "\n  " in captured.out
    payload = json.loads(captured.out)
    assert_public_safe_markers(payload)
    assert payload["accepted"] is True
    assert payload["target_type"] == "repo"
