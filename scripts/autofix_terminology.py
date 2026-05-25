#!/usr/bin/env python3
"""Safe local terminology autofix helper for HC-TRUST-LAYER."""

from __future__ import annotations

import argparse
from pathlib import Path

FORBIDDEN_PHRASE = "truth score"
REPLACEMENT_PHRASE = "advisory trust summary"

SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "coverage",
    ".cache",
    "artifacts",
}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def is_binary(path: Path) -> bool:
    with path.open("rb") as handle:
        chunk = handle.read(8192)
    return b"\x00" in chunk


def collect_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(repo_root)
        if should_skip(rel):
            continue
        if is_binary(path):
            continue
        files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Autofix known forbidden terminology safely.")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply replacements in-place. Default is dry-run.",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    changed_files: list[Path] = []
    remaining_violations: list[Path] = []

    for file_path in collect_files(repo_root):
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        if FORBIDDEN_PHRASE not in text:
            continue

        rel = file_path.relative_to(repo_root)
        updated = text.replace(FORBIDDEN_PHRASE, REPLACEMENT_PHRASE)

        if args.write and updated != text:
            file_path.write_text(updated, encoding="utf-8")
            changed_files.append(rel)

        check_text = updated if args.write else text
        if FORBIDDEN_PHRASE in check_text:
            remaining_violations.append(rel)

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"Mode: {mode}")

    if changed_files:
        print("Changed files:")
        for path in sorted(changed_files):
            print(f"- {path}")
    else:
        print("Changed files:\n- (none)")

    if remaining_violations:
        print("Remaining violations:")
        for path in sorted(set(remaining_violations)):
            print(f"- {path}")
        return 1

    print("Remaining violations:\n- (none)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
