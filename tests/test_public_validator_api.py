from public_validator_api import (
    build_validator_api_request,
    build_validator_api_response,
    validate_validator_api_request,
)



def test_valid_validator_api_request():
    request = build_validator_api_request(
        request_id="REQ-1",
        portable_package={"record_id": "REC-1"},
        client_type="BROWSER_EXTENSION",
    )

    result = validate_validator_api_request(request)

    assert result["valid"] is True



def test_validator_api_response():
    response = build_validator_api_response(
        request_id="REQ-1",
        decision="VERIFIED",
        trusted=True,
        trust_score=95,
        risk_level="LOW",
        reasons=[],
    )

    assert response["trusted"] is True
    assert response["portable"] is True
