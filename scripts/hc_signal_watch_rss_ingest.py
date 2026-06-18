#!/usr/bin/env python3
"""Fixture-based HC GitHub Changelog RSS signal normalizer.

This local script reads saved JSON or RSS/Atom XML fixtures and emits
normalized Signal Watch JSON. It does not call live networks, mutate GitHub
issues or comments, change labels or reviewers, approve pull requests, or merge
pull requests.
"""

from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}

BOUNDARIES = {
    "network_access": False,
    "repository_mutation": False,
    "issue_comment_automation": False,
    "label_reviewer_mutation": False,
    "approval_authority": False,
    "merge_authority": False,
}

KEYWORD_GROUPS: tuple[tuple[str, str, str, str, tuple[str, ...]], ...] = (
    (
        "workflow",
        "medium",
        "inspect workflow action versions and warnings",
        "GitHub Actions, runner, or workflow signal",
        (
            "actions",
            "workflow",
            "runner",
            "node",
            "deprecation",
            "ubuntu",
            "macos",
            "windows",
        ),
    ),
    (
        "dependency",
        "medium",
        "inspect dependency update policy",
        "dependency, Dependabot, or package ecosystem signal",
        ("dependabot", "dependency", "package", "pip", "npm", "advisory database"),
    ),
    (
        "security",
        "high",
        "inspect advisory security signal interpretation",
        "code scanning, secret scanning, or supply-chain signal",
        (
            "codeql",
            "code scanning",
            "secret scanning",
            "supply chain",
            "vulnerability",
            "security advisory",
        ),
    ),
    (
        "governance",
        "high",
        "inspect human-supervised governance and permission boundaries",
        "repository rules, permissions, approval, or policy signal",
        (
            "ruleset",
            "branch protection",
            "approval",
            "review",
            "permission",
            "token",
            "fork",
            "repository rules",
        ),
    ),
    (
        "automation",
        "medium",
        "inspect agent and automation boundaries",
        "Copilot, agent, bot, or automation signal",
        ("copilot", "agent", "bot", "automation", "ai"),
    ),
    (
        "public-verification",
        "low",
        "inspect public verification or release evidence expectations",
        "Pages, artifact, release, provenance, or public UX signal",
        ("pages", "artifact", "release", "provenance", "accessibility", "mobile"),
    ),
)

DEFAULT_AUTOMATION_BOUNDARY = (
    "advisory-only; no issue/comment automation, labels, reviewers, approval, or merge"
)


@dataclass(frozen=True)
class FeedEntry:
    source: str
    title: str
    url: str | None = None
    published: str | None = None
    category: str | None = None
    summary: str | None = None
    guid: str | None = None


def _clean(value: Any) -> str | None:
    if value is None:
        return None
    cleaned = re.sub(r"\s+", " ", str(value)).strip()
    return cleaned or None


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def _child_text(element: ET.Element, names: set[str]) -> str | None:
    for child in element:
        if _local_name(child.tag) in names:
            return _clean(child.text)
    return None


def _child_attr(element: ET.Element, child_name: str, attr: str) -> str | None:
    for child in element:
        if _local_name(child.tag) == child_name:
            return _clean(child.attrib.get(attr))
    return None


def _load_json_entries(path: Path) -> list[FeedEntry]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, dict):
        raw_entries = raw.get("entries") or raw.get("items") or []
        source = _clean(raw.get("source")) or "GitHub Changelog fixture"
    elif isinstance(raw, list):
        raw_entries = raw
        source = "GitHub Changelog fixture"
    else:
        raise ValueError("JSON fixture must be an object or list")

    if not isinstance(raw_entries, list):
        raise ValueError("JSON fixture entries must be a list")

    entries: list[FeedEntry] = []
    for index, item in enumerate(raw_entries):
        if not isinstance(item, dict):
            raise ValueError(f"JSON entry {index} must be an object")
        title = _clean(item.get("title"))
        if not title:
            raise ValueError(f"JSON entry {index} missing title")
        entries.append(
            FeedEntry(
                source=_clean(item.get("source")) or source,
                title=title,
                url=_clean(item.get("url") or item.get("link")),
                published=_clean(
                    item.get("published") or item.get("pubDate") or item.get("updated")
                ),
                category=_clean(item.get("category") or item.get("tag")),
                summary=_clean(
                    item.get("summary") or item.get("description") or item.get("note")
                ),
                guid=_clean(item.get("guid") or item.get("id")),
            )
        )
    return entries


def _load_xml_entries(path: Path) -> list[FeedEntry]:
    root = ET.fromstring(path.read_text(encoding="utf-8"))
    entries: list[FeedEntry] = []
    for element in root.iter():
        name = _local_name(element.tag)
        if name not in {"item", "entry"}:
            continue
        title = _child_text(element, {"title"})
        if not title:
            continue
        url = _child_text(element, {"link"}) or _child_attr(element, "link", "href")
        entries.append(
            FeedEntry(
                source="GitHub Changelog fixture",
                title=title,
                url=url,
                published=_child_text(element, {"pubdate", "published", "updated"}),
                category=_child_text(element, {"category"}),
                summary=_child_text(element, {"description", "summary", "content"}),
                guid=_child_text(element, {"guid", "id"}),
            )
        )
    return entries


def load_fixture(path: Path) -> list[FeedEntry]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        return _load_json_entries(path)
    if suffix in {".xml", ".rss", ".atom"}:
        return _load_xml_entries(path)
    raise ValueError("fixture must be .json, .xml, .rss, or .atom")


def _entry_key(entry: FeedEntry) -> str:
    if entry.url:
        return f"url:{entry.url.lower()}"
    if entry.guid:
        return f"guid:{entry.guid.lower()}"
    return "title-date:" + "|".join(
        part.lower() for part in (entry.title, entry.published or "")
    )


def _classify(entry: FeedEntry) -> dict[str, Any]:
    haystack = " ".join(
        part for part in (entry.title, entry.category, entry.summary) if part
    ).lower()
    matched: list[tuple[str, str, str, str, str]] = []
    for impact, risk, action, reason, keywords in KEYWORD_GROUPS:
        hits = [keyword for keyword in keywords if keyword in haystack]
        if hits:
            matched.append((impact, risk, action, reason, ", ".join(hits)))

    if matched:
        impact, risk, action, reason, keywords = matched[0]
        return {
            "impact": impact,
            "risk": risk,
            "recommended_action": action,
            "classification_reason": reason,
            "matched_keywords": keywords.split(", "),
            "evidence_gap": None,
        }

    return {
        "impact": "none",
        "risk": "low",
        "recommended_action": "record as no action unless repository operations are affected",
        "classification_reason": "no HC-relevant keyword matched this fixture entry",
        "matched_keywords": [],
        "evidence_gap": "fixture entry did not include an HC-relevant category or keyword",
    }


def normalize_entries(entries: list[FeedEntry]) -> dict[str, Any]:
    seen: set[str] = set()
    signals: list[dict[str, Any]] = []
    duplicates: list[dict[str, Any]] = []

    for entry in entries:
        key = _entry_key(entry)
        if key in seen:
            duplicates.append({"title": entry.title, "dedupe_key": key, "url": entry.url})
            continue
        seen.add(key)
        classification = _classify(entry)
        signals.append(
            {
                "source": entry.source,
                "title": entry.title,
                "url": entry.url,
                "published": entry.published,
                "category": entry.category,
                "note": entry.summary,
                "dedupe_key": key,
                "automation_boundary": DEFAULT_AUTOMATION_BOUNDARY,
                **classification,
            }
        )

    return {
        **SAFETY_MARKERS,
        **BOUNDARIES,
        "report_name": "HC Signal Watch RSS Fixture Ingestion",
        "mode": "local_fixture_only",
        "input_format": "json_or_xml_fixture",
        "signals": signals,
        "duplicates_suppressed": duplicates,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Normalize local GitHub Changelog RSS/JSON fixtures into advisory Signal Watch JSON."
    )
    parser.add_argument("fixture", type=Path, help="Local .json, .xml, .rss, or .atom fixture path")
    parser.add_argument("--indent", type=int, default=2, help="JSON indentation level")
    args = parser.parse_args(argv)

    payload = normalize_entries(load_fixture(args.fixture))
    print(json.dumps(payload, indent=args.indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
