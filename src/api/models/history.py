"""History endpoint response models."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .verification import VerificationProvenance, VerificationState


class HistoryRevision(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    revision_id: str
    verification_state: VerificationState
    timestamp: datetime


class HistoryResponse(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    status: str = "ok"
    endpoint: str = "history"
    revision_count: int = Field(ge=0)
    revisions: list[HistoryRevision] = Field(default_factory=list)
    provenance: VerificationProvenance
