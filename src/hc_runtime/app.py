"""Minimal FastAPI app for the HC:// reference runtime scaffold."""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from hc_runtime.contracts import malformed_input_response
from hc_runtime.routes.health import router as health_router
from hc_runtime.routes.verify import router as verify_router


def _public_safe_validation_error_response(request: Request) -> JSONResponse:
    record_id = request.path_params.get("record_id")
    payload = malformed_input_response(record_id=str(record_id) if record_id is not None else None)
    payload["detail"] = "Request validation failed."
    payload["malformed_input"] = True
    payload["public_exposure"] = "restricted"
    return JSONResponse(status_code=422, content=payload)


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

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, _exc: RequestValidationError) -> JSONResponse:
        return _public_safe_validation_error_response(request)

    app.include_router(health_router)
    app.include_router(verify_router)
    return app


app = create_app()
