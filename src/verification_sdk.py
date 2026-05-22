"""HC:// verification sdk core."""

from __future__ import annotations


def build_sdk_response(*, record_id: str, verification_status: str) -> dict:
    return {
        "record_id": record_id.strip(),
        "verification_status": verification_status.strip().upper(),
    }
