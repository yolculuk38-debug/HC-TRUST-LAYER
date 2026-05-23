"""HC:// protocol graph mapping."""

from __future__ import annotations


def build_graph_node(*, node_id: str, node_type: str) -> dict:
    return {
        "node_id": node_id.strip(),
        "node_type": node_type.strip().lower(),
    }


def build_graph_edge(*, source: str, target: str, relation: str) -> dict:
    return {
        "source": source.strip(),
        "target": target.strip(),
        "relation": relation.strip().lower(),
    }


def graph_edge_valid(edge: dict) -> bool:
    return bool(edge.get("source")) and bool(edge.get("target"))
