"""HC:// region sync core."""

from __future__ import annotations


def build_region_sync(*, source_region: str, target_region: str, sync_id: str) -> dict:
    return {
        "source_region": source_region.strip(),
        "target_region": target_region.strip(),
        "sync_id": sync_id.strip(),
    }
