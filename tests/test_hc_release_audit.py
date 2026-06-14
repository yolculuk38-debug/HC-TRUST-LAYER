import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from hc_release_audit import build_report, render_markdown


def test_release_audit_reports_boundaries_without_mutation(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "docs" / "project-control").mkdir(parents=True)
    (repo / "CHANGELOG.md").write_text("# Changelog\n\n- See #123.\n", encoding="utf-8")
    (repo / "VERSION").write_text("0.1.0\n", encoding="utf-8")
    (repo / "docs" / "project-control" / "task-ledger.md").write_text("# Task Ledger\n", encoding="utf-8")

    report = build_report(repo)

    assert report["advisory_only"] is True
    assert report["public_safe"] is True
    assert report["truth_guarantee"] is False
    assert report["publishes_release"] is False
    assert report["creates_tags"] is False
    assert report["modifies_changelog"] is False
    assert report["human_review_required"] is True
    assert report["merge_ready"] is False
    assert report["changelog_evidence"] is True
    assert report["task_ledger_evidence"] is True
    assert report["pr_reference_evidence"] is True


def test_release_audit_detects_changed_release_files_and_missing_pr_reference(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "docs" / "project-control").mkdir(parents=True)
    (repo / "CHANGELOG.md").write_text("# Changelog\n", encoding="utf-8")
    (repo / "VERSION").write_text("0.1.0\n", encoding="utf-8")
    (repo / "docs" / "project-control" / "task-ledger.md").write_text("# Task Ledger\n", encoding="utf-8")
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)
    subprocess.run(["git", "config", "user.name", "HC Test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "hc@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-m", "baseline"], cwd=repo, check=True, capture_output=True, text=True)
    (repo / "CHANGELOG.md").write_text("# Changelog\n\n- Release note without PR reference.\n", encoding="utf-8")

    report = build_report(repo)

    assert report["release_files_changed"] == ["CHANGELOG.md"]
    assert report["pr_reference_evidence"] is False
    assert "pr_reference_evidence" in report["missing_evidence"]


def test_release_audit_markdown_is_operator_readable(tmp_path: Path) -> None:
    report = build_report(tmp_path)
    markdown = render_markdown(report)

    assert "# HC Release Audit Report" in markdown
    assert "truth_guarantee=false" in markdown
    assert "merge_ready=false" in markdown
