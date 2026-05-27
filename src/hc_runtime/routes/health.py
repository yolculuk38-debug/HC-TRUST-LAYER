"""Health route for the HC:// reference runtime scaffold."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | bool]:
    """Return advisory runtime health status."""
    return {
        "status": "ok",
        "runtime": "hc-reference-runtime",
        "advisory_only": True,
    }
