from hc_trust.api_schema import API_RESPONSE_VERSION, to_api_response, validate_verify_response
from hc_trust.result_formatter import format_trust_result
from hc_trust.trust_engine import TrustResult


def test_to_api_response_adds_api_version():
    trust_result = TrustResult(score=91, level="STRONG_VERIFIED", indicators=[])
    payload = format_trust_result(
        "HC-TEST-2026-0001",
        trust_result,
        verified_at="2026-05-20T13:00:00+00:00",
    )

    response = to_api_response(payload)

    assert response["api_version"] == API_RESPONSE_VERSION
    assert response["record_id"] == "HC-TEST-2026-0001"
    assert validate_verify_response(response) is True


def test_validate_verify_response_rejects_missing_required_field():
    response = {
        "api_version": API_RESPONSE_VERSION,
        "record_id": "HC-TEST-2026-0001",
        "verification_id": "VR-HC-TEST-2026-0001",
        "trust_score": 91,
        "trust_level": "STRONG_VERIFIED",
        "verified_at": "2026-05-20T13:00:00+00:00",
        "experimental": True,
    }

    assert validate_verify_response(response) is False


def test_validate_verify_response_rejects_out_of_range_score():
    response = {
        "api_version": API_RESPONSE_VERSION,
        "record_id": "HC-TEST-2026-0001",
        "verification_id": "VR-HC-TEST-2026-0001",
        "trust_score": 101,
        "trust_level": "STRONG_VERIFIED",
        "indicators": [],
        "verified_at": "2026-05-20T13:00:00+00:00",
        "experimental": True,
    }

    assert validate_verify_response(response) is False
