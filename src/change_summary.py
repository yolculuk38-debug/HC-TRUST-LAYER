"""HC:// change summary helper."""

from __future__ import annotations

from datetime import UTC, datetime


def build_change_summary(*, version: str, title: str, changes: list[str]) -> dict:
    """Create a structured change summary for merged work."""

    return {
        "version": version.strip(),
        "title": title.strip(),
        "changes": [change.strip() for change in changes if change.strip()],
        "created_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }


def summarize_change(summary: dict) -> str:
    changes = summary.get("changes", [])
    return f"{summary.get('version', 'unknown')} - {summary.get('title', '')}: {len(changes)} changes"
