"""HC:// public explorer API core."""

from __future__ import annotations


def build_explorer_record(*, record_id: str, status: str, trust_score: int) -> dict:
    return {
        "record_id": record_id.strip(),
        "status": status.strip().upper(),
        "trust_score": max(0, min(int(trust_score), 100)),
    }
