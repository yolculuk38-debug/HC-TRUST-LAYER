from __future__ import annotations

from fastapi import APIRouter

from src.api.models.trust import TrustResponse
from src.api.models.verification import VerificationProvenance, VerificationState

router = APIRouter(prefix="/trust", tags=["trust"])


@router.get("/{record_id}", response_model=TrustResponse)
def trust_record(record_id: str) -> TrustResponse:
    return TrustResponse(
        trust_score=None,
        provenance=VerificationProvenance(
            record_id=record_id,
            verification_state=VerificationState.UNAVAILABLE,
            integrity_status=VerificationState.UNAVAILABLE,
            witness_count=0,
            revision_count=0,
            federation_sources=[],
        ),
    )
