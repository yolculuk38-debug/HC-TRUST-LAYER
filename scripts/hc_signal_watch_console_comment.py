#!/usr/bin/env python3
"""Update the fixed HC Signal Watch console latest-status comment.

This script is intentionally narrow: it may create or update one issue comment on
configured issue #1082 only when a report contains an actionable P0/P1/P2 signal.
It never creates issues, pull requests, labels, reviewer requests, approvals,
merges, or branch/file mutations.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

MARKER = "<!-- hc-signal-watch-console:latest -->"
EXPECTED_ISSUE_TITLE = "HC Signal Watch Console"
DEFAULT_CONSOLE_ISSUE = "1082"
ACTIONABLE_PRIORITIES = {"P0", "P1", "P2"}
ALLOWED_REPORT_FIELDS = {
    "generated_at",
    "run_timestamp",
    "artifact_name",
    "artifact_url",
    "artifact_digest",
    "artifact_hash",
}
FORBIDDEN_OUTPUT_KEYS = {
    "token",
    "secret",
    "password",
    "private_key",
    "authorization",
    "cookie",
    "raw_log",
    "private_account_data",
    "personal_data",
    "internal_security_sensitive_details",
}
BOUNDARY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
    "repository_file_branch_mutation": False,
    "issue_comment_automation": True,
    "automatic_issue_creation": False,
    "automatic_pr_creation": False,
    "label_reviewer_mutation": False,
    "approval_authority": False,
    "merge_authority": False,
    "issue_text_command_parsing": False,
}


@dataclass(frozen=True)
class GitHubContext:
    token: str
    repository: str
    run_id: str
    server_url: str
    issue_number: str

    @property
    def api_base(self) -> str:
        return f"https://api.github.com/repos/{self.repository}"

    @property
    def run_url(self) -> str:
        return f"{self.server_url.rstrip('/')}/{self.repository}/actions/runs/{self.run_id}"


def _read_json(path: Path) -> dict[str, Any]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("Signal Watch report JSON must be an object")
    return raw


def _env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name, default)
    return str(value or "").strip()


def context_from_env() -> GitHubContext:
    return GitHubContext(
        token=_env("GITHUB_TOKEN"),
        repository=_env("GITHUB_REPOSITORY"),
        run_id=_env("GITHUB_RUN_ID"),
        server_url=_env("GITHUB_SERVER_URL", "https://github.com"),
        issue_number=_env("HC_SIGNAL_WATCH_CONSOLE_ISSUE", DEFAULT_CONSOLE_ISSUE),
    )


def _first_actionable(report: dict[str, Any]) -> dict[str, Any] | None:
    actions = report.get("recommended_human_actions")
    if not isinstance(actions, list):
        return None
    for action in actions:
        if not isinstance(action, dict):
            continue
        priority = str(action.get("priority") or "").strip().upper()
        if priority in ACTIONABLE_PRIORITIES:
            return action
    return None


def has_actionable_signal(report: dict[str, Any]) -> bool:
    return _first_actionable(report) is not None


def _priority_for_risk(risk: Any) -> str:
    normalized = str(risk or "").strip().lower()
    if normalized in {"critical", "urgent"}:
        return "P0"
    if normalized == "high":
        return "P1"
    if normalized == "medium":
        return "P2"
    if normalized == "low":
        return "P3"
    return "P4"


def _signal_title_for_action(report: dict[str, Any], action: dict[str, Any]) -> str:
    action_source = _public_value(action.get("source"))
    action_priority = _public_value(action.get("priority")).upper()
    action_recommendation = _public_value(action.get("recommended_action"))
    for collection_name in ("github_changelog_fixture_signals", "signals"):
        signals = report.get(collection_name)
        if not isinstance(signals, list):
            continue
        for signal in signals:
            if not isinstance(signal, dict):
                continue
            signal_source = _public_value(signal.get("source"))
            signal_priority = _priority_for_risk(signal.get("risk"))
            signal_recommendation = _public_value(signal.get("recommended_action"))
            if (
                signal_source == action_source
                and signal_priority == action_priority
                and signal_recommendation == action_recommendation
            ):
                return _public_value(signal.get("title") or signal.get("signal"))
    return _public_value(action.get("title") or action.get("signal") or action.get("reason"))


def _public_value(value: Any) -> str:
    text = str(value or "").strip()
    return text.replace("\r", " ").replace("\n", " ")


def _report_field(report: dict[str, Any], *names: str) -> str | None:
    for name in names:
        if name in ALLOWED_REPORT_FIELDS and report.get(name):
            return _public_value(report[name])
    return None


def build_comment_body(report: dict[str, Any], context: GitHubContext) -> str | None:
    action = _first_actionable(report)
    if action is None:
        return None

    priority = _public_value(action.get("priority")).upper()
    source = _public_value(action.get("source")) or "Signal Watch"
    title = _signal_title_for_action(report, action)
    recommended_action = _public_value(action.get("recommended_action"))
    generated_at = _report_field(report, "generated_at", "run_timestamp") or _env("HC_SIGNAL_WATCH_RUN_TIMESTAMP")
    artifact_name = _report_field(report, "artifact_name") or _env("HC_SIGNAL_WATCH_ARTIFACT_NAME", "hc-signal-watch-report")
    artifact_url = _report_field(report, "artifact_url") or _env("HC_SIGNAL_WATCH_ARTIFACT_URL")
    artifact_digest = _report_field(report, "artifact_digest", "artifact_hash") or _env("HC_SIGNAL_WATCH_ARTIFACT_DIGEST")

    lines = [
        MARKER,
        "## HC Signal Watch latest status",
        "",
        "Actionable public-safe Signal Watch notification for the fixed console issue.",
        "",
        f"- workflow_run: {context.run_url}",
        f"- artifact_name: {artifact_name or 'not provided'}",
    ]
    if artifact_url:
        lines.append(f"- artifact_link: {artifact_url}")
    if artifact_digest:
        lines.append(f"- artifact_digest: {artifact_digest}")
    if generated_at:
        lines.append(f"- generated_at: {generated_at}")
    lines.extend(
        [
            f"- signal_source: {source}",
            f"- signal_title: {title or 'not provided'}",
            f"- priority: {priority}",
            f"- recommended_action: {recommended_action or 'human review required'}",
            "- advisory_only=true",
            "- public_safe=true",
            "- truth_guarantee=false",
            "- human_review_required=true",
            "- repository_file_branch_mutation=false",
            "- issue_comment_automation=true",
            "- automatic_issue_creation=false",
            "- automatic_pr_creation=false",
            "- label_reviewer_mutation=false",
            "- approval_authority=false",
            "- merge_authority=false",
            "- issue_text_command_parsing=false",
            "",
            "Notification is not an obligation.",
            "Trust the record, not the assistant.",
            "Human final authority remains required.",
            "Evidence source is the Actions summary/artifact, not this issue comment.",
            "Issue text is not a command surface.",
        ]
    )
    body = "\n".join(lines) + "\n"
    lowered = body.lower()
    if any(key in lowered for key in FORBIDDEN_OUTPUT_KEYS):
        raise ValueError("comment payload includes forbidden field text")
    return body


class GitHubClient:
    def __init__(self, context: GitHubContext) -> None:
        self.context = context

    def request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            f"{self.context.api_base}{path}",
            data=data,
            method=method,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.context.token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "Content-Type": "application/json",
            },
        )
        with urllib.request.urlopen(request, timeout=20) as response:  # nosec: controlled GitHub API URL
            response_data = response.read().decode("utf-8")
        return json.loads(response_data) if response_data else None


def _issue_is_valid(issue: dict[str, Any]) -> bool:
    return (
        issue.get("number") == int(DEFAULT_CONSOLE_ISSUE)
        and issue.get("state") == "open"
        and issue.get("title") == EXPECTED_ISSUE_TITLE
        and issue.get("locked") is not True
    )


def update_console_comment(report: dict[str, Any], context: GitHubContext, client: GitHubClient, dry_run: bool = False) -> str:
    if context.issue_number != DEFAULT_CONSOLE_ISSUE:
        return "quiet: configured issue is not #1082"
    body = build_comment_body(report, context)
    if body is None:
        return "quiet: no actionable P0/P1/P2 signal"
    if dry_run:
        print(body, end="")
        return "dry-run: would create or update latest-status comment"
    if not context.token or not context.repository or not context.run_id:
        return "quiet: missing GitHub context"

    try:
        issue = client.request("GET", f"/issues/{context.issue_number}")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError):
        return "quiet: issue not accessible"
    if not isinstance(issue, dict) or not _issue_is_valid(issue):
        return "quiet: issue missing, closed, renamed, locked, or invalid"

    try:
        comments = client.request("GET", f"/issues/{context.issue_number}/comments?per_page=100")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError):
        return "quiet: comments not accessible"
    if not isinstance(comments, list):
        return "quiet: comments not accessible"

    marker_comment = next((comment for comment in comments if isinstance(comment, dict) and MARKER in str(comment.get("body") or "")), None)
    if marker_comment and marker_comment.get("id"):
        client.request("PATCH", f"/issues/comments/{marker_comment['id']}", {"body": body})
        return "updated: latest-status comment"

    client.request("POST", f"/issues/{context.issue_number}/comments", {"body": body})
    return "created: latest-status comment"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Update the HC Signal Watch fixed console issue comment.")
    parser.add_argument("report", nargs="?", type=Path, default=None, help="Signal Watch report JSON path")
    parser.add_argument("--report", dest="report_flag", type=Path, default=None, help="Signal Watch report JSON path")
    parser.add_argument("--dry-run", action="store_true", help="Print the comment payload without calling GitHub")
    args = parser.parse_args(argv)

    report_path = args.report_flag or args.report or Path(_env("HC_SIGNAL_WATCH_REPORT_JSON", "hc-signal-watch-report.json"))
    try:
        report = _read_json(report_path)
        context = context_from_env()
        result = update_console_comment(report, context, GitHubClient(context), args.dry_run)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"quiet: {exc}", file=sys.stderr)
        return 0
    print(result, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
