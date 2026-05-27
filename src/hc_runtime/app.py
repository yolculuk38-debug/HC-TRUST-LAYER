"""Minimal FastAPI app for the HC:// reference runtime scaffold."""

from fastapi import FastAPI

from hc_runtime.routes.health import router as health_router
from hc_runtime.routes.verify import router as verify_router


def create_app() -> FastAPI:
    """Create advisory-only HC:// reference runtime application."""
    app = FastAPI(
        title="HC:// Reference Runtime",
        description=(
            "Advisory-only HC-TRUST-LAYER reference runtime scaffold. "
            "Not production-ready and not a truth guarantee."
        ),
        version="0.1.0",
    )
    app.include_router(health_router)
    app.include_router(verify_router)
    return app


app = create_app()
