"""FastAPI runtime service foundation for HC-TRUST-LAYER."""

from __future__ import annotations

from fastapi import FastAPI

from src.api.routes.federation import router as federation_router
from src.api.routes.history import router as history_router
from src.api.routes.trust import router as trust_router
from src.api.routes.verify import router as verify_router
from src.api.routes.witness import router as witness_router

app = FastAPI(title="HC-TRUST-LAYER Runtime Verification API", version="0.1.0-experimental")

app.include_router(verify_router)
app.include_router(trust_router)
app.include_router(history_router)
app.include_router(witness_router)
app.include_router(federation_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "hc-trust-layer-verification-runtime"}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": app.version, "api": "runtime-verification"}


@app.get("/experimental-status")
def experimental_status() -> dict[str, str]:
    return {
        "status": "experimental",
        "banner": "This verification runtime API is experimental and not for production trust decisions.",
    }
