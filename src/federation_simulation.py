"""HC:// federation simulation sandbox."""

from __future__ import annotations

from typing import Any

from federation_consensus import evaluate_federation_consensus


FEDERATION_SIMULATION_VERSION = "HC-FEDERATION-SIMULATION-V1"


def simulate_federation_scenario(
    *,
    nodes: list[dict[str, Any]],
    manipulation_pressure: int = 0,
) -> dict[str, Any]:
    """Simulate federation consensus under pressure."""

    votes = []
    degraded_nodes = 0

    for node in nodes:
        weight = int(node.get("weight", 0) or 0)
        trusted = bool(node.get("trusted", False))
        compromised = bool(node.get("compromised", False))

        if compromised:
            degraded_nodes += 1
            trusted = False

        if manipulation_pressure >= 50 and weight < 30:
            trusted = False

        votes.append({"approved": trusted, "weight": weight})

    consensus = evaluate_federation_consensus(votes)

    return {
        "federation_simulation_version": FEDERATION_SIMULATION_VERSION,
        "node_count": len(nodes),
        "degraded_nodes": degraded_nodes,
        "manipulation_pressure": manipulation_pressure,
        "consensus": consensus,
    }


__all__ = [
    "FEDERATION_SIMULATION_VERSION",
    "simulate_federation_scenario",
]
