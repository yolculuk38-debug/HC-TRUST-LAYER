from trust_badge import (
    TrustBadgeState,
    build_trust_badge,
)



def test_verified_trust_badge():
    result = build_trust_badge(
        record_id="REC-1",
        decision="VERIFIED",
        trusted=True,
        trust_score=95,
    )

    assert result["badge_state"] == TrustBadgeState.VERIFIED



def test_review_required_trust_badge():
    result = build_trust_badge(
        record_id="REC-2",
        decision="REVIEW_REQUIRED",
        trusted=False,
    )

    assert result["badge_state"] == TrustBadgeState.REVIEW_REQUIRED
