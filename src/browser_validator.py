"""HC:// browser validator prototype."""

from __future__ import annotations

from typing import Any


BROWSER_VALIDATOR_VERSION = "HC-BROWSER-VALIDATOR-V1"


class BadgeState:
    VERIFIED = "VERIFIED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    UNTRUSTED = "UNTRUSTED"
    INVALID = "INVALID"


def build_browser_validation_view(
    validation_result: dict[str, Any],
) -> dict[str, Any]:
    """Build browser-extension friendly validation view."""

    decision = validation_result.get("decision") or validation_result.get("status") or "UNTRUSTED"
    trusted = bool(validation_result.get("trusted", False) or validation_result.get("verified", False))
    reasons = list(validation_result.get("reasons", []) or [])

    if decision == "VERIFIED" and trusted:
        badge = BadgeState.VERIFIED
        message = "HC:// verified with trusted evidence."
    elif decision in {"REVIEW_REQUIRED", "PARTIAL"}:
        badge = BadgeState.REVIEW_REQUIRED
        message = "HC:// review required before trust."
    elif decision == "INVALID":
        badge = BadgeState.INVALID
        message = "HC:// invalid or rejected verification."
    else:
        badge = BadgeState.UNTRUSTED
        message = "HC:// not trusted by current evidence."

    return {
        "browser_validator_version": BROWSER_VALIDATOR_VERSION,
        "badge_state": badge,
        "trusted": badge == BadgeState.VERIFIED,
        "message": message,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "BROWSER_VALIDATOR_VERSION",
    "BadgeState",
    "build_browser_validation_view",
]
