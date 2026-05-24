"""Canonical verification service route scaffolding.

These functions intentionally return model placeholders to preserve backwards
compatibility while the transport layer is still under active development.
"""

from __future__ import annotations

from datetime import datetime, timezone

from src.api.models.verification_models import (
    FederationSourceSummary,
    ProvenanceSummary,
    RevisionHistoryResult,
    TrustResult,
    VerificationResult,
    VerificationState,
    WitnessSummary,
)


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
