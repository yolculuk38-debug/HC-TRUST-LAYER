import json

import pytest

from scripts.hc_task_claim import evaluate_claim, main


def base_fixture(**overrides):
    fixture = {
        "task_id": "HC-TASK-2026-001",
        "task_title": "Add local claim evaluator",
        "requested_by": "maintainer",
        "requested_action": "claim",
        "current_state": "ready",
        "open_prs": [],
        "existing_claims": [],
        "stale_after_hours": 24,
        "maintainer_acknowledged": False,
        "changed_files": ["scripts/hc_task_claim.py"],
        "notes": "Local-only advisory fixture.",
    }
    fixture.update(overrides)
    return fixture


def report(**overrides):
    return evaluate_claim(base_fixture(**overrides)).to_dict()


def test_valid_ready_task_can_produce_advisory_claim_ready():
    payload = report()

    assert payload["claim_allowed"] is True
    assert payload["claim_status"] == "advisory_claim_ready"
    assert payload["blockers"] == []


def test_open_pr_blocks_duplicate_claim():
    payload = report(open_prs=["#123"])

    assert payload["claim_allowed"] is False
    assert payload["claim_status"] == "advisory_claim_blocked"
    assert "open_pr_exists_do_not_duplicate" in payload["blockers"]


def test_existing_active_claim_blocks_duplicate_claim():
    payload = report(existing_claims=[{"task_id": "HC-TASK-2026-001", "state": "active"}])

    assert payload["claim_allowed"] is False
    assert "duplicate_active_claim" in payload["blockers"]


@pytest.mark.parametrize("state", ["claimed", "in_progress", "pr_open"])
def test_existing_claimed_in_progress_or_pr_open_claim_blocks_duplicate_claim(state):
    payload = report(existing_claims=[{"task_id": "HC-TASK-2026-001", "state": state}])

    assert payload["claim_allowed"] is False
    assert "duplicate_active_claim" in payload["blockers"]


def test_proposed_state_requires_maintainer_ready_decision():
    payload = report(current_state="proposed")

    assert payload["claim_allowed"] is False
    assert payload["claim_status"] == "advisory_claim_blocked"
    assert payload["next_human_action"] == "maintainer_ready_decision_required"


def test_pr_open_blocks_claim():
    payload = report(current_state="pr_open")

    assert payload["claim_allowed"] is False
    assert payload["claim_status"] == "advisory_claim_blocked"


def test_stale_without_maintainer_acknowledged_blocks_claim():
    payload = report(current_state="stale", maintainer_acknowledged=False)

    assert payload["claim_allowed"] is False
    assert payload["claim_status"] == "advisory_claim_blocked"


def test_stale_with_maintainer_acknowledged_can_produce_advisory_claim_ready():
    payload = report(current_state="stale", maintainer_acknowledged=True)

    assert payload["claim_allowed"] is True
    assert payload["claim_status"] == "advisory_claim_ready"


def test_invalid_task_id_blocks_claim():
    payload = report(task_id="TASK-1")

    assert payload["claim_allowed"] is False
    assert "invalid_task_id" in payload["blockers"]


def test_release_action_does_not_imply_repository_mutation():
    payload = report(requested_action="release", current_state="claimed")

    assert payload["claim_status"] == "manual_release_ready"
    assert payload["repository_mutation"] is False
    assert payload["approval_authority"] is False
    assert payload["merge_authority"] is False


def test_unsupported_state_release_blocks_manual_release_ready():
    payload = report(requested_action="release", current_state="typo")

    assert payload["claim_allowed"] is False
    assert payload["claim_status"] == "advisory_claim_blocked"
    assert "unsupported_current_state" in payload["warnings"]
    assert "unsupported_current_state" in payload["blockers"]
    assert payload["next_human_action"] == "maintainer_correct_or_review_current_state"


def test_status_action_is_advisory_only():
    payload = report(requested_action="status", current_state="ready")

    assert payload["claim_status"] == "status_only"
    assert payload["claim_allowed"] is False
    assert payload["advisory_only"] is True
    assert payload["human_review_required"] is True


def test_unknown_action_warns_and_blocks_claim():
    payload = report(requested_action="assign")

    assert payload["claim_allowed"] is False
    assert payload["claim_status"] == "advisory_claim_blocked"
    assert "unsupported_requested_action" in payload["warnings"]


def test_malformed_non_object_json_fails_cleanly(tmp_path):
    fixture = tmp_path / "claim.json"
    fixture.write_text(json.dumps(["not", "object"]), encoding="utf-8")

    with pytest.raises(ValueError, match="claim fixture must be a JSON object"):
        main([str(fixture)])


def test_output_preserves_hc_boundary_fields():
    payload = report()

    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["human_review_required"] is True
    assert payload["repository_mutation"] is False
    assert payload["issue_comment_automation"] is False
    assert payload["label_reviewer_mutation"] is False
    assert payload["approval_authority"] is False
    assert payload["merge_authority"] is False


def test_cli_outputs_pretty_json(tmp_path, capsys):
    fixture = tmp_path / "claim.json"
    fixture.write_text(json.dumps(base_fixture()), encoding="utf-8")

    exit_code = main([str(fixture), "--pretty"])
    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["task_id"] == "HC-TASK-2026-001"
    assert payload["claim_status"] == "advisory_claim_ready"
    assert captured.out.startswith("{\n")
