"""HC:// audit analytics core."""

from __future__ import annotations


def build_audit_metrics(*, verified_records: int, revoked_records: int) -> dict:
    return {
        "verified_records": max(0, int(verified_records)),
        "revoked_records": max(0, int(revoked_records)),
    }
