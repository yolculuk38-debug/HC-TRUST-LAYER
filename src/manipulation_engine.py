"""HC:// manipulation propagation engine."""

from __future__ import annotations

from typing import Any


MANIPULATION_ENGINE_VERSION = "HC-MANIPULATION-ENGINE-V1"


class ManipulationRisk:
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"



def evaluate_manipulation_signals(signals: dict[str, Any]) -> dict[str, Any]:
    """Evaluate coordinated manipulation and propagation risk."""

    if not isinstance(signals, dict):
        return _result(ManipulationRisk.CRITICAL, 100, ["invalid_signal_structure"])

    score = 0
    reasons: list[str] = []

    repost_clusters = int(signals.get("repost_clusters", 0) or 0)
    self_reference_loops = int(signals.get("self_reference_loops", 0) or 0)
    coordinated_signals = int(signals.get("coordinated_signals", 0) or 0)
    contamination_links = int(signals.get("contamination_links", 0) or 0)

    score += repost_clusters * 10
    score += self_reference_loops * 15
    score += coordinated_signals * 20
    score += contamination_links * 25

    if repost_clusters:
        reasons.append("repost_cluster_detected")

    if self_reference_loops:
        reasons.append("self_reference_loop_detected")

    if coordinated_signals:
        reasons.append("coordinated_manipulation_detected")

    if contamination_links:
        reasons.append("trust_contamination_detected")

    if score >= 80:
        return _result(ManipulationRisk.CRITICAL, score, reasons)

    if score >= 50:
        return _result(ManipulationRisk.HIGH, score, reasons)

    if score >= 20:
        return _result(ManipulationRisk.MEDIUM, score, reasons)

    return _result(ManipulationRisk.LOW, score, reasons)



def _result(risk: str, score: int, reasons: list[str]) -> dict[str, Any]:
    return {
        "manipulation_engine_version": MANIPULATION_ENGINE_VERSION,
        "risk": risk,
        "risk_score": score,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "MANIPULATION_ENGINE_VERSION",
    "ManipulationRisk",
    "evaluate_manipulation_signals",
]
