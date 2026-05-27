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

    advisory_state, _ = engine.classify(pipeline.run(record_id="good", qr_input="value hash:ok"))
    review_state, _ = engine.classify(pipeline.run(record_id="needs-review", qr_input="value"))
    unresolved_state, _ = engine.classify(pipeline.run(record_id="empty", qr_input="  "))
    degraded_state, _ = engine.classify(pipeline.run(record_id="degraded-record", qr_input="value hash:ok"))

    assert advisory_state.value == "ADVISORY"
    assert review_state.value == "REVIEW_REQUIRED"
    assert unresolved_state.value == "UNRESOLVED"
    assert degraded_state.value == "DEGRADED"
