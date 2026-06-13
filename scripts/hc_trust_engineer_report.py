#!/usr/bin/env python3
"""Deterministic report-only runner for HC Trust Engineer.

This module intentionally avoids network calls, LLM calls, subprocess execution,
repository writes, labels, assignments, approvals, merges, and issue closure.
It turns local event fixtures into public-safe advisory JSON.
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


@dataclass(frozen=True)
class EngineerReport:
    """Machine-readable HC Trust Engineer report."""

    agent: str
    mode: str
    advisory_only: bool
    public_safe: bool
    truth_guarantee: bool
    repository: str
    event_type: str
    target_number: int | None
    base_sha: str | None
    head_sha: str | None
    open_prs: list[int]
    changed_files: list[str]
    risk_flags: list[str]
    required_human_review: bool
    checks: list[dict[str, Any]]
    unresolved_threads: list[str]
    missing_evidence: list[str]
    recommended_next_action: str
    stop_reasons: list[str]
    scan: dict[str, Any]
    evidence_source: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "agent": self.agent,
            "mode": self.mode,
            "advisory_only": self.advisory_only,
            "public_safe": self.public_safe,
            "truth_guarantee": self.truth_guarantee,
            "repository": self.repository,
            "event_type": self.event_type,
            "target_number": self.target_number,
            "base_sha": self.base_sha,
            "head_sha": self.head_sha,
            "open_prs": self.open_prs,
            "changed_files": self.changed_files,
            "risk_flags": self.risk_flags,
            "required_human_review": self.required_human_review,
            "checks": self.checks,
            "unresolved_threads": self.unresolved_threads,
            "missing_evidence": self.missing_evidence,
            "recommended_next_action": self.recommended_next_action,
            "stop_reasons": self.stop_reasons,
            "scan": self.scan,
            "evidence_source": self.evidence_source,
        }


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _as_str_list(value: Any) -> list[str]:
    return sorted({str(item) for item in _as_list(value) if str(item).strip()})


def _as_int_list(value: Any) -> list[int]:
    items: list[int] = []
    for item in _as_list(value):
        try:
            items.append(int(item))
        except (TypeError, ValueError):
            continue
    return sorted(set(items))


def _normalize_checks(value: Any) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for item in _as_list(value):
        if isinstance(item, dict):
            name = str(item.get("name", "unknown"))
            status = str(item.get("status", "unknown"))
            conclusion = item.get("conclusion")
            checks.append(
                {
                    "name": name,
                    "status": status,
                    "conclusion": None if conclusion is None else str(conclusion),
                }
            )
    return sorted(
        checks, key=lambda entry: (entry["name"], entry["status"], str(entry["conclusion"]))
    )


def _build_stop_reasons(
    *,
    open_prs: list[int],
    checks: list[dict[str, Any]],
    unresolved_threads: list[str],
    missing_evidence: list[str],
    scan: dict[str, Any],
) -> list[str]:
    reasons: list[str] = []

    if len(open_prs) > 1:
        reasons.append("multiple_open_prs")
    if any(str(check.get("status")) in PENDING_STATUSES for check in checks):
        reasons.append("checks_pending")
    if any(str(check.get("conclusion")) in FAILURE_CONCLUSIONS for check in checks):
        reasons.append("checks_failed")
    if unresolved_threads:
        reasons.append("unresolved_review_threads")
    if missing_evidence:
        reasons.append("missing_evidence")
    if scan.get("protected_paths_touched"):
        reasons.append("protected_paths_touched")
    if scan.get("version_alignment_paths_touched"):
        reasons.append("version_alignment_review_required")

    return sorted(set(reasons))


def build_report(fixture: dict[str, Any]) -> EngineerReport:
    """Build a deterministic advisory report from a local fixture."""

    changed_files = _as_str_list(fixture.get("changed_files", []))
    open_prs = _as_int_list(fixture.get("open_prs", []))
    checks = _normalize_checks(fixture.get("checks", []))
    unresolved_threads = _as_str_list(fixture.get("unresolved_threads", []))
    missing_evidence = _as_str_list(fixture.get("missing_evidence", []))
    scan = scan_changed_paths(changed_files).to_dict()

    stop_reasons = _build_stop_reasons(
        open_prs=open_prs,
        checks=checks,
        unresolved_threads=unresolved_threads,
        missing_evidence=missing_evidence,
        scan=scan,
    )
    risk_flags = sorted(
        set(stop_reasons)
        | set(_as_str_list(scan.get("warnings", [])))
        | set(_as_str_list(scan.get("review_routes", [])))
    )
    required_human_review = bool(
        stop_reasons
        or scan.get("human_review_required")
        or unresolved_threads
        or missing_evidence
    )

    return EngineerReport(
        agent="HC Trust Engineer",
        mode="report_only",
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        repository=str(fixture.get("repository", "")),
        event_type=str(fixture.get("event_type", "unknown")),
        target_number=fixture.get("target_number"),
        base_sha=fixture.get("base_sha"),
        head_sha=fixture.get("head_sha"),
        open_prs=open_prs,
        changed_files=changed_files,
        risk_flags=risk_flags,
        required_human_review=required_human_review,
        checks=checks,
        unresolved_threads=unresolved_threads,
        missing_evidence=missing_evidence,
        recommended_next_action="stop" if stop_reasons else "continue",
        stop_reasons=stop_reasons,
        scan=scan,
        evidence_source="local fixture and changed file path metadata only",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a deterministic HC Trust Engineer report from a local JSON fixture."
    )
    parser.add_argument("fixture", help="Path to local JSON fixture.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    fixture = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    report = build_report(fixture).to_dict()
    indent = 2 if args.pretty else None
    print(json.dumps(report, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
