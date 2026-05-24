"""Federation endpoint response models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .verification import VerificationProvenance


class FederationResponse(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    status: str = "ok"
    endpoint: str = "federation"
    federation_sources: list[str] = Field(default_factory=list)
    provenance: VerificationProvenance
