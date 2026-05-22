"""HC:// trust recovery flow."""

from __future__ import annotations

from typing import Any


TRUST_RECOVERY_VERSION = "HC-TRUST-RECOVERY-V1"


class RecoveryStatus:
    REQUESTED = "REQUESTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    RESTORED = "RESTORED"
    DENIED = "DENIED"



def build_recovery_request(
    *,
    target_id: str,
    target_type: str,
    reason: str,
    evidence: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a trust recovery request."""

    return {
        "trust_recovery_version": TRUST_RECOVERY_VERSION,
        "target_id": target_id,
        "target_type": target_type,
        "status": RecoveryStatus.REQUESTED,
        "reason": reason,
        "evidence": evidence or {},
    }



def evaluate_recovery_request(request: dict[str, Any]) -> dict[str, Any]:
    """Evaluate whether a recovery request can restore trust."""

    if not isinstance(request, dict):
        return _result(RecoveryStatus.DENIED, False, ["invalid_recovery_request"])

    reasons: list[str] = []

    if not request.get("target_id"):
        reasons.append("missing_target_id")

    if not request.get("reason"):
        reasons.append("missing_recovery_reason")

    evidence = request.get("evidence", {})

    if not evidence:
        reasons.append("missing_recovery_evidence")

    if reasons:
        return _result(RecoveryStatus.UNDER_REVIEW, False, reasons)

    return _result(RecoveryStatus.RESTORED, True, [])



def _result(status: str, restored: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "trust_recovery_version": TRUST_RECOVERY_VERSION,
        "status": status,
        "restored": restored,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "TRUST_RECOVERY_VERSION",
    "RecoveryStatus",
    "build_recovery_request",
    "evaluate_recovery_request",
]
