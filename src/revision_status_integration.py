"""HC:// revision chain to status engine integration."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from revision_chain import RevisionChainStatus, verify_revision_chain
from verification_status_engine import determine_verification_status


INTEGRATION_VERSION = "HC-REVISION-STATUS-INTEGRATION-V1"


def verify_revision_status(
    revisions: list[dict[str, Any]],
    *,
    base_signals: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Verify revision chain and map result into centralized status engine."""

    chain_result = verify_revision_chain(revisions)
    signals = deepcopy(base_signals) if base_signals is not None else {}
    if isinstance(signals, dict) and chain_result.get("status") != RevisionChainStatus.VERIFIED:
        signals["invalid"] = True
    # A valid local revision hash chain does not authenticate provenance or content.

    status_result = determine_verification_status(signals)

    return {
        "integration_version": INTEGRATION_VERSION,
        "chain_result": chain_result,
        "status_result": status_result,
        "trusted": False,
        "verified": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
    }


__all__ = ["INTEGRATION_VERSION", "verify_revision_status"]
