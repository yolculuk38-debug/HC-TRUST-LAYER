from explainable_trust_graph import build_trust_graph_explanation


def test_verified_trust_graph():
    result = build_trust_graph_explanation(
        {
            "decision": "VERIFIED",
            "evidence_score": 95,
            "reasons": [],
        }
    )

    assert result["decision"] == "VERIFIED"
    assert len(result["nodes"]) > 0
    assert len(result["edges"]) > 0


def test_review_required_trust_graph():
    result = build_trust_graph_explanation(
        {
            "decision": "REVIEW_REQUIRED",
            "evidence_score": 40,
            "reasons": ["missing_registry_signal"],
        }
    )

    assert "missing_registry_signal" in result["explanation"]
