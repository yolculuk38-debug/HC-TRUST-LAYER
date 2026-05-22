"""HC:// human review queue system.

This module keeps human review entries deterministic and auditable while
remaining lightweight enough for GitHub-based verification workflows.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any


REVIEW_QUEUE_VERSION = "HC-REVIEW-QUEUE-V1"

ALLOWED_PRIORITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
ALLOWED_DECISIONS = {"APPROVED", "REJECTED", "NEEDS_MORE_EVIDENCE", "ESCALATED"}
OPEN_STATUSES = {"PENDING_REVIEW", "NEEDS_MORE_EVIDENCE", "ESCALATED"}
FINAL_STATUSES = {"APPROVED", "REJECTED"}


def _utc_now() -> str:
    """Return an ISO-8601 UTC timestamp with second precision."""

    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _require_non_empty(value: str, field_name: str) -> str:
    """Validate required text fields."""

    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


def create_review_entry(
    *,
    record_id: str,
    priority: str,
    reason: str,
) -> dict[str, Any]:
    """Create a human review queue entry."""

    normalized_priority = priority.strip().upper()
    if normalized_priority not in ALLOWED_PRIORITIES:
        raise ValueError(f"priority must be one of: {sorted(ALLOWED_PRIORITIES)}")

    return {
        "review_queue_version": REVIEW_QUEUE_VERSION,
        "record_id": _require_non_empty(record_id, "record_id"),
        "priority": normalized_priority,
        "reason": _require_non_empty(reason, "reason"),
        "status": "PENDING_REVIEW",
        "created_at": _utc_now(),
        "history": [],
    }


def add_review_decision(
    entry: dict[str, Any],
    *,
    reviewer_id: str,
    decision: str,
    note: str,
) -> dict[str, Any]:
    """Append a validated review decision to entry history."""

    current_status = entry.get("status")
    if current_status in FINAL_STATUSES:
        raise ValueError("finalized review entries cannot be changed")

    normalized_decision = decision.strip().upper()
    if normalized_decision not in ALLOWED_DECISIONS:
        raise ValueError(f"decision must be one of: {sorted(ALLOWED_DECISIONS)}")

    history = list(entry.get("history", []))
    history.append(
        {
            "reviewer_id": _require_non_empty(reviewer_id, "reviewer_id"),
            "decision": normalized_decision,
            "note": _require_non_empty(note, "note"),
            "decided_at": _utc_now(),
        }
    )

    updated = dict(entry)
    updated["history"] = history
    updated["status"] = normalized_decision

    return updated


def needs_review(entry: dict[str, Any]) -> bool:
    """Return True when an entry is still awaiting human resolution."""

    return entry.get("status") in OPEN_STATUSES


__all__ = [
    "ALLOWED_DECISIONS",
    "ALLOWED_PRIORITIES",
    "FINAL_STATUSES",
    "OPEN_STATUSES",
    "REVIEW_QUEUE_VERSION",
    "add_review_decision",
    "create_review_entry",
    "needs_review",
]
