"""HC:// public validator response core."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

PUBLIC_VALIDATOR_API_VERSION = "HC-PUBLIC-VALIDATOR-API-V1"

VALIDATOR_STATUS_VERIFIED = "VERIFIED"
VALIDATOR_STATUS_WARNING = "WARNING"
VALIDATOR_STATUS_FAILED = "FAILED"


def _utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _status_from_checks(checks: dict[str, bool]) -> str:
    if not checks:
        return VALIDATOR_STATUS_WARNING

    passed = sum(1 for value in checks.values() if value)

    if passed == len(checks):
        return VALIDATOR_STATUS_VERIFIED

    if passed == 0:
        return VALIDATOR_STATUS_FAILED

    return VALIDATOR_STATUS_WARNING



def build_validator_response(
    *,
    record_id: str,
    checks: dict[str, bool],
    trust_score: dict[str, Any] | None = None,
    snapshot: dict[str, Any] | None = None,
    witness_signatures: list[dict[str, Any]] | None = None,
    warnings: list[str] | None = None,
) -> dict[str, Any]:
    status = _status_from_checks(checks)

    return {
        "public_validator_api_version": PUBLIC_VALIDATOR_API_VERSION,
        "record_id": record_id.strip(),
        "status": status,
        "checked_at": _utc_now(),
        "checks": checks,
        "trust_score": trust_score or {},
        "snapshot": snapshot or {},
        "witness_signatures": witness_signatures or [],
        "warnings": warnings or [],
    }



def require_verified_response(response: dict[str, Any]) -> bool:
    if response.get("status") != VALIDATOR_STATUS_VERIFIED:
        raise ValueError("validator response is not fully verified")

    return True


__all__ = [
    "PUBLIC_VALIDATOR_API_VERSION",
    "VALIDATOR_STATUS_FAILED",
    "VALIDATOR_STATUS_VERIFIED",
    "VALIDATOR_STATUS_WARNING",
    "build_validator_response",
    "require_verified_response",
]
