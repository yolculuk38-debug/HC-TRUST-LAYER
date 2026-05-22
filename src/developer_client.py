"""HC:// developer client helpers."""

from __future__ import annotations


def build_client_request(*, record_id: str, verifier_id: str) -> dict:
    return {
        "record_id": record_id.strip(),
        "verifier_id": verifier_id.strip(),
    }


def build_client_result(*, record_id: str, status: str, trust_score: int) -> dict:
    return {
        "record_id": record_id.strip(),
        "status": status.strip().upper(),
        "trust_score": max(0, min(int(trust_score), 100)),
    }
