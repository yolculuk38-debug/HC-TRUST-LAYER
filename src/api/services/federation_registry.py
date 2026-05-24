"""Federation registry scaffolding for experimental trust synchronization."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class FederationNode:
    """Trusted federation node descriptor."""

    node_id: str
    endpoint_url: str
    public_key: str
    trust_scope: list[str] = field(default_factory=list)
    protocol_version: str = "hc-protocol-v1"
    verification_capabilities: list[str] = field(default_factory=list)


def list_default_nodes() -> list[FederationNode]:
    """Return a deterministic placeholder node set for experimental APIs."""

    return [
        FederationNode(
            node_id="local-experimental-node",
            endpoint_url="https://localhost.invalid/federation",
            public_key="TODO_PUBLIC_KEY",
            trust_scope=["record-verification"],
            protocol_version="hc-protocol-v1",
            verification_capabilities=["integrity-hash-check", "revision-chain-validation"],
        )
    ]
