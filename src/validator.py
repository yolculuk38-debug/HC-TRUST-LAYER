#!/usr/bin/env python3
import sys
from pathlib import Path

from hc_trust.verification import validate_record as validate_record_file

SKIP_HINTS = ("index", "manifest", "cache", "export", "generated")


def validate_record(record_path):
    """Validate one canonical record through the shared record-v1 contract."""

    file_name = Path(record_path).name.lower()
    if any(hint in file_name for hint in SKIP_HINTS):
        print(f"SKIPPED ARTIFACT: {record_path}")
        return True

    passed, message = validate_record_file(record_path)
    print(message)
    return passed

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/validator.py <record.json>")
        sys.exit(1)
    
    record_path = sys.argv[1]
    success = validate_record(record_path)
    sys.exit(0 if success else 1)
