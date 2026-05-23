"""HC:// verification explorer expansion.

Builds deterministic explorer-facing summaries for audit lineage,
federation paths, witness visibility, and replay history.
"""

from __future__ import annotations

from typing import Any, Iterable



def build_explorer_item(
    *,
    record_id: str,
    status: str,
    route: str = "local-validator",
    witnesses: Iterable[str] | None = None,
    federation_path: Iterable[str] | None = None,
    replay_events: Iterable[str] | None = None,
) -> dict[str, Any]:
    """Build a normalized explorer item."""

    return {
        "record_id": record_id.strip(),
        "status": status.strip().upper(),
        "route": route.strip(),
        "witnesses": sorted({witness.strip() for witness in witnesses or [] if witness.strip()}),
        "federation_path": sorted({node.strip() for node in federation_path or [] if node.strip()}),
        "replay_events": sorted({event.strip() for event in replay_events or [] if event.strip()}),
    }



def explorer_visibility_score(item: dict[str, Any]) -> int:
    """Score how much verification context is visible to the explorer."""

    score = 0
    score += 25 if item.get("record_id") else 0
    score += 25 if item.get("witnesses") else 0
    score += 25 if item.get("federation_path") else 0
    score += 25 if item.get("replay_events") else 0
    return score



def build_explorer_summary(item: dict[str, Any]) -> dict[str, Any]:
    """Build deterministic public explorer summary."""

    normalized = build_explorer_item(
        record_id=str(item.get("record_id", "")),
        status=str(item.get("status", "UNKNOWN")),
        route=str(item.get("route", "local-validator")),
        witnesses=item.get("witnesses", []),
        federation_path=item.get("federation_path", []),
        replay_events=item.get("replay_events", []),
    )

    return {
        **normalized,
        "visibility_score": explorer_visibility_score(normalized),
        "has_witness_lineage": bool(normalized["witnesses"]),
        "has_federation_path": bool(normalized["federation_path"]),
        "has_replay_history": bool(normalized["replay_events"]),
    }



def stable_explorer_snapshot(items: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return deterministic explorer ordering."""

    summaries = [build_explorer_summary(item) for item in items]
    return sorted(
        summaries,
        key=lambda item: (
            item["record_id"],
            item["route"],
            item["status"],
        ),
    )


__all__ = [
    "build_explorer_item",
    "explorer_visibility_score",
    "build_explorer_summary",
    "stable_explorer_snapshot",
]
