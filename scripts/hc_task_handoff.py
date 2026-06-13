#!/usr/bin/env python3
"""Build a safe HC Engineer task handoff package.

This bridge converts an existing local HC Engineer task-plan fixture into a
machine-readable handoff package that can be pasted into a coding assistant or
used by a future reviewed integration.

It does not call a network, an LLM, GitHub, Codex, Copilot, a workflow API, or a
repository write API. It only reads a local JSON fixture and prints JSON.
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

from scripts.hc_engineer_task_plan import build_plan


@dataclass(frozen=True)
class HCTaskHandoff:
    advisory_only: bool
    public_safe: bool
    truth_guarantee: bool
    invokes_external_agent: bool
    creates_pull_request: bool
    requires_human_submit: bool
    task_title: str
    plan: dict[str, Any]
    handoff_prompt_lines: list[str]
    stop_conditions: list[str]
    merge_gate: dict[str, Any]
    evidence_source: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "advisory_only": self.advisory_only,
            "public_safe": self.public_safe,
            "truth_guarantee": self.truth_guarantee,
            "invokes_external_agent": self.invokes_external_agent,
            "creates_pull_request": self.creates_pull_request,
            "requires_human_submit": self.requires_human_submit,
            "task_title": self.task_title,
            "plan": self.plan,
            "handoff_prompt_lines": self.handoff_prompt_lines,
            "stop_conditions": self.stop_conditions,
            "merge_gate": self.merge_gate,
            "evidence_source": self.evidence_source,
        }


def _load_fixture(path: str | Path) -> dict[str, Any]:
    fixture_path = Path(path)
    with fixture_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("handoff fixture must be a JSON object")
    return payload


def _build_prompt_lines(plan: dict[str, Any]) -> list[str]:
    planned_prs = plan.get("planned_prs") if isinstance(plan.get("planned_prs"), list) else []
    first_pr = planned_prs[0] if planned_prs and isinstance(planned_prs[0], dict) else {}
    expected_files = first_pr.get("expected_files") if isinstance(first_pr.get("expected_files"), list) else []
    return [
        "HC Trust Engineer task handoff package.",
        f"Task: {plan.get('task_title')}",
        "Mode: implement only the scoped change requested by this package.",
        "Boundary: advisory-only project; do not claim truth, production readiness, approval, or merge authority.",
        "Preserve existing tests and governance boundaries.",
        "Do not modify protected paths unless this task explicitly lists them and human review is expected.",
        "Open one small PR only.",
        "Include a concise summary and validation notes in the PR body.",
        f"Expected files: {', '.join(str(path) for path in expected_files) if expected_files else 'not predeclared'}",
    ]


def build_handoff(fixture: dict[str, Any]) -> HCTaskHandoff:
    """Build a deterministic handoff package from a local task fixture."""

    plan = build_plan(fixture).to_dict()
    return HCTaskHandoff(
        advisory_only=True,
        public_safe=True,
        truth_guarantee=False,
        invokes_external_agent=False,
        creates_pull_request=False,
        requires_human_submit=True,
        task_title=str(plan.get("task_title", "Untitled HC Engineer task")),
        plan=plan,
        handoff_prompt_lines=_build_prompt_lines(plan),
        stop_conditions=list(plan.get("stop_conditions", [])),
        merge_gate=dict(plan.get("merge_gate", {})),
        evidence_source="local task fixture plus hc_engineer_task_plan output",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build a deterministic HC task handoff package.")
    parser.add_argument("fixture", help="Path to a local JSON task fixture.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    package = build_handoff(_load_fixture(args.fixture)).to_dict()
    indent = 2 if args.pretty else None
    print(json.dumps(package, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
