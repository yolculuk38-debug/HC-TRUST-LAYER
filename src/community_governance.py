"""HC:// community governance core."""

from __future__ import annotations

COMMUNITY_ROLES = {
    "observer",
    "contributor",
    "reviewer",
    "maintainer",
    "security_reporter",
}

SENSITIVE_ACTIONS = {
    "merge",
    "release",
    "security_change",
    "schema_change",
    "workflow_change",
}


def normalize_role(role: str) -> str:
    value = role.strip().lower()
    return value if value in COMMUNITY_ROLES else "observer"


def can_request_review(role: str) -> bool:
    return normalize_role(role) in {"contributor", "reviewer", "maintainer", "security_reporter"}


def requires_maintainer_action(action: str) -> bool:
    return action.strip().lower() in SENSITIVE_ACTIONS


def build_community_record(*, actor: str, role: str, action: str) -> dict:
    normalized_role = normalize_role(role)
    return {
        "actor": actor.strip(),
        "role": normalized_role,
        "action": action.strip().lower(),
        "review_allowed": can_request_review(normalized_role),
        "maintainer_required": requires_maintainer_action(action),
    }
