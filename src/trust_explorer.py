"""HC:// trust explorer core."""

from __future__ import annotations


def build_trust_explorer_entry(*, entity_id: str, trust_score: int, trust_tier: str) -> dict:
    return {
        "entity_id": entity_id.strip(),
        "trust_score": trust_score,
        "trust_tier": trust_tier.strip().upper(),
    }
