#!/usr/bin/env python3
"""Manual-only HC Signal Watch live GitHub Changelog RSS dry-run fetcher.

This script fetches one public RSS/Atom URL, normalizes entries into Signal
Watch JSON, and writes optional JSON and Markdown artifact files. It is
advisory-only and does not mutate repository, issue, pull request, label,
reviewer, approval, or merge state.
"""

from __future__ import annotations

import argparse
import json
import socket
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from hc_signal_watch_rss_ingest import FeedEntry, normalize_entries

DEFAULT_RSS_URL = "https://github.blog/changelog/feed/"
SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
    "repository_mutation": False,
    "issue_comment_automation": False,
    "label_reviewer_mutation": False,
    "approval_authority": False,
    "merge_authority": False,
}


@dataclass(frozen=True)
class FetchResult:
    ok: bool
    xml_text: str | None = None
    error: str | None = None


def _clean(value: Any) -> str | None:
    if value is None:
        return None
    text = " ".join(str(value).split()).strip()
    return text or None


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


def parse_rss(xml_text: str, source_url: str) -> list[FeedEntry]:
    root = ET.fromstring(xml_text)
    entries: list[FeedEntry] = []
    for element in root.iter():
        if _local_name(element.tag) not in {"item", "entry"}:
            continue
        title = _child_text(element, {"title"})
        if not title:
            continue
        entries.append(
            FeedEntry(
                source="GitHub Changelog RSS live dry run",
                title=title,
                url=_child_text(element, {"link"}) or _child_attr(element, "link", "href"),
                published=_child_text(element, {"pubdate", "published", "updated"}),
                category=_child_text(element, {"category"}),
                summary=_child_text(element, {"description", "summary", "content"}),
                guid=_child_text(element, {"guid", "id"}),
            )
        )
    return entries


def fetch_rss(url: str, timeout_seconds: float) -> FetchResult:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "HC-TRUST-LAYER Signal Watch live RSS dry run"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            content_type = response.headers.get_content_charset() or "utf-8"
            return FetchResult(ok=True, xml_text=response.read().decode(content_type, errors="replace"))
    except (TimeoutError, socket.timeout) as exc:
        return FetchResult(ok=False, error=f"timeout while fetching RSS: {exc}")
    except urllib.error.URLError as exc:
        return FetchResult(ok=False, error=f"RSS fetch failed: {exc}")
    except OSError as exc:
        return FetchResult(ok=False, error=f"RSS fetch failed: {exc}")


def build_payload(url: str, timeout_seconds: float) -> dict[str, Any]:
    result = fetch_rss(url, timeout_seconds)
    payload: dict[str, Any] = {
        **SAFETY_MARKERS,
        "report_name": "HC Signal Watch Live GitHub Changelog RSS Dry Run",
        "mode": "manual_live_rss_dry_run",
        "source_url": url,
        "network_access": True,
        "fixed_default_url": DEFAULT_RSS_URL,
        "timeout_seconds": timeout_seconds,
        "safe_failure": not result.ok,
        "fetch_status": "ok" if result.ok else "error",
        "fetch_error": result.error,
        "signals": [],
        "duplicates_suppressed": [],
    }
    if not result.ok:
        payload["evidence_gaps"] = ["Live RSS fetch did not complete; human review remains required."]
        return payload

    try:
        normalized = normalize_entries(parse_rss(result.xml_text or "", url))
    except ET.ParseError as exc:
        payload["safe_failure"] = True
        payload["fetch_status"] = "error"
        payload["fetch_error"] = f"RSS parse failed: {exc}"
        payload["evidence_gaps"] = ["Live RSS parse did not complete; human review remains required."]
        return payload

    payload["signals"] = normalized["signals"]
    payload["duplicates_suppressed"] = normalized["duplicates_suppressed"]
    payload["evidence_gaps"] = [] if payload["signals"] else ["Live RSS feed contained no parsable entries."]
    return payload


def render_markdown(payload: dict[str, Any]) -> str:
    def b(name: str) -> str:
        return "true" if payload[name] else "false"

    lines = [
        "# HC Signal Watch Live GitHub Changelog RSS Dry Run",
        "",
        "## Safety markers",
        "",
        f"- advisory_only={b('advisory_only')}",
        f"- public_safe={b('public_safe')}",
        f"- truth_guarantee={b('truth_guarantee')}",
        f"- human_review_required={b('human_review_required')}",
        f"- repository_mutation={b('repository_mutation')}",
        f"- issue_comment_automation={b('issue_comment_automation')}",
        f"- label_reviewer_mutation={b('label_reviewer_mutation')}",
        f"- approval_authority={b('approval_authority')}",
        f"- merge_authority={b('merge_authority')}",
        "",
        "## Fetch status",
        "",
        f"- mode={payload['mode']}",
        f"- source_url={payload['source_url']}",
        f"- timeout_seconds={payload['timeout_seconds']}",
        f"- fetch_status={payload['fetch_status']}",
        f"- safe_failure={b('safe_failure')}",
    ]
    if payload.get("fetch_error"):
        lines.append(f"- fetch_error={payload['fetch_error']}")
    lines.extend(["", "## Signals", ""])
    if not payload["signals"]:
        lines.append("- No parsed live RSS signals. Human review remains required.")
    for signal in payload["signals"]:
        lines.extend([
            f"### {signal['title']}",
            "",
            f"- source: {signal['source']}",
            f"- url: {signal.get('url') or 'not supplied'}",
            f"- published: {signal.get('published') or 'not supplied'}",
            f"- impact: {signal['impact']}",
            f"- risk: {signal['risk']}",
            f"- recommended_action: {signal['recommended_action']}",
            f"- automation_boundary: {signal['automation_boundary']}",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch GitHub Changelog RSS as a manual Signal Watch dry-run report.")
    parser.add_argument("--url", default=DEFAULT_RSS_URL, help="GitHub Changelog RSS URL to fetch")
    parser.add_argument("--timeout", type=float, default=10.0, help="Fetch timeout in seconds")
    parser.add_argument("--json-output", type=Path, help="Optional JSON artifact path")
    parser.add_argument("--markdown-output", type=Path, help="Optional Markdown artifact path")
    args = parser.parse_args(argv)

    payload = build_payload(args.url, args.timeout)
    json_text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    md_text = render_markdown(payload)
    if args.json_output:
        args.json_output.write_text(json_text, encoding="utf-8")
    else:
        sys.stdout.write(json_text)
    if args.markdown_output:
        args.markdown_output.write_text(md_text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
