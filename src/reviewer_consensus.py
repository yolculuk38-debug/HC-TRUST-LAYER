"""HC:// reviewer consensus layer."""

from __future__ import annotations


def calculate_consensus(*, approvals: int, rejections: int) -> float:
    total = approvals + rejections
    if total <= 0:
        return 0.0
    return round((approvals / total) * 100, 2)


def consensus_passed(*, approvals: int, rejections: int, threshold: float = 70.0) -> bool:
    return calculate_consensus(approvals=approvals, rejections=rejections) >= threshold


def build_consensus_record(*, approvals: int, rejections: int) -> dict:
    score = calculate_consensus(approvals=approvals, rejections=rejections)
    return {
        "approvals": approvals,
        "rejections": rejections,
        "consensus_score": score,
        "status": "PASSED" if score >= 70 else "REVIEW_REQUIRED",
    }
