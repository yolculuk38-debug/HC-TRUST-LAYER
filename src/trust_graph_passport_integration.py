"""HC:// trust graph to trust passport integration."""

from __future__ import annotations

from typing import Any

from manipulation_detection import detect_coordinated_manipulation
from status_passport_integration import build_status_passport
from trust_graph import validate_trust_graph


INTEGRATION_VERSION = "HC-GRAPH-PASSPORT-INTEGRATION-V1"


def build_graph_trust_passport(
    record_id: str,
    signals: dict[str, Any],
    graph: dict[str, Any],
    *,
    verification_response: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a trust passport enriched with graph and manipulation signals."""

    graph_validation = validate_trust_graph(graph)
    manipulation = detect_coordinated_manipulation(graph)

    risk_flags = list(signals.get("risk_flags", []) or [])
    risk_flags.extend(graph_validation.get("review_flags", []) or [])
    risk_flags.extend(manipulation.get("risk_flags", []) or [])

    if graph_validation.get("status") == "INVALID":
        risk_flags.append("invalid_trust_graph")

    if manipulation.get("risk_level") in {"MEDIUM", "HIGH"}:
        risk_flags.append("manipulation_review_required")

    merged_signals = dict(signals)
    merged_signals["risk_flags"] = sorted(set(risk_flags))

    passport = build_status_passport(
        record_id,
        merged_signals,
        verification_response=verification_response,
        provenance_summary={
            "verified": graph_validation.get("status") == "VALID",
            "review_flags": graph_validation.get("review_flags", []),
            "risk_flags": sorted(set(risk_flags)),
            "edge_count": graph.get("edge_count", 0),
        },
    )
    passport["integration_version"] = INTEGRATION_VERSION
    passport["trust_graph_validation"] = graph_validation
    passport["manipulation_detection"] = manipulation
    return passport


__all__ = ["INTEGRATION_VERSION", "build_graph_trust_passport"]
