"""Tests for HC:// advisory validator pipeline and decision engine."""

from copy import deepcopy

from hc_runtime.events import RuntimeEventStore
from hc_runtime.decision_engine import TrustState
from hc_runtime.runtime import RuntimePolicyEngine, RuntimeQueueStore, TrustStateDecisionEngine, ValidatorPipeline


def test_validator_pipeline_hooks_execute() -> None:
    pipeline = ValidatorPipeline()

    result = pipeline.run(record_id="r1", qr_input="hc://sample hash:ok")

    assert result["schema_result"]["checked"] is True
    assert result["hash_result"]["checked"] is True
    assert result["escalation"]["placeholder"] is True


def test_decision_engine_supports_required_states() -> None:
    pipeline = ValidatorPipeline()
    engine = TrustStateDecisionEngine()

    advisory_state, _ = engine.classify(
        record_id="good",
        qr_input="value hash:ok",
        schema_valid=True,
        hash_verified=True,
        continuity_ok=True,
        replay_warning=False,
    )
    review_state, _ = engine.classify(
        record_id="needs-review",
        qr_input="value",
        schema_valid=True,
        hash_verified=False,
        continuity_ok=True,
        replay_warning=False,
    )
    unresolved_state, _ = engine.classify(
        record_id="empty",
        qr_input="  ",
        schema_valid=False,
        hash_verified=False,
        continuity_ok=True,
        replay_warning=False,
    )
    degraded_state, _ = engine.classify(
        record_id="degraded-record",
        qr_input="value hash:ok",
        schema_valid=True,
        hash_verified=True,
        continuity_ok=True,
        replay_warning=False,
    )
    replay_state, _ = engine.classify(
        record_id="replay-record",
        qr_input="value hash:ok replay",
        schema_valid=True,
        hash_verified=True,
        continuity_ok=True,
        replay_warning=True,
    )

    assert advisory_state.value == "ADVISORY"
    assert review_state.value == "REVIEW_REQUIRED"
    assert unresolved_state.value == "UNRESOLVED"
    assert degraded_state.value == "DEGRADED"
    assert replay_state.value == "REPLAY_WARNING"


def test_validator_pipeline_consistency_for_input_variants() -> None:
    pipeline = ValidatorPipeline()
    engine = TrustStateDecisionEngine()

    cases = [
        ("empty", "", False, False),
        ("normal", "hc://normal", True, False),
        ("hash-marked", "hc://normal hash:abc", True, True),
        ("repeated-same-input", "hc://normal hash:abc", True, True),
    ]

    for record_id, qr_input, expected_schema_valid, expected_hash in cases:
        result = pipeline.run(record_id=record_id, qr_input=qr_input)
        assert set(result.keys()) == {"record_id", "schema_result", "hash_result", "trust_assignment", "escalation"}
        assert result["schema_result"]["valid"] is expected_schema_valid
        assert result["hash_result"]["hash_verified"] is expected_hash
        assert isinstance(result["trust_assignment"]["warnings"], list)
        assert set(result["escalation"].keys()) == {"route", "required", "placeholder"}
        assert result["escalation"]["placeholder"] is True

        trust_state, warnings = engine.classify(
            record_id=record_id,
            qr_input=qr_input,
            schema_valid=result["schema_result"]["valid"],
            hash_verified=result["hash_result"]["hash_verified"],
            continuity_ok=True,
            replay_warning="replay" in qr_input.lower(),
        )

        if not qr_input.strip():
            assert trust_state is TrustState.UNRESOLVED
        elif "hash:" in qr_input.lower():
            assert trust_state is TrustState.ADVISORY
        else:
            assert trust_state is TrustState.REVIEW_REQUIRED

        assert isinstance(warnings, list)
        assert all(isinstance(warning, str) for warning in warnings)


def test_runtime_policy_layer_cannot_silently_override_validator_semantics() -> None:
    pipeline = ValidatorPipeline()
    engine = TrustStateDecisionEngine()

    pipeline_result = pipeline.run(record_id="boundary-record", qr_input="")
    assert pipeline_result["schema_result"]["valid"] is False
    assert pipeline_result["hash_result"]["hash_verified"] is False

    trust_state, warnings = engine.classify(
        record_id="boundary-record",
        qr_input="",
        schema_valid=pipeline_result["schema_result"]["valid"],
        hash_verified=pipeline_result["hash_result"]["hash_verified"],
        continuity_ok=True,
        replay_warning=False,
    )

    assert trust_state is TrustState.UNRESOLVED
    assert any("schema" in warning.lower() or "hash" in warning.lower() for warning in warnings)


def test_validator_escalation_routing_is_deterministic_for_identical_inputs() -> None:
    pipeline = ValidatorPipeline()

    first = pipeline.run(record_id="det-route", qr_input="hc://det-route")
    second = pipeline.run(record_id="det-route", qr_input="hc://det-route")

    assert first["escalation"] == second["escalation"]
    assert first["escalation"]["route"] == "human-supervised-validation"
    assert first["escalation"]["required"] is True
    assert first["escalation"]["placeholder"] is True


def test_runtime_queue_store_instances_are_state_isolated() -> None:
    first_store = RuntimeQueueStore()
    second_store = RuntimeQueueStore()

    first_store.enqueue_verification({"record_id": "r1"})
    first_store.enqueue_escalation({"record_id": "r1", "reason": "check"})
    first_store.enqueue_replay_warning({"record_id": "r1"})

    assert len(first_store.verification_queue) == 1
    assert len(first_store.escalation_queue) == 1
    assert len(first_store.replay_warning_queue) == 1
    assert second_store.verification_queue == []
    assert second_store.escalation_queue == []
    assert second_store.replay_warning_queue == []


def test_runtime_event_store_history_ordering_is_deterministic() -> None:
    store = RuntimeEventStore()
    record_id = "history-order-record"

    store.append_trust_transition(record_id=record_id, trust_state="ADVISORY", warnings=[])
    store.append_continuity_checkpoint(record_id=record_id, continuity_ok=True, warnings=[])
    store.append_replay_warning(record_id=record_id, reason="Replay marker detected.")

    history = store.history(record_id=record_id)
    assert [event["event_type"] for event in history] == [
        "trust_state_transition",
        "continuity_checkpoint",
        "replay_warning",
    ]
    assert all(event["advisory_only"] is True for event in history)
    assert all(event["public_safe"] is True for event in history)


def test_runtime_event_store_is_append_only_and_preserves_previous_events() -> None:
    store = RuntimeEventStore()
    record_id = "append-only-record"

    first_event = store.append_trust_transition(record_id=record_id, trust_state="ADVISORY", warnings=["w1"])
    first_event_snapshot = deepcopy(first_event)

    store.append_continuity_checkpoint(record_id=record_id, continuity_ok=True, warnings=[])
    store.append_replay_warning(record_id=record_id, reason="Replay marker detected.")

    history = store.history(record_id=record_id)
    assert len(history) == 3
    assert history[0] == first_event_snapshot
    assert history[0]["details"]["warnings"] == ["w1"]


def test_runtime_event_store_replay_and_continuity_history_is_deterministic() -> None:
    store = RuntimeEventStore()
    record_id = "deterministic-replay-record"

    store.append_trust_transition(record_id=record_id, trust_state="REPLAY_WARNING", warnings=["Replay warning active."])
    store.append_continuity_checkpoint(record_id=record_id, continuity_ok=False, warnings=["Continuity warning active."])
    store.append_replay_warning(record_id=record_id, reason="Replay marker detected.")

    history = store.history(record_id=record_id)
    assert [event["event_type"] for event in history] == [
        "trust_state_transition",
        "continuity_checkpoint",
        "replay_warning",
    ]
    assert history[0]["details"]["trust_state"] == "REPLAY_WARNING"
    assert history[1]["details"]["continuity_ok"] is False
    assert history[2]["details"]["reason"] == "Replay marker detected."


def test_runtime_policy_determinism_for_identical_advisory_inputs() -> None:
    engine = TrustStateDecisionEngine()

    advisory_state, _ = engine.classify(
        record_id="deterministic-advisory-record",
        qr_input="hc://deterministic hash:ok",
        schema_valid=True,
        hash_verified=True,
        continuity_ok=True,
        replay_warning=False,
    )
    first = RuntimePolicyEngine().evaluate(trust_state=advisory_state, replay_warning=False, degraded_mode=False)
    second = RuntimePolicyEngine().evaluate(trust_state=advisory_state, replay_warning=False, degraded_mode=False)

    assert first == second
    assert first["advisory_downgrade"] is False
    assert first["degraded_runtime_restriction"] is False
    assert first["replay_warning_escalation"] is False
    assert first["public_exposure"] == "standard"


def test_runtime_policy_degraded_and_replay_controls_are_deterministic() -> None:
    policy_engine = RuntimePolicyEngine()
    degraded_state = TrustState.DEGRADED

    degraded_first = policy_engine.evaluate(trust_state=degraded_state, replay_warning=False, degraded_mode=True)
    degraded_second = policy_engine.evaluate(trust_state=degraded_state, replay_warning=False, degraded_mode=True)
    replay_first = policy_engine.evaluate(trust_state=TrustState.REPLAY_WARNING, replay_warning=True, degraded_mode=False)
    replay_second = policy_engine.evaluate(
        trust_state=TrustState.REPLAY_WARNING,
        replay_warning=True,
        degraded_mode=False,
    )

    assert degraded_first == degraded_second
    assert replay_first == replay_second
    assert degraded_first["degraded_runtime_restriction"] is True
    assert replay_first["replay_warning_escalation"] is True
    assert degraded_first["advisory_downgrade"] is True
    assert replay_first["advisory_downgrade"] is True
