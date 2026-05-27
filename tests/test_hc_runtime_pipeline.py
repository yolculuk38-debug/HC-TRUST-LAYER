"""Tests for HC:// advisory validator pipeline and decision engine."""

from hc_runtime.runtime import TrustStateDecisionEngine, ValidatorPipeline


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
