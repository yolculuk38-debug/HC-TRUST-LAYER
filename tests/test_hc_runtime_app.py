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
async def test_telemetry_endpoints_expose_consistent_advisory_metadata(client: httpx.AsyncClient) -> None:
    telemetry_payloads = [
        (await client.get("/telemetry/health")).json(),
        (await client.get("/telemetry/runtime")).json(),
        (await client.get("/telemetry/queues")).json(),
    ]
    expected_metadata = {
        "advisory_only": True,
        "public_safe": True,
        "traceable": True,
        "truth_guarantee": False,
    }

    for payload in telemetry_payloads:
        for key, expected in expected_metadata.items():
            assert key in payload
            assert payload[key] is expected
        assert isinstance(payload["warnings"], list)
        assert all(isinstance(warning, str) for warning in payload["warnings"])


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


@pytest.mark.anyio
async def test_advisory_downgrade_safety_keeps_warnings_visible_and_public_safe(client: httpx.AsyncClient) -> None:
    degraded = (await client.post("/verify/downgrade-record", json={"qr_input": "hc://downgrade hash:ok degraded"})).json()
    replay = (await client.post("/verify/downgrade-record", json={"qr_input": "hc://downgrade hash:ok replay"})).json()

    for payload in (degraded, replay):
        assert payload["advisory_only"] is True
        assert payload["public_safe"] is True
        assert isinstance(payload["warnings"], list)
        assert payload["warnings"]
        assert all(isinstance(warning, str) for warning in payload["warnings"])

    assert any("degraded runtime restriction policy" in warning.lower() for warning in degraded["warnings"])
    assert any("replay-warning escalation policy" in warning.lower() for warning in replay["warnings"])


@pytest.mark.anyio
async def test_event_policy_correlation_remains_append_only_and_telemetry_consistent(client: httpx.AsyncClient) -> None:
    record_id = "event-policy-record"
    response = await client.post(f"/verify/{record_id}", json={"qr_input": "hc://event hash:ok replay"})
    payload = response.json()
    history_payload = (await client.get(f"/verify/{record_id}/history")).json()
    telemetry_runtime = (await client.get("/telemetry/runtime")).json()

    assert payload["public_exposure"] == "restricted"
    assert history_payload["replay_warning_visible"] is True
    assert isinstance(history_payload["events"], list)
    assert len(history_payload["events"]) >= 3
    assert all(event["public_safe"] is True for event in history_payload["events"])
    assert telemetry_runtime["advisory_only"] is True
    assert telemetry_runtime["public_safe"] is True


@pytest.mark.anyio
async def test_runtime_warning_lists_remain_deterministic_and_ordered(client: httpx.AsyncClient) -> None:
    first_response = await client.post(
        "/verify/warning-order-record",
        json={"qr_input": "hc://warning-order hash:ok replay degraded"},
    )
    second_response = await client.post(
        "/verify/warning-order-record",
        json={"qr_input": "hc://warning-order hash:ok replay degraded"},
    )
    first = first_response.json()
    second = second_response.json()

    assert isinstance(first["warnings"], list)
    assert isinstance(second["warnings"], list)
    assert first["warnings"] == second["warnings"]
    assert first["warnings"][0].lower().startswith("replay warning")
    assert first["warnings"][-1].lower().startswith("degraded runtime restriction policy")

    assert first_response.status_code == 200
    assert second_response.status_code == 200

    expected_keys = set(first.keys())
    assert set(second.keys()) == expected_keys
    assert second["replay_warning"] is True

    history = (await client.get("/verify/dup-record/history")).json()
    assert history["replay_warning_visible"] is True


@pytest.mark.anyio
async def test_identical_verification_inputs_are_deterministic_for_advisory_contract(client: httpx.AsyncClient) -> None:
    qr_input = "hc://deterministic hash:ok replay"
    first_payload = (await client.post("/verify/deterministic-record", json={"qr_input": qr_input})).json()
    second_payload = (await client.post("/verify/deterministic-record", json={"qr_input": qr_input})).json()

    stable_keys = {
        "status",
        "advisory_only",
        "public_safe",
        "traceable",
        "truth_guarantee",
        "trust_state",
        "replay_warning",
        "continuity_warning",
        "degraded_runtime",
        "recovery_mode",
        "public_exposure",
    }

    assert set(first_payload.keys()) == set(second_payload.keys())
    assert stable_keys.issubset(first_payload.keys())
    for key in stable_keys:
        assert first_payload[key] == second_payload[key]
    assert isinstance(first_payload["warnings"], list)
    assert isinstance(second_payload["warnings"], list)
    assert all(isinstance(warning, str) for warning in first_payload["warnings"])
    assert first_payload["warnings"] == second_payload["warnings"]


@pytest.mark.anyio
async def test_runtime_policy_flags_are_visible_and_deterministic(client: httpx.AsyncClient) -> None:
    payload = (await client.post("/verify/policy-visible-record", json={"qr_input": "hc://demo hash:ok replay degraded"})).json()

    assert payload["replay_warning"] is True
    assert payload["degraded_runtime"] is True
    assert payload["recovery_mode"] is True
    assert payload["public_exposure"] == "restricted"
    assert isinstance(payload["warnings"], list)
    assert any("replay-warning escalation policy" in warning.lower() for warning in payload["warnings"])
    assert any("degraded runtime restriction policy" in warning.lower() for warning in payload["warnings"])


@pytest.mark.anyio
async def test_verify_rejects_empty_payload_with_public_safe_validation_error(client: httpx.AsyncClient) -> None:
    response = await client.post("/verify/empty-payload-record", json={})

    assert response.status_code == 422
    payload = response.json()
    assert "detail" in payload
    assert "traceback" not in str(payload).lower()


@pytest.mark.anyio
async def test_verify_rejects_malformed_qr_input_type_with_public_safe_validation_error(client: httpx.AsyncClient) -> None:
    response = await client.post("/verify/malformed-qr-record", json={"qr_input": {"unexpected": "object"}})

    assert response.status_code == 422
    payload = response.json()
    assert "detail" in payload
    assert "traceback" not in str(payload).lower()


@pytest.mark.anyio
async def test_verify_accepts_oversized_advisory_input_placeholder_with_stable_contract(client: httpx.AsyncClient) -> None:
    oversized_qr_input = f"hc://oversized {'a' * 12000} hash:ok"
    response = await client.post("/verify/oversized-placeholder-record", json={"qr_input": oversized_qr_input})

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ADVISORY"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)


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


@pytest.mark.anyio
async def test_runtime_response_aligns_with_emitted_event_metadata(client: httpx.AsyncClient) -> None:
    response = await client.post("/verify/alignment-record", json={"qr_input": "hc://alignment hash:ok replay"})
    payload = response.json()
    history = (await client.get("/verify/alignment-record/history")).json()

    latest_transition = history["trust_state_transitions"][-1]
    assert payload["trust_state"] == latest_transition["details"]["trust_state"]
    assert payload["replay_warning"] is True
    assert history["replay_warning_visible"] is True


@pytest.mark.anyio
async def test_degraded_response_and_history_remain_consistent(client: httpx.AsyncClient) -> None:
    response = await client.post("/verify/degraded-consistency-record", json={"qr_input": "hc://demo hash:ok degraded"})
    payload = response.json()
    history = (await client.get("/verify/degraded-consistency-record/history")).json()

    event_types = [event["event_type"] for event in history["events"]]
    assert payload["degraded_runtime"] is True
    assert payload["recovery_mode"] is True
    assert "runtime_recovery_mode" in event_types


@pytest.mark.anyio
async def test_telemetry_and_event_visibility_remain_internally_consistent(client: httpx.AsyncClient) -> None:
    runtime_before = (await client.get("/telemetry/runtime")).json()
    queues_before = (await client.get("/telemetry/queues")).json()

    await client.post("/verify/telemetry-consistency-record", json={"qr_input": "hc://demo hash:ok replay degraded"})

    runtime_after = (await client.get("/telemetry/runtime")).json()
    queues_after = (await client.get("/telemetry/queues")).json()
    history = (await client.get("/verify/telemetry-consistency-record/history")).json()

    assert runtime_after["events_total"] >= runtime_before["events_total"] + len(history["events"])
    assert runtime_after["degraded_events"] >= runtime_before["degraded_events"] + 1
    assert queues_after["verification_queue"] == queues_before["verification_queue"] + 1
    assert queues_after["replay_warning_queue"] == queues_before["replay_warning_queue"] + 1
    assert queues_after["escalation_queue"] >= queues_before["escalation_queue"] + 1
    assert isinstance(runtime_after["warnings"], list)
    assert isinstance(queues_after["warnings"], list)
