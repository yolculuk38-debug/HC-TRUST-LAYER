"""HC:// signed bundle core."""

from __future__ import annotations


def create_signed_bundle(*, bundle_id: str, bundle_hash: str) -> dict:
    return {
        "bundle_id": bundle_id.strip(),
        "bundle_hash": bundle_hash.strip(),
    }
