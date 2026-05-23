"""HC:// federation resilience package.

Adds deterministic helpers for federation recovery, validator reputation,
trust weighting, peer isolation, and conflict resolution.
"""

from __future__ import annotations

from typing import Any, Iterable

RESOLVED = "RESOLVED"
NEEDS_REVIEW = "NEEDS_REVIEW"
ISOLATED = "ISOLATED"



def normalize_peer(peer: dict[str, Any]) -> dict[str, Any]:
    """Normalize federation peer state."""

    failures = max(0, int(peer.get("failed_attempts", 0)))
    trust_score = max(0, min(int(peer.get("trust_score", 0)), 100))

    return {
        "node_id": str(peer.get("node_id", "")).strip(),
        "trust_score": trust_score,
        "failed_attempts": failures,
        "active": bool(peer.get("active", True)),
        "isolated": failures >= 5 or trust_score < 25,
    }



def reputation_score(peer: dict[str, Any]) -> int:
    """Calculate deterministic validator reputation score."""

    normalized = normalize_peer(peer)
    penalty = normalized["failed_attempts"] * 5
    return max(0, normalized["trust_score"] - penalty)



def weighted_trust(peers: Iterable[dict[str, Any]]) -> int:
    """Calculate weighted trust score for active non-isolated peers."""

    normalized = [normalize_peer(peer) for peer in peers]
    eligible = [peer for peer in normalized if peer["active"] and not peer["isolated"]]

    if not eligible:
        return 0

    return round(sum(reputation_score(peer) for peer in eligible) / len(eligible))



def isolated_peers(peers: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return deterministic list of isolated peers."""

    isolated = [normalize_peer(peer) for peer in peers if normalize_peer(peer)["isolated"]]
    return sorted(isolated, key=lambda item: item["node_id"])



def resolve_conflict(results: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Resolve federation result conflict deterministically."""

    normalized = [
        {
            "record_id": str(result.get("record_id", "")).strip(),
            "status": str(result.get("status", "UNKNOWN")).strip().upper(),
            "trust_score": max(0, min(int(result.get("trust_score", 0)), 100)),
        }
        for result in results
    ]

    if not normalized:
        return {"status": NEEDS_REVIEW, "reason": "no federation results"}

    best = sorted(
        normalized,
        key=lambda item: (-item["trust_score"], item["status"], item["record_id"]),
    )[0]

    if best["trust_score"] < 70:
        return {"status": NEEDS_REVIEW, "reason": "insufficient trust score", "selected": best}

    return {"status": RESOLVED, "selected": best}


__all__ = [
    "RESOLVED",
    "NEEDS_REVIEW",
    "ISOLATED",
    "normalize_peer",
    "reputation_score",
    "weighted_trust",
    "isolated_peers",
    "resolve_conflict",
]
