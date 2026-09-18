import pytest

from certificate_chain import build_certificate_chain_entry, verify_certificate_chain
from verification_certificate import build_verification_certificate


def entry():
    return build_certificate_chain_entry(
        build_verification_certificate({"decision": "VERIFIED", "verified": True}),
        previous_certificate_hash="a" * 64,
    )


def test_builder_does_not_assert_unchecked_link_integrity():
    value = entry()
    assert value["chain_integrity"] is None
    assert value["chain_verified"] is False
    assert value["trusted"] is False
    assert value["previous_certificate_hash"] == "a" * 64


@pytest.mark.parametrize("flag", [True, False, None, "verified", 1, {}])
def test_declared_integrity_cannot_authenticate_a_chain(flag):
    result = verify_certificate_chain({**entry(), "chain_integrity": flag,
                                       "chain_verified": True, "trusted": True})
    assert result["shape_valid"] is True
    assert result["decision"] == "REVIEW_REQUIRED"
    assert result["chain_integrity"] is None
    for name in ("trusted", "verified", "chain_verified", "signature_verified", "issuer_verified", "truth_guarantee"):
        assert result[name] is False
    assert "certificate_chain_verification_not_performed" in result["reasons"]


@pytest.mark.parametrize("value", [None, [], "chain", 1, True, {}, {"chain_integrity": True}])
def test_malformed_chain_returns_invalid_without_raising(value):
    result = verify_certificate_chain(value)
    assert result["decision"] == "INVALID"
    assert result["trusted"] is False
    assert result["shape_valid"] is False


@pytest.mark.parametrize("override", [
    {"certificate": {}}, {"certificate": None}, {"certificate_chain_version": "unknown"},
    {"previous_certificate_hash": []}, {"previous_certificate_hash": " "},
])
def test_malformed_entry_fields(override):
    assert verify_certificate_chain({**entry(), **override})["shape_valid"] is False
