from __future__ import annotations

from fastapi import APIRouter

from src.api.models.history import HistoryResponse
from src.api.models.verification import VerificationProvenance, VerificationState

router = APIRouter(prefix="/history", tags=["history"])


@router.get("/{record_id}", response_model=HistoryResponse)
def history_record(record_id: str) -> HistoryResponse:
    return HistoryResponse(
        revision_count=0,
        revisions=[],
        provenance=VerificationProvenance(
            record_id=record_id,
            verification_state=VerificationState.UNAVAILABLE,
            integrity_status=VerificationState.UNAVAILABLE,
            witness_count=0,
            revision_count=0,
            federation_sources=[],
        ),
    )
