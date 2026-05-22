"""HC:// verification timeline engine."""

from __future__ import annotations

from typing import Any


VERIFICATION_TIMELINE_VERSION = "HC-VERIFICATION-TIMELINE-V1"


def build_timeline_event(
    *,
    event_type: str,
    timestamp: str,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a verification lifecycle event."""

    return {
        "event_type": event_type,
        "timestamp": timestamp,
        "details": details or {},
    }



def build_verification_timeline(
    *,
    record_id: str,
    events: list[dict[str, Any]],
) -> dict[str, Any]:
    """Build verification lifecycle timeline."""

    ordered_events = sorted(events, key=lambda item: item.get("timestamp", ""))

    return {
        "verification_timeline_version": VERIFICATION_TIMELINE_VERSION,
        "record_id": record_id,
        "event_count": len(ordered_events),
        "events": ordered_events,
    }



def evaluate_verification_timeline(
    timeline: dict[str, Any],
) -> dict[str, Any]:
    """Evaluate timeline completeness and lifecycle visibility."""

    if not isinstance(timeline, dict):
        return _result(False, ["invalid_timeline_structure"])

    reasons: list[str] = []
    event_types = {
        event.get("event_type")
        for event in timeline.get("events", [])
    }

    required = {
        "FIRST_SEEN",
        "VERIFICATION",
    }

    missing = required - event_types

    for item in sorted(missing):
        reasons.append(f"missing_{item.lower()}_event")

    trusted = not reasons

    return _result(trusted, reasons)



def _result(trusted: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "verification_timeline_version": VERIFICATION_TIMELINE_VERSION,
        "trusted": trusted,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "VERIFICATION_TIMELINE_VERSION",
    "build_timeline_event",
    "build_verification_timeline",
    "evaluate_verification_timeline",
]
