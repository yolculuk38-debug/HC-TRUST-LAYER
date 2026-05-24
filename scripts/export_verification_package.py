#!/usr/bin/env python3
"""HC-TRUST-LAYER verification package exporter skeleton.

This is a safe, non-production exporter skeleton for deriving a verification package
from a canonical record without mutating canonical data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ALLOWED_PREFIXES = (
    Path("records/pending"),
    Path("records/verified"),
    Path("records/archived"),
)

DISALLOWED_TOKENS = ("generated", "index", "export", "cache")

SKELETON_WARNINGS = [
    "exporter skeleton: non-production workflow for HC-TRUST-LAYER",
    "verification package is a derived artifact and non-canonical",
    "signatures are not yet implemented",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export a HC-TRUST-LAYER verification package skeleton from a canonical record."
    )
    parser.add_argument("canonical_record", help="Path to canonical record JSON under records/*")
    parser.add_argument(
        "--output",
        help=(
            "Optional output file path. Must be under examples/generated/. "
            "If omitted, package JSON is printed to stdout."
        ),
    )
    parser.add_argument(
        "--skip-schema-validation",
        action="store_true",
        help="Skip schema validation even if validator dependency is available.",
    )
    return parser.parse_args()


def normalize_record_path(path_text: str) -> Path:
    raw = Path(path_text)
    normalized = Path(raw.as_posix().lstrip("./"))
    return normalized


def assert_allowed_canonical_path(path: Path) -> None:
    if path.suffix.lower() != ".json":
        raise ValueError("canonical record must be a .json file")

    if any(token in path.as_posix().lower() for token in DISALLOWED_TOKENS):
        raise ValueError("canonical path includes disallowed generated/index/export/cache token")

    if not any(path.as_posix().startswith(prefix.as_posix() + "/") for prefix in ALLOWED_PREFIXES):
        raise ValueError(
            "canonical record path must be under records/pending/, records/verified/, or records/archived/"
        )


def assert_output_path(output_path: Path) -> None:
    if not output_path.as_posix().startswith("examples/generated/"):
        raise ValueError("output path must be under examples/generated/")


def source_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            text=True,
            capture_output=True,
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


def sha256_hex(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_record(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("canonical record must be a JSON object")
    return data


def assemble_package(record: dict, canonical_path: Path) -> dict:
    canonical_path_posix = canonical_path.as_posix()
    record_id = str(record.get("record_id") or record.get("id") or "UNKNOWN-RECORD-ID")
    record_hash = str(record.get("hash") or record.get("record_hash") or "")
    content_hash = str(record.get("content_hash") or "")
    verification_state = str(record.get("status") or record.get("verification_status") or "pending")

    if len(record_hash) != 64:
        record_hash = sha256_hex(json.dumps(record, sort_keys=True, separators=(",", ":")))
    if len(content_hash) != 64:
        content_hash = sha256_hex(str(record.get("content") or json.dumps(record, sort_keys=True)))

    package_id = "HC-PKG-" + sha256_hex(f"{canonical_path_posix}:{record_id}")[:24].upper()

    return {
        "package_version": "1.0",
        "package_id": package_id,
        "record_id": record_id,
        "record_hash": record_hash,
        "content_hash": content_hash,
        "verification_state": verification_state,
        "canonical_record_path": canonical_path_posix,
        "source_repository": "HC-TRUST-LAYER",
        "source_commit": source_commit(),
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "provenance": {
            "hc_uri": f"HC://record/{record_id}",
            "record_type": record.get("record_type"),
            "source": record.get("source"),
        },
        "audit": {
            "skeleton_export": True,
            "integrity_verification": "best-effort structural checks only",
            "canonical_mutation_performed": False,
        },
        "witnesses": record.get("witnesses") if isinstance(record.get("witnesses"), list) else [],
        "signatures": [],
        "verification_policy": {
            "mode": "skeleton",
            "non_canonical": True,
            "integrity_verification": "schema + path boundary checks",
        },
        "warnings": SKELETON_WARNINGS,
        "export_context": {
            "exporter": "scripts/export_verification_package.py",
            "exporter_mode": "skeleton",
            "derived_artifact": True,
        },
    }


def validate_against_schema(package: dict, schema_path: Path) -> list[str]:
    if not schema_path.exists():
        return [f"schema validation skipped: missing schema file at {schema_path.as_posix()}"]

    try:
        import jsonschema  # type: ignore
    except ImportError:
        return ["schema validation skipped: optional dependency 'jsonschema' is not installed"]

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=package, schema=schema)
    return []


def main() -> int:
    args = parse_args()
    canonical_path = normalize_record_path(args.canonical_record)

    try:
        assert_allowed_canonical_path(canonical_path)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    path_on_disk = Path(canonical_path)
    if not path_on_disk.exists() or not path_on_disk.is_file():
        print(f"ERROR: canonical record not found: {canonical_path.as_posix()}", file=sys.stderr)
        return 2

    try:
        record = load_record(path_on_disk)
        package = assemble_package(record, canonical_path)
    except Exception as exc:
        print(f"ERROR: failed to build verification package skeleton: {exc}", file=sys.stderr)
        return 1

    if not args.skip_schema_validation:
        try:
            validation_warnings = validate_against_schema(package, Path("schema/verification-package-v1.schema.json"))
        except Exception as exc:
            print(f"ERROR: schema validation failed: {exc}", file=sys.stderr)
            return 1
        if validation_warnings:
            package["warnings"] = list(package["warnings"]) + validation_warnings

    output_text = json.dumps(package, indent=2, sort_keys=True) + "\n"

    if args.output:
        out_path = Path(args.output)
        try:
            assert_output_path(out_path)
        except ValueError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_text, encoding="utf-8")
    else:
        sys.stdout.write(output_text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
