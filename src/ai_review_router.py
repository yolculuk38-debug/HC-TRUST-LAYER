"""HC:// AI reviewer orchestration."""

from __future__ import annotations

REVIEWER_GROUPS = {
    "LOW": ["automation-review"],
    "MEDIUM": ["protocol-review", "automation-review"],
    "HIGH": ["security-review", "manual-review"],
}


def select_review_group(risk_level: str) -> list[str]:
    return REVIEWER_GROUPS.get(risk_level.strip().upper(), ["protocol-review"])


def escalation_required(*, approvals: int, rejections: int) -> bool:
    return rejections > approvals


def build_review_route(*, risk_level: str, approvals: int, rejections: int) -> dict:
    return {
        "risk_level": risk_level.strip().upper(),
        "reviewers": select_review_group(risk_level),
        "escalation_required": escalation_required(
            approvals=approvals,
            rejections=rejections,
        ),
    }
