from __future__ import annotations

from fastapi import APIRouter, HTTPException

from src.api.models.verification import VerificationProvenance, VerificationState
from src.api.services.record_loader import RecordLoaderError, load_record

router = APIRouter(prefix="/verify", tags=["verification"])


@router.get("/{record_id}")
def verify_record(record_id: str) -> dict:
    try:
        loaded = load_record(record_id)
    except RecordLoaderError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    state = (
        VerificationState.VERIFIED
        if loaded["state"] == "verified"
        else VerificationState.UNAVAILABLE
    )
    provenance = VerificationProvenance(
        record_id=record_id,
        verification_state=state,
        integrity_status=state,
        witness_count=0,
        revision_count=0,
        federation_sources=[],
    )
    return {"status": "ok", "endpoint": "verify", "provenance": provenance.model_dump()}
