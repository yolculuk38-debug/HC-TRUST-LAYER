#!/usr/bin/env python3
"""Validate MVP-1 verification package example fixtures."""

from __future__ import annotations

import json
from pathlib import Path

REQUIRED_FIELDS = [
    "package_id",
    "content_hash",
    "provenance_summary",
    "provenance_timeline",
    "validator_reviews",
    "replay_indicators",
    "dispute_indicators",
    "trust_result",
    "trust_confidence",
    "audit_snapshot",
    "generated_at",
    "human_review_required",
]

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples" / "verification-packages"


def validate_file(file_path: Path) -> tuple[bool, str]:
    try:
        payload = json.loads(file_path.read_text(encoding="utf-8"))
    except OSError as exc:
        return False, f"unable to read file ({exc})"
    except json.JSONDecodeError as exc:
        return False, f"invalid JSON ({exc})"

    if not isinstance(payload, dict):
        return False, "top-level JSON value must be an object"

    missing_fields = [field for field in REQUIRED_FIELDS if field not in payload]
    if missing_fields:
        return False, "missing required fields: " + ", ".join(missing_fields)

    return True, "all required fields present"


def main() -> int:
    files = sorted(EXAMPLES_DIR.glob("*.json"))
    if not files:
        print(f"FAIL {EXAMPLES_DIR}: no example files found")
        return 1

    has_failures = False

    for file_path in files:
        is_valid, detail = validate_file(file_path)
        if is_valid:
            print(f"PASS {file_path}: {detail}")
            continue

        has_failures = True
        print(f"FAIL {file_path}: {detail}")

    return 1 if has_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
