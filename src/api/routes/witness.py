from __future__ import annotations

from fastapi import APIRouter

from src.api.models.verification import VerificationProvenance, VerificationState
from src.api.models.witness import WitnessResponse

router = APIRouter(prefix="/witness", tags=["witness"])


@router.get("/{witness_id}", response_model=WitnessResponse)
def witness_summary(witness_id: str) -> WitnessResponse:
    return WitnessResponse(
        witness_id=witness_id,
        witness_count=0,
        provenance=VerificationProvenance(
            record_id=witness_id,
            verification_state=VerificationState.UNAVAILABLE,
            integrity_status=VerificationState.UNAVAILABLE,
            witness_count=0,
            revision_count=0,
            federation_sources=[],
        ),
    )
