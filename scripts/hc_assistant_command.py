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
    "explain",
    "risks",
    "review",
)

HELP_LINES: tuple[str, ...] = (
    "HC Trust Engineer commands:",
    "- /hc help",
    "- /hc status",
    "- /hc next",
    "- /hc evidence",
    "- /hc explain <topic-or-path>",
    "- /hc risks",
    "- /hc review",
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

RISK_LINES: tuple[str, ...] = (
    "HC Trust Engineer risk checklist:",
    "- protected_path: schema, validators, records, signatures, policy, federation, runtime, governance, project-control, or workflow surfaces may require human-supervised review",
    "- workflow_risk: workflow changes can affect automation authority and must not run untrusted PR branch code",
    "- runtime_risk: runtime/API changes may affect public-safe response contracts and require tests",
    "- schema_validator_risk: schema or validator changes require compatibility and malformed-input evidence",
    "- record_hash_qr_risk: records, hashes, QR artifacts, and generated outputs must not imply truth, authenticity, or production readiness",
    "- governance_risk: governance and project-control docs can change operating authority and require careful review",
    "- stale_context_risk: chat memory or summaries must not outrank live GitHub state and trusted main-branch docs",
    "- implementation_risk: issue listeners, comments, labels, assignments, LLM, network, and repository writes require separate governance review",
    "Boundary: advisory only. This checklist does not decide PR outcome.",
)

REVIEW_LINES: tuple[str, ...] = (
    "HC Trust Engineer review preparation checklist:",
    "- collect_changed_files: list every changed path before review",
    "- classify_scope: identify docs, runtime, workflow, schema, validator, record, generated artifact, policy, federation, governance, or project-control scope",
    "- check_protected_paths: verify whether trust-kernel or governance-sensitive paths are touched",
    "- attach_evidence_bundle: include changed files, CI/check status, source-of-truth docs, and human-review requirement",
    "- inspect_ci_status: wait for required checks and record pending or failed checks honestly",
    "- compare_against_next_actions: do not revive completed or duplicate work without new repository evidence",
    "- preserve_boundaries: confirm advisory_only=true, public_safe=true, truth_guarantee=false",
    "- human_decision: leave approve, reject, merge, close, labels, and assignments to authorized human maintainers or explicit governance workflows",
    "Boundary: advisory only. This checklist prepares human review but does not perform review decisions.",
)

EXPLAIN_TOPICS: dict[str, tuple[str, ...]] = {
    "advisory-only": (
        "HC advisory-only means the system can observe, explain, warn, and suggest.",
        "It must not approve, reject, merge, close, certify, or guarantee truth.",
        "Human maintainers retain final authority.",
    ),
    "trust-kernel": (
        "The trust-kernel is the protected verification core of HC-TRUST-LAYER.",
        "It includes schema, validators, records, signatures, policy, federation, runtime, and governance-sensitive surfaces.",
        "Changes near the trust-kernel require human-supervised review and evidence.",
    ),
    "protected-paths": (
        "Protected paths are repository areas that require explicit human review before modification.",
        "Examples include schema/**, validators/**, records/**, signatures/**, policy/**, federation/**, src/hc_runtime/**, docs/governance/**, docs/project-control/**, and .github/workflows/**.",
        "The assistant may warn about these paths but must not override maintainers.",
    ),
    "commands": (
        "HC Trust Engineer commands use the /hc prefix.",
        "Implemented local commands include help, status, next, evidence, explain, risks, and review.",
        "The parser is local, deterministic, non-LLM, and not connected to issue comments yet.",
    ),
}


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


def _normalize_topic(args: list[str]) -> str:
    return " ".join(args).strip().lower().replace("_", "-")


def _build_explain_lines(args: list[str]) -> tuple[list[str], list[str]]:
    topic = _normalize_topic(args)
    if not topic:
        return (
            [
                "HC Trust Engineer explain topics:",
                "- advisory-only",
                "- trust-kernel",
                "- protected-paths",
                "- commands",
                "Boundary: advisory only. Human maintainers retain final authority.",
            ],
            ["No topic was provided; returning available static topics."],
        )

    if topic in EXPLAIN_TOPICS:
        return (
            [f"HC Trust Engineer explanation: {topic}", *EXPLAIN_TOPICS[topic], "Boundary: advisory only. Human maintainers retain final authority."],
            [],
        )

    return (
        [
            f"No static explanation is available for: {topic}",
            "Use /hc explain with one of: advisory-only, trust-kernel, protected-paths, commands.",
            "Boundary: advisory only. Human maintainers retain final authority.",
        ],
        ["Unknown explain topic ignored; no repository action was taken."],
    )


def parse_hc_command(raw_text: str) -> CommandResult:
    """Parse an explicit `/hc` command without executing any repository action."""

    command, args = _normalize_command(raw_text)

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

    if command == "explain":
        response_lines, warnings = _build_explain_lines(args)
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=False,
            command_prefix="/hc",
            command="explain",
            implemented=True,
            response_lines=response_lines,
            warnings=warnings,
            evidence_source="static explain topic map only",
        )

    if command == "risks":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=True,
            command_prefix="/hc",
            command="risks",
            implemented=True,
            response_lines=list(RISK_LINES),
            warnings=[
                "This local parser does not inspect the current PR or issue context.",
                "Use live changed-file evidence before applying this checklist to a specific PR.",
                "This checklist is not approval, rejection, merge authority, or a truth guarantee.",
            ],
            evidence_source="static risk checklist from HC assistant command interface",
        )

    if command == "review":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=True,
            command_prefix="/hc",
            command="review",
            implemented=True,
            response_lines=list(REVIEW_LINES),
            warnings=[
                "This local parser does not inspect the current PR or issue context.",
                "Attach live changed-file, CI, and review-thread evidence before using this checklist.",
                "This checklist is not approval, rejection, merge authority, or a truth guarantee.",
            ],
            evidence_source="static review preparation checklist from HC assistant command interface",
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
