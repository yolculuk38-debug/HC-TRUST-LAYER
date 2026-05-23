"""HC:// governance automation layer."""

from __future__ import annotations

ALLOWED_ACTIONS = {
    "merge_low_risk",
    "request_manual_review",
    "queue_validation",
    "trigger_audit",
}


class GovernanceViolationError(RuntimeError):
    """Raised when governance rules are violated."""


def validate_governance_action(action: str) -> bool:
    return action in ALLOWED_ACTIONS


def enforce_manual_review(risk_level: str) -> bool:
    return risk_level.upper() in {"HIGH", "CRITICAL"}


def build_governance_record(*, actor: str, action: str, risk_level: str) -> dict:
    if not validate_governance_action(action):
        raise GovernanceViolationError(f"unsupported governance action: {action}")

    return {
        "actor": actor,
        "action": action,
        "risk_level": risk_level.upper(),
        "manual_review_required": enforce_manual_review(risk_level),
    }
