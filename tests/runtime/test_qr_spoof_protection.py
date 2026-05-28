"""QR spoof-protection behavior tests for the HC:// advisory runtime."""

from __future__ import annotations

import hashlib
import json

import pytest
import httpx

from hc_runtime.app import create_app
from hc_runtime.state import EVENT_STORE, QUEUE_STORE

EXPECTED_QR_RESPONSE_KEYS = [
    "status",
    "advisory_only",
    "public_safe",
    "message",
    "warnings",
    "traceable",
    "truth_guarantee",
    "record_id",
    "trust_state",
    "replay_warning",
    "continuity_warning",
    "degraded_runtime",
    "recovery_mode",
    "public_exposure",
]


def _canonical_json(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _structured_qr_payload(record_id: str, **overrides: object) -> dict[str, object]:
    content = overrides.pop("content", {"record_id": record_id, "summary": "HC:// advisory QR test payload"})
    content_text = content if isinstance(content, str) else _canonical_json(content)
    payload: dict[str, object] = {
        "record_id": record_id,
        "verification_url": f"https://github.com/example/HC-TRUST-LAYER/verify/{record_id}",
        "content": content,
        "content_hash": _sha256_text(content_text),
        "created_at": "2026-05-28T00:00:00Z",
        "qr_version": "v1",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
    }
    payload.update(overrides)
    if "payload_hash" not in payload:
        payload["payload_hash"] = _sha256_text(_canonical_json(payload))
    return payload


def _encoded_qr(record_id: str, **overrides: object) -> str:
    return _canonical_json(_structured_qr_payload(record_id, **overrides))


@pytest.fixture(autouse=True)
def reset_runtime_state() -> None:
    EVENT_STORE._events.clear()
    QUEUE_STORE.verification_queue.clear()
    QUEUE_STORE.escalation_queue.clear()
    QUEUE_STORE.replay_warning_queue.clear()


@pytest.fixture()
async def client() -> httpx.AsyncClient:
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as async_client:
        yield async_client


def _assert_public_safe_advisory_contract(payload: dict[str, object], *, record_id: str) -> None:
    assert list(payload.keys()) == EXPECTED_QR_RESPONSE_KEYS
    assert payload["record_id"] == record_id
    assert payload["status"] == "ADVISORY"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert all(isinstance(warning, str) for warning in payload["warnings"])


def _warning_text(payload: dict[str, object]) -> str:
    return " ".join(str(warning).lower() for warning in payload["warnings"])


async def _post_qr(client: httpx.AsyncClient, record_id: str, qr_input: str) -> dict[str, object]:
    response = await client.post(f"/verify/{record_id}", json={"qr_input": qr_input})
    assert response.status_code == 200
    payload = response.json()
    _assert_public_safe_advisory_contract(payload, record_id=record_id)
    return payload


@pytest.mark.anyio
async def test_canonical_qr_payload_remains_advisory_public_safe_and_warning_field_exists(client: httpx.AsyncClient) -> None:
    record_id = "canonical-qr-spoof-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id))

    assert payload["trust_state"] == "ADVISORY"
    assert payload["warnings"] == []
    assert payload["public_exposure"] == "standard"


@pytest.mark.anyio
async def test_non_canonical_domain_warning_is_explicit_and_not_silently_trusted(client: httpx.AsyncClient) -> None:
    record_id = "non-canonical-domain-record"

    payload = await _post_qr(
        client,
        record_id,
        _encoded_qr(record_id, verification_url=f"https://spoof.example/verify/{record_id}"),
    )

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert "non-canonical qr verification_url domain" in _warning_text(payload)
    assert "human-supervised validation" in _warning_text(payload)


@pytest.mark.anyio
async def test_missing_record_id_warning_has_no_hidden_fallback(client: httpx.AsyncClient) -> None:
    record_id = "missing-record-id-record"
    payload_data = _structured_qr_payload(record_id)
    payload_data.pop("record_id")
    payload_data["payload_hash"] = _sha256_text(_canonical_json({k: v for k, v in payload_data.items() if k != "payload_hash"}))

    payload = await _post_qr(client, record_id, _canonical_json(payload_data))

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert "missing record_id" in _warning_text(payload)
    assert "hidden fallback" in _warning_text(payload)


@pytest.mark.anyio
async def test_record_id_mismatch_warning_is_visible(client: httpx.AsyncClient) -> None:
    record_id = "expected-record-id"

    payload = await _post_qr(client, record_id, _encoded_qr("spoofed-record-id"))

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert "record_id mismatch" in _warning_text(payload)


@pytest.mark.anyio
async def test_missing_payload_hash_warning_is_explicit(client: httpx.AsyncClient) -> None:
    record_id = "missing-payload-hash-record"
    payload_data = _structured_qr_payload(record_id)
    payload_data.pop("payload_hash")

    payload = await _post_qr(client, record_id, _canonical_json(payload_data))

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert "payload_hash is missing" in _warning_text(payload)


@pytest.mark.anyio
async def test_payload_hash_mismatch_warning_is_explicit(client: httpx.AsyncClient) -> None:
    record_id = "payload-hash-mismatch-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id, payload_hash="0" * 64))

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert "payload_hash mismatch" in _warning_text(payload)


@pytest.mark.anyio
async def test_content_hash_mismatch_warning_is_explicit(client: httpx.AsyncClient) -> None:
    record_id = "content-hash-mismatch-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id, content_hash="f" * 64))

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert "content_hash mismatch" in _warning_text(payload)


@pytest.mark.anyio
async def test_missing_signed_payload_reference_warning_is_visible(client: httpx.AsyncClient) -> None:
    record_id = "missing-signed-ref-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id, signed_payload_ref=""))

    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert "signed payload reference is missing" in _warning_text(payload)


@pytest.mark.anyio
async def test_stale_qr_timestamp_or_version_warning_remains_visible(client: httpx.AsyncClient) -> None:
    record_id = "stale-qr-version-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id, qr_version="v0", stale=True))

    assert payload["degraded_runtime"] is True
    assert payload["recovery_mode"] is True
    assert "stale qr version marker" in _warning_text(payload)
    assert "stale qr payload flag" in _warning_text(payload)


@pytest.mark.anyio
async def test_replay_marker_visibility_routes_public_safe_warning(client: httpx.AsyncClient) -> None:
    record_id = "replay-marker-record"

    payload = await _post_qr(client, record_id, _encoded_qr(record_id, replay_marker=True))

    assert payload["replay_warning"] is True
    assert payload["trust_state"] == "REPLAY_WARNING"
    assert payload["public_exposure"] == "restricted"
    assert "replay marker remains visible" in _warning_text(payload)
    assert QUEUE_STORE.replay_warning_queue[-1]["record_id"] == record_id


@pytest.mark.anyio
async def test_spoofed_qr_with_valid_looking_fields_remains_advisory_only(client: httpx.AsyncClient) -> None:
    record_id = "spoofed-valid-looking-record"

    payload = await _post_qr(
        client,
        record_id,
        _encoded_qr(
            record_id,
            verification_url=f"https://evil.example/HC-TRUST-LAYER/verify/{record_id}",
            payload_hash="a" * 64,
        ),
    )

    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["trust_state"] == "REVIEW_REQUIRED"
    assert "non-canonical qr verification_url domain" in _warning_text(payload)
    assert "payload_hash mismatch" in _warning_text(payload)


@pytest.mark.anyio
async def test_stable_qr_response_keys_across_spoof_stale_replay_and_mismatch_cases(client: httpx.AsyncClient) -> None:
    record_id = "stable-qr-keys-record"
    cases = [
        _encoded_qr(record_id),
        _encoded_qr(record_id, verification_url=f"https://spoof.example/verify/{record_id}"),
        _encoded_qr(record_id, stale=True),
        _encoded_qr(record_id, replay_marker=True),
        _encoded_qr(record_id, content_hash="1" * 64),
    ]

    responses = [await _post_qr(client, record_id, qr_input) for qr_input in cases]

    assert all(list(payload.keys()) == EXPECTED_QR_RESPONSE_KEYS for payload in responses)
    assert all(payload["advisory_only"] is True for payload in responses)
    assert all(payload["public_safe"] is True for payload in responses)
    assert all(payload["truth_guarantee"] is False for payload in responses)
    assert all(isinstance(payload["warnings"], list) for payload in responses)
