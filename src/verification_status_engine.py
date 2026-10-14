"""HC:// verification status engine.

Inspects legacy declarations for review without authenticating their contents.
Verification enums remain available for compatibility; declarations cannot reach
verified states or levels through this entry point.
"""

from __future__ import annotations

from copy import deepcopy
from enum import Enum
from typing import Any


STATUS_ENGINE_VERSION = "HC-VERIFICATION-STATUS-ENGINE-V1"


class VerificationLevel(str, Enum):
    LEVEL_0_UNVERIFIED = "LEVEL_0_UNVERIFIED"
    LEVEL_1_HASH_VERIFIED = "LEVEL_1_HASH_VERIFIED"
    LEVEL_2_WITNESS_REVIEWED = "LEVEL_2_WITNESS_REVIEWED"
    LEVEL_3_MULTI_WITNESS_VERIFIED = "LEVEL_3_MULTI_WITNESS_VERIFIED"
    LEVEL_4_PROVENANCE_LOCKED = "LEVEL_4_PROVENANCE_LOCKED"
    LEVEL_5_FEDERATED_VERIFIED = "LEVEL_5_FEDERATED_VERIFIED"


class VerificationState(str, Enum):
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    UNTRUSTED = "UNTRUSTED"
    INVALID = "INVALID"


def determine_verification_status(signals: dict[str, Any]) -> dict[str, Any]:
    """Contain legacy declarations without performing or implying proof checks."""
    reasons = ["source_declarations_not_verified"]
    risk_flags: list[str] = []
    valid = isinstance(signals, dict)
    if not valid:
        reasons.append("signals must be an object")
    else:
        for key in ("invalid", "hash_verified", "provenance_locked", "federated_verified"):
            if key in signals and not isinstance(signals[key], bool):
                valid = False
                reasons.append(f"invalid {key} declaration")
        for key in ("witness_count", "trust_score"):
            value = signals.get(key, 0)
            if type(value) is not int or value < 0 or (key == "trust_score" and value > 100):
                valid = False
                reasons.append(f"invalid {key} declaration")
        flags = signals.get("risk_flags", [])
        if not isinstance(flags, list) or any(not isinstance(flag, str) for flag in flags):
            valid = False
            reasons.append("risk_flags must be a list of strings")
        else:
            risk_flags = sorted(set(flags))
        if signals.get("invalid") is True:
            valid = False
            reasons.append("invalid signal present")

    return {
        "engine_version": STATUS_ENGINE_VERSION,
        "state": VerificationState.REVIEW_REQUIRED.value if valid else VerificationState.INVALID.value,
        "level": VerificationLevel.LEVEL_0_UNVERIFIED.value,
        "trusted": False,
        "verified": False,
        "trust_score": 0,
        "witness_count": 0,
        "source_claims": deepcopy(signals),
        "source_claims_verified": False,
        "content_hash_checked": False,
        "content_hash_valid": None,
        "signatures_verified": False,
        "identity_verified": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
        "risk_flags": risk_flags,
        "reasons": reasons,
    }


__all__ = [
    "STATUS_ENGINE_VERSION",
    "VerificationLevel",
    "VerificationState",
    "determine_verification_status",
]
