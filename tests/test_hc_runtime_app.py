"""Tests for the HC:// FastAPI reference runtime scaffold."""

from __future__ import annotations

import pytest

import fastapi  # noqa: F401
import httpx

from hc_runtime.app import create_app
from hc_runtime.state import EVENT_STORE, QUEUE_STORE


@pytest.fixture(autouse=True)
def reset_runtime_state() -> None:
    """Reset shared in-memory runtime state for test isolation."""
    EVENT_STORE._events.clear()
    QUEUE_STORE.verification_queue.clear()
    QUEUE_STORE.escalation_queue.clear()
    QUEUE_STORE.replay_warning_queue.clear()


@pytest.fixture()
async def client() -> httpx.AsyncClient:
    """Create an ASGI client compatible with modern httpx/FastAPI stacks."""
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as async_client:
        yield async_client


@pytest.mark.anyio
async def test_health_endpoint_returns_advisory_runtime_status(client: httpx.AsyncClient) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)


@pytest.mark.anyio
async def test_verify_endpoint_returns_advisory_placeholder_contract(client: httpx.AsyncClient) -> None:
    response = await client.get("/verify/placeholder-record")

    assert response.status_code == 200
    payload = response.json()
    assert payload["record_id"] == "placeholder-record"
    assert payload["status"] == "ADVISORY"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert "no truth guarantee" in payload["message"].lower()
    assert "truth guarantee" in payload["message"].lower()


@pytest.mark.anyio
async def test_verify_qr_flow_runs_pipeline_decision_and_response_contract(client: httpx.AsyncClient) -> None:
    response = await client.post("/verify/qr-record", json={"qr_input": "hc://demo hash:abc123"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ADVISORY"
    assert payload["trust_state"] == "ADVISORY"
    assert payload["replay_warning"] is False
    assert payload["continuity_warning"] is False
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)


@pytest.mark.anyio
async def test_qr_get_flow_runs_pipeline_and_public_safe_contract(client: httpx.AsyncClient) -> None:
    response = await client.get("/qr/qr-get-record")

    assert response.status_code == 200
    payload = response.json()
    assert payload["record_id"] == "qr-get-record"
    assert payload["status"] == "ADVISORY"
    assert payload["public_safe"] is True
    assert payload["advisory_only"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)


@pytest.mark.anyio
async def test_verify_history_endpoint_returns_public_safe_event_history(client: httpx.AsyncClient) -> None:
    await client.post("/verify/history-record", json={"qr_input": "hc://history hash:ok"})
    response = await client.get("/verify/history-record/history")

    assert response.status_code == 200
    payload = response.json()
    assert payload["record_id"] == "history-record"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert isinstance(payload["events"], list)
    assert isinstance(payload["trust_state_transitions"], list)


@pytest.mark.anyio
async def test_runtime_public_endpoints_never_expose_forbidden_authority_claims(client: httpx.AsyncClient) -> None:
    endpoint_payloads = [
        (await client.get("/health")).json(),
        (await client.get("/verify/unsafe-terms")).json(),
        (await client.post("/verify/unsafe-terms", json={"qr_input": "hc://demo hash:ok"})).json(),
        (await client.get("/qr/unsafe-terms")).json(),
        (await client.get("/verify/unsafe-terms/history")).json(),
        (await client.post("/federation/review", json={"record_id": "unsafe-terms"})).json(),
        (await client.get("/telemetry/health")).json(),
        (await client.get("/telemetry/runtime")).json(),
        (await client.get("/telemetry/queues")).json(),
    ]

    forbidden_phrases = [
        "objective truth",
        "forensic certainty",
        "enforcement",
        "autonomous governance",
        "production-ready",
    ]

    for payload in endpoint_payloads:
        message_text = str(payload.get("message", "")).lower()
        warning_text = " ".join(str(item).lower() for item in payload.get("warnings", []))
        searchable_text = f"{message_text} {warning_text}"
        for phrase in forbidden_phrases:
            assert phrase not in searchable_text


@pytest.mark.anyio
async def test_replay_warning_propagation_and_queueing(client: httpx.AsyncClient) -> None:
    response = await client.post("/verify/replay-record", json={"qr_input": "hc://demo hash:ok replay"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["replay_warning"] is True
    assert payload["public_exposure"] == "restricted"

    history = (await client.get("/verify/replay-record/history")).json()
    assert history["replay_warning_visible"] is True


@pytest.mark.anyio
async def test_federation_review_route_is_advisory_placeholder(client: httpx.AsyncClient) -> None:
    response = await client.post("/federation/review", json={"record_id": "fed-review-1", "replay_warning": True})

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ADVISORY"
    assert payload["relay"]["relay_mode"] == "local-placeholder"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert "production" not in payload["message"].lower()
    assert "objective truth" not in payload["message"].lower()


@pytest.mark.anyio
async def test_telemetry_routes_return_advisory_operational_signals(client: httpx.AsyncClient) -> None:
    telemetry_health_payload = (await client.get("/telemetry/health")).json()
    runtime_payload = (await client.get("/telemetry/runtime")).json()
    queues_payload = (await client.get("/telemetry/queues")).json()

    expected_shared_keys = {
        "status",
        "runtime_mode",
        "advisory_only",
        "public_safe",
        "traceable",
        "truth_guarantee",
        "warnings",
    }

    for payload in (telemetry_health_payload, runtime_payload, queues_payload):
        assert expected_shared_keys.issubset(payload.keys())
        assert payload["status"] == "ok"
        assert payload["runtime_mode"] == "prototype"
        assert payload["advisory_only"] is True
        assert payload["public_safe"] is True
        assert payload["traceable"] is True
        assert payload["truth_guarantee"] is False
        assert isinstance(payload["warnings"], list)

    assert queues_payload["degraded_queue_handling"] is True


@pytest.mark.anyio
async def test_degraded_runtime_recovery_behavior_is_public_safe(client: httpx.AsyncClient) -> None:
    response = await client.post("/verify/degraded-record", json={"qr_input": "hc://demo hash:ok degraded"})

    payload = response.json()
    assert response.status_code == 200
    assert payload["degraded_runtime"] is True
    assert payload["recovery_mode"] is True
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)


@pytest.mark.anyio
async def test_duplicate_verification_input_sets_replay_visibility_and_stable_shape(client: httpx.AsyncClient) -> None:
    first = await client.post("/verify/dup-record", json={"qr_input": "hc://dup hash:ok replay"})
    second = await client.post("/verify/dup-record", json={"qr_input": "hc://dup hash:ok replay"})

    assert first.status_code == 200
    assert second.status_code == 200

    expected_keys = set(first.json().keys())
    assert set(second.json().keys()) == expected_keys
    assert second.json()["replay_warning"] is True

    history = (await client.get("/verify/dup-record/history")).json()
    assert history["replay_warning_visible"] is True


@pytest.mark.anyio
async def test_continuity_history_ordering_and_append_only_visibility(client: httpx.AsyncClient) -> None:
    await client.post("/verify/continuity-record", json={"qr_input": "hc://continuity hash:ok"})
    history_first = (await client.get("/verify/continuity-record/history")).json()
    first_events = history_first["events"]
    first_events_snapshot = [event.copy() for event in first_events]

    await client.post("/verify/continuity-record", json={"qr_input": "hc://continuity hash:ok continuity-warning"})
    history_second = (await client.get("/verify/continuity-record/history")).json()
    second_events = history_second["events"]

    assert len(second_events) > len(first_events_snapshot)
    assert second_events[: len(first_events_snapshot)] == first_events_snapshot
    assert [event["event_type"] for event in first_events_snapshot[:2]] == [
        "trust_state_transition",
        "continuity_checkpoint",
    ]


@pytest.mark.anyio
async def test_runtime_state_isolation_starts_clean_for_each_test(client: httpx.AsyncClient) -> None:
    history = (await client.get("/verify/isolation-record/history")).json()
    assert history["events"] == []
    assert QUEUE_STORE.verification_queue == []
    assert QUEUE_STORE.escalation_queue == []
    assert QUEUE_STORE.replay_warning_queue == []
