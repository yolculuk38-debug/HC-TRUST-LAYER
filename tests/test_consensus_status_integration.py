from consensus_status_integration import consensus_to_status


def test_consensus_reached_status():
    result = consensus_to_status(
        {
            "status": "CONSENSUS_REACHED",
            "witness_count": 4,
        },
        base_signals={
            "provenance_locked": True,
            "trust_score": 95,
        },
    )

    assert result["status_result"]["state"] == "VERIFIED"


def test_partial_consensus_requires_review():
    result = consensus_to_status(
        {
            "status": "PARTIAL_CONSENSUS",
            "witness_count": 2,
        }
    )

    assert result["status_result"]["state"] == "REVIEW_REQUIRED"


def test_conflict_forces_invalid():
    result = consensus_to_status(
        {
            "status": "CONFLICT",
            "witness_count": 5,
        },
        base_signals={
            "hash_verified": True,
            "trust_score": 99,
        },
    )

    assert result["status_result"]["state"] == "INVALID"
