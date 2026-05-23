"""HC:// validator network coordination."""

from __future__ import annotations


def build_validator_node(*, node_id: str, trust_score: int) -> dict:
    return {
        "node_id": node_id.strip(),
        "trust_score": max(0, min(int(trust_score), 100)),
    }


def eligible_validators(nodes: list[dict], minimum_score: int = 70) -> list[dict]:
    return [node for node in nodes if int(node.get("trust_score", 0)) >= minimum_score]


def validator_consensus(nodes: list[dict], minimum_score: int = 70) -> bool:
    return len(eligible_validators(nodes, minimum_score=minimum_score)) >= 3
