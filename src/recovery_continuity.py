"""HC:// recovery continuity core."""

from __future__ import annotations


def build_recovery_checkpoint(*, checkpoint_id: str, continuity_hash: str) -> dict:
    return {
        "checkpoint_id": checkpoint_id.strip(),
        "continuity_hash": continuity_hash.strip(),
    }
