"""Verification, continuity, and federation routes for HC:// reference runtime."""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from hc_runtime.contracts import advisory_response
from hc_runtime.state import DECISION_ENGINE, EVENT_STORE, FEDERATION_RELAY, PIPELINE, POLICY_ENGINE, QUEUE_STORE

router = APIRouter()


class VerifyRequest(BaseModel):
    qr_input: str


def _run_qr_flow(*, record_id: str, qr_input: str) -> dict[str, object]:
    QUEUE_STORE.enqueue_verification({"record_id": record_id, "qr_input": qr_input})

    pipeline_result = PIPELINE.run(record_id=record_id, qr_input=qr_input)
    replay_warning = "replay" in qr_input.lower()
    continuity_ok = "continuity-warning" not in qr_input.lower() and "continuity-warning" not in record_id.lower()
    degraded_mode = "degraded" in qr_input.lower() or "degraded" in record_id.lower() or not continuity_ok

    trust_state, warnings = DECISION_ENGINE.classify(
        record_id=record_id,
        qr_input=qr_input,
        schema_valid=pipeline_result["schema_result"]["valid"],
        hash_verified=pipeline_result["hash_result"]["hash_verified"],
        continuity_ok=continuity_ok,
        replay_warning=replay_warning,
    )

    policy = POLICY_ENGINE.evaluate(trust_state=trust_state, replay_warning=replay_warning, degraded_mode=degraded_mode)
    warnings = [*warnings, *policy["warnings"]]

    EVENT_STORE.append_trust_transition(record_id=record_id, trust_state=trust_state.value, warnings=warnings)
    EVENT_STORE.append_continuity_checkpoint(record_id=record_id, continuity_ok=continuity_ok, warnings=warnings)

    if replay_warning:
        QUEUE_STORE.enqueue_replay_warning({"record_id": record_id, "source": "qr-verification"})
        QUEUE_STORE.enqueue_escalation({"record_id": record_id, "reason": "replay_warning"})
        EVENT_STORE.append_replay_warning(record_id=record_id, reason="Replay marker detected in advisory QR input.")

    if policy["advisory_downgrade"]:
        QUEUE_STORE.enqueue_escalation({"record_id": record_id, "reason": "advisory_downgrade"})

    if degraded_mode:
        EVENT_STORE.append_runtime_event(
            event_type="runtime_recovery_mode",
            record_id=record_id,
            details={"degraded_detected": True, "recovery_mode": True, "failover_safe": True},
        )

    payload = advisory_response(
        record_id=record_id,
        message=(
            "Advisory HC:// runtime flow executed: request → validator pipeline → trust-state engine "
            "→ event append → response contract → continuity history."
        ),
        warnings=warnings,
    )
    payload["trust_state"] = trust_state.value
    payload["replay_warning"] = replay_warning
    payload["continuity_warning"] = not continuity_ok
    payload["degraded_runtime"] = degraded_mode
    payload["recovery_mode"] = degraded_mode
    payload["public_exposure"] = policy["public_exposure"]
    return payload


@router.get("/verify/{record_id}")
def verify(record_id: str) -> dict[str, object]:
    EVENT_STORE.append_continuity_checkpoint(record_id=record_id, continuity_ok=True, warnings=[])
    return advisory_response(
        record_id=record_id,
        message=(
            "HC:// reference runtime placeholder response. "
            "Advisory only with no truth guarantee, no canonical record mutation, "
            "and no private data exposure."
        ),
        warnings=["Reference runtime response is advisory and requires human-supervised validation."],
    )


@router.post("/verify/{record_id}")
def verify_qr(record_id: str, request: VerifyRequest) -> dict[str, object]:
    return _run_qr_flow(record_id=record_id, qr_input=request.qr_input)


@router.get("/qr/{record_id}")
def verify_qr_get(record_id: str) -> dict[str, object]:
    return _run_qr_flow(record_id=record_id, qr_input=f"hc://{record_id} hash:advisory")


@router.get("/verify/{record_id}/history")
def verify_history(record_id: str) -> dict[str, object]:
    events = EVENT_STORE.history(record_id)
    return {
        "record_id": record_id,
        "advisory_only": True,
        "public_safe": True,
        "traceable": True,
        "truth_guarantee": False,
        "warnings": [],
        "replay_warning_visible": any(event["event_type"] == "replay_warning" for event in events),
        "trust_state_transitions": [e for e in events if e["event_type"] == "trust_state_transition"],
        "events": events,
    }


@router.post("/federation/review")
def federation_review(payload: dict[str, object]) -> dict[str, object]:
    record_id = str(payload.get("record_id", "unknown-record"))
    replay_warning = bool(payload.get("replay_warning", False))
    degraded_mode = bool(payload.get("degraded_mode", False))

    relay = FEDERATION_RELAY.review(record_id=record_id, degraded_mode=degraded_mode, replay_warning=replay_warning)
    EVENT_STORE.append_runtime_event(
        event_type="federation_review_placeholder",
        record_id=record_id,
        details={"local_only": True, "networking": False, "relay": relay},
    )

    return {
        "status": "ADVISORY",
        "advisory_only": True,
        "public_safe": True,
        "traceable": True,
        "truth_guarantee": False,
        "message": "Federation review placeholder accepted for human-supervised validation routing.",
        "warnings": [
            "Federation routing remains advisory in the HC:// reference runtime with no production-readiness or objective-truth guarantee."
        ],
        "relay": relay,
    }
