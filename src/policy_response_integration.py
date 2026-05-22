"""HC:// policy and response integration."""

from __future__ import annotations

from typing import Any


POLICY_RESPONSE_VERSION = "HC-POLICY-RESPONSE-V1"


def build_policy_aware_response(
    verification_response: dict[str, Any],
    policy_result: dict[str, Any],
) -> dict[str, Any]:
    """Attach policy decision to a verification response."""

    policy_decision = policy_result.get("decision", "REVIEW_REQUIRED")
    policy_reasons = list(policy_result.get("reasons", []) or [])

    response = dict(verification_response or {})
    response["policy_response_version"] = POLICY_RESPONSE_VERSION
    response["policy_decision"] = policy_decision
    response["policy_reasons"] = sorted(set(policy_reasons))
    response["policy_allowed"] = policy_decision == "ALLOW"

    if policy_decision == "DENY":
        response["status"] = "INVALID"
        response["trusted"] = False
    elif policy_decision == "REVIEW_REQUIRED":
        response["status"] = "REVIEW_REQUIRED"
        response["trusted"] = False

    return response


__all__ = [
    "POLICY_RESPONSE_VERSION",
    "build_policy_aware_response",
]
