"""HC:// validator API skeleton."""

from __future__ import annotations


def build_validation_request(*, record_id: str, content_hash: str) -> dict:
    return {
        "record_id": record_id.strip(),
        "content_hash": content_hash.strip(),
    }


def build_validation_response(*, record_id: str, valid: bool, reason: str = "") -> dict:
    return {
        "record_id": record_id.strip(),
        "valid": bool(valid),
        "reason": reason.strip(),
    }
