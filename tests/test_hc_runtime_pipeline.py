"""Tests for HC:// advisory validator pipeline and decision engine."""

from hc_runtime.events import RuntimeEventStore
from hc_runtime.decision_engine import TrustState
from hc_runtime.runtime import RuntimeQueueStore, TrustStateDecisionEngine, ValidatorPipeline


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
