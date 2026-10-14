from evidence_engine import EvidenceDecision, evaluate_evidence_bundle


def test_complete_declarations_require_review():
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

    assert result["decision"] == EvidenceDecision.REVIEW_REQUIRED


def test_partial_declarations_require_review():
    result = evaluate_evidence_bundle(
        {
            "hash": True,
            "provenance": True,
            "witness": True,
            "registry": False,
            "federation": False,
        }
    )

    assert result["decision"] == EvidenceDecision.REVIEW_REQUIRED
