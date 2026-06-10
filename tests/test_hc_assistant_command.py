import json

from scripts.hc_assistant_command import main, parse_hc_command


def test_help_command_returns_advisory_command_list():
    result = parse_hc_command("/hc help").to_dict()

    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is False
    assert result["command_prefix"] == "/hc"
    assert result["command"] == "help"
    assert result["implemented"] is True
    assert "- /hc help" in result["response_lines"]
    assert "- /hc status" in result["response_lines"]
    assert result["warnings"] == []
    assert result["evidence_source"] == "static command interface only"


def test_empty_hc_command_defaults_to_help():
    result = parse_hc_command("/hc").to_dict()

    assert result["command"] == "help"
    assert result["implemented"] is True


def test_status_command_is_static_and_warns_no_live_lookup():
    result = parse_hc_command("/hc status").to_dict()

    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert result["command"] == "status"
    assert result["implemented"] is True
    assert "- assistant_console_issue: #763" in result["response_lines"]
    assert (
        "This local parser does not perform live GitHub state lookup."
        in result["warnings"]
    )


def test_deferred_command_is_not_executed():
    result = parse_hc_command("/hc next").to_dict()

    assert result["command"] == "next"
    assert result["implemented"] is False
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert (
        "Command is intentionally deferred for a later governance-reviewed PR."
        in result["warnings"]
    )


def test_unknown_command_is_ignored_without_repository_action():
    result = parse_hc_command("/hc merge-now").to_dict()

    assert result["command"] == "merge-now"
    assert result["implemented"] is False
    assert result["advisory_only"] is True
    assert result["truth_guarantee"] is False
    assert "Unsupported command ignored; no repository action was taken." in result["warnings"]


def test_missing_prefix_is_treated_as_unknown():
    result = parse_hc_command("please approve this PR").to_dict()

    assert result["command"] == "unknown"
    assert result["implemented"] is False
    assert "Unsupported command ignored; no repository action was taken." in result["warnings"]


def test_cli_outputs_machine_readable_json(capsys):
    exit_code = main(["/hc", "status"])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["command"] == "status"
    assert payload["implemented"] is True
    assert payload["evidence_source"] == "static command interface only"
