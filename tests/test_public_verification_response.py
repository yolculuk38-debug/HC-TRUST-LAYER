from public_verification_response import build_public_verification_response


def test_verified_public_response():
    response = build_public_verification_response(
        {
            "record_id": "HC-1",
            "status": "VERIFIED",
            "trusted": True,
            "trust_score": 95,
            "verification_level": "LEVEL_5_FEDERATED_VERIFIED",
            "summary": {"hash": True},
        }
    )

    assert response["status"] == "VERIFIED"
    assert response["trusted"] is True


def test_review_required_public_response():
    response = build_public_verification_response(
        {
            "record_id": "HC-2",
            "status": "PARTIAL",
            "trusted": False,
            "risk_flags": ["edited_media"],
        }
    )

    assert response["status"] == "REVIEW_REQUIRED"


def test_invalid_public_response():
    response = build_public_verification_response(None)

    assert response["status"] == "INVALID"
