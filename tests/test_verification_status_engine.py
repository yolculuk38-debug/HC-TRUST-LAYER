from verification_status_engine import (
    VerificationLevel,
    VerificationState,
    determine_verification_status,
)


def test_invalid_signal_state():
    result = determine_verification_status({"invalid": True})
    assert result["state"] == VerificationState.INVALID.value


def test_untrusted_without_hash():
    result = determine_verification_status({"hash_verified": False})
    assert result["state"] == VerificationState.UNTRUSTED.value


def test_partial_multi_witness_status():
    result = determine_verification_status(
        {
            "hash_verified": True,
            "witness_count": 3,
            "trust_score": 70,
        }
    )

    assert result["state"] == VerificationState.PARTIAL.value
    assert result["level"] == VerificationLevel.LEVEL_3_MULTI_WITNESS_VERIFIED.value


def test_verified_federated_status():
    result = determine_verification_status(
        {
            "hash_verified": True,
            "witness_count": 4,
            "provenance_locked": True,
            "federated_verified": True,
            "trust_score": 95,
        }
    )

    assert result["state"] == VerificationState.VERIFIED.value
    assert result["trusted"] is True
    assert result["level"] == VerificationLevel.LEVEL_5_FEDERATED_VERIFIED.value


def test_review_required_with_risk_flags():
    result = determine_verification_status(
        {
            "hash_verified": True,
            "witness_count": 3,
            "trust_score": 99,
            "risk_flags": ["edited_media"],
        }
    )

    assert result["state"] == VerificationState.REVIEW_REQUIRED.value
