"""HC:// human review queue system."""

from __future__ import annotations

from typing import Any


REVIEW_QUEUE_VERSION = "HC-REVIEW-QUEUE-V1"



def create_review_entry(
    *,
    record_id: str,
    priority: str,
    reason: str,
) -> dict[str, Any]:
    """Create review queue entry."""

    return {
        "review_queue_version": REVIEW_QUEUE_VERSION,
        "record_id": record_id,
        "priority": priority,
        "reason": reason,
        "status": "PENDING_REVIEW",
        "history": [],
    }



def add_review_decision(
    entry: dict[str, Any],
    *,
    reviewer_id: str,
    decision: str,
    note: str,
) -> dict[str, Any]:
    """Append review decision history."""

    history = list(entry.get("history", []))

    history.append(
        {
            "reviewer_id": reviewer_id,
            "decision": decision,
            "note": note,
        }
    )

    updated = dict(entry)
    updated["history"] = history
    updated["status"] = decision

    return updated


__all__ = [
    "REVIEW_QUEUE_VERSION",
    "create_review_entry",
    "add_review_decision",
]
