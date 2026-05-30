"""Roundtrip audit tests for HC:// runtime public validation outputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import httpx
import pytest

from hc_runtime.app import create_app
from hc_runtime.contracts import QR_VERIFICATION_RESPONSE_KEYS
from hc_runtime.state import ABUSE_SIGNAL_TRACKER, EVENT_STORE, QUEUE_STORE


@pytest.fixture()
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(autouse=True)
def reset_runtime_state() -> None:
    EVENT_STORE._events.clear()
    QUEUE_STORE.verification_queue.clear()
    QUEUE_STORE.escalation_queue.clear()
    QUEUE_STORE.replay_warning_queue.clear()
    ABUSE_SIGNAL_TRACKER.reset()


@pytest.fixture()
async def client() -> httpx.AsyncClient:
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as async_client:
        yield async_client


def _canonical_json(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _structured_qr(record_id: str, **overrides: object) -> str:
    content = {"record_id": record_id, "summary": "HC:// persistence roundtrip audit payload"}
    payload: dict[str, object] = {
        "record_id": record_id,
        "verification_url": f"https://github.com/example/HC-TRUST-LAYER/verify/{record_id}",
        "content": content,
        "content_hash": _sha256_text(_canonical_json(content)),
        "created_at": "2026-05-29T00:00:00Z",
        "qr_version": "v1",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
    }
    payload.update(overrides)
    if "payload_hash" not in payload:
        payload["payload_hash"] = _sha256_text(_canonical_json(payload))
    return _canonical_json(payload)


def _roundtrip(payload: dict[str, Any]) -> dict[str, Any]:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    reread = json.loads(serialized)
    if set(QR_VERIFICATION_RESPONSE_KEYS).issubset(reread):
        return {key: reread[key] for key in QR_VERIFICATION_RESPONSE_KEYS}
    return reread


def _assert_roundtrip_contract(payload: dict[str, Any], *, record_id: str) -> None:
    assert list(payload.keys()) == list(QR_VERIFICATION_RESPONSE_KEYS)
    assert payload["record_id"] == record_id
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert payload["traceable"] is True
    assert isinstance(payload["warnings"], list)
    assert payload["qr_scan_summary"]["human_final_authority"] is True
    assert payload["qr_scan_summary"]["request_denied"] is False


async def _post(client: httpx.AsyncClient, record_id: str, qr_input: str) -> dict[str, Any]:
    response = await client.post(f"/verify/{record_id}", json={"qr_input": qr_input})
    assert response.status_code == 200
    payload = response.json()
    _assert_roundtrip_contract(payload, record_id=record_id)
    return payload


@pytest.mark.anyio
async def test_validation_output_roundtrips_as_public_safe_contract_data(client: httpx.AsyncClient) -> None:
    record_id = "persistence-roundtrip-normal"
    payload = await _post(client, record_id, _structured_qr(record_id))

    reread_payload = _roundtrip(payload)

    _assert_roundtrip_contract(reread_payload, record_id=record_id)
    assert reread_payload["warnings"] == []
    assert reread_payload["status"] == "ADVISORY"
    assert reread_payload["public_exposure"] == "standard"


@pytest.mark.anyio
async def test_replay_warning_remains_visible_after_roundtrip_serialization(client: httpx.AsyncClient) -> None:
    record_id = "persistence-roundtrip-replay"
    payload = await _post(client, record_id, "hc://runtime hash:ok replay")

    reread_payload = _roundtrip(payload)

    _assert_roundtrip_contract(reread_payload, record_id=record_id)
    assert reread_payload["trust_state"] == "REPLAY_WARNING"
    assert reread_payload["replay_warning"] is True
    assert reread_payload["public_exposure"] == "restricted"
    assert any("replay" in warning.lower() for warning in reread_payload["warnings"])


@pytest.mark.anyio
async def test_degraded_warning_remains_visible_after_roundtrip_serialization(client: httpx.AsyncClient) -> None:
    record_id = "persistence-roundtrip-degraded"
    payload = await _post(client, record_id, "hc://runtime hash:ok degraded")

    reread_payload = _roundtrip(payload)

    _assert_roundtrip_contract(reread_payload, record_id=record_id)
    assert reread_payload["trust_state"] == "DEGRADED"
    assert reread_payload["degraded_runtime"] is True
    assert reread_payload["recovery_mode"] is True
    assert reread_payload["public_exposure"] == "restricted"
    assert any("degraded" in warning.lower() for warning in reread_payload["warnings"])


@pytest.mark.anyio
async def test_warnings_field_survives_empty_and_non_empty_roundtrip_cases(client: httpx.AsyncClient) -> None:
    empty_warning_payload = await _post(
        client,
        "persistence-roundtrip-empty-warnings",
        _structured_qr("persistence-roundtrip-empty-warnings"),
    )
    non_empty_warning_payload = await _post(
        client,
        "persistence-roundtrip-non-empty-warnings",
        "hc://runtime hash:ok replay",
    )

    reread_empty = _roundtrip(empty_warning_payload)
    reread_non_empty = _roundtrip(non_empty_warning_payload)

    assert "warnings" in reread_empty
    assert "warnings" in reread_non_empty
    assert reread_empty["warnings"] == []
    assert isinstance(reread_non_empty["warnings"], list)
    assert reread_non_empty["warnings"]


@pytest.mark.anyio
async def test_stable_response_keys_and_no_secret_material_after_roundtrip(client: httpx.AsyncClient) -> None:
    record_id = "persistence-roundtrip-secret-redaction"
    payload = await _post(
        client,
        record_id,
        "hc://runtime hash:ok replay api_key=<redacted-api-key> private_key=<redacted-private-key>",
    )

    reread_payload = _roundtrip(payload)
    serialized_public_payload = json.dumps(reread_payload, sort_keys=True)

    assert list(reread_payload.keys()) == list(QR_VERIFICATION_RESPONSE_KEYS)
    assert "api_key" not in serialized_public_payload.lower()
    assert "private_key" not in serialized_public_payload.lower()
    assert "token" not in serialized_public_payload.lower()
    assert "<redacted-api-key>" not in serialized_public_payload
    assert "<redacted-private-key>" not in serialized_public_payload


@pytest.mark.anyio
async def test_write_read_reverify_flow_preserves_public_contract_boundaries(client: httpx.AsyncClient) -> None:
    record_id = "persistence-roundtrip-reverify"
    qr_input = _structured_qr(record_id)

    written_payload = await _post(client, record_id, qr_input)
    history_response = await client.get(f"/verify/{record_id}/history")
    reverified_payload = await _post(client, record_id, qr_input)

    read_history = _roundtrip(history_response.json())
    reread_reverified = _roundtrip(reverified_payload)

    assert history_response.status_code == 200
    assert read_history["record_id"] == record_id
    assert read_history["advisory_only"] is True
    assert read_history["public_safe"] is True
    assert read_history["truth_guarantee"] is False
    assert isinstance(read_history["warnings"], list)
    assert read_history["trust_state_transitions"]
    _assert_roundtrip_contract(written_payload, record_id=record_id)
    _assert_roundtrip_contract(reread_reverified, record_id=record_id)
    assert list(reread_reverified.keys()) == list(written_payload.keys())


def test_persistence_limitations_are_documented_as_advisory_only() -> None:
    runtime_doc = Path("docs/runtime/persistence-roundtrip-audit.md").read_text(encoding="utf-8")
    security_doc = Path("docs/security/persistence-risk-checklist.md").read_text(encoding="utf-8")
    combined = f"{runtime_doc}\n{security_doc}"

    assert "advisory_only=true" in combined
    assert "public_safe=true" in combined
    assert "truth_guarantee=false" in combined
    assert "warnings" in combined
    assert "No hidden fallback behavior" in combined or "hidden fallback behavior" in combined
    assert "Redis implementation: none" in combined
    assert "Database dependency: none" in combined
    assert "Schema mutation: none" in combined
    assert "Workflow mutation: none" in combined
    assert "Governance mutation: none" in combined
    assert "Canonical artifact mutation: none" in combined
    assert "Human final authority: required" in combined
