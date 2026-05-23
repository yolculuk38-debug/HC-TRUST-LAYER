"""HC:// immutable replay audit expansion.

Extends replay lineage visibility and deterministic replay verification.
"""

from __future__ import annotations

from typing import Any, Iterable


REPLAY_VERIFIED = "REPLAY_VERIFIED"
REPLAY_MISMATCH = "REPLAY_MISMATCH"
REPLAY_INCOMPLETE = "REPLAY_INCOMPLETE"



def normalize_replay_event(event: dict[str, Any]) -> dict[str, Any]:
    """Normalize replay audit event."""

    return {
        "event_id": str(event.get("event_id", "")).strip(),
        "record_id": str(event.get("record_id", "")).strip(),
        "snapshot_hash": str(event.get("snapshot_hash", "")).strip(),
        "verified": bool(event.get("verified", False)),
    }



def replay_lineage(events: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return deterministic replay lineage ordering."""

    normalized = [normalize_replay_event(event) for event in events]

    return sorted(
        normalized,
        key=lambda item: (
            item["record_id"],
            item["event_id"],
            item["snapshot_hash"],
        ),
    )



def replay_status(events: Iterable[dict[str, Any]]) -> str:
    """Determine immutable replay audit status."""

    normalized = replay_lineage(events)

    if not normalized:
        return REPLAY_INCOMPLETE

    if all(event["verified"] for event in normalized):
        return REPLAY_VERIFIED

    return REPLAY_MISMATCH



def build_replay_summary(events: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Build deterministic replay audit summary."""

    lineage = replay_lineage(events)

    return {
        "replay_status": replay_status(lineage),
        "event_count": len(lineage),
        "verified_events": len([event for event in lineage if event["verified"]]),
        "record_ids": sorted({event["record_id"] for event in lineage}),
    }


__all__ = [
    "REPLAY_VERIFIED",
    "REPLAY_MISMATCH",
    "REPLAY_INCOMPLETE",
    "normalize_replay_event",
    "replay_lineage",
    "replay_status",
    "build_replay_summary",
]
