"""HC:// signed export package."""

from __future__ import annotations

import hashlib
import json
from typing import Any


SIGNED_EXPORT_PACKAGE_VERSION = "HC-SIGNED-EXPORT-V1"



def build_signed_export_package(
    *,
    payload: dict[str, Any],
    signer_id: str,
) -> dict[str, Any]:
    """Build deterministic signed export package."""

    normalized = json.dumps(payload, sort_keys=True, separators=(",", ":"))

    signature = hashlib.sha256(
        f"{signer_id}:{normalized}".encode("utf-8")
    ).hexdigest()

    return {
        "signed_export_package_version": SIGNED_EXPORT_PACKAGE_VERSION,
        "signer_id": signer_id,
        "signature": signature,
        "payload": payload,
    }



def verify_signed_export_package(package: dict[str, Any]) -> dict[str, Any]:
    """Verify deterministic export signature."""

    if not isinstance(package, dict):
        return _result(False, ["invalid_signed_package_structure"])

    signer_id = package.get("signer_id")
    payload = package.get("payload")
    signature = package.get("signature")

    reasons: list[str] = []

    if not signer_id:
        reasons.append("missing_signer_id")

    if not isinstance(payload, dict):
        reasons.append("invalid_payload")

    if not signature:
        reasons.append("missing_signature")

    if reasons:
        return _result(False, reasons)

    normalized = json.dumps(payload, sort_keys=True, separators=(",", ":"))

    expected = hashlib.sha256(
        f"{signer_id}:{normalized}".encode("utf-8")
    ).hexdigest()

    if expected != signature:
        reasons.append("signature_mismatch")

    return _result(not reasons, reasons)



def _result(valid: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "signed_export_package_version": SIGNED_EXPORT_PACKAGE_VERSION,
        "valid": valid,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "SIGNED_EXPORT_PACKAGE_VERSION",
    "build_signed_export_package",
    "verify_signed_export_package",
]
