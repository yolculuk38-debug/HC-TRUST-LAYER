"""HC:// governance policy core."""

from __future__ import annotations

ALLOWED_POLICY_STATES = {
    "DRAFT",
    "ACTIVE",
    "RETIRED",
}


def create_governance_policy(*, policy_id: str, title: str, state: str) -> dict:
    normalized = state.strip().upper()

    if normalized not in ALLOWED_POLICY_STATES:
        raise ValueError("invalid governance policy state")

    return {
        "policy_id": policy_id.strip(),
        "title": title.strip(),
        "state": normalized,
    }
