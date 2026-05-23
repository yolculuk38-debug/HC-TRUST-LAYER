"""HC:// federation sync core."""

from __future__ import annotations


def build_node(*, node_id: str, endpoint: str) -> dict:
    return {
        "node_id": node_id.strip(),
        "endpoint": endpoint.strip(),
        "status": "DISCOVERED",
    }


def activate_node(node: dict) -> dict:
    updated = dict(node)
    updated["status"] = "ACTIVE"
    return updated


def ready_nodes(nodes: list[dict]) -> list[dict]:
    return [node for node in nodes if node.get("status") == "ACTIVE"]
