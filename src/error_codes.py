"""HC:// error code registry."""

from __future__ import annotations

ERROR_CODES = {
    "HC-001": "INVALID_INPUT",
    "HC-002": "INVALID_HASH",
    "HC-003": "REVOKED_ENTITY",
    "HC-004": "CONSENSUS_FAILURE",
    "HC-005": "UNTRUSTED_NODE",
}


def get_error_name(code: str) -> str:
    return ERROR_CODES.get(code.strip().upper(), "UNKNOWN_ERROR")
