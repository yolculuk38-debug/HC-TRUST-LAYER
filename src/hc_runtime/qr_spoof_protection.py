"""Advisory QR spoof-protection warning helpers for HC:// runtime flow."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

TRUSTED_QR_DOMAINS = {"github.com", "yolculuk38-debug.github.io"}
TRUSTED_PATH_HINTS = ("HC-TRUST-LAYER", "Insanlik-Zinciri", "records", "verify", "docs")
CURRENT_QR_VERSION = "v1"


@dataclass(frozen=True, slots=True)
class QRSpoofProtectionResult:
    """Public-safe advisory QR inspection output."""

    warnings: list[str]
    replay_warning: bool = False
    stale_warning: bool = False
    structured_payload: bool = False


def _canonical_json(data: Any) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _load_structured_payload(qr_input: str) -> dict[str, Any] | None:
    stripped = qr_input.strip()
    if not stripped.startswith("{"):
        return None
    try:
        decoded = json.loads(stripped)
    except json.JSONDecodeError:
        return None
    return decoded if isinstance(decoded, dict) else None


def _url_warning(verification_url: object) -> str | None:
    if not isinstance(verification_url, str) or not verification_url.strip():
        return "Canonical verification_url is missing from structured QR payload."

    parsed = urlparse(verification_url)
    if parsed.scheme != "https":
        return "Non-canonical QR verification_url scheme detected; HC:// runtime did not silently trust it."
    if parsed.netloc not in TRUSTED_QR_DOMAINS:
        return "Non-canonical QR verification_url domain detected; HC:// runtime did not silently trust it."
    if not any(hint in parsed.path for hint in TRUSTED_PATH_HINTS):
        return "Non-canonical QR verification_url path detected; HC:// runtime did not silently trust it."
    return None


def _payload_without_hash(payload: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in payload.items() if key != "payload_hash"}


def inspect_qr_spoof_protection(*, record_id: str, qr_input: str) -> QRSpoofProtectionResult:
    """Inspect QR input and return deterministic public-safe spoof warnings.

    The helper never grants trust and never mutates canonical records. It only
    exposes advisory warnings for structured QR payloads or visible replay/stale
    markers so the runtime response remains transparent and public-safe.
    """

    lowered = qr_input.lower()
    replay_warning = "replay" in lowered
    stale_warning = "stale" in lowered
    warnings: list[str] = []

    if stale_warning:
        warnings.append("Stale QR marker remains visible in advisory runtime response.")

    payload = _load_structured_payload(qr_input)
    if payload is None:
        return QRSpoofProtectionResult(
            warnings=warnings,
            replay_warning=replay_warning,
            stale_warning=stale_warning,
            structured_payload=False,
        )

    payload_record_id = payload.get("record_id")
    if not isinstance(payload_record_id, str) or not payload_record_id.strip():
        warnings.append("Structured QR payload is missing record_id; advisory runtime did not apply hidden fallback.")
    elif payload_record_id != record_id:
        warnings.append("Structured QR record_id mismatch remains visible in advisory runtime response.")

    url_warning = _url_warning(payload.get("verification_url"))
    if url_warning is not None:
        warnings.append(url_warning)

    payload_hash = payload.get("payload_hash")
    if not isinstance(payload_hash, str) or not payload_hash.strip():
        warnings.append("Structured QR payload_hash is missing; payload integrity remains unresolved.")
    else:
        calculated_payload_hash = _sha256_text(_canonical_json(_payload_without_hash(payload)))
        if calculated_payload_hash.lower() != payload_hash.lower():
            warnings.append("Structured QR payload_hash mismatch remains explicit in advisory runtime response.")

    content_hash = payload.get("content_hash")
    content = payload.get("content")
    if isinstance(content_hash, str) and content_hash.strip() and "content" in payload:
        content_text = content if isinstance(content, str) else _canonical_json(content)
        if _sha256_text(content_text).lower() != content_hash.lower():
            warnings.append("Structured QR content_hash mismatch remains explicit in advisory runtime response.")
    elif not isinstance(content_hash, str) or not content_hash.strip():
        warnings.append("Structured QR content_hash is missing; content integrity remains unresolved.")

    if not payload.get("signed_payload_ref"):
        warnings.append("Signed payload reference is missing from structured QR payload.")

    qr_version = payload.get("qr_version")
    if qr_version not in (None, CURRENT_QR_VERSION):
        stale_warning = True
        warnings.append("Stale QR version marker remains visible in advisory runtime response.")

    if payload.get("replay_marker") is True:
        replay_warning = True
        warnings.append("Replay marker remains visible in advisory runtime response.")

    if payload.get("stale") is True:
        stale_warning = True
        warnings.append("Stale QR payload flag remains visible in advisory runtime response.")

    return QRSpoofProtectionResult(
        warnings=warnings,
        replay_warning=replay_warning,
        stale_warning=stale_warning,
        structured_payload=True,
    )
