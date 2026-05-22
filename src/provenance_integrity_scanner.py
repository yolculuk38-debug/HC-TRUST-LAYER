"""HC:// provenance integrity scanner."""

from __future__ import annotations

from typing import Any


PROVENANCE_SCANNER_VERSION = "HC-PROVENANCE-SCANNER-V1"


class ProvenanceRisk:
    CLEAN = "CLEAN"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    INVALID = "INVALID"



def scan_provenance_integrity(provenance: dict[str, Any]) -> dict[str, Any]:
    """Scan provenance data for broken lineage and tamper anomalies."""

    if not isinstance(provenance, dict):
        return _result(ProvenanceRisk.INVALID, ["invalid_provenance_structure"])

    reasons: list[str] = []

    if provenance.get("orphan_revision"):
        reasons.append("orphan_revision_detected")

    if provenance.get("broken_lineage"):
        reasons.append("broken_lineage_detected")

    if provenance.get("forged_reference"):
        reasons.append("forged_provenance_reference")

    if provenance.get("tamper_anomaly"):
        reasons.append("tamper_anomaly_detected")

    if "forged_provenance_reference" in reasons or "broken_lineage_detected" in reasons:
        decision = ProvenanceRisk.INVALID
    elif reasons:
        decision = ProvenanceRisk.REVIEW_REQUIRED
    else:
        decision = ProvenanceRisk.CLEAN

    return _result(decision, reasons)



def _result(decision: str, reasons: list[str]) -> dict[str, Any]:
    return {
        "provenance_scanner_version": PROVENANCE_SCANNER_VERSION,
        "decision": decision,
        "trusted": decision == ProvenanceRisk.CLEAN,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "PROVENANCE_SCANNER_VERSION",
    "ProvenanceRisk",
    "scan_provenance_integrity",
]
