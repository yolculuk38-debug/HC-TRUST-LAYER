"""HC:// advisory QR payload inspection utilities.

This module performs local structure, hash, and URL checks.  It does not
cryptographically verify signatures, authenticate issuers, or grant trust.
A QR scan is only a pointer to verification data; it is not proof by itself.
"""

from __future__ import annotations

import hashlib
import json
import re
from enum import Enum
from typing import Any
from urllib.parse import urlparse

TRUSTED_QR_DOMAINS = {"github.com", "yolculuk38-debug.github.io"}
TRUSTED_REPOSITORY_PATH = "HC-TRUST-LAYER"
TRUSTED_PATH_HINTS = ("records", "verify", "docs")
SHA256_RE = re.compile(r"^[a-fA-F0-9]{64}$")


class QRStatus(str, Enum):
    """Machine-readable advisory QR inspection status values."""

    SIGNATURE_UNVERIFIED = "SIGNATURE_UNVERIFIED"
    HASH_MISMATCH = "HASH_MISMATCH"
    INVALID_QR = "INVALID_QR"
    UNSAFE_URL = "UNSAFE_URL"
    UNSIGNED = "UNSIGNED"


REQUIRED_FIELDS = ("record_id", "content_hash", "verification_url", "created_at")


def canonical_json(data: Any) -> str:
    """Return deterministic JSON for QR payload hashing and comparison."""

    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    """Return SHA-256 hex digest for UTF-8 text."""

    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _load_payload(
    payload: str | dict[str, Any],
) -> tuple[dict[str, Any] | None, str | None]:
    if isinstance(payload, dict):
        return payload, None
    if isinstance(payload, str):
        try:
            decoded = json.loads(payload)
        except json.JSONDecodeError as exc:
            return None, f"QR payload is not valid JSON: {exc}"
        if not isinstance(decoded, dict):
            return None, "QR payload JSON must be an object"
        return decoded, None
    return None, "QR payload must be a JSON string or object"


def _safe_verification_url(url: str) -> tuple[bool, str | None]:
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return False, "verification_url must use https"
    if parsed.netloc not in TRUSTED_QR_DOMAINS:
        return False, f"untrusted verification_url domain: {parsed.netloc}"
    has_trusted_repository_path = TRUSTED_REPOSITORY_PATH in parsed.path
    has_trusted_path_hint = any(hint in parsed.path for hint in TRUSTED_PATH_HINTS)
    if not has_trusted_repository_path or not has_trusted_path_hint:
        return False, "verification_url path does not match HC verification paths"
    return True, None


def verify_qr_payload(payload: str | dict[str, Any]) -> dict[str, Any]:
    """Inspect a QR payload without authenticating or trusting it.

    The function name is retained for compatibility.  A successful local
    structure/hash/URL pass still returns ``SIGNATURE_UNVERIFIED`` because this
    module has no key resolution or cryptographic signature verification.

    Expected payload fields:
    - record_id
    - content_hash
    - verification_url
    - created_at
    - signature: optional
    - content: optional; when present, SHA-256 must match content_hash
    """

    data, error = _load_payload(payload)
    if error:
        return _result(QRStatus.INVALID_QR, error)
    assert data is not None

    missing = [field for field in REQUIRED_FIELDS if not data.get(field)]
    if missing:
        return _result(
            QRStatus.INVALID_QR,
            f"missing required field(s): {', '.join(missing)}",
        )

    content_hash = str(data["content_hash"])
    if not SHA256_RE.match(content_hash):
        return _result(
            QRStatus.HASH_MISMATCH,
            "content_hash is not a valid SHA-256 hex digest",
        )

    is_safe_url, url_error = _safe_verification_url(str(data["verification_url"]))
    if not is_safe_url:
        return _result(QRStatus.UNSAFE_URL, str(url_error))

    content = data.get("content")
    if content is not None:
        content_text = content if isinstance(content, str) else canonical_json(content)
        calculated_hash = sha256_text(content_text)
        if calculated_hash.lower() != content_hash.lower():
            return _result(
                QRStatus.HASH_MISMATCH,
                "content hash does not match QR payload content",
                calculated_hash=calculated_hash,
            )

    signature = data.get("signature")
    if signature is None or (isinstance(signature, str) and not signature.strip()):
        return _result(
            QRStatus.UNSIGNED,
            "QR payload passed local structure, hash, and URL checks but is unsigned",
            signature_present=False,
        )
    if not isinstance(signature, str):
        return _result(
            QRStatus.INVALID_QR,
            "signature must be a non-empty string when provided",
            signature_present=True,
        )

    return _result(
        QRStatus.SIGNATURE_UNVERIFIED,
        (
            "QR payload passed local structure, hash, and URL checks; "
            "signature presence was not cryptographically verified"
        ),
        signature_present=True,
    )


def _result(status: QRStatus, reason: str, **details: Any) -> dict[str, Any]:
    """Return the fixed fail-closed advisory boundary for QR inspection."""

    return {
        "status": status.value,
        "trusted": False,
        "signature_verified": False,
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
        "human_review_required": True,
        "reason": reason,
        **details,
    }


__all__ = [
    "TRUSTED_QR_DOMAINS",
    "QRStatus",
    "canonical_json",
    "sha256_text",
    "verify_qr_payload",
]
