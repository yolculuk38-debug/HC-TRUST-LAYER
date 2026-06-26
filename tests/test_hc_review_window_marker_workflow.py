from pathlib import Path

WORKFLOW = Path(".github/workflows/hc-review-window-marker.yml")


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


def test_hc_review_window_marker_updates_existing_marker() -> None:
    text = _workflow_text()

    assert "<!-- hc-review-window -->" in text
    assert "issues.listComments" in text
    assert "issues.updateComment" in text
    assert "issues.createComment" in text
    assert "existing.length > 0" in text
    assert "90 * 1000" in text
