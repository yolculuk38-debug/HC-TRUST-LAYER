"""Legacy HC:// declaration inspector; no cryptographic verification is performed."""

from __future__ import annotations

from typing import Any


VALIDATOR_VERSION = "HC-PUBLIC-VALIDATOR-V1"


class PublicValidatorDecision:
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    INVALID = "INVALID"
    UNTRUSTED = "UNTRUSTED"


def validate_public_proof(proof: dict[str, Any]) -> dict[str, Any]:
    """Inspect basic shapes/conflicts without trusting supplied success flags."""

    reasons: list[str] = []
    risk_flags: list[str] = [
        "content_hash_not_verified", "witness_signatures_not_verified",
        "provenance_not_verified", "trust_passport_not_verified",
        "revision_integrity_not_verified",
    ]

    if not isinstance(proof, dict):
        return _response(PublicValidatorDecision.INVALID, ["invalid proof structure"])

    required_fields = [
        "record_id",
        "content_hash",
        "trust_passport",
    ]

    for field in required_fields:
        if field not in proof or proof[field] is None:
            reasons.append(f"missing_{field}")

    for field in ("record_id", "content_hash"):
        value = proof.get(field)
        if not isinstance(value, str) or not value.strip():
            reasons.append(f"invalid_{field}")
    if not isinstance(proof.get("trust_passport"), dict):
        reasons.append("invalid_trust_passport_structure")
    verification_level = proof.get("verification_level")
    if verification_level is not None and not isinstance(verification_level, str):
        reasons.append("invalid_verification_level")

    revision_chain = proof.get("revision_chain", {})
    if not isinstance(revision_chain, dict):
        reasons.append("invalid_revision_chain_structure")
    elif revision_chain.get("broken"):
        reasons.append("broken_revision_chain")

    if proof.get("content_hash_valid") is False:
        reasons.append("invalid_content_hash")

    witnesses = proof.get("witnesses", [])
    if not isinstance(witnesses, list):
        reasons.append("invalid_witnesses_structure")
        witnesses = []

    conflicting_witnesses = 0

    for witness in witnesses:
        if not isinstance(witness, dict):
            reasons.append("invalid_witness_structure")
            continue

        if witness.get("conflict"):
            conflicting_witnesses += 1

        signature = witness.get("witness_signature")
        if not isinstance(signature, str) or not signature.strip():
            risk_flags.append("missing_witness_signature")
            continue

        reference = witness.get("provenance_reference")
        if not isinstance(reference, str) or not reference.strip():
            risk_flags.append("missing_provenance_reference")
            continue

    if conflicting_witnesses:
        reasons.append("conflicting_witnesses")

    if reasons:
        decision = PublicValidatorDecision.INVALID
    else:
        decision = PublicValidatorDecision.REVIEW_REQUIRED

    return _response(
        decision,
        reasons,
        risk_flags=risk_flags,
        verification_level=verification_level,
        record_id=proof.get("record_id"),
    )


def _response(
    decision: str,
    reasons: list[str],
    *,
    risk_flags: list[str] | None = None,
    verification_level: str | None = None,
    record_id: str | None = None,
) -> dict[str, Any]:
    return {
        "validator_version": VALIDATOR_VERSION,
        "record_id": record_id,
        "decision": decision,
        "verified": False,
        "verification_level": None,
        "source_claims": {"verification_level": verification_level},
        "source_claims_verified": False,
        "content_hash_checked": False,
        "content_hash_valid": False,
        "signature_verified": False,
        "witnesses_verified": False,
        "identity_verified": False,
        "trusted": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
        "reasons": sorted(set(reasons)),
        "risk_flags": sorted(set(risk_flags or [])),
    }


__all__ = [
    "VALIDATOR_VERSION",
    "PublicValidatorDecision",
    "validate_public_proof",
]
