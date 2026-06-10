import json

from scripts.hc_assistant_command import main, parse_hc_command


def test_help_command_lists_core_commands():
    result = parse_hc_command("/hc help").to_dict()

    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["command"] == "help"
    assert result["implemented"] is True
    assert "- /hc help" in result["response_lines"]
    assert "- /hc status" in result["response_lines"]
    assert "- /hc next" in result["response_lines"]
    assert "- /hc evidence" in result["response_lines"]
    assert "- /hc explain <topic-or-path>" in result["response_lines"]
    assert "- /hc risks" in result["response_lines"]


def test_empty_hc_command_defaults_to_help():
    result = parse_hc_command("/hc").to_dict()

    assert result["command"] == "help"
    assert result["implemented"] is True


def test_status_command_is_static_and_advisory():
    result = parse_hc_command("/hc status").to_dict()

    assert result["command"] == "status"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert "- assistant_console_issue: #763" in result["response_lines"]
    assert result["evidence_source"] == "static command interface only"


def test_next_command_returns_static_project_control_guidance():
    result = parse_hc_command("/hc next").to_dict()

    assert result["command"] == "next"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert "- mode: REPORT ONLY" in result["response_lines"]
    assert (
        result["evidence_source"]
        == "static project-control guidance from docs/project-control/next-actions.md"
    )


def test_evidence_command_returns_checklist():
    result = parse_hc_command("/hc evidence").to_dict()

    assert result["command"] == "evidence"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True
    assert "HC Trust Engineer evidence bundle checklist:" in result["response_lines"]
    assert any(line.startswith("- changed_files:") for line in result["response_lines"])
    assert any(line.startswith("- checks:") for line in result["response_lines"])
    assert any(line.startswith("- advisory_boundary:") for line in result["response_lines"])


def test_explain_command_lists_topics_when_no_topic_is_provided():
    result = parse_hc_command("/hc explain").to_dict()

    assert result["command"] == "explain"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert "HC Trust Engineer explain topics:" in result["response_lines"]
    assert "- advisory-only" in result["response_lines"]
    assert "No topic was provided; returning available static topics." in result["warnings"]


def test_explain_command_returns_static_topic_details():
    result = parse_hc_command("/hc explain advisory-only").to_dict()

    assert result["command"] == "explain"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert "HC Trust Engineer explanation: advisory-only" in result["response_lines"]
    assert any("must not approve" in line for line in result["response_lines"])
    assert result["warnings"] == []
    assert result["evidence_source"] == "static explain topic map only"


def test_explain_unknown_topic_is_advisory_only():
    result = parse_hc_command("/hc explain unknown-topic").to_dict()

    assert result["command"] == "explain"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert "No static explanation is available for: unknown-topic" in result["response_lines"]
    assert "Unknown explain topic ignored; no repository action was taken." in result["warnings"]


def test_risks_command_returns_static_risk_checklist():
    result = parse_hc_command("/hc risks").to_dict()

    assert result["command"] == "risks"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True
    assert "HC Trust Engineer risk checklist:" in result["response_lines"]
    assert any(line.startswith("- protected_path:") for line in result["response_lines"])
    assert any(line.startswith("- workflow_risk:") for line in result["response_lines"])
    assert any(line.startswith("- stale_context_risk:") for line in result["response_lines"])
    assert (
        result["evidence_source"]
        == "static risk checklist from HC assistant command interface"
    )


def test_deferred_review_command_is_not_implemented():
    result = parse_hc_command("/hc review").to_dict()

    assert result["command"] == "review"
    assert result["implemented"] is False
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False


def test_unknown_command_is_ignored():
    result = parse_hc_command("/hc unknown-command").to_dict()

    assert result["command"] == "unknown-command"
    assert result["implemented"] is False
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False


def test_missing_prefix_is_treated_as_unknown():
    result = parse_hc_command("plain text without prefix").to_dict()

    assert result["command"] == "unknown"
    assert result["implemented"] is False


def test_cli_outputs_machine_readable_status_json(capsys):
    exit_code = main(["/hc", "status"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "status"
    assert payload["implemented"] is True
    assert payload["advisory_only"] is True


def test_cli_outputs_machine_readable_evidence_json(capsys):
    exit_code = main(["/hc", "evidence"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "evidence"
    assert payload["implemented"] is True
    assert payload["advisory_only"] is True
    assert payload["human_review_required"] is True


def test_cli_outputs_machine_readable_explain_json(capsys):
    exit_code = main(["/hc", "explain", "trust-kernel"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "explain"
    assert payload["implemented"] is True
    assert payload["advisory_only"] is True
    assert payload["evidence_source"] == "static explain topic map only"


def test_cli_outputs_machine_readable_risks_json(capsys):
    exit_code = main(["/hc", "risks"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "risks"
    assert payload["implemented"] is True
    assert payload["advisory_only"] is True
    assert payload["human_review_required"] is True
