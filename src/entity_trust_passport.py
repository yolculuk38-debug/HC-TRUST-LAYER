"""HC:// entity trust passport core."""

from __future__ import annotations

TRUST_PASSPORT_VERSION = "HC-TRUST-PASSPORT-V1"


def create_trust_passport(*, entity_id: str, trust_score: int, trust_tier: str) -> dict:
    return {
        "trust_passport_version": TRUST_PASSPORT_VERSION,
        "entity_id": entity_id.strip(),
        "trust_score": max(0, min(int(trust_score), 100)),
        "trust_tier": trust_tier.strip().upper(),
    }
