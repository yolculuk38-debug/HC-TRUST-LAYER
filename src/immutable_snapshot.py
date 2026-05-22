"""HC:// immutable snapshot chain core."""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from typing import Any


IMMUTABLE_SNAPSHOT_VERSION = "HC-IMMUTABLE-SNAPSHOT-V1"
GENESIS_PREVIOUS_HASH = "0" * 64


def _utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_json(data: dict[str, Any]) -> str:
    """Return stable JSON for deterministic hashing."""

    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def calculate_snapshot_hash(payload: dict[str, Any]) -> str:
    """Calculate SHA-256 hash for a snapshot payload."""

    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def create_snapshot(
    *,
    record_id: str,
    record_hash: str,
    previous_snapshot_hash: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create an immutable-style snapshot entry."""

    previous_hash = previous_snapshot_hash or GENESIS_PREVIOUS_HASH
    payload = {
        "immutable_snapshot_version": IMMUTABLE_SNAPSHOT_VERSION,
        "record_id": record_id.strip(),
        "record_hash": record_hash.strip(),
        "previous_snapshot_hash": previous_hash.strip(),
        "created_at": _utc_now(),
        "metadata": metadata or {},
    }
    payload["snapshot_hash"] = calculate_snapshot_hash(payload)
    return payload


def verify_snapshot(snapshot: dict[str, Any]) -> bool:
    """Verify snapshot integrity by recalculating its hash."""

    if "snapshot_hash" not in snapshot:
        raise ValueError("missing snapshot_hash")

    expected = snapshot["snapshot_hash"]
    payload = dict(snapshot)
    payload.pop("snapshot_hash")
    actual = calculate_snapshot_hash(payload)

    if actual != expected:
        raise ValueError("snapshot hash mismatch")

    return True


def verify_snapshot_link(
    *,
    previous_snapshot: dict[str, Any],
    current_snapshot: dict[str, Any],
) -> bool:
    """Verify that current snapshot links to previous snapshot."""

    verify_snapshot(previous_snapshot)
    verify_snapshot(current_snapshot)

    if current_snapshot.get("previous_snapshot_hash") != previous_snapshot.get("snapshot_hash"):
        raise ValueError("snapshot chain link mismatch")

    return True


__all__ = [
    "GENESIS_PREVIOUS_HASH",
    "IMMUTABLE_SNAPSHOT_VERSION",
    "calculate_snapshot_hash",
    "canonical_json",
    "create_snapshot",
    "verify_snapshot",
    "verify_snapshot_link",
]
