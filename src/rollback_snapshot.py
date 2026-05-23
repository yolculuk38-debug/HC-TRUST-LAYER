"""HC:// rollback snapshot core."""

from __future__ import annotations

from datetime import UTC, datetime

ROLLBACK_SNAPSHOT_VERSION = "HC-ROLLBACK-SNAPSHOT-V1"


def create_rollback_snapshot(*, snapshot_id: str, commit_sha: str, reason: str) -> dict:
    """Create a rollback checkpoint before or after risky changes."""

    return {
        "rollback_snapshot_version": ROLLBACK_SNAPSHOT_VERSION,
        "snapshot_id": snapshot_id.strip(),
        "commit_sha": commit_sha.strip(),
        "reason": reason.strip(),
        "created_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "status": "READY",
    }


def mark_snapshot_used(snapshot: dict) -> dict:
    updated = dict(snapshot)
    updated["status"] = "USED"
    return updated
