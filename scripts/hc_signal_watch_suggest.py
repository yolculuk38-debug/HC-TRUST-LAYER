#!/usr/bin/env python3
"""Local HC Signal Watch dry-run suggestion generator.

This script converts recommended_human_actions from a local HC Signal Watch
JSON report into copy-ready issue/PR suggestion text. It is dry-run only: it
reads one local JSON file and writes suggestions to stdout. It does not call
GitHub, access networks, mutate repository state, create issues or comments,
change labels or reviewers, approve pull requests, or merge pull requests.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
    "network_access": False,
    "repository_mutation": False,
    "issue_comment_automation": False,
    "label_reviewer_mutation": False,
    "approval_authority": False,
    "merge_authority": False,
}

NO_ACTION_VALUES = {"", "no-action", "no action", "none"}
SUGGESTION_AUTOMATION_BOUNDARY = (
    "dry-run text generation only; no GitHub API calls; no network access; "
    "no issue/comment creation; no label/reviewer mutation; no approval authority; no merge authority"
)


def _is_no_action(value: Any) -> bool:
    return str(value or "").strip().lower() in NO_ACTION_VALUES


def _suggested_type(priority: str, recommended_action: Any) -> str:
    if _is_no_action(recommended_action):
        return "no_action"
    if priority in {"P1", "P2"}:
        return "issue"
    if priority == "P3":
        return "issue"
    return "no_action"


def _load_report(path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Signal Watch report file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Signal Watch report file is not valid JSON: {path}") from exc

    if not isinstance(raw, dict):
        raise ValueError("Signal Watch report JSON must be an object")
    actions = raw.get("recommended_human_actions", [])
    if actions is None:
        raw["recommended_human_actions"] = []
    elif not isinstance(actions, list):
        raise ValueError("Signal Watch report recommended_human_actions must be a list")
    return raw


def _title_for(action: dict[str, Any], suggested_type: str) -> str:
    priority = str(action.get("priority") or "P4")
    source = str(action.get("source") or "Signal Watch")
    recommended_action = str(action.get("recommended_action") or "no-action")
    if suggested_type == "no_action":
        return f"[{priority}] No action suggested for {source}"
    return f"[{priority}] Review Signal Watch action: {recommended_action}"


def _body_for(action: dict[str, Any], suggested_type: str) -> str:
    priority = str(action.get("priority") or "P4")
    source = str(action.get("source") or "unknown")
    reason = str(action.get("reason") or "No reason supplied by Signal Watch report.")
    recommended_action = str(action.get("recommended_action") or "no-action")
    boundary = str(action.get("automation_boundary") or SUGGESTION_AUTOMATION_BOUNDARY)

    lines = [
        "## HC Signal Watch dry-run suggestion",
        "",
        "This is copy-ready advisory text generated from a local HC Signal Watch report.",
        "Human review is required before creating any GitHub issue, PR, comment, label, reviewer request, approval, merge, or repository-state change.",
        "",
        f"- suggested_type: {suggested_type}",
        f"- priority: {priority}",
        f"- source: {source}",
        f"- reason: {reason}",
        f"- recommended_action: {recommended_action}",
        "- human_review_required: true",
        f"- automation_boundary: {boundary}",
        "",
        "## Safety markers",
        "",
    ]
    lines.extend(f"- {key}={_markdown_bool(value)}" for key, value in SAFETY_MARKERS.items())
    return "\n".join(lines)


def build_suggestions(report: dict[str, Any]) -> dict[str, Any]:
    suggestions: list[dict[str, Any]] = []
    for index, action in enumerate(report.get("recommended_human_actions", [])):
        if not isinstance(action, dict):
            raise ValueError(f"recommended_human_actions entry {index} must be an object")
        priority = str(action.get("priority") or "P4")
        recommended_action = str(action.get("recommended_action") or "no-action")
        suggested_type = _suggested_type(priority, recommended_action)
        suggestion = {
            "suggested_type": suggested_type,
            "priority": priority,
            "title": _title_for(action, suggested_type),
            "body": _body_for(action, suggested_type),
            "source": str(action.get("source") or "unknown"),
            "reason": str(action.get("reason") or "No reason supplied by Signal Watch report."),
            "recommended_action": recommended_action,
            "human_review_required": True,
            "automation_boundary": SUGGESTION_AUTOMATION_BOUNDARY,
            **SAFETY_MARKERS,
        }
        suggestions.append(suggestion)

    return {
        **SAFETY_MARKERS,
        "report_name": "HC Signal Watch Dry-Run Suggestions",
        "mode": "local_dry_run_text_generation_only",
        "suggestions": suggestions,
    }


def _markdown_bool(value: bool) -> str:
    return "true" if value else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# HC Signal Watch Dry-Run Suggestions",
        "",
        "## Safety markers",
        "",
    ]
    lines.extend(f"- {key}={_markdown_bool(payload[key])}" for key in SAFETY_MARKERS)
    lines.extend(["", "## Suggestions", ""])

    suggestions = payload.get("suggestions", [])
    if suggestions:
        for suggestion in suggestions:
            lines.extend(
                [
                    f"### {suggestion['title']}",
                    "",
                    f"- suggested_type: {suggestion['suggested_type']}",
                    f"- priority: {suggestion['priority']}",
                    f"- source: {suggestion['source']}",
                    f"- reason: {suggestion['reason']}",
                    f"- recommended_action: {suggestion['recommended_action']}",
                    f"- human_review_required: {_markdown_bool(suggestion['human_review_required'])}",
                    f"- automation_boundary: {suggestion['automation_boundary']}",
                    "",
                    "#### Copy-ready body",
                    "",
                    suggestion["body"],
                    "",
                ]
            )
    else:
        lines.append("No dry-run suggestions were generated from recommended_human_actions.")
        lines.append("")

    lines.extend(
        [
            "## Non-goals",
            "",
            "This dry-run generator does not:",
            "",
            "- create GitHub issues, pull requests, comments, labels, or reviewer requests;",
            "- approve, reject, close, or merge pull requests;",
            "- call GitHub APIs or access the network;",
            "- mutate repository files, branches, workflow runs, or repository state;",
            "- guarantee truth, correctness, production readiness, legal truth, identity finality, or forensic certainty.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate local dry-run HC Signal Watch issue/PR suggestion text.")
    parser.add_argument("report", type=Path, help="Local JSON report from scripts/hc_signal_watch_report.py --format json")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    args = parser.parse_args()

    try:
        payload = build_suggestions(_load_report(args.report))
    except ValueError as exc:
        parser.error(str(exc))

    if args.format == "json":
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(render_markdown(payload), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
