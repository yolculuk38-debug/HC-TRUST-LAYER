#!/usr/bin/env python3
"""Terminology guard for HC-TRUST-LAYER documentation."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable

FORBIDDEN_PHRASES = [
    "proves truth",
    "guarantees truth",
    "absolute truth",
    "AI judge",
    "AI authority",
    "autonomous AI governance",
    "world-changing",
    "guaranteed trust",
]

WARNING_PHRASES = [
    "experimental project",
    "experimental protocol",
    "Humanity Chain as main brand",
    "social AI club",
    "AI decides",
]

DEFAULT_TARGETS = ["README.md", "docs/**/*.md", ".github/**/*.md"]


def parse_allowlist(path: Path) -> dict[Path, set[str]]:
    if not path.exists():
        return {}

    allowlist: dict[Path, set[str]] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid allowlist entry at {path}:{lineno}: {raw}")

        file_part, phrase_part = line.split(":", maxsplit=1)
        rel_file = Path(file_part.strip())
        phrase = phrase_part.strip()
        if not rel_file.as_posix() or not phrase:
            raise ValueError(f"Invalid allowlist entry at {path}:{lineno}: {raw}")

        allowlist.setdefault(rel_file, set()).add(phrase.casefold())
    return allowlist


def iter_targets(repo_root: Path, patterns: Iterable[str]) -> list[Path]:
    files: set[Path] = set()
    for pattern in patterns:
        if any(ch in pattern for ch in "*?["):
            files.update(repo_root.glob(pattern))
        else:
            p = repo_root / pattern
            if p.exists():
                files.add(p)
    return sorted(path for path in files if path.is_file())


def find_matches(lines: list[str], phrase: str) -> list[int]:
    needle = phrase.casefold()
    return [idx for idx, line in enumerate(lines, start=1) if needle in line.casefold()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Check docs for forbidden/warning terminology.")
    parser.add_argument("--allowlist", default=".terminology_allowlist")
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        default=os.getenv("TERMINOLOGY_STRICT_WARNINGS", "").lower() in {"1", "true", "yes"},
        help="Treat warning phrases as failures.",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    allowlist = parse_allowlist(repo_root / args.allowlist)
    targets = iter_targets(repo_root, DEFAULT_TARGETS)

    failures = 0
    warnings = 0

    for file_path in targets:
        rel_path = file_path.relative_to(repo_root)
        allowed = allowlist.get(rel_path, set())
        lines = file_path.read_text(encoding="utf-8").splitlines()

        for phrase in FORBIDDEN_PHRASES:
            if phrase.casefold() in allowed:
                continue
            for line_no in find_matches(lines, phrase):
                print(f"ERROR: {rel_path}:{line_no}: forbidden phrase '{phrase}'")
                failures += 1

        for phrase in WARNING_PHRASES:
            if phrase.casefold() in allowed:
                continue
            for line_no in find_matches(lines, phrase):
                print(f"WARNING: {rel_path}:{line_no}: warning phrase '{phrase}'")
                warnings += 1

    if failures:
        print(f"Found {failures} forbidden phrase match(es).")
        return 1

    if warnings and args.strict_warnings:
        print(f"Found {warnings} warning phrase match(es); strict warnings enabled.")
        return 1

    if warnings:
        print(f"Found {warnings} warning phrase match(es).")
    else:
        print("Terminology check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
