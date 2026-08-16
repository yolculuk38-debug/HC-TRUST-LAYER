"""HC Optical Egress Guard decision and evidence-boundary tests."""

from __future__ import annotations

import copy
import hashlib

import pytest

from hc_trust.canonicalization import canonicalize_json
from hc_trust.egress_guard import (
    DECISION_ALLOW,
    DECISION_BLOCK,
    DECISION_HASH_PROFILE,
    EVENT_HASH_PROFILE,
    POLICY_HASH_PROFILE,
    EgressGuardError,
    build_fail_closed_error,
    evaluate_egress_event,
)


def _policy() -> dict:
    return {
        "schema_version": "hc-egress-policy-v1",
        "policy_id": "policy-test-001",
        "channel_type": "OPTICAL",
        "enforcement_mode": "EVIDENCE_ONLY",
        "thresholds": {
            "min_intensity_ratio": 0.85,
            "max_intensity_ratio": 1.15,
            "max_polarization_deviation_deg": 2.0,
            "max_out_of_band_fraction": 0.01,
        },
    }


def _event() -> dict:
    return {
        "schema_version": "hc-egress-sensor-event-v1",
        "event_id": "event-test-001",
        "session_id": "session-test-001",
        "captured_at": "2026-08-15T04:00:00Z",
        "channel_id": "optical-egress-01",
        "channel_type": "OPTICAL",
        "telemetry": {
            "sensor_health": "OK",
            "calibration_status": "VALID",
            "controller_is_independent": True,
            "intensity_ratio": 1.0,
            "polarization_deviation_deg": 0.2,
            "out_of_band_fraction": 0.001,
            "detector_saturated": False,
            "power_state": "ON",
            "shutter_state": "OPEN",
        },
    }


def test_normal_event_produces_bounded_allow_result() -> None:
    result = evaluate_egress_event(_event(), _policy())

    assert result["decision"] == DECISION_ALLOW
    assert result["recommended_action"] == "ALLOW_CHANNEL"
    assert result["reason_codes"] == ["POLICY_CHECKS_PASSED"]
    assert result["hardware_enforcement_performed"] is False
    assert result["human_review_required"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["assurance"] == {
        "policy_authentication": "NOT_VERIFIED",
        "telemetry_authentication": "NOT_VERIFIED",
        "decision_authentication": "NOT_SIGNED",
        "hardware_enforcement": "NOT_CONNECTED",
        "replay_protection": "NOT_IMPLEMENTED",
        "quantum_security": "NOT_CLAIMED",
    }


def test_trip_signals_produce_fixed_order_fail_closed_reasons() -> None:
    event = _event()
    event["telemetry"].update(
        {
            "sensor_health": "DEGRADED",
            "calibration_status": "EXPIRED",
            "controller_is_independent": False,
            "intensity_ratio": 0.2,
            "polarization_deviation_deg": 20.0,
            "out_of_band_fraction": 0.4,
            "detector_saturated": True,
            "power_state": "LOSS",
            "shutter_state": "OPEN",
        }
    )

    result = evaluate_egress_event(event, _policy())

    assert result["decision"] == DECISION_BLOCK
    assert result["recommended_action"] == "CLOSE_AND_HOLD"
    assert result["reason_codes"] == [
        "SENSOR_HEALTH_NOT_OK",
        "CALIBRATION_NOT_VALID",
        "CONTROLLER_NOT_INDEPENDENT",
        "DETECTOR_SATURATED",
        "POWER_NOT_ON",
        "FAIL_SAFE_SHUTTER_NOT_CLOSED",
        "INTENSITY_BELOW_POLICY",
        "POLARIZATION_DEVIATION_ABOVE_POLICY",
        "OUT_OF_BAND_FRACTION_ABOVE_POLICY",
    ]


def test_power_loss_with_closed_shutter_still_blocks_without_false_failure() -> None:
    event = _event()
    event["telemetry"]["power_state"] = "LOSS"
    event["telemetry"]["shutter_state"] = "CLOSED"

    result = evaluate_egress_event(event, _policy())

    assert result["decision"] == DECISION_BLOCK
    assert result["reason_codes"] == ["POWER_NOT_ON"]
    assert "FAIL_SAFE_SHUTTER_NOT_CLOSED" not in result["reason_codes"]


def test_above_maximum_intensity_blocks() -> None:
    event = _event()
    event["telemetry"]["intensity_ratio"] = 1.5

    result = evaluate_egress_event(event, _policy())

    assert result["decision"] == DECISION_BLOCK
    assert result["reason_codes"] == ["INTENSITY_ABOVE_POLICY"]


def test_result_and_digests_are_deterministic_and_inputs_are_not_mutated() -> None:
    event = _event()
    policy = _policy()
    event_snapshot = copy.deepcopy(event)
    policy_snapshot = copy.deepcopy(policy)

    first = evaluate_egress_event(event, policy)
    second = evaluate_egress_event(copy.deepcopy(event), copy.deepcopy(policy))

    assert first == second
    assert event == event_snapshot
    assert policy == policy_snapshot
    assert first["evidence"]["event_digest"] == {
        "algorithm": "sha-256",
        "profile": EVENT_HASH_PROFILE,
        "value": hashlib.sha256(canonicalize_json(event)).hexdigest(),
    }
    assert first["evidence"]["policy_digest"] == {
        "algorithm": "sha-256",
        "profile": POLICY_HASH_PROFILE,
        "value": hashlib.sha256(canonicalize_json(policy)).hexdigest(),
    }
    unhashed_result = dict(first)
    decision_digest = unhashed_result.pop("decision_digest")
    assert decision_digest == {
        "algorithm": "sha-256",
        "profile": DECISION_HASH_PROFILE,
        "value": hashlib.sha256(canonicalize_json(unhashed_result)).hexdigest(),
    }


@pytest.mark.parametrize(
    ("mutation", "reason_code", "field"),
    [
        (lambda event: event.pop("channel_id"), "REQUIRED_FIELD_MISSING", "event.channel_id"),
        (lambda event: event.update({"unexpected": True}), "UNKNOWN_FIELD", "event"),
        (
            lambda event: event["telemetry"].update({"detector_saturated": 1}),
            "BOOLEAN_REQUIRED",
            "event.telemetry.detector_saturated",
        ),
        (
            lambda event: event.update({"captured_at": "2026-08-15T04:00:00"}),
            "INVALID_TIMESTAMP",
            "event.captured_at",
        ),
    ],
)
def test_invalid_event_contract_fails_closed(mutation, reason_code, field) -> None:
    event = _event()
    mutation(event)

    with pytest.raises(EgressGuardError) as exc_info:
        evaluate_egress_event(event, _policy())

    assert exc_info.value.reason_code == reason_code
    assert exc_info.value.document == "EVENT"
    assert exc_info.value.field == field
    error_result = build_fail_closed_error(exc_info.value)
    assert error_result["decision"] == DECISION_BLOCK
    assert error_result["recommended_action"] == "CLOSE_AND_HOLD"
    assert error_result["hardware_enforcement_performed"] is False


def test_policy_cannot_enable_unimplemented_hardware_mode() -> None:
    policy = _policy()
    policy["enforcement_mode"] = "HARDWARE"

    with pytest.raises(EgressGuardError) as exc_info:
        evaluate_egress_event(_event(), policy)

    assert exc_info.value.reason_code == "UNSUPPORTED_FIELD_VALUE"
    assert exc_info.value.document == "POLICY"
    assert exc_info.value.field == "policy.enforcement_mode"


def test_policy_rejects_inverted_intensity_thresholds() -> None:
    policy = _policy()
    policy["thresholds"]["min_intensity_ratio"] = 1.2
    policy["thresholds"]["max_intensity_ratio"] = 0.8

    with pytest.raises(EgressGuardError) as exc_info:
        evaluate_egress_event(_event(), policy)

    assert exc_info.value.reason_code == "INVALID_THRESHOLD_ORDER"
    assert exc_info.value.document == "POLICY"


def test_numeric_booleans_are_not_accepted_as_measurements() -> None:
    event = _event()
    event["telemetry"]["intensity_ratio"] = True

    with pytest.raises(EgressGuardError) as exc_info:
        evaluate_egress_event(event, _policy())

    assert exc_info.value.reason_code == "NUMBER_REQUIRED"
    assert exc_info.value.field == "event.telemetry.intensity_ratio"


@pytest.mark.parametrize(
    ("document", "field"),
    [
        ("EVENT", "event.telemetry.intensity_ratio"),
        ("POLICY", "policy.thresholds.max_intensity_ratio"),
    ],
)
def test_huge_integer_numeric_inputs_fail_closed(document, field) -> None:
    event = _event()
    policy = _policy()
    if document == "EVENT":
        event["telemetry"]["intensity_ratio"] = 10**10000
    else:
        policy["thresholds"]["max_intensity_ratio"] = 10**10000

    with pytest.raises(EgressGuardError) as exc_info:
        evaluate_egress_event(event, policy)

    assert exc_info.value.reason_code == "NUMBER_OUT_OF_RANGE"
    assert exc_info.value.document == document
    assert exc_info.value.field == field
    error_result = build_fail_closed_error(exc_info.value)
    assert error_result["decision"] == DECISION_BLOCK
    assert error_result["recommended_action"] == "CLOSE_AND_HOLD"
