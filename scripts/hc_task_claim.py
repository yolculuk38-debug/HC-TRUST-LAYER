#!/usr/bin/env python3
"""Evaluate a local HC task claim fixture.

This script converts one local JSON task-claim fixture into a deterministic,
machine-readable advisory claim report. It does not call a network, subprocess,
LLM, GitHub API, workflow API, or repository write API. It only reads a local
JSON fixture and prints JSON to stdout.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

TASK_ID_RE = re.compile(r"^HC-TASK-\d{4}-\d{3}$")
SUPPORTED_ACTIONS = {"claim", "release", "status"}
SUPPORTED_STATES = {
    "proposed",
    "ready",
    "claimed",
    "in_progress",
    "pr_open",
    "completed",
    "released",
    "blocked",
    "stale",
}
ACTIVE_CLAIM_STATES = {"active", "in_progress", "pr_open"}


@dataclass(frozen=True)
class HCTaskClaimReport:
    task_id: str
    task_title: str
    requested_action: str
    current_state: str
    normalized_state: str
    claim_allowed: bool
    claim_status: str
    blockers: list[str]
    warnings: list[str]
    next_human_action: str
    evidence_source: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "advisory_only": True,
            "public_safe": True,
            "truth_guarantee": False,
            "human_review_required": True,
            "repository_mutation": False,
            "issue_comment_automation": False,
            "label_reviewer_mutation": False,
            "approval_authority": False,
            "merge_authority": False,
            "task_id": self.task_id,
            "task_title": self.task_title,
            "requested_action": self.requested_action,
            "current_state": self.current_state,
            "normalized_state": self.normalized_state,
            "claim_allowed": self.claim_allowed,
            "claim_status": self.claim_status,
            "blockers": self.blockers,
            "warnings": self.warnings,
            "next_human_action": self.next_human_action,
            "evidence_source": self.evidence_source,
        }


def _load_fixture(path: str | Path) -> dict[str, Any]:
    fixture_path = Path(path)
    with fixture_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("claim fixture must be a JSON object")
    return payload


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _has_active_duplicate_claim(existing_claims: list[Any], task_id: str) -> bool:
    for claim in existing_claims:
        if not isinstance(claim, dict):
            continue
        if str(claim.get("task_id", "")) != task_id:
            continue
        state = str(claim.get("state", claim.get("claim_state", ""))).strip().lower()
        if state in ACTIVE_CLAIM_STATES:
            return True
    return False


def _normalize_state(state: Any) -> str:
    normalized = str(state or "").strip().lower()
    return normalized if normalized in SUPPORTED_STATES else "blocked"


def evaluate_claim(fixture: dict[str, Any]) -> HCTaskClaimReport:
    """Build a deterministic advisory claim report from a local fixture."""

    task_id = str(fixture.get("task_id", "")).strip()
    task_title = str(fixture.get("task_title", "")).strip()
    requested_action = str(fixture.get("requested_action", "claim")).strip().lower()
    current_state = str(fixture.get("current_state", "")).strip()
    normalized_state = _normalize_state(current_state)
    open_prs = _as_list(fixture.get("open_prs"))
    existing_claims = _as_list(fixture.get("existing_claims"))
    maintainer_acknowledged = bool(fixture.get("maintainer_acknowledged", False))

    blockers: list[str] = []
    warnings: list[str] = []

    if not TASK_ID_RE.match(task_id):
        blockers.append("invalid_task_id")
    if requested_action not in SUPPORTED_ACTIONS:
        warnings.append("unsupported_requested_action")
    if current_state.strip().lower() not in SUPPORTED_STATES:
        warnings.append("unsupported_current_state")
    if open_prs:
        blockers.append("open_pr_exists_do_not_duplicate")
    if _has_active_duplicate_claim(existing_claims, task_id):
        blockers.append("duplicate_active_claim")

    claim_allowed = False
    claim_status = "advisory_claim_blocked"
    next_human_action = "review_blockers_before_any_manual_action"

    if requested_action == "status":
        claim_status = "status_only"
        next_human_action = "review_advisory_status_only"
    elif requested_action == "release":
        if "invalid_task_id" not in blockers:
            claim_allowed = normalized_state in {"claimed", "in_progress", "stale", "blocked"}
        claim_status = "manual_release_ready" if claim_allowed and not open_prs else "advisory_claim_blocked"
        next_human_action = (
            "manually_review_release_request" if claim_allowed else "review_blockers_before_manual_release"
        )
    elif requested_action == "claim" and not blockers:
        if normalized_state == "ready":
            claim_allowed = True
            next_human_action = "manually_acknowledge_advisory_claim_or_decline"
        elif normalized_state == "stale" and maintainer_acknowledged:
            claim_allowed = True
            next_human_action = "manually_acknowledge_stale_task_claim_or_decline"
        elif normalized_state == "proposed":
            next_human_action = "maintainer_ready_decision_required"
        else:
            next_human_action = "do_not_claim_without_maintainer_review"
        claim_status = "advisory_claim_ready" if claim_allowed else "advisory_claim_blocked"

    if requested_action not in SUPPORTED_ACTIONS:
        claim_allowed = False
        claim_status = "advisory_claim_blocked"
        next_human_action = "choose_supported_requested_action"

    return HCTaskClaimReport(
        task_id=task_id,
        task_title=task_title,
        requested_action=requested_action,
        current_state=current_state,
        normalized_state=normalized_state,
        claim_allowed=claim_allowed,
        claim_status=claim_status,
        blockers=blockers,
        warnings=warnings,
        next_human_action=next_human_action,
        evidence_source="local task claim fixture",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate a deterministic local HC task claim fixture.")
    parser.add_argument("fixture", help="Path to a local JSON task-claim fixture.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    report = evaluate_claim(_load_fixture(args.fixture)).to_dict()
    print(json.dumps(report, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
