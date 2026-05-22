from policy_engine import PolicyDecision, evaluate_policy


def test_allow_policy():
    result = evaluate_policy(
        evidence_score=95,
        manipulation_risk="LOW",
        registry_trusted=True,
        federation_trusted=True,
        revoked=False,
    )

    assert result["decision"] == PolicyDecision.ALLOW


def test_review_required_policy():
    result = evaluate_policy(
        evidence_score=40,
        manipulation_risk="HIGH",
        registry_trusted=False,
        federation_trusted=False,
        revoked=False,
    )

    assert result["decision"] == PolicyDecision.REVIEW_REQUIRED


def test_denied_policy():
    result = evaluate_policy(
        evidence_score=95,
        manipulation_risk="LOW",
        registry_trusted=True,
        federation_trusted=True,
        revoked=True,
    )

    assert result["decision"] == PolicyDecision.DENY
