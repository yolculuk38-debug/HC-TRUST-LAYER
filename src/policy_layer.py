"""HC:// moderation and policy layer."""

from __future__ import annotations

ALLOWED_POLICY_ACTIONS = {
    "allow",
    "warn",
    "request_review",
    "block",
}

SEVERITY_ACTIONS = {
    "LOW": "allow",
    "MEDIUM": "warn",
    "HIGH": "request_review",
    "CRITICAL": "block",
}


def normalize_severity(severity: str) -> str:
    value = severity.strip().upper()
    return value if value in SEVERITY_ACTIONS else "MEDIUM"


def choose_policy_action(severity: str) -> str:
    return SEVERITY_ACTIONS[normalize_severity(severity)]


def build_policy_decision(*, subject_id: str, severity: str, reason: str) -> dict:
    action = choose_policy_action(severity)
    return {
        "subject_id": subject_id.strip(),
        "severity": normalize_severity(severity),
        "reason": reason.strip(),
        "action": action,
        "requires_review": action in {"request_review", "block"},
    }
