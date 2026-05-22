from trust_orchestrator import orchestrate_trust_pipeline



def test_end_to_end_verified_pipeline():
    result = orchestrate_trust_pipeline(
        evidence_bundle={
            "hash": True,
            "provenance": True,
            "witness": True,
            "registry": True,
            "federation": True,
            "audit": True,
            "qr": True,
        },
        manipulation_signals={
            "repost_clusters": 0,
            "self_reference_loops": 0,
            "coordinated_signals": 0,
            "contamination_links": 0,
        },
        registry_trusted=True,
        federation_trusted=True,
        revoked=False,
    )

    assert result["evidence"]["decision"] == "VERIFIED"
    assert result["policy"]["decision"] == "ALLOW"
    assert result["risk"]["risk_level"] == "LOW"



def test_end_to_end_review_required_pipeline():
    result = orchestrate_trust_pipeline(
        evidence_bundle={
            "hash": True,
            "provenance": False,
            "witness": False,
            "registry": False,
            "federation": False,
        },
        manipulation_signals={
            "repost_clusters": 3,
            "self_reference_loops": 2,
            "coordinated_signals": 2,
            "contamination_links": 1,
        },
        registry_trusted=False,
        federation_trusted=False,
        revoked=False,
    )

    assert result["policy"]["decision"] == "REVIEW_REQUIRED"
    assert result["risk"]["risk_level"] in {"HIGH", "CRITICAL"}
