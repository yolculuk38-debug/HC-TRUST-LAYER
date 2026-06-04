"""HC:// QR anti-spoof verification layer."""

from __future__ import annotations

import hashlib
import hmac
import json
from typing import Any


QR_SECURITY_VERSION = "HC-QR-SECURITY-V1"
ALLOWED_QR_DOMAINS = {
    "github.com",
    "yolculuk38-debug.github.io",
}



def canonical_payload(payload: dict[str, Any]) -> str:
    """Return deterministic payload serialization."""

    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)



def sign_qr_payload(payload: dict[str, Any], secret_key: str) -> str:
    """Generate deterministic HMAC signature for QR payload."""

    serialized = canonical_payload(payload).encode("utf-8")
    return hmac.new(
        secret_key.encode("utf-8"),
        serialized,
        hashlib.sha256,
    ).hexdigest()



def verify_qr_signature(
    *,
    payload: dict[str, Any],
    signature: str,
    secret_key: str,
) -> bool:
    """Verify QR payload signature integrity."""

    expected_signature = sign_qr_payload(payload, secret_key)

    if not hmac.compare_digest(expected_signature, signature):
        raise ValueError("invalid qr signature")

    return True



def verify_qr_domain(domain: str) -> bool:
    """Verify trusted QR verification domain."""

    normalized = domain.strip().lower()

    if normalized not in ALLOWED_QR_DOMAINS:
        raise ValueError("untrusted qr verification domain")

    return True



def build_secure_qr_payload(
    *,
    record_id: str,
    verification_url: str,
    snapshot_hash: str,
) -> dict[str, Any]:
    """Create normalized QR verification payload."""

    return {
        "qr_security_version": QR_SECURITY_VERSION,
        "record_id": record_id.strip(),
        "verification_url": verification_url.strip(),
        "snapshot_hash": snapshot_hash.strip(),
    }


__all__ = [
    "ALLOWED_QR_DOMAINS",
    "QR_SECURITY_VERSION",
    "build_secure_qr_payload",
    "canonical_payload",
    "sign_qr_payload",
    "verify_qr_domain",
    "verify_qr_signature",
]
