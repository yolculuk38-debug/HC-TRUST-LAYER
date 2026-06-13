#!/usr/bin/env python3
"""Deterministic local source inventory reporter for HC project control.

This script lists Python files under selected repository roots and classifies them
by path. It intentionally avoids network calls, LLM calls, subprocess execution,
repository writes, file deletion, file moves, workflow changes, GitHub actions,
secret reads, and authority-changing behavior.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_SCAN_ROOTS = ("src", "scripts", "tests")


@dataclass(frozen=True)
class SourceInventoryEntry:
    """Single inventory-only file classification."""

    path: str
    category: str
    status: str
    notes: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "category": self.category,
            "status": self.status,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class SourceInventoryReport:
    """Machine-readable advisory source inventory report."""

    advisory_only: bool
    public_safe: bool
    truth_guarantee: bool
    inventory_only: bool
    modifies_repository: bool
    repo_root: str
    roots_scanned: list[str]
    python_file_count: int
    categories: dict[str, int]
    files: list[SourceInventoryEntry]

    def to_dict(self) -> dict[str, Any]:
        return {
            "advisory_only": self.advisory_only,
            "public_safe": self.public_safe,
            "truth_guarantee": self.truth_guarantee,
            "inventory_only": self.inventory_only,
            "modifies_repository": self.modifies_repository,
            "repo_root": self.repo_root,
            "roots_scanned": self.roots_scanned,
            "python_file_count": self.python_file_count,
            "categories": dict(sorted(self.categories.items())),
            "files": [entry.to_dict() for entry in self.files],
        }


def _repo_relative(repo_root: Path, path: Path) -> str:
    return path.resolve().relative_to(repo_root.resolve()).as_posix()


def _classify_path(relative_path: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    parts = relative_path.split("/")

    if relative_path.startswith("tests/"):
        return "test_support", notes
    if relative_path.startswith("scripts/"):
        return "operator_support", notes
    if relative_path.startswith("src/hc_runtime/"):
        return "runtime_implementation", notes
    if relative_path.startswith("src/hc_trust/"):
        return "trust_layer_implementation", notes
    if relative_path.startswith("src/security/"):
        notes.append("security_adjacent_review_recommended")
        return "security_adjacent", notes
    if "experimental" in parts or "archive" in parts:
        notes.append("manual_review_recommended")
        return "experimental_or_archival", notes
    if relative_path.startswith("src/"):
        return "source_implementation", notes
    return "other_python", notes


def _iter_python_files(repo_root: Path, scan_roots: tuple[str, ...]) -> list[Path]:
    files: list[Path] = []
    for root_name in scan_roots:
        root = repo_root / root_name
        if not root.exists() or not root.is_dir():
            continue
        files.extend(path for path in root.rglob("*.py") if path.is_file())
    return sorted(files, key=lambda path: _repo_relative(repo_root, path))


def build_source_inventory(repo_root: Path, scan_roots: tuple[str, ...] = DEFAULT_SCAN_ROOTS) -> SourceInventoryReport:
    """Build an advisory source inventory without modifying repository files."""

    resolved_root = repo_root.resolve()
    entries: list[SourceInventoryEntry] = []
    categories: dict[str, int] = {}

    for file_path in _iter_python_files(resolved_root, scan_roots):
        relative_path = _repo_relative(resolved_root, file_path)
        category, notes = _classify_path(relative_path)
        categories[category] = categories.get(category, 0) + 1
        entries.append(
            SourceInventoryEntry(
                path=relative_path,
                category=category,
                status="inventory_only",
                notes=notes,
            )
        )

    roots_scanned = [root for root in scan_roots if (resolved_root / root).exists()]
    return SourceInventoryReport(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        inventory_only=True,
        modifies_repository=False,
        repo_root=str(resolved_root),
        roots_scanned=roots_scanned,
        python_file_count=len(entries),
        categories=categories,
        files=entries,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build an advisory HC source inventory report.")
    parser.add_argument("repo_root", nargs="?", default=".", help="Repository root to scan. Defaults to current directory.")
    parser.add_argument(
        "--root",
        action="append",
        dest="scan_roots",
        help="Repository-relative root to scan. Can be passed multiple times. Defaults to src, scripts, tests.",
    )
    args = parser.parse_args(argv)

    scan_roots = tuple(args.scan_roots) if args.scan_roots else DEFAULT_SCAN_ROOTS
    report = build_source_inventory(Path(args.repo_root), scan_roots=scan_roots)
    print(json.dumps(report.to_dict(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
