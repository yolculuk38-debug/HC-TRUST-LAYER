"""HC:// changelog helper."""

from __future__ import annotations

from datetime import UTC, datetime


def build_changelog_entry(*, title: str, summary: str) -> dict:
    return {
        "title": title.strip(),
        "summary": summary.strip(),
        "timestamp": datetime.now(UTC).isoformat(),
    }
