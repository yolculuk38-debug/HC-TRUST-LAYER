"""HC:// audit graph core."""

from __future__ import annotations


def create_audit_edge(*, source_id: str, target_id: str, relation: str) -> dict:
    return {
        "source_id": source_id.strip(),
        "target_id": target_id.strip(),
        "relation": relation.strip().upper(),
    }
