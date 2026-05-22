from evidence_engine import EvidenceDecision, evaluate_evidence_bundle


def test_verified_evidence_bundle():
    result = evaluate_evidence_bundle(
        {
            "hash": True,
            "provenance": True,
            "witness": True,
            "registry": True,
            "federation": True,
            "audit": True,
            "qr": True,
        }
    )

    assert result["decision"] == EvidenceDecision.VERIFIED


def test_partial_evidence_bundle():
    result = evaluate_evidence_bundle(
        {
            "hash": True,
            "provenance": True,
            "witness": True,
            "registry": False,
            "federation": False,
        }
    )

    assert result["decision"] == EvidenceDecision.PARTIAL
