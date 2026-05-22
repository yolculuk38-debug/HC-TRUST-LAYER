"""HC:// trust orchestrator core."""

from __future__ import annotations

from typing import Any

from evidence_engine import evaluate_evidence_bundle
from manipulation_engine import evaluate_manipulation_signals
from policy_engine import evaluate_policy
from risk_summary import build_risk_summary


TRUST_ORCHESTRATOR_VERSION = "HC-TRUST-ORCHESTRATOR-V1"



def orchestrate_trust_pipeline(
    *,
    evidence_bundle: dict[str, Any],
    manipulation_signals: dict[str, Any],
    registry_trusted: bool,
    federation_trusted: bool,
    revoked: bool,
) -> dict[str, Any]:
    """Run the HC:// trust orchestration pipeline."""

    evidence_result = evaluate_evidence_bundle(evidence_bundle)

    manipulation_result = evaluate_manipulation_signals(manipulation_signals)

    policy_result = evaluate_policy(
        evidence_score=evidence_result.get("evidence_score", 0),
        manipulation_risk=manipulation_result.get("risk", "LOW"),
        registry_trusted=registry_trusted,
        federation_trusted=federation_trusted,
        revoked=revoked,
    )

    risk_result = build_risk_summary(
        manipulation_result=manipulation_result,
        policy_result=policy_result,
    )

    return {
        "trust_orchestrator_version": TRUST_ORCHESTRATOR_VERSION,
        "evidence": evidence_result,
        "manipulation": manipulation_result,
        "policy": policy_result,
        "risk": risk_result,
    }


__all__ = [
    "TRUST_ORCHESTRATOR_VERSION",
    "orchestrate_trust_pipeline",
]
