"""HC:// public validator API spec."""

from __future__ import annotations

from typing import Any


PUBLIC_VALIDATOR_API_VERSION = "HC-PUBLIC-VALIDATOR-API-V1"


def build_validator_api_request(
    *,
    request_id: str,
    portable_package: dict[str, Any],
    client_type: str = "SDK",
) -> dict[str, Any]:
    """Build a public validator API request payload."""

    return {
        "api_version": PUBLIC_VALIDATOR_API_VERSION,
        "request_id": request_id,
        "client_type": client_type,
        "portable_package": portable_package,
    }


def build_validator_api_response(
    *,
    request_id: str,
    decision: str,
    trusted: bool,
    trust_score: int | None = None,
    risk_level: str | None = None,
    reasons: list[str] | None = None,
) -> dict[str, Any]:
    """Build a public validator API response payload."""

    return {
        "api_version": PUBLIC_VALIDATOR_API_VERSION,
        "request_id": request_id,
        "decision": decision,
        "trusted": bool(trusted),
        "trust_score": trust_score,
        "risk_level": risk_level,
        "reasons": sorted(set(reasons or [])),
        "explainable": True,
        "portable": True,
    }


def validate_validator_api_request(request: dict[str, Any]) -> dict[str, Any]:
    """Validate public validator API request shape."""

    if not isinstance(request, dict):
        return _result(False, ["invalid_api_request_structure"])

    reasons: list[str] = []

    for field in ["api_version", "request_id", "client_type", "portable_package"]:
        if field not in request:
            reasons.append(f"missing_{field}")

    if request.get("api_version") != PUBLIC_VALIDATOR_API_VERSION:
        reasons.append("unsupported_api_version")

    return _result(not reasons, reasons)


def _result(valid: bool, reasons: list[str]) -> dict[str, Any]:
    return {
        "api_version": PUBLIC_VALIDATOR_API_VERSION,
        "valid": valid,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "PUBLIC_VALIDATOR_API_VERSION",
    "build_validator_api_request",
    "build_validator_api_response",
    "validate_validator_api_request",
]
