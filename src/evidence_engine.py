"""HC:// multi-source evidence engine."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


EVIDENCE_ENGINE_VERSION = "HC-EVIDENCE-ENGINE-V1"


class EvidenceDecision:
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    INVALID = "INVALID"


REQUIRED_EVIDENCE_SIGNALS = [
    "hash",
    "provenance",
    "witness",
    "registry",
    "federation",
]


def evaluate_evidence_bundle(bundle: dict[str, Any]) -> dict[str, Any]:
    """Inspect declarations; their completeness does not verify evidence."""

    reasons: list[str] = ["source_declarations_not_verified"]
    declaration_score = 0
    valid = isinstance(bundle, dict)
    if valid:
        for signal in [*REQUIRED_EVIDENCE_SIGNALS, "audit", "qr"]:
            if signal in bundle and not isinstance(bundle[signal], bool):
                valid = False
                reasons.append(f"invalid_{signal}_signal")
            if signal in REQUIRED_EVIDENCE_SIGNALS:
                if bundle.get(signal) is True:
                    declaration_score += 20
                else:
                    reasons.append(f"missing_{signal}_signal")
        declaration_score += 10 if bundle.get("audit") is True else 0
        declaration_score += 5 if bundle.get("qr") is True else 0
    else:
        reasons.append("invalid_evidence_bundle")

    return {
        "evidence_engine_version": EVIDENCE_ENGINE_VERSION,
        "decision": EvidenceDecision.REVIEW_REQUIRED if valid else EvidenceDecision.INVALID,
        "evidence_score": 0,
        "declaration_score": declaration_score,
        "source_claims": deepcopy(bundle),
        "source_claims_verified": False,
        "verified": False,
        "trusted": False,
        "content_hash_checked": False,
        "content_hash_valid": None,
        "signatures_verified": False,
        "identity_verified": False,
        "advisory_only": True,
        "public_safe": False,
        "truth_guarantee": False,
        "human_review_required": True,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "EVIDENCE_ENGINE_VERSION",
    "EvidenceDecision",
    "evaluate_evidence_bundle",
]
