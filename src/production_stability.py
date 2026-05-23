"""HC:// production stabilization helpers.

This module defines small deterministic helpers for stable validator-facing
outputs. It does not change existing public verification behavior.
"""

from __future__ import annotations

from typing import Any, Iterable

STABLE_PROTOCOL_VERSION = "HC-STABLE-V1"


FINAL_STATES = {
    "VERIFIED",
    "UNTRUSTED",
    "INVALID",
    "UNSAFE",
    "REJECTED",
}


def clamp_score(score: int) -> int:
    """Clamp trust score into the stable public range."""

    return max(0, min(int(score), 100))



def normalize_status(status: str) -> str:
    """Normalize trust status for stable public output."""

    normalized = str(status).strip().upper()
    return normalized if normalized else "INVALID"



def stable_trust_result(
    *,
    record_id: str,
    status: str,
    trust_score: int,
    reason: str = "",
    protocol_version: str = STABLE_PROTOCOL_VERSION,
) -> dict[str, Any]:
    """Build deterministic trust result payload for public consumers."""

    normalized_status = normalize_status(status)

    return {
        "protocol_version": protocol_version,
        "record_id": record_id.strip(),
        "status": normalized_status,
        "final": normalized_status in FINAL_STATES,
        "trust_score": clamp_score(trust_score),
        "reason": reason.strip(),
    }



def stable_output_snapshot(results: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return deterministic ordering for public trust outputs."""

    normalized = [
        stable_trust_result(
            record_id=str(result.get("record_id", "")),
            status=str(result.get("status", "INVALID")),
            trust_score=int(result.get("trust_score", 0)),
            reason=str(result.get("reason", "")),
            protocol_version=str(result.get("protocol_version", STABLE_PROTOCOL_VERSION)),
        )
        for result in results
    ]

    return sorted(
        normalized,
        key=lambda item: (
            item["record_id"],
            item["status"],
            item["trust_score"],
        ),
    )



def compatibility_contract() -> dict[str, Any]:
    """Describe stable production compatibility guarantees."""

    return {
        "protocol_version": STABLE_PROTOCOL_VERSION,
        "deterministic_outputs": True,
        "score_range": [0, 100],
        "final_states": sorted(FINAL_STATES),
        "network_calls": False,
    }


__all__ = [
    "STABLE_PROTOCOL_VERSION",
    "FINAL_STATES",
    "clamp_score",
    "normalize_status",
    "stable_trust_result",
    "stable_output_snapshot",
    "compatibility_contract",
]
