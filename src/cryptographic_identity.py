"""HC:// cryptographic witness identity core."""

from __future__ import annotations

import hashlib
from typing import Any

CRYPTOGRAPHIC_IDENTITY_VERSION = "HC-CRYPTOGRAPHIC-IDENTITY-V1"



def generate_identity_fingerprint(
    *,
    witness_id: str,
    public_key: str,
) -> str:
    payload = f"{witness_id.strip()}::{public_key.strip()}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()



def create_cryptographic_identity(
    *,
    witness_id: str,
    public_key: str,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    fingerprint = generate_identity_fingerprint(
        witness_id=witness_id,
        public_key=public_key,
    )

    return {
        "cryptographic_identity_version": CRYPTOGRAPHIC_IDENTITY_VERSION,
        "witness_id": witness_id.strip(),
        "public_key": public_key.strip(),
        "identity_fingerprint": fingerprint,
        "metadata": metadata or {},
    }



def verify_identity_fingerprint(identity: dict[str, Any]) -> bool:
    expected = generate_identity_fingerprint(
        witness_id=identity["witness_id"],
        public_key=identity["public_key"],
    )

    if expected != identity.get("identity_fingerprint"):
        raise ValueError("identity fingerprint mismatch")

    return True
