"""HC:// contributor trust roles."""

from __future__ import annotations

ROLE_LEVELS = {
    "observer": 0,
    "contributor": 1,
    "reviewer": 2,
    "maintainer": 3,
}


def calculate_role_level(role: str) -> int:
    return ROLE_LEVELS.get(role.strip().lower(), 0)


def can_escalate_review(*, actor_role: str, target_role: str) -> bool:
    return calculate_role_level(actor_role) >= calculate_role_level(target_role)


def build_role_record(*, actor: str, role: str, reputation: int) -> dict:
    return {
        "actor": actor.strip(),
        "role": role.strip().lower(),
        "reputation": max(0, min(int(reputation), 100)),
        "role_level": calculate_role_level(role),
    }
