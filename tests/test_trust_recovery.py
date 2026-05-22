from trust_recovery import (
    RecoveryStatus,
    build_recovery_request,
    evaluate_recovery_request,
)



def test_restored_recovery_request():
    request = build_recovery_request(
        target_id="REC-1",
        target_type="CERTIFICATE",
        reason="false_positive_revocation",
        evidence={"audit_snapshot": True},
    )

    result = evaluate_recovery_request(request)

    assert result["status"] == RecoveryStatus.RESTORED



def test_under_review_recovery_request():
    request = build_recovery_request(
        target_id="REC-2",
        target_type="CERTIFICATE",
        reason="",
        evidence={},
    )

    result = evaluate_recovery_request(request)

    assert result["status"] == RecoveryStatus.UNDER_REVIEW
