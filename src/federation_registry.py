"""HC:// federation registry core."""

from __future__ import annotations

TRUST_STATES = {"PENDING", "TRUSTED", "SUSPENDED"}


def register_node(*, node_id: str, endpoint: str, trust_state: str = "PENDING") -> dict:
    state = trust_state.strip().upper()
    if state not in TRUST_STATES:
        state = "PENDING"
    return {
        "node_id": node_id.strip(),
        "endpoint": endpoint.strip(),
        "trust_state": state,
    }


def trusted_nodes(nodes: list[dict]) -> list[dict]:
    return [node for node in nodes if node.get("trust_state") == "TRUSTED"]


def update_node_state(node: dict, trust_state: str) -> dict:
    updated = dict(node)
    state = trust_state.strip().upper()
    updated["trust_state"] = state if state in TRUST_STATES else "PENDING"
    return updated
