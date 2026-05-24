"""Witness endpoint response models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .verification import VerificationProvenance


class WitnessResponse(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    status: str = "ok"
    endpoint: str = "witness"
    witness_id: str
    witness_count: int = Field(ge=0)
    provenance: VerificationProvenance
