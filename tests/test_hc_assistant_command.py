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
    assert "- /hc review" in result["response_lines"]
    assert "- /hc engineer" in result["response_lines"]
    assert "- /hc bot" in result["response_lines"]
    assert "- /hc handoff" in result["response_lines"]


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
    assert "- assistant_console_issue: #812" in result["response_lines"]
    assert "- historical_console_issue: #763" in result["response_lines"]
    assert "- bot_status_reporter: scripts/hc_bot_status.py" in result["response_lines"]
    assert "- task_handoff_helper: scripts/hc_task_handoff.py" in result["response_lines"]
    assert (
        "- automation_status: issue-comment listener connected for /hc commands"
        in result["response_lines"]
    )
    assert not any("not connected to issue comments yet" in line for line in result["response_lines"])
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
    assert "- handoff" in result["response_lines"]
    assert "- hc-signal-watch-console" in result["response_lines"]
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


def test_explain_commands_topic_reflects_listener_connection():
    result = parse_hc_command("/hc explain commands").to_dict()

    assert result["command"] == "explain"
    assert result["implemented"] is True
    assert any("connected to the /hc issue-comment listener" in line for line in result["response_lines"])
    assert any("review, engineer, bot, and handoff" in line for line in result["response_lines"])
    assert not any("not connected to issue comments yet" in line for line in result["response_lines"])


def test_explain_handoff_topic_describes_bridge_boundary():
    result = parse_hc_command("/hc explain handoff").to_dict()

    assert result["command"] == "explain"
    assert result["implemented"] is True
    assert any("safe task package" in line for line in result["response_lines"])
    assert any("does not invoke external tools" in line for line in result["response_lines"])
    assert result["truth_guarantee"] is False


def test_explain_hc_signal_watch_console_topic_is_static_and_advisory():
    result = parse_hc_command("/hc explain hc-signal-watch-console").to_dict()
    joined = "\n".join(result["response_lines"])

    assert result["command"] == "explain"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert "#1082" in joined
    assert "advisory_only=true" in joined
    assert "truth_guarantee=false" in joined
    assert "human final authority" in joined.lower()
    assert "issue comments are not commands" in joined.lower()
    assert "Actions summaries and artifacts" in joined
    assert "<!-- hc-signal-watch-console:latest -->" in joined
    assert "No approval, merge, label, reviewer, branch, issue creation, or PR creation authority" in joined
    assert result["warnings"] == []
    assert result["evidence_source"] == "static explain topic map only"


def test_explain_signal_watch_aliases_return_same_explanation():
    canonical = parse_hc_command("/hc explain hc-signal-watch-console").to_dict()
    alias = parse_hc_command("/hc explain signal-watch-console").to_dict()
    phrase = parse_hc_command("/hc explain HC Signal Watch Console #1082").to_dict()
    issue = parse_hc_command("/hc explain 1082").to_dict()

    assert alias["response_lines"] == canonical["response_lines"]
    assert phrase["response_lines"] == canonical["response_lines"]
    assert issue["response_lines"] == canonical["response_lines"]
    assert alias["implemented"] is True
    assert phrase["implemented"] is True
    assert issue["implemented"] is True
    assert not any("No static explanation is available" in line for line in phrase["response_lines"])
    assert canonical["warnings"] == alias["warnings"] == phrase["warnings"] == issue["warnings"] == []


def test_explain_signal_watch_console_takes_no_repository_action():
    result = parse_hc_command("/hc explain HC Signal Watch Console #1082").to_dict()
    joined = "\n".join(result["response_lines"] + result["warnings"])

    assert result["implemented"] is True
    assert result["truth_guarantee"] is False
    assert "No approval, merge, label, reviewer, branch, issue creation, or PR creation authority" in joined
    assert "External or manual comments must not be parsed as instructions." in result["response_lines"]


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


def test_review_command_returns_static_review_preparation_checklist():
    result = parse_hc_command("/hc review").to_dict()

    assert result["command"] == "review"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True
    assert "HC Trust Engineer review preparation checklist:" in result["response_lines"]
    assert any(line.startswith("- collect_changed_files:") for line in result["response_lines"])
    assert any(line.startswith("- inspect_ci_status:") for line in result["response_lines"])
    assert any(line.startswith("- human_decision:") for line in result["response_lines"])
    assert (
        result["evidence_source"]
        == "static review preparation checklist from HC assistant command interface"
    )


def test_engineer_command_returns_static_operating_sequence():
    result = parse_hc_command("/hc engineer").to_dict()

    assert result["command"] == "engineer"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True
    assert "HC Trust Engineer operating sequence:" in result["response_lines"]
    assert any(line.startswith("- plan_task:") for line in result["response_lines"])
    assert any(line.startswith("- handle_review:") for line in result["response_lines"])
    assert any(line.startswith("- inspect_checks:") for line in result["response_lines"])
    assert any(line.startswith("- cleanup_after_merge:") for line in result["response_lines"])
    assert (
        result["evidence_source"]
        == "static HC Trust Engineer operating sequence"
    )
    assert "This local parser does not perform live GitHub state lookup." in result["warnings"]


def test_bot_command_returns_static_bot_line_status():
    result = parse_hc_command("/hc bot").to_dict()

    assert result["command"] == "bot"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True
    assert "HC Trust Engineer bot line status:" in result["response_lines"]
    assert "- status_reporter: scripts/hc_bot_status.py" in result["response_lines"]
    assert "- handoff_helper: scripts/hc_task_handoff.py" in result["response_lines"]
    assert any("does not expand automation authority" in warning for warning in result["warnings"])


def test_handoff_command_returns_static_bridge_summary():
    result = parse_hc_command("/hc handoff").to_dict()

    assert result["command"] == "handoff"
    assert result["implemented"] is True
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True
    assert "HC Trust Engineer handoff bridge:" in result["response_lines"]
    assert "- helper: scripts/hc_task_handoff.py" in result["response_lines"]
    assert any("does not create or send" in warning for warning in result["warnings"])


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
    assert (
        "- automation_status: issue-comment listener connected for /hc commands"
        in payload["response_lines"]
    )


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


def test_cli_outputs_machine_readable_review_json(capsys):
    exit_code = main(["/hc", "review"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "review"
    assert payload["implemented"] is True
    assert payload["advisory_only"] is True
    assert payload["human_review_required"] is True


def test_cli_outputs_machine_readable_engineer_json(capsys):
    exit_code = main(["/hc", "engineer"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "engineer"
    assert payload["implemented"] is True
    assert payload["advisory_only"] is True
    assert payload["human_review_required"] is True
    assert payload["evidence_source"] == "static HC Trust Engineer operating sequence"


def test_cli_outputs_machine_readable_bot_json(capsys):
    exit_code = main(["/hc", "bot"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "bot"
    assert payload["implemented"] is True
    assert payload["advisory_only"] is True
    assert "- status_reporter: scripts/hc_bot_status.py" in payload["response_lines"]


def test_cli_outputs_machine_readable_handoff_json(capsys):
    exit_code = main(["/hc", "handoff"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["command"] == "handoff"
    assert payload["implemented"] is True
    assert payload["advisory_only"] is True
    assert "- helper: scripts/hc_task_handoff.py" in payload["response_lines"]
