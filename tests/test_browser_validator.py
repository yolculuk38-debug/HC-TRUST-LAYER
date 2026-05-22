from browser_validator import (
    BadgeState,
    build_browser_validation_view,
)



def test_verified_browser_view():
    result = build_browser_validation_view(
        {
            "decision": "VERIFIED",
            "trusted": True,
        }
    )

    assert result["badge_state"] == BadgeState.VERIFIED



def test_review_required_browser_view():
    result = build_browser_validation_view(
        {
            "decision": "REVIEW_REQUIRED",
            "trusted": False,
            "reasons": ["policy_review_required"],
        }
    )

    assert result["badge_state"] == BadgeState.REVIEW_REQUIRED
