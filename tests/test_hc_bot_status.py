import json

from scripts.hc_bot_status import build_bot_status, main


def test_bot_status_is_report_only_and_public_safe():
    status = build_bot_status().to_dict()

    assert status["status"] == "report_only_advisory_mvp"
    assert status["advisory_only"] is True
    assert status["public_safe"] is True
    assert status["truth_guarantee"] is False
    assert status["human_review_required"] is True
    assert "no_repository_writes=true" in status["boundaries"]
    assert "no_approval_or_merge_authority=true" in status["boundaries"]


def test_bot_status_separates_active_and_parked_components():
    status = build_bot_status().to_dict()

    assert "hc_control_bot_path_scanner" in status["active_components"]
    assert "hc_assistant_command_parser" in status["active_components"]
    assert "hc_assistant_issue_comment_listener" in status["active_components"]
    assert "github_app" in status["parked_components"]
    assert "live_chat_ui" in status["parked_components"]
    assert "llm_memory_layer" in status["parked_components"]
    assert "automatic_merge" in status["parked_components"]


def test_bot_status_next_steps_do_not_expand_authority():
    status = build_bot_status().to_dict()

    assert "keep_report_only_runner_green" in status["next_safe_steps"]
    assert "require_human_review_for_authority_expansion" in status["next_safe_steps"]
    assert status["evidence_source"] == "static repository bot-line status map"


def test_cli_outputs_machine_readable_bot_status(capsys):
    exit_code = main([])

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["status"] == "report_only_advisory_mvp"
    assert payload["advisory_only"] is True
    assert payload["truth_guarantee"] is False
    assert "hc_engineer_task_planner" in payload["active_components"]
    assert "semantic_llm_review" in payload["parked_components"]
