"""HC:// supply-chain risk core.

Evaluates package, extension, workflow, and dependency metadata as
verification signals. This module does not install, fetch, or execute anything.
"""

from __future__ import annotations

from typing import Any
from urllib.parse import urlparse


SUPPLY_CHAIN_VERSION = "HC-SUPPLY-CHAIN-RISK-V1"
SUPPORTED_ARTIFACT_TYPES = {"package", "extension", "workflow", "dependency", "container", "repository"}


class SupplyChainStatus:
    LOW_RISK = "LOW_RISK"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    HIGH_RISK = "HIGH_RISK"
    INVALID = "INVALID"


def evaluate_supply_chain_artifact(artifact: dict[str, Any]) -> dict[str, Any]:
    """Evaluate supply-chain risk metadata without external calls."""

    if not isinstance(artifact, dict):
        return {"status": SupplyChainStatus.INVALID, "risk_score": 100, "reason": "artifact must be an object"}

    required = {"artifact_id", "artifact_type", "source_url", "version"}
    missing = required.difference(artifact)
    if missing:
        return {
            "status": SupplyChainStatus.INVALID,
            "risk_score": 100,
            "reason": f"missing required field(s): {', '.join(sorted(missing))}",
        }

    if artifact["artifact_type"] not in SUPPORTED_ARTIFACT_TYPES:
        return {"status": SupplyChainStatus.INVALID, "risk_score": 100, "reason": "unsupported artifact type"}

    parsed = urlparse(str(artifact["source_url"]))
    if parsed.scheme != "https":
        return {"status": SupplyChainStatus.HIGH_RISK, "risk_score": 90, "reason": "source_url must use https"}

    risk_score = 0
    flags: list[str] = []

    if not artifact.get("signed"):
        risk_score += 25
        flags.append("unsigned_artifact")

    if not artifact.get("pinned_version"):
        risk_score += 15
        flags.append("unpinned_version")

    if artifact.get("network_access"):
        risk_score += 20
        flags.append("network_access")

    if artifact.get("exec_permissions"):
        risk_score += 25
        flags.append("exec_permissions")

    if not artifact.get("provenance_verified"):
        risk_score += 20
        flags.append("missing_provenance")

    risk_score = min(100, risk_score)

    if risk_score >= 70:
        status = SupplyChainStatus.HIGH_RISK
    elif risk_score >= 30:
        status = SupplyChainStatus.REVIEW_REQUIRED
    else:
        status = SupplyChainStatus.LOW_RISK

    return {
        "supply_chain_version": SUPPLY_CHAIN_VERSION,
        "status": status,
        "risk_score": risk_score,
        "risk_flags": flags,
        "reason": "supply-chain artifact evaluated",
    }


__all__ = [
    "SUPPLY_CHAIN_VERSION",
    "SUPPORTED_ARTIFACT_TYPES",
    "SupplyChainStatus",
    "evaluate_supply_chain_artifact",
]
