"""HC:// trust engine expansion."""

from __future__ import annotations


def weighted_score(*, base_score: int, witness_bonus: int, risk_penalty: int) -> int:
    score = int(base_score) + int(witness_bonus) - int(risk_penalty)
    return max(0, min(score, 100))


def build_trust_result(*, record_id: str, score: int) -> dict:
    if score >= 85:
        level = "HIGH"
    elif score >= 60:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "record_id": record_id.strip(),
        "score": max(0, min(int(score), 100)),
        "level": level,
    }
