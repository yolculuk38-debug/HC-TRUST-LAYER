"""HC:// trust score engine core.

Trust scores are heuristic verification signals.
They are not absolute truth values.
"""

from __future__ import annotations

from typing import Any


MAX_SCORE = 100
MIN_SCORE = 0


def clamp_score(score: float) -> int:
    """Clamp score to HC:// trust score bounds."""

    return max(MIN_SCORE, min(MAX_SCORE, round(score)))


def calculate_trust_score(data: dict[str, Any]) -> dict[str, Any]:
    """Calculate a deterministic trust score.

    Inputs are intentionally conservative and auditable.
    """

    score = 0.0
    reasons: list[str] = []

    verified_hash = bool(data.get("verified_hash"))
    qr_verified = bool(data.get("qr_verified"))
    signed = bool(data.get("signed"))
    audit_snapshot = bool(data.get("audit_snapshot"))
    export_verified = bool(data.get("export_verified"))
    consensus = bool(data.get("consensus_reached"))

    witness_count = int(data.get("witness_count", 0))
    conflict_count = int(data.get("conflict_count", 0))
    unsafe_flags = int(data.get("unsafe_flags", 0))

    if verified_hash:
        score += 25
        reasons.append("verified content hash")

    if qr_verified:
        score += 10
        reasons.append("verified QR payload")

    if signed:
        score += 15
        reasons.append("signed verification")

    if audit_snapshot:
        score += 10
        reasons.append("audit snapshot present")

    if export_verified:
        score += 10
        reasons.append("verified export/import package")

    if consensus:
        score += 20
        reasons.append("multi-witness consensus reached")

    if witness_count > 0:
        witness_bonus = min(witness_count * 2, 10)
        score += witness_bonus
        reasons.append(f"{witness_count} witness participation")

    if conflict_count > 0:
        penalty = min(conflict_count * 15, 45)
        score -= penalty
        reasons.append(f"-{penalty} conflict penalty")

    if unsafe_flags > 0:
        penalty = min(unsafe_flags * 20, 60)
        score -= penalty
        reasons.append(f"-{penalty} unsafe verification penalty")

    final_score = clamp_score(score)

    if final_score >= 85:
        trust_level = "HIGH"
    elif final_score >= 60:
        trust_level = "MODERATE"
    elif final_score >= 35:
        trust_level = "LOW"
    else:
        trust_level = "UNTRUSTED"

    return {
        "trust_score": final_score,
        "trust_level": trust_level,
        "trusted": final_score >= 60,
        "reasons": reasons,
    }


__all__ = ["calculate_trust_score", "clamp_score"]
