"""HC:// verification status to trust passport integration."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from trust_passport import build_trust_passport
from verification_status_engine import determine_verification_status


INTEGRATION_VERSION = "HC-STATUS-PASSPORT-INTEGRATION-V1"


def build_status_passport(
    record_id: str,
    signals: dict[str, Any],
    *,
    verification_response: dict[str, Any] | None = None,
    evidence_summary: dict[str, Any] | None = None,
    federation_summary: dict[str, Any] | None = None,
    provenance_summary: dict[str, Any] | None = None,
    audit_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a trust passport enriched with central status engine output."""

    status_result = determine_verification_status(signals)

    response = verification_response if verification_response is not None else {
        "decision": status_result["state"], "trusted": False,
    }

    passport = build_trust_passport(
        record_id,
        response,
        evidence_summary=evidence_summary,
        federation_summary=federation_summary,
        provenance_summary=provenance_summary,
        audit_summary=audit_summary,
    )
    passport["source_claims"]["status_signals"] = deepcopy(signals)
    if status_result["state"] == "INVALID":
        passport["status"] = passport["decision"] = "INVALID"
    passport["risk_flags"] = sorted(set(passport["risk_flags"] + status_result["risk_flags"]))
    passport["integration_version"] = INTEGRATION_VERSION
    passport["status_engine"] = status_result
    passport["verification_level"] = status_result["level"]
    passport["verification_reasons"] = status_result.get("reasons", [])
    return passport


__all__ = ["INTEGRATION_VERSION", "build_status_passport"]
