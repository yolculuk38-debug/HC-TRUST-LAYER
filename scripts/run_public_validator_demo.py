#!/usr/bin/env python3
"""Run deterministic, local-only HC:// Public Validator demo scenarios."""

from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "docs" / "demo" / "fixtures" / "results"
SCENARIOS: dict[str, Path] = {
    "banana": FIXTURE_DIR / "banana.json",
    "building": FIXTURE_DIR / "building.json",
    "news": FIXTURE_DIR / "news.json",
    "qr-spoof": FIXTURE_DIR / "qr-spoof.json",
}
SAFETY_MARKERS: dict[str, bool] = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}
REQUIRED_FIELDS = {
    "record_id",
    "scenario",
    "status",
    "source_chain",
    "responsibility_chain",
    "evidence",
    "missing_evidence",
    "conflicting_evidence",
    "warnings",
    *SAFETY_MARKERS,
}


def load_fixture(scenario: str) -> dict[str, Any]:
    """Load a public-safe demo result fixture for a supported scenario."""
    with SCENARIOS[scenario].open(encoding="utf-8") as handle:
        result = json.load(handle)

    missing_fields = REQUIRED_FIELDS.difference(result)
    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"Fixture {scenario!r} is missing required fields: {missing}")

    for key, value in SAFETY_MARKERS.items():
        if result[key] is not value:
            raise ValueError(f"Fixture {scenario!r} has invalid safety marker {key!r}")

    return result


def build_result(scenario: str) -> dict[str, Any]:
    """Return a deterministic public-safe demo result for a supported scenario."""
    return deepcopy(load_fixture(scenario))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a local-only, advisory HC:// Public Validator demo scenario."
    )
    parser.add_argument(
        "scenario",
        choices=sorted(SCENARIOS),
        help="Demo scenario to run.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    print(json.dumps(build_result(args.scenario), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
