import json
from pathlib import Path

from scripts.hc_council_issue_command_bridge import build_issue_command_bridge, main


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_PATH = ROOT / "examples" / "hc_council_issue_command.example.json"


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


def fixture(body="/hc council review pr 1201", author_association="OWNER"):
    return {
        "event_name": "issue_comment",
        "repository": {"full_name": "yolculuk38-debug/HC-TRUST-LAYER"},
        "issue": {
            "number": 1201,
            "pull_request": {
                "url": "https://api.github.com/repos/yolculuk38-debug/HC-TRUST-LAYER/pulls/1201"
            },
        },
        "comment": {
            "body": body,
            "author_association": author_association,
        },
        "evidence_refs": [
            "scripts/hc_council_issue_command_bridge.py",
            "scripts/hc_council_command.py",
        ],
    }


def test_bridge_accepts_owner_issue_comment_command_as_report_only():
    payload = build_issue_command_bridge(fixture())

    assert_public_safe_markers(payload)
    assert payload["event_source"] == "github_issue_comment_fixture"
    assert payload["repository"] == "yolculuk38-debug/HC-TRUST-LAYER"
    assert payload["issue_number"] == 1201
    assert payload["comment_author_association"] == "OWNER"
    assert payload["accepted"] is True
    assert payload["command"] == "/hc council review pr 1201"
    assert payload["next_action"] == "run_local_council_report_fixture"
    assert payload["stop_reasons"] == []
    assert payload["command_result"]["target_type"] == "pr"
    assert payload["command_result"]["target_number"] == 1201
    assert "bridge_fixture_requires_live_policy_checks" in payload["warnings"]


def test_bridge_accepts_member_and_collaborator_commands():
    for association in ["MEMBER", "COLLABORATOR"]:
        payload = build_issue_command_bridge(fixture(author_association=association))

        assert_public_safe_markers(payload)
        assert payload["accepted"] is True
        assert payload["comment_author_association"] == association


def test_bridge_rejects_unauthorized_comment_author():
    payload = build_issue_command_bridge(fixture(author_association="NONE"))

    assert_public_safe_markers(payload)
    assert payload["accepted"] is False
    assert payload["next_action"] == "stop"
    assert payload["command_result"] is None
    assert payload["stop_reasons"] == ["unauthorized_comment_author"]


def test_bridge_rejects_unsupported_event():
    event = fixture()
    event["event_name"] = "pull_request"

    payload = build_issue_command_bridge(event)

    assert_public_safe_markers(payload)
    assert payload["accepted"] is False
    assert payload["stop_reasons"] == ["unsupported_event"]


def test_bridge_rejects_empty_non_command_and_multiline_comments():
    cases = {
        "": "empty_comment_body",
        "please review this": "not_hc_council_command",
        "/hc council status\n/hc council risks": "ambiguous_multiline_comment",
    }

    for body, reason in cases.items():
        payload = build_issue_command_bridge(fixture(body=body))

        assert_public_safe_markers(payload)
        assert payload["accepted"] is False
        assert payload["stop_reasons"] == [reason]
        assert payload["next_action"] == "stop"


def test_bridge_propagates_command_parser_fail_closed_result():
    payload = build_issue_command_bridge(fixture(body="/hc council review pr nope"))

    assert_public_safe_markers(payload)
    assert payload["accepted"] is False
    assert payload["stop_reasons"] == ["invalid_pr_number"]
    assert payload["command_result"]["accepted"] is False


def test_example_fixture_is_valid_and_public_safe():
    payload = build_issue_command_bridge(json.loads(EXAMPLE_PATH.read_text(encoding="utf-8")))

    assert_public_safe_markers(payload)
    assert payload["accepted"] is True
    assert payload["command_result"]["target_number"] == 1201
    assert payload["evidence_refs"] == [
        "scripts/hc_council_command.py",
        "scripts/hc_council_issue_command_bridge.py",
    ]


def test_cli_outputs_deterministic_public_safe_json(tmp_path, capsys):
    event_path = tmp_path / "event.json"
    event_path.write_text(json.dumps(fixture()), encoding="utf-8")

    exit_code = main([str(event_path), "--pretty"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)
    assert exit_code == 0
    assert "\n  " in captured.out
    assert_public_safe_markers(payload)
    assert payload["accepted"] is True
    assert payload["evidence_source"] == "local GitHub issue-comment fixture only"
