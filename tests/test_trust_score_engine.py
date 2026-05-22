from trust_score_engine import TrustTier, calculate_trust_score



def test_verified_trust_score():
    result = calculate_trust_score(
        evidence_score=90,
        manipulation_risk="LOW",
        federation_weight=15,
        audit_continuity=True,
        provenance_continuity=True,
    )

    assert result["trust_tier"] == TrustTier.VERIFIED



def test_low_trust_score():
    result = calculate_trust_score(
        evidence_score=35,
        manipulation_risk="CRITICAL",
        federation_weight=0,
        audit_continuity=False,
        provenance_continuity=False,
    )

    assert result["trust_tier"] == TrustTier.LOW
    assert result["trust_score"] < 40
