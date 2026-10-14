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
LOCAL_MANIFEST_SCHEMA_PATH = ROOT / "src" / "hc_trust" / "schemas" / "verification-package-manifest-v1.schema.json"
LOCAL_MANIFEST_EXAMPLES = sorted((ROOT / "examples" / "verification-package").glob("*/manifest.json"))


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

    local_schema = json.loads(LOCAL_MANIFEST_SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(local_schema)
    local_validator = Draft202012Validator(local_schema)
    local_errors = []
    for manifest_path in LOCAL_MANIFEST_EXAMPLES:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        local_errors.extend(
            (manifest_path, error)
            for error in local_validator.iter_errors(manifest)
        )

    if local_errors:
        print("FAIL: local verification package manifest does not conform to schema")
        for manifest_path, error in local_errors:
            path = ".".join(str(part) for part in error.absolute_path) or "<root>"
            print(f" - {manifest_path.relative_to(ROOT)}:{path}: {error.message}")
        return 1

    print("PASS: flat verification package example and local directory manifests conform to their schemas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
