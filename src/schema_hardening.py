"""HC:// schema hardening layer."""

from __future__ import annotations

from typing import Any


SCHEMA_HARDENING_VERSION = "HC-SCHEMA-HARDENING-V1"


SUPPORTED_PACKAGE_VERSIONS = {
    "HC-PORTABLE-PACKAGE-V2",
}


REQUIRED_TOP_LEVEL_FIELDS = {
    "portable_package_version",
    "record_id",
    "exported_proof",
    "certificate",
    "risk_summary",
    "policy_state",
    "audit_snapshot",
    "timeline",
}



def validate_hardened_package(package: dict[str, Any]) -> dict[str, Any]:
    """Apply strict schema hardening validation."""

    if not isinstance(package, dict):
        return _result(False, ["invalid_package_structure"])

    reasons: list[str] = []

    version = package.get("portable_package_version")

    if version not in SUPPORTED_PACKAGE_VERSIONS:
        reasons.append("unsupported_package_version")

    missing_fields = REQUIRED_TOP_LEVEL_FIELDS - set(package.keys())

    for field in sorted(missing_fields):
        reasons.append(f"missing_required_field:{field}")

    if not isinstance(package.get("record_id"), str):
        reasons.append("invalid_record_id_type")

    if not isinstance(package.get("exported_proof"), dict):
        reasons.append("invalid_exported_proof_structure")

    if not isinstance(package.get("certificate"), dict):
        reasons.append("invalid_certificate_structure")

    if not isinstance(package.get("risk_summary"), dict):
        reasons.append("invalid_risk_summary_structure")

    malformed = any(
        key.startswith("__")
        for key in package.keys()
    )

    if malformed:
        reasons.append("malformed_reserved_field_detected")

    return _result(not reasons, reasons)



def _result(valid: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "schema_hardening_version": SCHEMA_HARDENING_VERSION,
        "valid": valid,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "SCHEMA_HARDENING_VERSION",
    "SUPPORTED_PACKAGE_VERSIONS",
    "REQUIRED_TOP_LEVEL_FIELDS",
    "validate_hardened_package",
]
