"""HC:// security gate layer."""

from __future__ import annotations

from typing import Any


SECURITY_GATE_VERSION = "HC-SECURITY-GATE-V1"


class SecurityDecision:
    ALLOW = "ALLOW"
    REVIEW = "REVIEW"
    QUARANTINE = "QUARANTINE"
    CRITICAL_LOCK = "CRITICAL_LOCK"



def evaluate_security_gate(
    *,
    risk_level: str,
    adaptive_risk: str,
    compromised_nodes: int = 0,
) -> dict[str, Any]:
    """Evaluate quarantine and escalation security gates."""

    reasons: list[str] = []

    if risk_level == "CRITICAL" or adaptive_risk == "CRITICAL":
        reasons.append("critical_risk_detected")
        decision = SecurityDecision.CRITICAL_LOCK
    elif compromised_nodes >= 2:
        reasons.append("multiple_compromised_nodes")
        decision = SecurityDecision.QUARANTINE
    elif risk_level in {"HIGH", "ELEVATED"}:
        reasons.append("human_review_required")
        decision = SecurityDecision.REVIEW
    else:
        decision = SecurityDecision.ALLOW

    return {
        "security_gate_version": SECURITY_GATE_VERSION,
        "decision": decision,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "SECURITY_GATE_VERSION",
    "SecurityDecision",
    "evaluate_security_gate",
]
