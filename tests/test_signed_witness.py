from signed_witness import (
    build_witness_payload,
    sign_witness,
    verify_witness_signature,
)


SECRET = "hc-secret"


def test_valid_signed_witness():
    payload = build_witness_payload(
        "HC-2026-0001",
        "witness-1",
        "PASS",
        "abc123",
    )

    signed_payload = sign_witness(payload, SECRET)
    result = verify_witness_signature(signed_payload, SECRET)

    assert result["verified"] is True


def test_tampered_signed_witness():
    payload = build_witness_payload(
        "HC-2026-0001",
        "witness-1",
        "PASS",
        "abc123",
    )

    signed_payload = sign_witness(payload, SECRET)
    signed_payload["payload"]["verdict"] = "FAIL"

    result = verify_witness_signature(signed_payload, SECRET)

    assert result["verified"] is False


def test_invalid_signature_version():
    payload = build_witness_payload(
        "HC-2026-0001",
        "witness-1",
        "PASS",
        "abc123",
    )

    signed_payload = sign_witness(payload, SECRET)
    signed_payload["signature_version"] = "OLD"

    result = verify_witness_signature(signed_payload, SECRET)

    assert result["verified"] is False


def test_missing_signature():
    result = verify_witness_signature({"payload": {}}, SECRET)
    assert result["verified"] is False
