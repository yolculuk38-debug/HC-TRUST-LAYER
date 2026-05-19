"""Normalize Humanity Chain JSON records with explicit safe-write controls."""

from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path

RECORDS_DIR = Path("records")
PROTECTED_PARTS = {"archive", "verified"}


def is_protected_record(record_path: Path) -> bool:
    return any(part in PROTECTED_PARTS for part in record_path.parts)


def render_normalized_content(record_path: Path) -> tuple[str, str]:
    original = record_path.read_text(encoding="utf-8")
    data = json.loads(original)
    normalized = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    return original, normalized


def print_diff(record_path: Path, original: str, normalized: str) -> None:
    diff = difflib.unified_diff(
        original.splitlines(),
        normalized.splitlines(),
        fromfile=f"{record_path} (current)",
        tofile=f"{record_path} (normalized)",
        lineterm="",
    )
    print(f"[DRY-RUN] Proposed changes for {record_path}:")
    for line in diff:
        print(line)


def normalize_record(record_path: Path, dry_run: bool, write: bool) -> bool:
    original, normalized = render_normalized_content(record_path)
    changed = original != normalized

    if not changed:
        print(f"[OK] {record_path}")
        return False

    warning = f"[WARNING] Record would be changed: {record_path}"
    print(warning)

    if dry_run:
        print_diff(record_path, original, normalized)
        return True

    if is_protected_record(record_path):
        print(f"[SKIPPED] Protected record not overwritten: {record_path}")
        return True

    if not write:
        print(f"[SKIPPED] Use --write to apply changes: {record_path}")
        return True

    record_path.write_text(normalized, encoding="utf-8")
    print(f"[UPDATED] {record_path}")
    return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize JSON records safely. By default no files are modified; "
            "use --write to apply changes."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview proposed changes as diffs without modifying files.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Explicitly apply normalization changes to writable record files.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if not RECORDS_DIR.exists():
        print("records directory not found.")
        return

    changed_count = 0
    for record_path in sorted(RECORDS_DIR.rglob("*.json")):
        if normalize_record(record_path, dry_run=args.dry_run, write=args.write):
            changed_count += 1

    if changed_count and not args.write:
        print(
            "\nSummary: Changes detected but not written. "
            "Run with --write to apply writable record updates."
        )


if __name__ == "__main__":
    main()
