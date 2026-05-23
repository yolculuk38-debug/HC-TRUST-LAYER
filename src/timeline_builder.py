"""HC:// timeline builder core."""

from __future__ import annotations

from datetime import UTC, datetime

CATEGORY_MAP = {
    "security": "SECURITY",
    "risk": "SECURITY",
    "docs": "DOCUMENTATION",
    "validation": "VALIDATION",
    "schema": "PROTOCOL",
    "trust": "TRUST",
    "queue": "AUTOMATION",
    "pipeline": "AUTOMATION",
}


def choose_category(title: str) -> str:
    text = title.lower()
    for keyword, category in CATEGORY_MAP.items():
        if keyword in text:
            return category
    return "GENERAL"


def build_timeline_entry(*, pr_number: int, title: str, summary: str) -> dict:
    return {
        "pr_number": int(pr_number),
        "title": title.strip(),
        "summary": summary.strip(),
        "category": choose_category(title),
        "recorded_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }


def sort_timeline(entries: list[dict]) -> list[dict]:
    return sorted(entries, key=lambda item: int(item.get("pr_number", 0)))
