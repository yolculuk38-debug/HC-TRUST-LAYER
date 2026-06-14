import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from hc_release_audit import build_report, render_markdown


def _init_repo(repo: Path) -> None:
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)
    subprocess.run(["git", "config", "user.name", "HC Test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "hc@example.invalid"], cwd=repo, check=True)


def _commit(repo: Path, message: str) -> str:
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-m", message], cwd=repo, check=True, capture_output=True, text=True)
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def _write_release_files(repo: Path, changelog: str) -> None:
    (repo / "docs" / "project-control").mkdir(parents=True)
    (repo / "CHANGELOG.md").write_text(changelog, encoding="utf-8")
    (repo / "VERSION").write_text("0.1.0\n", encoding="utf-8")
    (repo / "docs" / "project-control" / "task-ledger.md").write_text("# Task Ledger\n", encoding="utf-8")


def test_release_audit_reports_boundaries_without_mutation(tmp_path: Path) -> None:
    repo = tmp_path
    _write_release_files(repo, "# Changelog\n\n- See #123.\n")

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
    assert report["pr_reference_evidence"] is False


def test_release_audit_detects_worktree_release_file_without_current_reference(tmp_path: Path) -> None:
    repo = tmp_path
    _write_release_files(repo, "# Changelog\n")
    _init_repo(repo)
    _commit(repo, "baseline")
    (repo / "CHANGELOG.md").write_text("# Changelog\n\n- Current release note.\n", encoding="utf-8")

    report = build_report(repo)

    assert report["release_files_changed"] == ["CHANGELOG.md"]
    assert report["pr_reference_evidence"] is False
    assert "pr_reference_evidence" in report["missing_evidence"]


def test_release_audit_detects_committed_pr_range_without_current_reference(tmp_path: Path) -> None:
    repo = tmp_path
    _write_release_files(repo, "# Changelog\n\n- Historical #123.\n")
    _init_repo(repo)
    base_sha = _commit(repo, "baseline")
    (repo / "CHANGELOG.md").write_text("# Changelog\n\n- Historical #123.\n- Current release note.\n", encoding="utf-8")
    head_sha = _commit(repo, "release note")

    report = build_report(repo, base_ref=base_sha, head_ref=head_sha)

    assert report["diff_mode"] == "ref_range"
    assert report["release_files_changed"] == ["CHANGELOG.md"]
    assert report["pr_reference_evidence"] is False
    assert "pr_reference_evidence" in report["missing_evidence"]


def test_release_audit_accepts_explicit_current_pr_number(tmp_path: Path) -> None:
    repo = tmp_path
    _write_release_files(repo, "# Changelog\n")
    _init_repo(repo)
    base_sha = _commit(repo, "baseline")
    (repo / "CHANGELOG.md").write_text("# Changelog\n\n- Current release note.\n", encoding="utf-8")
    head_sha = _commit(repo, "release note")

    report = build_report(repo, base_ref=base_sha, head_ref=head_sha, pr_number="975")

    assert report["release_files_changed"] == ["CHANGELOG.md"]
    assert report["pr_reference_evidence"] is True
    assert "pr_reference_evidence" not in report["missing_evidence"]


def test_release_audit_ignores_unrelated_added_pr_references(tmp_path: Path) -> None:
    repo = tmp_path
    _write_release_files(repo, "# Changelog\n")
    (repo / "docs").mkdir(exist_ok=True)
    (repo / "docs" / "note.md").write_text("# Note\n", encoding="utf-8")
    _init_repo(repo)
    base_sha = _commit(repo, "baseline")
    (repo / "CHANGELOG.md").write_text("# Changelog\n\n- Current release note.\n", encoding="utf-8")
    (repo / "docs" / "note.md").write_text("# Note\n\n- Unrelated #999.\n", encoding="utf-8")
    head_sha = _commit(repo, "release note with unrelated ref")

    report = build_report(repo, base_ref=base_sha, head_ref=head_sha)

    assert report["release_files_changed"] == ["CHANGELOG.md"]
    assert report["pr_reference_evidence"] is False
    assert "pr_reference_evidence" in report["missing_evidence"]


def test_release_audit_markdown_is_operator_readable(tmp_path: Path) -> None:
    report = build_report(tmp_path)
    markdown = render_markdown(report)

    assert "# HC Release Audit Report" in markdown
    assert "truth_guarantee=false" in markdown
    assert "merge_ready=false" in markdown
