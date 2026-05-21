"""HC:// browser and mobile verifier entry foundation."""

from __future__ import annotations

from typing import Any

from offline_verifier import verify_offline_proof_package


VERIFIER_ENTRY_VERSION = "HC-VERIFIER-ENTRY-V1"


class VerificationPlatform:
    BROWSER = "BROWSER"
    MOBILE = "MOBILE"
    API = "API"
    SDK = "SDK"


def verify_from_entry_point(
    proof_package: dict[str, Any],
    *,
    platform: str = VerificationPlatform.BROWSER,
) -> dict[str, Any]:
    """Unified verifier entry point for browser/mobile/API integrations."""

    offline_result = verify_offline_proof_package(proof_package)

    return {
        "verifier_entry_version": VERIFIER_ENTRY_VERSION,
        "platform": platform,
        "portable": True,
        "verification": offline_result,
    }


__all__ = [
    "VERIFIER_ENTRY_VERSION",
    "VerificationPlatform",
    "verify_from_entry_point",
]
