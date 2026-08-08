"""Local advisory QR payload parser for HC:// runtime flows.

This module intentionally performs only local JSON payload parsing and
structural validation. It does not verify authenticity, fetch URLs, call a
backend, or make truth claims about an HC:// record.
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any, Optional, Tuple
from urllib.parse import urlparse

from hc_trust.canonicalization import CanonicalizationError, strict_json_loads
from hc_trust.hashing import (
    CONTENT_HASH_PROFILE_FIELD,
    ContentHashError,
    calculate_content_hash,
    calculate_qr_payload_hash,
)

VALID_PAYLOAD = "valid_payload"
INVALID_PAYLOAD = "invalid_payload"
MALFORMED_PAYLOAD = "malformed_payload"

REQUIRED_FIELDS = (
    "qr_version",
    "record_id",
    "canonical_url",
    "payload_hash",
    "content_hash",
    "issued_at",
    "issuer_id",
    "algorithm",
    "key_id",
)

EXPECTED_FIELD_TYPES = {field: str for field in REQUIRED_FIELDS}
RECORD_ID_RE = re.compile(r"^HC-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{4}-\d{4}$")

ALLOWED_QR_PAYLOAD_STATUSES = (
    VALID_PAYLOAD,
    INVALID_PAYLOAD,
    MALFORMED_PAYLOAD,
)

RESULT_FIELD_CONTRACT = (
    "status",
    "warnings",
    "errors",
    "advisory_only",
    "public_safe",
    "truth_guarantee",
    "human_review_required",
)

SAFETY_MARKERS = {
    "advisory_only": True,
    "public_safe": True,
    "truth_guarantee": False,
    "human_review_required": True,
}


def _build_result(
    status: str,
    warnings: Optional[list[str]] = None,
    errors: Optional[list[str]] = None,
) -> dict[str, Any]:
    """Build the exact public-safe parser response contract."""

    if status not in ALLOWED_QR_PAYLOAD_STATUSES:
        raise ValueError(f"Unsupported QR payload parser status: {status}")

    result = {
        "status": status,
        "warnings": list(warnings or []),
        "errors": list(errors or []),
        **SAFETY_MARKERS,
    }

    return {field: result[field] for field in RESULT_FIELD_CONTRACT}


def _load_payload(payload: str) -> Tuple[Optional[dict[str, Any]], list[str]]:
    if not isinstance(payload, str):
        return None, ["QR payload input must be a JSON string."]

    try:
        decoded = strict_json_loads(payload)
    except CanonicalizationError as exc:
        return None, [f"QR payload is malformed JSON: {exc.reason}."]

    if not isinstance(decoded, dict):
        return None, ["QR payload JSON must be an object."]

    return decoded, []


def _compute_advisory_payload_hash(data: dict[str, Any]) -> str:
    """Compute the versioned advisory QR payload digest without granting trust."""

    return calculate_qr_payload_hash(data)


def _has_valid_record_id(record_id: str) -> bool:
    return bool(RECORD_ID_RE.fullmatch(record_id))


def _has_valid_canonical_url(canonical_url: str) -> bool:
    try:
        parsed = urlparse(canonical_url)
    except ValueError:
        return False
    return parsed.scheme == "https" and bool(parsed.netloc)


def _has_valid_issued_at(issued_at: str) -> bool:
    if not issued_at.endswith("Z"):
        return False
    try:
        datetime.strptime(issued_at, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return False
    return True


def parse_qr_payload(payload: str) -> dict[str, Any]:
    """Parse a local QR JSON payload and return advisory validation output.

    The parser checks shape, required fields, string field types, record_id
    shape, canonical_url presence/shape, issued_at timestamp shape, an advisory
    parser-local payload_hash consistency check, and unknown fields. It does not
    perform cryptographic verification, signature checks, network calls, URL
    fetches, backend/API calls, schema validation, or truth verification.
    """

    data, malformed_errors = _load_payload(payload)
    if malformed_errors:
        return _build_result(MALFORMED_PAYLOAD, errors=malformed_errors)
    assert data is not None

    warnings: list[str] = []
    errors: list[str] = []

    required = set(REQUIRED_FIELDS)
    consumed_optional_fields = (
        {"content", CONTENT_HASH_PROFILE_FIELD} if "content" in data else set()
    )
    unknown_fields = sorted(set(data) - required - consumed_optional_fields)
    for field in unknown_fields:
        warnings.append(f"Unknown QR payload field ignored: {field}.")

    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if missing_fields:
        warnings.append(
            f"Missing required QR payload field(s): {', '.join(missing_fields)}."
        )
        errors.append("QR payload is missing required field(s).")

    for field in REQUIRED_FIELDS:
        if field not in data:
            continue
        if not isinstance(data[field], EXPECTED_FIELD_TYPES[field]):
            errors.append(f"QR payload field {field} must be a string.")
        elif not data[field].strip():
            errors.append(f"QR payload field {field} must not be empty.")

    record_id = data.get("record_id")
    if (
        isinstance(record_id, str)
        and record_id.strip()
        and not _has_valid_record_id(record_id)
    ):
        errors.append(
            "QR payload record_id does not match HC:// record identifier format."
        )

    canonical_url = data.get("canonical_url")
    if (
        isinstance(canonical_url, str)
        and canonical_url.strip()
        and not _has_valid_canonical_url(canonical_url)
    ):
        errors.append("QR payload canonical_url must be an absolute https URL.")

    issued_at = data.get("issued_at")
    if (
        isinstance(issued_at, str)
        and issued_at.strip()
        and not _has_valid_issued_at(issued_at)
    ):
        errors.append(
            "QR payload issued_at must use UTC format YYYY-MM-DDTHH:MM:SSZ."
        )

    if "content" in data:
        try:
            if CONTENT_HASH_PROFILE_FIELD in data:
                actual_content_hash = calculate_content_hash(
                    data["content"], data[CONTENT_HASH_PROFILE_FIELD]
                )
            else:
                actual_content_hash = calculate_content_hash(data["content"])
        except ContentHashError as exc:
            errors.append(
                f"QR payload content hash could not be safely calculated: {exc.reason}."
            )
        else:
            declared_content_hash = data.get("content_hash")
            if (
                isinstance(declared_content_hash, str)
                and declared_content_hash.strip()
                and declared_content_hash.strip().lower() != actual_content_hash.lower()
            ):
                errors.append(
                    "QR payload content_hash does not match actual payload content."
                )

    payload_hash = data.get("payload_hash")
    if isinstance(payload_hash, str) and payload_hash.strip():
        declared_payload_hash = payload_hash.strip().lower()
        try:
            advisory_payload_hash = _compute_advisory_payload_hash(data).lower()
        except ContentHashError as exc:
            errors.append(
                f"QR payload hash could not be safely calculated: {exc.reason}."
            )
        else:
            if declared_payload_hash != advisory_payload_hash:
                errors.append(
                    "QR payload payload_hash does not match advisory canonical payload hash."
                )

    status = INVALID_PAYLOAD if errors else VALID_PAYLOAD
    return _build_result(status, warnings=warnings, errors=errors)


__all__ = [
    "ALLOWED_QR_PAYLOAD_STATUSES",
    "INVALID_PAYLOAD",
    "MALFORMED_PAYLOAD",
    "RESULT_FIELD_CONTRACT",
    "VALID_PAYLOAD",
    "parse_qr_payload",
]
