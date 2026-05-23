"""HC:// immutable snapshot layer."""

from __future__ import annotations

from datetime import UTC, datetime


def build_snapshot(*, snapshot_id: str, source_ref: str, content_hash: str) -> dict:
    return {
        "snapshot_id": snapshot_id.strip(),
        "source_ref": source_ref.strip(),
        "content_hash": content_hash.strip(),
        "created_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "state": "IMMUTABLE",
    }


def verify_snapshot(snapshot: dict, expected_hash: str) -> bool:
    return snapshot.get("content_hash") == expected_hash.strip()
