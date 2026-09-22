from offline_verifier import (
    create_demo_offline_package,
    verify_offline_proof_package,
)


def test_offline_verification_package():
    package = create_demo_offline_package("HC-OFFLINE-1")

    result = verify_offline_proof_package(package)

    assert result["offline_capable"] is True
    assert result["network_required"] is False
    assert result["validation"]["decision"] == "REVIEW_REQUIRED"
    assert result["validation"]["verified"] is False
    assert result["public_safe"] is False


def test_offline_result_stays_unverified_in_sdk_response():
    from sdk_response import build_sdk_verification_response

    result = verify_offline_proof_package(create_demo_offline_package("HC-SDK-DEMO"))
    response = build_sdk_verification_response(result)
    assert response["decision"] == "REVIEW_REQUIRED"
    assert response["verified"] is False
    assert response["verification_level"] is None
