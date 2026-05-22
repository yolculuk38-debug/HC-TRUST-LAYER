from policy_response_integration import build_policy_aware_response



def test_policy_allow_response():
    result = build_policy_aware_response(
        {
            "status": "VERIFIED",
            "trusted": True,
        },
        {
            "decision": "ALLOW",
            "reasons": [],
        },
    )

    assert result["policy_allowed"] is True



def test_policy_deny_response():
    result = build_policy_aware_response(
        {
            "status": "VERIFIED",
            "trusted": True,
        },
        {
            "decision": "DENY",
            "reasons": ["revoked_record_or_certificate"],
        },
    )

    assert result["trusted"] is False
    assert result["status"] == "INVALID"
