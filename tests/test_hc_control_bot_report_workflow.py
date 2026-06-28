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


def test_stale_baseline_scanner_uses_trusted_base_implementation() -> None:
    text = _workflow_text()

    assert "Check out trusted base revision" in text
    assert "ref: ${{ github.event.pull_request.base.sha }}" in text
    assert "path: trusted-base" in text
    assert "python trusted-base/scripts/hc_stale_baseline_report.py" in text
    assert "Scanner implementation: trusted base revision" in text


def test_stale_baseline_scanner_scans_pr_docs_as_data_with_base_baselines() -> None:
    text = _workflow_text()

    for expected in (
        "Check out PR head documentation as data",
        "ref: ${{ github.event.pull_request.head.sha }}",
        "path: pr-docs-data",
        "find docs -type f -name '*.md'",
        "cp \"pr-docs-data/${doc}\" \"${scan_root}/${doc}\"",
        "Documentation scan input: proposed PR documentation from docs/**/*.md copied as data only.",
        "Trusted baseline inputs: base pyproject.toml, requirements.txt, and .github/workflows/** when present.",
        "cp -R trusted-base/.github/workflows",
        "--repo-root \"${scan_root}\" --markdown",
    ):
        assert expected in text

    assert "python pr-docs-data/" not in text
    assert "bash pr-docs-data/" not in text
    assert "./pr-docs-data/" not in text


def test_stale_baseline_scanner_section_is_advisory_report_only() -> None:
    text = _workflow_text()

    for expected in (
        "## HC Stale Baseline Scanner",
        "Boundary: advisory/report-only; missing-boundary findings do not fail CI by default.",
        "Boundary: no PR-branch scripts, workflows, or governance files are executed or trusted as instructions.",
        "human_review_required=true",
        "Warning: trusted stale baseline scanner exited with status",
        "This is a warning only, not a trust claim.",
        "exit 0",
    ):
        assert expected in text

    assert "--fail-on-missing-boundary" not in text


def test_hc_control_bot_report_has_no_approval_merge_comment_or_label_authority() -> None:
    text = _workflow_text()

    forbidden = (
        "pull-requests: write",
        "contents: write",
        "issues: write",
        "gh pr review",
        "gh pr merge",
        "gh pr edit",
        "gh issue comment",
        "actions/github-script",
        "createComment",
        "addLabels",
        "requestReviewers",
        "createReview",
        "pulls.merge",
        "gh api repos/",
    )
    for token in forbidden:
        assert token not in text
