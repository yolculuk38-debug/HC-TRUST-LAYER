import pytest

from hc_trust.audit_trail import build_audit_event, canonical_event, hash_event, verify_audit_event


def test_canonical_event_is_deterministic():
    first = canonical_event({"b": 2, "a": 1})
    second = canonical_event({"a": 1, "b": 2})

    assert first == second
    assert first == '{"a":1,"b":2}'


def test_build_audit_event_verifies():
    event = build_audit_event(
        event_id="evt-001",
        event_type="verification",
        record_id="HC-TEST-2026-0001",
        payload_hash="a" * 64,
        timestamp="2026-05-20T13:00:00+00:00",
    )

    assert len(event["event_hash"]) == 64
    assert verify_audit_event(event) is True


def test_audit_event_detects_tampering():
    event = build_audit_event(
        event_id="evt-001",
        event_type="verification",
        record_id="HC-TEST-2026-0001",
        payload_hash="a" * 64,
        timestamp="2026-05-20T13:00:00+00:00",
    )
    event["record_id"] = "HC-TAMPERED-2026-0001"

    assert verify_audit_event(event) is False


def test_audit_event_links_previous_event_hash():
    first = build_audit_event(
        event_id="evt-001",
        event_type="verification",
        record_id="HC-TEST-2026-0001",
        payload_hash="a" * 64,
        timestamp="2026-05-20T13:00:00+00:00",
    )
    second = build_audit_event(
        event_id="evt-002",
        event_type="review",
        record_id="HC-TEST-2026-0001",
        payload_hash="b" * 64,
        timestamp="2026-05-20T14:00:00+00:00",
        previous_event_hash=first["event_hash"],
    )

    assert second["previous_event_hash"] == first["event_hash"]
    assert verify_audit_event(second) is True


def test_build_audit_event_requires_fields():
    with pytest.raises(ValueError, match="event_id must be a non-empty string"):
        build_audit_event(
            event_id="",
            event_type="verification",
            record_id="HC-TEST-2026-0001",
            payload_hash="a" * 64,
            timestamp="2026-05-20T13:00:00+00:00",
        )
