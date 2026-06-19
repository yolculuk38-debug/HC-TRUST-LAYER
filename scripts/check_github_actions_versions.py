#!/usr/bin/env python3
"""Deterministic stale GitHub Actions version guard for HC-TRUST-LAYER."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_WORKFLOWS_DIR = Path(".github/workflows")
USES_RE = re.compile(r"\buses:\s*([^\s#]+)")

# Explicit denylist for action major versions known to emit Node.js 20 runtime
# deprecation warnings in this repository. Keep this local and deterministic;
# Dependabot remains responsible for discovering routine upstream updates.
DEPRECATED_ACTIONS: dict[str, str] = {
    "actions/checkout@v4": "actions/checkout@v6",
    "actions/upload-artifact@v4": "actions/upload-artifact@v7",
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    reference: str
    replacement: str

    def render(self) -> str:
        return (
            f"ERROR: {self.path}:{self.line}: deprecated GitHub Action "
            f"'{self.reference}' detected; use '{self.replacement}'"
        )


def workflow_files(workflows_dir: Path) -> list[Path]:
    if not workflows_dir.exists():
        return []
    return sorted(
        path
        for pattern in ("*.yml", "*.yaml")
        for path in workflows_dir.glob(pattern)
        if path.is_file()
    )


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        match = USES_RE.search(line)
        if not match:
            continue
        reference = match.group(1).strip('"\'')
        replacement = DEPRECATED_ACTIONS.get(reference)
        if replacement:
            findings.append(Finding(path=path, line=line_no, reference=reference, replacement=replacement))
    return findings


def scan_workflows(workflows_dir: Path = DEFAULT_WORKFLOWS_DIR) -> list[Finding]:
    findings: list[Finding] = []
    for path in workflow_files(workflows_dir):
        findings.extend(scan_file(path))
    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check workflow files for explicitly deprecated GitHub Actions versions."
    )
    parser.add_argument(
        "--workflows-dir",
        type=Path,
        default=DEFAULT_WORKFLOWS_DIR,
        help="Directory containing GitHub Actions workflow .yml/.yaml files.",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    findings = scan_workflows(args.workflows_dir)
    if findings:
        for finding in findings:
            print(finding.render())
        print("ERROR: stale GitHub Actions versions detected")
        return 1
    print("OK: no explicitly deprecated GitHub Actions versions detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
