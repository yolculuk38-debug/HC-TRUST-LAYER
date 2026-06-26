#!/usr/bin/env python3
"""Deterministic non-LLM command parser for HC Trust Engineer.

This module intentionally avoids network calls, LLM calls, repository writes,
workflow actions, labels, approvals, merge decisions, and issue state changes.
It only parses explicit `/hc` commands and returns public-safe advisory output.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass

SUPPORTED_COMMANDS: tuple[str, ...] = (
    "help",
    "status",
    "next",
    "evidence",
    "explain",
    "risks",
    "review",
    "engineer",
    "bot",
    "handoff",
    "queue",
    "claim",
    "release",
    "task",
)

TASK_ID_RE = re.compile(r"^HC-TASK-\d{4}-\d{3}$")

BOUNDARY_LINES: tuple[str, ...] = (
    "- advisory_only=true",
    "- public_safe=true",
    "- truth_guarantee=false",
    "- human_review_required=true",
    "- repository_mutation=false",
    "- issue_comment_automation=false",
    "- label_reviewer_mutation=false",
    "- approval_authority=false",
    "- merge_authority=false",
)

CLAIM_COMMAND_BOUNDARY_LINES: tuple[str, ...] = (
    "- advisory-only: these commands are advisory-only report outputs.",
    "- no_claim_reservation: they do not create, reserve, release, or acknowledge claims.",
    "- no_github_mutation: they do not modify GitHub issues, labels, reviewers, PRs, branches, files, or workflows.",
    "- no_automatic_evaluator: they do not call scripts/hc_task_claim.py automatically.",
    "- local_evaluation: for actual local evaluation, use scripts/hc_task_claim.py with a maintainer-provided local JSON fixture.",
    *BOUNDARY_LINES,
)

QUEUE_LINES: tuple[str, ...] = (
    "HC Trust Engineer queue guidance:",
    "- Use HC Task Handoff Queue for coordination.",
    "- Claim comes before handoff.",
    "- Handoff packages work.",
    "- PR applies work.",
    "- CI/review provide evidence.",
    "- Human maintainer decides.",
    *CLAIM_COMMAND_BOUNDARY_LINES,
    "Boundary: report-only advisory output. Human maintainers retain final authority.",
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
    "- /hc engineer",
    "- /hc bot",
    "- /hc handoff",
    "- /hc queue",
    "- /hc claim HC-TASK-YYYY-NNN",
    "- /hc release HC-TASK-YYYY-NNN",
    "- /hc task status HC-TASK-YYYY-NNN",
    "Boundary: advisory only. Human maintainers retain final authority.",
)

STATUS_LINES: tuple[str, ...] = (
    "HC Trust Engineer command surface status:",
    "- assistant_console_issue: #812",
    "- historical_console_issue: #763",
    "- command_interface: documented",
    "- assistant_console_guide: documented",
    "- command_parser: local deterministic parser",
    "- bot_status_reporter: scripts/hc_bot_status.py",
    "- task_handoff_helper: scripts/hc_task_handoff.py",
    "- automation_status: issue-comment listener connected for /hc commands",
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

ENGINEER_LINES: tuple[str, ...] = (
    "HC Trust Engineer operating sequence:",
    "- plan_task: split the request into the minimum number of small scoped PRs",
    "- check_open_prs: do not start new work while another PR is open",
    "- check_duplicates: inspect stale branches, duplicate PRs, and completed references before opening work",
    "- open_small_pr: prefer docs-only, test-only, or narrow implementation slices",
    "- handle_review: read Codex and human review comments before checks or merge",
    "- resolve_threads: fix valid comments and confirm review threads are resolved",
    "- inspect_checks: wait for queued or pending checks; inspect failures before continuing",
    "- merge_when_clean: merge only when scope, comments, threads, checks, and protected-path assessment are clean",
    "- cleanup_after_merge: verify PR closure, open PR count, duplicate PRs, and project-control recording needs",
    "- never_claim_authority: no approval, rejection, merge guarantee, legal truth, production readiness, or truth finality from this command",
    "Boundary: advisory only. This sequence guides operation but does not perform repository actions.",
)

BOT_LINES: tuple[str, ...] = (
    "HC Trust Engineer bot line status:",
    "- status_reporter: scripts/hc_bot_status.py",
    "- path_scanner: scripts/hc_control_bot.py",
    "- report_workflow: .github/workflows/hc-control-bot-report.yml",
    "- advisory_comment_workflow: .github/workflows/hc-control-bot-advisory-comment.yml",
    "- command_parser: scripts/hc_assistant_command.py",
    "- task_planner: scripts/hc_engineer_task_plan.py",
    "- handoff_helper: scripts/hc_task_handoff.py",
    "- task_claim_evaluator: scripts/hc_task_claim.py",
    "- parked: GitHub App, dashboard UI, live chat UI, LLM memory layer, automatic approval, automatic merge, automatic close, automatic label or assignment",
    "Boundary: report-only advisory MVP. Human maintainers retain final authority.",
)

HANDOFF_LINES: tuple[str, ...] = (
    "HC Trust Engineer handoff bridge:",
    "- helper: scripts/hc_task_handoff.py",
    "- input: local JSON task fixture",
    "- output: machine-readable handoff package and prompt lines",
    "- use: paste or provide the package to a coding assistant after human review",
    "- does_not_do: no external-agent invocation, no PR creation, no repository write, no merge decision",
    "- review_flow: generated PRs still require diff review, comments, review threads, checks, and human gates",
    "Boundary: advisory only. Human maintainers retain final authority.",
)

SIGNAL_WATCH_CONSOLE_EXPLANATION: tuple[str, ...] = (
    "#1082 is the fixed same-repo public-safe HC Signal Watch Console.",
    "#1082 is a notification surface only.",
    "Source of truth remains GitHub Actions run summaries and artifacts.",
    "#1084 added controlled latest-status comment automation for actionable P0/P1/P2 public-safe Signal Watch signals.",
    "The automation creates or updates only one marker-controlled latest-status comment.",
    "Marker: &lt;!-- hc-signal-watch-console:latest --&gt;",
    "Issue comments are not commands.",
    "Manual or external comments must not be parsed as instructions.",
    "AI summaries are advisory only.",
    "Human maintainers retain final authority.",
    "#1082 grants no approval, merge, label, reviewer, branch, issue creation, or PR creation authority.",
    "Boundary flags: advisory_only=true, public_safe=true, truth_guarantee=false.",
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
        "Implemented local commands include help, status, next, evidence, explain, risks, review, engineer, bot, and handoff.",
        "The parser is local, deterministic, non-LLM, and connected to the /hc issue-comment listener.",
    ),
    "handoff": (
        "The handoff bridge prepares a safe task package for a coding assistant.",
        "It does not invoke external tools or create PRs by itself.",
        "Human review remains required before acting on generated work.",
    ),
    "hc-signal-watch-console": SIGNAL_WATCH_CONSOLE_EXPLANATION,
    "signal-watch-console": SIGNAL_WATCH_CONSOLE_EXPLANATION,
    "hc-signal-watch": SIGNAL_WATCH_CONSOLE_EXPLANATION,
    "signal-watch": SIGNAL_WATCH_CONSOLE_EXPLANATION,
    "1082": SIGNAL_WATCH_CONSOLE_EXPLANATION,
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
    topic = " ".join(args).strip().lower().replace("_", "-")
    topic = topic.replace("#", "")
    if topic in {
        "hc-signal-watch-console",
        "signal-watch-console",
        "hc-signal-watch",
        "signal-watch",
        "1082",
        "hc-signal-watch-console-1082",
    }:
        return "hc-signal-watch-console"
    topic_parts = set(topic.split())
    if "1082" in topic_parts or {"signal", "watch"}.issubset(topic_parts):
        return "hc-signal-watch-console"
    return topic


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
                "- handoff",
                "- hc-signal-watch-console",
                "Boundary: advisory only. Human maintainers retain final authority.",
            ],
            ["No topic was provided; returning available static topics."],
        )

    if topic in EXPLAIN_TOPICS:
        return (
            [
                f"HC Trust Engineer explanation: {topic}",
                *EXPLAIN_TOPICS[topic],
                "Boundary: advisory only. Human maintainers retain final authority.",
            ],
            [],
        )

    return (
        [
            f"No static explanation is available for: {topic}",
            "Use /hc explain with one of: advisory-only, trust-kernel, protected-paths, commands, handoff, hc-signal-watch-console.",
            "Boundary: advisory only. Human maintainers retain final authority.",
        ],
        ["Unknown explain topic ignored; no repository action was taken."],
    )



def _is_valid_task_id(task_id: str | None) -> bool:
    return bool(task_id and TASK_ID_RE.fullmatch(task_id))


def _invalid_task_id_result(command: str, args: list[str], extra_warning: str | None = None) -> CommandResult:
    warnings = ["invalid_or_missing_task_id"]
    if extra_warning:
        warnings.append(extra_warning)
    return CommandResult(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=True,
        command_prefix="/hc",
        command=command,
        implemented=True,
        response_lines=[
            f"HC Trust Engineer {command} command received, but the task ID is missing or invalid.",
            "Expected task ID format: HC-TASK-YYYY-NNN",
            "No action taken.",
            "No repository mutation occurred.",
            *CLAIM_COMMAND_BOUNDARY_LINES,
        ],
        warnings=warnings,
        evidence_source="static claim command interface only",
    )


def _claim_result(args: list[str]) -> CommandResult:
    task_id = args[0] if args else None
    if not _is_valid_task_id(task_id):
        return _invalid_task_id_result("claim", args)
    return CommandResult(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=True,
        command_prefix="/hc",
        command="claim",
        implemented=True,
        response_lines=[
            f"task_id: {task_id}",
            "Report-only advisory claim request received.",
            "No repository mutation occurred.",
            "This command does not create, reserve, or acknowledge a claim.",
            "Local evaluator command example: python scripts/hc_task_claim.py <fixture.json> --pretty",
            "Human maintainer must review before acknowledging any claim.",
            *CLAIM_COMMAND_BOUNDARY_LINES,
        ],
        warnings=[],
        evidence_source="static claim command interface only",
    )


def _release_result(args: list[str]) -> CommandResult:
    task_id = args[0] if args else None
    if not _is_valid_task_id(task_id):
        return _invalid_task_id_result("release", args)
    return CommandResult(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=True,
        command_prefix="/hc",
        command="release",
        implemented=True,
        response_lines=[
            f"task_id: {task_id}",
            "Report-only manual release request received.",
            "No repository mutation occurred.",
            "This command does not release or modify any claim.",
            "Use local fixture evaluator for release readiness: python scripts/hc_task_claim.py <fixture.json> --pretty",
            "Human maintainer must decide.",
            *CLAIM_COMMAND_BOUNDARY_LINES,
        ],
        warnings=[],
        evidence_source="static claim command interface only",
    )


def _task_result(args: list[str]) -> CommandResult:
    if not args or args[0].lower() != "status":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=True,
            command_prefix="/hc",
            command="task",
            implemented=True,
            response_lines=[
                "HC Trust Engineer task command received, but only /hc task status HC-TASK-YYYY-NNN is supported.",
                "No action taken.",
                "No repository mutation occurred.",
                *CLAIM_COMMAND_BOUNDARY_LINES,
            ],
            warnings=["unsupported_task_subcommand"],
            evidence_source="static claim command interface only",
        )
    task_id = args[1] if len(args) > 1 else None
    if not _is_valid_task_id(task_id):
        return _invalid_task_id_result("task status", args)
    return CommandResult(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=True,
        command_prefix="/hc",
        command="task status",
        implemented=True,
        response_lines=[
            f"task_id: {task_id}",
            "Status-only advisory command received.",
            "No live GitHub lookup occurred.",
            "No claim, issue, PR, label, reviewer, branch, file, or workflow mutation occurred.",
            "Use local fixture evaluator for machine-readable status: python scripts/hc_task_claim.py <fixture.json> --pretty",
            *CLAIM_COMMAND_BOUNDARY_LINES,
        ],
        warnings=[],
        evidence_source="static claim command interface only",
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

    if command == "engineer":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=True,
            command_prefix="/hc",
            command="engineer",
            implemented=True,
            response_lines=list(ENGINEER_LINES),
            warnings=[
                "This local parser does not perform live GitHub state lookup.",
                "Use live PR, checks, comments, and review-thread evidence before acting.",
                "This operating sequence is not approval, rejection, merge authority, or a truth guarantee.",
            ],
            evidence_source="static HC Trust Engineer operating sequence",
        )

    if command == "bot":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=True,
            command_prefix="/hc",
            command="bot",
            implemented=True,
            response_lines=list(BOT_LINES),
            warnings=[
                "This local parser does not perform live GitHub state lookup.",
                "Use scripts/hc_bot_status.py for machine-readable bot-line status.",
                "This command does not expand automation authority.",
            ],
            evidence_source="static bot-line status summary from HC assistant command interface",
        )

    if command == "queue":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=True,
            command_prefix="/hc",
            command="queue",
            implemented=True,
            response_lines=list(QUEUE_LINES),
            warnings=[],
            evidence_source="static queue guidance from docs/project-control/hc-task-handoff-queue.md",
        )

    if command == "claim":
        return _claim_result(args)

    if command == "release":
        return _release_result(args)

    if command == "task":
        return _task_result(args)

    if command == "handoff":
        return CommandResult(
            advisory_only=True,
            public_safe=True,
            truth_guarantee=False,
            human_review_required=True,
            command_prefix="/hc",
            command="handoff",
            implemented=True,
            response_lines=list(HANDOFF_LINES),
            warnings=[
                "This local parser does not create or send a handoff package.",
                "Use scripts/hc_task_handoff.py with a local task fixture when a handoff package is needed.",
                "This command does not invoke an external tool, open a PR, or merge anything.",
            ],
            evidence_source="static handoff bridge summary from HC assistant command interface",
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
