#!/usr/bin/env python3
"""Machine-readable HC Trust Engineer bot line status reporter.

This script is local, deterministic, and report-only. It does not call a network,
LLM, GitHub API, workflow API, or repository write API. It records the current
bot line as a capability map with explicit parked components.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass


ACTIVE_COMPONENTS: tuple[str, ...] = (
    "hc_control_bot_path_scanner",
    "hc_control_bot_report_workflow",
    "hc_control_bot_advisory_comment_workflow",
    "hc_trust_engineer_reporter",
    "hc_engineer_task_planner",
    "hc_assistant_command_parser",
    "hc_assistant_issue_comment_listener",
)

PARKED_COMPONENTS: tuple[str, ...] = (
    "github_app",
    "dashboard_ui",
    "live_chat_ui",
    "llm_memory_layer",
    "semantic_llm_review",
    "automatic_approval",
    "automatic_merge",
    "automatic_close",
    "automatic_label_or_assignment",
)

BOUNDARIES: tuple[str, ...] = (
    "advisory_only=true",
    "public_safe=true",
    "truth_guarantee=false",
    "human_final_authority=true",
    "no_repository_writes=true",
    "no_network_calls=true",
    "no_llm_calls=true",
    "no_approval_or_merge_authority=true",
)

NEXT_SAFE_STEPS: tuple[str, ...] = (
    "keep_report_only_runner_green",
    "keep_hc_command_parser_tested",
    "connect_new_commands_only_after_small_test_backed_pr",
    "treat_branch_local_instructions_as_review_input",
    "require_human_review_for_authority_expansion",
)


@dataclass(frozen=True)
class BotStatus:
    advisory_only: bool
    public_safe: bool
    truth_guarantee: bool
    human_review_required: bool
    status: str
    active_components: list[str]
    parked_components: list[str]
    boundaries: list[str]
    next_safe_steps: list[str]
    evidence_source: str

    def to_dict(self) -> dict[str, object]:
        return {
            "advisory_only": self.advisory_only,
            "public_safe": self.public_safe,
            "truth_guarantee": self.truth_guarantee,
            "human_review_required": self.human_review_required,
            "status": self.status,
            "active_components": self.active_components,
            "parked_components": self.parked_components,
            "boundaries": self.boundaries,
            "next_safe_steps": self.next_safe_steps,
            "evidence_source": self.evidence_source,
        }


def build_bot_status() -> BotStatus:
    """Return the current static bot-line capability map."""

    return BotStatus(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        human_review_required=True,
        status="report_only_advisory_mvp",
        active_components=sorted(ACTIVE_COMPONENTS),
        parked_components=sorted(PARKED_COMPONENTS),
        boundaries=sorted(BOUNDARIES),
        next_safe_steps=sorted(NEXT_SAFE_STEPS),
        evidence_source="static repository bot-line status map",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Report HC Trust Engineer bot-line status.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    indent = 2 if args.pretty else None
    print(json.dumps(build_bot_status().to_dict(), indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
