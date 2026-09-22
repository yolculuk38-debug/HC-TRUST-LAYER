"""Portable HC:// declarations; building a package does not verify evidence."""

from __future__ import annotations

from typing import Any


EXPORTED_PROOF_VERSION = "HC-EXPORTED-PROOF-V1"


def build_exported_proof(
    *,
    record_id: str,
    content_hash: str,
    verification_level: str,
    trust_passport: dict[str, Any],
    witnesses: list[dict[str, Any]] | None = None,
    revision_chain: dict[str, Any] | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Preserve unverified source declarations, without hashing or signing."""

    return {
        "proof_version": EXPORTED_PROOF_VERSION,
        "record_id": record_id,
        "content_hash": content_hash,
        "content_hash_valid": None,
        "content_hash_checked": False,
        "verification_level": None,
        "trust_passport": {},
        "source_claims": {
            "verification_level": verification_level,
            "trust_passport": trust_passport,
        },
        "source_claims_verified": False,
        "verified": False,
        "signature_verified": False,
        "witnesses_verified": False,
        "trusted": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
        "witnesses": witnesses or [],
        "revision_chain": revision_chain or {},
        "metadata": metadata or {},
    }


__all__ = [
    "EXPORTED_PROOF_VERSION",
    "build_exported_proof",
]
