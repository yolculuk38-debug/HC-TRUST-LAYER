"""HC:// merge queue hardening core."""

from __future__ import annotations


def detect_duplicate_prs(items: list[dict]) -> list[int]:
    """Return duplicate PR numbers from queue items."""

    seen: set[int] = set()
    duplicates: set[int] = set()

    for item in items:
        pr_number = int(item.get("pr_number", 0))
        if pr_number in seen:
            duplicates.add(pr_number)
        seen.add(pr_number)

    return sorted(duplicates)


def mark_stale_items(items: list[dict], *, max_age_hours: int) -> list[dict]:
    """Mark queue items as stale when their age exceeds the allowed window."""

    hardened: list[dict] = []
    for item in items:
        updated = dict(item)
        age_hours = int(updated.get("age_hours", 0))
        if age_hours > max_age_hours:
            updated["status"] = "STALE"
        hardened.append(updated)
    return hardened


def requeue_failed_item(item: dict) -> dict:
    """Return a failed item to the queue with incremented retry count."""

    updated = dict(item)
    updated["retry_count"] = int(updated.get("retry_count", 0)) + 1
    updated["status"] = "REQUEUED"
    return updated
