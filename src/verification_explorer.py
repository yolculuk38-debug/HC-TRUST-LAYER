"""HC:// verification explorer skeleton."""

from __future__ import annotations


def build_explorer_item(*, record_id: str, trust_level: str, status: str) -> dict:
    return {
        "record_id": record_id.strip(),
        "trust_level": trust_level.strip().upper(),
        "status": status.strip().upper(),
    }


def filter_verified(items: list[dict]) -> list[dict]:
    return [item for item in items if item.get("status") == "VERIFIED"]


def summarize_explorer(items: list[dict]) -> dict:
    verified = filter_verified(items)
    return {
        "total": len(items),
        "verified": len(verified),
        "unverified": len(items) - len(verified),
    }
