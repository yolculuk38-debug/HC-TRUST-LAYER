"""HC:// distributed validator consensus layer.

Implements deterministic validator agreement helpers for distributed
verification preparation.
"""

from __future__ import annotations

from typing import Any, Iterable


MINIMUM_CONSENSUS = 3
DEFAULT_THRESHOLD = 0.66



def normalize_vote(vote: dict[str, Any]) -> dict[str, Any]:
    """Normalize validator vote."""

    return {
        "validator_id": str(vote.get("validator_id", "")).strip(),
        "decision": str(vote.get("decision", "reject")).strip().lower(),
        "trust_score": max(0, min(int(vote.get("trust_score", 0)), 100)),
    }



def eligible_votes(votes: Iterable[dict[str, Any]], minimum_score: int = 70) -> list[dict[str, Any]]:
    """Filter eligible validator votes."""

    normalized = [normalize_vote(vote) for vote in votes]
    return [vote for vote in normalized if vote["trust_score"] >= minimum_score]



def consensus_ratio(votes: Iterable[dict[str, Any]], decision: str = "approve") -> float:
    """Calculate deterministic consensus ratio."""

    normalized = [normalize_vote(vote) for vote in votes]

    if not normalized:
        return 0.0

    matching = [vote for vote in normalized if vote["decision"] == decision]
    return len(matching) / len(normalized)



def consensus_reached(
    votes: Iterable[dict[str, Any]],
    *,
    threshold: float = DEFAULT_THRESHOLD,
    minimum_votes: int = MINIMUM_CONSENSUS,
) -> bool:
    """Determine if distributed validator consensus is reached."""

    normalized = eligible_votes(votes)

    if len(normalized) < int(minimum_votes):
        return False

    return consensus_ratio(normalized) >= float(threshold)



def build_consensus_result(votes: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Build deterministic consensus result."""

    normalized = eligible_votes(votes)
    ratio = consensus_ratio(normalized)

    return {
        "eligible_validators": len(normalized),
        "consensus_ratio": round(ratio, 4),
        "consensus_reached": consensus_reached(normalized),
        "validator_ids": sorted({vote["validator_id"] for vote in normalized}),
    }


__all__ = [
    "MINIMUM_CONSENSUS",
    "DEFAULT_THRESHOLD",
    "normalize_vote",
    "eligible_votes",
    "consensus_ratio",
    "consensus_reached",
    "build_consensus_result",
]
