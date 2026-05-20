import pytest

from hc_trust.verify_gateway import build_verify_response


def test_build_verify_response_clean_evidence_returns_strong_verified():
    response = build_verify_response("HC-TEST-2026-0001", {"hash_valid": True})

    assert response["record_id"] == "HC-TEST-2026-0001"
    assert response["trust_level"] == "STRONG_VERIFIED"
    assert response["indicators"] == []


def test_build_verify_response_hash_mismatch_indicator():
    response = build_verify_response("HC-TEST-2026-0002", {"hash_valid": False})

    assert "hash_mismatch" in response["indicators"]


def test_build_verify_response_rejects_empty_record_id():
    with pytest.raises(ValueError, match="record_id must be a non-empty string"):
        build_verify_response("", {"hash_valid": True})


def test_build_verify_response_rejects_non_dict_evidence():
    with pytest.raises(ValueError, match="evidence must be a dict"):
        build_verify_response("HC-TEST-2026-0003", [])
