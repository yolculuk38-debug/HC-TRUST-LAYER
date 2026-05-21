from trust_passport import (
    TrustPassportStatus,
    build_trust_passport,
)


def verified_response():
    return {
        "decision": "VERIFIED",
        "trusted": True,
        "signals": {
            "trust_score": 95,
            "hash": True,
            "qr": True,
            "consensus": True,
            "audit": True,
            "signature": True,
        },
    }


def test_verified_passport():
    passport = build_trust_passport(
        "HC-1",
        verified_response(),
    )

    assert passport["status"] == TrustPassportStatus.VERIFIED


def test_review_required_due_to_risk_flags():
    passport = build_trust_passport(
        "HC-2",
        verified_response(),
        provenance_summary={"review_flags": ["edited_media"]},
    )

    assert passport["status"] == TrustPassportStatus.REVIEW_REQUIRED


def test_partial_passport():
    response = verified_response()
    response["decision"] = "PARTIAL"
    response["trusted"] = False
    response["signals"]["trust_score"] = 70

    passport = build_trust_passport("HC-3", response)
    assert passport["status"] == TrustPassportStatus.PARTIAL


def test_invalid_passport_input():
    passport = build_trust_passport("", {})
    assert passport["status"] == TrustPassportStatus.INVALID
