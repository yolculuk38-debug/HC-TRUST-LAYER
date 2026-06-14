import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_ruleset_readiness import build_report, render_markdown


def test_ruleset_readiness_reports_boundaries_and_workflow_presence(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / ".github" / "workflows").mkdir(parents=True)
    (repo / ".github" / "workflows" / "validate.yml").write_text("name: validate\n", encoding="utf-8")

    report = build_report(repo)

    assert report["advisory_only"] is True
    assert report["public_safe"] is True
    assert report["truth_guarantee"] is False
    assert report["human_review_required"] is True
    assert report["settings_verified_locally"] is False
    assert report["github_api_called"] is False
    assert report["mutates_repository_settings"] is False
    assert ".github/workflows/" in report["protected_surfaces"]
    by_name = {item["name"]: item for item in report["expected_required_checks"]}
    assert by_name["validate"]["workflow_exists"] is True
    assert by_name["terminology"]["workflow_exists"] is False


def test_ruleset_readiness_markdown_is_operator_readable(tmp_path: Path) -> None:
    report = build_report(tmp_path)
    markdown = render_markdown(report)

    assert "# HC GitHub Ruleset Readiness Report" in markdown
    assert "truth_guarantee=false" in markdown
    assert "settings_verified_locally=false" in markdown
    assert "GitHub branch protection and ruleset enforcement cannot be verified" in markdown
