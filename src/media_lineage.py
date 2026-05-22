"""HC:// media lineage core."""

from __future__ import annotations

MEDIA_LINEAGE_VERSION = "HC-MEDIA-LINEAGE-V1"


def create_media_lineage_entry(*, media_id: str, media_hash: str, parent_hash: str = "") -> dict:
    return {
        "media_lineage_version": MEDIA_LINEAGE_VERSION,
        "media_id": media_id.strip(),
        "media_hash": media_hash.strip(),
        "parent_hash": parent_hash.strip(),
    }


def has_parent_lineage(entry: dict) -> bool:
    return bool(entry.get("parent_hash"))
