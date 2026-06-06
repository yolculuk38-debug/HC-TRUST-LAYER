#!/usr/bin/env python3
"""Run deterministic, local-only HC:// Public Validator demo scenarios."""

from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from typing import Any

SAFETY_MARKERS: dict[str, bool] = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}

SCENARIOS: dict[str, dict[str, Any]] = {
    "banana": {
        "record_id": "HC-DEMO-PV-FIXTURE-FOOD-0001",
        "scenario": "imported_banana_food_provenance",
        "status": "needs_human_review",
        "source_chain": [
            "Demo grower cooperative harvest note",
            "Demo packhouse lot record",
            "Demo export inspection note",
            "Demo carrier handoff note",
            "Demo destination intake note",
            "Demo lab method summary",
        ],
        "responsibility_chain": [
            "Demo grower cooperative",
            "Demo packhouse operator",
            "Demo export broker",
            "Demo carrier",
            "Demo destination intake reviewer",
            "Demo human review approver",
        ],
        "evidence": [
            {
                "type": "demo_lot_record",
                "reference": "DEMO-LOT-0187-RECORD",
                "evidence_status": "present",
            },
            {
                "type": "demo_inspection_summary",
                "reference": "DEMO-ORIGIN-INSPECTION-REF",
                "evidence_status": "present",
            },
            {
                "type": "demo_lab_method_summary",
                "reference": "DEMO-LAB-METHOD-FOOD-01",
                "evidence_status": "present",
            },
        ],
        "missing_evidence": [
            "Independent confirmation of origin inspection issuer authority",
            "Destination intake image evidence",
            "Complete transport temperature log",
        ],
        "conflicting_evidence": [
            "Destination intake count differs from export count by two cartons.",
        ],
        "warnings": [
            "Advisory demo result only; not a food safety certification.",
            "Visible provenance is incomplete and requires human review.",
            "Conflicting carton count should be reviewed before relying on this demo result.",
        ],
    },
    "building": {
        "record_id": "HC-DEMO-PV-FIXTURE-CONCRETE-0001",
        "scenario": "building_concrete_provenance",
        "status": "needs_human_review",
        "source_chain": [
            "Demo concrete plant batch ticket",
            "Demo mixer truck dispatch note",
            "Demo field sample collection note",
            "Demo lab receipt note",
            "Demo test result reference",
        ],
        "responsibility_chain": [
            "Demo concrete plant",
            "Demo mixer truck operator",
            "Demo field technician",
            "Demo concrete lab reviewer",
            "Demo supervising authority reviewer",
        ],
        "evidence": [
            {
                "type": "demo_batch_ticket",
                "reference": "DEMO-CONCRETE-BATCH-5509-TICKET",
                "evidence_status": "present",
            },
            {
                "type": "demo_sample_collection_note",
                "reference": "DEMO-SAMPLE-CONCRETE-CYL-03",
                "evidence_status": "partial",
            },
            {
                "type": "demo_test_result_reference",
                "reference": "DEMO-CONCRETE-RESULT-28DAY-03",
                "evidence_status": "present",
            },
        ],
        "missing_evidence": [
            "Independent confirmation of sample collection witness",
            "Complete curing condition log",
            "Signed supervising authority review note",
        ],
        "conflicting_evidence": [
            "Field sample timestamp is later than one dispatch note timestamp and requires human review.",
        ],
        "warnings": [
            "Advisory demo result only; not a building safety or code compliance certification.",
            "Demo result references must not be treated as proof of structural integrity.",
            "Chain-of-custody contains partial field sample evidence.",
        ],
    },
    "news": {
        "record_id": "HC-DEMO-PV-FIXTURE-NEWS-0001",
        "scenario": "news_source_provenance",
        "status": "needs_human_review",
        "source_chain": [
            "Demo public meeting note",
            "Demo reporter interview note",
            "Demo press statement",
            "Demo public dataset summary",
            "Demo correction note",
        ],
        "responsibility_chain": [
            "Demo staff reporter",
            "Demo assigning editor",
            "Demo publisher review desk",
            "Demo human reviewer",
        ],
        "evidence": [
            {
                "type": "demo_original_source_note",
                "reference": "DEMO-MEETING-NOTE-2026-05-02",
                "evidence_status": "present",
            },
            {
                "type": "demo_referenced_source",
                "reference": "DEMO-PRESS-STATEMENT-01",
                "evidence_status": "present",
            },
            {
                "type": "demo_correction_history",
                "reference": "DEMO-CORRECTION-NOTE-01",
                "evidence_status": "present",
            },
        ],
        "missing_evidence": [
            "Final independent confirmation response",
            "Full context for the public dataset summary",
        ],
        "conflicting_evidence": [
            "Demo press statement and demo meeting note use different date wording for the same event.",
        ],
        "warnings": [
            "Advisory demo result only; not a truth rating or news certification.",
            "Source provenance is partial and requires human editorial review.",
            "Opinion or analysis marker should remain visible to public reviewers.",
        ],
    },
    "qr-spoof": {
        "record_id": "HC-DEMO-PV-FIXTURE-QR-0001",
        "scenario": "qr_spoof_non_canonical_link",
        "status": "needs_human_review",
        "source_chain": [
            "Demo QR label scan observation",
            "Demo expected HC:// canonical reference",
            "Demo issuer reference note",
        ],
        "responsibility_chain": [
            "Demo label issuer",
            "Demo scanner operator",
            "Demo human reviewer",
        ],
        "evidence": [
            {
                "type": "demo_scanned_url_observation",
                "reference": "DEMO-SCANNED-URL-OBSERVATION-01",
                "evidence_status": "present",
            },
            {
                "type": "demo_canonical_url_reference",
                "reference": "DEMO-CANONICAL-HC-REFERENCE-01",
                "evidence_status": "present",
            },
            {
                "type": "demo_issuer_reference",
                "reference": "DEMO-ISSUER-QR-01",
                "evidence_status": "partial",
            },
        ],
        "missing_evidence": [
            "Independently verified issuer authority",
            "Signed payload evidence",
            "Real payload hash verification",
            "Original QR artifact image",
        ],
        "conflicting_evidence": [
            "Scanned URL differs from the expected HC:// canonical URL in this demo fixture.",
        ],
        "warnings": [
            "Advisory demo result only; not a fraud finding or forensic determination.",
            "Non-canonical link condition requires human review before any reliance.",
            "This fixture does not validate signatures, generate QR artifacts, or fetch remote URLs.",
        ],
    },
}


def build_result(scenario: str) -> dict[str, Any]:
    """Return a deterministic public-safe demo result for a supported scenario."""
    result = deepcopy(SCENARIOS[scenario])
    result.update(SAFETY_MARKERS)
    return result


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
