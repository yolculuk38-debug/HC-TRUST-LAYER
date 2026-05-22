"""HC:// federation node identity core."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any


FEDERATION_NODE_IDENTITY_VERSION = "HC-FEDERATION-NODE-IDENTITY-V1"

ALLOWED_NODE_TYPES = {
    "PUBLIC_VALIDATOR",
    "INSTITUTIONAL_VALIDATOR",
    "COMMUNITY_VALIDATOR",
    "ARCHIVE_NODE",
    "OBSERVER_NODE",
}

ALLOWED_TRUST_STATES = {
    "TRUSTED",
    "LIMITED",
    "PENDING_REVIEW",
    "SUSPENDED",
    "REVOKED",
}


def _utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _non_empty(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


def create_node_identity(
    *,
    node_id: str,
    node_name: str,
    node_type: str,
    operator_id: str,
    public_key_fingerprint: str,
    trust_state: str = "PENDING_REVIEW",
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create normalized federation node identity."""

    normalized_type = node_type.strip().upper()
    normalized_state = trust_state.strip().upper()

    if normalized_type not in ALLOWED_NODE_TYPES:
        raise ValueError(f"node_type must be one of: {sorted(ALLOWED_NODE_TYPES)}")

    if normalized_state not in ALLOWED_TRUST_STATES:
        raise ValueError(f"trust_state must be one of: {sorted(ALLOWED_TRUST_STATES)}")

    return {
        "federation_node_identity_version": FEDERATION_NODE_IDENTITY_VERSION,
        "node_id": _non_empty(node_id, "node_id"),
        "node_name": _non_empty(node_name, "node_name"),
        "node_type": normalized_type,
        "operator_id": _non_empty(operator_id, "operator_id"),
        "public_key_fingerprint": _non_empty(
            public_key_fingerprint,
            "public_key_fingerprint",
        ),
        "trust_state": normalized_state,
        "created_at": _utc_now(),
        "metadata": metadata or {},
    }


def validate_node_identity(identity: dict[str, Any]) -> bool:
    """Validate federation node identity structure."""

    required_fields = {
        "federation_node_identity_version",
        "node_id",
        "node_name",
        "node_type",
        "operator_id",
        "public_key_fingerprint",
        "trust_state",
        "created_at",
    }
    missing = required_fields.difference(identity.keys())
    if missing:
        raise ValueError(f"missing node identity fields: {sorted(missing)}")

    if identity["node_type"] not in ALLOWED_NODE_TYPES:
        raise ValueError("invalid node_type")

    if identity["trust_state"] not in ALLOWED_TRUST_STATES:
        raise ValueError("invalid trust_state")

    return True


def is_node_allowed_to_validate(identity: dict[str, Any]) -> bool:
    """Return whether a node may participate in validation."""

    validate_node_identity(identity)
    return identity.get("trust_state") in {"TRUSTED", "LIMITED"}


__all__ = [
    "ALLOWED_NODE_TYPES",
    "ALLOWED_TRUST_STATES",
    "FEDERATION_NODE_IDENTITY_VERSION",
    "create_node_identity",
    "is_node_allowed_to_validate",
    "validate_node_identity",
]
