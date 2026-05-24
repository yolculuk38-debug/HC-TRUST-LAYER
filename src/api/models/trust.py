"""Trust endpoint response models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .verification import VerificationProvenance


class TrustResponse(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    status: str = "ok"
    endpoint: str = "trust"
    trust_score: float | None = Field(default=None, ge=0.0, le=1.0)
    provenance: VerificationProvenance
