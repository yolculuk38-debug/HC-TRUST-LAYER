from pathlib import Path

WORKFLOW = Path(".github/workflows/hc-review-window-marker.yml")
HANDOFF_QUEUE = Path("docs/project-control/hc-task-handoff-queue.md")


def _workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_hc_review_window_marker_is_advisory_and_comment_only() -> None:
    text = _workflow_text()

    assert "name: HC Review Window Marker" in text
    assert "workflow_dispatch:" in text
    assert "pr_number:" in text
    assert "head_sha:" in text
    assert "pull_request:" not in text
    assert "pull_request_target:" not in text
    assert "automatic PR triggers are disabled" in text
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


def test_hc_review_window_marker_consumes_workflow_dispatch_payload_inputs() -> None:
    text = _workflow_text()

    assert "const workflowInputs = context.payload.inputs || {};" in text
    assert "const inputPrNumber = workflowInputs.pr_number || '';" in text
    assert "const inputHeadSha = workflowInputs.head_sha || '';" in text
    assert "core.getInput('pr_number')" not in text
    assert "core.getInput('head_sha')" not in text
    assert "const prNumber = pr ? pr.number : Number(inputPrNumber);" in text
    assert "const headSha = pr ? pr.head.sha : (inputHeadSha || context.sha);" in text


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
    assert "Missing pull request metadata or manual pr_number input." in text


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
