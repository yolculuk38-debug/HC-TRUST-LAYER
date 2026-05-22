"""HC:// mobile verification flow."""

from __future__ import annotations

from typing import Any


MOBILE_VERIFICATION_VERSION = "HC-MOBILE-VERIFICATION-V1"


class MobileTrustState:
    VERIFIED = "VERIFIED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    UNTRUSTED = "UNTRUSTED"
    INVALID = "INVALID"


def build_mobile_verification_view(
    *,
    qr_payload: dict[str, Any],
    validation_result: dict[str, Any],
) -> dict[str, Any]:
    """Build mobile-friendly QR verification response."""

    decision = validation_result.get("decision") or validation_result.get("status") or "UNTRUSTED"
    trusted = bool(validation_result.get("trusted", False) or validation_result.get("verified", False))
    reasons = list(validation_result.get("reasons", []) or [])

    if decision == "VERIFIED" and trusted:
        state = MobileTrustState.VERIFIED
        action = "SHOW_TRUST_PASSPORT"
    elif decision in {"REVIEW_REQUIRED", "PARTIAL"}:
        state = MobileTrustState.REVIEW_REQUIRED
        action = "SHOW_REVIEW_WARNING"
    elif decision == "INVALID":
        state = MobileTrustState.INVALID
        action = "BLOCK_TRUST_DISPLAY"
    else:
        state = MobileTrustState.UNTRUSTED
        action = "SHOW_UNTRUSTED_WARNING"

    return {
        "mobile_verification_version": MOBILE_VERIFICATION_VERSION,
        "record_id": qr_payload.get("record_id"),
        "source": "QR",
        "trust_state": state,
        "trusted": state == MobileTrustState.VERIFIED,
        "recommended_action": action,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "MOBILE_VERIFICATION_VERSION",
    "MobileTrustState",
    "build_mobile_verification_view",
]
