"""HC:// trust score engine."""

from __future__ import annotations

from typing import Any


TRUST_SCORE_ENGINE_VERSION = "HC-TRUST-SCORE-ENGINE-V2"
MAX_TRUST_SCORE = 100


class TrustTier:
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    VERIFIED = "VERIFIED"



def clamp_score(value: int) -> int:
    """Clamp score into normalized range."""

    return max(0, min(value, MAX_TRUST_SCORE))



def calculate_trust_score(
    *,
    evidence_score: int,
    manipulation_risk: str,
    federation_weight: int,
    audit_continuity: bool,
    provenance_continuity: bool,
    witness_count: int = 0,
) -> dict[str, Any]:
    """Calculate explainable HC:// trust score."""

    score = int(evidence_score)
    reasons: list[str] = []

    score += min(max(federation_weight, 0), 20)
    score += min(max(witness_count, 0), 5) * 3

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

    score = clamp_score(score)

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
        "max_trust_score": MAX_TRUST_SCORE,
        "trust_tier": tier,
        "reasons": sorted(set(reasons)),
        "witness_count": witness_count,
    }


__all__ = [
    "MAX_TRUST_SCORE",
    "TRUST_SCORE_ENGINE_VERSION",
    "TrustTier",
    "calculate_trust_score",
    "clamp_score",
]
