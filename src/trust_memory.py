"""HC:// persistent trust memory core."""

from __future__ import annotations


def create_memory_entry(*, entity_id: str, memory_hash: str) -> dict:
    return {
        "entity_id": entity_id.strip(),
        "memory_hash": memory_hash.strip(),
    }
