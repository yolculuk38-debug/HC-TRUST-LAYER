"""Replay and continuity edge-case coverage for HC:// advisory runtime behavior."""

from __future__ import annotations

from copy import deepcopy

from hc_runtime.contracts.responses import advisory_response
from hc_runtime.decision_engine import TrustState, TrustStateDecisionEngine
from hc_runtime.events import RuntimeEventStore
from hc_runtime.runtime import RuntimePolicyEngine, RuntimeQueueStore, ValidatorPipeline


EXPECTED_RUNTIME_RESPONSE_KEYS = [
    "status",
    "advisory_only",
    "public_safe",
    "message",
    "warnings",
    "traceable",
    "truth_guarantee",
    "record_id",
    "trust_state",
    "replay_warning",
    "continuity_warning",
    "degraded_runtime",
    "recovery_mode",
    "public_exposure",
]

EXPECTED_HISTORY_KEYS = {
    "record_id",
    "advisory_only",
    "public_safe",
    "traceable",
    "truth_guarantee",
    "warnings",
    "replay_warning_visible",
    "trust_state_transitions",
    "events",
}


def _run_isolated_qr_flow(
    *,
    record_id: str,
    qr_input: str,
    event_store: RuntimeEventStore | None = None,
) -> tuple[dict[str, object], RuntimeEventStore]:
    """Exercise the runtime components without mutating shared app state."""
    queue_store = RuntimeQueueStore()
    pipeline = ValidatorPipeline()
    decision_engine = TrustStateDecisionEngine()
    policy_engine = RuntimePolicyEngine()
    event_store = event_store or RuntimeEventStore()

    queue_store.enqueue_verification({"record_id": record_id, "qr_input": qr_input})
    pipeline_result = pipeline.run(record_id=record_id, qr_input=qr_input)
    replay_warning = "replay" in qr_input.lower()
    continuity_ok = "continuity-warning" not in qr_input.lower() and "continuity-warning" not in record_id.lower()
    degraded_mode = "degraded" in qr_input.lower() or "degraded" in record_id.lower() or not continuity_ok

    trust_state, warnings = decision_engine.classify(
        record_id=record_id,
        qr_input=qr_input,
        schema_valid=pipeline_result["schema_result"]["valid"],
        hash_verified=pipeline_result["hash_result"]["hash_verified"],
        continuity_ok=continuity_ok,
        replay_warning=replay_warning,
    )

    policy = policy_engine.evaluate(trust_state=trust_state, replay_warning=replay_warning, degraded_mode=degraded_mode)
    warnings = [*warnings, *policy["warnings"]]

    event_store.append_trust_transition(record_id=record_id, trust_state=trust_state.value, warnings=warnings)
    event_store.append_continuity_checkpoint(record_id=record_id, continuity_ok=continuity_ok, warnings=warnings)

    if replay_warning:
        queue_store.enqueue_replay_warning({"record_id": record_id, "source": "qr-verification"})
        queue_store.enqueue_escalation({"record_id": record_id, "reason": "replay_warning"})
        event_store.append_replay_warning(record_id=record_id, reason="Replay marker detected in advisory QR input.")

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
    return payload, event_store


def _history_response(*, record_id: str, event_store: RuntimeEventStore) -> dict[str, object]:
    events = event_store.history(record_id)
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


def _assert_advisory_runtime_contract(payload: dict[str, object], *, record_id: str) -> None:
    assert list(payload.keys()) == EXPECTED_RUNTIME_RESPONSE_KEYS
    assert payload["record_id"] == record_id
    assert payload["status"] == "ADVISORY"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert "canonical_record" not in payload
    assert "generated_artifact" not in payload


def _assert_no_secret_or_token_exposure(payload: object) -> None:
    serialized = str(payload).lower()
    assert "secret" not in serialized
    assert "token" not in serialized
    assert "credential" not in serialized


def test_duplicate_verification_input_is_deterministic_and_advisory_only() -> None:
    record_id = "duplicate-replay-edge-record"
    qr_input = "hc://duplicate-replay-edge-record hash:ok replay"

    first = _run_isolated_qr_flow(record_id=record_id, qr_input=qr_input)[0]
    second = _run_isolated_qr_flow(record_id=record_id, qr_input=qr_input)[0]

    _assert_advisory_runtime_contract(first, record_id=record_id)
    _assert_advisory_runtime_contract(second, record_id=record_id)
    assert first == second
    assert first["replay_warning"] is True
    assert first["trust_state"] == TrustState.REPLAY_WARNING.value
    assert first["public_exposure"] == "restricted"
    assert any("Replay warning" in warning for warning in first["warnings"])
    assert any("Human-supervised validation" in warning for warning in first["warnings"])


def test_stale_replayed_input_keeps_warning_visible_without_authority_escalation() -> None:
    record_id = "stale-replayed-advisory-record"
    payload = _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://stale-replayed-advisory-record hash:ok replay stale observed-at:2020-01-01",
    )[0]

    _assert_advisory_runtime_contract(payload, record_id=record_id)
    assert payload["replay_warning"] is True
    assert payload["trust_state"] == TrustState.REPLAY_WARNING.value
    assert payload["truth_guarantee"] is False
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert all("objective truth" not in warning.lower() for warning in payload["warnings"])
    assert all("autonomous" not in warning.lower() for warning in payload["warnings"])
    assert any("Replay warning" in warning for warning in payload["warnings"])


def test_missing_event_history_returns_stable_empty_public_safe_shape() -> None:
    record_id = "missing-history-edge-record-with-no-events"

    history = _history_response(record_id=record_id, event_store=RuntimeEventStore())

    assert set(history.keys()) == EXPECTED_HISTORY_KEYS
    assert history["record_id"] == record_id
    assert history["advisory_only"] is True
    assert history["public_safe"] is True
    assert history["traceable"] is True
    assert history["truth_guarantee"] is False
    assert history["warnings"] == []
    assert history["replay_warning_visible"] is False
    assert history["trust_state_transitions"] == []
    assert history["events"] == []


def test_continuity_ordering_is_append_only_and_deterministic() -> None:
    store = RuntimeEventStore()
    record_id = "continuity-ordering-edge-record"

    trust_event = store.append_trust_transition(
        record_id=record_id,
        trust_state=TrustState.DEGRADED.value,
        warnings=["Continuity warning detected in advisory runtime flow."],
    )
    trust_event_snapshot = deepcopy(trust_event)
    store.append_continuity_checkpoint(
        record_id=record_id,
        continuity_ok=False,
        warnings=["Continuity warning detected in advisory runtime flow."],
    )
    store.append_replay_warning(record_id=record_id, reason="Replay marker detected in advisory QR input.")

    history = store.history(record_id)

    assert [event["event_type"] for event in history] == [
        "trust_state_transition",
        "continuity_checkpoint",
        "replay_warning",
    ]
    assert history[0] == trust_event_snapshot
    assert history[1]["details"]["continuity_ok"] is False
    assert history[2]["details"]["reason"] == "Replay marker detected in advisory QR input."
    assert all(event["advisory_only"] is True for event in history)
    assert all(event["public_safe"] is True for event in history)


def test_replay_warning_visibility_is_preserved_in_public_history() -> None:
    record_id = "replay-visibility-edge-record"

    response, event_store = _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://replay-visibility-edge-record hash:ok replay",
    )
    history = _history_response(record_id=record_id, event_store=event_store)

    _assert_advisory_runtime_contract(response, record_id=record_id)
    assert set(history.keys()) == EXPECTED_HISTORY_KEYS
    assert history["replay_warning_visible"] is True
    assert len(history["trust_state_transitions"]) >= 1
    assert any(event["event_type"] == "replay_warning" for event in history["events"])
    assert all(event["advisory_only"] is True for event in history["events"])
    assert all(event["public_safe"] is True for event in history["events"])


def test_event_history_consistency_for_replay_and_continuity_markers() -> None:
    record_id = "event-history-consistency-edge-record"

    _, event_store = _run_isolated_qr_flow(
        record_id=record_id,
        qr_input="hc://event-history-consistency-edge-record hash:ok replay continuity-warning",
    )
    history = _history_response(record_id=record_id, event_store=event_store)
    events = history["events"]

    assert [event["event_type"] for event in events] == [
        "trust_state_transition",
        "continuity_checkpoint",
        "replay_warning",
        "runtime_recovery_mode",
    ]
    assert history["replay_warning_visible"] is True
    assert history["trust_state_transitions"] == [events[0]]
    assert events[0]["details"]["trust_state"] == TrustState.REPLAY_WARNING.value
    assert any("Replay warning" in warning for warning in events[0]["details"]["warnings"])
    assert events[1]["details"]["continuity_ok"] is False
    assert events[3]["details"] == {"degraded_detected": True, "recovery_mode": True, "failover_safe": True}


def test_malformed_continuity_state_is_handled_as_safe_degraded_advisory_state() -> None:
    engine = TrustStateDecisionEngine()

    trust_state, warnings = engine.classify(
        record_id="malformed-continuity-edge-record",
        qr_input="hc://malformed-continuity-edge-record hash:ok",
        schema_valid=True,
        hash_verified=True,
        continuity_ok=False,
        replay_warning=False,
    )

    assert trust_state is TrustState.DEGRADED
    assert warnings == [
        "Continuity warning detected in advisory runtime flow.",
        "Human-supervised validation is required before trust interpretation.",
    ]
    assert all("objective truth" not in warning.lower() for warning in warnings)
    assert all("autonomous" not in warning.lower() for warning in warnings)


def test_replay_markers_are_deterministic_and_do_not_expose_secret_input_text() -> None:
    record_id = "redacted-replay-edge-record"
    qr_input = "hc://redacted-replay-edge-record hash:ok replay token=SECRET-123 credential=SECRET-456"

    first, event_store = _run_isolated_qr_flow(record_id=record_id, qr_input=qr_input)
    second = _run_isolated_qr_flow(record_id=record_id, qr_input=qr_input)[0]
    public_history = _history_response(record_id=record_id, event_store=event_store)

    assert first == second
    _assert_advisory_runtime_contract(first, record_id=record_id)
    assert first["replay_warning"] is True
    assert first["truth_guarantee"] is False
    assert first["public_safe"] is True
    _assert_no_secret_or_token_exposure(first)
    _assert_no_secret_or_token_exposure(public_history)
