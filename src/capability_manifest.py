"""HC:// capability manifest core."""

from __future__ import annotations


def create_capability_manifest(*, node_id: str, capabilities: list[str]) -> dict:
    return {
        "node_id": node_id.strip(),
        "capabilities": sorted({cap.strip().upper() for cap in capabilities}),
    }
