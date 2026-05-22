"""HC:// mobile verifier bridge."""

from __future__ import annotations


def build_mobile_verifier_payload(*, qr_id: str, verification_status: str) -> dict:
    return {
        "qr_id": qr_id.strip(),
        "verification_status": verification_status.strip().upper(),
    }
