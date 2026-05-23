"""HC:// merge queue controller."""

from __future__ import annotations

RISK_ORDER = {
    "LOW": 0,
    "MEDIUM": 1,
    "HIGH": 2,
}

PRIORITY_ORDER = {
    "HIGH": 0,
    "MEDIUM": 1,
    "LOW": 2,
}


def build_queue_item(*, pr_number: int, risk_level: str, priority: str = "MEDIUM") -> dict:
    return {
        "pr_number": int(pr_number),
        "risk_level": risk_level.strip().upper(),
        "priority": priority.strip().upper(),
        "status": "QUEUED",
    }


def sort_merge_queue(items: list[dict]) -> list[dict]:
    return sorted(
        items,
        key=lambda item: (
            RISK_ORDER.get(item.get("risk_level", "HIGH"), 2),
            PRIORITY_ORDER.get(item.get("priority", "MEDIUM"), 1),
            int(item.get("pr_number", 0)),
        ),
    )


def next_merge_candidate(items: list[dict]) -> dict | None:
    queue = sort_merge_queue(items)
    return queue[0] if queue else None
