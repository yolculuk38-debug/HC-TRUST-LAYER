"""HC:// federation consensus engine."""

from __future__ import annotations

from typing import Any


FEDERATION_CONSENSUS_VERSION = "HC-FEDERATION-CONSENSUS-V1"


class ConsensusDecision:
    CONSENSUS_REACHED = "CONSENSUS_REACHED"
    PARTIAL_CONSENSUS = "PARTIAL_CONSENSUS"
    CONFLICT = "CONFLICT"



def evaluate_federation_consensus(
    federation_votes: list[dict[str, Any]],
    quorum_threshold: int = 70,
) -> dict[str, Any]:
    """Evaluate weighted federation consensus."""

    total_weight = 0
    approval_weight = 0
    rejection_weight = 0
    reasons: list[str] = []

    for vote in federation_votes:
        weight = int(vote.get("weight", 0) or 0)
        approved = bool(vote.get("approved", False))

        total_weight += weight

        if approved:
            approval_weight += weight
        else:
            rejection_weight += weight

    consensus_score = 0

    if total_weight > 0:
        consensus_score = int((approval_weight / total_weight) * 100)

    if rejection_weight > approval_weight:
        reasons.append("federation_conflict_detected")
        decision = ConsensusDecision.CONFLICT
    elif consensus_score >= quorum_threshold:
        decision = ConsensusDecision.CONSENSUS_REACHED
    else:
        reasons.append("quorum_not_reached")
        decision = ConsensusDecision.PARTIAL_CONSENSUS

    return {
        "federation_consensus_version": FEDERATION_CONSENSUS_VERSION,
        "decision": decision,
        "consensus_score": consensus_score,
        "approval_weight": approval_weight,
        "rejection_weight": rejection_weight,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "FEDERATION_CONSENSUS_VERSION",
    "ConsensusDecision",
    "evaluate_federation_consensus",
]
