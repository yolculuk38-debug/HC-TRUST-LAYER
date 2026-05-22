"""HC:// deployment manifest core."""

from __future__ import annotations


def build_deployment_manifest(*, deployment_id: str, manifest_hash: str) -> dict:
    return {
        "deployment_id": deployment_id.strip(),
        "manifest_hash": manifest_hash.strip(),
    }
