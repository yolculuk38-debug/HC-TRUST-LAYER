"""Secret-like input redaction coverage for HC:// runtime outputs."""

from __future__ import annotations

import json
from typing import Any

import pytest

from hc_runtime.contracts import advisory_response
from hc_runtime.events import RuntimeEventStore
from hc_runtime.runtime import RuntimeQueueStore

EXPECTED_ADVISORY_RESPONSE_KEYS = [
    "status",
    "advisory_only",
    "public_safe",
    "message",
    "warnings",
    "traceable",
    "truth_guarantee",
    "record_id",
]

PUBLIC_SAFE_MARKER = "[REDACTED]"
FAKE_GITHUB_TOKEN_MARKER = "ghp_" + ("A" * 24)
FAKE_API_KEY_MARKER = "api_key=" + ("B" * 28)
FAKE_PRIVATE_KEY_MARKER = (
    "-----BEGIN "
    "PRIVATE KEY-----\n"
    + ("C" * 32)
    + "\n-----END "
    "PRIVATE KEY-----"
)
MALFORMED_SECRET_LIKE_MARKER = "token=" + ("D" * 24) + " -----BEGIN " "PRIVATE KEY-----"


def _serialized(payload: Any) -> str:
    return json.dumps(payload)


def _roundtrip_payload(payload: dict[str, Any]) -> dict[str, Any]:
    return json.loads(json.dumps(payload))


def _assert_public_safe_contract(payload: dict[str, Any], *, record_id: str) -> None:
    assert list(payload.keys()) == EXPECTED_ADVISORY_RESPONSE_KEYS
    assert payload["record_id"] == record_id
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)


def _assert_markers_not_exposed(payload: Any, markers: list[str]) -> None:
    serialized = _serialized(payload)
    for marker in markers:
        assert marker not in serialized


@pytest.mark.parametrize(
    ("marker", "record_id"),
    [
        (FAKE_GITHUB_TOKEN_MARKER, "github-redaction-record"),
        (FAKE_API_KEY_MARKER, "api-redaction-record"),
        (FAKE_PRIVATE_KEY_MARKER, "private-redaction-record"),
        (MALFORMED_SECRET_LIKE_MARKER, "malformed-redaction-record"),
    ],
)
def test_secret_like_input_is_redacted_from_runtime_response_and_warning_text(
    marker: str,
    record_id: str,
) -> None:
    payload = advisory_response(
        record_id=record_id,
        message=f"HC:// advisory runtime inspected public-safe input {marker}",
        warnings=[f"Public-safe warning redacted secret-like input {marker}"],
    )

    _assert_public_safe_contract(payload, record_id=record_id)
    assert payload["warnings"]
    assert PUBLIC_SAFE_MARKER in _serialized(payload)
    _assert_markers_not_exposed(payload, [marker])


def test_runtime_response_roundtrip_preserves_stable_public_safe_key_order() -> None:
    payload = advisory_response(
        record_id="stable-redaction-record",
        message="HC:// advisory runtime response remains deterministic.",
        warnings=None,
    )

    _assert_public_safe_contract(payload, record_id="stable-redaction-record")
    roundtripped = _roundtrip_payload(payload)

    _assert_public_safe_contract(roundtripped, record_id="stable-redaction-record")
    assert roundtripped["warnings"] == []
    assert list(roundtripped.keys()) == EXPECTED_ADVISORY_RESPONSE_KEYS


def test_secret_like_input_is_redacted_from_telemetry_like_runtime_payloads() -> None:
    queue_store = RuntimeQueueStore()
    event_store = RuntimeEventStore()
    record_id = "telemetry-redaction-record"
    qr_input = f"hc://{record_id} hash:ok {FAKE_GITHUB_TOKEN_MARKER} {FAKE_API_KEY_MARKER}"

    queue_store.enqueue_verification({"record_id": record_id, "qr_input": qr_input})
    queue_store.enqueue_escalation(
        {
            "record_id": record_id,
            "reason": "advisory-redaction-audit",
            "details": {"input": qr_input, "private_marker": FAKE_PRIVATE_KEY_MARKER},
            "advisory_only": True,
            "public_safe": True,
            "truth_guarantee": False,
        }
    )
    queue_store.enqueue_replay_warning({"record_id": record_id, "source": qr_input})
    event_store.append_runtime_event(
        event_type="redaction_audit",
        record_id=record_id,
        details={"warning": f"redact malformed marker {MALFORMED_SECRET_LIKE_MARKER}"},
    )

    telemetry_like_payload = {
        "verification_queue": queue_store.verification_queue,
        "escalation_queue": queue_store.escalation_queue,
        "replay_warning_queue": queue_store.replay_warning_queue,
        "events": event_store._events,
    }

    assert PUBLIC_SAFE_MARKER in _serialized(telemetry_like_payload)
    _assert_markers_not_exposed(
        telemetry_like_payload,
        [
            qr_input,
            FAKE_GITHUB_TOKEN_MARKER,
            FAKE_API_KEY_MARKER,
            FAKE_PRIVATE_KEY_MARKER,
            MALFORMED_SECRET_LIKE_MARKER,
        ],
    )
    assert queue_store.escalation_queue[-1]["advisory_only"] is True
    assert queue_store.escalation_queue[-1]["public_safe"] is True
    assert queue_store.escalation_queue[-1]["truth_guarantee"] is False
