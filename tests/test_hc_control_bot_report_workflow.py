from pathlib import Path

WORKFLOW = Path(".github/workflows/hc-control-bot-report.yml")


def _workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_hc_control_bot_report_includes_review_window_status() -> None:
    text = _workflow_text()

    for expected in (
        "## HC Review Window Status",
        "Head SHA:",
        "Observed at:",
        "Eligible after:",
        "waiting for late Codex review/comments before HC Trust Engineer may report merge-readiness",
        "Merge still requires final HC Trust Engineer review and explicit maintainer command.",
        "GITHUB_STEP_SUMMARY",
        "hc-review-window-status.md",
    ):
        assert expected in text


def test_hc_control_bot_report_preserves_review_window_advisory_boundaries() -> None:
    text = _workflow_text()

    for expected in (
        "Checks are not delayed by this timer.",
        "advisory_only=true",
        "public_safe=true",
        "truth_guarantee=false",
        "human final authority remains required",
    ):
        assert expected in text

    for forbidden in (
        "pull-requests: write",
        "contents: write",
        "actions: write",
        "checks: write",
        "issues: write",
        "issues.addLabels",
        "pulls.requestReviewers",
        "pulls.createReview",
        "pulls.merge",
    ):
        assert forbidden not in text


def test_hc_control_bot_report_includes_stale_baseline_scanner_section() -> None:
    text = _workflow_text()

    for expected in (
        "## HC Stale Baseline Scanner",
        "python scripts/hc_stale_baseline_report.py --markdown",
        "hc-stale-baseline-scanner.md",
        "This scanner compares documentation against repository-declared baselines.",
        "It does not fetch latest upstream versions.",
        "CI/checks are evidence, not trust authority.",
        "Human review remains final.",
        "The report-only HC stale baseline scanner exited non-zero",
        "GITHUB_STEP_SUMMARY",
    ):
        assert expected in text


def test_hc_control_bot_report_preserves_stale_baseline_advisory_boundaries() -> None:
    text = _workflow_text()

    for expected in (
        "advisory_only=true",
        "public_safe=true",
        "truth_guarantee=false",
        "human_review_required=true",
        "approval_authority=false",
        "merge_authority=false",
    ):
        assert expected in text

    for forbidden in (
        "--fail-on-missing-boundary",
        "pull-requests: write",
        "contents: write",
        "actions: write",
        "checks: write",
        "issues: write",
        "issues.addLabels",
        "pulls.requestReviewers",
        "pulls.createReview",
        "pulls.merge",
    ):
        assert forbidden not in text
