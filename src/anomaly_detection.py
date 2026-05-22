"""HC:// anomaly detection core."""

from __future__ import annotations

from typing import Any

ANOMALY_DETECTION_VERSION = "HC-ANOMALY-DETECTION-V1"

RISK_LEVELS = {
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
}



def detect_verification_anomalies(
    *,
    failed_attempts: int,
    consensus_confidence: float,
    revoked_entity_detected: bool,
    manipulation_signals: int,
) -> dict[str, Any]:
    risk = "LOW"
    reasons: list[str] = []

    if failed_attempts >= 5:
        risk = "MEDIUM"
        reasons.append("multiple_failed_attempts")

    if consensus_confidence < 40:
        risk = "HIGH"
        reasons.append("low_consensus_confidence")

    if revoked_entity_detected:
        risk = "CRITICAL"
        reasons.append("revoked_entity_detected")

    if manipulation_signals >= 3:
        risk = "CRITICAL"
        reasons.append("manipulation_signal_threshold")

    return {
        "anomaly_detection_version": ANOMALY_DETECTION_VERSION,
        "risk_level": risk,
        "reasons": sorted(set(reasons)),
    }
