"""Safety contract tests for HC:// advisory telemetry payloads."""

from __future__ import annotations

from typing import Any

import httpx
import pytest

from hc_runtime.app import create_app
from hc_runtime.state import ABUSE_SIGNAL_TRACKER, EVENT_STORE, QUEUE_STORE

TELEMETRY_ENDPOINTS = (
    "/telemetry/health",
    "/telemetry/runtime",
    "/telemetry/queues",
)

BASE_KEY_ORDER = (
    "status",
    "runtime_mode",
    "advisory_only",
    "runtime_stage",
    "verification_mode",
    "public_safe",
    "traceable",
    "truth_guarantee",
    "warnings",
    "human_review_required",
    "degraded",
    "degraded_reasons",
)

ENDPOINT_KEY_ORDER = {
    "/telemetry/health": BASE_KEY_ORDER,
    "/telemetry/runtime": BASE_KEY_ORDER + ("events_total", "degraded_events"),
    "/telemetry/queues": BASE_KEY_ORDER
    + (
        "verification_queue",
        "escalation_queue",
        "replay_warning_queue",
        "degraded_queue_handling",
    ),
}


@pytest.fixture(autouse=True)
def reset_runtime_state() -> None:
    """Reset shared advisory runtime state for deterministic telemetry tests."""
    EVENT_STORE._events.clear()
    QUEUE_STORE.verification_queue.clear()
    QUEUE_STORE.escalation_queue.clear()
    QUEUE_STORE.replay_warning_queue.clear()
    ABUSE_SIGNAL_TRACKER.reset()


@pytest.fixture()
async def client() -> httpx.AsyncClient:
    """Create an ASGI client for telemetry endpoint contract checks."""
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as async_client:
        yield async_client


async def _telemetry_payloads(client: httpx.AsyncClient) -> dict[str, dict[str, Any]]:
    payloads: dict[str, dict[str, Any]] = {}
    for endpoint in TELEMETRY_ENDPOINTS:
        response = await client.get(endpoint)
        assert response.status_code == 200
        payloads[endpoint] = response.json()
    return payloads


@pytest.mark.anyio
async def test_telemetry_payload_key_order_is_deterministic(client: httpx.AsyncClient) -> None:
    payloads = await _telemetry_payloads(client)

    for endpoint, payload in payloads.items():
        assert tuple(payload.keys()) == ENDPOINT_KEY_ORDER[endpoint]


@pytest.mark.anyio
async def test_telemetry_payload_safety_flags_are_locked(client: httpx.AsyncClient) -> None:
    payloads = await _telemetry_payloads(client)

    for payload in payloads.values():
        assert payload["advisory_only"] is True
        assert payload["public_safe"] is True
        assert payload["truth_guarantee"] is False
        assert payload["verification_mode"] == "advisory"
        assert payload["runtime_stage"] == "prototype"
        assert isinstance(payload["warnings"], list)
