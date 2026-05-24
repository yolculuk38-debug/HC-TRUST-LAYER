"""Canonical verification service route scaffolding.

These functions intentionally return model placeholders to preserve backwards
compatibility while the transport layer is still under active development.
"""

from __future__ import annotations

from datetime import datetime, timezone
from dataclasses import asdict
from typing import Any

from src.api.models.verification_models import (
    FederationSourceSummary,
    ProvenanceSummary,
    RevisionHistoryResult,
    TrustResult,
    VerificationResult,
    VerificationState,
    WitnessSummary,
)
from src.api.services.federation_registry import list_default_nodes


EXPERIMENTAL_PROTOCOL_VERSION = "0.1.0-experimental"


def get_verify(record_id: str) -> VerificationResult:
    """Scaffold for `GET /verify/{record_id}`."""
    now = datetime.now(tz=timezone.utc)
    return VerificationResult(
        record_id=record_id,
        state=VerificationState.UNAVAILABLE,
        trust_score=None,
        provenance=ProvenanceSummary(
            witness_count=0,
            revision_state=VerificationState.UNAVAILABLE,
            federation_state=VerificationState.UNAVAILABLE,
            verification_timestamp=now,
            provenance_status=VerificationState.UNAVAILABLE,
            integrity_status=VerificationState.UNAVAILABLE,
        ),
    )


def get_trust(record_id: str) -> TrustResult:
    """Scaffold for `GET /trust/{record_id}`."""
    return TrustResult(
        record_id=record_id,
        state=VerificationState.UNAVAILABLE,
        trust_score=None,
        confidence=None,
        rationale=["Trust lookup scaffolding is initialized but not yet wired."],
    )


def get_history(record_id: str) -> RevisionHistoryResult:
    """Scaffold for `GET /history/{record_id}`."""
    return RevisionHistoryResult(
        record_id=record_id,
        current_state=VerificationState.UNAVAILABLE,
        revisions=[],
    )


def get_witness(witness_id: str) -> WitnessSummary:
    """Scaffold for `GET /witness/{witness_id}`."""
    return WitnessSummary(
        witness_id=witness_id,
        state=VerificationState.UNAVAILABLE,
        trust_score=None,
        metadata={"status": "Witness lookup scaffolding is initialized."},
    )


def get_federation(record_id: str) -> list[FederationSourceSummary]:
    """Scaffold for `GET /federation/{record_id}`."""
    _ = record_id
    return []


def get_federation_nodes() -> dict[str, Any]:
    """Experimental scaffold for `GET /federation/nodes`."""

    nodes = [asdict(node) for node in list_default_nodes()]
    return {
        "status": "experimental",
        "protocol_version": EXPERIMENTAL_PROTOCOL_VERSION,
        "nodes": nodes,
    }


def get_federation_status() -> dict[str, Any]:
    """Experimental scaffold for `GET /federation/status`."""

    return {
        "status": "experimental",
        "sync_state": "not-configured",
        "message": "Federation status endpoint is scaffolded for distributed trust sync.",
    }


def get_federation_capabilities() -> dict[str, Any]:
    """Experimental scaffold for `GET /federation/capabilities`."""

    return {
        "status": "experimental",
        "capabilities": [
            "integrity-hash-check",
            "revision-chain-validation",
            "witness-reference-normalization",
        ],
    }


def get_federation_sync_preview() -> dict[str, Any]:
    """Experimental scaffold for `GET /federation/sync-preview`."""

    return {
        "status": "experimental",
        "preview": {
            "eligible_nodes": [node.node_id for node in list_default_nodes()],
            "planned_actions": ["capability-negotiation", "manifest-version-check"],
            "non_production_warning": True,
        },
    }


def export_verification_package(record_id: str) -> dict[str, Any]:
    """Experimental scaffold for `GET /verify/export/{record_id}`."""

    return {
        "status": "experimental",
        "package": {
            "package_version": EXPERIMENTAL_PROTOCOL_VERSION,
            "record_id": record_id,
            "provenance": {
                "source_system": "hc-trust-layer",
                "export_reason": "verification-preview",
            },
            "revision_references": [],
            "witness_references": [],
            "integrity_hash_references": [],
            "federation_source_references": [],
        },
    }
