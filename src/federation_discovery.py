"""HC:// federation discovery core."""

from __future__ import annotations


def build_discovery_entry(*, node_id: str, endpoint: str) -> dict:
    return {
        "node_id": node_id.strip(),
        "endpoint": endpoint.strip(),
    }
