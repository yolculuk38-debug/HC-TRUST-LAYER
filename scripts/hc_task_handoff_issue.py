#!/usr/bin/env python3
"""Parse an HC Task Handoff issue body into a local handoff package.

This helper is local, deterministic, and report-only. It does not call a network,
LLM, GitHub API, workflow API, or repository write API. It reads a local issue
body text file and prints JSON.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.hc_task_handoff import build_handoff

FIELD_ALIASES: dict[str, str] = {
    "task title": "task_title",
    "goal": "goal",
    "allowed path scope": "changed_files",
    "blocked scope": "blocked_scope",
    "evidence required": "evidence_required",
    "validation expected": "validation_expected",
    "handoff package": "handoff_package",
}


def _normalize_heading(value: str) -> str:
    return value.strip().strip("#").strip().lower()


def _clean_lines(value: str) -> list[str]:
    lines: list[str] = []
    for raw_line in value.splitlines():
        line = raw_line.strip()
        if not line or line == "_No response_":
            continue
        if line.startswith("```"):
            continue
        lines.append(line)
    return lines


def _parse_issue_sections(issue_body: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None

    for raw_line in issue_body.splitlines():
        line = raw_line.rstrip()
        if line.startswith("### "):
            current = _normalize_heading(line)
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)

    return {heading: "\n".join(lines).strip() for heading, lines in sections.items()}


def issue_body_to_fixture(issue_body: str) -> dict[str, Any]:
    """Convert GitHub issue-form markdown into a task-plan fixture."""

    sections = _parse_issue_sections(issue_body)
    fixture: dict[str, Any] = {
        "open_prs": [],
        "unresolved_review_comments": [],
        "checks": [],
    }

    for heading, raw_value in sections.items():
        key = FIELD_ALIASES.get(heading)
        if key is None:
            continue
        if key in {"changed_files", "blocked_scope", "evidence_required", "validation_expected"}:
            fixture[key] = _clean_lines(raw_value)
        elif key == "handoff_package":
            value = raw_value.strip()
            if value and value != "_No response_":
                fixture[key] = value
        else:
            lines = _clean_lines(raw_value)
            fixture[key] = "\n".join(lines).strip() if lines else ""

    if not fixture.get("task_title"):
        fixture["task_title"] = "Untitled HC task handoff"

    return fixture


def build_issue_handoff(issue_body: str) -> dict[str, Any]:
    """Build an advisory handoff package from an issue-form body."""

    fixture = issue_body_to_fixture(issue_body)
    package = build_handoff(fixture).to_dict()
    return {
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "source": "local issue body text",
        "fixture": fixture,
        "handoff": package,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Parse an HC task handoff issue body.")
    parser.add_argument("issue_body", help="Path to a local issue body markdown/text file.")
    parser.add_argument("--fixture-only", action="store_true", help="Print only the generated fixture JSON.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    issue_body = Path(args.issue_body).read_text(encoding="utf-8")
    payload = issue_body_to_fixture(issue_body) if args.fixture_only else build_issue_handoff(issue_body)
    indent = 2 if args.pretty else None
    print(json.dumps(payload, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
