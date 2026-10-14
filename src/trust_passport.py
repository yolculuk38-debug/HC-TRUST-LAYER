"""HC:// trust passport core.

Builds an advisory summary of unverified declarations. It performs no signature,
identity, provenance or content verification.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


TRUST_PASSPORT_VERSION = "HC-TRUST-PASSPORT-V1"


class TrustPassportStatus:
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    UNTRUSTED = "UNTRUSTED"
    INVALID = "INVALID"


def build_trust_passport(
    record_id: str,
    verification_response: dict[str, Any],
    *,
    evidence_summary: dict[str, Any] | None = None,
    federation_summary: dict[str, Any] | None = None,
    provenance_summary: dict[str, Any] | None = None,
    audit_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Summarize unverified source claims without granting trust authority."""
    claims = {
        "verification_response": deepcopy(verification_response),
        "evidence_summary": deepcopy(evidence_summary),
        "federation_summary": deepcopy(federation_summary),
        "provenance_summary": deepcopy(provenance_summary),
        "audit_summary": deepcopy(audit_summary),
    }
    valid = isinstance(record_id, str) and bool(record_id.strip()) and isinstance(verification_response, dict)
    risk_flags: list[str] = []
    if isinstance(verification_response, dict):
        signals = verification_response.get("signals", {})
        decision = verification_response.get("decision", "REVIEW_REQUIRED")
        if not isinstance(signals, dict) or not isinstance(decision, str) or decision == "INVALID":
            valid = False
        if "trusted" in verification_response and not isinstance(verification_response["trusted"], bool):
            valid = False
        if isinstance(signals, dict):
            score = signals.get("trust_score", 0)
            if type(score) is not int or not 0 <= score <= 100:
                valid = False
            for key in ("hash", "qr", "consensus", "audit", "signature"):
                if key in signals and not isinstance(signals[key], bool):
                    valid = False
    for summary in (evidence_summary, federation_summary, provenance_summary, audit_summary):
        if summary is None:
            continue
        if not isinstance(summary, dict):
            valid = False
            continue
        for key in ("risk_flags", "review_flags"):
            flags = summary.get(key, [])
            if not isinstance(flags, list) or any(not isinstance(flag, str) for flag in flags):
                valid = False
            else:
                risk_flags.extend(flags)

    status = TrustPassportStatus.REVIEW_REQUIRED if valid else TrustPassportStatus.INVALID
    return {
        "passport_version": TRUST_PASSPORT_VERSION,
        "record_id": record_id,
        "status": status,
        "decision": status,
        "trusted": False,
        "verified": False,
        "trust_score": 0,
        "risk_flags": sorted(set(risk_flags)),
        "summary": {key: False for key in (
            "hash", "qr", "consensus", "audit", "signature", "federation", "provenance", "evidence"
        )},
        "source_claims": claims,
        "source_claims_verified": False,
        "content_hash_checked": False,
        "content_hash_valid": None,
        "signatures_verified": False,
        "identity_verified": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
        "reason": "source_declarations_not_verified" if valid else "invalid_passport_input",
    }


__all__ = ["TRUST_PASSPORT_VERSION", "TrustPassportStatus", "build_trust_passport"]
