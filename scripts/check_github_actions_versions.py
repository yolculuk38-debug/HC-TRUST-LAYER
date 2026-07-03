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

# Explicit denylist for GitHub-maintained action versions known or expected to
# emit Node.js 20 runtime deprecation warnings in repository-controlled
# workflows. Keep this narrow, local, and deterministic; Dependabot remains
# responsible for discovering routine upstream updates.
DEPRECATED_ACTION_MAJORS: dict[tuple[str, str], str] = {
    ("actions/checkout", "v4"): "actions/checkout@v7",
    ("actions/checkout", "v5"): "actions/checkout@v7",
    ("actions/checkout", "v6"): "actions/checkout@v7",
    ("actions/upload-artifact", "v4"): "actions/upload-artifact@v7",
    ("actions/upload-artifact", "v5"): "actions/upload-artifact@v7",
    ("actions/upload-artifact", "v6"): "actions/upload-artifact@v7",
    ("actions/download-artifact", "v4"): "actions/download-artifact@v8",
    ("actions/download-artifact", "v5"): "actions/download-artifact@v8",
    ("actions/download-artifact", "v6"): "actions/download-artifact@v8",
    ("actions/download-artifact", "v7"): "actions/download-artifact@v8",
    ("actions/setup-python", "v4"): "actions/setup-python@v6",
    ("actions/setup-python", "v5"): "actions/setup-python@v6",
    ("github/codeql-action/init", "v3"): "github/codeql-action/init@v4",
    ("github/codeql-action/analyze", "v3"): "github/codeql-action/analyze@v4",
    ("github/codeql-action/upload-sarif", "v3"): "github/codeql-action/upload-sarif@v4",
}

# Same-major stale refs where a stable Node.js 24-compatible patch is required.
DEPRECATED_ACTION_REFS: dict[str, str] = {
    "actions/attest-build-provenance@v4": "actions/attest-build-provenance@v4.1.1",
    "actions/attest-build-provenance@v4.0.0": "actions/attest-build-provenance@v4.1.1",
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    reference: str
    deprecated_major: str
    replacement: str

    def render(self) -> str:
        return (
            f"ERROR: {self.path}:{self.line}: deprecated GitHub Action "
            f"'{self.reference}' detected for stale ref '{self.deprecated_major}'; "
            f"use '{self.replacement}'"
        )


def split_action_reference(reference: str) -> tuple[str, str] | None:
    if "@" not in reference:
        return None
    action, ref = reference.rsplit("@", 1)
    if not action or not ref:
        return None
    return action, ref


def matches_major(ref: str, major: str) -> bool:
    return ref == major or ref.startswith(f"{major}.")


def deprecated_replacement(reference: str) -> tuple[str, str] | None:
    exact_replacement = DEPRECATED_ACTION_REFS.get(reference)
    if exact_replacement is not None:
        return reference.rsplit("@", 1)[1], exact_replacement

    parsed = split_action_reference(reference)
    if parsed is None:
        return None
    action, ref = parsed
    for (deprecated_action, deprecated_major), replacement in DEPRECATED_ACTION_MAJORS.items():
        if action == deprecated_action and matches_major(ref, deprecated_major):
            return deprecated_major, replacement
    return None


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
        deprecated = deprecated_replacement(reference)
        if deprecated:
            deprecated_major, replacement = deprecated
            findings.append(
                Finding(
                    path=path,
                    line=line_no,
                    reference=reference,
                    deprecated_major=deprecated_major,
                    replacement=replacement,
                )
            )
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
