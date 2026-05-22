"""HC:// network trust proof core."""

from __future__ import annotations

NETWORK_TRUST_PROOF_VERSION = "HC-NETWORK-TRUST-PROOF-V1"


def create_network_trust_proof(
    *,
    source_registry: str,
    target_registry: str,
    record_id: str,
    proof_hash: str,
) -> dict:
    """Create a portable trust proof between two registries."""

    return {
        "network_trust_proof_version": NETWORK_TRUST_PROOF_VERSION,
        "source_registry": source_registry.strip(),
        "target_registry": target_registry.strip(),
        "record_id": record_id.strip(),
        "proof_hash": proof_hash.strip(),
    }


def validate_network_trust_proof(proof: dict) -> bool:
    """Validate portable network trust proof shape."""

    required = {
        "network_trust_proof_version",
        "source_registry",
        "target_registry",
        "record_id",
        "proof_hash",
    }
    missing = required.difference(proof.keys())
    if missing:
        raise ValueError(f"missing network trust proof fields: {sorted(missing)}")

    return True
