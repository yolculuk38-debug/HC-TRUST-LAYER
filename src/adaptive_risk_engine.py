"""HC:// adaptive risk engine."""

from __future__ import annotations

from typing import Any


ADAPTIVE_RISK_ENGINE_VERSION = "HC-ADAPTIVE-RISK-V1"


class AdaptiveRiskLevel:
    STABLE = "STABLE"
    ELEVATED = "ELEVATED"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"



def evaluate_adaptive_risk(
    *,
    propagation_growth: int,
    federation_degradation: int,
    anomaly_signals: int,
    trust_decay: int,
) -> dict[str, Any]:
    """Evaluate adaptive and evolving HC:// risk signals."""

    score = 0
    reasons: list[str] = []

    score += max(propagation_growth, 0) * 10
    score += max(federation_degradation, 0) * 15
    score += max(anomaly_signals, 0) * 20
    score += max(trust_decay, 0) * 10

    if propagation_growth:
        reasons.append("propagation_growth_detected")

    if federation_degradation:
        reasons.append("federation_degradation_detected")

    if anomaly_signals:
        reasons.append("anomaly_escalation_detected")

    if trust_decay:
        reasons.append("trust_decay_detected")

    if score >= 80:
        level = AdaptiveRiskLevel.CRITICAL
    elif score >= 50:
        level = AdaptiveRiskLevel.HIGH
    elif score >= 20:
        level = AdaptiveRiskLevel.ELEVATED
    else:
        level = AdaptiveRiskLevel.STABLE

    return {
        "adaptive_risk_engine_version": ADAPTIVE_RISK_ENGINE_VERSION,
        "adaptive_risk_level": level,
        "adaptive_risk_score": score,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "ADAPTIVE_RISK_ENGINE_VERSION",
    "AdaptiveRiskLevel",
    "evaluate_adaptive_risk",
]
