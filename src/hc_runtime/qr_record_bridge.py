"""Local advisory bridge from QR payload content_hash to canonical record lookup.

This module intentionally stays local-only. It parses a QR payload, reuses the
existing Public Validator record_id lookup boundary, and compares the QR
payload content_hash with the matched local canonical record content_hash when
exactly one allowed record is found. It does not verify QR authenticity,
signatures, issuer authority, canonical URLs, or truth.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from hc_runtime.public_validator_lookup import (
    ALLOWED_RECORD_PATTERNS,
    ROOT,
    lookup_public_validator_record,
)
from hc_runtime.qr_payload_parser import (
    INVALID_PAYLOAD,
    MALFORMED_PAYLOAD,
    SAFETY_MARKERS,
    VALID_PAYLOAD,
    parse_qr_payload,
)

ALLOWED_BRIDGE_STATUSES: tuple[str, ...] = (
    "bridge_match",
    "bridge_mismatch",
    "record_not_found",
    "duplicate_record_id",
    "invalid_payload",
    "malformed_payload",
    "bridge_not_checked",
)

RESULT_FIELD_CONTRACT: tuple[str, ...] = (
    "qr_payload_status",
    "record_lookup_status",
    "content_hash_match",
    "bridge_status",
    "warnings",
    "errors",
    "advisory_only",
    "public_safe",
    "truth_guarantee",
    "human_review_required",
)


def _base_result(
    qr_payload_status: str,
    bridge_status: str,
    *,
    record_lookup_status: str = "not_checked",
    content_hash_match: bool | None = None,
) -> dict[str, Any]:
    if bridge_status not in ALLOWED_BRIDGE_STATUSES:
        raise ValueError(f"Unsupported QR record bridge status: {bridge_status}")

    result: dict[str, Any] = {
        "qr_payload_status": qr_payload_status,
        "record_lookup_status": record_lookup_status,
        "content_hash_match": content_hash_match,
        "bridge_status": bridge_status,
        "warnings": [],
        "errors": [],
        **SAFETY_MARKERS,
    }
    if tuple(result) != RESULT_FIELD_CONTRACT:
        raise RuntimeError("QR record bridge result contract changed unexpectedly.")
    return result


def _load_payload_object(payload: str | dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    if isinstance(payload, dict):
        return dict(payload), None
    if not isinstance(payload, str):
        return None, "QR payload bridge input must be a JSON string or payload object."
    try:
        decoded = json.loads(payload)
    except json.JSONDecodeError as exc:
        return None, f"QR payload is malformed JSON: {exc.msg}."
    if not isinstance(decoded, dict):
        return None, "QR payload JSON must be an object."
    return decoded, None


def _parser_input(payload: str | dict[str, Any]) -> str:
    if isinstance(payload, str):
        return payload
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def _normalize_hash(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    normalized = value.strip().lower()
    return normalized or None


def _is_allowed_lookup_source(source_path: object) -> bool:
    if not isinstance(source_path, str):
        return False
    for pattern in ALLOWED_RECORD_PATTERNS:
        directory = Path(pattern).parent.as_posix()
        if source_path.startswith(f"{directory}/") and source_path.endswith(".json"):
            return True
    return False


def _load_record_content_hash(root: Path, source_path: str) -> tuple[str | None, str | None]:
    if not _is_allowed_lookup_source(source_path):
        return None, "Public Validator lookup returned a source outside the allowed canonical record paths."

    record_path = (root / source_path).resolve()
    try:
        record_path.relative_to(root.resolve())
    except ValueError:
        return None, "Public Validator lookup source could not be constrained to the local repository root."

    try:
        with record_path.open(encoding="utf-8") as handle:
            record = json.load(handle)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return None, f"Matched local record content_hash could not be loaded: {exc.__class__.__name__}."

    if not isinstance(record, dict):
        return None, "Matched local record JSON must be an object."

    normalized = _normalize_hash(record.get("content_hash"))
    if normalized is None:
        return None, "Matched local record content_hash is missing or invalid."
    return normalized, None


def check_qr_payload_record_bridge(
    payload_result_or_payload: str | dict[str, Any], *, repo_root: Path | str | None = None
) -> dict[str, Any]:
    """Check QR payload content_hash against one local canonical record match.

    The bridge accepts either a raw QR payload JSON string or a parsed payload
    object. It first uses the local QR payload parser. It only proceeds to the
    existing local Public Validator lookup path when the payload is parser-valid
    and contains a usable QR record_id and content_hash. Lookup remains limited
    to the existing allowed canonical record paths:
    records/pending/*.json, records/verified/*.json, and
    records/archived/*.json.

    The result is public-safe and advisory-only. A content_hash match does not
    prove QR authenticity, issuer authority, signature verification, canonical
    URL control, record truth, or production readiness.
    """

    parser_result = parse_qr_payload(_parser_input(payload_result_or_payload))
    qr_payload_status = parser_result["status"]

    payload, load_error = _load_payload_object(payload_result_or_payload)
    if qr_payload_status == MALFORMED_PAYLOAD or load_error is not None:
        result = _base_result(MALFORMED_PAYLOAD, "malformed_payload")
        result["warnings"].extend(parser_result["warnings"])
        result["errors"].extend(parser_result["errors"] or ([load_error] if load_error else []))
        return result

    assert payload is not None
    result = _base_result(qr_payload_status, "bridge_not_checked")
    result["warnings"].extend(parser_result["warnings"])
    result["errors"].extend(parser_result["errors"])

    if qr_payload_status != VALID_PAYLOAD:
        result["bridge_status"] = INVALID_PAYLOAD
        result["warnings"].append(
            "QR payload record bridge was not checked because the payload did not pass local advisory parser checks."
        )
        return result

    record_id = payload.get("record_id")
    content_hash = _normalize_hash(payload.get("content_hash"))
    if not isinstance(record_id, str) or not record_id.strip() or content_hash is None:
        result["bridge_status"] = INVALID_PAYLOAD
        result["warnings"].append(
            "QR payload record bridge was not checked because record_id or content_hash was missing or invalid."
        )
        return result

    resolved_root = Path(repo_root or ROOT).resolve()
    lookup_result = lookup_public_validator_record(record_id, root=resolved_root)
    result["record_lookup_status"] = lookup_result["status"]

    if lookup_result["status"] == "not_found":
        result["bridge_status"] = "record_not_found"
        result["warnings"].append(
            "No matching record_id was found in allowed local canonical record directories; content_hash was not compared."
        )
        return result

    if lookup_result["status"] == "duplicate_record_id":
        result["bridge_status"] = "duplicate_record_id"
        result["warnings"].append(
            "Duplicate record_id matches were found in allowed local canonical record directories; content_hash was not compared."
        )
        result["errors"].append(
            "QR payload record bridge requires exactly one local canonical record match."
        )
        return result

    if lookup_result["status"] != "found":
        result["bridge_status"] = "bridge_not_checked"
        result["warnings"].append(
            "QR payload record bridge was not checked because local record lookup did not find exactly one allowed record."
        )
        result["errors"].extend(lookup_result.get("errors", []))
        return result

    source_path = lookup_result.get("source_path")
    local_content_hash, content_hash_error = _load_record_content_hash(
        resolved_root, source_path if isinstance(source_path, str) else ""
    )
    if content_hash_error is not None or local_content_hash is None:
        result["bridge_status"] = "bridge_not_checked"
        result["errors"].append(content_hash_error or "Matched local record content_hash could not be checked.")
        return result

    result["content_hash_match"] = content_hash == local_content_hash
    if result["content_hash_match"]:
        result["bridge_status"] = "bridge_match"
        result["warnings"].append(
            "QR payload content_hash matches the local canonical record content_hash; this is advisory-only and does not prove QR authenticity, issuer authority, or truth."
        )
    else:
        result["bridge_status"] = "bridge_mismatch"
        result["warnings"].append(
            "QR payload content_hash does not match the local canonical record content_hash; human review remains required."
        )
        result["errors"].append("QR payload content_hash mismatch against matched local canonical record.")

    return result
