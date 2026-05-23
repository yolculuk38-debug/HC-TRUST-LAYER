"""HC:// portable verification layer."""

from __future__ import annotations


def build_portable_manifest(*, record_id: str, content_hash: str, source: str) -> dict:
    return {
        "record_id": record_id.strip(),
        "content_hash": content_hash.strip(),
        "source": source.strip(),
        "portable": True,
    }


def verify_manifest(manifest: dict, expected_hash: str) -> bool:
    return manifest.get("content_hash") == expected_hash.strip()


def import_ready(manifest: dict) -> bool:
    return bool(manifest.get("portable", False))
