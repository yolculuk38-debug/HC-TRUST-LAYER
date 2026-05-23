"""HC:// reputation layer core."""

from __future__ import annotations

LEVEL_WEIGHTS = {
    "LOW": 10,
    "MEDIUM": 0,
    "HIGH": -20,
}


def calculate_reputation(*, validation_ok: bool, witness_count: int, level: str) -> int:
    score = 50

    score += 25 if validation_ok else -25
    score += max(0, witness_count) * 5
    score += LEVEL_WEIGHTS.get(level.upper(), -10)

    return max(0, min(score, 100))


def classify_reputation(score: int) -> str:
    if score >= 85:
        return "HIGH"
    if score >= 60:
        return "MEDIUM"
    return "LOW"
