"""Verification response models for the experimental runtime API."""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class VerificationState(str, Enum):
    """Normalized verification states shared across runtime API responses."""

    VERIFIED = "verified"
    SUSPICIOUS = "suspicious"
    DISPUTED = "disputed"
    REVOKED = "revoked"
    SUPERSEDED = "superseded"
    UNAVAILABLE = "unavailable"


class VerificationProvenance(BaseModel):
    """Common provenance fields included in verification-facing responses."""

    model_config = ConfigDict(use_enum_values=True)

    record_id: str
    verification_state: VerificationState
    integrity_status: VerificationState
    witness_count: int = Field(ge=0)
    revision_count: int = Field(ge=0)
    federation_sources: list[str] = Field(default_factory=list)
    verification_timestamp: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc)
    )
