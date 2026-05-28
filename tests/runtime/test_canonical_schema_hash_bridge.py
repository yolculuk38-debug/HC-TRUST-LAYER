"""Canonical schema/hash bridge coverage for HC:// advisory runtime behavior."""

from __future__ import annotations

import hashlib
from copy import deepcopy
from typing import Any

from hc_runtime.contracts.responses import advisory_response
from hc_runtime.decision_engine import TrustStateDecisionEngine
from hc_runtime.runtime import RuntimePolicyEngine, ValidatorPipeline

EXPECTED_BRIDGE_KEYS = [
    "checked",
    "placeholder",
    "lookup_performed",
    "found",
    "record_id_match",
    "malformed",
    "schema_valid",
    "content_hash_present",
    "hash_verified",
    "lookup_status",
    "warnings",
]

EXPECTED_SCHEMA_KEYS = [
    "checked",
    "placeholder",
    "valid",
    "canonical_lookup_status",
    "warnings",
]

EXPECTED_HASH_KEYS = [
    "checked",
    "placeholder",
    "hash_verified",
    "canonical_lookup_status",
    "warnings",
]

EXPECTED_PIPELINE_KEYS = [
    "record_id",
    "canonical_bridge",
    "schema_result",
    "hash_result",
    "trust_assignment",
    "escalation",
]

EXPECTED_RUNTIME_RESPONSE_KEYS = [
    "status",
    "advisory_only",
    "public_safe",
    "message",
    "warnings",
    "traceable",
    "truth_guarantee",
    "record_id",
    "trust_state",
    "canonical_lookup_status",
    "schema_valid",
    "hash_verified",
]


def _sha256(content: object) -> str:
    if isinstance(content, str):
        payload = content
    else:
        import json

        payload = json.dumps(content, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _record(record_id: str, content: object = "canonical content") -> dict[str, object]:
    return {"record_id": record_id, "content": content, "content_hash": _sha256(content)}


def _run_pipeline(record_id: str, records: dict[str, object]) -> dict[str, Any]:
    return ValidatorPipeline(canonical_records=records).run(
        record_id=record_id,
        qr_input=f"hc://{record_id} hash:advisory",
    )


def _runtime_response(record_id: str, records: dict[str, object]) -> dict[str, object]:
    pipeline_result = _run_pipeline(record_id, records)
    decision_engine = TrustStateDecisionEngine()
    policy_engine = RuntimePolicyEngine()
    trust_state, warnings = decision_engine.classify(
        record_id=record_id,
        qr_input=f"hc://{record_id} hash:advisory",
        schema_valid=pipeline_result["schema_result"]["valid"],
        hash_verified=pipeline_result["hash_result"]["hash_verified"],
        continuity_ok=True,
        replay_warning=False,
    )
    policy = policy_engine.evaluate(trust_state=trust_state, replay_warning=False, degraded_mode=False)
    payload = advisory_response(
        record_id=record_id,
        message="Advisory HC:// runtime bridge response for canonical schema/hash checks.",
        warnings=[*pipeline_result["trust_assignment"]["warnings"], *warnings, *policy["warnings"]],
    )
    payload["trust_state"] = trust_state.value
    payload["canonical_lookup_status"] = pipeline_result["canonical_bridge"]["lookup_status"]
    payload["schema_valid"] = pipeline_result["schema_result"]["valid"]
    payload["hash_verified"] = pipeline_result["hash_result"]["hash_verified"]
    return payload


def _assert_stable_bridge_contract(result: dict[str, Any], *, record_id: str) -> None:
    assert list(result.keys()) == EXPECTED_PIPELINE_KEYS
    assert result["record_id"] == record_id
    assert list(result["canonical_bridge"].keys()) == EXPECTED_BRIDGE_KEYS
    assert list(result["schema_result"].keys()) == EXPECTED_SCHEMA_KEYS
    assert list(result["hash_result"].keys()) == EXPECTED_HASH_KEYS
    assert isinstance(result["canonical_bridge"]["warnings"], list)
    assert isinstance(result["schema_result"]["warnings"], list)
    assert isinstance(result["hash_result"]["warnings"], list)
    assert isinstance(result["trust_assignment"]["warnings"], list)
    assert result["canonical_bridge"]["checked"] is True
    assert result["canonical_bridge"]["placeholder"] is True
    assert result["canonical_bridge"]["lookup_performed"] is True


def _assert_advisory_runtime_contract(payload: dict[str, object], *, record_id: str) -> None:
    assert list(payload.keys()) == EXPECTED_RUNTIME_RESPONSE_KEYS
    assert payload["record_id"] == record_id
    assert payload["status"] == "ADVISORY"
    assert payload["advisory_only"] is True
    assert payload["public_safe"] is True
    assert payload["truth_guarantee"] is False
    assert isinstance(payload["warnings"], list)
    assert "canonical_record" not in payload


def test_canonical_record_found_bridges_schema_and_sha256_success_without_mutation() -> None:
    record_id = "bridge-found-record"
    records = {record_id: _record(record_id, content={"claim": "HC:// advisory bridge"})}
    before = deepcopy(records)

    result = _run_pipeline(record_id, records)
    payload = _runtime_response(record_id, records)

    _assert_stable_bridge_contract(result, record_id=record_id)
    _assert_advisory_runtime_contract(payload, record_id=record_id)
    assert result["canonical_bridge"]["lookup_status"] == "verified"
    assert result["schema_result"]["valid"] is True
    assert result["hash_result"]["hash_verified"] is True
    assert result["canonical_bridge"]["warnings"] == []
    assert payload["canonical_lookup_status"] == "verified"
    assert payload["warnings"] == []
    assert records == before


def test_canonical_record_missing_keeps_lookup_failure_visible_and_advisory_only() -> None:
    record_id = "bridge-missing-record"

    result = _run_pipeline(record_id, {})
    payload = _runtime_response(record_id, {})

    _assert_stable_bridge_contract(result, record_id=record_id)
    _assert_advisory_runtime_contract(payload, record_id=record_id)
    assert result["canonical_bridge"]["lookup_status"] == "missing"
    assert result["canonical_bridge"]["found"] is False
    assert result["schema_result"]["valid"] is False
    assert result["hash_result"]["hash_verified"] is False
    assert any("lookup returned no record" in warning.lower() for warning in payload["warnings"])


def test_malformed_canonical_record_remains_visible_without_hidden_fallback() -> None:
    record_id = "bridge-malformed-record"

    result = _run_pipeline(record_id, {record_id: ["not", "a", "record"]})
    payload = _runtime_response(record_id, {record_id: ["not", "a", "record"]})

    _assert_stable_bridge_contract(result, record_id=record_id)
    _assert_advisory_runtime_contract(payload, record_id=record_id)
    assert result["canonical_bridge"]["lookup_status"] == "malformed"
    assert result["canonical_bridge"]["malformed"] is True
    assert result["schema_result"]["valid"] is False
    assert any("malformed" in warning.lower() for warning in payload["warnings"])


def test_schema_invalid_canonical_record_fails_advisory_schema_bridge() -> None:
    record_id = "bridge-schema-invalid-record"
    content = "schema invalid canonical content"
    records = {record_id: {"record_id": "different-record", "content": content, "content_hash": _sha256(content)}}

    result = _run_pipeline(record_id, records)
    payload = _runtime_response(record_id, records)

    _assert_stable_bridge_contract(result, record_id=record_id)
    _assert_advisory_runtime_contract(payload, record_id=record_id)
    assert result["canonical_bridge"]["lookup_status"] == "schema_invalid"
    assert result["canonical_bridge"]["record_id_match"] is False
    assert result["schema_result"]["valid"] is False
    assert result["hash_result"]["hash_verified"] is True
    assert any("schema validation failed" in warning.lower() for warning in payload["warnings"])


def test_content_hash_missing_warns_and_leaves_sha256_unresolved() -> None:
    record_id = "bridge-hash-missing-record"
    records = {record_id: {"record_id": record_id, "content": "missing hash"}}

    result = _run_pipeline(record_id, records)
    payload = _runtime_response(record_id, records)

    _assert_stable_bridge_contract(result, record_id=record_id)
    _assert_advisory_runtime_contract(payload, record_id=record_id)
    assert result["canonical_bridge"]["lookup_status"] == "hash_missing"
    assert result["canonical_bridge"]["content_hash_present"] is False
    assert result["hash_result"]["hash_verified"] is False
    assert any("content_hash is missing" in warning.lower() for warning in payload["warnings"])


def test_content_hash_mismatch_emits_explicit_sha256_warning() -> None:
    record_id = "bridge-hash-mismatch-record"
    records = {record_id: {"record_id": record_id, "content": "hash mismatch", "content_hash": _sha256("other")}}

    result = _run_pipeline(record_id, records)
    payload = _runtime_response(record_id, records)

    _assert_stable_bridge_contract(result, record_id=record_id)
    _assert_advisory_runtime_contract(payload, record_id=record_id)
    assert result["canonical_bridge"]["lookup_status"] == "hash_mismatch"
    assert result["canonical_bridge"]["schema_valid"] is True
    assert result["hash_result"]["hash_verified"] is False
    assert any("content_hash mismatch" in warning.lower() for warning in payload["warnings"])


def test_sha256_verification_success_and_failure_are_deterministic() -> None:
    success_id = "bridge-sha-success-record"
    failure_id = "bridge-sha-failure-record"

    success_a = _run_pipeline(success_id, {success_id: _record(success_id, "stable")})
    success_b = _run_pipeline(success_id, {success_id: _record(success_id, "stable")})
    failure_a = _run_pipeline(
        failure_id,
        {failure_id: {"record_id": failure_id, "content": "stable", "content_hash": _sha256("changed")}},
    )
    failure_b = _run_pipeline(
        failure_id,
        {failure_id: {"record_id": failure_id, "content": "stable", "content_hash": _sha256("changed")}},
    )

    assert success_a == success_b
    assert failure_a == failure_b
    assert success_a["hash_result"]["hash_verified"] is True
    assert failure_a["hash_result"]["hash_verified"] is False


def test_runtime_output_keys_stay_stable_across_success_missing_invalid_and_mismatch_states() -> None:
    cases = {
        "success": {"stable-success": _record("stable-success")},
        "missing": {},
        "invalid": {"stable-invalid": {"record_id": "other", "content": "invalid", "content_hash": _sha256("invalid")}},
        "mismatch": {"stable-mismatch": {"record_id": "stable-mismatch", "content": "a", "content_hash": _sha256("b")}},
    }
    ids = {
        "success": "stable-success",
        "missing": "stable-missing",
        "invalid": "stable-invalid",
        "mismatch": "stable-mismatch",
    }

    for state, records in cases.items():
        payload = _runtime_response(ids[state], records)
        _assert_advisory_runtime_contract(payload, record_id=ids[state])
        assert payload["advisory_only"] is True
        assert payload["public_safe"] is True
        assert payload["truth_guarantee"] is False
