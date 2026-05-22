"""HC:// distributed validator consensus core."""

from __future__ import annotations

from collections import Counter
from typing import Any


VALIDATOR_CONSENSUS_VERSION = "HC-VALIDATOR-CONSENSUS-V1"

CONSENSUS_VERIFIED = "VERIFIED"
CONSENSUS_WARNING = "WARNING"
CONSENSUS_REJECTED = "REJECTED"

ALLOWED_DECISIONS = {
    CONSENSUS_VERIFIED,
    CONSENSUS_WARNING,
    CONSENSUS_REJECTED,
}



def normalize_decision(decision: str) -> str:
    normalized = decision.strip().upper()

    if normalized not in ALLOWED_DECISIONS:
        raise ValueError(f"invalid consensus decision: {decision}")

    return normalized



def build_validator_vote(
    *,
    node_id: str,
    decision: str,
    trust_weight: int,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create normalized validator vote."""

    return {
        "node_id": node_id.strip(),
        "decision": normalize_decision(decision),
        "trust_weight": max(0, int(trust_weight)),
        "metadata": metadata or {},
    }



def calculate_consensus(
    votes: list[dict[str, Any]],
) -> dict[str, Any]:
    """Calculate weighted validator consensus."""

    if not votes:
        raise ValueError("consensus requires at least one vote")

    weighted_totals: Counter[str] = Counter()

    for vote in votes:
        decision = normalize_decision(vote["decision"])
        weighted_totals[decision] += max(0, int(vote["trust_weight"]))

    consensus_decision, consensus_weight = weighted_totals.most_common(1)[0]
    total_weight = sum(weighted_totals.values())

    confidence = 0
    if total_weight > 0:
        confidence = round((consensus_weight / total_weight) * 100, 2)

    return {
        "validator_consensus_version": VALIDATOR_CONSENSUS_VERSION,
        "consensus_decision": consensus_decision,
        "consensus_confidence": confidence,
        "total_validator_weight": total_weight,
        "weighted_totals": dict(weighted_totals),
        "vote_count": len(votes),
    }


__all__ = [
    "ALLOWED_DECISIONS",
    "CONSENSUS_REJECTED",
    "CONSENSUS_VERIFIED",
    "CONSENSUS_WARNING",
    "VALIDATOR_CONSENSUS_VERSION",
    "build_validator_vote",
    "calculate_consensus",
    "normalize_decision",
]
