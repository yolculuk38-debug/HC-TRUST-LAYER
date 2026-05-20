import pytest

from hc_trust.result_formatter import FORMAT_VERSION, format_trust_result
from hc_trust.trust_engine import TrustResult


def test_format_trust_result_api_ready_payload():
    result = TrustResult(score=91, level="STRONG_VERIFIED", indicators=[])

    payload = format_trust_result(
        "HC-TEST-2026-0001",
        result,
        verification_id="VR-HC-TEST-2026-0001",
        verified_at="2026-05-20T10:00:00+00:00",
    )

    assert payload == {
        "format_version": FORMAT_VERSION,
        "verification_id": "VR-HC-TEST-2026-0001",
        "record_id": "HC-TEST-2026-0001",
        "trust_score": 91,
        "trust_level": "STRONG_VERIFIED",
        "indicators": [],
        "verified_at": "2026-05-20T10:00:00+00:00",
        "experimental": True,
    }


def test_format_trust_result_generates_default_verification_id():
    result = TrustResult(score=60, level="PARTIAL_TRUST", indicators=["hash_mismatch"])

    payload = format_trust_result(
        "HC-TEST-2026-0002",
        result,
        verified_at="2026-05-20T10:00:00+00:00",
    )

    assert payload["verification_id"] == "VR-HC-TEST-2026-0002"
    assert payload["indicators"] == ["hash_mismatch"]


def test_format_trust_result_rejects_missing_record_id():
    result = TrustResult(score=100, level="STRONG_VERIFIED", indicators=[])

    with pytest.raises(ValueError, match="record_id is required"):
        format_trust_result("", result)
