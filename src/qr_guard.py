"""HC:// QR verification hardening."""

from __future__ import annotations

TRUSTED_PREFIXES = {
    "hc://",
    "https://hc-trust-layer.org/verify/",
}


def is_trusted_payload(payload: str) -> bool:
    normalized = payload.strip().lower()
    return any(normalized.startswith(prefix) for prefix in TRUSTED_PREFIXES)


def detect_qr_risk(payload: str) -> str:
    return "LOW" if is_trusted_payload(payload) else "HIGH"


def build_qr_record(*, payload: str) -> dict:
    return {
        "payload": payload.strip(),
        "trusted": is_trusted_payload(payload),
        "risk_level": detect_qr_risk(payload),
    }
