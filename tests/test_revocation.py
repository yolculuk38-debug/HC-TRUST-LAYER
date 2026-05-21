from revocation import (
    RevocationStatus,
    apply_revocation_check,
    build_revocation_record,
)


def test_revoked_result():
    record = build_revocation_record(
        target_id="CERT-1",
        target_type="CERTIFICATE",
        status=RevocationStatus.REVOKED,
        reason="tampered_certificate",
    )

    result = apply_revocation_check(
        {"decision": "VERIFIED"},
        record,
    )

    assert result["decision"] == "INVALID"


def test_review_required_revocation():
    record = build_revocation_record(
        target_id="CERT-2",
        target_type="CERTIFICATE",
        status=RevocationStatus.SUSPENDED,
        reason="issuer_review",
    )

    result = apply_revocation_check(
        {"decision": "VERIFIED"},
        record,
    )

    assert result["decision"] == "REVIEW_REQUIRED"
