"""HC:// adversarial payload lab."""

from __future__ import annotations

from typing import Any


ADVERSARIAL_PAYLOAD_LAB_VERSION = "HC-ADVERSARIAL-PAYLOAD-LAB-V1"


def inspect_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Inspect suspicious portable verification payloads."""

    if not isinstance(payload, dict):
        return _result(False, ["invalid_payload_structure"])

    reasons: list[str] = []

    if any(str(key).startswith("__") for key in payload.keys()):
        reasons.append("reserved_field_detected")

    if payload.get("portable_package_version") not in {"HC-PORTABLE-PACKAGE-V2", None}:
        reasons.append("unexpected_package_version")

    if payload.get("qr_url") and not str(payload.get("qr_url")).startswith("https://"):
        reasons.append("unsafe_qr_url")

    if payload.get("provenance") == "forged":
        reasons.append("forged_provenance_marker")

    return _result(not reasons, reasons)


def _result(clean: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "adversarial_payload_lab_version": ADVERSARIAL_PAYLOAD_LAB_VERSION,
        "clean": clean,
        "decision": "CLEAN" if clean else "REVIEW_REQUIRED",
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "ADVERSARIAL_PAYLOAD_LAB_VERSION",
    "inspect_payload",
]
