"""HC:// revocation registry core."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any


REVOCATION_REGISTRY_VERSION = "HC-REVOCATION-REGISTRY-V1"

REVOCABLE_ENTITY_TYPES = {
    "RECORD",
    "WITNESS_SIGNATURE",
    "FEDERATION_NODE",
    "QR_PAYLOAD",
    "EXPORT_PACKAGE",
}

REVOCATION_REASONS = {
    "COMPROMISED_KEY",
    "INVALID_SIGNATURE",
    "MALICIOUS_ACTIVITY",
    "POLICY_VIOLATION",
    "DUPLICATE_OR_SUPERSEDED",
    "MANUAL_SECURITY_REVIEW",
}


def _utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _required(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


def create_revocation_entry(
    *,
    entity_id: str,
    entity_type: str,
    reason: str,
    revoked_by: str,
    evidence_hash: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create normalized revocation registry entry."""

    normalized_type = entity_type.strip().upper()
    normalized_reason = reason.strip().upper()

    if normalized_type not in REVOCABLE_ENTITY_TYPES:
        raise ValueError(f"entity_type must be one of: {sorted(REVOCABLE_ENTITY_TYPES)}")

    if normalized_reason not in REVOCATION_REASONS:
        raise ValueError(f"reason must be one of: {sorted(REVOCATION_REASONS)}")

    return {
        "revocation_registry_version": REVOCATION_REGISTRY_VERSION,
        "entity_id": _required(entity_id, "entity_id"),
        "entity_type": normalized_type,
        "reason": normalized_reason,
        "revoked_by": _required(revoked_by, "revoked_by"),
        "evidence_hash": evidence_hash or "",
        "revoked_at": _utc_now(),
        "metadata": metadata or {},
    }


def is_entity_revoked(entity_id: str, registry: list[dict[str, Any]]) -> bool:
    """Return True when an entity exists in the revocation registry."""

    target = entity_id.strip()
    return any(entry.get("entity_id") == target for entry in registry)


def require_not_revoked(entity_id: str, registry: list[dict[str, Any]]) -> bool:
    """Raise if entity has been revoked."""

    if is_entity_revoked(entity_id, registry):
        raise ValueError("entity is revoked")

    return True


__all__ = [
    "REVOCABLE_ENTITY_TYPES",
    "REVOCATION_REASONS",
    "REVOCATION_REGISTRY_VERSION",
    "create_revocation_entry",
    "is_entity_revoked",
    "require_not_revoked",
]
