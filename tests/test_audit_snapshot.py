from audit_snapshot import (
    build_audit_snapshot,
    evaluate_audit_snapshot,
)


def test_valid_audit_snapshot():
    snapshot = build_audit_snapshot(
        snapshot_id="snap-1",
        trust_state="VERIFIED",
        evidence_score=95,
        previous_snapshot_hash="prev-hash",
    )

    result = evaluate_audit_snapshot(snapshot)

    assert result["trusted"] is True


def test_review_required_snapshot():
    snapshot = build_audit_snapshot(
        snapshot_id="snap-2",
        trust_state="REVIEW_REQUIRED",
        evidence_score=40,
        risk_flags=["manipulation_risk"],
    )

    result = evaluate_audit_snapshot(snapshot)

    assert result["decision"] == "REVIEW_REQUIRED"
