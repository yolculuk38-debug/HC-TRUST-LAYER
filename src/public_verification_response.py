"""HC:// public verification response core."""

from __future__ import annotations

from typing import Any


PUBLIC_RESPONSE_VERSION = "HC-PUBLIC-VERIFY-RESPONSE-V1"


class PublicVerificationStatus:
    VERIFIED = "VERIFIED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    UNTRUSTED = "UNTRUSTED"
    INVALID = "INVALID"


def build_public_verification_response(
    trust_passport: dict[str, Any],
    *,
    include_private_details: bool = False,
) -> dict[str, Any]:
    """Create a stable public response from a trust passport."""

    if not isinstance(trust_passport, dict):
        return {
            "public_response_version": PUBLIC_RESPONSE_VERSION,
            "status": PublicVerificationStatus.INVALID,
            "trusted": False,
            "reason": "invalid trust passport",
        }

    status = trust_passport.get("status", PublicVerificationStatus.UNTRUSTED)
    trusted = bool(trust_passport.get("trusted", False))
    risk_flags = list(trust_passport.get("risk_flags", []) or [])
    trust_score = int(trust_passport.get("trust_score", 0) or 0)

    if status == "VERIFIED" and trusted:
        public_status = PublicVerificationStatus.VERIFIED
    elif status in {"REVIEW_REQUIRED", "PARTIAL"} or risk_flags:
        public_status = PublicVerificationStatus.REVIEW_REQUIRED
    elif status == "INVALID":
        public_status = PublicVerificationStatus.INVALID
    else:
        public_status = PublicVerificationStatus.UNTRUSTED

    response = {
        "public_response_version": PUBLIC_RESPONSE_VERSION,
        "record_id": trust_passport.get("record_id"),
        "status": public_status,
        "trusted": public_status == PublicVerificationStatus.VERIFIED,
        "trust_score": trust_score,
        "verification_level": trust_passport.get("verification_level"),
        "summary": trust_passport.get("summary", {}),
        "risk_flags": sorted(set(risk_flags)),
        "message": _public_message(public_status),
    }

    if include_private_details:
        response["details"] = trust_passport

    return response


def _public_message(status: str) -> str:
    if status == PublicVerificationStatus.VERIFIED:
        return "Record verification passed with strong evidence."
    if status == PublicVerificationStatus.REVIEW_REQUIRED:
        return "Record has verification evidence but requires additional review."
    if status == PublicVerificationStatus.INVALID:
        return "Record verification is invalid."
    return "Record is not trusted by the current verification evidence."


__all__ = [
    "PUBLIC_RESPONSE_VERSION",
    "PublicVerificationStatus",
    "build_public_verification_response",
]
