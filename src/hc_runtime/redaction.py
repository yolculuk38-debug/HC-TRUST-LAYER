"""Public-safe redaction helpers for HC:// advisory runtime outputs."""

from __future__ import annotations

import re
from typing import Any

_REDACTION_MARKER = "[REDACTED]"
_SECRET_LIKE_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?(?:-----END [A-Z ]*PRIVATE KEY-----|$)"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"(?i)\b(?:api[_-]?key|token|secret|credential|private[_-]?key)\s*[:=]\s*\S+"),
)


def redact_secret_like_text(value: str) -> str:
    """Return a public-safe string with common secret-like markers removed."""
    redacted = value
    for pattern in _SECRET_LIKE_PATTERNS:
        redacted = pattern.sub(_REDACTION_MARKER, redacted)
    return redacted


def redact_public_payload(payload: Any) -> Any:
    """Recursively redact secret-like string values while preserving payload shape."""
    if isinstance(payload, str):
        return redact_secret_like_text(payload)
    if isinstance(payload, list):
        return [redact_public_payload(item) for item in payload]
    if isinstance(payload, tuple):
        return tuple(redact_public_payload(item) for item in payload)
    if isinstance(payload, dict):
        return {key: redact_public_payload(value) for key, value in payload.items()}
    return payload
