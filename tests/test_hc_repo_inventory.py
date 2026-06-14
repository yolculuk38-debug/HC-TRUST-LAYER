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
    assert "## Files, newest first" in markdown
    assert "`src/b.py`" in markdown or "`docs/a.md`" in markdown
