import json

from qr_hardening import QRStatus, sha256_text, verify_qr_payload

SAFE_URL = "https://github.com/yolculuk38-debug/HC-TRUST-LAYER/blob/main/docs/index.md"


def build_payload(content="HC:// TRUST", signed=True):
    payload = {
        "record_id": "HC-QR-2026-0001",
        "content": content,
        "content_hash": sha256_text(content),
        "verification_url": SAFE_URL,
        "created_at": "2026-05-21T09:20:00Z",
    }
    if signed:
        payload["signature"] = "HC-SIGNATURE"
    return payload


def test_signature_presence_stays_unverified_and_untrusted():
    result = verify_qr_payload(build_payload())
    assert result["status"] == QRStatus.SIGNATURE_UNVERIFIED.value
    assert result["trusted"] is False
    assert result["signature_present"] is True
    assert result["signature_verified"] is False
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True


def test_unsigned_qr_payload():
    result = verify_qr_payload(build_payload(signed=False))
    assert result["status"] == QRStatus.UNSIGNED.value
    assert result["trusted"] is False


def test_tampered_qr_payload_hash_mismatch():
    payload = build_payload()
    payload["content"] = "tampered"
    result = verify_qr_payload(payload)
    assert result["status"] == QRStatus.HASH_MISMATCH.value


def test_unsafe_qr_url():
    payload = build_payload()
    payload["verification_url"] = "https://evil.example/phishing"
    result = verify_qr_payload(payload)
    assert result["status"] == QRStatus.UNSAFE_URL.value


def test_invalid_qr_missing_fields():
    payload = {"record_id": "HC"}
    result = verify_qr_payload(payload)
    assert result["status"] == QRStatus.INVALID_QR.value


def test_invalid_qr_json_string():
    result = verify_qr_payload("not-json")
    assert result["status"] == QRStatus.INVALID_QR.value


def test_valid_json_payload_input():
    payload = build_payload()
    result = verify_qr_payload(json.dumps(payload))
    assert result["status"] == QRStatus.SIGNATURE_UNVERIFIED.value


def test_legacy_archive_repo_path_on_allowed_domain_is_not_safe():
    for url in [
        "https://github.com/yolculuk38-debug/legacy-archive-repo",
        "https://github.com/yolculuk38-debug/legacy-archive-repo/blob/main/records/HC-QR-2026-0001.json",
    ]:
        payload = build_payload()
        payload["verification_url"] = url

        result = verify_qr_payload(payload)

        assert result["status"] == QRStatus.UNSAFE_URL.value
        assert result["trusted"] is False


def test_github_hc_trust_layer_records_path_passes_url_check_without_trust():
    payload = build_payload()
    payload["verification_url"] = (
        "https://github.com/yolculuk38-debug/HC-TRUST-LAYER/blob/main/records/HC-QR-2026-0001.json"
    )

    result = verify_qr_payload(payload)

    assert result["status"] == QRStatus.SIGNATURE_UNVERIFIED.value
    assert result["trusted"] is False


def test_github_and_pages_repository_backed_urls_do_not_grant_trust():
    for url in [
        SAFE_URL,
        "https://yolculuk38-debug.github.io/HC-TRUST-LAYER/verify/HC-QR-2026-0001",
    ]:
        payload = build_payload()
        payload["verification_url"] = url

        result = verify_qr_payload(payload)

        assert result["status"] == QRStatus.SIGNATURE_UNVERIFIED.value
        assert result["trusted"] is False


def test_non_string_signature_is_invalid_and_unverified():
    payload = build_payload()
    payload["signature"] = {"value": "not-verified"}

    result = verify_qr_payload(payload)

    assert result["status"] == QRStatus.INVALID_QR.value
    assert result["trusted"] is False
    assert result["signature_verified"] is False
