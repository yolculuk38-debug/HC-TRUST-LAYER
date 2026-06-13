import json

from scripts.hc_engineer_task_plan import build_plan, main


def test_clean_docs_only_task_plans_one_pr_and_allows_merge_gate_after_checks():
    plan = build_plan(
        {
            "task_title": "Document HC Engineer operator flow",
            "changed_files": ["docs/hc-engineer/operator-flow.md"],
            "checks": [{"name": "docs", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert plan["task_title"] == "Document HC Engineer operator flow"
    assert len(plan["planned_prs"]) == 1
    assert plan["planned_prs"][0]["preserves_one_open_pr_discipline"] is True
    assert plan["stop_conditions"] == []
    assert plan["merge_gate"]["allowed"] is True
    assert plan["merge_gate"]["state"] == "allowed_after_checks"


def test_task_with_open_pr_blocks_new_work():
    plan = build_plan(
        {
            "task_title": "Add follow-up task",
            "open_prs": [123],
            "changed_files": ["docs/follow-up.md"],
            "checks": [{"name": "docs", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert "open_pr_exists_stop_before_starting_new_work" in plan["stop_conditions"]
    assert plan["merge_gate"]["allowed"] is False
    assert plan["review_order"][0].startswith("Stop new work")


def test_task_with_unresolved_codex_or_review_comment_requires_resolve_first():
    plan = build_plan(
        {
            "task_title": "Resolve review feedback",
            "changed_files": ["docs/review.md"],
            "unresolved_review_comments": ["codex-comment-1"],
            "checks": [{"name": "docs", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert "unresolved_review_comments_resolve_before_checks_or_merge" in plan["stop_conditions"]
    assert plan["merge_gate"]["requires_review_resolution_first"] is True
    assert plan["review_order"].index(
        "Resolve Codex and human review comments before inspecting checks or considering merge."
    ) < plan["review_order"].index("Inspect required checks after review comments are resolved.")


def test_task_with_failed_or_pending_checks_blocks_merge():
    pending = build_plan(
        {
            "task_title": "Pending checks task",
            "changed_files": ["docs/pending.md"],
            "checks": [{"name": "tests", "status": "in_progress", "conclusion": None}],
        }
    ).to_dict()
    failed = build_plan(
        {
            "task_title": "Failed checks task",
            "changed_files": ["docs/failed.md"],
            "checks": [{"name": "tests", "status": "completed", "conclusion": "failure"}],
        }
    ).to_dict()

    assert "checks_pending_merge_blocked" in pending["stop_conditions"]
    assert pending["merge_gate"]["allowed"] is False
    assert "checks_failed_merge_blocked" in failed["stop_conditions"]
    assert failed["merge_gate"]["allowed"] is False


def test_task_with_protected_path_requires_human_review():
    plan = build_plan(
        {
            "task_title": "Schema-adjacent task",
            "changed_files": ["schema/record-v1.schema.json"],
            "checks": [{"name": "tests", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert "protected_paths_require_human_review" in plan["stop_conditions"]
    assert plan["planned_prs"][0]["human_review_required"] is True
    assert plan["merge_gate"]["requires_human_review"] is True
    assert plan["merge_gate"]["allowed"] is False


def test_output_always_preserves_advisory_public_truth_boundaries(tmp_path, capsys):
    fixture = tmp_path / "fixture.json"
    fixture.write_text(
        json.dumps(
            {
                "task_title": "Boundary check",
                "changed_files": ["examples/hc-engineer/task-plan-fixture.json"],
                "checks": [{"name": "tests", "status": "completed", "conclusion": "success"}],
            }
        ),
        encoding="utf-8",
    )

    built = build_plan(json.loads(fixture.read_text(encoding="utf-8"))).to_dict()
    exit_code = main([str(fixture)])
    payload = json.loads(capsys.readouterr().out)

    assert built["advisory_only"] is True
    assert built["public_safe"] is True
    assert built["truth_guarantee"] is False
    assert exit_code == 0
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False


def test_scanner_human_review_path_without_protected_path_blocks_clean_merge_gate():
    plan = build_plan(
        {
            "task_title": "Align package version notes",
            "changed_files": ["pyproject.toml"],
            "checks": [{"name": "tests", "status": "completed", "conclusion": "success"}],
        }
    ).to_dict()

    assert "protected_paths_require_human_review" not in plan["stop_conditions"]
    assert "scanner_human_review_required" in plan["stop_conditions"]
    assert plan["planned_prs"][0]["human_review_required"] is True
    assert plan["merge_gate"]["requires_human_review"] is True
    assert plan["merge_gate"]["allowed"] is False
    assert plan["merge_gate"]["state"] != "allowed_after_checks"
    assert any("human review" in step for step in plan["review_order"])


def test_completed_skipped_check_does_not_count_as_success():
    plan = build_plan(
        {
            "task_title": "Skipped check task",
            "changed_files": ["docs/skipped.md"],
            "checks": [{"name": "docs", "status": "completed", "conclusion": "skipped"}],
        }
    ).to_dict()

    assert "checks_skipped_require_human_review" in plan["stop_conditions"]
    assert plan["merge_gate"]["requires_human_review"] is True
    assert plan["merge_gate"]["allowed"] is False
    assert plan["merge_gate"]["state"] != "allowed_after_checks"
