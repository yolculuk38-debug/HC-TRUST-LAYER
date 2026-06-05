"""Telemetry payload contract coverage for HC:// advisory runtime endpoints."""

from __future__ import annotations

import json
from collections.abc import Callable
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
QUEUE_FIELDS = ("verification_queue", "escalation_queue", "replay_warning_queue")
SECRET_MARKERS = (
    "token=",
    "api_key=",
    "credential=",
    "ghp_",
    "akia0000000000000000",
    "-----begin private key-----",
)


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


def _append_degraded_runtime_event(record_id: str = "telemetry-degraded-record") -> None:
    EVENT_STORE.append_runtime_event(
        event_type="runtime_recovery_mode",
        record_id=record_id,
        details={"degraded_detected": True, "recovery_mode": True, "failover_safe": True},
    )


def _populate_verification_queue(record_id: str = "telemetry-verification-record") -> None:
    QUEUE_STORE.enqueue_verification({"record_id": record_id, "qr_input": "hc://demo hash:ok"})


def _populate_replay_warning_queue(record_id: str = "telemetry-replay-record") -> None:
    QUEUE_STORE.enqueue_replay_warning({"record_id": record_id, "source": "qr-verification"})


def _populate_escalation_queue(record_id: str = "telemetry-escalation-record") -> None:
    QUEUE_STORE.enqueue_escalation(
        {
            "record_id": record_id,
            "reason": "replay_warning",
            "source": "qr-verification",
            "advisory_only": True,
            "public_safe": True,
            "truth_guarantee": False,
        }
    )


def _populate_secret_like_queue_items() -> None:
    QUEUE_STORE.enqueue_verification(
        {
            "record_id": "telemetry-redaction-record",
            "qr_input": (
                "hc://demo hash:ok token=example-token-value-000000 "
                "api_key=example-api-key-value-000000 credential=example-credential-value-000000 "
                "ghp_000000000000000000000000 AKIA0000000000000000 "
                "-----BEGIN PRIVATE KEY-----example-----END PRIVATE KEY-----"
            ),
        }
    )
    QUEUE_STORE.enqueue_escalation(
        {
            "record_id": "telemetry-redaction-record",
            "reason": "credential=example-credential-value-000000",
            "source": "qr-verification token=example-token-value-000000",
            "advisory_only": True,
            "public_safe": True,
            "truth_guarantee": False,
        }
    )
    QUEUE_STORE.enqueue_replay_warning(
        {
            "record_id": "telemetry-redaction-record",
            "source": "api_key=example-api-key-value-000000",
        }
    )


def _assert_base_telemetry_contract(
    payload: dict[str, Any],
    *,
    degraded: bool,
    human_review_required: bool,
) -> None:
    assert payload["advisory_only"] is True
    assert payload["runtime_stage"] == "prototype"
    assert payload["verification_mode"] == "advisory"
    assert payload["public_safe"] is True
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert all(isinstance(warning, str) for warning in payload["warnings"])
    assert payload["human_review_required"] is human_review_required
    expected_review_flag = bool(payload["warnings"]) or (
        human_review_required and not bool(payload["warnings"])
    )
    assert payload["human_review_required"] is expected_review_flag
    assert payload["degraded"] is degraded
    assert payload["status"] == ("degraded" if degraded else "ok")
    assert payload["degraded_reasons"] == (["runtime_recovery_mode"] if degraded else [])
    assert bool(payload["warnings"]) is degraded


def _assert_runtime_telemetry_contract(payload: dict[str, Any], *, degraded: bool) -> None:
    assert isinstance(payload["events_total"], int)
    assert not isinstance(payload["events_total"], bool)
    assert isinstance(payload["degraded_events"], int)
    assert not isinstance(payload["degraded_events"], bool)
    assert payload["degraded_events"] == (1 if degraded else 0)
    assert payload["events_total"] >= payload["degraded_events"]


def _assert_queue_telemetry_contract(
    payload: dict[str, Any],
    *,
    expected_counts: dict[str, int],
) -> None:
    for field in QUEUE_FIELDS:
        assert isinstance(payload[field], list)
        count = len(payload[field])
        assert isinstance(count, int)
        assert not isinstance(count, bool)
        assert count == expected_counts[field]

    assert payload["degraded_queue_handling"] is True
    assert len(payload["replay_warning_queue"]) == expected_counts["replay_warning_queue"]


async def _telemetry_payloads(client: httpx.AsyncClient) -> dict[str, dict[str, Any]]:
    payloads: dict[str, dict[str, Any]] = {}
    for endpoint in TELEMETRY_ENDPOINTS:
        response = await client.get(endpoint)
        assert response.status_code == 200
        payloads[endpoint] = response.json()
    return payloads


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("case_name", "setup", "degraded", "expected_counts", "queue_human_review_required"),
    [
        (
            "clean runtime state",
            lambda: None,
            False,
            {"verification_queue": 0, "escalation_queue": 0, "replay_warning_queue": 0},
            False,
        ),
        (
            "degraded runtime event exists",
            _append_degraded_runtime_event,
            True,
            {"verification_queue": 0, "escalation_queue": 0, "replay_warning_queue": 0},
            True,
        ),
        (
            "replay warning queue populated",
            _populate_replay_warning_queue,
            False,
            {"verification_queue": 0, "escalation_queue": 0, "replay_warning_queue": 1},
            False,
        ),
        (
            "escalation queue populated",
            _populate_escalation_queue,
            False,
            {"verification_queue": 0, "escalation_queue": 1, "replay_warning_queue": 0},
            True,
        ),
        (
            "verification queue populated",
            _populate_verification_queue,
            False,
            {"verification_queue": 1, "escalation_queue": 0, "replay_warning_queue": 0},
            False,
        ),
        (
            "mixed degraded replay escalation state",
            lambda: (
                _append_degraded_runtime_event("telemetry-mixed-degraded-record"),
                _populate_replay_warning_queue("telemetry-mixed-replay-record"),
                _populate_escalation_queue("telemetry-mixed-escalation-record"),
            ),
            True,
            {"verification_queue": 0, "escalation_queue": 1, "replay_warning_queue": 1},
            True,
        ),
    ],
    ids=lambda value: value if isinstance(value, str) else None,
)
async def test_telemetry_payload_contract_is_stable_across_runtime_queue_edges(
    client: httpx.AsyncClient,
    case_name: str,
    setup: Callable[[], object],
    degraded: bool,
    expected_counts: dict[str, int],
    queue_human_review_required: bool,
) -> None:
    setup()

    payloads = await _telemetry_payloads(client)

    _assert_base_telemetry_contract(
        payloads["/telemetry/health"],
        degraded=degraded,
        human_review_required=degraded,
    )
    _assert_base_telemetry_contract(
        payloads["/telemetry/runtime"],
        degraded=degraded,
        human_review_required=degraded,
    )
    _assert_runtime_telemetry_contract(payloads["/telemetry/runtime"], degraded=degraded)
    _assert_base_telemetry_contract(
        payloads["/telemetry/queues"],
        degraded=degraded,
        human_review_required=queue_human_review_required,
    )
    _assert_queue_telemetry_contract(payloads["/telemetry/queues"], expected_counts=expected_counts)

    assert case_name


@pytest.mark.anyio
async def test_telemetry_payloads_do_not_expose_secret_token_or_credential_markers(
    client: httpx.AsyncClient,
) -> None:
    _populate_secret_like_queue_items()

    payloads = await _telemetry_payloads(client)
    serialized_payloads = json.dumps(payloads, sort_keys=True).lower()

    for marker in SECRET_MARKERS:
        assert marker not in serialized_payloads
    assert "[redacted]" in serialized_payloads
    _assert_queue_telemetry_contract(
        payloads["/telemetry/queues"],
        expected_counts={
            "verification_queue": 1,
            "escalation_queue": 1,
            "replay_warning_queue": 1,
        },
    )


@pytest.mark.anyio
async def test_human_review_required_bool_algebra_is_deterministic(client: httpx.AsyncClient) -> None:
    """Validate that human_review_required follows the deterministic bool algebra:
    human_review_required = bool(warnings) OR escalation_required

    This ensures:
    - When warnings exist, human_review_required=True
    - When escalation queue has items, human_review_required=True
    - Otherwise, human_review_required=False
    """
    # Case 1: clean state (no warnings, no escalation)
    payloads_clean = await _telemetry_payloads(client)
    for endpoint_name, payload in payloads_clean.items():
        warnings_bool = bool(payload["warnings"])
        escalation_bool = bool(payload.get("escalation_queue", []))
        expected = warnings_bool or escalation_bool
        assert payload["human_review_required"] is expected, (
            f"{endpoint_name}: human_review_required={payload['human_review_required']} "
            f"does not match bool(warnings)={warnings_bool} or "
            f"escalation_required={escalation_bool}, expected={expected}"
        )

    # Case 2: degraded runtime (warnings exist)
    EVENT_STORE._events.clear()
    QUEUE_STORE.verification_queue.clear()
    QUEUE_STORE.escalation_queue.clear()
    QUEUE_STORE.replay_warning_queue.clear()

    _append_degraded_runtime_event()
    payloads_degraded = await _telemetry_payloads(client)
    for endpoint_name, payload in payloads_degraded.items():
        # degraded state always has warnings
        assert bool(payload["warnings"]) is True
        assert payload["human_review_required"] is True

    # Case 3: escalation queue populated (escalation_required=True)
    EVENT_STORE._events.clear()
    QUEUE_STORE.verification_queue.clear()
    QUEUE_STORE.escalation_queue.clear()
    QUEUE_STORE.replay_warning_queue.clear()

    _populate_escalation_queue()
    payloads_escalation = await _telemetry_payloads(client)
    for endpoint_name, payload in payloads_escalation.items():
        escalation_bool = bool(payload.get("escalation_queue", []))
        warnings_bool = bool(payload["warnings"])
        # /telemetry/queues should have escalation_queue populated
        if endpoint_name == "/telemetry/queues":
            assert escalation_bool is True
            expected = warnings_bool or escalation_bool
            assert payload["human_review_required"] is expected
        else:
            # Other endpoints don't expose escalation_queue directly, but they're aware of it
            # via escalation_required parameter passed to _telemetry_base
            expected = warnings_bool or escalation_bool
            assert payload["human_review_required"] is expected
