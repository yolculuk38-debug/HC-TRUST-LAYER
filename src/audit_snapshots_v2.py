"""HC:// immutable audit snapshots v2.

Snapshots create a deterministic, parent-linked audit chain.
They are immutable-style records: changes create new snapshots instead of rewriting history.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


SNAPSHOT_VERSION = "HC-AUDIT-SNAPSHOT-V2"
GENESIS_PARENT = "GENESIS"


def canonical_json(data: dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def snapshot_hash(snapshot: dict[str, Any]) -> str:
    """Calculate deterministic snapshot hash excluding snapshot_hash field."""

    unsigned = dict(snapshot)
    unsigned.pop("snapshot_hash", None)
    return hashlib.sha256(canonical_json(unsigned).encode("utf-8")).hexdigest()


def create_snapshot(
    snapshot_id: str,
    record_hashes: list[str],
    created_at: str,
    *,
    parent_snapshot_hash: str = GENESIS_PARENT,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Create deterministic immutable-style audit snapshot."""

    snapshot = {
        "snapshot_version": SNAPSHOT_VERSION,
        "snapshot_id": snapshot_id,
        "created_at": created_at,
        "parent_snapshot_hash": parent_snapshot_hash,
        "record_hashes": sorted(record_hashes),
        "metadata": metadata or {},
    }
    snapshot["snapshot_hash"] = snapshot_hash(snapshot)
    return snapshot


def verify_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(snapshot, dict):
        return {"verified": False, "reason": "snapshot must be an object"}

    required = [
        "snapshot_version",
        "snapshot_id",
        "created_at",
        "parent_snapshot_hash",
        "record_hashes",
        "snapshot_hash",
    ]
    missing = [field for field in required if field not in snapshot]
    if missing:
        return {"verified": False, "reason": f"missing required field(s): {', '.join(missing)}"}

    if snapshot["snapshot_version"] != SNAPSHOT_VERSION:
        return {"verified": False, "reason": "unsupported snapshot version"}

    expected = snapshot_hash(snapshot)
    if expected != snapshot["snapshot_hash"]:
        return {
            "verified": False,
            "reason": "snapshot hash mismatch",
            "expected_hash": expected,
        }

    return {"verified": True, "reason": "snapshot verified"}


def verify_snapshot_chain(snapshots: list[dict[str, Any]]) -> dict[str, Any]:
    """Verify parent-linked snapshot chain order and integrity."""

    if not isinstance(snapshots, list):
        return {"verified": False, "reason": "snapshots must be a list"}
    if not snapshots:
        return {"verified": False, "reason": "snapshot chain is empty"}

    previous_hash = GENESIS_PARENT
    for index, snapshot in enumerate(snapshots):
        result = verify_snapshot(snapshot)
        if not result["verified"]:
            return {"verified": False, "reason": f"snapshot {index} failed: {result['reason']}"}

        if snapshot["parent_snapshot_hash"] != previous_hash:
            return {
                "verified": False,
                "reason": "parent snapshot hash mismatch",
                "index": index,
                "expected_parent": previous_hash,
                "actual_parent": snapshot["parent_snapshot_hash"],
            }
        previous_hash = snapshot["snapshot_hash"]

    return {
        "verified": True,
        "reason": "snapshot chain verified",
        "snapshot_count": len(snapshots),
        "latest_snapshot_hash": previous_hash,
    }


__all__ = [
    "SNAPSHOT_VERSION",
    "GENESIS_PARENT",
    "create_snapshot",
    "verify_snapshot",
    "verify_snapshot_chain",
    "snapshot_hash",
]
