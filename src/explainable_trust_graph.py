"""HC:// explainable trust graph."""

from __future__ import annotations

from typing import Any


TRUST_GRAPH_VERSION = "HC-EXPLAINABLE-TRUST-GRAPH-V1"


def build_trust_graph_explanation(evidence_result: dict[str, Any]) -> dict[str, Any]:
    """Build a human-readable trust graph explanation from evidence output."""

    if not isinstance(evidence_result, dict):
        return {
            "trust_graph_version": TRUST_GRAPH_VERSION,
            "decision": "INVALID",
            "nodes": [],
            "edges": [],
            "explanation": "Invalid evidence result.",
            "reasons": ["invalid_evidence_result"],
        }

    decision = evidence_result.get("decision", "REVIEW_REQUIRED")
    score = int(evidence_result.get("evidence_score", 0) or 0)
    reasons = list(evidence_result.get("reasons", []) or [])

    nodes = [
        {"id": "hash", "type": "evidence"},
        {"id": "provenance", "type": "evidence"},
        {"id": "witness", "type": "evidence"},
        {"id": "registry", "type": "trust_control"},
        {"id": "federation", "type": "trust_control"},
        {"id": "decision", "type": "outcome", "value": decision},
    ]

    edges = [
        {"from": "hash", "to": "decision"},
        {"from": "provenance", "to": "decision"},
        {"from": "witness", "to": "decision"},
        {"from": "registry", "to": "decision"},
        {"from": "federation", "to": "decision"},
    ]

    return {
        "trust_graph_version": TRUST_GRAPH_VERSION,
        "decision": decision,
        "evidence_score": score,
        "nodes": nodes,
        "edges": edges,
        "explanation": _explain(decision, score, reasons),
        "reasons": sorted(set(reasons)),
    }


def _explain(decision: str, score: int, reasons: list[str]) -> str:
    if decision == "VERIFIED":
        return f"Verification passed with strong layered evidence score {score}."
    if decision == "PARTIAL":
        return f"Verification has partial support with evidence score {score}."
    if decision == "REVIEW_REQUIRED":
        return f"Verification requires review due to missing or weak signals: {', '.join(reasons)}."
    return f"Verification is invalid or insufficient with evidence score {score}."


__all__ = [
    "TRUST_GRAPH_VERSION",
    "build_trust_graph_explanation",
]
