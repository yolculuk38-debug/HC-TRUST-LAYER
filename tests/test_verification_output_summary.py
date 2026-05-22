from verification_output_summary import (
    build_output_summary,
    validate_output_summary,
)



def test_valid_output_summary():
    summary = build_output_summary(
        record_id="REC-1",
        decision="VERIFIED",
        trusted=True,
        trust_score=97,
    )

    result = validate_output_summary(summary)

    assert result["valid"] is True



def test_invalid_output_summary():
    result = validate_output_summary(
        {
            "record_id": "REC-2",
        }
    )

    assert result["valid"] is False
