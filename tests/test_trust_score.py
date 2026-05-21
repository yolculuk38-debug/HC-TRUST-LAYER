from trust_score import calculate_trust_score


def test_high_trust_score():
    result = calculate_trust_score(
        {
            "verified_hash": True,
            "qr_verified": True,
            "signed": True,
            "audit_snapshot": True,
            "export_verified": True,
            "consensus_reached": True,
            "witness_count": 5,
        }
    )

    assert result["trust_level"] == "HIGH"
    assert result["trusted"] is True


def test_moderate_trust_score():
    result = calculate_trust_score(
        {
            "verified_hash": True,
            "signed": True,
            "witness_count": 2,
        }
    )

    assert result["trust_level"] in {"MODERATE", "LOW"}


def test_untrusted_score_with_conflicts():
    result = calculate_trust_score(
        {
            "verified_hash": False,
            "conflict_count": 3,
            "unsafe_flags": 2,
        }
    )

    assert result["trust_level"] == "UNTRUSTED"
    assert result["trusted"] is False


def test_score_clamped_to_maximum():
    result = calculate_trust_score(
        {
            "verified_hash": True,
            "qr_verified": True,
            "signed": True,
            "audit_snapshot": True,
            "export_verified": True,
            "consensus_reached": True,
            "witness_count": 100,
        }
    )

    assert result["trust_score"] <= 100


def test_score_clamped_to_minimum():
    result = calculate_trust_score(
        {
            "conflict_count": 100,
            "unsafe_flags": 100,
        }
    )

    assert result["trust_score"] >= 0
