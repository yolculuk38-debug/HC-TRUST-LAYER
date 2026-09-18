import pytest

from certificate_verifier import verify_certificate


def declaration(**overrides):
    return {"certificate_version": "HC-CERTIFICATE-V1", "issuer": "arbitrary caller",
            "decision": "VERIFIED", "verified": True, "risk_flags": [], **overrides}


def test_self_declared_certificate_is_not_authenticated():
    result = verify_certificate(declaration(signature="forged", issuer_verified=True))
    assert result["shape_valid"] is True
    for field in ("trusted", "verified", "signature_verified", "issuer_verified", "truth_guarantee"):
        assert result[field] is False
    assert result["decision"] == "REVIEW_REQUIRED"
    assert "certificate_authentication_not_performed" in result["reasons"]
    assert result["advisory_only"] is True
    assert result["human_review_required"] is True


def test_certificate_risk_flags_remain_visible():
    result = verify_certificate(declaration(risk_flags=["spoof_risk", "spoof_risk"]))
    assert result["risk_flags"] == ["spoof_risk"]
    assert result["trusted"] is False


@pytest.mark.parametrize("payload", [None, [], "certificate", 1, True, {}])
def test_malformed_certificate_fails_closed(payload):
    result = verify_certificate(payload)
    assert result["shape_valid"] is False
    assert result["trusted"] is False


@pytest.mark.parametrize("flags", [None, "risk", 1, {}, [1], [{}], ["risk", []]])
def test_malformed_risk_flags_fail_closed(flags):
    result = verify_certificate(declaration(risk_flags=flags))
    assert result["shape_valid"] is False
    assert "invalid_risk_flags" in result["reasons"]
    assert result["trusted"] is False


@pytest.mark.parametrize("override", [
    {"issuer": []}, {"issuer": " "}, {"verified": 1}, {"decision": []},
    {"certificate_version": "unknown"},
])
def test_malformed_claim_fields_are_not_valid_shape(override):
    assert verify_certificate(declaration(**override))["shape_valid"] is False
