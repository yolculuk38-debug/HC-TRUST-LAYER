#!/usr/bin/env python3
"""Deterministic repository inventory reporter for HC project control.

The reporter is local and report-only. It classifies repository files,
connects obvious source/test anchors, and orders entries by last Git commit
metadata when available.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SKIP_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
DEFAULT_ROOTS = (
    ".github",
    "docs",
    "examples",
    "legacy",
    "records",
    "schema",
    "scripts",
    "src",
    "tests",
    "validators",
    "policy",
    "signatures",
    "federation",
)
ROOT_FILES = (
    "AGENTS.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "HC_BOOTSTRAP.md",
    "LICENSE",
    "README.md",
    "ROADMAP.md",
    "SECURITY.md",
    "pyproject.toml",
    "requirements.txt",
    "test_integration.py",
)
PROTECTED_PREFIXES = (
    ".github/workflows/",
    "records/",
    "schema/",
    "validators/",
    "policy/",
    "signatures/",
    "federation/",
    "canonical/",
)
PROTECTED_FILES = {
    "CODEOWNERS",
    ".github/CODEOWNERS",
    "protocol-graph.json",
    "verification-map.json",
    "trust-kernel-index.json",
}


@dataclass(frozen=True)
class InventoryEntry:
    path: str
    category: str
    lifecycle: str
    owner_role: str
    protected_surface: bool
    direct_test_anchor: str | None
    last_commit_iso: str | None
    last_commit_sha: str | None
    last_commit_subject: str | None
    last_commit_author_name: str | None
    last_commit_committer_name: str | None
    last_commit_pr_number: int | None
    last_commit_url: str | None
    review_order: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "category": self.category,
            "lifecycle": self.lifecycle,
            "owner_role": self.owner_role,
            "protected_surface": self.protected_surface,
            "direct_test_anchor": self.direct_test_anchor,
            "last_commit_iso": self.last_commit_iso,
            "last_commit_sha": self.last_commit_sha,
            "last_commit_subject": self.last_commit_subject,
            "last_commit_author_name": self.last_commit_author_name,
            "last_commit_committer_name": self.last_commit_committer_name,
            "last_commit_pr_number": self.last_commit_pr_number,
            "last_commit_url": self.last_commit_url,
            "review_order": self.review_order,
        }


def _repo_relative(repo_root: Path, path: Path) -> str:
    return path.resolve().relative_to(repo_root.resolve()).as_posix()


def _is_skipped(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def _iter_inventory_files(repo_root: Path, roots: tuple[str, ...]) -> list[Path]:
    files: list[Path] = []
    for root_name in roots:
        root = repo_root / root_name
        if root.is_file() and not _is_skipped(root):
            files.append(root)
        elif root.is_dir():
            files.extend(path for path in root.rglob("*") if path.is_file() and not _is_skipped(path))
    for root_file in ROOT_FILES:
        path = repo_root / root_file
        if path.is_file() and path not in files:
            files.append(path)
    return sorted(files, key=lambda path: _repo_relative(repo_root, path))


def _git_remote_commit_url(repo_root: Path, sha: str | None) -> str | None:
    if not sha:
        return None
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=repo_root,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    remote = result.stdout.strip()
    if result.returncode != 0 or not remote:
        return None
    match = re.match(r"(?:https://github\.com/|git@github\.com:)([^/]+)/([^/]+?)(?:\.git)?$", remote)
    if not match:
        return None
    owner, repo = match.groups()
    return f"https://github.com/{owner}/{repo}/commit/{sha}"


def _infer_pr_number(subject: str | None) -> int | None:
    if not subject:
        return None
    match = re.search(r"\(#(\d+)\)\s*$", subject)
    if not match:
        return None
    return int(match.group(1))


def _git_last_commit(
    repo_root: Path, relative_path: str
) -> tuple[str | None, str | None, str | None, str | None, str | None, int | None, str | None]:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI%x1f%H%x1f%s%x1f%an%x1f%cn", "--", relative_path],
            cwd=repo_root,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None, None, None, None, None, None, None
    output = result.stdout.strip()
    if result.returncode != 0 or not output:
        return None, None, None, None, None, None, None
    parts = output.split("\x1f", 4)
    if len(parts) != 5:
        return None, None, None, None, None, None, None
    commit_iso, sha, subject, author_name, committer_name = parts
    return (
        commit_iso,
        sha,
        subject,
        author_name,
        committer_name,
        _infer_pr_number(subject),
        _git_remote_commit_url(repo_root, sha),
    )


def _protected_surface(relative_path: str) -> bool:
    return relative_path in PROTECTED_FILES or relative_path.startswith(PROTECTED_PREFIXES)


def _category(relative_path: str) -> str:
    if relative_path.startswith(".github/workflows/"):
        return "github_workflow"
    if relative_path.startswith(".github/"):
        return "github_configuration"
    if relative_path.startswith("legacy/"):
        return "legacy_test"
    if relative_path.startswith("tests/") or relative_path == "test_integration.py":
        return "test"
    if relative_path.startswith("src/hc_trust/"):
        return "trust_layer_source"
    if relative_path.startswith("src/hc_runtime/"):
        return "runtime_source"
    if relative_path.startswith("src/"):
        return "source"
    if relative_path.startswith("scripts/"):
        return "operator_script"
    if relative_path.startswith("docs/project-control/"):
        return "project_control_doc"
    if relative_path.startswith("docs/"):
        return "documentation"
    if relative_path.startswith("examples/"):
        return "example"
    if relative_path.startswith("records/"):
        return "record"
    if relative_path.startswith("schema/"):
        return "schema"
    if relative_path.startswith("validators/"):
        return "validator"
    if relative_path.startswith("policy/"):
        return "policy"
    if relative_path.startswith("signatures/"):
        return "signature_material"
    if relative_path.startswith("federation/"):
        return "federation"
    if relative_path.endswith((".md", ".txt")):
        return "root_documentation"
    if relative_path.endswith((".toml", ".yml", ".yaml", ".json")):
        return "root_configuration"
    return "other"


def _owner_role(category: str, protected: bool) -> str:
    if protected:
        return "protected-surface-reviewer"
    if category in {"trust_layer_source", "record", "schema", "validator", "policy", "signature_material", "federation"}:
        return "trust-layer-reviewer"
    if category == "runtime_source":
        return "runtime-reviewer"
    if category in {"test", "legacy_test"}:
        return "test-reviewer"
    if category in {"github_workflow", "github_configuration"}:
        return "governance-reviewer"
    if category in {"operator_script", "project_control_doc"}:
        return "operator-reviewer"
    return "docs-or-general-reviewer"


def _lifecycle(category: str, protected: bool, direct_test_anchor: str | None) -> str:
    if protected:
        return "protected_review_required"
    if category == "legacy_test":
        return "legacy_test_support"
    if category == "test":
        return "test_support"
    if direct_test_anchor:
        return "active_with_test_anchor"
    if category in {"documentation", "project_control_doc", "root_documentation", "example"}:
        return "docs_or_example_support"
    if category in {"operator_script", "source", "runtime_source", "trust_layer_source"}:
        return "review_needed_without_direct_test_anchor"
    return "inventory_only_review_needed"


def _reference_tokens(relative_path: str) -> set[str]:
    path = Path(relative_path)
    stem = path.stem
    tokens = {stem}
    if relative_path.startswith("src/"):
        tokens.add(".".join(path.with_suffix("").parts[1:]))
    return tokens


def _test_anchor(repo_root: Path, relative_path: str, all_paths: set[str]) -> str | None:
    if not relative_path.endswith(".py") or relative_path.startswith("tests/"):
        return None
    stem = Path(relative_path).stem
    exact_candidates = [
        f"tests/test_{stem}.py",
        f"tests/runtime/test_{stem}.py",
        f"tests/test_{stem}_core.py",
    ]
    for candidate in exact_candidates:
        if candidate in all_paths:
            return candidate

    prefix_candidates = sorted(
        path
        for path in all_paths
        if path.startswith("tests/") and Path(path).name.startswith(f"test_{stem}_") and path.endswith(".py")
    )
    if prefix_candidates:
        return prefix_candidates[0]

    reference_tokens = _reference_tokens(relative_path)
    reference_candidates: list[tuple[int, str]] = []
    for test_path in sorted(path for path in all_paths if path.startswith("tests/") and path.endswith(".py")):
        try:
            test_text = (repo_root / test_path).read_text(encoding="utf-8")
        except OSError:
            continue
        reference_count = sum(test_text.count(token) for token in reference_tokens)
        if reference_count:
            reference_candidates.append((-reference_count, test_path))
    if reference_candidates:
        return sorted(reference_candidates)[0][1]
    return None


def build_inventory(repo_root: Path, roots: tuple[str, ...] = DEFAULT_ROOTS) -> dict[str, Any]:
    resolved_root = repo_root.resolve()
    files = _iter_inventory_files(resolved_root, roots)
    all_paths = {_repo_relative(resolved_root, path) for path in files}
    raw_entries: list[tuple[str, InventoryEntry]] = []
    categories: dict[str, int] = {}
    lifecycles: dict[str, int] = {}

    for path in files:
        relative_path = _repo_relative(resolved_root, path)
        category = _category(relative_path)
        protected = _protected_surface(relative_path)
        direct_test_anchor = _test_anchor(resolved_root, relative_path, all_paths)
        lifecycle = _lifecycle(category, protected, direct_test_anchor)
        (
            last_commit_iso,
            last_commit_sha,
            last_commit_subject,
            last_commit_author_name,
            last_commit_committer_name,
            last_commit_pr_number,
            last_commit_url,
        ) = _git_last_commit(resolved_root, relative_path)
        categories[category] = categories.get(category, 0) + 1
        lifecycles[lifecycle] = lifecycles.get(lifecycle, 0) + 1
        raw_entries.append(
            (
                relative_path,
                InventoryEntry(
                    path=relative_path,
                    category=category,
                    lifecycle=lifecycle,
                    owner_role=_owner_role(category, protected),
                    protected_surface=protected,
                    direct_test_anchor=direct_test_anchor,
                    last_commit_iso=last_commit_iso,
                    last_commit_sha=last_commit_sha,
                    last_commit_subject=last_commit_subject,
                    last_commit_author_name=last_commit_author_name,
                    last_commit_committer_name=last_commit_committer_name,
                    last_commit_pr_number=last_commit_pr_number,
                    last_commit_url=last_commit_url,
                    review_order=0,
                ),
            )
        )

    ordered = sorted(
        (entry for _, entry in raw_entries),
        key=lambda entry: (entry.last_commit_iso or "", entry.path),
        reverse=True,
    )
    ordered = [entry.__class__(**{**entry.to_dict(), "review_order": index + 1}) for index, entry in enumerate(ordered)]

    return {
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "inventory_only": True,
        "modifies_repository": False,
        "order": "last_git_commit_desc_then_path",
        "roots_scanned": [root for root in roots if (resolved_root / root).exists()],
        "file_count": len(ordered),
        "categories": dict(sorted(categories.items())),
        "lifecycles": dict(sorted(lifecycles.items())),
        "files": [entry.to_dict() for entry in ordered],
    }


def _entries_for_view(files: list[dict[str, Any]], view: str) -> list[dict[str, Any]]:
    if view == "all":
        return files
    if view == "tests":
        return [entry for entry in files if entry["category"] == "test"]
    if view == "source":
        return [
            entry
            for entry in files
            if entry["category"] in {"source", "runtime_source", "trust_layer_source", "operator_script"}
        ]
    if view == "workflows":
        return [entry for entry in files if entry["category"] == "github_workflow"]
    if view == "docs":
        return [
            entry
            for entry in files
            if entry["category"] in {"documentation", "project_control_doc", "root_documentation", "example"}
        ]
    if view == "protected":
        return [
            entry
            for entry in files
            if entry["protected_surface"]
            or entry["category"] in {"record", "schema", "validator", "policy", "signature_material", "federation"}
        ]
    if view == "review_needed":
        return sorted(
            (
                entry
                for entry in files
                if entry["lifecycle"]
                in {
                    "protected_review_required",
                    "review_needed_without_direct_test_anchor",
                    "inventory_only_review_needed",
                }
            ),
            key=lambda entry: (
                0 if entry["lifecycle"] == "protected_review_required" else 1,
                0 if entry["protected_surface"] else 1,
                entry["review_order"],
            ),
        )
    raise ValueError(f"Unknown inventory view: {view}")


def _append_entries_table(lines: list[str], entries: list[dict[str, Any]]) -> None:
    lines.extend([
        "",
        "| Order | Path | Category | Lifecycle | Protected | Test anchor | Actor | PR | Last commit |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
    ])
    if not entries:
        lines.append("|  | _No files in this view._ |  |  |  |  |  |  |  |")
        return
    for entry in entries:
        test_anchor = entry["direct_test_anchor"] or ""
        actor = entry["last_commit_author_name"] or ""
        pr_number = entry["last_commit_pr_number"]
        pr = f"#{pr_number}" if pr_number is not None else ""
        last_commit = entry["last_commit_iso"] or ""
        if entry["last_commit_sha"]:
            last_commit = f"{last_commit} `{entry['last_commit_sha'][:12]}`".strip()
        lines.append(
            f"| {entry['review_order']} | `{entry['path']}` | {entry['category']} | "
            f"{entry['lifecycle']} | {str(entry['protected_surface']).lower()} | "
            f"`{test_anchor}` | {actor} | {pr} | {last_commit} |"
        )


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# HC Repository Inventory Ledger",
        "",
        "Status: generated advisory inventory.",
        "",
        f"File count: {report['file_count']}",
        "",
        "## Category summary",
        "",
        "| Category | Count |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {category} | {count} |" for category, count in report["categories"].items())
    lines.extend([
        "",
        "## Lifecycle summary",
        "",
        "| Lifecycle | Count |",
        "| --- | ---: |",
    ])
    lines.extend(f"| {lifecycle} | {count} |" for lifecycle, count in report["lifecycles"].items())
    view_sections = [
        ("Latest changes — all files", "all"),
        ("Tests — newest first", "tests"),
        ("Source — newest first", "source"),
        ("Workflows — newest first", "workflows"),
        ("Docs — newest first", "docs"),
        ("Records / schema / protected — newest first", "protected"),
        ("Review-needed — priority first", "review_needed"),
    ]
    for heading, view in view_sections:
        lines.extend(["", f"## {heading}"])
        _append_entries_table(lines, _entries_for_view(report["files"], view))
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build an advisory HC repository inventory ledger.")
    parser.add_argument("repo_root", nargs="?", default=".")
    parser.add_argument("--format", choices=("json", "md"), default="json")
    parser.add_argument("--root", action="append", dest="scan_roots")
    args = parser.parse_args(argv)

    roots = tuple(args.scan_roots) if args.scan_roots else DEFAULT_ROOTS
    report = build_inventory(Path(args.repo_root), roots=roots)
    if args.format == "md":
        print(render_markdown(report))
    else:
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
