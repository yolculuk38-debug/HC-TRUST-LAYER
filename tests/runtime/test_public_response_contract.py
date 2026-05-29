"""Contract tests for HC:// runtime public response integration surfaces."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import httpx
import pytest

from hc_runtime.app import create_app
from hc_runtime.contracts import MALFORMED_INPUT_RESPONSE_KEYS, QR_VERIFICATION_RESPONSE_KEYS
from hc_runtime.state import ABUSE_SIGNAL_TRACKER, EVENT_STORE, QUEUE_STORE


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
    content = {"record_id": record_id, "summary": "HC:// public response contract test payload"}
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


def _warning_text(payload: dict[str, Any]) -> str:
    return " ".join(str(warning).lower() for warning in payload["warnings"])


def _assert_public_contract(payload: dict[str, Any], *, record_id: str) -> None:
    assert list(payload.keys()) == list(QR_VERIFICATION_RESPONSE_KEYS)
    assert payload["record_id"] == record_id
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert payload["qr_scan_summary"]["advisory_only"] is True
    assert payload["qr_scan_summary"]["public_safe"] is True
    assert payload["qr_scan_summary"]["truth_guarantee"] is False
    assert payload["qr_scan_summary"]["request_denied"] is False
    assert payload["qr_scan_summary"]["human_final_authority"] is True


async def _post(client: httpx.AsyncClient, record_id: str, qr_input: str) -> dict[str, Any]:
    response = await client.post(f"/verify/{record_id}", json={"qr_input": qr_input})
    assert response.status_code == 200
    payload = response.json()
    _assert_public_contract(payload, record_id=record_id)
    return payload


@pytest.mark.anyio
async def test_normal_validation_response_contract_has_empty_warnings_field(client: httpx.AsyncClient) -> None:
    record_id = "normal-runtime-contract"

    payload = await _post(client, record_id, _structured_qr(record_id))

    assert payload["status"] == "ADVISORY"
    assert payload["trust_state"] == "ADVISORY"
    assert payload["warnings"] == []
    assert payload["degraded_runtime"] is False
    assert payload["replay_warning"] is False
    assert payload["public_exposure"] == "standard"


@pytest.mark.anyio
async def test_degraded_validation_response_contract_keeps_state_visible(client: httpx.AsyncClient) -> None:
    payload = await _post(client, "degraded-runtime-contract", "hc://runtime hash:ok degraded")

    assert payload["trust_state"] == "DEGRADED"
    assert payload["degraded_runtime"] is True
    assert payload["recovery_mode"] is True
    assert payload["public_exposure"] == "restricted"
    assert any("degraded" in warning.lower() for warning in payload["warnings"])


@pytest.mark.anyio
async def test_qr_spoof_warning_response_contract_is_advisory_only(client: httpx.AsyncClient) -> None:
    record_id = "qr-spoof-runtime-contract"

    payload = await _post(
        client,
        record_id,
        _structured_qr(record_id, verification_url=f"https://spoof.example/verify/{record_id}"),
    )

    assert payload["qr_risk_level"] == "HIGH"
    assert payload["human_review_recommended"] is True
    assert payload["escalation_queued"] is True
    assert "spoof" in _warning_text(payload)
    assert payload["advisory_only"] is True
    assert payload["truth_guarantee"] is False
    assert QUEUE_STORE.escalation_queue[-1]["advisory_only"] is True
    assert QUEUE_STORE.escalation_queue[-1]["truth_guarantee"] is False


@pytest.mark.anyio
async def test_abuse_advisory_response_contract_does_not_block(client: httpx.AsyncClient) -> None:
    await _post(client, "abuse-runtime-contract-001", "")
    payload = await _post(client, "abuse-runtime-contract-002", "")

    assert "repeated_malformed_input" in payload["qr_scan_summary"]["abuse_signal_reasons"]
    assert payload["qr_scan_summary"]["abuse_signal_level"] == "MEDIUM"
    assert payload["qr_scan_summary"]["request_denied"] is False
    assert "advisory warning only" in _warning_text(payload)
    assert "no request denial" in _warning_text(payload)


@pytest.mark.anyio
async def test_replay_warning_response_contract_is_visible_and_advisory(client: httpx.AsyncClient) -> None:
    payload = await _post(client, "replay-runtime-contract", "hc://runtime hash:ok replay")

    assert payload["trust_state"] == "REPLAY_WARNING"
    assert payload["replay_warning"] is True
    assert payload["public_exposure"] == "restricted"
    assert any("replay" in warning.lower() for warning in payload["warnings"])
    assert QUEUE_STORE.replay_warning_queue[-1]["source"] == "qr-verification"


@pytest.mark.anyio
async def test_malformed_input_response_contract_preserves_public_safe_fields(client: httpx.AsyncClient) -> None:
    response = await client.post("/verify/malformed-runtime-contract", json={"unexpected": "field"})
    payload = response.json()

    assert response.status_code == 422
    assert list(payload.keys()) == list(MALFORMED_INPUT_RESPONSE_KEYS)
    assert payload["record_id"] == "malformed-runtime-contract"
    assert payload["status"] == "MALFORMED_INPUT"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert payload["malformed_input"] is True
    assert payload["public_exposure"] == "restricted"
    assert any("malformed" in warning.lower() for warning in payload["warnings"])


@pytest.mark.anyio
async def test_stable_output_keys_preserved_across_public_response_cases(client: httpx.AsyncClient) -> None:
    cases = [
        ("stable-contract-normal", _structured_qr("stable-contract-normal")),
        ("stable-contract-degraded", "hc://runtime hash:ok degraded"),
        ("stable-contract-replay", "hc://runtime hash:ok replay"),
        (
            "stable-contract-spoof",
            _structured_qr("stable-contract-spoof", verification_url="https://spoof.example/verify/stable-contract-spoof"),
        ),
    ]

    payloads = [await _post(client, record_id, qr_input) for record_id, qr_input in cases]

    assert [list(payload.keys()) for payload in payloads] == [list(QR_VERIFICATION_RESPONSE_KEYS)] * len(cases)
    assert all(payload["advisory_only"] is True for payload in payloads)
    assert all(payload["public_safe"] is True for payload in payloads)
    assert all(payload["truth_guarantee"] is False for payload in payloads)
    assert all(isinstance(payload["warnings"], list) for payload in payloads)


def test_public_response_contract_documentation_lists_stable_runtime_keys() -> None:
    document = Path("docs/runtime/public-response-contract.md").read_text(encoding="utf-8")

    for key in QR_VERIFICATION_RESPONSE_KEYS:
        assert f"`{key}`" in document
    for key in MALFORMED_INPUT_RESPONSE_KEYS:
        assert f"`{key}`" in document
    assert "`advisory_only=true`" in document
    assert "`public_safe=true`" in document
    assert "`truth_guarantee=false`" in document
    assert "warnings" in document
    assert "autonomous blocking" in document
