"""Build portable advisory summaries of unverified SDK declarations."""

from __future__ import annotations

from typing import Any


CERTIFICATE_VERSION = "HC-CERTIFICATE-V1"


def build_verification_certificate(
    sdk_response: dict[str, Any], *, issuer: str = "HC://",
) -> dict[str, Any]:
    """Preserve source claims without issuing an authenticated certificate.

    ``issuer`` is a caller declaration. SDK decision/level/verified values are
    retained only under ``source_claims`` and are not independently verified.
    Invalid SDK objects or risk/reason arrays are rejected explicitly.
    """
    if not isinstance(sdk_response, dict):
        raise ValueError("sdk_response must be an object")
    if not isinstance(issuer, str) or not issuer.strip():
        raise ValueError("issuer must be a non-empty declaration")
    for name in ("risk_flags", "reasons"):
        values = sdk_response.get(name, [])
        if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
            raise ValueError(f"{name} must be a list of strings")

    return {
        "certificate_version": CERTIFICATE_VERSION,
        "issuer": issuer,
        "decision": "REVIEW_REQUIRED",
        "verified": False,
        "trusted": False,
        "signature_verified": False,
        "issuer_verified": False,
        "verification_level": None,
        "source_claims": {
            name: sdk_response.get(name)
            for name in ("decision", "verified", "verification_level")
        },
        "source_claims_verified": False,
        "risk_flags": list(sdk_response.get("risk_flags", [])),
        "reasons": sorted(set(sdk_response.get("reasons", []) + ["certificate_authentication_not_performed"])),
        "portable": True,
        "explainable": True,
        "human_readable": True,
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "human_review_required": True,
    }


__all__ = ["CERTIFICATE_VERSION", "build_verification_certificate"]
