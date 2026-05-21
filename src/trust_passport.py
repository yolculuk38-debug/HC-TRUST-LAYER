"""HC:// trust passport core.

Builds a compact, user-facing verification summary for QR, web,
mobile, and institutional verification views.
"""

from __future__ import annotations

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
    """Build a single compact trust passport response."""

    if not record_id or not isinstance(verification_response, dict):
        return {
            "passport_version": TRUST_PASSPORT_VERSION,
            "record_id": record_id,
            "status": TrustPassportStatus.INVALID,
            "trusted": False,
            "reason": "invalid record_id or verification response",
        }

    decision = verification_response.get("decision", "UNTRUSTED")
    signals = verification_response.get("signals", {}) if isinstance(verification_response.get("signals", {}), dict) else {}
    trust_score = int(signals.get("trust_score", 0))
    trusted = bool(verification_response.get("trusted", False))

    risk_flags: list[str] = []
    for summary in [evidence_summary, federation_summary, provenance_summary, audit_summary]:
        if isinstance(summary, dict):
            risk_flags.extend(summary.get("risk_flags", []))
            risk_flags.extend(summary.get("review_flags", []))

    if decision == "VERIFIED" and trusted and not risk_flags:
        status = TrustPassportStatus.VERIFIED
    elif decision in {"VERIFIED", "PARTIAL"} and trust_score >= 60:
        status = TrustPassportStatus.PARTIAL if not risk_flags else TrustPassportStatus.REVIEW_REQUIRED
    elif risk_flags:
        status = TrustPassportStatus.REVIEW_REQUIRED
    else:
        status = TrustPassportStatus.UNTRUSTED

    return {
        "passport_version": TRUST_PASSPORT_VERSION,
        "record_id": record_id,
        "status": status,
        "trusted": trusted and status == TrustPassportStatus.VERIFIED,
        "trust_score": trust_score,
        "decision": decision,
        "risk_flags": sorted(set(risk_flags)),
        "summary": {
            "hash": bool(signals.get("hash", False)),
            "qr": bool(signals.get("qr", False)),
            "consensus": bool(signals.get("consensus", False)),
            "audit": bool(signals.get("audit", False)),
            "signature": bool(signals.get("signature", False)),
            "federation": bool(federation_summary and federation_summary.get("verified", False)),
            "provenance": bool(provenance_summary and provenance_summary.get("verified", False)),
            "evidence": bool(evidence_summary and evidence_summary.get("verified", False)),
        },
        "evidence_summary": evidence_summary or {},
        "federation_summary": federation_summary or {},
        "provenance_summary": provenance_summary or {},
        "audit_summary": audit_summary or {},
    }


__all__ = ["TRUST_PASSPORT_VERSION", "TrustPassportStatus", "build_trust_passport"]
