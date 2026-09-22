from public_validator import validate_public_proof

import pytest


def test_forged_signature_strings_cannot_verify_a_proof():
    result = validate_public_proof(
        {
            "record_id": "HC-VALID-1",
            "content_hash": "abc123",
            "content_hash_valid": True,
            "verification_level": "LEVEL_3_MULTI_WITNESS_VERIFIED",
            "trust_passport": {"status": "VERIFIED"},
            "witnesses": [
                {
                    "witness_signature": "sig1",
                    "provenance_reference": "prov1",
                },
                {
                    "witness_signature": "sig2",
                    "provenance_reference": "prov2",
                },
            ],
        }
    )

    assert result["decision"] == "REVIEW_REQUIRED"
    assert result["verified"] is False
    assert result["content_hash_checked"] is False
    assert result["signature_verified"] is False
    assert result["witnesses_verified"] is False
    assert result["verification_level"] is None
    assert result["source_claims"]["verification_level"] == "LEVEL_3_MULTI_WITNESS_VERIFIED"


def test_invalid_hash():
    result = validate_public_proof(
        {
            "record_id": "HC-INVALID-HASH",
            "content_hash": "bad",
            "content_hash_valid": False,
            "verification_level": "LEVEL_1_HASH_VERIFIED",
            "trust_passport": {},
        }
    )

    assert result["decision"] == "INVALID"
    assert "invalid_content_hash" in result["reasons"]


def test_broken_revision_chain():
    result = validate_public_proof(
        {
            "record_id": "HC-CHAIN",
            "content_hash": "abc",
            "content_hash_valid": True,
            "verification_level": "LEVEL_2_WITNESS_REVIEWED",
            "trust_passport": {},
            "revision_chain": {"broken": True},
        }
    )

    assert result["decision"] == "INVALID"


def test_missing_witness_signature():
    result = validate_public_proof(
        {
            "record_id": "HC-WITNESS",
            "content_hash": "abc",
            "content_hash_valid": True,
            "verification_level": "LEVEL_2_WITNESS_REVIEWED",
            "trust_passport": {},
            "witnesses": [
                {
                    "provenance_reference": "prov1",
                }
            ],
        }
    )

    assert result["decision"] == "REVIEW_REQUIRED"


def test_conflicting_witnesses():
    result = validate_public_proof(
        {
            "record_id": "HC-CONFLICT",
            "content_hash": "abc",
            "content_hash_valid": True,
            "verification_level": "LEVEL_3_MULTI_WITNESS_VERIFIED",
            "trust_passport": {},
            "witnesses": [
                {
                    "witness_signature": "sig1",
                    "provenance_reference": "prov1",
                    "conflict": True,
                }
            ],
        }
    )

    assert result["decision"] == "INVALID"


def test_missing_provenance_reference():
    result = validate_public_proof(
        {
            "record_id": "HC-PROVENANCE",
            "content_hash": "abc",
            "content_hash_valid": True,
            "verification_level": "LEVEL_2_WITNESS_REVIEWED",
            "trust_passport": {},
            "witnesses": [
                {
                    "witness_signature": "sig1",
                }
            ],
        }
    )

    assert result["decision"] == "REVIEW_REQUIRED"


@pytest.mark.parametrize("change", [
    {"revision_chain": None}, {"revision_chain": []},
    {"witnesses": "signature"}, {"witnesses": {}}, {"witnesses": [None]},
    {"trust_passport": "VERIFIED"}, {"verification_level": {}},
    {"record_id": []}, {"content_hash": ""},
])
def test_malformed_nested_input_fails_closed(change):
    proof = {"record_id": "HC-DEMO", "content_hash": "declared", "trust_passport": {}}
    result = validate_public_proof({**proof, **change})
    assert result["decision"] == "INVALID"
    assert result["verified"] is False
    assert result["signature_verified"] is False


@pytest.mark.parametrize("witness_count", [0, 1, 2, 20])
def test_caller_success_flags_and_witness_counts_never_grant_trust(witness_count):
    result = validate_public_proof({
        "record_id": "HC-DEMO", "content_hash": "declared",
        "trust_passport": {"status": "VERIFIED"},
        "verification_level": "LEVEL_3_MULTI_WITNESS_VERIFIED",
        "verified": True, "trusted": True, "signature_verified": True,
        "content_hash_valid": True, "content_hash_checked": True,
        "witnesses": [{"witness_signature": "fake", "provenance_reference": "fake"}] * witness_count,
    })
    assert result["decision"] == "REVIEW_REQUIRED"
    for name in ("verified", "trusted", "signature_verified", "witnesses_verified",
                 "identity_verified", "content_hash_checked", "content_hash_valid",
                 "source_claims_verified", "public_safe", "truth_guarantee"):
        assert result[name] is False
