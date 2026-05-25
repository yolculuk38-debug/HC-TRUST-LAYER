#!/usr/bin/env python3
"""MVP-1 CLI viewer for HC:// verification package examples."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "package_id",
    "trust_result",
    "trust_confidence",
    "content_hash",
    "provenance_summary",
    "provenance_timeline",
    "validator_reviews",
    "replay_indicators",
    "dispute_indicators",
    "audit_snapshot",
    "human_review_required",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="View an MVP-1 HC:// verification package in a human-readable format."
    )
    parser.add_argument("json_file", help="Path to a verification package JSON file.")
    return parser.parse_args()


def format_value(value: object) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, indent=2)
    return str(value)


def main() -> int:
    args = parse_args()
    file_path = Path(args.json_file)

    if not file_path.exists():
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        return 1

    try:
        payload = json.loads(file_path.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"Error: unable to read file '{file_path}': {exc}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON in '{file_path}': {exc}", file=sys.stderr)
        return 1

    if not isinstance(payload, dict):
        print("Error: verification package must be a JSON object.", file=sys.stderr)
        return 1

    missing_fields = [field for field in REQUIRED_FIELDS if field not in payload]
    if missing_fields:
        print(
            "Error: missing required MVP fields: " + ", ".join(missing_fields),
            file=sys.stderr,
        )
        return 1

    print("HC:// MVP-1 Verification Package Summary")
    print(f"source_file: {file_path}")
    print("-" * 72)

    for field in REQUIRED_FIELDS:
        print(f"{field}: {format_value(payload[field])}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
