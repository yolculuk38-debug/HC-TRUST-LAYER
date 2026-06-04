from qr_hardening import sha256_text
from qr_passport_integration import verify_qr_trust_passport


SAFE_URL = "https://github.com/yolculuk38-debug/HC-TRUST-LAYER/blob/main/docs/index.md"


def test_verified_qr_passport():
    content = "HC:// QR passport integration"
    payload = {
        "record_id": "HC-1",
        "content": content,
        "content_hash": sha256_text(content),
        "verification_url": SAFE_URL,
        "created_at": "2026-05-21T09:20:00Z",
        "signature": "HC-SIGNATURE",
    }

    result = verify_qr_trust_passport(
        payload,
        signals={
            "hash_verified": True,
            "trust_score": 95,
            "witness_count": 4,
            "provenance_locked": True,
            "federated_verified": True,
        },
    )

    assert result["status_engine"]["state"] in {"VERIFIED", "PARTIAL"}


def test_invalid_qr_passport():
    result = verify_qr_trust_passport(
        "invalid-payload",
        signals={
            "hash_verified": False,
            "trust_score": 0,
        },
    )

    assert result["status_engine"]["state"] in {"INVALID", "UNTRUSTED"}
