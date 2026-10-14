#!/usr/bin/env python3
import argparse
from pathlib import Path

from hc_trust.verification import is_generated_artifact_file, validate_record as validate_record_file
from hc_trust.record_selection import (
    RecordSelectionError, classify_record_file, record_selection_context,
)



def validate_record(record_path, *, repo_root=None):
    """Validate one file, with canonical selection when a root is available."""

    try:
        path, root = record_selection_context(record_path, repo_root=repo_root)
    except RecordSelectionError as exc:
        print(f"ERROR: {exc}")
        return False
    kind = classify_record_file(path, repo_root=root)
    if kind == "artifact" or (root is None and is_generated_artifact_file(Path(record_path).name)):
        print(f"SKIPPED ARTIFACT: {record_path}")
        return True
    if root is not None and kind != "record":
        print(f"ERROR: outside canonical record boundary: {record_path}")
        return False

    passed, message = validate_record_file(path)
    print(message)
    return passed

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate one local record JSON file")
    parser.add_argument("record_path")
    parser.add_argument("--repo-root", help="Canonical repository root; relative paths use this root")
    args = parser.parse_args()
    success = validate_record(args.record_path, repo_root=args.repo_root)
    raise SystemExit(0 if success else 1)
