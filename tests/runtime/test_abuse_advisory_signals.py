"""Advisory abuse-signal coverage for HC:// runtime and QR flows."""

from __future__ import annotations

import hashlib
import json

import httpx
import pytest

from hc_runtime.abuse_signals import AdvisoryAbuseSignalTracker
from hc_runtime.app import create_app
from hc_runtime.qr_spoof_protection import QRRiskLevel
from hc_runtime.state import ABUSE_SIGNAL_TRACKER, EVENT_STORE, QUEUE_STORE

SECRET_MARKERS = ("ghp_", "token=", "api_key=", "private_key=", "-----BEGIN")


def _canonical_json(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _structured_qr(record_id: str, **overrides: object) -> str:
    content = {"record_id": record_id, "summary": "HC:// advisory abuse signal test payload"}
    payload: dict[str, object] = {
        "record_id": record_id,
        "verification_url": f"https://github.com/example/HC-TRUST-LAYER/verify/{record_id}",
        "content": content,
        "content_hash": _sha256_text(_canonical_json(content)),
        "created_at": "2026-05-28T00:00:00Z",
        "qr_version": "v1",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
    }
    payload.update(overrides)
    if "payload_hash" not in payload:
        payload["payload_hash"] = _sha256_text(_canonical_json(payload))
    return _canonical_json(payload)


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


async def _post(client: httpx.AsyncClient, record_id: str, qr_input: str) -> dict[str, object]:
    response = await client.post(f"/verify/{record_id}", json={"qr_input": qr_input})
    assert response.status_code == 200
    payload = response.json()
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert payload["qr_scan_summary"]["request_denied"] is False
    assert payload["qr_scan_summary"]["human_final_authority"] is True
    return payload


def _warning_text(payload: dict[str, object]) -> str:
    return " ".join(str(warning).lower() for warning in payload["warnings"])


@pytest.mark.anyio
async def test_repeated_malformed_inputs_produce_advisory_warning_without_denial(client: httpx.AsyncClient) -> None:
    first = await _post(client, "malformed-family-001", "")
    second = await _post(client, "malformed-family-002", "")

    assert first["qr_scan_summary"]["abuse_signal_reasons"] == []
    assert second["trust_state"] == "UNRESOLVED"
    assert second["qr_scan_summary"]["abuse_signal_level"] == "MEDIUM"
    assert "repeated_malformed_input" in second["qr_scan_summary"]["abuse_signal_reasons"]
    assert second["qr_scan_summary"]["abuse_pattern_counts"]["malformed_input"] == 2
    assert "advisory warning only" in _warning_text(second)
    assert "no request denial" in _warning_text(second)


@pytest.mark.anyio
async def test_repeated_spoof_risk_qr_inputs_remain_visible_and_advisory(client: httpx.AsyncClient) -> None:
    first = await _post(
        client,
        "spoof-family-001",
        _structured_qr("spoof-family-001", verification_url="https://spoof.example/verify/spoof-family-001"),
    )
    second = await _post(
        client,
        "spoof-family-002",
        _structured_qr("spoof-family-002", verification_url="https://spoof.example/verify/spoof-family-002"),
    )

    assert first["qr_risk_level"] == "HIGH"
    assert second["qr_risk_level"] == "INCIDENT"
    assert "repeated_spoof_risk_qr" in second["qr_scan_summary"]["abuse_signal_reasons"]
    assert second["qr_scan_summary"]["abuse_signal_level"] == "HIGH"
    assert "human-supervised validation" in _warning_text(second)
    assert second["escalation_queued"] is True
    assert QUEUE_STORE.escalation_queue[-1]["advisory_only"] is True
    assert QUEUE_STORE.escalation_queue[-1]["truth_guarantee"] is False


@pytest.mark.anyio
async def test_repeated_replay_markers_emit_advisory_escalation_signal_only(client: httpx.AsyncClient) -> None:
    first = await _post(client, "replay-family-001", "hc://runtime hash:ok replay")
    second = await _post(client, "replay-family-002", "hc://runtime hash:ok replay")

    assert first["replay_warning"] is True
    assert second["replay_warning"] is True
    assert "repeated_replay_marker" in second["qr_scan_summary"]["abuse_signal_reasons"]
    assert second["qr_scan_summary"]["abuse_signal_level"] == "HIGH"
    assert "no autonomous blocking" in _warning_text(second)
    assert all(item.get("reason") != "blocked" for item in QUEUE_STORE.escalation_queue)


@pytest.mark.anyio
async def test_degraded_validator_state_remains_visible_with_advisory_abuse_signal(client: httpx.AsyncClient) -> None:
    await _post(client, "degraded-family-001", "hc://runtime hash:ok degraded")
    second = await _post(client, "degraded-family-002", "hc://runtime hash:ok degraded")

    assert second["degraded_runtime"] is True
    assert second["recovery_mode"] is True
    assert "repeated_degraded_validator_state" in second["qr_scan_summary"]["abuse_signal_reasons"]
    assert second["qr_scan_summary"]["abuse_pattern_counts"]["degraded_state"] == 2
    assert "degraded visibility remains" in _warning_text(second)


@pytest.mark.anyio
async def test_mixed_low_medium_high_risk_signals_preserve_stable_public_safe_keys(client: httpx.AsyncClient) -> None:
    low = await _post(client, "mixed-low", _structured_qr("mixed-low"))
    medium = await _post(client, "mixed-medium", _structured_qr("mixed-medium", signed_payload_ref=""))
    high = await _post(
        client,
        "mixed-high",
        _structured_qr("mixed-high", verification_url="https://mixed-spoof.example/verify/mixed-high"),
    )

    expected_keys = list(low.keys())
    assert [payload["qr_risk_level"] for payload in [low, medium, high]] == ["LOW", "MEDIUM", "HIGH"]
    assert [list(payload.keys()) for payload in [low, medium, high]] == [expected_keys, expected_keys, expected_keys]
    assert all(payload["advisory_only"] is True for payload in [low, medium, high])
    assert all(payload["public_safe"] is True for payload in [low, medium, high])
    assert all(payload["truth_guarantee"] is False for payload in [low, medium, high])
    assert all(isinstance(payload["warnings"], list) for payload in [low, medium, high])


@pytest.mark.anyio
async def test_abuse_warnings_remain_public_safe_and_do_not_echo_raw_tokens(client: httpx.AsyncClient) -> None:
    secretish_input = "hc://secret-family hash:ok replay token=<redacted-token> api_key=<redacted-api-key>"

    await _post(client, "secret-family-001", secretish_input)
    second = await _post(client, "secret-family-002", secretish_input)
    serialized = json.dumps(second, sort_keys=True).lower()

    assert "repeated_replay_marker" in second["qr_scan_summary"]["abuse_signal_reasons"]
    for marker in SECRET_MARKERS:
        assert marker.lower() not in serialized


def test_advisory_abuse_signal_helper_is_public_safe_and_non_blocking() -> None:
    tracker = AdvisoryAbuseSignalTracker()

    first = tracker.inspect(
        record_id="helper-family-001",
        schema_valid=False,
        qr_risk_level=QRRiskLevel.LOW,
        qr_risk_reasons=[],
        qr_risk_group_keys=[],
        replay_warning=True,
        degraded_mode=True,
    )
    second = tracker.inspect(
        record_id="helper-family-002",
        schema_valid=False,
        qr_risk_level=QRRiskLevel.LOW,
        qr_risk_reasons=[],
        qr_risk_group_keys=[],
        replay_warning=True,
        degraded_mode=True,
    )

    assert first.request_denied is False
    assert second.advisory_only is True
    assert second.public_safe is True
    assert second.truth_guarantee is False
    assert second.request_denied is False
    assert second.human_final_authority is True
    assert {"repeated_malformed_input", "repeated_replay_marker", "repeated_degraded_validator_state"}.issubset(
        set(second.reasons)
    )
