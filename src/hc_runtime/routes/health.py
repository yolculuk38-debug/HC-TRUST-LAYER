"""Health and telemetry routes for HC:// advisory runtime prototype."""

from fastapi import APIRouter

from hc_runtime.state import EVENT_STORE, QUEUE_STORE

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "runtime": "hc-reference-runtime",
        "advisory_only": True,
    }


@router.get("/telemetry/health")
def telemetry_health() -> dict[str, object]:
    return {"status": "ok", "advisory_only": True, "runtime_mode": "prototype"}


@router.get("/telemetry/runtime")
def telemetry_runtime() -> dict[str, object]:
    return {
        "advisory_only": True,
        "public_safe": True,
        "events_total": len(EVENT_STORE._events),
        "degraded_events": len([e for e in EVENT_STORE._events if e["event_type"] == "runtime_recovery_mode"]),
    }


@router.get("/telemetry/queues")
def telemetry_queues() -> dict[str, object]:
    return {
        "advisory_only": True,
        "verification_queue": len(QUEUE_STORE.verification_queue),
        "escalation_queue": len(QUEUE_STORE.escalation_queue),
        "replay_warning_queue": len(QUEUE_STORE.replay_warning_queue),
        "degraded_queue_handling": True,
    }
