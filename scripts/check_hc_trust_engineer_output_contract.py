#!/usr/bin/env python3
"""Validate an illustrative HC Trust Engineer Operating Loop output envelope.

This checker is local-only and report-only. It validates the shape of a sample
contract envelope; it does not verify truth, identity, security posture, legal
status, production readiness, or merge readiness.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_ENVELOPE_FIELDS = [
    "report_type",
    "generated_at",
    "repository",
    "source_of_truth",
    "evidence_window",
    "advisory_only",
    "public_safe",
    "truth_guarantee",
    "human_review_required",
    "repository_mutation",
    "issue_comment_automation",
    "label_reviewer_mutation",
    "approval_authority",
    "merge_authority",
    "outputs",
]

HARD_BOUNDARIES = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
    "repository_mutation": False,
    "issue_comment_automation": False,
    "label_reviewer_mutation": False,
    "approval_authority": False,
    "merge_authority": False,
}

REQUIRED_MARKERS = [
    f"{name}={str(value).lower()}" for name, value in HARD_BOUNDARIES.items()
]

SECTION_REQUIRED_FIELDS = {
    "STATE_SUMMARY": [
        "summary",
        "evidence_reviewed",
        "open_pr_count",
        "recent_merged_prs",
        "known_uncertainties",
    ],
    "CHAIN_STATUS": [
        "chain_id",
        "chain_type",
        "related_prs",
        "status",
        "evidence",
        "uncertainty",
    ],
    "NEXT_ACTION_CANDIDATE": [
        "action_type",
        "title",
        "reason",
        "allowed_scope",
        "forbidden_scope",
        "expected_risk",
        "human_decision_required",
    ],
    "RISK_BOUNDARY_CLASSIFICATION": [
        "risk_level",
        "reason",
        "protected_paths_touched",
        "automation_authority_change",
        "runtime_or_validator_impact",
    ],
    "HUMAN_HANDOFF_NOTE": [
        "recommendation",
        "decision_needed",
        "safe_next_step",
        "do_not_do",
        "final_authority",
    ],
}

OPTIONAL_SECTION_REQUIRED_FIELDS = {
    "READY_FOR_CLOSURE_NOTE": [
        "chain_id",
        "reason",
        "evidence",
        "human_action_required",
        "must_follow_closure_report_mode_rules",
    ],
    "NOT_READY_FOR_CLOSURE": [
        "chain_id",
        "missing_evidence",
        "blocker",
        "uncertainty",
        "recommended_follow_up",
    ],
}

REQUIRED_SECTIONS = set(SECTION_REQUIRED_FIELDS)
CHAIN_STATUS_VALUES = {
    "complete",
    "partially_complete",
    "blocked",
    "duplicated",
    "stale",
    "unknown",
}
NEXT_ACTION_VALUES = {
    "immediate_safe_action",
    "follow_up_planning_action",
    "parked_action",
    "blocked_action",
}
RISK_LEVEL_VALUES = {"low", "medium", "high"}


class ContractError(ValueError):
    """Raised when the local sample does not match the output contract."""


def _require_mapping(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContractError(f"{path} must be an object")
    return value


def _require_list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise ContractError(f"{path} must be a list")
    return value


def _section_map(outputs: Any) -> dict[str, dict[str, Any]]:
    sections: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(_require_list(outputs, "outputs")):
        section = _require_mapping(item, f"outputs[{index}]")
        name = section.get("section")
        if not isinstance(name, str) or not name:
            raise ContractError(f"outputs[{index}].section is required")
        sections[name] = section
    return sections


def _validate_section_fields(
    section: dict[str, Any], section_name: str, required_fields: list[str]
) -> None:
    for field in required_fields:
        if field not in section:
            raise ContractError(f"{section_name} missing required field: {field}")


def validate_contract(payload: dict[str, Any]) -> None:
    envelope = _require_mapping(payload, "envelope")

    for field in REQUIRED_ENVELOPE_FIELDS:
        if field not in envelope:
            raise ContractError(f"missing required envelope field: {field}")

    for field, expected in HARD_BOUNDARIES.items():
        actual = envelope[field]
        if actual is not expected:
            expected_text = str(expected).lower()
            actual_text = (
                str(actual).lower() if isinstance(actual, bool) else repr(actual)
            )
            raise ContractError(
                f"{field} must be exactly {expected_text}; got {actual_text}"
            )

    markers = _require_list(
        envelope.get("hard_boundary_markers"), "hard_boundary_markers"
    )
    for marker in REQUIRED_MARKERS:
        if marker not in markers:
            raise ContractError(f"missing exact hard boundary marker: {marker}")

    sections = _section_map(envelope["outputs"])
    for section_name in sorted(REQUIRED_SECTIONS - sections.keys()):
        raise ContractError(f"missing required output section: {section_name}")

    for section_name, required_fields in SECTION_REQUIRED_FIELDS.items():
        _validate_section_fields(
            sections[section_name], section_name, required_fields
        )

    for section_name, required_fields in OPTIONAL_SECTION_REQUIRED_FIELDS.items():
        if section_name in sections:
            _validate_section_fields(
                sections[section_name], section_name, required_fields
            )

    status = sections["CHAIN_STATUS"]["status"]
    if status not in CHAIN_STATUS_VALUES:
        raise ContractError(f"CHAIN_STATUS.status has invalid value: {status!r}")

    action_type = sections["NEXT_ACTION_CANDIDATE"]["action_type"]
    if action_type not in NEXT_ACTION_VALUES:
        raise ContractError(
            f"NEXT_ACTION_CANDIDATE.action_type has invalid value: {action_type!r}"
        )

    risk_level = sections["RISK_BOUNDARY_CLASSIFICATION"]["risk_level"]
    if risk_level not in RISK_LEVEL_VALUES:
        raise ContractError(
            f"RISK_BOUNDARY_CLASSIFICATION.risk_level has invalid value: {risk_level!r}"
        )

    forbidden_scope = _require_list(
        sections["NEXT_ACTION_CANDIDATE"]["forbidden_scope"],
        "NEXT_ACTION_CANDIDATE.forbidden_scope",
    )
    if "schemas/**" in forbidden_scope:
        raise ContractError(
            "NEXT_ACTION_CANDIDATE.forbidden_scope must not use schemas/**"
        )
    if "schema/**" not in forbidden_scope:
        raise ContractError(
            "NEXT_ACTION_CANDIDATE.forbidden_scope must include schema/**"
        )


def load_contract(path: Path) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON in {path}: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print(
            "usage: python scripts/check_hc_trust_engineer_output_contract.py <fixture.json>",
            file=sys.stderr,
        )
        return 2

    path = Path(args[0])
    try:
        validate_contract(load_contract(path))
    except ContractError as exc:
        print(
            f"HC Trust Engineer output contract validation failed: {exc}",
            file=sys.stderr,
        )
        return 1

    print(f"HC Trust Engineer output contract sample is valid: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
