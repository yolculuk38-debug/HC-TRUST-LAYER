from mobile_verification_flow import (
    MobileTrustState,
    build_mobile_verification_view,
)



def test_mobile_verified_flow():
    result = build_mobile_verification_view(
        qr_payload={"record_id": "REC-1"},
        validation_result={
            "decision": "VERIFIED",
            "trusted": True,
        },
    )

    assert result["trust_state"] == MobileTrustState.VERIFIED



def test_mobile_review_flow():
    result = build_mobile_verification_view(
        qr_payload={"record_id": "REC-2"},
        validation_result={
            "decision": "REVIEW_REQUIRED",
            "trusted": False,
        },
    )

    assert result["trust_state"] == MobileTrustState.REVIEW_REQUIRED
