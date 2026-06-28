from scripts.hc_workflow_taxonomy_drift_report import analyze_changed_paths, render_markdown


def _report(paths: list[str]) -> str:
    return render_markdown(analyze_changed_paths(paths))


def test_no_workflow_changes_is_ok() -> None:
    report = _report(["README.md"])

    assert "status: ok" in report
    assert "No workflow file changes detected." in report
    assert "Changed workflow files:\n- None" in report


def test_workflow_changed_without_taxonomy_warns() -> None:
    report = _report([".github/workflows/foo.yml"])

    assert "status: warning" in report
    assert "Workflow files changed without workflow taxonomy update. Human review required." in report
    assert "advisory_only=true" in report
    assert "public_safe=true" in report
    assert "truth_guarantee=false" in report
    assert "human_review_required=true" in report
    assert "`.github/workflows/foo.yml`" in report
    assert "`docs/project-control/workflow-taxonomy.md`" in report
    assert "does not block merge" in report


def test_workflow_changed_with_taxonomy_is_ok() -> None:
    report = _report([".github/workflows/foo.yml", "docs/project-control/workflow-taxonomy.md"])

    assert "status: ok" in report
    assert "Workflow taxonomy update was detected" in report
    assert "human_review_required=true" in report


def test_multiple_workflow_files_warning_lists_all() -> None:
    report = _report([".github/workflows/b.yml", ".github/workflows/a.yml"])

    assert "status: warning" in report
    assert report.index("`.github/workflows/a.yml`") < report.index("`.github/workflows/b.yml`")


def test_non_workflow_github_file_does_not_warn() -> None:
    report = _report([".github/dependabot.yml"])

    assert "status: ok" in report
    assert "status: warning" not in report


def test_empty_changed_file_list_is_ok() -> None:
    report = _report([])

    assert "status: ok" in report
    assert "Changed workflow files:\n- None" in report


def test_duplicate_paths_are_deduplicated() -> None:
    report = _report([".github/workflows/foo.yml", ".github/workflows/foo.yml"])

    assert report.count("`.github/workflows/foo.yml`") == 1


def test_windows_style_path_separators_are_normalized() -> None:
    report = _report([r".github\workflows\foo.yml"])

    assert "status: warning" in report
    assert "`.github/workflows/foo.yml`" in report
