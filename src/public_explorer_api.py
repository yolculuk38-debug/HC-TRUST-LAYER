"""HC:// public explorer API runtime layer.

All explorer routes are intentionally marked experimental/non-production.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

EXPLORER_RUNTIME_VERSION = "HC-TRUST-LAYER-EXPLORER-RUNTIME-V1-EXPERIMENTAL"


def build_explorer_record(*, record_id: str, status: str, trust_score: int) -> dict:
    return {
        "record_id": record_id.strip(),
        "status": status.strip().upper(),
        "trust_score": max(0, min(int(trust_score), 100)),
    }


def get_explorer_record_lookup(
    *,
    record_id: str,
    record_store: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Experimental explorer lookup for a public record ID."""

    normalized_record_id = (record_id or "").strip()
    store = record_store or {}
    raw_record = store.get(normalized_record_id)

    if raw_record is None:
        payload = {
            "record_id": normalized_record_id,
            "found": False,
            "status": "UNAVAILABLE",
            "trust_score": 0,
            "message": "record not found in experimental explorer runtime",
        }
    else:
        payload = {
            "record_id": normalized_record_id,
            "found": True,
            "status": str(raw_record.get("status", "UNAVAILABLE")).upper(),
            "trust_score": max(0, min(int(raw_record.get("trust_score", 0) or 0), 100)),
            "verification_level": raw_record.get("verification_level"),
            "last_updated": raw_record.get("last_updated"),
        }

    return _public_safe_response(route="record_lookup", payload=payload)


def get_explorer_receipt_lookup(
    *,
    receipt_id: str,
    receipt_store: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Experimental explorer lookup for verification receipts."""

    normalized_receipt_id = (receipt_id or "").strip()
    store = receipt_store or {}
    raw_receipt = store.get(normalized_receipt_id)

    if raw_receipt is None:
        payload = {
            "receipt_id": normalized_receipt_id,
            "found": False,
            "verification_state": "UNAVAILABLE",
            "message": "verification receipt not found in experimental explorer runtime",
        }
    else:
        payload = {
            "receipt_id": normalized_receipt_id,
            "found": True,
            "verification_state": str(raw_receipt.get("verification_state", "UNAVAILABLE")).upper(),
            "verification_timestamp": raw_receipt.get("verification_timestamp"),
            "federation_confirmations": int(raw_receipt.get("federation_confirmations", 0) or 0),
            "witness_summary": deepcopy(raw_receipt.get("witness_summary", {})),
            "integrity_summary": deepcopy(raw_receipt.get("integrity_summary", {})),
            "revision_summary": deepcopy(raw_receipt.get("revision_summary", {})),
        }

    return _public_safe_response(route="receipt_lookup", payload=payload)


def get_federation_status_summary(
    *,
    nodes: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Experimental explorer federation status summary."""

    normalized_nodes = nodes or []
    total = len(normalized_nodes)
    online = sum(1 for node in normalized_nodes if str(node.get("state", "")).upper() == "ONLINE")
    degraded = sum(1 for node in normalized_nodes if str(node.get("state", "")).upper() == "DEGRADED")
    offline = sum(1 for node in normalized_nodes if str(node.get("state", "")).upper() == "OFFLINE")

    payload = {
        "network": "HC-TRUST-LAYER-FEDERATION",
        "total_nodes": total,
        "online_nodes": online,
        "degraded_nodes": degraded,
        "offline_nodes": offline,
        "sync_state": "experimental",
    }
    return _public_safe_response(route="federation_status_summary", payload=payload)


def _public_safe_response(*, route: str, payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "runtime": "explorer",
        "status": "experimental",
        "non_production": True,
        "runtime_version": EXPLORER_RUNTIME_VERSION,
        "route": route,
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "payload": payload,
    }


__all__ = [
    "EXPLORER_RUNTIME_VERSION",
    "build_explorer_record",
    "get_explorer_record_lookup",
    "get_explorer_receipt_lookup",
    "get_federation_status_summary",
]
