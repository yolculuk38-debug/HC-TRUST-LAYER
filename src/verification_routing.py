"""HC:// public verification routing layer.

Routes verification requests into deterministic validator paths.
This module does not perform network activity.
"""

from __future__ import annotations

from typing import Any, Iterable

DEFAULT_ROUTE = "local-validator"
FEDERATION_ROUTE = "federation-validator"
HIGH_TRUST_ROUTE = "high-trust-validator"



def normalize_request(request: dict[str, Any]) -> dict[str, Any]:
    """Normalize public verification request."""

    return {
        "record_id": str(request.get("record_id", "")).strip(),
        "trust_score": max(0, min(int(request.get("trust_score", 0)), 100)),
        "federated": bool(request.get("federated", False)),
        "priority": str(request.get("priority", "normal")).strip().lower(),
    }



def select_route(request: dict[str, Any]) -> str:
    """Select deterministic verification route."""

    normalized = normalize_request(request)

    if normalized["trust_score"] >= 90:
        return HIGH_TRUST_ROUTE

    if normalized["federated"]:
        return FEDERATION_ROUTE

    return DEFAULT_ROUTE



def build_route_result(request: dict[str, Any]) -> dict[str, Any]:
    """Build deterministic verification routing result."""

    normalized = normalize_request(request)

    return {
        "record_id": normalized["record_id"],
        "route": select_route(normalized),
        "priority": normalized["priority"],
        "federated": normalized["federated"],
        "trust_score": normalized["trust_score"],
    }



def stable_route_snapshot(requests: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return deterministic route ordering for audit visibility."""

    routes = [build_route_result(request) for request in requests]

    return sorted(
        routes,
        key=lambda item: (
            item["route"],
            item["record_id"],
            item["trust_score"],
        ),
    )


__all__ = [
    "DEFAULT_ROUTE",
    "FEDERATION_ROUTE",
    "HIGH_TRUST_ROUTE",
    "normalize_request",
    "select_route",
    "build_route_result",
    "stable_route_snapshot",
]
