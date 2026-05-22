"""HC:// multi-source evidence engine."""

from __future__ import annotations

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
    """Evaluate multi-source HC:// evidence bundle."""

    if not isinstance(bundle, dict):
        return _result(EvidenceDecision.INVALID, 0, ["invalid_evidence_bundle"])

    score = 0
    reasons: list[str] = []

    for signal in REQUIRED_EVIDENCE_SIGNALS:
        if bundle.get(signal) is True:
            score += 20
        else:
            reasons.append(f"missing_{signal}_signal")

    if bundle.get("audit") is True:
        score += 10

    if bundle.get("qr") is True:
        score += 5

    if score >= 90:
        return _result(EvidenceDecision.VERIFIED, score, reasons)

    if score >= 60:
        return _result(EvidenceDecision.PARTIAL, score, reasons)

    if score >= 30:
        return _result(EvidenceDecision.REVIEW_REQUIRED, score, reasons)

    return _result(EvidenceDecision.INVALID, score, reasons)



def _result(decision: str, score: int, reasons: list[str]) -> dict[str, Any]:
    return {
        "evidence_engine_version": EVIDENCE_ENGINE_VERSION,
        "decision": decision,
        "evidence_score": score,
        "reasons": sorted(set(reasons)),
    }


__all__ = [
    "EVIDENCE_ENGINE_VERSION",
    "EvidenceDecision",
    "evaluate_evidence_bundle",
]
