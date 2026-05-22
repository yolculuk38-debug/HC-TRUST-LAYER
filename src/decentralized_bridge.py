"""HC:// decentralized verification bridge core."""

from __future__ import annotations

BRIDGE_VERSION = "HC-DECENTRALIZED-BRIDGE-V1"


def create_bridge_link(*, local_network: str, remote_network: str, bridge_hash: str) -> dict:
    return {
        "bridge_version": BRIDGE_VERSION,
        "local_network": local_network.strip(),
        "remote_network": remote_network.strip(),
        "bridge_hash": bridge_hash.strip(),
    }
