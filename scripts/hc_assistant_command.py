#!/usr/bin/env python3
"""Deterministic non-LLM command parser for HC Trust Engineer.

This module intentionally avoids network calls, LLM calls, repository writes,
workflow actions, labels, approvals, merge decisions, and issue state changes.
It only parses explicit `/hc` commands and returns public-safe advisory output.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

SUPPORTED_COMMANDS: tuple[str, ...] = (
    "help",
    "status",
    "next",
    "evidence",
)

HELP_LINES: tuple[str, ...] = (
    "HC Trust Engineer commands:",
    "- /hc help",
    "- /hc status",
    "- /hc next",
    "- /hc evidence",
    "- /hc explain <topic-or-path> (documented, not implemented in this parser)",
    "Boundary: advisory only. Human maintainers retain final authority.",
)

STATUS_LINES: tuple[str, ...] = (
    "HC Trust Engineer command surface status:",
    "- assistant_console_issue: #763",
    "- command_interface: documented",
    "- assistant_console_guide: documented",
    "- command_parser: local deterministic parser",
    "- automation_status: not connected to issue comments yet",
    "- authority: advisory only; human maintainers retain final authority",
)

NEXT_LINES: tuple[str, ...] = (
    "HC Trust Engineer next safe task:",
    "- mode: REPORT ONLY",
    "- next_action: evidence-triggered runtime or planning follow-up only if new repository evidence appears",
    "- scope: narrow evidence report, navigation refresh, or implementation planning only when triggered by concrete repo evidence",
    "- blocked_work: do not modify runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy from this command output",
    "- avoid: duplicate public validator/public explorer planning and unrequested implementation expansion",
    "- source: docs/project-control/next-actions.md",
    "- before_acting: read docs/project-control/next-actions.md directly and confirm new repository evidence or explicit authorization exists",
    "Boundary: advisory only. Human maintainers retain final authority.",
)

EVIDENCE_LINES: tuple[str, ...] = (
    "HC Trust Engineer evidence bundle checklist:",
    "- changed_files: list every file path touched",
    "- scope: state whether the change is docs-only, runtime, workflow, schema, validator, record, generated artifact, policy, federation, or governance-adjacent",
    "- source_of_truth: cite live GitHub state and trusted main-branch docs when available",
    "- checks: include relevant CI/check results or state that checks are not yet available",
    "- protected_path_assessment: state whether protected or trust-kernel-adjacent paths are touched",
    "- advisory_boundary: confirm advisory_only=true, public_safe=true, truth_guarantee=false",
    "- human_review: state whether human review is required before merge or implementation expansion",
    "- do_not_claim: do not claim approval, rejection, merge authority, production readiness, legal validity, or objective truth",
    "Boundary: advisory only. Human maintainers retain final authority.",
)


@dataclass(frozen=True)
class CommandResult:
    """Machine-readable advisory result for an HC assistant command."""

    advisory_only: bool
    public_safe: bool
    truth_guarantee: bool
    human_review_required: bool
    command_prefix: str
    command: str
    implemented: bool
    response_lines: list[str]
    warnings: list[str]
    evidence_source: str

    def to_dict(self) -> dict[str, object]:
        return {
            "advisory_only": self.advisory_only,
            "public_safe": self.public_safe,
            "truth_guarantee": self.truth_guarantee,
            "human_review_required": self.human_review_required,
            "command_prefix": self.command_prefix,
            "command": self.command,
            "implemented": self.implemented,
            "response_lines": self.response_lines,
            "warnings": self.warnings,
            "evidence_source": self.evidence_source,
        }


def _normalize_command(raw_text: str) -> tuple[str, list[str]]:
    parts = raw_text.strip().split()
    if not parts:
        return "", []
    prefix = parts[0].strip().lower()
    if prefix != "/hc":
        return "", parts[1:]
    if len(parts) == 1:
        return "help", []
    return parts[1].strip().lower(), parts[2:]


def parse_hc_command(raw_text: str) -> CommandResult:
    """Parse an explicit `/hc` command without executing any repository action."""

    command, _args = _normalize_command(raw_text)

    if command == "help":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=False,
            command_prefix="/hc",
            command="help",
            implemented=True,
            response_lines=list(HELP_LINES),
            warnings=[],
            evidence_source="static command interface only",
        )

    if command == "status":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=False,
            command_prefix="/hc",
            command="status",
            implemented=True,
            response_lines=list(STATUS_LINES),
            warnings=[
                "This local parser does not perform live GitHub state lookup.",
                "Use a separate GitHub-verified control pass for current PR state.",
            ],
            evidence_source="static command interface only",
        )

    if command == "next":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=False,
            command_prefix="/hc",
            command="next",
            implemented=True,
            response_lines=list(NEXT_LINES),
            warnings=[
                "This local parser does not perform live GitHub state lookup.",
                "Proceed only if new repository evidence appears or an authorized reviewer requests implementation planning.",
                "Read docs/project-control/next-actions.md directly before acting on this static summary.",
            ],
            evidence_source="static project-control guidance from docs/project-control/next-actions.md",
        )

    if command == "evidence":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=True,
            command_prefix="/hc",
            command="evidence",
            implemented=True,
            response_lines=list(EVIDENCE_LINES),
            warnings=[
                "This local parser does not inspect the current PR or issue context.",
                "Attach live GitHub evidence separately before acting on this checklist.",
                "This checklist is not approval, rejection, merge authority, or a truth guarantee.",
            ],
            evidence_source="static evidence checklist from HC assistant command interface",
        )

    if command in {"explain", "review", "risks"}:
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=False,
            command_prefix="/hc",
            command=command,
            implemented=False,
            response_lines=[
                f"/hc {command} is documented but not implemented in this parser.",
                "Boundary: advisory only. Human maintainers retain final authority.",
            ],
            warnings=["Command is intentionally deferred for a later governance-reviewed PR."],
            evidence_source="static command interface only",
        )

    return CommandResult(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=False,
        command_prefix="/hc",
        command=command or "unknown",
        implemented=False,
        response_lines=[
            "Unknown or unsupported command.",
            "Use /hc help for available commands.",
        ],
        warnings=["Unsupported command ignored; no repository action was taken."],
        evidence_source="static command interface only",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parse deterministic HC Trust Engineer assistant commands."
    )
    parser.add_argument(
        "command_text",
        nargs="*",
        help="Command text such as '/hc help' or '/hc status'.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    raw_text = " ".join(args.command_text)
    result = parse_hc_command(raw_text).to_dict()
    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
