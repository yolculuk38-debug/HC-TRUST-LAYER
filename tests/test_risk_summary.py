from risk_summary import RiskLevel, build_risk_summary



def test_low_risk_summary():
    result = build_risk_summary()

    assert result["risk_level"] == RiskLevel.LOW



def test_critical_risk_summary():
    result = build_risk_summary(
        manipulation_result={
            "risk": "CRITICAL",
            "reasons": ["coordinated_manipulation_detected"],
        },
        revocation_result={
            "decision": "INVALID",
            "reasons": ["revoked"],
        },
        policy_result={
            "decision": "DENY",
            "reasons": ["revoked_record_or_certificate"],
        },
    )

    assert result["risk_level"] == RiskLevel.CRITICAL
