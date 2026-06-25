#!/usr/bin/env python3
"""Emit one local HC Trust Engineer Operating Loop output envelope.

This emitter is standard-library-only, local-only, and report-only. It reads an
explicit JSON input file, constructs one advisory envelope, validates that
envelope with the local output-contract validator, and prints JSON only after
validation succeeds. It does not read live repository state, call network APIs,
run subprocesses, mutate the repository, or provide approval or merge authority.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_hc_trust_engineer_output_contract import (
    ContractError,
    HARD_BOUNDARIES,
    REQUIRED_MARKERS,
    validate_contract,
)

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
PROTECTED_SCOPE_PREFIXES = (
    "records/",
    "qr/",
    "hash/",
    "agents/",
    "schema/",
    "schemas/",
    ".github/workflows/",
    "src/",
)
PROTECTED_SCOPE_GLOBS = {
    "records/**",
    "qr/**",
    "hash/**",
    "agents/**",
    "schema/**",
    "schemas/**",
    ".github/workflows/**",
    "src/**",
}
AUTOMATION_AUTHORITY_TERMS = (
    "workflow",
    "automation_authority",
    "approval_authority",
    "merge_authority",
    "label_reviewer",
    "issue_comment",
)

REQUIRED_INPUT_FIELDS = [
    "repository",
    "generated_at",
    "evidence_window",
    "open_pr_count",
    "recent_merged_prs",
    "chain_id",
    "chain_type",
    "chain_status",
    "next_action_title",
    "next_action_type",
    "risk_level",
    "known_uncertainties",
]


class EmitterInputError(ValueError):
    """Raised when the local emitter input is incomplete or unsafe."""


def _require_mapping(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise EmitterInputError(f"{path} must be an object")
    return value


def _require_list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise EmitterInputError(f"{path} must be a list")
    return value


def _string_list(data: dict[str, Any], field: str) -> list[str]:
    values = _require_list(data[field], field)
    if not all(isinstance(item, str) and item for item in values):
        raise EmitterInputError(f"{field} must be a list of non-empty strings")
    return values


def _optional_string_list(data: dict[str, Any], field: str, default: list[str]) -> list[str]:
    if field not in data:
        return default
    return _string_list(data, field)


def _require_string(data: dict[str, Any], field: str) -> str:
    value = data[field]
    if not isinstance(value, str) or not value:
        raise EmitterInputError(f"{field} must be a non-empty string")
    return value


def _scope_entry(entry: str) -> str:
    normalized = entry.strip()
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _scope_targets(entry: str, path: str) -> bool:
    normalized = _scope_entry(entry)
    normalized_path = _scope_entry(path)
    if normalized == normalized_path:
        return True
    if normalized.endswith("/**"):
        return normalized_path.startswith(normalized[:-3])
    return normalized.startswith(f"{normalized_path}/")


def _scope_has_protected_path(scope: list[str]) -> bool:
    for entry in scope:
        normalized = _scope_entry(entry)
        if normalized in PROTECTED_SCOPE_GLOBS:
            return True
        if any(normalized.startswith(prefix) for prefix in PROTECTED_SCOPE_PREFIXES):
            return True
    return False


def _scope_has_runtime_or_validator_impact(scope: list[str]) -> bool:
    for entry in scope:
        normalized = _scope_entry(entry)
        name = Path(normalized).name.lower()
        if normalized.startswith("scripts/") or normalized.startswith("src/"):
            return True
        if normalized in {
            "scripts/check_hc_trust_engineer_output_contract.py",
            "scripts/hc_trust_engineer_local_emitter.py",
        }:
            return True
        if any(term in name for term in ("validator", "check", "governance", "emitter")):
            return True
    return False


def _input_suggests_automation_authority_change(data: dict[str, Any]) -> bool:
    explicit = data.get("automation_authority_change")
    if isinstance(explicit, bool):
        return explicit
    values = [
        str(data.get("next_action_title", "")),
        str(data.get("next_action_reason", "")),
        str(data.get("risk_reason", "")),
    ]
    return any(
        term in value.lower()
        for value in values
        for term in AUTOMATION_AUTHORITY_TERMS
    )


def _derive_risk_boundary(
    data: dict[str, Any], allowed_scope: list[str], forbidden_scope: list[str]
) -> dict[str, Any]:
    del forbidden_scope  # Forbidden-only paths are boundaries, not candidate touches.

    protected_paths_touched = _scope_has_protected_path(allowed_scope)
    runtime_or_validator_impact = _scope_has_runtime_or_validator_impact(allowed_scope)
    automation_authority_change = any(
        _scope_targets(entry, ".github/workflows") for entry in allowed_scope
    ) or _input_suggests_automation_authority_change(data)
    derived_high_risk = (
        protected_paths_touched
        or runtime_or_validator_impact
        or automation_authority_change
    )
    risk_level = "high" if derived_high_risk else data["risk_level"]

    return {
        "risk_level": risk_level,
        "protected_paths_touched": protected_paths_touched,
        "automation_authority_change": automation_authority_change,
        "runtime_or_validator_impact": runtime_or_validator_impact,
    }


def load_input(path: Path) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError as exc:
        raise EmitterInputError(f"input file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise EmitterInputError(f"invalid JSON in {path}: {exc}") from exc

    data = _require_mapping(data, "input")
    for field in REQUIRED_INPUT_FIELDS:
        if field not in data:
            raise EmitterInputError(f"missing required input field: {field}")

    status = _require_string(data, "chain_status")
    if status not in CHAIN_STATUS_VALUES:
        raise EmitterInputError(f"chain_status has invalid value: {status!r}")

    action_type = _require_string(data, "next_action_type")
    if action_type not in NEXT_ACTION_VALUES:
        raise EmitterInputError(f"next_action_type has invalid value: {action_type!r}")

    risk_level = _require_string(data, "risk_level")
    if risk_level not in RISK_LEVEL_VALUES:
        raise EmitterInputError(f"risk_level has invalid value: {risk_level!r}")

    open_pr_count = data["open_pr_count"]
    if not isinstance(open_pr_count, int) or open_pr_count < 0:
        raise EmitterInputError("open_pr_count must be a non-negative integer")

    _require_string(data, "repository")
    _require_string(data, "generated_at")
    _require_string(data, "evidence_window")
    _require_string(data, "chain_id")
    _require_string(data, "chain_type")
    _require_string(data, "next_action_title")
    _string_list(data, "recent_merged_prs")
    _string_list(data, "known_uncertainties")
    return data


def build_envelope(data: dict[str, Any]) -> dict[str, Any]:
    evidence_reviewed = _optional_string_list(
        data,
        "evidence_reviewed",
        ["Explicit local JSON input file; illustrative only, not live repository state."],
    )
    related_prs = _optional_string_list(data, "related_prs", data["recent_merged_prs"])
    chain_evidence = _optional_string_list(data, "chain_evidence", evidence_reviewed)
    allowed_scope = _optional_string_list(
        data,
        "allowed_scope",
        [
            "scripts/hc_trust_engineer_local_emitter.py",
            "tests/project_control/test_hc_trust_engineer_local_emitter.py",
            "tests/fixtures/project_control/**",
        ],
    )
    forbidden_scope = _optional_string_list(
        data,
        "forbidden_scope",
        ["records/**", "schema/**", ".github/workflows/**"],
    )
    if "schema/**" not in forbidden_scope:
        forbidden_scope.append("schema/**")
    forbidden_scope = [item for item in forbidden_scope if item != "schemas/**"]
    risk_boundary = _derive_risk_boundary(data, allowed_scope, forbidden_scope)

    return {
        "report_type": "hc_trust_engineer_operating_loop",
        "generated_at": data["generated_at"],
        "repository": data["repository"],
        "source_of_truth": "Explicit local JSON input file; no live repository-state reading",
        "evidence_window": data["evidence_window"],
        **HARD_BOUNDARIES,
        "hard_boundary_markers": list(REQUIRED_MARKERS),
        "outputs": [
            {
                "section": "STATE_SUMMARY",
                "summary": data.get(
                    "state_summary",
                    "Local report-only HC Trust Engineer Operating Loop envelope built from explicit input.",
                ),
                "evidence_reviewed": evidence_reviewed,
                "open_pr_count": data["open_pr_count"],
                "recent_merged_prs": data["recent_merged_prs"],
                "known_uncertainties": data["known_uncertainties"],
            },
            {
                "section": "CHAIN_STATUS",
                "chain_id": data["chain_id"],
                "chain_type": data["chain_type"],
                "related_prs": related_prs,
                "status": data["chain_status"],
                "evidence": chain_evidence,
                "uncertainty": data["known_uncertainties"],
            },
            {
                "section": "NEXT_ACTION_CANDIDATE",
                "action_type": data["next_action_type"],
                "title": data["next_action_title"],
                "reason": data.get(
                    "next_action_reason",
                    "Candidate next action is advisory and requires human review before use.",
                ),
                "allowed_scope": allowed_scope,
                "forbidden_scope": forbidden_scope,
                "expected_risk": risk_boundary["risk_level"],
                "human_decision_required": True,
            },
            {
                "section": "RISK_BOUNDARY_CLASSIFICATION",
                "risk_level": risk_boundary["risk_level"],
                "reason": data.get(
                    "risk_reason",
                    "Local-only report output does not grant automation authority or mutate repository state.",
                ),
                "protected_paths_touched": risk_boundary["protected_paths_touched"],
                "automation_authority_change": risk_boundary["automation_authority_change"],
                "runtime_or_validator_impact": risk_boundary["runtime_or_validator_impact"],
            },
            {
                "section": "HUMAN_HANDOFF_NOTE",
                "recommendation": data.get(
                    "handoff_recommendation",
                    "Human maintainer should review the advisory envelope and decide any next step.",
                ),
                "decision_needed": data.get(
                    "decision_needed", "Accept, revise, defer, or reject the advisory next-action candidate."
                ),
                "safe_next_step": data.get(
                    "safe_next_step", "Run local validation and review the emitted JSON before any action."
                ),
                "do_not_do": data.get(
                    "do_not_do",
                    "Do not comment, label, approve, merge, or mutate repository state automatically.",
                ),
                "final_authority": "Human maintainer",
            },
        ],
    }


def emit_from_file(path: Path) -> dict[str, Any]:
    envelope = build_envelope(load_input(path))
    validate_contract(envelope)
    return envelope


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Emit a local-only HC Trust Engineer Operating Loop envelope."
    )
    parser.add_argument("--input", required=True, type=Path, help="explicit local JSON input file")
    args = parser.parse_args(argv)

    try:
        envelope = emit_from_file(args.input)
    except (EmitterInputError, ContractError) as exc:
        print(f"HC Trust Engineer local emitter failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(envelope, indent=2, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
