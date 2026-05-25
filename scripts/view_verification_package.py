#!/usr/bin/env python3
"""MVP-1 CLI viewer for HC:// verification package examples."""

from __future__ import annotations

import argparse
import json
import re
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

ALLOWED_TRUST_RESULTS = {
    "VERIFIED TRACE",
    "PARTIAL TRACE",
    "REPLAY WARNING",
    "DISPUTED",
    "UNVERIFIED",
}

SHA256_HEX_RE = re.compile(r"^[0-9a-f]{64}$")


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


def is_human_readable_confidence(value: object) -> bool:
    if not isinstance(value, str):
        return False
    cleaned = value.strip()
    return len(cleaned) >= 3 and bool(re.search(r"[A-Za-z]", cleaned))


def collect_warnings(payload: dict[str, object]) -> list[str]:
    warnings: list[str] = []

    trust_result = payload.get("trust_result")
    if not isinstance(trust_result, str) or trust_result not in ALLOWED_TRUST_RESULTS:
        warnings.append(
            "trust_result should be one of: VERIFIED TRACE, PARTIAL TRACE, "
            "REPLAY WARNING, DISPUTED, UNVERIFIED."
        )

    content_hash = payload.get("content_hash")
    if not isinstance(content_hash, str) or not SHA256_HEX_RE.fullmatch(content_hash):
        warnings.append("content_hash should match lowercase SHA-256 hex format (64 hex characters).")

    if not is_human_readable_confidence(payload.get("trust_confidence")):
        warnings.append("trust_confidence should be present and human-readable.")

    for field in ["provenance_timeline", "validator_reviews", "replay_indicators", "dispute_indicators"]:
        if not isinstance(payload.get(field), list):
            warnings.append(f"{field} should be an array.")

    return warnings


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

    warnings = collect_warnings(payload)

    print("HC:// MVP-1 Verification Package Summary")
    print(f"source_file: {file_path}")
    print("-" * 72)

    if warnings:
        print("WARNING: advisory package validation findings")
        for warning in warnings:
            print(f"- {warning}")
        print("- Viewer output remains advisory and requires human-supervised validation.")
        print("-" * 72)

    for field in REQUIRED_FIELDS:
        print(f"{field}: {format_value(payload[field])}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
