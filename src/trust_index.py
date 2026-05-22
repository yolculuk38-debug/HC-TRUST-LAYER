"""HC:// trust index core."""

from __future__ import annotations


def build_index_entry(*, record_id: str, trust_score: int) -> dict:
    return {
        "record_id": record_id.strip(),
        "trust_score": max(0, min(int(trust_score), 100)),
    }
