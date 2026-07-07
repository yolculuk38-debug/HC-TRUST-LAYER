#!/usr/bin/env python3
"""Deterministic local command parser for HC Council commands.

This module intentionally avoids network calls, provider calls, subprocess
execution, repository writes, labels, assignments, approvals, merges, and issue
closure. It only normalizes local command text into public-safe JSON.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "0.1"
PREFIX = ("/hc", "council")
REPORT_ONLY_ACTIONS = {"status", "risks", "evidence", "daily"}
REVIEW_TARGETS = {"repo", "pr"}


@dataclass(frozen=True)
class CouncilCommandResult:
    schema_version: str
    mode: str
    advisory_only: bool
    public_safe: bool
    truth_guarantee: bool
    command: str
    accepted: bool
    action: str | None
    target_type: str | None
    target_number: int | None
    evidence_refs: list[str]
    stop_reasons: list[str]
    warnings: list[str]
    next_action: str
    evidence_source: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "mode": self.mode,
            "advisory_only": self.advisory_only,
            "public_safe": self.public_safe,
            "truth_guarantee": self.truth_guarantee,
            "command": self.command,
            "accepted": self.accepted,
            "action": self.action,
            "target_type": self.target_type,
            "target_number": self.target_number,
            "evidence_refs": self.evidence_refs,
            "stop_reasons": self.stop_reasons,
            "warnings": self.warnings,
            "next_action": self.next_action,
            "evidence_source": self.evidence_source,
        }


def _as_str_list(value: Any) -> list[str]:
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    return sorted({str(item).strip() for item in items if str(item).strip()})


def _tokenize(command: str) -> list[str]:
    return re.sub(r"\s+", " ", command.strip()).split(" ") if command.strip() else []


def _stop(command: str, reason: str) -> CouncilCommandResult:
    return CouncilCommandResult(
        schema_version=SCHEMA_VERSION,
        mode="report_only",
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        command=command.strip(),
        accepted=False,
        action=None,
        target_type=None,
        target_number=None,
        evidence_refs=[],
        stop_reasons=[reason],
        warnings=[],
        next_action="stop",
        evidence_source="local command text only",
    )


def parse_command(command: str, *, evidence_refs: list[str] | None = None) -> CouncilCommandResult:
    """Parse one local HC Council command into a deterministic advisory result."""

    normalized_command = command.strip()
    tokens = _tokenize(normalized_command)
    refs = _as_str_list(evidence_refs)

    if len(tokens) < 3:
        return _stop(normalized_command, "command_too_short")
    if tuple(tokens[:2]) != PREFIX:
        return _stop(normalized_command, "invalid_prefix")

    action = tokens[2]

    if action in REPORT_ONLY_ACTIONS:
        if len(tokens) != 3:
            return _stop(normalized_command, "unexpected_arguments")
        return CouncilCommandResult(
            schema_version=SCHEMA_VERSION,
            mode="report_only",
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            command=normalized_command,
            accepted=True,
            action=action,
            target_type=None,
            target_number=None,
            evidence_refs=refs,
            stop_reasons=[],
            warnings=[],
            next_action="run_report_only_status",
            evidence_source="local command text only",
        )

    if action != "review":
        return _stop(normalized_command, "unknown_action")

    if len(tokens) < 4:
        return _stop(normalized_command, "missing_review_target")

    target = tokens[3]
    if target not in REVIEW_TARGETS:
        return _stop(normalized_command, "unknown_review_target")

    if target == "repo":
        if len(tokens) != 4:
            return _stop(normalized_command, "unexpected_arguments")
        return CouncilCommandResult(
            schema_version=SCHEMA_VERSION,
            mode="report_only",
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            command=normalized_command,
            accepted=True,
            action=action,
            target_type="repo",
            target_number=None,
            evidence_refs=refs,
            stop_reasons=[],
            warnings=["repo_review_requires_current_gate_snapshot"],
            next_action="build_council_fixture",
            evidence_source="local command text only",
        )

    if len(tokens) != 5:
        return _stop(normalized_command, "invalid_pr_review_syntax")

    try:
        pr_number = int(tokens[4])
    except ValueError:
        return _stop(normalized_command, "invalid_pr_number")

    if pr_number < 1:
        return _stop(normalized_command, "invalid_pr_number")

    return CouncilCommandResult(
        schema_version=SCHEMA_VERSION,
        mode="report_only",
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        command=normalized_command,
        accepted=True,
        action=action,
        target_type="pr",
        target_number=pr_number,
        evidence_refs=refs,
        stop_reasons=[],
        warnings=["pr_review_requires_live_github_gate_snapshot"],
        next_action="build_council_fixture",
        evidence_source="local command text only",
    )


def parse_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    command = str(fixture.get("command", ""))
    refs = _as_str_list(fixture.get("evidence_refs", []))
    return parse_command(command, evidence_refs=refs).to_dict()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parse a local HC Council command into report-only JSON."
    )
    parser.add_argument("fixture", help="Path to a local JSON fixture containing command text.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    fixture = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    result = parse_fixture(fixture)
    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
