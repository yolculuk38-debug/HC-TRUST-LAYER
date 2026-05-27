"""Verification and continuity routes for the HC:// reference runtime."""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from hc_runtime.contracts import advisory_response
from hc_runtime.runtime import RuntimeEventStore, TrustStateDecisionEngine, ValidatorPipeline

router = APIRouter()

_EVENT_STORE = RuntimeEventStore()
_PIPELINE = ValidatorPipeline()
_DECISION_ENGINE = TrustStateDecisionEngine()


class VerifyRequest(BaseModel):
    qr_input: str


def _run_qr_flow(*, record_id: str, qr_input: str) -> dict[str, object]:
    pipeline_result = _PIPELINE.run(record_id=record_id, qr_input=qr_input)
    replay_warning = "replay" in qr_input.lower()
    continuity_ok = "continuity-warning" not in qr_input.lower() and "continuity-warning" not in record_id.lower()

    trust_state, warnings = _DECISION_ENGINE.classify(
        record_id=record_id,
        qr_input=qr_input,
        schema_valid=pipeline_result["schema_result"]["valid"],
        hash_verified=pipeline_result["hash_result"]["hash_verified"],
        continuity_ok=continuity_ok,
        replay_warning=replay_warning,
    )

    _EVENT_STORE.append_trust_transition(record_id=record_id, trust_state=trust_state.value, warnings=warnings)

    if replay_warning:
        _EVENT_STORE.append_replay_warning(record_id=record_id, reason="Replay marker detected in advisory QR input.")

    continuity_warnings = [warning for warning in warnings if "continuity warning" in warning.lower()]
    _EVENT_STORE.append_continuity_checkpoint(
        record_id=record_id,
        continuity_ok=continuity_ok,
        warnings=continuity_warnings,
    )

    payload = advisory_response(
        record_id=record_id,
        message=(
            "Advisory HC:// QR verification flow executed: QR input → validator pipeline "
            "→ decision engine → event append → public-safe response."
        ),
        warnings=warnings,
    )
    payload["trust_state"] = trust_state.value
    payload["replay_warning"] = replay_warning
    payload["continuity_warning"] = not continuity_ok
    return payload


@router.get("/verify/{record_id}")
def verify(record_id: str) -> dict[str, object]:
    """Return an advisory-only, public-safe placeholder verification response."""
    _EVENT_STORE.append_continuity_checkpoint(record_id=record_id, continuity_ok=True, warnings=[])
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


@router.post("/verify/{record_id}")
def verify_qr(record_id: str, request: VerifyRequest) -> dict[str, object]:
    """Run minimal advisory verification runtime flow for QR verification input."""
    return _run_qr_flow(record_id=record_id, qr_input=request.qr_input)


@router.get("/qr/{record_id}")
def verify_qr_get(record_id: str) -> dict[str, object]:
    """Run advisory QR verification runtime integration via GET route."""
    return _run_qr_flow(record_id=record_id, qr_input=f"hc://{record_id} hash:advisory")


@router.get("/verify/{record_id}/history")
def verify_history(record_id: str) -> dict[str, object]:
    """Return advisory continuity/event history placeholder for a record."""
    return {
        "record_id": record_id,
        "advisory_only": True,
        "public_safe": True,
        "events": _EVENT_STORE.history(record_id),
    }


@router.post("/federation/review")
def federation_review(payload: dict[str, object]) -> dict[str, object]:
    """Advisory federation review placeholder with local-only processing."""
    record_id = str(payload.get("record_id", "unknown-record"))
    _EVENT_STORE.append_runtime_event(
        event_type="federation_review_placeholder",
        record_id=record_id,
        details={"local_only": True, "networking": False},
    )
    return {
        "status": "ADVISORY",
        "advisory_only": True,
        "public_safe": True,
        "message": (
            "Federation review placeholder accepted for human-supervised validation routing. "
            "No external networking or federation transport is performed in this runtime."
        ),
    }
