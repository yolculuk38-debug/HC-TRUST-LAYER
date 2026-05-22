"""HC:// distributed cache core."""

from __future__ import annotations


def build_cache_entry(*, cache_key: str, cache_hash: str) -> dict:
    return {
        "cache_key": cache_key.strip(),
        "cache_hash": cache_hash.strip(),
    }
