"""Combined local advisory QR/Public Validator result for HC:// records.

This module intentionally combines only existing local-only layers: the QR
payload parser, the QR-to-local-record bridge, and the Public Validator local
record lookup/schema/hash advisory result. It does not call a network, fetch
canonical_url, add backend/API behavior, verify signatures, prove QR
authenticity, prove issuer authority, or verify truth.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from hc_runtime.public_validator_lookup import ROOT, lookup_public_validator_record
from hc_runtime.qr_payload_parser import SAFETY_MARKERS
from hc_runtime.qr_record_bridge import check_qr_payload_record_bridge

ALLOWED_QR_PUBLIC_VALIDATOR_STATUSES: tuple[str, ...] = (
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

BRIDGE_STATUS_TO_COMBINED_STATUS: dict[str, str] = {
    "bridge_match": "qr_record_validated",
    "bridge_mismatch": "qr_record_mismatch",
    "record_not_found": "record_not_found",
    "duplicate_record_id": "duplicate_record_id",
    "invalid_payload": "invalid_payload",
    "malformed_payload": "malformed_payload",
    "bridge_not_checked": "validation_not_checked",
}


def _payload_object(payload: str | dict[str, Any]) -> dict[str, Any] | None:
    if isinstance(payload, dict):
        return dict(payload)
    if not isinstance(payload, str):
        return None
    try:
        decoded = json.loads(payload)
    except json.JSONDecodeError:
        return None
    if not isinstance(decoded, dict):
        return None
    return decoded


def _build_result(
    *,
    status: str,
    qr_payload_status: str,
    bridge_status: str,
    record_lookup_status: str,
    content_hash_match: bool | None,
    local_validator: dict[str, Any] | None,
    warnings: list[str],
    errors: list[str],
) -> dict[str, Any]:
    if status not in ALLOWED_QR_PUBLIC_VALIDATOR_STATUSES:
        raise ValueError(f"Unsupported QR Public Validator status: {status}")

    result: dict[str, Any] = {
        "status": status,
        "qr_payload_status": qr_payload_status,
        "bridge_status": bridge_status,
        "record_lookup_status": record_lookup_status,
        "content_hash_match": content_hash_match,
        "local_validator": local_validator,
        "warnings": list(warnings),
        "errors": list(errors),
        **SAFETY_MARKERS,
    }
    if tuple(result) != RESULT_FIELD_CONTRACT:
        raise RuntimeError("QR Public Validator result contract changed unexpectedly.")
    return result


def run_qr_public_validator(
    payload: str | dict[str, Any], *, repo_root: Path | str | None = None
) -> dict[str, Any]:
    """Return one public-safe local advisory QR/Public Validator result.

    The function parses the QR payload, runs the parser-local advisory
    ``payload_hash`` check through the existing QR parser/bridge flow, compares
    QR ``content_hash`` with exactly one matched local canonical record when
    available, and includes the existing local Public Validator lookup plus
    schema/hash advisory result only when the local lookup finds exactly one
    record.

    Lookup remains constrained to the existing Public Validator allowed local
    canonical record paths. Demo fixtures are not canonical records. The
    function does not fetch ``canonical_url``, call a network, call a backend or
    API, verify signatures, prove QR authenticity, prove issuer authority,
    prove truth, or claim production readiness. Human review remains required.
    """

    resolved_root = Path(repo_root or ROOT).resolve()
    bridge_result = check_qr_payload_record_bridge(payload, repo_root=resolved_root)
    bridge_status = bridge_result["bridge_status"]
    status = BRIDGE_STATUS_TO_COMBINED_STATUS.get(bridge_status, "validation_not_checked")

    local_validator: dict[str, Any] | None = None
    payload_object = _payload_object(payload)
    record_id = payload_object.get("record_id") if payload_object is not None else None

    if bridge_result["record_lookup_status"] == "found" and isinstance(record_id, str):
        lookup_result = lookup_public_validator_record(record_id, root=resolved_root)
        if lookup_result["status"] == "found":
            local_validator = lookup_result
        else:
            status = BRIDGE_STATUS_TO_COMBINED_STATUS.get(
                bridge_result["bridge_status"], "validation_not_checked"
            )

    warnings = list(bridge_result["warnings"])
    errors = list(bridge_result["errors"])
    warnings.append(
        "Combined QR/Public Validator result is local advisory output only; QR payload validity does not prove QR authenticity, content_hash match does not prove truth, and local schema/hash validation does not prove issuer authority."
    )

    return _build_result(
        status=status,
        qr_payload_status=bridge_result["qr_payload_status"],
        bridge_status=bridge_status,
        record_lookup_status=bridge_result["record_lookup_status"],
        content_hash_match=bridge_result["content_hash_match"],
        local_validator=local_validator,
        warnings=warnings,
        errors=errors,
    )
