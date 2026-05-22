"""HC:// policy engine."""

from __future__ import annotations

from typing import Any


POLICY_ENGINE_VERSION = "HC-POLICY-ENGINE-V1"


class PolicyDecision:
    ALLOW = "ALLOW"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    DENY = "DENY"



def evaluate_policy(
    *,
    evidence_score: int,
    manipulation_risk: str = "LOW",
    registry_trusted: bool = False,
    federation_trusted: bool = False,
    revoked: bool = False,
) -> dict[str, Any]:
    """Evaluate HC:// verification policy requirements."""

    reasons: list[str] = []

    if revoked:
        return _result(PolicyDecision.DENY, ["revoked_record_or_certificate"])

    if evidence_score < 60:
        reasons.append("evidence_score_below_policy_threshold")

    if manipulation_risk in {"HIGH", "CRITICAL"}:
        reasons.append("manipulation_risk_above_policy_threshold")

    if not registry_trusted:
        reasons.append("registry_not_trusted")

    if not federation_trusted:
        reasons.append("federation_not_trusted")

    if reasons:
        return _result(PolicyDecision.REVIEW_REQUIRED, reasons)

    return _result(PolicyDecision.ALLOW, [])



def _result(decision: str, reasons: list[str]) -> dict[str, Any]:
    return {
        "policy_engine_version": POLICY_ENGINE_VERSION,
        "decision": decision,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "POLICY_ENGINE_VERSION",
    "PolicyDecision",
    "evaluate_policy",
]
