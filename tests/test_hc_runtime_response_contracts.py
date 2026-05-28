"""Tests for HC:// reference runtime public verification response contracts."""

from pathlib import Path

import pytest

import fastapi  # noqa: F401
import httpx

from hc_runtime.contracts.responses import (
    advisory_response,
    continuity_warning_response,
    degraded_runtime_response,
    malformed_input_response,
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
        malformed_input_response("rec-h"),
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
        "degraded",
        "degraded_reasons",
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


@pytest.mark.anyio
async def test_replay_and_degraded_response_warning_lists_remain_stable() -> None:
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        replay_payload = (
            await client.post("/verify/replay-contract-record", json={"qr_input": "hc://demo hash:ok replay"})
        ).json()
        degraded_payload = (
            await client.post("/verify/degraded-contract-record", json={"qr_input": "hc://demo hash:ok degraded"})
        ).json()

    assert isinstance(replay_payload["warnings"], list)
    assert isinstance(degraded_payload["warnings"], list)
    assert all(isinstance(warning, str) for warning in replay_payload["warnings"])
    assert all(isinstance(warning, str) for warning in degraded_payload["warnings"])


@pytest.mark.anyio
async def test_verify_response_field_order_and_shape_are_stable_for_runtime_outputs() -> None:
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        payload = (await client.post("/verify/order-contract-record", json={"qr_input": "hc://demo hash:ok replay"})).json()

    expected_order = [
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
    assert list(payload.keys()) == expected_order
    assert isinstance(payload["warnings"], list)


@pytest.mark.anyio
async def test_malformed_verify_payload_does_not_leak_internal_trace_text() -> None:
    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.post("/verify/malformed-record", json={"unexpected": "field"})

    assert response.status_code == 422
    payload = response.json()
    serialized = str(payload).lower()
    assert "traceback" not in serialized
    assert "internal server error" not in serialized
    assert "exception" not in serialized


def test_runtime_response_builders_keep_warning_lists_normalized() -> None:
    payload = advisory_response("normalized-warning-record", "Normalized warning response.", warnings=["one", "two"])
    degraded = degraded_runtime_response("normalized-degraded-record", warnings=["degraded warning"])

    assert isinstance(payload["warnings"], list)
    assert isinstance(degraded["warnings"], list)
    assert payload["warnings"] == ["one", "two"]
    assert degraded["warnings"] == ["degraded warning"]
    assert payload["public_safe"] is True
    assert degraded["public_safe"] is True


def _assert_validator_runtime_contract(payload: dict, expected_record_id: str) -> None:
    assert payload["record_id"] == expected_record_id
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert all(isinstance(warning, str) for warning in payload["warnings"])


@pytest.mark.anyio
async def test_validator_runtime_responses_are_consistent_for_qr_input_cases() -> None:
    cases = [
        ("empty-qr-input", "", "UNRESOLVED", True, False),
        ("normal-qr-input", "hc://normal hash:ok", "ADVISORY", False, False),
        ("invalid-hash-marker", "hc://normal sha256:not-a-validator-marker", "REVIEW_REQUIRED", True, False),
        ("stale-replayed-payload", "hc://normal hash:ok stale replay", "REPLAY_WARNING", True, True),
        ("degraded-validator-state", "hc://normal hash:ok degraded", "DEGRADED", True, False),
    ]

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        for record_id, qr_input, trust_state, expects_warning, expects_replay in cases:
            response = await client.post(f"/verify/{record_id}", json={"qr_input": qr_input})
            payload = response.json()

            assert response.status_code == 200
            _assert_validator_runtime_contract(payload, record_id)
            assert payload["trust_state"] == trust_state
            assert payload["replay_warning"] is expects_replay
            assert bool(payload["warnings"]) is expects_warning
            if "degraded" in record_id or "degraded" in qr_input:
                assert payload["degraded_runtime"] is True
                assert payload["recovery_mode"] is True


@pytest.mark.anyio
async def test_malformed_and_missing_validator_payloads_return_public_safe_warning_contract() -> None:
    cases = [
        ("missing-payload-fields", {"unexpected": "field"}),
        ("malformed-qr-input", {"qr_input": {"not": "a string"}}),
    ]
    expected_order = [
        "status",
        "advisory_only",
        "public_safe",
        "message",
        "warnings",
        "traceable",
        "truth_guarantee",
        "record_id",
        "malformed_input",
        "public_exposure",
    ]

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        for record_id, request_json in cases:
            response = await client.post(f"/verify/{record_id}", json=request_json)
            payload = response.json()

            assert response.status_code == 422
            assert list(payload.keys()) == expected_order
            _assert_validator_runtime_contract(payload, record_id)
            assert payload["status"] == "MALFORMED_INPUT"
            assert payload["malformed_input"] is True
            assert payload["public_exposure"] == "restricted"
            assert any("malformed" in warning.lower() for warning in payload["warnings"])
            assert any("no hidden fallback" in warning.lower() for warning in payload["warnings"])


@pytest.mark.anyio
async def test_replay_degraded_and_escalation_visibility_remain_explicit() -> None:
    record_id = "warning-escalation-visibility"

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        payload = (
            await client.post(
                f"/verify/{record_id}",
                json={"qr_input": "hc://warning-escalation hash:ok replay degraded continuity-warning"},
            )
        ).json()
        history = (await client.get(f"/verify/{record_id}/history")).json()
        queues = (await client.get("/telemetry/queues")).json()

    _assert_validator_runtime_contract(payload, record_id)
    assert payload["replay_warning"] is True
    assert payload["continuity_warning"] is True
    assert payload["degraded_runtime"] is True
    assert payload["recovery_mode"] is True
    assert payload["public_exposure"] == "restricted"
    assert any("replay" in warning.lower() for warning in payload["warnings"])
    assert any("degraded" in warning.lower() for warning in payload["warnings"])
    assert any("human-supervised validation" in warning.lower() for warning in payload["warnings"])
    assert history["replay_warning_visible"] is True
    assert any(item["reason"] == "replay_warning" for item in queues["escalation_queue"])
    assert any(item["reason"] == "advisory_downgrade" for item in queues["escalation_queue"])


@pytest.mark.anyio
async def test_validator_output_keys_are_stable_across_normal_replayed_and_degraded_responses() -> None:
    expected_order = [
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
    cases = [
        ("stable-normal-output", "hc://stable hash:ok"),
        ("stable-replayed-output", "hc://stable hash:ok replay"),
        ("stable-degraded-output", "hc://stable hash:ok degraded"),
    ]

    transport = httpx.ASGITransport(app=create_app())
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        payloads = [
            (await client.post(f"/verify/{record_id}", json={"qr_input": qr_input})).json()
            for record_id, qr_input in cases
        ]

    assert [list(payload.keys()) for payload in payloads] == [expected_order, expected_order, expected_order]
    for payload, (record_id, _qr_input) in zip(payloads, cases, strict=True):
        _assert_validator_runtime_contract(payload, record_id)
