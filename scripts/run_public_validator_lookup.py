#!/usr/bin/env python3
"""Run local-only HC:// Public Validator record_id lookup."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hc_runtime.public_validator_lookup import lookup_public_validator_record


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve a record_id against local canonical HC:// record directories only."
    )
    parser.add_argument("record_id", help="Record ID to look up; paths and URLs are rejected.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    print(json.dumps(lookup_public_validator_record(args.record_id, root=ROOT), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
