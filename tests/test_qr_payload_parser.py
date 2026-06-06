import json

from hc_runtime.qr_payload_parser import parse_qr_payload


VALID_PAYLOAD = {
    "qr_version": "1",
    "record_id": "HC-EXAMPLE-2026-0001",
    "canonical_url": "https://example.invalid/record/HC-EXAMPLE-2026-0001",
    "payload_hash": "abc",
    "content_hash": "def",
    "issued_at": "2026-01-01T00:00:00Z",
    "issuer_id": "demo",
    "algorithm": "none",
    "key_id": "demo-key",
}


def encode(payload):
    return json.dumps(payload)


def test_valid_payload_returns_advisory_valid_payload():
    result = parse_qr_payload(encode(VALID_PAYLOAD))

    assert result["status"] == "valid_payload"
    assert result["warnings"] == []
    assert result["errors"] == []
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is True


def test_missing_field_returns_warning_and_invalid_payload():
    payload = dict(VALID_PAYLOAD)
    del payload["payload_hash"]

    result = parse_qr_payload(encode(payload))

    assert result["status"] == "invalid_payload"
    assert any(
        "Missing required QR payload field(s): payload_hash." == warning
        for warning in result["warnings"]
    )
    assert result["errors"] == ["QR payload is missing required field(s)."]


def test_malformed_json_returns_malformed_payload():
    result = parse_qr_payload('{"record_id":')

    assert result["status"] == "malformed_payload"
    assert result["warnings"] == []
    assert result["errors"]


def test_invalid_record_id_returns_invalid_payload():
    payload = dict(VALID_PAYLOAD, record_id="not-an-hc-record")

    result = parse_qr_payload(encode(payload))

    assert result["status"] == "invalid_payload"
    assert (
        "QR payload record_id does not match HC:// record identifier format."
        in result["errors"]
    )


def test_unknown_field_returns_warning_without_invalidating_payload():
    payload = dict(VALID_PAYLOAD, debug_note="local-only")

    result = parse_qr_payload(encode(payload))

    assert result["status"] == "valid_payload"
    assert result["warnings"] == ["Unknown QR payload field ignored: debug_note."]
    assert result["errors"] == []


def test_safety_markers_always_present():
    for raw_payload in [
        encode(VALID_PAYLOAD),
        '{"record_id":',
        encode({"record_id": "bad"}),
    ]:
        result = parse_qr_payload(raw_payload)

        assert result["advisory_only"] is True
        assert result["public_safe"] is True
        assert result["truth_guarantee"] is False
        assert result["human_review_required"] is True
