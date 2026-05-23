"""HC:// production federation layer.

Defines deterministic production federation policies and validator mesh
compatibility rules.
"""

from __future__ import annotations

from typing import Any, Iterable

PRODUCTION_FEDERATION_VERSION = "HC-FEDERATION-PROD-V1"



def normalize_federation_node(node: dict[str, Any]) -> dict[str, Any]:
    """Normalize federation node state."""

    return {
        "node_id": str(node.get("node_id", "")).strip(),
        "trust_score": max(0, min(int(node.get("trust_score", 0)), 100)),
        "active": bool(node.get("active", False)),
        "policy_version": str(node.get("policy_version", PRODUCTION_FEDERATION_VERSION)).strip(),
    }



def eligible_federation_nodes(
    nodes: Iterable[dict[str, Any]],
    minimum_score: int = 75,
) -> list[dict[str, Any]]:
    """Return production eligible federation nodes."""

    normalized = [normalize_federation_node(node) for node in nodes]

    return [
        node
        for node in normalized
        if node["active"] and node["trust_score"] >= minimum_score
    ]



def federation_policy_contract() -> dict[str, Any]:
    """Describe production federation compatibility rules."""

    return {
        "policy_version": PRODUCTION_FEDERATION_VERSION,
        "minimum_trust_score": 75,
        "deterministic_ordering": True,
        "requires_active_nodes": True,
    }



def federation_mesh_snapshot(nodes: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return deterministic federation mesh ordering."""

    eligible = eligible_federation_nodes(nodes)

    return sorted(
        eligible,
        key=lambda item: (
            item["trust_score"] * -1,
            item["node_id"],
        ),
    )


__all__ = [
    "PRODUCTION_FEDERATION_VERSION",
    "normalize_federation_node",
    "eligible_federation_nodes",
    "federation_policy_contract",
    "federation_mesh_snapshot",
]
