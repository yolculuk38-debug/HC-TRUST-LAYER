from __future__ import annotations

from fastapi import APIRouter

from src.api.models.federation import FederationResponse
from src.api.models.verification import VerificationProvenance, VerificationState

router = APIRouter(prefix="/federation", tags=["federation"])


@router.get("/{record_id}", response_model=FederationResponse)
def federation_record(record_id: str) -> FederationResponse:
    return FederationResponse(
        federation_sources=[],
        provenance=VerificationProvenance(
            record_id=record_id,
            verification_state=VerificationState.UNAVAILABLE,
            integrity_status=VerificationState.UNAVAILABLE,
            witness_count=0,
            revision_count=0,
            federation_sources=[],
        ),
    )
