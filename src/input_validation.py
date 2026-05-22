"""HC:// input validation core."""

from __future__ import annotations


def require_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


def require_hash(value: str, field_name: str) -> str:
    normalized = require_text(value, field_name)
    if len(normalized) < 32:
        raise ValueError(f"{field_name} is too short to be a trust hash")
    return normalized
