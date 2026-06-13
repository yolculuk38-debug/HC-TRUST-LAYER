import json

from scripts.hc_task_handoff import build_handoff, main


def test_handoff_is_report_only_and_does_not_invoke_external_agent():
    package = build_handoff(
        {
            "task_title": "Add docs note",
            "changed_files": ["docs/project-control/example.md"],
            "checks": [{"name": "ci", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert package["advisory_only"] is True
    assert package["public_safe"] is True
    assert package["truth_guarantee"] is False
    assert package["invokes_external_agent"] is False
    assert package["creates_pull_request"] is False
    assert package["requires_human_submit"] is True
    assert package["task_title"] == "Add docs note"


def test_handoff_wraps_engineer_plan_and_prompt_lines():
    package = build_handoff(
        {
            "task_title": "Add docs note",
            "changed_files": ["docs/project-control/example.md"],
            "checks": [{"name": "ci", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert package["plan"]["planned_pr_count"] == 1
    assert package["merge_gate"]["allowed"] is True
    assert package["stop_conditions"] == []
    assert "HC Trust Engineer task handoff package." in package["handoff_prompt_lines"]
    assert any("Open one small PR only." == line for line in package["handoff_prompt_lines"])
    assert any("Expected files: docs/project-control/example.md" == line for line in package["handoff_prompt_lines"])


def test_handoff_preserves_stop_conditions_for_existing_open_prs():
    package = build_handoff(
        {
            "task_title": "Blocked task",
            "changed_files": ["docs/project-control/example.md"],
            "open_prs": ["#1"],
            "checks": [{"name": "ci", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert "open_pr_exists_stop_before_starting_new_work" in package["stop_conditions"]
    assert package["merge_gate"]["allowed"] is False


def test_handoff_cli_outputs_json(tmp_path, capsys):
    fixture = tmp_path / "task.json"
    fixture.write_text(
        json.dumps(
            {
                "task_title": "Add docs note",
                "changed_files": ["docs/project-control/example.md"],
                "checks": [{"name": "ci", "status": "completed", "conclusion": "success"}],
            }
        ),
        encoding="utf-8",
    )

    exit_code = main([str(fixture)])
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["task_title"] == "Add docs note"
    assert payload["advisory_only"] is True
    assert payload["invokes_external_agent"] is False
    assert payload["creates_pull_request"] is False
