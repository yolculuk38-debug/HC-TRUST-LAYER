"""Advisory QR spoof-protection warning helpers for HC:// runtime flow."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any
from urllib.parse import urlparse

TRUSTED_QR_DOMAINS = {"github.com", "yolculuk38-debug.github.io"}
TRUSTED_PATH_HINTS = ("HC-TRUST-LAYER", "records", "verify", "docs")
CURRENT_QR_VERSION = "v1"


class QRRiskLevel(StrEnum):
    """Deterministic QR spoof risk bands for advisory runtime routing."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    INCIDENT = "INCIDENT"


@dataclass(frozen=True, slots=True)
class QRSpoofProtectionResult:
    """Public-safe advisory QR inspection output."""

    warnings: list[str]
    replay_warning: bool = False
    stale_warning: bool = False
    structured_payload: bool = False
    risk_level: QRRiskLevel = QRRiskLevel.LOW
    risk_reasons: list[str] = field(default_factory=list)
    risk_group_keys: list[str] = field(default_factory=list)


@dataclass(slots=True)
class _RiskSignals:
    medium: list[str] = field(default_factory=list)
    high: list[str] = field(default_factory=list)
    group_keys: list[str] = field(default_factory=list)

    def add_medium(self, reason: str) -> None:
        if reason not in self.medium:
            self.medium.append(reason)

    def add_high(self, reason: str, group_key: str | None = None) -> None:
        if reason not in self.high:
            self.high.append(reason)
        if group_key and group_key not in self.group_keys:
            self.group_keys.append(group_key)

    def level(self) -> QRRiskLevel:
        if self.high:
            return QRRiskLevel.HIGH
        if self.medium:
            return QRRiskLevel.MEDIUM
        return QRRiskLevel.LOW

    def reasons(self) -> list[str]:
        return [*self.high, *self.medium]


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


def _url_warning(verification_url: object, signals: _RiskSignals) -> str | None:
    if not isinstance(verification_url, str) or not verification_url.strip():
        signals.add_high("verification_url_missing", "url:missing")
        return "Canonical verification_url is missing from structured QR payload."

    parsed = urlparse(verification_url)
    if parsed.scheme != "https":
        signals.add_high("non_canonical_scheme", f"scheme:{parsed.scheme or 'missing'}")
        return "Non-canonical QR verification_url scheme detected; HC:// runtime did not silently trust it."
    if parsed.netloc not in TRUSTED_QR_DOMAINS:
        signals.add_high("non_canonical_domain", f"domain:{parsed.netloc or 'missing'}")
        return "Non-canonical QR verification_url domain detected; HC:// runtime did not silently trust it."
    if not any(hint in parsed.path for hint in TRUSTED_PATH_HINTS):
        signals.add_high("non_canonical_path", f"path:{parsed.path or 'missing'}")
        return "Non-canonical QR verification_url path detected; HC:// runtime did not silently trust it."
    return None


def _payload_without_hash(payload: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in payload.items() if key != "payload_hash"}


def _record_family(record_id: str) -> str:
    return record_id.rsplit("-", 1)[0] if "-" in record_id else record_id


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
    signals = _RiskSignals()

    if replay_warning:
        signals.add_medium("replay_marker_visible")
    if stale_warning:
        signals.add_medium("stale_marker_visible")
        warnings.append("Stale QR marker remains visible in advisory runtime response.")

    payload = _load_structured_payload(qr_input)
    if payload is None:
        return QRSpoofProtectionResult(
            warnings=warnings,
            replay_warning=replay_warning,
            stale_warning=stale_warning,
            structured_payload=False,
            risk_level=signals.level(),
            risk_reasons=signals.reasons(),
            risk_group_keys=signals.group_keys,
        )

    payload_record_id = payload.get("record_id")
    if not isinstance(payload_record_id, str) or not payload_record_id.strip():
        signals.add_high("record_id_missing", f"record_family:{_record_family(record_id)}")
        warnings.append("Structured QR payload is missing record_id; advisory runtime did not apply hidden fallback.")
    elif payload_record_id != record_id:
        signals.add_high("record_id_mismatch", f"record_family:{_record_family(record_id)}")
        warnings.append("Structured QR record_id mismatch remains visible in advisory runtime response.")

    url_warning = _url_warning(payload.get("verification_url"), signals)
    if url_warning is not None:
        warnings.append(url_warning)

    payload_hash = payload.get("payload_hash")
    if not isinstance(payload_hash, str) or not payload_hash.strip():
        signals.add_medium("payload_hash_missing")
        warnings.append("Structured QR payload_hash is missing; payload integrity remains unresolved.")
    else:
        calculated_payload_hash = _sha256_text(_canonical_json(_payload_without_hash(payload)))
        if calculated_payload_hash.lower() != payload_hash.lower():
            signals.add_high("payload_hash_mismatch", f"payload_pattern:{_record_family(record_id)}")
            warnings.append("Structured QR payload_hash mismatch remains explicit in advisory runtime response.")

    content_hash = payload.get("content_hash")
    content = payload.get("content")
    if isinstance(content_hash, str) and content_hash.strip() and "content" in payload:
        content_text = content if isinstance(content, str) else _canonical_json(content)
        if _sha256_text(content_text).lower() != content_hash.lower():
            signals.add_high("content_hash_mismatch", f"payload_pattern:{_record_family(record_id)}")
            warnings.append("Structured QR content_hash mismatch remains explicit in advisory runtime response.")
    elif not isinstance(content_hash, str) or not content_hash.strip():
        signals.add_medium("content_hash_missing")
        warnings.append("Structured QR content_hash is missing; content integrity remains unresolved.")

    if not payload.get("signed_payload_ref"):
        signals.add_medium("signed_payload_ref_missing")
        warnings.append("Signed payload reference is missing from structured QR payload.")

    qr_version = payload.get("qr_version")
    if qr_version not in (None, CURRENT_QR_VERSION):
        stale_warning = True
        signals.add_medium("stale_qr_version")
        warnings.append("Stale QR version marker remains visible in advisory runtime response.")

    if payload.get("replay_marker") is True:
        replay_warning = True
        signals.add_medium("replay_marker_visible")
        warnings.append("Replay marker remains visible in advisory runtime response.")

    if payload.get("stale") is True:
        stale_warning = True
        signals.add_medium("stale_qr_payload")
        warnings.append("Stale QR payload flag remains visible in advisory runtime response.")

    return QRSpoofProtectionResult(
        warnings=warnings,
        replay_warning=replay_warning,
        stale_warning=stale_warning,
        structured_payload=True,
        risk_level=signals.level(),
        risk_reasons=signals.reasons(),
        risk_group_keys=signals.group_keys,
    )
