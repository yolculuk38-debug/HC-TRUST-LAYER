#!/usr/bin/env python3
"""Generate the deterministic Public Validator demo QR access aid."""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path
import sys

import qrcode


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "docs" / "demo" / "public-validator-demo-qr.svg"

DEMO_RECORD_ID = "HC-DEMO-PV-FIXTURE-FOOD-0001"
DEMO_TARGET_URL = (
    "https://yolculuk38-debug.github.io/HC-TRUST-LAYER/"
    "demo/public-validator-static-viewer.html"
    f"?record_id={DEMO_RECORD_ID}#result-heading"
)

ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_M
BOX_SIZE = 10
BORDER = 4


def _matrix_path(matrix: list[list[bool]]) -> str:
    """Return one compact SVG path containing each dark module."""

    fragments: list[str] = []

    for y, row in enumerate(matrix):
        x = 0
        while x < len(row):
            if not row[x]:
                x += 1
                continue

            start = x
            while x < len(row) and row[x]:
                x += 1

            run_length = x - start
            fragments.append(f"M{start} {y}h{run_length}v1h-{run_length}z")

    return "".join(fragments)


def generate_svg() -> str:
    """Generate a text-only SVG for the fixed public demo URL."""

    qr = qrcode.QRCode(
        error_correction=ERROR_CORRECTION,
        box_size=BOX_SIZE,
        border=BORDER,
    )
    qr.add_data(DEMO_TARGET_URL)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    size = len(matrix)
    path = _matrix_path(matrix)

    target = escape(DEMO_TARGET_URL, quote=True)
    record_id = escape(DEMO_RECORD_ID, quote=True)

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{size}mm" height="{size}mm" viewBox="0 0 {size} {size}" '
        'role="img" aria-labelledby="qr-title qr-description" '
        f'data-record-id="{record_id}" data-target-url="{target}" '
        'data-advisory-only="true" data-public-safe="true" '
        'data-truth-guarantee="false" data-human-review-required="true" '
        'shape-rendering="crispEdges">\n'
        f'  <title id="qr-title">Public Validator demo QR for {record_id}</title>\n'
        '  <desc id="qr-description">Scannable demo access aid. It does not prove '
        'QR authenticity, signed payload validity, or truth. Human review is required.</desc>\n'
        f'  <rect width="{size}" height="{size}" fill="#fff"/>\n'
        f'  <path d="{path}" fill="#000"/>\n'
        '</svg>\n'
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate or check the Public Validator demo QR SVG."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the committed SVG differs from deterministic output.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output path (default: {DEFAULT_OUTPUT.relative_to(ROOT)}).",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    expected = generate_svg()

    if args.check:
        try:
            actual = args.output.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"Missing Public Validator demo QR asset: {args.output}", file=sys.stderr)
            return 1

        if actual != expected:
            print(
                "Public Validator demo QR asset is stale; regenerate it with "
                "scripts/generate_public_validator_demo_qr.py.",
                file=sys.stderr,
            )
            return 1

        print(f"Public Validator demo QR asset is current: {args.output}")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(expected, encoding="utf-8")
    print(f"Wrote Public Validator demo QR asset: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
