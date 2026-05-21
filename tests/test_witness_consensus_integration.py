from witness_consensus_integration import evaluate_witness_consensus
from witness_standard import create_witness_record


def ai_witness(witness_id: str, verdict: str = "PASS"):
    return create_witness_record(
        witness_id,
        "AI",
        verdict,
        "2026-05-21T00:00:00Z",
        verification_method="model-review",
        confidence_score=90,
        provenance_reference="hash-1",
        model_name="HC-GPT",
        witness_signature="signed",
    )


def test_consensus_success():
    result = evaluate_witness_consensus(
        [
            ai_witness("w1"),
            ai_witness("w2"),
            ai_witness("w3"),
        ]
    )

    assert result["consensus"]["consensus_reached"] is True


def test_invalid_witness_filtered():
    broken = ai_witness("bad")
    broken["witness_type"] = "BROKEN"

    result = evaluate_witness_consensus(
        [
            ai_witness("w1"),
            broken,
            ai_witness("w2"),
            ai_witness("w3"),
        ]
    )

    assert result["valid_witness_count"] == 3
