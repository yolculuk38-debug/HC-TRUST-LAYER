import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from hc_repo_inventory import build_inventory, render_markdown


def test_inventory_classifies_source_test_docs_and_workflow(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "src" / "hc_trust").mkdir(parents=True)
    (repo / "tests").mkdir()
    (repo / "docs" / "project-control").mkdir(parents=True)
    (repo / ".github" / "workflows").mkdir(parents=True)

    (repo / "src" / "hc_trust" / "verification_package.py").write_text("", encoding="utf-8")
    (repo / "tests" / "test_verification_package.py").write_text("", encoding="utf-8")
    (repo / "docs" / "project-control" / "state.md").write_text("", encoding="utf-8")
    (repo / ".github" / "workflows" / "inventory.yml").write_text("", encoding="utf-8")

    report = build_inventory(repo)
    by_path = {entry["path"]: entry for entry in report["files"]}

    assert report["advisory_only"] is True
    assert report["inventory_only"] is True
    assert report["modifies_repository"] is False
    assert by_path["src/hc_trust/verification_package.py"]["category"] == "trust_layer_source"
    assert by_path["src/hc_trust/verification_package.py"]["direct_test_anchor"] == "tests/test_verification_package.py"
    assert by_path["tests/test_verification_package.py"]["lifecycle"] == "test_support"
    assert by_path["docs/project-control/state.md"]["category"] == "project_control_doc"
    assert by_path[".github/workflows/inventory.yml"]["protected_surface"] is True
    assert by_path[".github/workflows/inventory.yml"]["owner_role"] == "protected-surface-reviewer"


def test_inventory_orders_entries_and_renders_markdown(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "src").mkdir()
    (repo / "docs").mkdir()
    (repo / "src" / "b.py").write_text("", encoding="utf-8")
    (repo / "docs" / "a.md").write_text("", encoding="utf-8")

    report = build_inventory(repo)
    orders = [entry["review_order"] for entry in report["files"]]
    markdown = render_markdown(report)

    assert orders == [1, 2]
    assert "# HC Repository Inventory Ledger" in markdown
    assert "## Latest changes — all files" in markdown
    assert "## Tests — newest first" in markdown
    assert "## Source — newest first" in markdown
    assert "## Workflows — newest first" in markdown
    assert "## Docs — newest first" in markdown
    assert "## Records / schema / protected — newest first" in markdown
    assert "## Review-needed — priority first" in markdown
    assert "| Order | Path | Category | Lifecycle | Protected | Test anchor | Actor | PR | Last commit |" in markdown
    assert "`src/b.py`" in markdown or "`docs/a.md`" in markdown


def test_inventory_matches_prefix_test_anchor(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "src" / "hc_trust").mkdir(parents=True)
    (repo / "tests").mkdir()

    (repo / "src" / "hc_trust" / "verification_package.py").write_text("", encoding="utf-8")
    (repo / "tests" / "test_verification_package_hash_core.py").write_text("", encoding="utf-8")

    report = build_inventory(repo)
    by_path = {entry["path"]: entry for entry in report["files"]}

    assert (
        by_path["src/hc_trust/verification_package.py"]["direct_test_anchor"]
        == "tests/test_verification_package_hash_core.py"
    )


def test_inventory_matches_reference_test_anchor(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "scripts").mkdir()
    (repo / "tests").mkdir()

    (repo / "scripts" / "check_pr_governance.py").write_text("", encoding="utf-8")
    (repo / "tests" / "test_pr_governance_preflight.py").write_text(
        'from importlib.util import spec_from_file_location\n'
        'SPEC = spec_from_file_location("check_pr_governance", MODULE_PATH)\n',
        encoding="utf-8",
    )

    report = build_inventory(repo)
    by_path = {entry["path"]: entry for entry in report["files"]}

    assert (
        by_path["scripts/check_pr_governance.py"]["direct_test_anchor"]
        == "tests/test_pr_governance_preflight.py"
    )


def test_inventory_entries_include_actor_pr_trace_fields(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "src").mkdir()
    (repo / "src" / "example.py").write_text("", encoding="utf-8")

    report = build_inventory(repo)

    assert report["files"]
    for entry in report["files"]:
        assert "last_commit_author_name" in entry
        assert "last_commit_committer_name" in entry
        assert "last_commit_pr_number" in entry
        assert "last_commit_url" in entry


def test_inventory_reads_git_actor_pr_and_commit_url(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "src").mkdir()
    (repo / "src" / "trace.py").write_text("print('trace')\n", encoding="utf-8")

    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)
    subprocess.run(["git", "config", "user.name", "HC Test Author"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "hc-test@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "add", "src/trace.py"], cwd=repo, check=True)
    subprocess.run(
        ["git", "commit", "-m", "Add trace inventory evidence (#123)"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        ["git", "remote", "add", "origin", "https://github.com/example/repo.git"],
        cwd=repo,
        check=True,
    )
    sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    report = build_inventory(repo)
    by_path = {entry["path"]: entry for entry in report["files"]}
    entry = by_path["src/trace.py"]

    assert entry["last_commit_author_name"] == "HC Test Author"
    assert entry["last_commit_committer_name"] == "HC Test Author"
    assert entry["last_commit_pr_number"] == 123
    assert entry["last_commit_url"] == f"https://github.com/example/repo/commit/{sha}"


def test_inventory_source_view_includes_operator_scripts(tmp_path: Path) -> None:
    repo = tmp_path
    (repo / "scripts").mkdir()
    (repo / "scripts" / "hc_operator.py").write_text("", encoding="utf-8")

    markdown = render_markdown(build_inventory(repo))

    source_section = markdown.split("## Source — newest first", 1)[1].split("## Workflows — newest first", 1)[0]
    assert "`scripts/hc_operator.py`" in source_section
    assert "operator_script" in source_section
