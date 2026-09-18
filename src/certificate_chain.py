"""Advisory certificate lineage declarations; no cryptographic chain verification."""

from __future__ import annotations

from typing import Any

from certificate_verifier import verify_certificate


CERTIFICATE_CHAIN_VERSION = "HC-CERTIFICATE-CHAIN-V1"


def build_certificate_chain_entry(
    certificate: dict[str, Any],
    *,
    previous_certificate_hash: str | None = None,
) -> dict[str, Any]:
    """Wrap a claimed predecessor reference without asserting link integrity.

    Retained caller data is not redacted and must not be published without a
    separate disclosure review; ``public_safe`` is therefore false.
    """
    return {
        "certificate_chain_version": CERTIFICATE_CHAIN_VERSION,
        "certificate": certificate,
        "previous_certificate_hash": previous_certificate_hash,
        "chain_integrity": None,
        "chain_verified": False,
        "trusted": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
    }


def verify_certificate_chain(chain_entry: object) -> dict[str, Any]:
    """Inspect entry shape; caller-supplied integrity flags grant no trust.

    A predecessor string is only a reference. No predecessor is loaded and no
    digest, signature, ordering or chain authority is verified here.
    """
    reasons: list[str] = []
    if not isinstance(chain_entry, dict):
        reasons.append("invalid_chain_entry")
    else:
        if chain_entry.get("certificate_chain_version") != CERTIFICATE_CHAIN_VERSION:
            reasons.append("unsupported_certificate_chain_version")
        if not verify_certificate(chain_entry.get("certificate"))["shape_valid"]:
            reasons.append("invalid_certificate_shape")
        previous = chain_entry.get("previous_certificate_hash")
        if previous is not None and (not isinstance(previous, str) or not previous.strip()):
            reasons.append("invalid_previous_certificate_reference")

    return {
        "certificate_chain_version": CERTIFICATE_CHAIN_VERSION,
        "shape_valid": not reasons,
        "chain_integrity": None,
        "chain_verified": False,
        "signature_verified": False,
        "issuer_verified": False,
        "trusted": False,
        "verified": False,
        "decision": "INVALID" if reasons else "REVIEW_REQUIRED",
        "reasons": sorted(set(reasons + ["certificate_chain_verification_not_performed"])),
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "human_review_required": True,
    }


__all__ = [
    "CERTIFICATE_CHAIN_VERSION", "build_certificate_chain_entry", "verify_certificate_chain",
]
