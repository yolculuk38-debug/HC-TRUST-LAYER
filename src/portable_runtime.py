"""HC:// portable verifier runtime.

Provides deterministic offline verification runtime helpers and portable
cross-platform verification preparation.
"""

from __future__ import annotations

from typing import Any, Iterable

RUNTIME_VERSION = "HC-RUNTIME-V1"



def runtime_context(*, offline: bool = True, portable: bool = True) -> dict[str, Any]:
    """Build portable runtime context."""

    return {
        "runtime_version": RUNTIME_VERSION,
        "offline": bool(offline),
        "portable": bool(portable),
    }



def verify_runtime_record(record: dict[str, Any]) -> dict[str, Any]:
    """Normalize portable runtime verification result."""

    verified = bool(record.get("verified", False))

    return {
        "record_id": str(record.get("record_id", "")).strip(),
        "verified": verified,
        "status": "VERIFIED" if verified else "REVIEW",
    }



def portable_snapshot(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return deterministic runtime verification snapshot."""

    normalized = [verify_runtime_record(record) for record in records]

    return sorted(
        normalized,
        key=lambda item: (
            item["status"],
            item["record_id"],
        ),
    )



def external_node_ready(node: dict[str, Any]) -> bool:
    """Check external federation node runtime readiness."""

    return bool(node.get("active", False)) and bool(node.get("portable_support", False))


__all__ = [
    "RUNTIME_VERSION",
    "runtime_context",
    "verify_runtime_record",
    "portable_snapshot",
    "external_node_ready",
]
