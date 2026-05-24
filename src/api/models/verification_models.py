"""Verification service response models.

This module defines canonical response structures for verification-oriented
public APIs. Models are intentionally minimal and framework-agnostic so they
can be reused by CLI, SDK, and HTTP transport layers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class VerificationState(str, Enum):
    """Normalized verification states used across API responses."""

    VERIFIED = "verified"
    SUSPICIOUS = "suspicious"
    DISPUTED = "disputed"
    REVOKED = "revoked"
    SUPERSEDED = "superseded"
    UNAVAILABLE = "unavailable"


@dataclass(slots=True)
class FederationSourceSummary:
    """Federation source participation summary for a record lookup."""

    source_id: str
    source_name: str
    state: VerificationState
    last_synced_at: datetime | None = None
    evidence_refs: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ProvenanceSummary:
    """Common provenance response structure."""

    witness_count: int
    revision_state: VerificationState
    federation_state: VerificationState
    verification_timestamp: datetime
    provenance_status: VerificationState
    integrity_status: VerificationState


@dataclass(slots=True)
class WitnessSummary:
    """Witness-oriented summary view for API responses."""

    witness_id: str
    state: VerificationState
    trust_score: float | None
    signed_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class VerificationResult:
    """Primary verification route response payload."""

    record_id: str
    state: VerificationState
    trust_score: float | None
    provenance: ProvenanceSummary
    sources: list[FederationSourceSummary] = field(default_factory=list)


@dataclass(slots=True)
class TrustResult:
    """Trust lookup route response payload."""

    record_id: str
    state: VerificationState
    trust_score: float | None
    confidence: float | None
    rationale: list[str] = field(default_factory=list)


@dataclass(slots=True)
class RevisionHistoryEntry:
    """Single revision entry in a revision history response."""

    revision_id: str
    state: VerificationState
    timestamp: datetime
    parent_revision_id: str | None = None


@dataclass(slots=True)
class RevisionHistoryResult:
    """Revision history route response payload."""

    record_id: str
    current_state: VerificationState
    revisions: list[RevisionHistoryEntry] = field(default_factory=list)
