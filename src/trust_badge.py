"""HC trust badge standard."""

from __future__ import annotations

from typing import Any


TRUST_BADGE_VERSION = "HC-TRUST-BADGE-V1"


class TrustBadgeState:
    VERIFIED = "VERIFIED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    UNTRUSTED = "UNTRUSTED"
    INVALID = "INVALID"


def build_trust_badge(
    *,
    record_id: str,
    decision: str,
    trusted: bool,
    verification_url: str | None = None,
    trust_score: int | None = None,
) -> dict[str, Any]:
    """Build portable trust badge metadata."""

    if decision in {"VERIFIED", "ALLOW"} and trusted:
        state = TrustBadgeState.VERIFIED
        label = "HC Verified"
    elif decision in {"REVIEW_REQUIRED", "PARTIAL", "REVIEW"}:
        state = TrustBadgeState.REVIEW_REQUIRED
        label = "HC Review Required"
    elif decision in {"INVALID", "DENY", "REVOKED"}:
        state = TrustBadgeState.INVALID
        label = "HC Invalid"
    else:
        state = TrustBadgeState.UNTRUSTED
        label = "HC Untrusted"

    return {
        "trust_badge_version": TRUST_BADGE_VERSION,
        "record_id": record_id,
        "badge_state": state,
        "label": label,
        "trusted": state == TrustBadgeState.VERIFIED,
        "verification_url": verification_url,
        "trust_score": trust_score,
        "embed_safe": True,
    }


__all__ = [
    "TRUST_BADGE_VERSION",
    "TrustBadgeState",
    "build_trust_badge",
]
