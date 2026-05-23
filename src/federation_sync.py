"""HC:// federation sync layer core.

Federation allows multiple HC:// repositories or nodes to exchange
verification metadata without automatic trust.
"""

from __future__ import annotations

from typing import Any, Iterable
from urllib.parse import urlparse


TRUSTED_PROTOCOLS = {"https"}
SUPPORTED_FEDERATION_VERSION = "HC-FEDERATION-V1"

HEALTHY = "healthy"
STALE = "stale"
FAILED = "failed"
RECOVERED = "recovered"


class FederationStatus:
    VERIFIED = "VERIFIED"
    UNTRUSTED = "UNTRUSTED"
    INVALID = "INVALID"
    UNSAFE = "UNSAFE"


REQUIRED_FIELDS = {
    "federation_version",
    "node_id",
    "snapshot_hash",
    "source_url",
    "export_verified",
}


def validate_federation_packet(packet: dict[str, Any]) -> dict[str, Any]:
    """Validate external federation metadata packet."""

    if not isinstance(packet, dict):
        return {
            "status": FederationStatus.INVALID,
            "trusted": False,
            "reason": "packet must be an object",
        }

    missing = REQUIRED_FIELDS.difference(packet)
    if missing:
        return {
            "status": FederationStatus.INVALID,
            "trusted": False,
            "reason": f"missing required field(s): {', '.join(sorted(missing))}",
        }

    if packet["federation_version"] != SUPPORTED_FEDERATION_VERSION:
        return {
            "status": FederationStatus.INVALID,
            "trusted": False,
            "reason": "unsupported federation version",
        }

    parsed = urlparse(str(packet["source_url"]))
    if parsed.scheme not in TRUSTED_PROTOCOLS:
        return {
            "status": FederationStatus.UNSAFE,
            "trusted": False,
            "reason": "unsafe federation protocol",
        }

    export_verified = bool(packet.get("export_verified"))
    snapshot_verified = bool(packet.get("snapshot_verified", False))
    signed = bool(packet.get("signed", False))
    consensus = bool(packet.get("consensus", False))

    trust_signals = sum([
        export_verified,
        snapshot_verified,
        signed,
        consensus,
    ])

    if trust_signals >= 3:
        return {
            "status": FederationStatus.VERIFIED,
            "trusted": True,
            "trust_signals": trust_signals,
            "reason": "federation packet passed verification thresholds",
        }

    return {
        "status": FederationStatus.UNTRUSTED,
        "trusted": False,
        "trust_signals": trust_signals,
        "reason": "external federation packet remains untrusted",
    }


def sync_health(*, failed_attempts: int = 0, last_error: str = "") -> str:
    """Return deterministic federation sync health."""

    failures = max(0, int(failed_attempts))

    if failures >= 3:
        return FAILED

    if failures > 0 or last_error.strip():
        return STALE

    return HEALTHY



def build_sync_state(
    *,
    node_id: str,
    manifest_hash: str,
    verified_at: str,
    trust_score: int = 0,
    failed_attempts: int = 0,
    last_error: str = "",
) -> dict:
    """Create normalized deterministic federation sync state."""

    failures = max(0, int(failed_attempts))

    return {
        "node_id": node_id.strip(),
        "manifest_hash": manifest_hash.strip(),
        "verified_at": verified_at.strip(),
        "trust_score": max(0, min(int(trust_score), 100)),
        "failed_attempts": failures,
        "last_error": last_error.strip(),
        "sync_health": sync_health(
            failed_attempts=failures,
            last_error=last_error,
        ),
    }



def recovered_sync_state(state: dict[str, Any]) -> dict[str, Any]:
    """Normalize recovered federation state after successful sync."""

    normalized = dict(state)
    normalized["failed_attempts"] = 0
    normalized["last_error"] = ""
    normalized["sync_health"] = RECOVERED
    return normalized



def deterministic_sync_snapshot(states: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return replay-safe deterministic federation snapshot ordering."""

    normalized = [
        build_sync_state(
            node_id=str(state.get("node_id", "")),
            manifest_hash=str(state.get("manifest_hash", "")),
            verified_at=str(state.get("verified_at", "")),
            trust_score=int(state.get("trust_score", 0)),
            failed_attempts=int(state.get("failed_attempts", 0)),
            last_error=str(state.get("last_error", "")),
        )
        for state in states
    ]

    return sorted(
        normalized,
        key=lambda item: (
            item["node_id"],
            item["manifest_hash"],
        ),
    )


__all__ = [
    "SUPPORTED_FEDERATION_VERSION",
    "FederationStatus",
    "validate_federation_packet",
    "sync_health",
    "build_sync_state",
    "recovered_sync_state",
    "deterministic_sync_snapshot",
]
