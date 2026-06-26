from pathlib import Path

WORKFLOW = Path(".github/workflows/hc-review-window-marker.yml")
HANDOFF_QUEUE = Path("docs/project-control/hc-task-handoff-queue.md")


def _workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_hc_review_window_marker_is_advisory_and_comment_only() -> None:
    text = _workflow_text()

    assert "name: HC Review Window Marker" in text
    assert "pull_request_target:" in text
    assert "contents: read" in text
    assert "pull-requests: read" in text
    assert "issues: write" in text
    assert "actions/checkout" not in text

    for forbidden in (
        "pull-requests: write",
        "contents: write",
        "actions: write",
        "checks: write",
        "issues.addLabels",
        "pulls.requestReviewers",
        "pulls.createReview",
        "pulls.merge",
    ):
        assert forbidden not in text


def test_hc_review_window_marker_updates_only_auto_owned_marker() -> None:
    text = _workflow_text()

    assert "<!-- hc-review-window -->" in text
    assert "<!-- hc-review-window:auto-marker -->" in text
    assert "const autoMarker = '<!-- hc-review-window:auto-marker -->';" in text
    assert "comment.body.includes(autoMarker)" in text
    assert "comment.body.includes(marker)" not in text
    assert "issues.listComments" in text
    assert "issues.updateComment" in text
    assert "issues.createComment" in text
    assert "existing.length > 0" in text
    assert "90 * 1000" in text


def test_hc_review_window_marker_comment_permission_fallback_is_non_blocking() -> None:
    text = _workflow_text()

    for expected in (
        "Resource not accessible by integration",
        "error.status === 403",
        "core.warning",
        "GITHUB_STEP_SUMMARY",
        "writeMarkerSummary",
        "isCommentPermissionFallback",
    ):
        assert expected in text

    update_call = "try {\n                await github.rest.issues.updateComment"
    create_call = "try {\n              await github.rest.issues.createComment"
    assert update_call in text
    assert create_call in text
    assert "throw error;" in text
    assert "core.setFailed('Missing pull request metadata.');" in text


def test_hc_task_handoff_queue_documents_non_blocking_marker_boundary() -> None:
    text = HANDOFF_QUEUE.read_text(encoding="utf-8")

    for expected in (
        "dedicated non-blocking PR marker workflow",
        "must not be a required check",
        "delay checks",
        "approve, reject, merge, label, assign, close, request reviewers",
        "create task authority",
        "replace live PR review",
        "replace maintainer decision",
        "Manual or handoff review-window notes remain audit records",
        "must not be overwritten by the automated workflow",
    ):
        assert expected in text
