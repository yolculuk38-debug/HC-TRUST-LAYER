"""Deterministic, fail-closed evidence evaluation for one optical egress channel.

This module evaluates caller-supplied telemetry. It does not authenticate sensor
hardware, actuate a shutter, or make a quantum-security claim. Those boundaries
are repeated in every successful result so an evidence packet remains honest
when it is viewed outside the CLI that produced it.
"""

from __future__ import annotations

import hashlib
import math
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from .canonicalization import (
    CanonicalizationError,
    canonicalize_json,
    strict_json_loads,
)

EVENT_SCHEMA_VERSION = "hc-egress-sensor-event-v1"
POLICY_SCHEMA_VERSION = "hc-egress-policy-v1"
DECISION_SCHEMA_VERSION = "hc-egress-decision-v1"
ERROR_SCHEMA_VERSION = "hc-egress-error-v1"
ENGINE_VERSION = "0.1.0"
MAX_JSON_BYTES = 64 * 1024

HASH_ALGORITHM = "sha-256"
EVENT_HASH_PROFILE = "hc-egress-event-jcs-sha256-v1"
POLICY_HASH_PROFILE = "hc-egress-policy-jcs-sha256-v1"
DECISION_HASH_PROFILE = "hc-egress-decision-jcs-sha256-v1"

DECISION_ALLOW = "ALLOW"
DECISION_BLOCK = "BLOCK"
ACTION_ALLOW = "ALLOW_CHANNEL"
ACTION_BLOCK = "CLOSE_AND_HOLD"

_IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
_TIMESTAMP_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?(?:Z|[+-]\d{2}:\d{2})$"
)

_EVENT_FIELDS = {
    "schema_version",
    "event_id",
    "session_id",
    "captured_at",
    "channel_id",
    "channel_type",
    "telemetry",
}
_TELEMETRY_FIELDS = {
    "sensor_health",
    "calibration_status",
    "controller_is_independent",
    "intensity_ratio",
    "polarization_deviation_deg",
    "out_of_band_fraction",
    "detector_saturated",
    "power_state",
    "shutter_state",
}
_POLICY_FIELDS = {
    "schema_version",
    "policy_id",
    "channel_type",
    "enforcement_mode",
    "thresholds",
}
_THRESHOLD_FIELDS = {
    "min_intensity_ratio",
    "max_intensity_ratio",
    "max_polarization_deviation_deg",
    "max_out_of_band_fraction",
}


class EgressGuardError(ValueError):
    """Public-safe validation failure at the Egress Guard boundary."""

    def __init__(
        self,
        reason_code: str,
        *,
        document: str,
        field: str | None = None,
    ) -> None:
        self.reason_code = reason_code
        self.document = document
        self.field = field
        super().__init__(reason_code)


def _raise(
    reason_code: str,
    *,
    document: str,
    field: str | None = None,
) -> None:
    raise EgressGuardError(reason_code, document=document, field=field)


def _require_exact_fields(
    value: Any,
    expected: set[str],
    *,
    document: str,
    field: str,
) -> dict[str, Any]:
    if type(value) is not dict:
        _raise("OBJECT_REQUIRED", document=document, field=field)

    missing = sorted(expected.difference(value))
    if missing:
        _raise(
            "REQUIRED_FIELD_MISSING",
            document=document,
            field=f"{field}.{missing[0]}",
        )

    if set(value).difference(expected):
        _raise("UNKNOWN_FIELD", document=document, field=field)
    return value


def _require_literal(
    value: Any,
    expected: str,
    *,
    document: str,
    field: str,
) -> str:
    if type(value) is not str:
        _raise("STRING_REQUIRED", document=document, field=field)
    if value != expected:
        _raise("UNSUPPORTED_FIELD_VALUE", document=document, field=field)
    return value


def _require_enum(
    value: Any,
    allowed: set[str],
    *,
    document: str,
    field: str,
) -> str:
    if type(value) is not str:
        _raise("STRING_REQUIRED", document=document, field=field)
    if value not in allowed:
        _raise("UNSUPPORTED_FIELD_VALUE", document=document, field=field)
    return value


def _require_identifier(value: Any, *, document: str, field: str) -> str:
    if type(value) is not str:
        _raise("STRING_REQUIRED", document=document, field=field)
    if _IDENTIFIER_RE.fullmatch(value) is None:
        _raise("INVALID_IDENTIFIER", document=document, field=field)
    return value


def _require_timestamp(value: Any, *, document: str, field: str) -> str:
    if type(value) is not str:
        _raise("STRING_REQUIRED", document=document, field=field)
    if _TIMESTAMP_RE.fullmatch(value) is None:
        _raise("INVALID_TIMESTAMP", document=document, field=field)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        _raise("INVALID_TIMESTAMP", document=document, field=field)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        _raise("TIMESTAMP_OFFSET_REQUIRED", document=document, field=field)
    return value


def _require_boolean(value: Any, *, document: str, field: str) -> bool:
    if type(value) is not bool:
        _raise("BOOLEAN_REQUIRED", document=document, field=field)
    return value


def _require_number(
    value: Any,
    *,
    minimum: float,
    maximum: float,
    document: str,
    field: str,
) -> int | float:
    if type(value) not in (int, float):
        _raise("NUMBER_REQUIRED", document=document, field=field)
    if not math.isfinite(value):
        _raise("FINITE_NUMBER_REQUIRED", document=document, field=field)
    if not minimum <= value <= maximum:
        _raise("NUMBER_OUT_OF_RANGE", document=document, field=field)
    return value


def _validate_policy(policy: Any) -> dict[str, Any]:
    document = "POLICY"
    policy_object = _require_exact_fields(
        policy,
        _POLICY_FIELDS,
        document=document,
        field="policy",
    )
    _require_literal(
        policy_object["schema_version"],
        POLICY_SCHEMA_VERSION,
        document=document,
        field="policy.schema_version",
    )
    _require_identifier(
        policy_object["policy_id"], document=document, field="policy.policy_id"
    )
    _require_literal(
        policy_object["channel_type"],
        "OPTICAL",
        document=document,
        field="policy.channel_type",
    )
    _require_literal(
        policy_object["enforcement_mode"],
        "EVIDENCE_ONLY",
        document=document,
        field="policy.enforcement_mode",
    )

    thresholds = _require_exact_fields(
        policy_object["thresholds"],
        _THRESHOLD_FIELDS,
        document=document,
        field="policy.thresholds",
    )
    minimum_intensity = _require_number(
        thresholds["min_intensity_ratio"],
        minimum=0.0,
        maximum=10.0,
        document=document,
        field="policy.thresholds.min_intensity_ratio",
    )
    maximum_intensity = _require_number(
        thresholds["max_intensity_ratio"],
        minimum=0.0,
        maximum=10.0,
        document=document,
        field="policy.thresholds.max_intensity_ratio",
    )
    if minimum_intensity > maximum_intensity:
        _raise(
            "INVALID_THRESHOLD_ORDER",
            document=document,
            field="policy.thresholds",
        )
    _require_number(
        thresholds["max_polarization_deviation_deg"],
        minimum=0.0,
        maximum=90.0,
        document=document,
        field="policy.thresholds.max_polarization_deviation_deg",
    )
    _require_number(
        thresholds["max_out_of_band_fraction"],
        minimum=0.0,
        maximum=1.0,
        document=document,
        field="policy.thresholds.max_out_of_band_fraction",
    )
    return policy_object


def _validate_event(event: Any) -> dict[str, Any]:
    document = "EVENT"
    event_object = _require_exact_fields(
        event,
        _EVENT_FIELDS,
        document=document,
        field="event",
    )
    _require_literal(
        event_object["schema_version"],
        EVENT_SCHEMA_VERSION,
        document=document,
        field="event.schema_version",
    )
    for field in ("event_id", "session_id", "channel_id"):
        _require_identifier(
            event_object[field], document=document, field=f"event.{field}"
        )
    _require_timestamp(
        event_object["captured_at"],
        document=document,
        field="event.captured_at",
    )
    _require_literal(
        event_object["channel_type"],
        "OPTICAL",
        document=document,
        field="event.channel_type",
    )

    telemetry = _require_exact_fields(
        event_object["telemetry"],
        _TELEMETRY_FIELDS,
        document=document,
        field="event.telemetry",
    )
    _require_enum(
        telemetry["sensor_health"],
        {"OK", "DEGRADED", "FAILED"},
        document=document,
        field="event.telemetry.sensor_health",
    )
    _require_enum(
        telemetry["calibration_status"],
        {"VALID", "EXPIRED", "UNKNOWN"},
        document=document,
        field="event.telemetry.calibration_status",
    )
    _require_boolean(
        telemetry["controller_is_independent"],
        document=document,
        field="event.telemetry.controller_is_independent",
    )
    _require_number(
        telemetry["intensity_ratio"],
        minimum=0.0,
        maximum=10.0,
        document=document,
        field="event.telemetry.intensity_ratio",
    )
    _require_number(
        telemetry["polarization_deviation_deg"],
        minimum=0.0,
        maximum=90.0,
        document=document,
        field="event.telemetry.polarization_deviation_deg",
    )
    _require_number(
        telemetry["out_of_band_fraction"],
        minimum=0.0,
        maximum=1.0,
        document=document,
        field="event.telemetry.out_of_band_fraction",
    )
    _require_boolean(
        telemetry["detector_saturated"],
        document=document,
        field="event.telemetry.detector_saturated",
    )
    _require_enum(
        telemetry["power_state"],
        {"ON", "LOSS", "UNKNOWN"},
        document=document,
        field="event.telemetry.power_state",
    )
    _require_enum(
        telemetry["shutter_state"],
        {"OPEN", "CLOSED", "UNKNOWN"},
        document=document,
        field="event.telemetry.shutter_state",
    )
    return event_object


def _digest(value: dict[str, Any], profile: str, *, document: str) -> dict[str, str]:
    try:
        canonical_bytes = canonicalize_json(value)
    except CanonicalizationError as exc:
        raise EgressGuardError(
            "CANONICALIZATION_FAILED", document=document
        ) from exc
    return {
        "algorithm": HASH_ALGORITHM,
        "profile": profile,
        "value": hashlib.sha256(canonical_bytes).hexdigest(),
    }


def _reason_codes(
    event: dict[str, Any], policy: dict[str, Any]
) -> list[str]:
    telemetry = event["telemetry"]
    thresholds = policy["thresholds"]
    reasons: list[str] = []

    if event["channel_type"] != policy["channel_type"]:
        reasons.append("CHANNEL_TYPE_MISMATCH")
    if telemetry["sensor_health"] != "OK":
        reasons.append("SENSOR_HEALTH_NOT_OK")
    if telemetry["calibration_status"] != "VALID":
        reasons.append("CALIBRATION_NOT_VALID")
    if telemetry["controller_is_independent"] is not True:
        reasons.append("CONTROLLER_NOT_INDEPENDENT")
    if telemetry["detector_saturated"] is True:
        reasons.append("DETECTOR_SATURATED")
    if telemetry["power_state"] != "ON":
        reasons.append("POWER_NOT_ON")
        if telemetry["shutter_state"] != "CLOSED":
            reasons.append("FAIL_SAFE_SHUTTER_NOT_CLOSED")
    elif telemetry["shutter_state"] != "OPEN":
        reasons.append("SHUTTER_NOT_OPEN")
    if telemetry["intensity_ratio"] < thresholds["min_intensity_ratio"]:
        reasons.append("INTENSITY_BELOW_POLICY")
    if telemetry["intensity_ratio"] > thresholds["max_intensity_ratio"]:
        reasons.append("INTENSITY_ABOVE_POLICY")
    if (
        telemetry["polarization_deviation_deg"]
        > thresholds["max_polarization_deviation_deg"]
    ):
        reasons.append("POLARIZATION_DEVIATION_ABOVE_POLICY")
    if (
        telemetry["out_of_band_fraction"]
        > thresholds["max_out_of_band_fraction"]
    ):
        reasons.append("OUT_OF_BAND_FRACTION_ABOVE_POLICY")
    return reasons


def _assurance_boundary() -> dict[str, str]:
    return {
        "policy_authentication": "NOT_VERIFIED",
        "telemetry_authentication": "NOT_VERIFIED",
        "decision_authentication": "NOT_SIGNED",
        "hardware_enforcement": "NOT_CONNECTED",
        "replay_protection": "NOT_IMPLEMENTED",
        "quantum_security": "NOT_CLAIMED",
    }


def evaluate_egress_event(
    event: dict[str, Any], policy: dict[str, Any]
) -> dict[str, Any]:
    """Return a deterministic advisory decision for one supplied event."""

    validated_policy = _validate_policy(policy)
    validated_event = _validate_event(event)
    reasons = _reason_codes(validated_event, validated_policy)
    decision = DECISION_BLOCK if reasons else DECISION_ALLOW
    recommended_action = ACTION_BLOCK if reasons else ACTION_ALLOW

    result: dict[str, Any] = {
        "schema_version": DECISION_SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "event_id": validated_event["event_id"],
        "session_id": validated_event["session_id"],
        "channel_id": validated_event["channel_id"],
        "policy_id": validated_policy["policy_id"],
        "decision": decision,
        "recommended_action": recommended_action,
        "reason_codes": reasons or ["POLICY_CHECKS_PASSED"],
        "evidence": {
            "event_digest": _digest(
                validated_event, EVENT_HASH_PROFILE, document="EVENT"
            ),
            "policy_digest": _digest(
                validated_policy, POLICY_HASH_PROFILE, document="POLICY"
            ),
        },
        "assurance": _assurance_boundary(),
        "hardware_enforcement_performed": False,
        "human_review_required": True,
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
    }
    result["decision_digest"] = _digest(
        result, DECISION_HASH_PROFILE, document="DECISION"
    )
    return result


def load_egress_json(path: str | Path, *, document: str) -> dict[str, Any]:
    """Load one UTF-8 JSON document through HC's strict JSON boundary."""

    if document not in {"EVENT", "POLICY"}:
        raise ValueError("document must be EVENT or POLICY")
    try:
        with Path(path).open("rb") as file_object:
            raw_document = file_object.read(MAX_JSON_BYTES + 1)
    except OSError as exc:
        raise EgressGuardError("JSON_READ_FAILED", document=document) from exc
    if len(raw_document) > MAX_JSON_BYTES:
        raise EgressGuardError("JSON_TOO_LARGE", document=document)
    try:
        text = raw_document.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise EgressGuardError("JSON_INVALID_UTF8", document=document) from exc
    try:
        value = strict_json_loads(text)
    except CanonicalizationError as exc:
        raise EgressGuardError("JSON_INVALID", document=document) from exc
    if type(value) is not dict:
        raise EgressGuardError("OBJECT_REQUIRED", document=document)
    return value


def build_fail_closed_error(error: EgressGuardError) -> dict[str, Any]:
    """Return a public-safe BLOCK result when an input cannot be evaluated."""

    result: dict[str, Any] = {
        "schema_version": ERROR_SCHEMA_VERSION,
        "engine_version": ENGINE_VERSION,
        "status": "INVALID_INPUT",
        "decision": DECISION_BLOCK,
        "recommended_action": ACTION_BLOCK,
        "reason_codes": [error.reason_code],
        "error_document": error.document,
        "assurance": _assurance_boundary(),
        "hardware_enforcement_performed": False,
        "human_review_required": True,
        "advisory_only": True,
        "public_safe": True,
        "truth_guarantee": False,
    }
    if error.field is not None:
        result["error_field"] = error.field
    return result


__all__ = [
    "ACTION_ALLOW",
    "ACTION_BLOCK",
    "DECISION_ALLOW",
    "DECISION_BLOCK",
    "DECISION_SCHEMA_VERSION",
    "ENGINE_VERSION",
    "EVENT_SCHEMA_VERSION",
    "MAX_JSON_BYTES",
    "POLICY_SCHEMA_VERSION",
    "EgressGuardError",
    "build_fail_closed_error",
    "evaluate_egress_event",
    "load_egress_json",
]
