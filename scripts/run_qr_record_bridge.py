#!/usr/bin/env python3
"""Run the local-only advisory HC:// QR payload to record bridge."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from hc_runtime.qr_record_bridge import check_qr_payload_record_bridge


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check one local HC:// QR payload JSON string against local record content_hash."
    )
    parser.add_argument(
        "payload",
        help="QR payload JSON string to bridge locally.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    print(
        json.dumps(
            check_qr_payload_record_bridge(args.payload),
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
