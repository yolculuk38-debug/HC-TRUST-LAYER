#!/usr/bin/env python3
"""Deterministic local task planner for HC Engineer.

This module converts a local JSON fixture into an ordered, advisory PR plan.
It intentionally avoids network calls, LLM calls, subprocess execution, repository
writes, secret reads, workflow changes, and GitHub actions such as opening,
approving, rejecting, merging, closing, labeling, assigning, or requesting review.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.hc_control_bot import scan_changed_paths

FAILURE_CONCLUSIONS = {"failure", "cancelled", "timed_out", "action_required"}
PENDING_STATUSES = {"queued", "in_progress", "requested", "waiting", "pending"}
SUCCESS_CONCLUSIONS = {"success", "neutral"}
MANUAL_REVIEW_CONCLUSIONS = {"skipped"}


@dataclass(frozen=True)
class HCEngineerTaskPlan:
    """Machine-readable advisory task plan for HC Engineer."""

    advisory_only: bool
    public_safe: bool
    truth_guarantee: bool
    task_title: str
    planned_prs: list[dict[str, Any]]
    planned_pr_count: int
    stop_conditions: list[str]
    review_order: list[str]
    merge_gate: dict[str, Any]
    post_merge_cleanup: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "advisory_only": self.advisory_only,
            "public_safe": self.public_safe,
            "truth_guarantee": self.truth_guarantee,
            "task_title": self.task_title,
            "planned_prs": self.planned_prs,
            "planned_pr_count": self.planned_pr_count,
            "stop_conditions": self.stop_conditions,
            "review_order": self.review_order,
            "merge_gate": self.merge_gate,
            "post_merge_cleanup": self.post_merge_cleanup,
        }


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _str_list(value: Any) -> list[str]:
    return sorted({str(item) for item in _as_list(value) if str(item).strip()})


def _normalize_checks(value: Any) -> list[dict[str, str | None]]:
    checks: list[dict[str, str | None]] = []
    for item in _as_list(value):
        if not isinstance(item, dict):
            continue
        conclusion = item.get("conclusion")
        checks.append(
            {
                "name": str(item.get("name", "unknown")),
                "status": str(item.get("status", "unknown")),
                "conclusion": None if conclusion is None else str(conclusion),
            }
        )
    return sorted(checks, key=lambda check: (check["name"], check["status"], str(check["conclusion"])))


def _unresolved_comments(fixture: dict[str, Any]) -> list[str]:
    return _str_list(
        fixture.get("unresolved_review_comments")
        or fixture.get("unresolved_comments")
        or fixture.get("review_comments")
        or []
    )


def _build_stop_conditions(
    *,
    open_prs: list[str],
    unresolved_comments: list[str],
    checks: list[dict[str, str | None]],
    protected_paths: list[str],
    human_review_required: bool,
) -> list[str]:
    stop_conditions: list[str] = []
    if open_prs:
        stop_conditions.append("open_pr_exists_stop_before_starting_new_work")
    if unresolved_comments:
        stop_conditions.append("unresolved_review_comments_resolve_before_checks_or_merge")
    if any(check["status"] in PENDING_STATUSES for check in checks):
        stop_conditions.append("checks_pending_merge_blocked")
    if any(check["conclusion"] in FAILURE_CONCLUSIONS for check in checks):
        stop_conditions.append("checks_failed_merge_blocked")
    if any(check["conclusion"] in MANUAL_REVIEW_CONCLUSIONS for check in checks):
        stop_conditions.append("checks_skipped_require_human_review")
    if protected_paths:
        stop_conditions.append("protected_paths_require_human_review")
    if human_review_required:
        stop_conditions.append("scanner_human_review_required")
    return sorted(set(stop_conditions))


def _build_review_order(
    *,
    open_prs: list[str],
    unresolved_comments: list[str],
    checks: list[dict[str, str | None]],
    protected_paths: list[str],
    human_review_required: bool,
) -> list[str]:
    order: list[str] = []
    if open_prs:
        order.append("Stop new work until existing open PRs are resolved to preserve one-open-PR discipline.")
    order.append("Confirm the task fixture and changed-path scope are local-only and public-safe.")
    if protected_paths:
        order.append("Request human review for protected or trust-kernel-adjacent paths before merge consideration.")
    elif human_review_required:
        order.append("Request human review for scanner-marked governance, version-alignment, or sensitive review routes before merge consideration.")
    if unresolved_comments:
        order.append("Resolve Codex and human review comments before inspecting checks or considering merge.")
    order.append("Inspect required checks after review comments are resolved.")
    if checks:
        order.append("Treat pending, failed, or skipped checks as merge blockers until they pass or are explicitly reviewed by a human maintainer.")
    order.append("Merge only after one-open-PR discipline, review resolution, required human review, and required checks are satisfied.")
    return order


def _planned_prs(
    task_title: str,
    changed_files: list[str],
    protected_paths: list[str],
    human_review_required: bool,
) -> list[dict[str, Any]]:
    summary = "Implement the requested HC Engineer task-planning change as one small, reviewable PR."
    if changed_files and all(path.startswith(("docs/", "examples/")) for path in changed_files):
        summary = "Add or update documentation/example-only task-planning material in one small PR."
    if protected_paths:
        summary = "Do not begin protected-path work without explicit human review and justification."
    return [
        {
            "order": 1,
            "title": task_title,
            "scope": summary,
            "expected_files": changed_files,
            "human_review_required": human_review_required,
            "preserves_one_open_pr_discipline": True,
        }
    ]


def _merge_gate(
    *,
    stop_conditions: list[str],
    checks: list[dict[str, str | None]],
    unresolved_comments: list[str],
    protected_paths: list[str],
    human_review_required: bool,
) -> dict[str, Any]:
    check_blockers = [condition for condition in stop_conditions if condition.startswith("checks_")]
    review_blockers = [condition for condition in stop_conditions if "review" in condition or "comments" in condition]
    allowed = not stop_conditions and bool(checks) and all(
        check["status"] == "completed" and check["conclusion"] in SUCCESS_CONCLUSIONS
        for check in checks
    )
    return {
        "allowed": allowed,
        "state": "allowed_after_checks" if allowed else "blocked_or_waiting",
        "blocked_by": stop_conditions,
        "requires_checks_inspection": True,
        "requires_review_resolution_first": bool(unresolved_comments),
        "requires_human_review": human_review_required,
        "check_blockers": check_blockers,
        "review_blockers": review_blockers,
    }


def build_plan(fixture: dict[str, Any]) -> HCEngineerTaskPlan:
    """Build deterministic advisory PR planning JSON from a local fixture."""

    task_title = str(fixture.get("task_title") or fixture.get("title") or "Untitled HC Engineer task")
    changed_files = _str_list(fixture.get("changed_files") or fixture.get("touched_paths") or [])
    open_prs = _str_list(fixture.get("open_prs"))
    unresolved_comments = _unresolved_comments(fixture)
    checks = _normalize_checks(fixture.get("checks"))
    scan = scan_changed_paths(changed_files).to_dict()
    protected_paths = _str_list(scan.get("protected_paths_touched"))
    human_review_required = bool(scan.get("human_review_required"))

    stop_conditions = _build_stop_conditions(
        open_prs=open_prs,
        unresolved_comments=unresolved_comments,
        checks=checks,
        protected_paths=protected_paths,
        human_review_required=human_review_required,
    )

    return HCEngineerTaskPlan(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        task_title=task_title,
        planned_prs=_planned_prs(task_title, changed_files, protected_paths, human_review_required),
        planned_pr_count=1,
        stop_conditions=stop_conditions,
        review_order=_build_review_order(
            open_prs=open_prs,
            unresolved_comments=unresolved_comments,
            checks=checks,
            protected_paths=protected_paths,
            human_review_required=human_review_required,
        ),
        merge_gate=_merge_gate(
            stop_conditions=stop_conditions,
            checks=checks,
            unresolved_comments=unresolved_comments,
            protected_paths=protected_paths,
            human_review_required=human_review_required,
        ),
        post_merge_cleanup=[
            "Confirm the merged PR is closed before starting another PR.",
            "Preserve local fixture evidence for audit-friendly follow-up.",
            "Do not perform labels, assignments, approvals, closure, or merge actions from this planner.",
        ],
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a deterministic advisory HC Engineer task plan from a local JSON fixture."
    )
    parser.add_argument("fixture", help="Path to a local JSON fixture.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    fixture = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    indent = 2 if args.pretty else None
    print(json.dumps(build_plan(fixture).to_dict(), indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
