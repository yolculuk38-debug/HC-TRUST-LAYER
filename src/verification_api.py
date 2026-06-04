"""Minimal HC:// verification response compatibility API.

This module preserves advisory-only verification response semantics for
checked-in compatibility tests. It does not assert truth finality,
production readiness, or autonomous governance outcomes.
"""

from __future__ import annotations

from enum import Enum
from typing import Any


class VerificationDecision(str, Enum):
    """Advisory HC:// verification decision labels."""

    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    UNTRUSTED = "UNTRUSTED"
    INVALID = "INVALID"


def _clamp_trust_score(value: Any) -> int:
    try:
        score = int(value)
    except (TypeError, ValueError):
        score = 0
    return max(0, min(100, score))


def _signal_bool(signals: dict[str, Any], key: str) -> bool:
    return signals.get(key) is True


def build_verification_response(
    record_id: str,
    signals: dict[str, Any] | None = None,
    *,
    checked_at: str | None = None,
) -> dict[str, Any]:
    """Build a deterministic advisory verification response.

    The response combines provided layer signals conservatively and keeps the
    human-supervised validation boundary explicit: a ``VERIFIED`` label here is
    an advisory compatibility result, not a claim of final truth.
    """

    if not record_id or not isinstance(signals, dict):
        normalized_signals = {
            "trust_score": 0,
            "advisory_only": True,
            "human_supervised_validation_required": True,
        }
        return {
            "record_id": record_id,
            "decision": VerificationDecision.INVALID,
            "trusted": False,
            "signals": normalized_signals,
            "checked_at": checked_at,
        }

    normalized_signals = dict(signals)
    trust_score = _clamp_trust_score(normalized_signals.get("trust_score", 0))
    normalized_signals["trust_score"] = trust_score
    normalized_signals["advisory_only"] = True
    normalized_signals["human_supervised_validation_required"] = True

    if signals.get("hash") is False:
        decision = VerificationDecision.UNTRUSTED
        trusted = False
    elif all(_signal_bool(signals, key) for key in ("hash", "qr", "consensus", "audit", "signature")) and trust_score >= 90:
        decision = VerificationDecision.VERIFIED
        trusted = True
    elif signals.get("hash") is True:
        decision = VerificationDecision.PARTIAL
        trusted = False
    else:
        decision = VerificationDecision.PARTIAL
        trusted = False

    return {
        "record_id": record_id,
        "decision": decision,
        "trusted": trusted,
        "signals": normalized_signals,
        "checked_at": checked_at,
    }


__all__ = ["VerificationDecision", "build_verification_response"]
