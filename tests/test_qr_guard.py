from qr_guard import build_qr_record, detect_qr_risk, is_trusted_payload


def test_hc_scheme_payloads_remain_trusted():
    assert is_trusted_payload("hc://record/HC-QR-2026-0001") is True
    assert detect_qr_risk("hc://record/HC-QR-2026-0001") == "LOW"


def test_repository_backed_payloads_remain_trusted():
    for payload in [
        "https://github.com/yolculuk38-debug/HC-TRUST-LAYER/blob/main/docs/index.md",
        "https://yolculuk38-debug.github.io/HC-TRUST-LAYER/verify/HC-QR-2026-0001",
    ]:
        record = build_qr_record(payload=payload)

        assert record["trusted"] is True
        assert record["risk_level"] == "LOW"


def test_legacy_public_verifier_payload_is_not_trusted():
    payload = "https://hc-trust-layer.org/verify/HC-QR-2026-0001"

    record = build_qr_record(payload=payload)

    assert is_trusted_payload(payload) is False
    assert record["trusted"] is False
    assert record["risk_level"] == "HIGH"
