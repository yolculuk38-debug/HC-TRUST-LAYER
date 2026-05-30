"""Health and telemetry routes for HC:// advisory runtime prototype."""

from fastapi import APIRouter

from hc_runtime.state import EVENT_STORE, QUEUE_STORE

router = APIRouter()

DEGRADED_RUNTIME_EVENT = "runtime_recovery_mode"
DEGRADED_RUNTIME_WARNING = "Degraded runtime events are visible for advisory human-supervised validation."


def _degraded_runtime_events() -> list[dict[str, object]]:
    return [event for event in EVENT_STORE._events if event["event_type"] == DEGRADED_RUNTIME_EVENT]


def _telemetry_base(*, degraded: bool, escalation_required: bool = False) -> dict[str, object]:
    warnings = [DEGRADED_RUNTIME_WARNING] if degraded else []
    return {
        "status": "degraded" if degraded else "ok",
        "runtime_mode": "prototype",
        "advisory_only": True,
        "runtime_stage": "prototype",
        "verification_mode": "advisory",
        "public_safe": True,
        "traceable": True,
        "truth_guarantee": False,
        "warnings": warnings,
        "human_review_required": bool(warnings) or escalation_required,
        "degraded": degraded,
        "degraded_reasons": ["runtime_recovery_mode"] if degraded else [],
    }


@router.get("/health")
def health() -> dict[str, object]:
    return {
        "status": "ok",
        "runtime": "hc-reference-runtime",
        "advisory_only": True,
        "runtime_stage": "prototype",
        "verification_mode": "advisory",
        "public_safe": True,
        "traceable": True,
        "truth_guarantee": False,
        "warnings": [],
        "human_review_required": False,
    }


@router.get("/telemetry/health")
def telemetry_health() -> dict[str, object]:
    degraded = bool(_degraded_runtime_events())
    return _telemetry_base(degraded=degraded)


@router.get("/telemetry/runtime")
def telemetry_runtime() -> dict[str, object]:
    degraded_events = _degraded_runtime_events()
    payload = _telemetry_base(degraded=bool(degraded_events))
    payload["events_total"] = len(EVENT_STORE._events)
    payload["degraded_events"] = len(degraded_events)
    return payload


@router.get("/telemetry/queues")
def telemetry_queues() -> dict[str, object]:
    degraded = bool(_degraded_runtime_events())
    payload = _telemetry_base(degraded=degraded, escalation_required=bool(QUEUE_STORE.escalation_queue))
    payload["verification_queue"] = len(QUEUE_STORE.verification_queue)
    payload["escalation_queue"] = len(QUEUE_STORE.escalation_queue)
    payload["replay_warning_queue"] = len(QUEUE_STORE.replay_warning_queue)
    payload["degraded_queue_handling"] = True
    return payload
