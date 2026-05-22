"""HC:// witness signature validation layer."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any


WITNESS_SIGNATURE_VERSION = "HC-WITNESS-SIGNATURE-V1"

ALLOWED_WITNESS_TYPES = {
    "AI_WITNESS",
    "HUMAN_WITNESS",
    "COMMIT_WITNESS",
    "TIMESTAMP_WITNESS",
}

ALLOWED_VERIFICATION_METHODS = {
    "HASH_VERIFIED",
    "MANUAL_REVIEW",
    "MULTI_SOURCE_MATCH",
    "COMMIT_AUDIT",
}



def _utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")



def _validate_non_empty(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized



def create_witness_signature(
    *,
    witness_id: str,
    witness_type: str,
    verification_method: str,
    record_id: str,
    signature_hash: str,
) -> dict[str, Any]:
    """Create a normalized witness signature entry."""

    normalized_type = witness_type.strip().upper()
    normalized_method = verification_method.strip().upper()

    if normalized_type not in ALLOWED_WITNESS_TYPES:
        raise ValueError(
            f"witness_type must be one of: {sorted(ALLOWED_WITNESS_TYPES)}"
        )

    if normalized_method not in ALLOWED_VERIFICATION_METHODS:
        raise ValueError(
            "verification_method must be one of: "
            f"{sorted(ALLOWED_VERIFICATION_METHODS)}"
        )

    return {
        "witness_signature_version": WITNESS_SIGNATURE_VERSION,
        "witness_id": _validate_non_empty(witness_id, "witness_id"),
        "witness_type": normalized_type,
        "verification_method": normalized_method,
        "record_id": _validate_non_empty(record_id, "record_id"),
        "signature_hash": _validate_non_empty(signature_hash, "signature_hash"),
        "signed_at": _utc_now(),
    }



def validate_witness_signature(signature: dict[str, Any]) -> bool:
    """Validate witness signature structure."""

    required_fields = {
        "witness_signature_version",
        "witness_id",
        "witness_type",
        "verification_method",
        "record_id",
        "signature_hash",
        "signed_at",
    }

    missing = required_fields.difference(signature.keys())

    if missing:
        raise ValueError(f"missing witness signature fields: {sorted(missing)}")

    if signature["witness_type"] not in ALLOWED_WITNESS_TYPES:
        raise ValueError("invalid witness_type")

    if signature["verification_method"] not in ALLOWED_VERIFICATION_METHODS:
        raise ValueError("invalid verification_method")

    return True


__all__ = [
    "ALLOWED_VERIFICATION_METHODS",
    "ALLOWED_WITNESS_TYPES",
    "WITNESS_SIGNATURE_VERSION",
    "create_witness_signature",
    "validate_witness_signature",
]
