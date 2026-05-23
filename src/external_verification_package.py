"""HC:// external verification package.

Creates deterministic portable verification bundles for external systems,
offline verification, and cross-platform audit transfer.
"""

from __future__ import annotations

from typing import Any, Iterable

PACKAGE_VERSION = "HC-VERIFY-PACKAGE-V1"



def normalize_package_record(record: dict[str, Any]) -> dict[str, Any]:
    """Normalize portable verification record."""

    return {
        "record_id": str(record.get("record_id", "")).strip(),
        "content_hash": str(record.get("content_hash", "")).strip(),
        "verification_status": str(record.get("verification_status", "UNKNOWN")).strip().upper(),
    }



def build_verification_package(
    *,
    records: Iterable[dict[str, Any]],
    exported_by: str,
    federation_enabled: bool = False,
) -> dict[str, Any]:
    """Build deterministic external verification package."""

    normalized = [normalize_package_record(record) for record in records]

    return {
        "package_version": PACKAGE_VERSION,
        "exported_by": exported_by.strip(),
        "federation_enabled": bool(federation_enabled),
        "record_count": len(normalized),
        "records": sorted(
            normalized,
            key=lambda item: (
                item["record_id"],
                item["content_hash"],
            ),
        ),
    }



def verify_external_package(package: dict[str, Any]) -> dict[str, Any]:
    """Verify deterministic structure of external verification package."""

    records = package.get("records", [])

    valid = (
        package.get("package_version") == PACKAGE_VERSION
        and isinstance(records, list)
        and all(record.get("record_id") for record in records)
    )

    return {
        "valid": valid,
        "record_count": len(records),
        "package_version": package.get("package_version", "UNKNOWN"),
    }


__all__ = [
    "PACKAGE_VERSION",
    "normalize_package_record",
    "build_verification_package",
    "verify_external_package",
]
