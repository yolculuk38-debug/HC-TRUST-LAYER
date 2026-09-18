"""Advisory inspection of certificate-shaped declarations, without issuer authentication."""

from __future__ import annotations

from typing import Any


CERTIFICATE_VERIFIER_VERSION = "HC-CERTIFICATE-VERIFIER-V1"


def verify_certificate(certificate: object) -> dict[str, Any]:
    """Inspect shape only; declared verification and signature fields grant no trust.

    The legacy function name is retained. No signature, issuer authority or key
    ownership check is implemented by this inspector. Retained risk-flag text
    is caller-controlled and not redacted, so this result is not public-safe.
    """
    reasons: list[str] = []
    risk_flags: list[str] = []

    if not isinstance(certificate, dict):
        return _result(["invalid_certificate_structure"])

    if certificate.get("certificate_version") != "HC-CERTIFICATE-V1":
        reasons.append("unsupported_certificate_version")
    issuer = certificate.get("issuer")
    if not isinstance(issuer, str) or not issuer.strip():
        reasons.append("missing_or_invalid_issuer")
    if not isinstance(certificate.get("decision"), str) or not certificate["decision"].strip():
        reasons.append("invalid_declared_decision")
    if type(certificate.get("verified")) is not bool:
        reasons.append("invalid_declared_verified_flag")

    declared_flags = certificate.get("risk_flags", [])
    if not isinstance(declared_flags, list) or any(
        not isinstance(flag, str) for flag in declared_flags
    ):
        reasons.append("invalid_risk_flags")
    else:
        risk_flags = declared_flags

    return _result(reasons, risk_flags=risk_flags)


def _result(
    shape_errors: list[str], *, risk_flags: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "certificate_verifier_version": CERTIFICATE_VERIFIER_VERSION,
        "shape_valid": not shape_errors,
        "trusted": False,
        "verified": False,
        "signature_verified": False,
        "issuer_verified": False,
        "decision": "REVIEW_REQUIRED",
        "reasons": sorted(set(shape_errors + ["certificate_authentication_not_performed"])),
        "risk_flags": sorted(set(risk_flags or [])),
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
    }


__all__ = ["CERTIFICATE_VERIFIER_VERSION", "verify_certificate"]
