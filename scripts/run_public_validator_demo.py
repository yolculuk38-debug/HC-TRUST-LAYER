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
SCENARIO_RECORD_IDS: dict[str, str] = {
    "banana": "HC-DEMO-PV-FIXTURE-FOOD-0001",
    "building": "HC-DEMO-PV-FIXTURE-CONCRETE-0001",
    "news": "HC-DEMO-PV-FIXTURE-NEWS-0001",
    "qr-spoof": "HC-DEMO-PV-FIXTURE-QR-0001",
}
RECORD_ID_SCENARIOS = {
    record_id: scenario for scenario, record_id in SCENARIO_RECORD_IDS.items()
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

    expected_record_id = SCENARIO_RECORD_IDS[scenario]
    if result["record_id"] != expected_record_id:
        raise ValueError(
            f"Fixture {scenario!r} has record_id {result['record_id']!r}; "
            f"expected {expected_record_id!r}"
        )

    return result


def build_result(scenario: str) -> dict[str, Any]:
    """Return a deterministic public-safe demo result for a supported scenario."""
    return deepcopy(load_fixture(scenario))


def resolve_scenario(selector: str) -> str:
    """Resolve a scenario name or bundled demo record ID without external lookup."""
    candidate = selector.strip()
    if candidate in SCENARIOS:
        return candidate

    scenario = RECORD_ID_SCENARIOS.get(candidate.upper())
    if scenario is not None:
        return scenario

    raise argparse.ArgumentTypeError(
        "expected a supported scenario name or bundled demo record_id"
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a local-only, advisory HC:// Public Validator demo by scenario "
            "name or bundled demo record_id."
        )
    )
    parser.add_argument(
        "scenario",
        type=resolve_scenario,
        metavar="SCENARIO_OR_RECORD_ID",
        help="Supported demo scenario name or bundled demo record_id.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    print(json.dumps(build_result(args.scenario), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
