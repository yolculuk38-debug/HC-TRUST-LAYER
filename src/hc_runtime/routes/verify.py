"""Verification placeholder route for the HC:// reference runtime scaffold."""

from fastapi import APIRouter

from hc_runtime.contracts import advisory_response

router = APIRouter()


@router.get("/verify/{record_id}")
def verify(record_id: str) -> dict[str, object]:
    """Return an advisory-only, public-safe placeholder verification response."""
    return advisory_response(
        record_id=record_id,
        message=(
            "HC:// reference runtime placeholder response. "
            "Advisory only with no truth guarantee, no canonical record mutation, "
            "and no private data exposure."
        ),
        warnings=[
            "Reference runtime response is advisory and requires human-supervised validation."
        ],
    )
