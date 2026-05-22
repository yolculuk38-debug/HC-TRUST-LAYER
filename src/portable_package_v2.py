"""HC:// portable verification package v2."""

from __future__ import annotations

from typing import Any


PORTABLE_PACKAGE_V2_VERSION = "HC-PORTABLE-PACKAGE-V2"


def build_portable_package_v2(
    *,
    record_id: str,
    exported_proof: dict[str, Any],
    certificate: dict[str, Any] | None = None,
    certificate_chain: dict[str, Any] | None = None,
    risk_summary: dict[str, Any] | None = None,
    policy_state: dict[str, Any] | None = None,
    audit_snapshot: dict[str, Any] | None = None,
    timeline: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a complete portable HC:// verification package."""

    return {
        "portable_package_version": PORTABLE_PACKAGE_V2_VERSION,
        "record_id": record_id,
        "exported_proof": exported_proof,
        "certificate": certificate or {},
        "certificate_chain": certificate_chain or {},
        "risk_summary": risk_summary or {},
        "policy_state": policy_state or {},
        "audit_snapshot": audit_snapshot or {},
        "timeline": timeline or {},
    }


def validate_portable_package_v2(package: dict[str, Any]) -> dict[str, Any]:
    """Validate portable package v2 shape."""

    if not isinstance(package, dict):
        return _result(False, ["invalid_package_structure"])

    reasons: list[str] = []

    required_fields = [
        "portable_package_version",
        "record_id",
        "exported_proof",
        "certificate",
        "risk_summary",
        "policy_state",
        "audit_snapshot",
        "timeline",
    ]

    for field in required_fields:
        if field not in package:
            reasons.append(f"missing_{field}")

    if package.get("portable_package_version") != PORTABLE_PACKAGE_V2_VERSION:
        reasons.append("unsupported_portable_package_version")

    return _result(not reasons, reasons)


def _result(valid: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "portable_package_version": PORTABLE_PACKAGE_V2_VERSION,
        "valid": valid,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "PORTABLE_PACKAGE_V2_VERSION",
    "build_portable_package_v2",
    "validate_portable_package_v2",
]
