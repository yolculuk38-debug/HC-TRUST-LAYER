"""HC:// audit snapshot layer."""

from __future__ import annotations

from typing import Any


AUDIT_SNAPSHOT_VERSION = "HC-AUDIT-SNAPSHOT-V1"



def build_audit_snapshot(
    *,
    snapshot_id: str,
    trust_state: str,
    evidence_score: int,
    previous_snapshot_hash: str | None = None,
    risk_flags: list[str] | None = None,
) -> dict[str, Any]:
    """Build immutable-style audit snapshot."""

    return {
        "audit_snapshot_version": AUDIT_SNAPSHOT_VERSION,
        "snapshot_id": snapshot_id,
        "trust_state": trust_state,
        "evidence_score": int(evidence_score),
        "previous_snapshot_hash": previous_snapshot_hash,
        "risk_flags": sorted(set(risk_flags or [])),
    }



def evaluate_audit_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]:
    """Evaluate audit snapshot integrity and trust visibility."""

    if not isinstance(snapshot, dict):
        return _result(False, "INVALID", ["invalid_snapshot_structure"])

    reasons: list[str] = []

    if not snapshot.get("snapshot_id"):
        reasons.append("missing_snapshot_id")

    if snapshot.get("risk_flags"):
        reasons.extend(snapshot.get("risk_flags", []))

    trusted = not reasons

    return _result(
        trusted,
        "VERIFIED" if trusted else "REVIEW_REQUIRED",
        reasons,
    )



def _result(trusted: bool, decision: str, reasons: list[str]) -> dict[str, Any]:
    return {
        "audit_snapshot_version": AUDIT_SNAPSHOT_VERSION,
        "trusted": trusted,
        "decision": decision,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "AUDIT_SNAPSHOT_VERSION",
    "build_audit_snapshot",
    "evaluate_audit_snapshot",
]
