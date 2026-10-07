"""HC:// offline verification flow."""

from __future__ import annotations

from typing import Any

from exported_proof import build_exported_proof
from public_validator import validate_public_proof


OFFLINE_VERIFIER_VERSION = "HC-OFFLINE-VERIFIER-V1"


def verify_offline_proof_package(
    proof_package: dict[str, Any],
) -> dict[str, Any]:
    """Inspect declarations offline; no cryptographic proof is verified."""

    validation = validate_public_proof(proof_package)

    return {
        "offline_verifier_version": OFFLINE_VERIFIER_VERSION,
        "offline_capable": True,
        "network_required": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
        "validation": validation,
    }


def create_demo_offline_package(record_id: str) -> dict[str, Any]:
    """Create explicitly unverified demonstration declarations."""

    return build_exported_proof(
        record_id=record_id,
        content_hash="offline-demo-hash",
        verification_level="UNVERIFIED_DEMO",
        trust_passport={"status": "UNVERIFIED_DEMO"},
        witnesses=[
            {
                "witness_signature": "offline-sig-1",
                "provenance_reference": "offline-prov-1",
            },
            {
                "witness_signature": "offline-sig-2",
                "provenance_reference": "offline-prov-2",
            },
        ],
        revision_chain={"broken": False},
    )


__all__ = [
    "OFFLINE_VERIFIER_VERSION",
    "verify_offline_proof_package",
    "create_demo_offline_package",
]
