"""Minimal HC:// verification orchestrator compatibility layer.

The orchestrator combines supplied layer outputs into an advisory response for
human-supervised validation. It intentionally avoids final truth claims and does
not modify schemas, records, workflows, policy, federation, signing, or trust
kernel indexes.
"""

from __future__ import annotations

from typing import Any

from verification_api import build_verification_response


ORCHESTRATOR_VERSION = "HC-ORCHESTRATOR-V1"


def _layer_is_true(result: dict[str, Any] | None, *keys: str) -> bool | None:
    if result is None:
        return None
    for key in keys:
        if key in result:
            return result.get(key) is True
    return None


def _trust_score(trust_score_result: dict[str, Any] | None) -> int:
    if not isinstance(trust_score_result, dict):
        return 0
    if "decayed_score" in trust_score_result:
        return trust_score_result.get("decayed_score")
    return trust_score_result.get("trust_score", 0)


def orchestrate_verification(
    record_id: str,
    *,
    hash_result: dict[str, Any] | None = None,
    qr_result: dict[str, Any] | None = None,
    consensus_result: dict[str, Any] | None = None,
    audit_result: dict[str, Any] | None = None,
    signature_result: dict[str, Any] | None = None,
    trust_score_result: dict[str, Any] | None = None,
    checked_at: str | None = None,
) -> dict[str, Any]:
    """Combine verification layers conservatively into an advisory response."""

    signals: dict[str, Any] = {
        "trust_score": _trust_score(trust_score_result),
        "advisory_only": True,
        "human_supervised_validation_required": True,
    }

    layer_values = {
        "hash": _layer_is_true(hash_result, "verified", "trusted"),
        "qr": _layer_is_true(qr_result, "trusted", "verified"),
        "consensus": _layer_is_true(consensus_result, "trusted", "verified"),
        "audit": _layer_is_true(audit_result, "verified", "trusted"),
        "signature": _layer_is_true(signature_result, "verified", "trusted"),
    }
    signals.update({key: value for key, value in layer_values.items() if value is not None})

    response = build_verification_response(record_id, signals, checked_at=checked_at)
    response["orchestrator_version"] = ORCHESTRATOR_VERSION
    response["layer_results"] = {
        "hash_result": hash_result,
        "qr_result": qr_result,
        "consensus_result": consensus_result,
        "audit_result": audit_result,
        "signature_result": signature_result,
        "trust_score_result": trust_score_result,
    }
    return response


__all__ = ["ORCHESTRATOR_VERSION", "orchestrate_verification"]
