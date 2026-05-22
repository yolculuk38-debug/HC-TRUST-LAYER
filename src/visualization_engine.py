"""HC:// visualization engine core."""

from __future__ import annotations


def build_visualization_node(*, node_id: str, label: str, trust_tier: str) -> dict:
    return {
        "node_id": node_id.strip(),
        "label": label.strip(),
        "trust_tier": trust_tier.strip().upper(),
    }
