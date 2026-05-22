"""HC:// trust score engine."""

from __future__ import annotations

from typing import Any


TRUST_SCORE_ENGINE_VERSION = "HC-TRUST-SCORE-ENGINE-V1"


class TrustTier:
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    VERIFIED = "VERIFIED"



def calculate_trust_score(
    *,
    evidence_score: int,
    manipulation_risk: str,
    federation_weight: int,
    audit_continuity: bool,
    provenance_continuity: bool,
) -> dict[str, Any]:
    """Calculate explainable HC:// trust score."""

    score = int(evidence_score)
    reasons: list[str] = []

    score += min(max(federation_weight, 0), 20)

    if audit_continuity:
        score += 10
    else:
        reasons.append("missing_audit_continuity")

    if provenance_continuity:
        score += 10
    else:
        reasons.append("missing_provenance_continuity")

    if manipulation_risk == "MEDIUM":
        score -= 15
        reasons.append("medium_manipulation_penalty")
    elif manipulation_risk == "HIGH":
        score -= 35
        reasons.append("high_manipulation_penalty")
    elif manipulation_risk == "CRITICAL":
        score -= 60
        reasons.append("critical_manipulation_penalty")

    score = max(0, min(score, 100))

    if score >= 90:
        tier = TrustTier.VERIFIED
    elif score >= 70:
        tier = TrustTier.HIGH
    elif score >= 40:
        tier = TrustTier.MODERATE
    else:
        tier = TrustTier.LOW

    return {
        "trust_score_engine_version": TRUST_SCORE_ENGINE_VERSION,
        "trust_score": score,
        "trust_tier": tier,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "TRUST_SCORE_ENGINE_VERSION",
    "TrustTier",
    "calculate_trust_score",
]
