#!/usr/bin/env python3
"""Validate the verification package example against the v1 schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "verification-package-v1.schema.json"
EXAMPLE_PATH = ROOT / "examples" / "verification-package-example.json"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    example = json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda err: list(err.absolute_path))

    if errors:
        print("FAIL: verification package example does not conform to schema")
        for error in errors:
            path = ".".join(str(part) for part in error.absolute_path) or "<root>"
            print(f" - {path}: {error.message}")
        return 1

    print("PASS: verification package example conforms to schema")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
