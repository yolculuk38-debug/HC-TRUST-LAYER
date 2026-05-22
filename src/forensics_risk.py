"""HC:// forensics risk core."""

from __future__ import annotations


def calculate_forensics_risk(*, mismatch_count: int, anomaly_count: int) -> dict:
    score = (mismatch_count * 15) + (anomaly_count * 20)

    if score >= 80:
        level = "CRITICAL"
    elif score >= 50:
        level = "HIGH"
    elif score >= 25:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "forensics_risk_score": score,
        "forensics_risk_level": level,
    }
