#!/usr/bin/env python3
"""Local HC GitHub Signal Watch report generator.

This script is deterministic and report-only. It reads local repository files and
an optional operator-provided signal JSON file. It does not call GitHub, fetch
external network resources, mutate repository state, approve pull requests, merge
pull requests, change labels, or change reviewer assignments.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}

WATCH_POLICY_PATH = Path("docs/project-control/github-signal-watch-policy.md")
DEPENDABOT_PATH = Path(".github/dependabot.yml")

SIGNAL_KEYWORDS: tuple[tuple[str, str, str, str], ...] = (
    ("dependabot", "dependency", "medium", "inspect dependency update policy"),
    ("dependency", "dependency", "medium", "inspect dependency update policy"),
    ("pip", "dependency", "medium", "inspect Python dependency update policy"),
    ("actions", "workflow", "medium", "inspect workflow action versions and warnings"),
    ("workflow", "workflow", "medium", "inspect workflow action versions and warnings"),
    ("runner", "workflow", "medium", "inspect runner and action runtime assumptions"),
    ("node", "workflow", "medium", "inspect action runtime deprecation warnings"),
    ("codeql", "security", "medium", "inspect code scanning baseline and annotations"),
    ("code scanning", "security", "medium", "inspect code scanning baseline and annotations"),
    ("secret scanning", "security", "high", "inspect secret scanning configuration and alerts"),
    ("supply chain", "security", "high", "inspect supply-chain security posture"),
    ("copilot", "automation", "medium", "inspect agent and automation boundaries"),
    ("agent", "automation", "medium", "inspect agent and automation boundaries"),
    ("fork", "community", "low", "inspect onboarding and contribution boundaries"),
    ("star", "community", "low", "inspect onboarding and public safety language"),
    ("watcher", "community", "low", "inspect onboarding and public safety language"),
    ("follower", "community", "low", "inspect onboarding and public safety language"),
)

CHANGELOG_SIGNAL_FIELDS = (
    "source",
    "title",
    "url",
    "published",
    "category",
    "impact",
    "risk",
    "recommended_action",
    "classification_reason",
    "matched_keywords",
    "evidence_gap",
    "automation_boundary",
    "dedupe_key",
)

PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}

ACTION_AUTOMATION_BOUNDARY = (
    "advisory-only; report-only; no live network; no GitHub API calls; "
    "no issue/comment creation; no label/reviewer mutation; no approval authority; no merge authority"
)


def _priority_for_signal(risk: Any, evidence_gap: Any = None, recommended_action: Any = None) -> str:
    normalized = str(risk or "").strip().lower()
    if normalized == "high":
        return "P1"
    if normalized == "medium":
        return "P2"
    if normalized == "low":
        return "P3"
    return "P4"


def _build_recommended_human_actions(
    findings: list[SignalFinding],
    changelog_signals: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    queued: list[tuple[int, dict[str, Any]]] = []

    for index, finding in enumerate(findings):
        queued.append(
            (
                index,
                {
                    "priority": _priority_for_signal(finding.risk, finding.evidence_gap, finding.recommended_action),
                    "source": finding.source,
                    "reason": finding.evidence_gap
                    or f"operator signal classified as {finding.risk} risk with {finding.impact} impact",
                    "recommended_action": finding.recommended_action,
                    "human_review_required": True,
                    "automation_boundary": ACTION_AUTOMATION_BOUNDARY,
                },
            )
        )

    offset = len(queued)
    for index, signal in enumerate(changelog_signals):
        risk = signal.get("risk")
        evidence_gap = signal.get("evidence_gap")
        recommended_action = signal.get("recommended_action")
        queued.append(
            (
                offset + index,
                {
                    "priority": _priority_for_signal(risk, evidence_gap, recommended_action),
                    "source": str(signal.get("source") or "GitHub Changelog fixture"),
                    "reason": str(
                        evidence_gap
                        or signal.get("classification_reason")
                        or f"GitHub Changelog fixture signal classified as {risk or 'unknown'} risk"
                    ),
                    "recommended_action": str(recommended_action or "record evidence gap for human review"),
                    "human_review_required": True,
                    "automation_boundary": ACTION_AUTOMATION_BOUNDARY,
                },
            )
        )

    queued.sort(key=lambda item: (PRIORITY_ORDER[item[1]["priority"]], item[0]))
    return [action for _, action in queued]


@dataclass(frozen=True)
class SignalInput:
    source: str
    title: str
    url: str | None = None
    note: str | None = None


@dataclass(frozen=True)
class SignalFinding:
    signal: str
    source: str
    impact: str
    risk: str
    recommended_action: str
    automation_boundary: str
    evidence_gap: str | None
    url: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "signal": self.signal,
            "source": self.source,
            "impact": self.impact,
            "risk": self.risk,
            "recommended_action": self.recommended_action,
            "automation_boundary": self.automation_boundary,
            "evidence_gap": self.evidence_gap,
            "url": self.url,
        }


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _has_text(path: Path, text: str) -> bool:
    return text in _read_text(path)


def _dependabot_status(repo_root: Path) -> dict[str, Any]:
    path = repo_root / DEPENDABOT_PATH
    content = _read_text(path)
    return {
        "path": DEPENDABOT_PATH.as_posix(),
        "present": path.exists(),
        "github_actions_weekly": "package-ecosystem: \"github-actions\"" in content and "interval: \"weekly\"" in content,
        "pip_weekly": "package-ecosystem: \"pip\"" in content and "interval: \"weekly\"" in content,
        "github_actions_grouped": "groups:" in content and "github-actions:" in content,
    }


def _policy_status(repo_root: Path) -> dict[str, Any]:
    path = repo_root / WATCH_POLICY_PATH
    return {
        "path": WATCH_POLICY_PATH.as_posix(),
        "present": path.exists(),
        "requires_repo_wide_pr_search": _has_text(path, "repo:yolculuk38-debug/HC-TRUST-LAYER is:pr is:open"),
        "requires_annotation_review": _has_text(path, "check annotations and warnings"),
        "requires_community_signal_review": _has_text(path, "repository visibility signals"),
    }


def _registry_status(repo_root: Path) -> dict[str, Any]:
    path = repo_root / "docs/project-control/active-work-registry.md"
    return {
        "path": path.relative_to(repo_root).as_posix(),
        "present": path.exists(),
        "links_policy": WATCH_POLICY_PATH.as_posix() in _read_text(path),
    }


def _load_signals(path: Path | None) -> list[SignalInput]:
    if path is None:
        return []

    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("signal JSON must be a list of objects")

    signals: list[SignalInput] = []
    for index, entry in enumerate(raw):
        if not isinstance(entry, dict):
            raise ValueError(f"signal entry {index} must be an object")
        source = str(entry.get("source", "unknown")).strip() or "unknown"
        title = str(entry.get("title", "")).strip()
        if not title:
            raise ValueError(f"signal entry {index} missing title")
        url = entry.get("url")
        note = entry.get("note")
        signals.append(
            SignalInput(
                source=source,
                title=title,
                url=str(url).strip() if url else None,
                note=str(note).strip() if note else None,
            )
        )
    return signals


def _load_changelog_signals(path: Path | None) -> list[dict[str, Any]]:
    if path is None:
        return []
    if not path.exists():
        raise ValueError(f"changelog signal file not found: {path}")

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"changelog signal file is not valid JSON: {path}") from exc

    if not isinstance(raw, dict):
        raise ValueError("changelog signal JSON must be the normalized fixture or live dry-run object")
    mode = raw.get("mode")
    if mode == "local_fixture_only":
        if raw.get("network_access") is not False:
            raise ValueError("changelog signal JSON must declare network_access=false")
    elif mode == "manual_live_rss_dry_run":
        if raw.get("safe_failure") is True or raw.get("fetch_status") != "ok":
            return []
    else:
        raise ValueError("changelog signal JSON must come from local fixture normalization or live RSS dry-run")

    raw_signals = raw.get("signals")
    if not isinstance(raw_signals, list):
        raise ValueError("changelog signal JSON must include a signals list")

    signals: list[dict[str, Any]] = []
    for index, entry in enumerate(raw_signals):
        if not isinstance(entry, dict):
            raise ValueError(f"changelog signal entry {index} must be an object")
        title = str(entry.get("title", "")).strip()
        if not title:
            raise ValueError(f"changelog signal entry {index} missing title")
        signal = {field: entry.get(field) for field in CHANGELOG_SIGNAL_FIELDS if field in entry}
        signal.setdefault("source", "GitHub Changelog fixture")
        signal["title"] = title
        signals.append(signal)
    return signals


def classify_signal(signal: SignalInput) -> SignalFinding:
    haystack = " ".join(part for part in (signal.source, signal.title, signal.note or "") if part).lower()
    for keyword, impact, risk, action in SIGNAL_KEYWORDS:
        if keyword in haystack:
            return SignalFinding(
                signal=signal.title,
                source=signal.source,
                impact=impact,
                risk=risk,
                recommended_action=action,
                automation_boundary="advisory-only; no automatic approval or merge",
                evidence_gap=None,
                url=signal.url,
            )

    return SignalFinding(
        signal=signal.title,
        source=signal.source,
        impact="none",
        risk="low",
        recommended_action="record as no action unless repository operations are affected",
        automation_boundary="advisory-only; no automatic approval or merge",
        evidence_gap="no HC-relevant keyword matched this signal",
        url=signal.url,
    )


def build_report(
    repo_root: Path,
    signal_file: Path | None = None,
    changelog_signals_file: Path | None = None,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    signal_inputs = _load_signals(signal_file)
    findings = [classify_signal(signal) for signal in signal_inputs]
    changelog_signals = _load_changelog_signals(changelog_signals_file)

    report: dict[str, Any] = {
        **SAFETY_MARKERS,
        "report_name": "HC GitHub Signal Watch",
        "mode": "local_report_only",
        "network_access": False,
        "repository_mutation": False,
        "issue_comment_automation": False,
        "label_reviewer_mutation": False,
        "approval_authority": False,
        "merge_authority": False,
        "policy": _policy_status(repo_root),
        "active_work_registry": _registry_status(repo_root),
        "dependabot": _dependabot_status(repo_root),
        "mandatory_live_checks": [
            "repo-wide open PR search: repo:yolculuk38-debug/HC-TRUST-LAYER is:pr is:open",
            "Dependabot PR review",
            "comments, review threads, reviews, check annotations, neutral checks, and advisory artifacts",
            "GitHub Changelog review for Actions, Application Security, Supply Chain Security, Platform Governance, Copilot, and Collaboration Tools",
            "community visibility signal review when stars, watchers, forks, followers, or first-time contributors appear",
        ],
        "signals": [finding.to_dict() for finding in findings],
        "github_changelog_fixture_signals": changelog_signals,
        "recommended_human_actions": _build_recommended_human_actions(findings, changelog_signals),
        "evidence_gaps": [],
    }

    if not signal_inputs:
        report["evidence_gaps"].append("No signal JSON was supplied; live GitHub Home and Changelog signals were not evaluated by this local report.")

    if not report["dependabot"]["present"]:
        report["evidence_gaps"].append("Dependabot configuration file is missing.")
    if not report["policy"]["present"]:
        report["evidence_gaps"].append("GitHub Signal Watch policy file is missing.")
    if not report["active_work_registry"]["links_policy"]:
        report["evidence_gaps"].append("Active Work Registry does not link the GitHub Signal Watch policy.")

    return report


def _markdown_bool(value: bool) -> str:
    return "true" if value else "false"


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# HC GitHub Signal Watch Report",
        "",
        "## Safety markers",
        "",
        f"- advisory_only={_markdown_bool(report['advisory_only'])}",
        f"- public_safe={_markdown_bool(report['public_safe'])}",
        f"- truth_guarantee={_markdown_bool(report['truth_guarantee'])}",
        f"- human_review_required={_markdown_bool(report['human_review_required'])}",
        f"- mode={report['mode']}",
        f"- network_access={_markdown_bool(report['network_access'])}",
        f"- repository_mutation={_markdown_bool(report['repository_mutation'])}",
        f"- issue_comment_automation={_markdown_bool(report['issue_comment_automation'])}",
        f"- label_reviewer_mutation={_markdown_bool(report['label_reviewer_mutation'])}",
        f"- approval_authority={_markdown_bool(report['approval_authority'])}",
        f"- merge_authority={_markdown_bool(report['merge_authority'])}",
        "",
        "## Local readiness checks",
        "",
        f"- policy_present={_markdown_bool(report['policy']['present'])}",
        f"- registry_links_policy={_markdown_bool(report['active_work_registry']['links_policy'])}",
        f"- dependabot_present={_markdown_bool(report['dependabot']['present'])}",
        f"- github_actions_weekly={_markdown_bool(report['dependabot']['github_actions_weekly'])}",
        f"- pip_weekly={_markdown_bool(report['dependabot']['pip_weekly'])}",
        f"- github_actions_grouped={_markdown_bool(report['dependabot']['github_actions_grouped'])}",
        "",
        "## Mandatory live checks",
        "",
    ]

    lines.extend(f"- {item}" for item in report["mandatory_live_checks"])
    lines.extend(["", "## Signals", ""])

    if report["signals"]:
        for finding in report["signals"]:
            lines.extend(
                [
                    f"### {finding['signal']}",
                    "",
                    f"- source: {finding['source']}",
                    f"- impact: {finding['impact']}",
                    f"- risk: {finding['risk']}",
                    f"- recommended_action: {finding['recommended_action']}",
                    f"- automation_boundary: {finding['automation_boundary']}",
                    f"- evidence_gap: {finding['evidence_gap'] or 'none'}",
                    f"- url: {finding['url'] or 'none'}",
                    "",
                ]
            )
    else:
        lines.append("No operator-provided signals were supplied to this local report.")
        lines.append("")

    lines.extend(["## GitHub Changelog fixture signals", ""])
    if report["github_changelog_fixture_signals"]:
        for signal in report["github_changelog_fixture_signals"]:
            lines.extend(
                [
                    f"### {signal['title']}",
                    "",
                    f"- source: {signal.get('source', 'GitHub Changelog fixture')}",
                    f"- url: {signal.get('url') or 'none'}",
                    f"- published: {signal.get('published') or 'none'}",
                    f"- category: {signal.get('category') or 'none'}",
                    f"- impact: {signal.get('impact') or 'none'}",
                    f"- risk: {signal.get('risk') or 'none'}",
                    f"- recommended_action: {signal.get('recommended_action') or 'none'}",
                    f"- classification_reason: {signal.get('classification_reason') or 'none'}",
                    f"- matched_keywords: {', '.join(signal.get('matched_keywords') or []) or 'none'}",
                    f"- evidence_gap: {signal.get('evidence_gap') or 'none'}",
                    f"- automation_boundary: {signal.get('automation_boundary') or 'none'}",
                    f"- dedupe_key: {signal.get('dedupe_key') or 'none'}",
                    "",
                ]
            )
    else:
        lines.append("No GitHub Changelog fixture signals were supplied to this local report.")
        lines.append("")

    lines.extend(["## Recommended human actions", ""])
    if report["recommended_human_actions"]:
        for action in report["recommended_human_actions"]:
            lines.extend(
                [
                    f"### {action['priority']} — {action['source']}",
                    "",
                    f"- reason: {action['reason']}",
                    f"- recommended_action: {action['recommended_action']}",
                    f"- human_review_required: {_markdown_bool(action['human_review_required'])}",
                    f"- automation_boundary: {action['automation_boundary']}",
                    "",
                ]
            )
    else:
        lines.append("No recommended human actions were generated by this local report.")
        lines.append("")

    lines.extend(["## Evidence gaps", ""])
    if report["evidence_gaps"]:
        lines.extend(f"- {gap}" for gap in report["evidence_gaps"])
    else:
        lines.append("- none")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a local HC GitHub Signal Watch report.")
    parser.add_argument("repo_root", nargs="?", default=".", help="Repository root path")
    parser.add_argument("--signals", type=Path, default=None, help="Optional JSON list of operator-provided signals")
    parser.add_argument(
        "--changelog-signals",
        type=Path,
        default=None,
        help="Optional normalized local fixture JSON from hc_signal_watch_rss_ingest.py",
    )
    parser.add_argument("--format", choices=("json", "md"), default="json")
    args = parser.parse_args()

    try:
        report = build_report(Path(args.repo_root), args.signals, args.changelog_signals)
    except ValueError as exc:
        parser.error(str(exc))
    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_markdown(report), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
