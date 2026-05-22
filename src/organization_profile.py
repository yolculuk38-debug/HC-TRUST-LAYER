"""HC:// organization profile core."""

from __future__ import annotations


def build_organization_profile(*, organization_id: str, name: str, trust_state: str) -> dict:
    return {
        "organization_id": organization_id.strip(),
        "name": name.strip(),
        "trust_state": trust_state.strip().upper(),
    }
