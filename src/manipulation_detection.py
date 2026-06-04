"""Minimal HC:// trust graph manipulation detection compatibility module.

Signals returned here are advisory review-routing indicators for
human-supervised validation, not forensic certainty claims.
"""

from __future__ import annotations

from collections import Counter
from enum import Enum
from typing import Any

from trust_graph import validate_trust_graph


class ManipulationRiskLevel(str, Enum):
    """Advisory coordinated manipulation risk labels."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"
    INVALID = "INVALID"


def _invalid_result(reason: str) -> dict[str, Any]:
    return {
        "risk_level": ManipulationRiskLevel.INVALID,
        "risk_flags": [],
        "reasons": [reason],
        "advisory_only": True,
        "human_supervised_validation_required": True,
    }


def detect_coordinated_manipulation(graph: dict[str, Any]) -> dict[str, Any]:
    """Detect basic advisory manipulation patterns in a trust graph."""

    if not isinstance(graph, dict):
        return _invalid_result("graph must be an object")

    validation = validate_trust_graph(graph)
    if validation.get("status") == "INVALID":
        return _invalid_result(str(validation.get("reason", "invalid graph")))

    edges = graph.get("edges")
    if not isinstance(edges, list):
        return _invalid_result("graph edges must be a list")

    flags: set[str] = set()
    target_counts: Counter[str] = Counter()
    edge_type_counts: Counter[str] = Counter()
    observed_at_counts: Counter[str] = Counter()

    for edge in edges:
        if not isinstance(edge, dict):
            return _invalid_result("graph edges must be objects")

        source_id = edge.get("source_id")
        target_id = edge.get("target_id")
        edge_type = edge.get("edge_type")
        observed_at = edge.get("observed_at")

        target_counts[str(target_id)] += 1
        edge_type_counts[str(edge_type)] += 1
        observed_at_counts[str(observed_at)] += 1

        if source_id == target_id:
            flags.add("self_reference_loop")

    if edge_type_counts["mirrors"] >= 5:
        flags.add("mirror_cluster")

    if any(count >= 5 for count in target_counts.values()):
        flags.add("single_target_amplification")

    if any(count >= 5 for count in observed_at_counts.values()):
        flags.add("synchronized_timing")

    if edge_type_counts["repost_of"] >= 5:
        flags.add("repost_cluster")

    if {"mirror_cluster", "single_target_amplification"}.issubset(flags):
        risk_level = ManipulationRiskLevel.HIGH
    elif flags:
        risk_level = ManipulationRiskLevel.MEDIUM
    else:
        risk_level = ManipulationRiskLevel.LOW

    return {
        "risk_level": risk_level,
        "risk_flags": sorted(flags),
        "reasons": sorted(flags),
        "advisory_only": True,
        "human_supervised_validation_required": True,
    }


__all__ = ["ManipulationRiskLevel", "detect_coordinated_manipulation"]
