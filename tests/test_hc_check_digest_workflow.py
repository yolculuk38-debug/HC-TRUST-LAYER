from pathlib import Path

WORKFLOW = Path(".github/workflows/hc-check-digest.yml")


def _workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_hc_check_digest_workflow_keeps_read_only_permissions() -> None:
    text = _workflow_text()

    for permission in (
        "contents: read",
        "actions: read",
        "checks: read",
        "pull-requests: read",
    ):
        assert permission in text
    for forbidden_permission in (
        "contents: write",
        "actions: write",
        "checks: write",
        "pull-requests: write",
        "issues: write",
    ):
        assert forbidden_permission not in text


def test_hc_check_digest_avoids_concurrency_cancellation() -> None:
    text = _workflow_text()

    assert "concurrency:" not in text
    assert "cancel-in-progress" not in text


def test_hc_check_digest_self_trigger_skips_before_steps() -> None:
    text = _workflow_text()

    assert "github.event_name != 'check_run'" in text
    assert "!contains(github.event.check_run.name, 'HC Check Digest')" in text
    assert "!contains(github.event.check_run.name, 'Build advisory PR health digest')" in text
    assert "github.event_name != 'workflow_run'" in text
    assert "github.event.workflow_run.name != 'HC Check Digest'" in text


def test_hc_check_digest_workflow_still_publishes_required_outputs() -> None:
    text = _workflow_text()

    for required_output in (
        "hc-check-digest.json",
        "hc-check-digest.md",
        "${GITHUB_STEP_SUMMARY}",
        "name: hc-check-digest",
    ):
        assert required_output in text
