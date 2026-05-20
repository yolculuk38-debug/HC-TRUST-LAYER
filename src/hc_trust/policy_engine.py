from typing import Dict


DECISION_ACCEPT = "ACCEPT"
DECISION_REVIEW = "REVIEW"
DECISION_DISPUTE = "DISPUTE"
DECISION_REJECT = "REJECT"


def evaluate_trust_policy(
    *,
    normalized_score: int,
    risk_flags: Dict | None = None,
    witness_summary: Dict | None = None,
) -> Dict:
    """Evaluate HC:// trust policy and return a machine-readable decision."""

    if not isinstance(normalized_score, int):
        raise ValueError("normalized_score must be an integer")

    score = max(0, min(normalized_score, 100))
    risk_flags = risk_flags or {}
    witness_summary = witness_summary or {}

    high_risk = risk_flags.get("high_risk") is True
    risk_flag_count = int(risk_flags.get("risk_flag_count", 0))
    has_independent_mix = witness_summary.get("has_independent_mix") is True

    reasons = []

    if high_risk:
        decision = DECISION_REJECT
        reasons.append("high_risk_flag_present")
    elif score < 26:
        decision = DECISION_REJECT
        reasons.append("score_below_minimum_trust_threshold")
    elif risk_flag_count >= 3:
        decision = DECISION_DISPUTE
        reasons.append("multiple_risk_flags_present")
    elif score < 76:
        decision = DECISION_REVIEW
        reasons.append("score_requires_review")
    elif not has_independent_mix:
        decision = DECISION_REVIEW
        reasons.append("independent_witness_mix_missing")
    else:
        decision = DECISION_ACCEPT
        reasons.append("score_and_witness_policy_passed")

    return {
        "decision": decision,
        "score": score,
        "reasons": reasons,
        "experimental": True,
    }
