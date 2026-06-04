"""Minimal HC:// advisory risk summary compatibility module."""

from __future__ import annotations

from enum import Enum
from typing import Any


class RiskLevel(str, Enum):
    """Advisory risk labels used by compatibility tests."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


def _as_upper(value: Any) -> str:
    if isinstance(value, Enum):
        value = value.value
    return str(value or "").upper()


def _collect_reasons(*results: dict[str, Any] | None) -> list[str]:
    reasons: list[str] = []
    for result in results:
        if isinstance(result, dict):
            reasons.extend(str(reason) for reason in result.get("reasons", []) or [])
            reasons.extend(str(flag) for flag in result.get("risk_flags", []) or [])
    return sorted(set(reasons))


def build_risk_summary(
    *,
    manipulation_result: dict[str, Any] | None = None,
    revocation_result: dict[str, Any] | None = None,
    policy_result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a deterministic advisory risk summary.

    Defaults to LOW when no risk signals are present. Critical manipulation,
    revocation invalidation, or policy deny conditions map to CRITICAL for
    review routing without asserting final truth.
    """

    manipulation_risk = _as_upper((manipulation_result or {}).get("risk"))
    revocation_decision = _as_upper((revocation_result or {}).get("decision"))
    policy_decision = _as_upper((policy_result or {}).get("decision"))

    if manipulation_risk == "CRITICAL" or revocation_decision == "INVALID" or policy_decision == "DENY":
        risk_level = RiskLevel.CRITICAL
    elif manipulation_risk == "HIGH":
        risk_level = RiskLevel.HIGH
    elif manipulation_risk == "MEDIUM" or policy_decision == "REVIEW_REQUIRED":
        risk_level = RiskLevel.MEDIUM
    else:
        risk_level = RiskLevel.LOW

    return {
        "risk_level": risk_level,
        "reasons": _collect_reasons(manipulation_result, revocation_result, policy_result),
        "advisory_only": True,
        "human_supervised_validation_required": True,
    }


__all__ = ["RiskLevel", "build_risk_summary"]
