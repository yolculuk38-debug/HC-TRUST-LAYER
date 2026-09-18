import pytest

from certificate_verifier import verify_certificate
from verification_certificate import build_verification_certificate


def test_sdk_claims_are_preserved_only_as_unverified_declarations():
    source = {"decision": "VERIFIED", "verified": True,
              "verification_level": "LEVEL_4_PROVENANCE_LOCKED",
              "risk_flags": ["risk"], "reasons": ["source_reason"],
              "signature_verified": True, "issuer_verified": True}
    certificate = build_verification_certificate(source)
    assert certificate["source_claims"] == {key: source[key] for key in (
        "decision", "verified", "verification_level")}
    assert certificate["source_claims_verified"] is False
    assert certificate["verification_level"] is None
    assert certificate["decision"] == "REVIEW_REQUIRED"
    for name in ("verified", "trusted", "signature_verified", "issuer_verified", "truth_guarantee"):
        assert certificate[name] is False
    assert certificate["portable"] is True
    assert certificate["human_readable"] is True
    assert "source_reason" in certificate["reasons"]
    assert certificate["risk_flags"] == ["risk"]
    assert verify_certificate(certificate)["shape_valid"] is True
    assert verify_certificate(certificate)["trusted"] is False
    source["risk_flags"].append("later")
    assert certificate["risk_flags"] == ["risk"]


@pytest.mark.parametrize("source", [None, [], "response", {"risk_flags": None},
                                        {"reasons": [1]}, {"risk_flags": "risk"}])
def test_invalid_sdk_input_is_rejected(source):
    with pytest.raises(ValueError):
        build_verification_certificate(source)


@pytest.mark.parametrize("issuer", [None, [], "", " "])
def test_invalid_issuer_is_rejected(issuer):
    with pytest.raises(ValueError):
        build_verification_certificate({}, issuer=issuer)
