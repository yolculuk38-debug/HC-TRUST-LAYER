"""HC:// consensus to verification status integration."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from consensus_rules import ConsensusStatus
from verification_status_engine import determine_verification_status


INTEGRATION_VERSION = "HC-CONSENSUS-STATUS-INTEGRATION-V1"


def consensus_to_status(
    consensus_result: dict[str, Any],
    *,
    base_signals: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Preserve consensus declarations without inventing successful proof checks."""
    signals = deepcopy(base_signals) if base_signals is not None else {}
    if not isinstance(signals, dict):
        status_result = determine_verification_status(signals)
    else:
        signals["consensus_claim"] = deepcopy(consensus_result)
        status = consensus_result.get("status") if isinstance(consensus_result, dict) else None
        count = consensus_result.get("witness_count", 0) if isinstance(consensus_result, dict) else None
        if (not isinstance(status, str) or status not in {item.value for item in ConsensusStatus}
                or status in {ConsensusStatus.CONFLICT.value, ConsensusStatus.INVALID_INPUT.value}
                or type(count) is not int or count < 0):
            signals["invalid"] = True
        status_result = determine_verification_status(signals)

    return {
        "integration_version": INTEGRATION_VERSION,
        "source_claims": {"consensus_result": deepcopy(consensus_result),
                          "base_signals": deepcopy(base_signals)},
        "status_result": status_result,
        "source_claims_verified": False,
        "trusted": False,
        "verified": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
    }


__all__ = ["INTEGRATION_VERSION", "consensus_to_status"]
