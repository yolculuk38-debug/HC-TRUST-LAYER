from hc_trust.evidence_weight import calculate_evidence_weight


def test_verified_hash_weight():
    result = calculate_evidence_weight([
        {"type": "hash", "verified": True}
    ])

    assert result["evidence_score"] == 40


def test_unverified_evidence_rejected():
    result = calculate_evidence_weight([
        {"type": "human_witness", "verified": False}
    ])

    assert result["evidence_score"] == 0
    assert "unverified_human_witness" in result["rejected_evidence"]


def test_score_is_bounded():
    result = calculate_evidence_weight([
        {"type": "hash", "verified": True},
        {"type": "signature", "verified": True},
        {"type": "institution_witness", "verified": True},
        {"type": "human_witness", "verified": True},
        {"type": "ai_witness", "verified": True},
        {"type": "system_witness", "verified": True},
    ])

    assert result["evidence_score"] <= 100
