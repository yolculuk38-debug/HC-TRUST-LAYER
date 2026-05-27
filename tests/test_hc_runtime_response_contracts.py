"""Tests for HC:// reference runtime public verification response contracts."""

from pathlib import Path

import pytest

import fastapi  # noqa: F401
import httpx

from hc_runtime.contracts.responses import (
    advisory_response,
    continuity_warning_response,
    degraded_runtime_response,
    disputed_response,
    not_found_response,
    unresolved_response,
    verified_placeholder_response,
)
from hc_runtime.app import create_app


def _assert_public_safe_contract(payload: dict, expected_status: str, expected_record_id: str | None) -> None:
    if expected_record_id is None:
        assert "record_id" not in payload
    else:
        assert payload["record_id"] == expected_record_id

    assert payload["status"] == expected_status
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert isinstance(payload["message"], str)
    assert isinstance(payload["warnings"], list)
    assert payload["traceable"] is True
    assert payload["truth_guarantee"] is False
    assert "production" not in payload["message"].lower() or "no production readiness" in payload["message"].lower()
    assert "objective truth" not in payload["message"].lower()


def test_advisory_response_contract_shape() -> None:
    payload = advisory_response("rec-1", "Advisory message", warnings=["w1"])
    _assert_public_safe_contract(payload, "ADVISORY", "rec-1")


def test_verified_placeholder_response_contract_shape() -> None:
    payload = verified_placeholder_response("rec-2")
    _assert_public_safe_contract(payload, "VERIFIED_PLACEHOLDER", "rec-2")


def test_disputed_response_contract_shape() -> None:
    payload = disputed_response("rec-3")
    _assert_public_safe_contract(payload, "DISPUTED", "rec-3")


def test_unresolved_response_contract_shape() -> None:
    payload = unresolved_response("rec-4")
    _assert_public_safe_contract(payload, "UNRESOLVED", "rec-4")


def test_continuity_warning_response_contract_shape() -> None:
    payload = continuity_warning_response("rec-5")
    _assert_public_safe_contract(payload, "CONTINUITY_WARNING", "rec-5")


def test_degraded_runtime_response_contract_shape() -> None:
    payload = degraded_runtime_response("rec-6")
    _assert_public_safe_contract(payload, "DEGRADED_RUNTIME", "rec-6")


def test_not_found_response_contract_shape_without_record_id() -> None:
    payload = not_found_response()
    _assert_public_safe_contract(payload, "NOT_FOUND", None)


def test_not_found_response_contract_shape_with_record_id() -> None:
    payload = not_found_response("rec-404")
    _assert_public_safe_contract(payload, "NOT_FOUND", "rec-404")


def test_verify_route_uses_advisory_response_contract_builder() -> None:
    verify_route = Path("src/hc_runtime/routes/verify.py").read_text(encoding="utf-8")

    assert "from hc_runtime.contracts import advisory_response" in verify_route
    assert "return advisory_response(" in verify_route


def test_verify_runtime_routes_preserve_advisory_contract_guarantees() -> None:
    verify_route = Path("src/hc_runtime/routes/verify.py").read_text(encoding="utf-8")

    assert '"advisory_only": True' in verify_route
    assert '"public_safe": True' in verify_route
    assert '"truth_guarantee": False' in verify_route
    assert '"warnings": [' in verify_route or '"warnings": []' in verify_route


def test_advisory_contract_messages_do_not_imply_forbidden_claims() -> None:
    payloads = [
        advisory_response("rec-a", "Advisory only response with no truth guarantee."),
        verified_placeholder_response("rec-b"),
        disputed_response("rec-c"),
        unresolved_response("rec-d"),
        continuity_warning_response("rec-e"),
        degraded_runtime_response("rec-f"),
        not_found_response("rec-g"),
    ]
    forbidden_phrases = [
        "objective truth",
        "forensic certainty",
        "autonomous governance",
        "production ready",
        "production readiness achieved",
        "enforcement authority",
    ]

    for payload in payloads:
        message = payload["message"].lower()
        assert payload["advisory_only"] is True
        assert payload["public_safe"] is True
        assert payload["truth_guarantee"] is False
        assert isinstance(payload["warnings"], list)
        for forbidden in forbidden_phrases:
            assert forbidden not in message


@pytest.mark.anyio
async def test_telemetry_payload_shape_stability_regression() -> None:
    expected_health_keys = {
        "status",
        "runtime_mode",
        "advisory_only",
        "public_safe",
        "traceable",
        "truth_guarantee",
        "warnings",
    }
    expected_runtime_keys = expected_health_keys | {"events_total", "degraded_events"}
    expected_queue_keys = expected_health_keys | {
        "verification_queue",
        "escalation_queue",
        "replay_warning_queue",
        "degraded_queue_handling",
    }

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        telemetry_health_payload = (await client.get("/telemetry/health")).json()
        telemetry_runtime_payload = (await client.get("/telemetry/runtime")).json()
        telemetry_queues_payload = (await client.get("/telemetry/queues")).json()

    assert set(telemetry_health_payload.keys()) == expected_health_keys
    assert set(telemetry_runtime_payload.keys()) == expected_runtime_keys
    assert set(telemetry_queues_payload.keys()) == expected_queue_keys
