"""HC:// federation synchronization event core."""

from __future__ import annotations

from datetime import UTC, datetime

FEDERATION_SYNC_VERSION = "HC-FEDERATION-SYNC-V1"


def create_sync_event(*, source_node: str, target_node: str, sync_hash: str) -> dict:
    return {
        "federation_sync_version": FEDERATION_SYNC_VERSION,
        "source_node": source_node.strip(),
        "target_node": target_node.strip(),
        "sync_hash": sync_hash.strip(),
        "synced_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }
