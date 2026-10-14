"""HC:// multi-witness consensus rules.

Consensus is not automatic truth. It is a structured verification signal
computed from unauthenticated declarations; distinct IDs do not prove independence.
"""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
from enum import Enum
from typing import Any


class ConsensusStatus(str, Enum):
    CONSENSUS_REACHED = "CONSENSUS_REACHED"
    PARTIAL_CONSENSUS = "PARTIAL_CONSENSUS"
    CONFLICT = "CONFLICT"
    INSUFFICIENT_WITNESSES = "INSUFFICIENT_WITNESSES"
    INVALID_INPUT = "INVALID_INPUT"


VALID_VERDICTS = {"PASS", "FAIL", "ABSTAIN"}
DEFAULT_MIN_WITNESSES = 3
DEFAULT_THRESHOLD = 0.67


def _normalize_witness(witness: dict[str, Any]) -> dict[str, Any] | None:
    witness_id = witness.get("witness_id") or witness.get("id")
    witness_type = witness.get("witness_type") or witness.get("type") or "unknown"
    verdict = str(witness.get("verdict", "")).upper()
    content_hash = witness.get("content_hash")

    if (not isinstance(witness_id, str) or not witness_id.strip()
            or verdict not in VALID_VERDICTS
            or (content_hash is not None and not isinstance(content_hash, str))):
        return None

    return {
        "witness_id": str(witness_id),
        "witness_type": str(witness_type),
        "verdict": verdict,
        "content_hash": content_hash,
    }


def _evaluate_declarations(
    witnesses: list[dict[str, Any]],
    *,
    min_witnesses: int = DEFAULT_MIN_WITNESSES,
    threshold: float = DEFAULT_THRESHOLD,
) -> dict[str, Any]:
    """Evaluate witness consensus for a record.

    Rules:
    - Duplicate witness IDs are ignored after first valid entry.
    - ABSTAIN does not count toward PASS/FAIL agreement.
    - Conflicting content hashes reduce consensus confidence.
    - Consensus requires minimum witnesses and threshold agreement.
    """

    if not isinstance(witnesses, list):
        return {"status": ConsensusStatus.INVALID_INPUT.value, "trusted": False, "reason": "witnesses must be a list"}
    if (type(min_witnesses) is not int or min_witnesses < 1
            or type(threshold) not in (int, float) or not (0 < threshold <= 1)):
        return {"status": ConsensusStatus.INVALID_INPUT.value, "trusted": False, "reason": "invalid consensus parameters"}

    normalized: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for witness in witnesses:
        if not isinstance(witness, dict):
            continue
        item = _normalize_witness(witness)
        if item is None or item["witness_id"] in seen_ids:
            continue
        seen_ids.add(item["witness_id"])
        normalized.append(item)

    if len(normalized) < min_witnesses:
        return {
            "status": ConsensusStatus.INSUFFICIENT_WITNESSES.value,
            "trusted": False,
            "witness_count": len(normalized),
            "required_witnesses": min_witnesses,
            "reason": "not enough distinct declared witness IDs",
        }

    active = [w for w in normalized if w["verdict"] != "ABSTAIN"]
    if not active:
        return {"status": ConsensusStatus.CONFLICT.value, "trusted": False, "reason": "all witnesses abstained"}

    verdict_counts = Counter(w["verdict"] for w in active)
    top_verdict, top_count = verdict_counts.most_common(1)[0]
    agreement_ratio = top_count / len(active)

    hashes = {w["content_hash"] for w in active if w.get("content_hash")}
    hash_conflict = len(hashes) > 1

    result = {
        "trusted": False,
        "witness_count": len(normalized),
        "active_witness_count": len(active),
        "top_verdict": top_verdict,
        "agreement_ratio": round(agreement_ratio, 4),
        "threshold": threshold,
        "hash_conflict": hash_conflict,
        "verdict_counts": dict(verdict_counts),
        "consensus_reached": False,
    }

    if hash_conflict:
        result.update({"status": ConsensusStatus.CONFLICT.value, "reason": "witnesses disagree on content_hash"})
        return result

    if top_verdict == "PASS" and agreement_ratio >= threshold:
        result.update({
            "status": ConsensusStatus.CONSENSUS_REACHED.value,
            "trusted": False,
            "consensus_reached": True,
            "reason": "unauthenticated PASS declarations meet the agreement threshold",
        })
        return result

    if agreement_ratio >= threshold:
        result.update({"status": ConsensusStatus.CONFLICT.value, "reason": f"{top_verdict} consensus reached"})
        return result

    result.update({"status": ConsensusStatus.PARTIAL_CONSENSUS.value, "reason": "agreement below threshold"})
    return result


def evaluate_consensus(
    witnesses: list[dict[str, Any]],
    *,
    min_witnesses: int = DEFAULT_MIN_WITNESSES,
    threshold: float = DEFAULT_THRESHOLD,
) -> dict[str, Any]:
    """Count declared agreement without authenticating witnesses or their hashes."""
    result = _evaluate_declarations(witnesses, min_witnesses=min_witnesses, threshold=threshold)
    result.update({
        "source_claims": {"witnesses": deepcopy(witnesses)},
        "source_claims_verified": False,
        "trusted": False,
        "verified": False,
        "content_hash_checked": False,
        "content_hash_valid": None,
        "signatures_verified": False,
        "identity_verified": False,
        "witness_independence_verified": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
    })
    return result


__all__ = ["ConsensusStatus", "evaluate_consensus"]
