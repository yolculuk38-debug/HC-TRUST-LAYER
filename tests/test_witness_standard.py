from witness_standard import (
    WitnessStandardStatus,
    create_witness_record,
    validate_witness_record,
)


def test_valid_ai_witness():
    witness = create_witness_record(
        "ai-1",
        "AI",
        "PASS",
        "2026-05-21T00:00:00Z",
        verification_method="model-review",
        confidence_score=92,
        provenance_reference="HC-REF-1",
        model_name="HC-GPT",
        witness_signature="signed",
    )

    result = validate_witness_record(witness)

    assert result["status"] == WitnessStandardStatus.VALID


def test_review_required_unsigned_witness():
    witness = create_witness_record(
        "human-1",
        "HUMAN",
        "PASS",
        "2026-05-21T00:00:00Z",
        verification_method="manual-review",
        confidence_score=80,
        reviewer_id="reviewer-a",
    )

    result = validate_witness_record(witness)

    assert result["status"] == WitnessStandardStatus.REVIEW_REQUIRED
    assert "unsigned_witness" in result["review_flags"]


def test_invalid_witness_type():
    witness = create_witness_record(
        "bad-1",
        "UNKNOWN",
        "PASS",
        "2026-05-21T00:00:00Z",
        verification_method="unknown",
        confidence_score=50,
    )

    result = validate_witness_record(witness)

    assert result["status"] == WitnessStandardStatus.INVALID
