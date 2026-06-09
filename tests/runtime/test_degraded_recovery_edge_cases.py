"""Degraded recovery edge-case coverage for HC:// advisory runtime behavior."""

from __future__ import annotations

from hc_runtime.contracts.responses import advisory_response
from hc_runtime.decision_engine import TrustState, TrustStateDecisionEngine
from hc_runtime.events import RuntimeEventStore
from hc_runtime.runtime import RuntimePolicyEngine, RuntimeQueueStore, ValidatorPipeline


EXPECTED_RUNTIME_RESPONSE_KEYS = [
    "status",
    "advisory_only",
    "runtime_stage",
    "verification_mode",
    "public_safe",
    "message",
    "warnings",
    "traceable",
    "truth_guarantee",
    "human_review_required",
    "record_id",
    "trust_state",
    "replay_warning",
    "continuity_warning",
    "degraded_runtime",
    "recovery_mode",
    "public_exposure",
]

EXPECTED_HISTORY_KEYS = [
    "record_id",
    "advisory_only",
    "runtime_stage",
    "verification_mode",
    "public_safe",
    "traceable",
    "truth_guarantee",
    "warnings",
    "human_review_required",
    "replay_warning_visible",
    "trust_state_transitions",
    "events",
]

EXPECTED_TELEMETRY_KEYS = [
    "status",
    "runtime_mode",
    "advisory_only",
    "runtime_stage",
    "verification_mode",
    "public_safe",
    "traceable",
    "truth_guarantee",
    "warnings",
    "human_review_required",
    "degraded",
    "degraded_reasons",
    "events_total",
    "degraded_events",
    "verification_queue",
    "escalation_queue",
    "replay_warning_queue",
    "degraded_queue_handling",
]

FORBIDDEN_AUTHORITY_TERMS = [
    "objective truth",
    "forensic certainty",
    "autonomous governance",
    "production ready",
    "production-ready",
    "authoritative",
]


class PartialQueueStore(RuntimeQueueStore):
    """Queue store that simulates loss of one derived queue view after enqueue."""

    def drop_replay_warning_view(self) -> None:
        self.replay_warning_queue.clear()


def _run_isolated_qr_flow(
    *,
    record_id: str,
    qr_input: str,
    event_store: RuntimeEventStore | None = None,
    queue_store: RuntimeQueueStore | None = None,
) -> tuple[dict[str, object], RuntimeEventStore, RuntimeQueueStore]:
    """Exercise HC:// runtime components without shared app state or runtime refactors."""
    queue_store = queue_store or RuntimeQueueStore()
    pipeline = ValidatorPipeline()
    decision_engine = TrustStateDecisionEngine()
    policy_engine = RuntimePolicyEngine()
    event_store = event_store or RuntimeEventStore()

    queue_store.enqueue_verification({"record_id": record_id, "qr_input": qr_input})
    pipeline_result = pipeline.run(record_id=record_id, qr_input=qr_input)
    replay_warning = "replay" in qr_input.lower()
    continuity_ok = (
        "continuity-warning" not in qr_input.lower()
        and "continuity-warning" not in record_id.lower()
    )
    degraded_mode = "degraded" in qr_input.lower() or "degraded" in record_id.lower() or not continuity_ok

    trust_state, warnings = decision_engine.classify(
        record_id=record_id,
        qr_input=qr_input,
        schema_valid=pipeline_result["schema_result"]["valid"],
        hash_verified=pipeline_result["hash_result"]["hash_verified"],
        continuity_ok=continuity_ok,
        replay_warning=replay_warning,
    )

    policy = policy_engine.evaluate(
        trust_state=trust_state,
        replay_warning=replay_warning,
        degraded_mode=degraded_mode,
    )
    warnings = [*warnings, *policy["warnings"]]

    event_store.append_trust_transition(record_id=record_id, trust_state=trust_state.value, warnings=warnings)
    event_store.append_continuity_checkpoint(record_id=record_id, continuity_ok=continuity_ok, warnings=warnings)

    if replay_warning:
        queue_store.enqueue_replay_warning({"record_id": record_id, "source": "qr-verification"})
        queue_store.enqueue_escalation({"record_id": record_id, "reason": "replay_warning"})
        event_store.append_replay_warning(
            record_id=record_id,
            reason="Replay marker detected in advisory QR input.",
        )

    if policy["advisory_downgrade"]:
        queue_store.enqueue_escalation({"record_id": record_id, "reason": "advisory_downgrade"})

    if degraded_mode:
        event_store.append_runtime_event(
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
    return payload, event_store, queue_store


def _history_response(*, record_id: str, event_store: RuntimeEventStore) -> dict[str, object]:
    events = event_store.history(record_id)
    return {
        "record_id": record_id,
        "advisory_only": True,
        "runtime_stage": "prototype",
        "verification_mode": "advisory",
        "public_safe": True,
        "traceable": True,
        "truth_guarantee": False,
        "warnings": [],
        "human_review_required": False,
        "replay_warning_visible": any(event["event_type"] == "replay_warning" for event in events),
        "trust_state_transitions": [event for event in events if event["event_type"] == "trust_state_transition"],
        "events": events,
    }


def _telemetry_snapshot(*, event_store: RuntimeEventStore, queue_store: RuntimeQueueStore) -> dict[str, object]:
    degraded_events = [event for event in event_store._events if event.get("event_type") == "runtime_recovery_mode"]
    degraded = bool(degraded_events)
    return {
        "status": "degraded" if degraded else "ok",
        "runtime_mode": "prototype",
        "advisory_only": True,
        "runtime_stage": "prototype",
        "verification_mode": "advisory",
        "public_safe": True,
        "traceable": True,
        "truth_guarantee": False,
        "warnings": ["Degraded runtime events are visible for advisory human-supervised validation."] if degraded else [],
        "human_review_required": degraded or bool(queue_store.escalation_queue),
        "degraded": degraded,
        "degraded_reasons": ["runtime_recovery_mode"] if degraded else [],
        "events_total": len(event_store._events),
        "degraded_events": len(degraded_events),
        "verification_queue": len(queue_store.verification_queue),
        "escalation_queue": len(queue_store.escalation_queue),
        "replay_warning_queue": len(queue_store.replay_warning_queue),
        "degraded_queue_handling": True,
    }


def _assert_advisory_contract(payload: dict[str, object], *, record_id: str) -> None:
    assert list(payload.keys()) == EXPECTED_RUNTIME_RESPONSE_KEYS
    assert payload["record_id"] == record_id
    assert payload["status"] == "ADVISORY"
    assert payload["advisory_only"] is True
    assert payload["runtime_stage"] == "prototype"
    assert payload["verification_mode"] == "advisory"
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert payload["human_review_required"] is bool(payload["warnings"])
    assert isinstance(payload["warnings"], list)
    assert "canonical_record" not in payload
    assert "generated_artifact" not in payload


def _assert_history_contract(history: dict[str, object], *, record_id: str) -> None:
    assert list(history.keys()) == EXPECTED_HISTORY_KEYS
    assert history["record_id"] == record_id
    assert history["advisory_only"] is True
    assert history["runtime_stage"] == "prototype"
    assert history["verification_mode"] == "advisory"
    assert history["public_safe"] is True
    assert history["traceable"] is True
    assert history["truth_guarantee"] is False
    assert history["human_review_required"] is bool(history["warnings"])
    assert isinstance(history["warnings"], list)


def _assert_telemetry_contract(payload: dict[str, object]) -> None:
    assert list(payload.keys()) == EXPECTED_TELEMETRY_KEYS
    assert payload["advisory_only"] is True
    assert payload["runtime_stage"] == "prototype"
    assert payload["verification_mode"] == "advisory"
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert payload["human_review_required"] is bool(payload["warnings"])
    assert isinstance(payload["warnings"], list)


def _assert_public_safe_no_authority_claims(payload: object) -> None:
    serialized = str(payload).lower()
    assert "secret" not in serialized
    assert "token" not in serialized
    assert "credential" not in serialized
    for forbidden in FORBIDDEN_AUTHORITY_TERMS:
        assert forbidden not in serialized


def test_degraded_runtime_state_remains_traceable_deterministic_and_advisory_only() -> None:
    record_id = "degraded-edge-record"

    payload, event_store, queue_store = _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://degraded-edge hash:ok degraded",
    )
    history = _history_response(record_id=record_id, event_store=event_store)
    telemetry = _telemetry_snapshot(event_store=event_store, queue_store=queue_store)

    _assert_advisory_contract(payload, record_id=record_id)
    _assert_history_contract(history, record_id=record_id)
    _assert_telemetry_contract(telemetry)
    assert payload["trust_state"] == TrustState.DEGRADED.value
    assert payload["degraded_runtime"] is True
    assert payload["recovery_mode"] is True
    assert payload["public_exposure"] == "restricted"
    assert telemetry["status"] == "degraded"
    assert telemetry["degraded_reasons"] == ["runtime_recovery_mode"]
    assert [event["event_type"] for event in history["events"]] == [
        "trust_state_transition",
        "continuity_checkpoint",
        "runtime_recovery_mode",
    ]
    assert any("degraded runtime restriction policy" in warning.lower() for warning in payload["warnings"])
    _assert_public_safe_no_authority_claims(
        {"payload": payload, "history": history, "telemetry": telemetry}
    )


def test_recovery_after_degraded_state_preserves_append_only_continuity() -> None:
    record_id = "recovered-advisory-record"
    event_store = RuntimeEventStore()

    degraded_payload, event_store, queue_store = _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://recover hash:ok degraded",
        event_store=event_store,
    )
    degraded_history = _history_response(record_id=record_id, event_store=event_store)
    degraded_events_snapshot = [event.copy() for event in degraded_history["events"]]

    recovered_payload, event_store, queue_store = _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://recover hash:ok",
        event_store=event_store,
        queue_store=queue_store,
    )
    recovered_history = _history_response(record_id=record_id, event_store=event_store)
    telemetry = _telemetry_snapshot(event_store=event_store, queue_store=queue_store)

    _assert_advisory_contract(degraded_payload, record_id=record_id)
    _assert_advisory_contract(recovered_payload, record_id=record_id)
    _assert_history_contract(recovered_history, record_id=record_id)
    _assert_telemetry_contract(telemetry)
    assert degraded_payload["degraded_runtime"] is True
    assert recovered_payload["degraded_runtime"] is False
    assert recovered_payload["recovery_mode"] is False
    assert recovered_payload["trust_state"] == TrustState.ADVISORY.value
    assert recovered_payload["public_exposure"] == "standard"
    assert recovered_history["events"][: len(degraded_events_snapshot)] == degraded_events_snapshot
    assert [event["event_type"] for event in recovered_history["events"][-2:]] == [
        "trust_state_transition",
        "continuity_checkpoint",
    ]
    assert all(event["advisory_only"] is True for event in recovered_history["events"])
    assert all(event["public_safe"] is True for event in recovered_history["events"])


def test_recovery_response_does_not_hide_prior_degraded_telemetry_visibility() -> None:
    record_id = "recovery-telemetry-visible-record"
    event_store = RuntimeEventStore()

    _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://recovery-visible hash:ok degraded",
        event_store=event_store,
    )
    recovered_payload, event_store, queue_store = _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://recovery-visible hash:ok",
        event_store=event_store,
    )
    recovered_history = _history_response(record_id=record_id, event_store=event_store)
    telemetry = _telemetry_snapshot(event_store=event_store, queue_store=queue_store)

    _assert_advisory_contract(recovered_payload, record_id=record_id)
    _assert_history_contract(recovered_history, record_id=record_id)
    _assert_telemetry_contract(telemetry)
    assert recovered_payload["degraded_runtime"] is False
    assert telemetry["status"] == "degraded"
    assert telemetry["degraded"] is True
    assert telemetry["degraded_events"] == 1
    assert telemetry["degraded_reasons"] == ["runtime_recovery_mode"]
    assert any(event["event_type"] == "runtime_recovery_mode" for event in recovered_history["events"])


def test_partial_queue_failure_keeps_replay_marker_visible_without_authority_escalation() -> None:
    record_id = "partial-queue-replay-record"
    queue_store = PartialQueueStore()

    payload, event_store, queue_store = _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://partial hash:ok degraded replay",
        queue_store=queue_store,
    )
    queue_store.drop_replay_warning_view()
    history = _history_response(record_id=record_id, event_store=event_store)
    telemetry = _telemetry_snapshot(event_store=event_store, queue_store=queue_store)

    _assert_advisory_contract(payload, record_id=record_id)
    _assert_history_contract(history, record_id=record_id)
    _assert_telemetry_contract(telemetry)
    assert payload["replay_warning"] is True
    assert history["replay_warning_visible"] is True
    assert any(event["event_type"] == "replay_warning" for event in history["events"])
    assert telemetry["replay_warning_queue"] == 0
    assert telemetry["degraded_queue_handling"] is True
    assert telemetry["truth_guarantee"] is False
    _assert_public_safe_no_authority_claims(
        {"payload": payload, "history": history, "telemetry": telemetry}
    )


def test_partial_telemetry_and_malformed_recovery_event_state_are_public_safe() -> None:
    record_id = "malformed-recovery-state-record"
    event_store = RuntimeEventStore()
    queue_store = RuntimeQueueStore()
    event_store.append_runtime_event(
        event_type="runtime_recovery_mode",
        record_id=record_id,
        details={"degraded_detected": "unknown", "recovery_mode": None},
    )

    history = _history_response(record_id=record_id, event_store=event_store)
    telemetry = _telemetry_snapshot(event_store=event_store, queue_store=queue_store)

    _assert_history_contract(history, record_id=record_id)
    _assert_telemetry_contract(telemetry)
    assert telemetry["status"] == "degraded"
    assert telemetry["degraded_events"] == 1
    assert telemetry["verification_queue"] == 0
    assert history["events"][0]["details"] == {"degraded_detected": "unknown", "recovery_mode": None}
    _assert_public_safe_no_authority_claims({"history": history, "telemetry": telemetry})


def test_missing_runtime_event_state_returns_stable_advisory_telemetry_shape() -> None:
    record_id = "missing-runtime-event-record"
    event_store = RuntimeEventStore()
    queue_store = RuntimeQueueStore()

    history = _history_response(record_id=record_id, event_store=event_store)
    telemetry = _telemetry_snapshot(event_store=event_store, queue_store=queue_store)

    _assert_history_contract(history, record_id=record_id)
    _assert_telemetry_contract(telemetry)
    assert telemetry["status"] == "ok"
    assert telemetry["degraded"] is False
    assert telemetry["degraded_reasons"] == []
    assert telemetry["degraded_events"] == 0
    assert history["events"] == []
    assert history["replay_warning_visible"] is False


def test_stable_advisory_response_during_degraded_mode_does_not_leak_sensitive_input() -> None:
    record_id = "stable-degraded-sensitive-record"
    qr_input = (
        "hc://stable-degraded hash:ok degraded replay "
        "token=SECRET-123 credential=SECRET-456"
    )

    first, event_store, queue_store = _run_isolated_qr_flow(record_id=record_id, qr_input=qr_input)
    second = _run_isolated_qr_flow(record_id=record_id, qr_input=qr_input)[0]
    history = _history_response(record_id=record_id, event_store=event_store)
    telemetry = _telemetry_snapshot(event_store=event_store, queue_store=queue_store)

    _assert_advisory_contract(first, record_id=record_id)
    _assert_advisory_contract(second, record_id=record_id)
    _assert_history_contract(history, record_id=record_id)
    _assert_telemetry_contract(telemetry)
    assert first == second
    assert first["replay_warning"] is True
    assert second["replay_warning"] is True
    assert history["replay_warning_visible"] is True
    assert any(event["event_type"] == "replay_warning" for event in history["events"])
    _assert_public_safe_no_authority_claims(first)
    _assert_public_safe_no_authority_claims(second)
    _assert_public_safe_no_authority_claims(history)
