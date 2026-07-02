"""Compatibility wrapper for HC:// runtime redaction helpers."""

from __future__ import annotations

from hc_runtime.contracts.redaction import redact_public_payload, redact_secret_like_text

__all__ = ["redact_public_payload", "redact_secret_like_text"]
