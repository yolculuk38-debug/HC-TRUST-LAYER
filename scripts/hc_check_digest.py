#!/usr/bin/env python3
"""Build a deterministic local HC Check Digest from JSON fixtures.

The digest is report-only. It reads local JSON files, does not call GitHub or
network services, does not mutate repository state, and does not grant approval
or merge authority.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
    "network_access": False,
    "repository_mutation": False,
    "approval_authority": False,
    "merge_authority": False,
}

REQUIRED_FAILURE_KEYWORDS = (
    "validation",
    "canonical artifact boundary",
    "docs drift",
    "terminology",
    "policy evaluation",
    "scope guard",
)
ADVISORY_KEYWORDS = (
    "hc control bot report",
    "signal watch report",
    "repository inventory",
    "release audit",
    "pr risk labeler",
)
AUTOMATION_KEYWORDS = (
    "safe auto merge",
    "enable pr auto-merge",
    "terminology autofix suggest",
)

FAIL_STATUSES = {"failure", "failed", "error", "cancelled", "timed_out", "action_required"}
WARNING_LEVELS = {"warning", "notice", "advisory"}
PRIORITY_TOKEN_RE = re.compile(r"(?<![a-z0-9])p([123])(?![a-z0-9])")

PUBLIC_SURFACE_REQUIRED_ACTIONS = {
    "public-safe demo link": "demo/mini-public-validator-demo.md",
    "browser-side preview link": "self-service-verify.html",
    "Start here link": "START_HERE.md",
    "README link": "readme",
    "official repository link": "git" + "hub.com/yolculuk38-debug/HC-TRUST-LAYER",
    "project status link": "project-control/project-state.md",
    "Issues / contribute link": "issues",
}
PUBLIC_SURFACE_REQUIRED_TARGETS = (
    "docs/demo/mini-public-validator-demo.md",
    "docs/self-service-verify.html",
    "docs/START_HERE.md",
    "README.md",
    "docs/project-control/project-state.md",
)
PUBLIC_SURFACE_ENTRY_DOCS = (
    "docs/index.md",
    "README.md",
    "docs/START_HERE.md",
    "docs/demo/mini-public-validator-demo.md",
)
RISKY_PUBLIC_SURFACE_CLAIMS = (
    "production-ready",
    "production readiness",
    "guaranteed truth",
    "legal finality",
    "institutional finality",
    "identity finality",
    "certification authority",
    "autonomous authority",
    "autonomous system authority",
    "forensic certainty",
    "guaranteed correctness",
)
NEGATIVE_CONTEXT_MARKERS = (
    "no ",
    "not ",
    "does not ",
    "do not ",
    "without ",
    "is not ",
    "are not ",
    "doesn't ",
    "isn't ",
    "limitations",
    "risks",
)


def _resolve_repo_root(repo_root: str | Path | None = None) -> Path:
    return Path(repo_root or Path.cwd()).resolve()


def _read_repo_text(repo_root: Path, relative_path: str) -> str:
    path = repo_root / relative_path
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _public_surface_item(status: str, detail: str) -> dict[str, str]:
    return {"status": status, "detail": detail}


def _sentence_has_negative_context(sentence: str) -> bool:
    lowered = sentence.lower()
    return any(marker in lowered for marker in NEGATIVE_CONTEXT_MARKERS)


def _risky_public_claims(text: str) -> list[str]:
    risky: list[str] = []
    sentences = re.split(r"(?<=[.!?])\s+|\n+", text)
    for phrase in RISKY_PUBLIC_SURFACE_CLAIMS:
        for sentence in sentences:
            if phrase in sentence.lower() and not _sentence_has_negative_context(sentence):
                risky.append(phrase)
                break
    return risky


def evaluate_public_surface(repo_root: str | Path | None = None) -> dict[str, Any]:
    """Return report-only public surface status for HC Check Digest."""
    root = _resolve_repo_root(repo_root)
    index_text = _read_repo_text(root, "docs/index.md")
    index_lower = index_text.lower()

    landing_warnings: list[str] = []
    if "archived" in index_lower:
        landing_warnings.append("ARCHIVED appears in docs/index.md")
    if not any(term in index_lower for term in ("active", "partial", "advisory")):
        landing_warnings.append("active / partial / advisory status language is missing")
    if "active public navigation" not in index_lower or "hc-trust-layer" not in index_lower:
        landing_warnings.append("HC-TRUST-LAYER active public navigation identity is unclear")
    if any(name in index_lower for name in ("insanlik-zinciri", "humanity chain", "İnsanlık Zinciri".lower())):
        landing_warnings.append("legacy project name appears in active landing identity")

    missing_actions = [
        label
        for label, needle in PUBLIC_SURFACE_REQUIRED_ACTIONS.items()
        if needle.lower() not in index_lower
    ]
    missing_targets = [
        relative_path for relative_path in PUBLIC_SURFACE_REQUIRED_TARGETS if not (root / relative_path).is_file()
    ]

    boundary_warnings: list[str] = []
    combined_entry_text = "\n".join(_read_repo_text(root, path) for path in PUBLIC_SURFACE_ENTRY_DOCS)
    combined_lower = combined_entry_text.lower()
    if "advisory" not in combined_lower:
        boundary_warnings.append("advisory-only boundary language is missing")
    if "human" not in combined_lower or not any(
        term in combined_lower for term in ("final authority", "review remains", "review required", "human review")
    ):
        boundary_warnings.append("human review / human final authority language is missing")
    risky_claims = _risky_public_claims(combined_entry_text)
    if risky_claims:
        boundary_warnings.append(
            "risky public claim wording appears outside limitation context: " + ", ".join(sorted(set(risky_claims)))
        )

    checks = {
        "landing_status_clarity": _public_surface_item(
            "WARN" if landing_warnings else "PASS",
            "; ".join(landing_warnings) if landing_warnings else "active advisory public navigation is visible",
        ),
        "visitor_action_links": _public_surface_item(
            "WARN" if missing_actions else "PASS",
            "missing: " + ", ".join(missing_actions) if missing_actions else "required visitor action paths are present",
        ),
        "public_preview_targets": _public_surface_item(
            "WARN" if missing_targets else "PASS",
            "missing: " + ", ".join(missing_targets) if missing_targets else "required public preview targets exist",
        ),
        "boundary_language": _public_surface_item(
            "WARN" if boundary_warnings else "PASS",
            "; ".join(boundary_warnings)
            if boundary_warnings
            else "advisory-only, public-safe, and human final authority boundaries are visible",
        ),
    }
    status = "WARN" if any(item["status"] == "WARN" for item in checks.values()) else "PASS"
    return {
        "status": status,
        "checks": checks,
        "notes": [
            "report-only",
            "no runtime behavior changed",
            "human final authority remains required",
        ],
    }


def _load_json(path: str | None) -> Any:
    if not path:
        return []
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _items(payload: Any) -> list[dict[str, Any]]:
    if payload is None:
        return []
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key in ("checks", "reviews", "threads", "artifacts", "items", "data"):
            value = payload.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]
        return [payload]
    return []


def _text(item: dict[str, Any], *keys: str) -> str:
    values = [str(item.get(key, "")) for key in keys]
    return " ".join(values).strip()


def _name(item: dict[str, Any]) -> str:
    return _text(item, "name", "check", "title", "context", "workflow", "type") or "unnamed signal"


def _status(item: dict[str, Any]) -> str:
    return _text(item, "status", "conclusion", "state", "result").lower()


def _outcome_values(item: dict[str, Any]) -> set[str]:
    return {
        str(item.get(key, "")).strip().lower()
        for key in ("conclusion", "result", "status", "state")
        if str(item.get(key, "")).strip()
    }


def _is_outdated(item: dict[str, Any]) -> bool:
    return bool(item.get("outdated") or item.get("is_outdated"))


def _is_resolved(item: dict[str, Any]) -> bool:
    state = _text(item, "state", "status", "resolution").lower()
    return bool(item.get("resolved") or item.get("is_resolved") or state in {"resolved", "closed", "dismissed"})


def _codex_severity(item: dict[str, Any]) -> str:
    text = _text(item, "severity", "priority", "level", "body", "comment", "title", "name").lower()
    match = PRIORITY_TOKEN_RE.search(text)
    if match:
        return f"P{match.group(1)}"
    return ""


def _entry(item: dict[str, Any], reason: str) -> dict[str, str]:
    return {"name": _name(item), "status": _status(item) or "unknown", "reason": reason}


def _is_required_failure(item: dict[str, Any]) -> bool:
    haystack = _text(item, "name", "check", "title", "context", "workflow", "type", "category").lower()
    outcomes = _outcome_values(item)
    return bool(outcomes & FAIL_STATUSES) and any(keyword in haystack for keyword in REQUIRED_FAILURE_KEYWORDS)


def _is_advisory(item: dict[str, Any]) -> bool:
    haystack = _text(item, "name", "check", "title", "context", "workflow", "type", "category", "severity", "level").lower()
    outcomes = _outcome_values(item)
    return any(keyword in haystack for keyword in ADVISORY_KEYWORDS) or bool(outcomes & WARNING_LEVELS) or any(
        level in haystack for level in WARNING_LEVELS
    )


def _is_automation_helper(item: dict[str, Any]) -> bool:
    haystack = _text(item, "name", "check", "title", "context", "workflow", "type", "category").lower()
    return any(keyword in haystack for keyword in AUTOMATION_KEYWORDS)


REPO_HEALTH_GROUPS = ("changelog", "dependabot", "codeql", "weekly_summary")
REPO_HEALTH_LEVELS = {"blocker", "advisory", "neutral/baseline", "informational"}


def _repo_health_group(item: dict[str, Any], fallback: str | None = None) -> str:
    aliases = {
        "github_changelog": "changelog",
        "github_changelog_release_notes": "changelog",
        "release_notes": "changelog",
        "release_note": "changelog",
        "dependabot_update": "dependabot",
        "dependabot_updates": "dependabot",
        "codeql_baseline": "codeql",
        "weekly": "weekly_summary",
        "weekly_repo_health": "weekly_summary",
    }
    for key in ("group", "source", "type", "category"):
        value = str(item.get(key, "")).strip().lower().replace("-", "_").replace(" ", "_")
        group = aliases.get(value, value)
        if group in REPO_HEALTH_GROUPS:
            return group
    if fallback in REPO_HEALTH_GROUPS:
        return fallback
    return "weekly_summary"


def _truthy_marker(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return bool(value)


def _repo_health_level(item: dict[str, Any], group: str) -> str:
    markers = {
        str(item.get(key, "")).strip().lower().replace("_", "/")
        for key in ("level", "severity", "classification", "category", "type", "status", "state", "result")
        if str(item.get(key, "")).strip()
    }
    explicit_blocking = any(_truthy_marker(item.get(key)) for key in ("blocking", "blocker", "security_blocking"))
    explicit_security_dependabot = group == "dependabot" and (
        _truthy_marker(item.get("security")) or bool(markers & {"security", "security/blocking"})
    )
    if explicit_blocking or explicit_security_dependabot or bool(markers & {"blocker", "blocking", "security/blocking"}):
        if group != "weekly_summary":
            return "blocker"
    if markers & {"neutral", "baseline", "neutral/baseline"}:
        return "neutral/baseline"
    if markers & {"info", "informational", "notice"} or group == "weekly_summary":
        return "informational"
    return "advisory"


def _repo_health_entry(item: dict[str, Any], group: str) -> dict[str, str]:
    level = _repo_health_level(item, group)
    return {
        "name": _name(item),
        "status": _status(item) or level,
        "level": level,
        "reason": _text(item, "reason", "summary", "note", "body", "description") or f"{group} repo-health signal",
    }


def normalize_repo_health_signals(repo_health: Any = None) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {group: [] for group in REPO_HEALTH_GROUPS}
    if isinstance(repo_health, dict):
        found_grouped = False
        for group in REPO_HEALTH_GROUPS:
            value = repo_health.get(group)
            if value is not None:
                found_grouped = True
                for item in _items(value):
                    grouped[group].append(_repo_health_entry(item, group))
        if found_grouped:
            return grouped
    if isinstance(repo_health, list):
        raw_items = []
        for value in repo_health:
            if isinstance(value, dict):
                grouped_value = False
                for group in REPO_HEALTH_GROUPS:
                    if value.get(group) is not None:
                        grouped_value = True
                        for item in _items(value.get(group)):
                            grouped[group].append(_repo_health_entry(item, group))
                if grouped_value:
                    continue
            raw_items.extend(_items(value))
    else:
        raw_items = _items(repo_health)
    for item in raw_items:
        group = _repo_health_group(item)
        grouped[group].append(_repo_health_entry(item, group))
    return grouped


def _repo_health_counts(repo_health_signals: dict[str, list[dict[str, str]]]) -> dict[str, int]:
    counts = {"blocker": 0, "advisory": 0, "neutral_baseline": 0, "informational": 0}
    for entries in repo_health_signals.values():
        for entry in entries:
            level = entry["level"]
            if level == "neutral/baseline":
                counts["neutral_baseline"] += 1
            else:
                counts[level] += 1
    return counts


def build_digest(
    checks: Any = None,
    reviews: Any = None,
    threads: Any = None,
    artifacts: Any = None,
    repo_health: Any = None,
    repo_root: str | Path | None = None,
) -> dict[str, Any]:
    blocking: list[dict[str, str]] = []
    advisory: list[dict[str, str]] = []
    automation_helpers: list[dict[str, str]] = []
    external_review: list[dict[str, str]] = []
    artifact_entries: list[dict[str, str]] = []

    for check in _items(checks):
        if _is_automation_helper(check):
            automation_helpers.append(_entry(check, "automation helper signal"))
        if _is_required_failure(check):
            blocking.append(_entry(check, "failed required check candidate"))
        elif _is_advisory(check):
            advisory.append(_entry(check, "advisory check signal"))

    for review in _items(reviews):
        severity = _codex_severity(review)
        is_codex = "codex" in _text(review, "author", "source", "name", "title", "body").lower()
        if is_codex or _text(review, "author", "source", "reviewer"):
            external_review.append(_entry(review, "external review signal"))
        if is_codex and severity in {"P1", "P2"} and not _is_resolved(review) and not _is_outdated(review):
            blocking.append(_entry(review, f"open Codex {severity} feedback"))

    for thread in _items(threads):
        external_review.append(_entry(thread, "review thread signal"))
        if not _is_resolved(thread) and not _is_outdated(thread):
            blocking.append(_entry(thread, "unresolved non-outdated review thread"))

    for artifact in _items(artifacts):
        artifact_entries.append(_entry(artifact, "local artifact signal"))

    repo_health_signals = normalize_repo_health_signals(repo_health)
    repo_health_counts = _repo_health_counts(repo_health_signals)
    for group, entries in repo_health_signals.items():
        for entry in entries:
            if entry["level"] == "blocker":
                blocking.append({
                    "name": entry["name"],
                    "status": entry["status"],
                    "reason": f"repo-health {group} blocker",
                })

    if blocking:
        merge_guidance = "do_not_merge"
    elif advisory or repo_health_counts["advisory"]:
        merge_guidance = "human_review_before_merge"
    else:
        merge_guidance = "merge_allowed_after_human_review"

    summary = {
        "blocking_count": len(blocking),
        "advisory_count": len(advisory),
        "automation_helper_count": len(automation_helpers),
        "external_review_count": len(external_review),
        "artifact_count": len(artifact_entries),
        "repo_health_counts": repo_health_counts,
        "merge_guidance": merge_guidance,
    }
    return {
        **SAFETY_MARKERS,
        "blocking": blocking,
        "advisory": advisory,
        "automation_helpers": automation_helpers,
        "external_review": external_review,
        "artifacts": artifact_entries,
        "repo_health_signals": repo_health_signals,
        "public_surface": evaluate_public_surface(repo_root),
        "merge_guidance": merge_guidance,
        "summary": summary,
    }


def _render_section(lines: list[str], title: str, items: list[dict[str, str]]) -> None:
    lines.extend([f"## {title}", ""])
    if not items:
        lines.extend(["none", ""])
        return
    for item in items:
        lines.append(f"- {item['name']} ({item['status']}): {item['reason']}")
    lines.append("")


def render_markdown(digest: dict[str, Any]) -> str:
    lines = ["# HC Check Digest", "", "## Safety markers", ""]
    for key in SAFETY_MARKERS:
        lines.append(f"- {key}: {str(digest[key]).lower()}")
    lines.append("")
    _render_section(lines, "Blocking", digest["blocking"])
    _render_section(lines, "Advisory", digest["advisory"])
    _render_section(lines, "Automation helpers", digest["automation_helpers"])
    _render_section(lines, "External review", digest["external_review"])
    _render_section(lines, "Artifacts", digest["artifacts"])
    lines.extend(["## Repo health signals", ""])
    for group in REPO_HEALTH_GROUPS:
        lines.extend([f"### {group}", ""])
        entries = digest.get("repo_health_signals", {}).get(group, [])
        if not entries:
            lines.extend(["none", ""])
            continue
        for entry in entries:
            lines.append(f"- {entry['name']} ({entry['status']}, {entry['level']}): {entry['reason']}")
        lines.append("")
    public_surface = digest.get("public_surface", evaluate_public_surface())
    lines.extend(["## Public Surface", "", f"Status: {public_surface['status']}", ""])
    labels = {
        "landing_status_clarity": "Landing status clarity",
        "visitor_action_links": "Visitor action links",
        "public_preview_targets": "Public preview targets",
        "boundary_language": "Boundary language",
    }
    for key, label in labels.items():
        item = public_surface["checks"][key]
        detail = item.get("detail", "")
        suffix = f" — {detail}" if detail else ""
        lines.append(f"- {label}: {item['status']}{suffix}")
    lines.extend(["", "Notes:"])
    for note in public_surface.get("notes", []):
        lines.append(f"- {note}")
    lines.append("")
    lines.extend(["## Merge guidance", "", digest["merge_guidance"], ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a local report-only HC Check Digest.")
    parser.add_argument("--checks")
    parser.add_argument("--reviews")
    parser.add_argument("--threads")
    parser.add_argument("--artifacts")
    parser.add_argument("--repo-health", action="append", default=[])
    parser.add_argument("--format", choices=("json", "md"), default="json")
    args = parser.parse_args()

    digest = build_digest(
        checks=_load_json(args.checks),
        reviews=_load_json(args.reviews),
        threads=_load_json(args.threads),
        artifacts=_load_json(args.artifacts),
        repo_health=[_load_json(path) for path in args.repo_health],
    )
    if args.format == "json":
        print(json.dumps(digest, indent=2, sort_keys=True))
    else:
        print(render_markdown(digest), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
