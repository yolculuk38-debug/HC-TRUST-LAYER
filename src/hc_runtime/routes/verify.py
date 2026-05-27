"""Verification placeholder route for the HC:// reference runtime scaffold."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/verify/{record_id}")
def verify(record_id: str) -> dict[str, str]:
    """Return an advisory-only, public-safe placeholder verification response."""
    return {
        "record_id": record_id,
        "status": "ADVISORY",
        "message": (
            "HC:// reference runtime placeholder response. "
            "Advisory only with no truth guarantee, no canonical record mutation, "
            "and no private data exposure."
        ),
    }
