"""HC:// cross-platform verification bridge."""

from __future__ import annotations

from typing import Any


CROSS_PLATFORM_BRIDGE_VERSION = "HC-CROSS-PLATFORM-BRIDGE-V1"


class PlatformSource:
    WEB = "WEB"
    MOBILE = "MOBILE"
    API = "API"
    BROWSER_EXTENSION = "BROWSER_EXTENSION"
    ENTERPRISE = "ENTERPRISE"
    UNKNOWN = "UNKNOWN"



def normalize_platform_payload(
    payload: dict[str, Any],
    *,
    platform: str = PlatformSource.UNKNOWN,
) -> dict[str, Any]:
    """Normalize external platform verification payloads."""

    if not isinstance(payload, dict):
        return {
            "cross_platform_bridge_version": CROSS_PLATFORM_BRIDGE_VERSION,
            "valid": False,
            "platform": platform,
            "reasons": ["invalid_platform_payload"],
        }

    record_id = payload.get("record_id") or payload.get("id")
    content_hash = payload.get("content_hash") or payload.get("hash")

    reasons: list[str] = []

    if not record_id:
        reasons.append("missing_record_id")

    if not content_hash:
        reasons.append("missing_content_hash")

    return {
        "cross_platform_bridge_version": CROSS_PLATFORM_BRIDGE_VERSION,
        "valid": not reasons,
        "platform": platform,
        "record_id": record_id,
        "content_hash": content_hash,
        "metadata": payload.get("metadata", {}),
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "CROSS_PLATFORM_BRIDGE_VERSION",
    "PlatformSource",
    "normalize_platform_payload",
]
