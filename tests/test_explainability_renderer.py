from explainability_renderer import render_explanation



def test_verified_explanation():
    result = render_explanation(
        decision="VERIFIED",
        trust_score=95,
        risk_level="LOW",
    )

    assert result["recommended_action"] == "TRUST_PASSPORT_VISIBLE"



def test_security_lock_explanation():
    result = render_explanation(
        decision="CRITICAL_LOCK",
        reasons=["critical_risk_detected"],
        risk_level="CRITICAL",
    )

    assert result["recommended_action"] == "SECURITY_LOCK"
