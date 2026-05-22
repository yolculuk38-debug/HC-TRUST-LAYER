from trust_orchestrator import orchestrate_trust_pipeline



def test_trust_orchestrator_pipeline():
    result = orchestrate_trust_pipeline(
        evidence_bundle={
            "hash": True,
            "provenance": True,
            "witness": True,
            "registry": True,
            "federation": True,
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

    assert "evidence" in result
    assert "manipulation" in result
    assert "policy" in result
    assert "risk" in result
