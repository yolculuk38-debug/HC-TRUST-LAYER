"""Combined local advisory QR + Public Validator result.

This module combines the local QR record bridge with the existing local Public
Validator lookup result. It is local-only and advisory-only. It does not verify
QR authenticity, signatures, issuer authority, canonical URLs, legal status,
regulatory status, safety status, or truth.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from hc_runtime.public_validator_lookup import ROOT, lookup_public_validator_record
from hc_runtime.qr_record_bridge import check_qr_payload_record_bridge

ALLOWED_COMBINED_STATUSES: tuple[str, ...] = (
    "qr_record_validated",
    "qr_record_mismatch",
    "record_not_found",
    "duplicate_record_id",
    "invalid_payload",
    "malformed_payload",
    "validation_not_checked",
)

RESULT_FIELD_CONTRACT: tuple[str, ...] = (
    "status",
    "qr_payload_status",
    "bridge_status",
    "record_lookup_status",
    "content_hash_match",
    "local_validator",
    "warnings",
    "errors",
    "advisory_only",
    "public_safe",
    "truth_guarantee",
    "human_review_required",
)

SAFETY_MARKERS: dict[str, bool] = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}


def _base_result(status: str, bridge_result: dict[str, Any]) -> dict[str, Any]:
    if status not in ALLOWED_COMBINED_STATUSES:
        raise ValueError(f"Unsupported combined QR Public Validator status: {status}")

    result: dict[str, Any] = {
        "status": status,
        "qr_payload_status": bridge_result.get("qr_payload_status"),
        "bridge_status": bridge_result.get("bridge_status"),
        "record_lookup_status": bridge_result.get("record_lookup_status"),
        "content_hash_match": bridge_result.get("content_hash_match"),
        "local_validator": None,
        "warnings": list(bridge_result.get("warnings", [])),
        "errors": list(bridge_result.get("errors", [])),
        **SAFETY_MARKERS,
    }
    if tuple(result) != RESULT_FIELD_CONTRACT:
        raise RuntimeError("Combined QR Public Validator result contract changed unexpectedly.")
    return result


def _combined_status_from_bridge(bridge_result: dict[str, Any]) -> str:
    bridge_status = bridge_result.get("bridge_status")
    if bridge_status == "bridge_match":
        return "qr_record_validated"
    if bridge_status == "bridge_mismatch":
        return "qr_record_mismatch"
    if bridge_status == "record_not_found":
        return "record_not_found"
    if bridge_status == "duplicate_record_id":
        return "duplicate_record_id"
    if bridge_status == "malformed_payload":
        return "malformed_payload"
    if bridge_status == "invalid_payload":
        return "invalid_payload"
    return "validation_not_checked"


def _extract_record_id(payload: str | dict[str, Any]) -> str | None:
    if isinstance(payload, dict):
        value = payload.get("record_id")
        return value if isinstance(value, str) else None
    if not isinstance(payload, str):
        return None

    # Avoid duplicating parser logic beyond a local, no-network extraction for the
    # already-checked lookup path. Malformed payloads are handled by the bridge.
    import json

    try:
        decoded = json.loads(payload)
    except json.JSONDecodeError:
        return None
    if not isinstance(decoded, dict):
        return None
    value = decoded.get("record_id")
    return value if isinstance(value, str) else None


def run_qr_public_validator(payload: str | dict[str, Any], *, repo_root: Path | str | None = None) -> dict[str, Any]:
    """Return one combined local QR + Public Validator advisory result.

    The combined result first runs the local QR record bridge. If the bridge can
    resolve exactly one local canonical record, the function includes the existing
    local Public Validator lookup/schema/hash advisory result in `local_validator`.

    This function is local-only. It does not fetch canonical_url, call a network,
    verify signatures, prove QR authenticity, prove issuer authority, or provide
    truth verification. Human review remains required.
    """

    resolved_root = Path(repo_root or ROOT).resolve()
    bridge_result = check_qr_payload_record_bridge(payload, repo_root=resolved_root)
    combined_status = _combined_status_from_bridge(bridge_result)
    result = _base_result(combined_status, bridge_result)

    if bridge_result.get("record_lookup_status") == "found":
        record_id = _extract_record_id(payload)
        if record_id is None:
            result["warnings"].append(
                "Local Public Validator lookup was not included because record_id could not be extracted from the QR payload."
            )
            result["status"] = "validation_not_checked"
            return result

        local_validator = lookup_public_validator_record(record_id, root=resolved_root)
        result["local_validator"] = local_validator
        result["warnings"].append(
            "Combined local QR/Public Validator result is advisory-only; local validation does not prove QR authenticity, issuer authority, or truth."
        )
    else:
        result["warnings"].append(
            "Local Public Validator lookup result was not embedded because the QR record bridge did not find exactly one local canonical record."
        )

    return result
