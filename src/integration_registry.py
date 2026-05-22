"""HC:// integration registry core."""

from __future__ import annotations


def register_integration(*, integration_id: str, integration_type: str, endpoint: str) -> dict:
    return {
        "integration_id": integration_id.strip(),
        "integration_type": integration_type.strip().upper(),
        "endpoint": endpoint.strip(),
    }
