#!/usr/bin/env python3
"""Local issue-comment bridge for HC Council commands.

This module converts explicit GitHub issue-comment event fixtures into
public-safe, report-only command payloads. It intentionally performs no network
calls, no provider calls, no repository writes, no labels, no assignments, no
approvals, no merges, and no issue or pull request closure.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts.hc_council_command import parse_command

SCHEMA_VERSION = "0.1"
ALLOWED_AUTHOR_ASSOCIATIONS = {"OWNER", "MEMBER", "COLLABORATOR"}
COMMAND_PREFIX = "/hc council"


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_str_list(value: Any) -> list[str]:
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    return sorted({str(item).strip() for item in items if str(item).strip()})


def _repository_name(event: dict[str, Any]) -> str:
    repository = event.get("repository", "")
    if isinstance(repository, dict):
        return str(repository.get("full_name", "")).strip()
    return str(repository).strip()


def _single_command_line(body: str) -> tuple[str | None, str | None]:
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    if not lines:
        return None, "empty_comment_body"
    if len(lines) != 1:
        return None, "ambiguous_multiline_comment"
    command = lines[0]
    if not command.startswith(COMMAND_PREFIX):
        return None, "not_hc_council_command"
    return command, None


def _stop(
    *,
    event: dict[str, Any],
    command: str | None,
    reason: str,
    evidence_refs: list[str] | None = None,
) -> dict[str, Any]:
    issue = _as_dict(event.get("issue", {}))
    comment = _as_dict(event.get("comment", {}))
    return {
        "schema_version": SCHEMA_VERSION,
        "mode": "report_only",
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "event_source": "github_issue_comment_fixture",
        "repository": _repository_name(event),
        "issue_number": issue.get("number"),
        "comment_author_association": str(comment.get("author_association", "")).strip(),
        "command": command,
        "accepted": False,
        "command_result": None,
        "evidence_refs": _as_str_list(evidence_refs),
        "stop_reasons": [reason],
        "warnings": [],
        "next_action": "stop",
        "evidence_source": "local GitHub issue-comment fixture only",
    }


def build_issue_command_bridge(event: dict[str, Any]) -> dict[str, Any]:
    """Build a deterministic report-only bridge result from one local fixture."""

    evidence_refs = _as_str_list(event.get("evidence_refs", []))
    if event.get("event_name") != "issue_comment":
        return _stop(event=event, command=None, reason="unsupported_event", evidence_refs=evidence_refs)

    comment = _as_dict(event.get("comment", {}))
    command, command_error = _single_command_line(str(comment.get("body", "")))
    if command_error:
        return _stop(
            event=event,
            command=command,
            reason=command_error,
            evidence_refs=evidence_refs,
        )

    author_association = str(comment.get("author_association", "")).strip()
    if author_association not in ALLOWED_AUTHOR_ASSOCIATIONS:
        return _stop(
            event=event,
            command=command,
            reason="unauthorized_comment_author",
            evidence_refs=evidence_refs,
        )

    command_result = parse_command(command or "", evidence_refs=evidence_refs).to_dict()
    issue = _as_dict(event.get("issue", {}))
    accepted = bool(command_result["accepted"])
    warnings = list(command_result["warnings"])
    if accepted:
        warnings.append("bridge_fixture_requires_live_policy_checks")

    return {
        "schema_version": SCHEMA_VERSION,
        "mode": "report_only",
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "event_source": "github_issue_comment_fixture",
        "repository": _repository_name(event),
        "issue_number": issue.get("number"),
        "comment_author_association": author_association,
        "command": command,
        "accepted": accepted,
        "command_result": command_result,
        "evidence_refs": command_result["evidence_refs"],
        "stop_reasons": [] if accepted else command_result["stop_reasons"],
        "warnings": warnings,
        "next_action": "run_local_council_report_fixture" if accepted else "stop",
        "evidence_source": "local GitHub issue-comment fixture only",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a local issue-comment fixture into report-only HC Council JSON."
    )
    parser.add_argument("fixture", help="Path to a local GitHub issue-comment fixture JSON file.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    event = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    result = build_issue_command_bridge(event)
    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
