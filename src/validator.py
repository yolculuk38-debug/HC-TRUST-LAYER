#!/usr/bin/env python3
import sys

from hc_trust.verification import is_generated_artifact_file, validate_record as validate_record_file



def validate_record(record_path):
    """Validate one canonical record through the shared record-v1 contract."""

    if is_generated_artifact_file(record_path):
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
