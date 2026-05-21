from public_validator import validate_public_proof


def test_valid_proof():
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

    assert result["decision"] == "VERIFIED"


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
