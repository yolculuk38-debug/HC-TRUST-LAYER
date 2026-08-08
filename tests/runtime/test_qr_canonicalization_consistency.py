"""Shared QR JCS hashing and strict-boundary regressions."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from hc_runtime.qr_payload_parser import (
    MALFORMED_PAYLOAD,
    VALID_PAYLOAD,
    _compute_advisory_payload_hash,
    parse_qr_payload,
)
from hc_runtime.qr_record_bridge import check_qr_payload_record_bridge
from hc_runtime.qr_public_validator import run_qr_public_validator
from hc_runtime.qr_spoof_protection import QRRiskLevel, inspect_qr_spoof_protection
from hc_trust.canonicalization import canonicalize_json
from hc_trust.hashing import (
    HC_CONTENT_HASH_PROFILE,
    calculate_content_hash,
    calculate_qr_payload_hash,
)


def _shared_payload(record_id: str = "HC-JCS-2026-0001") -> dict[str, object]:
    content = {"z": ["\u00e9", {"b": 2, "a": 1.0}], "a": False}
    payload: dict[str, object] = {
        "qr_version": "v1",
        "record_id": record_id,
        "canonical_url": f"https://github.com/yolculuk38-debug/HC-TRUST-LAYER/records/{record_id}.json",
        "payload_hash": "pending",
        "content_hash": calculate_content_hash(content, HC_CONTENT_HASH_PROFILE),
        "issued_at": "2026-08-08T08:00:00Z",
        "issuer_id": "hc-test",
        "algorithm": "sha-256",
        "key_id": "test-key",
        "verification_url": f"https://github.com/yolculuk38-debug/HC-TRUST-LAYER/verify/{record_id}",
        "signed_payload_ref": f"signed-payloads/{record_id}.json",
        "content_hash_profile": HC_CONTENT_HASH_PROFILE,
        "content": content,
    }
    payload["payload_hash"] = calculate_qr_payload_hash(payload)
    return payload


def test_parser_and_spoof_inspection_share_jcs_payload_hashing() -> None:
    payload = _shared_payload()
    encoded = canonicalize_json(payload).decode("utf-8")

    assert _compute_advisory_payload_hash(payload) == calculate_qr_payload_hash(payload)
    assert parse_qr_payload(encoded)["status"] == VALID_PAYLOAD

    spoof = inspect_qr_spoof_protection(record_id=str(payload["record_id"]), qr_input=encoded)
    assert spoof.structured_payload is True
    assert "payload_hash_mismatch" not in spoof.risk_reasons
    assert "content_hash_mismatch" not in spoof.risk_reasons


def test_parser_and_spoof_normalize_declared_hash_case_and_whitespace_identically() -> None:
    payload = _shared_payload()
    payload["content_hash"] = f"  {str(payload['content_hash']).upper()}  "
    payload["payload_hash"] = calculate_qr_payload_hash(payload)
    payload["payload_hash"] = f"  {str(payload['payload_hash']).upper()}  "
    encoded = canonicalize_json(payload).decode("utf-8")

    parser_result = parse_qr_payload(encoded)
    spoof_result = inspect_qr_spoof_protection(
        record_id=str(payload["record_id"]),
        qr_input=encoded,
    )

    assert parser_result["status"] == VALID_PAYLOAD
    assert "payload_hash_mismatch" not in spoof_result.risk_reasons
    assert "content_hash_mismatch" not in spoof_result.risk_reasons


def test_bridge_dict_and_json_string_inputs_are_identical(tmp_path: Path) -> None:
    payload = _shared_payload()
    record_id = str(payload["record_id"])
    record = {
        "record_id": record_id,
        "content": payload["content"],
        "content_hash": payload["content_hash"],
        "content_hash_profile": HC_CONTENT_HASH_PROFILE,
    }
    path = tmp_path / "records" / "pending" / f"{record_id}.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")

    from_dict = check_qr_payload_record_bridge(payload, repo_root=tmp_path)
    from_text = check_qr_payload_record_bridge(canonicalize_json(payload).decode("utf-8"), repo_root=tmp_path)

    assert from_dict == from_text
    assert from_dict["bridge_status"] == "bridge_match"
    assert from_dict["content_hash_match"] is True


def test_bridge_does_not_match_an_unverifiable_canonical_record(tmp_path: Path) -> None:
    payload = _shared_payload()
    record_id = str(payload["record_id"])
    record = {
        "record_id": record_id,
        "content": payload["content"],
        "content_hash": payload["content_hash"],
    }
    path = tmp_path / "records" / "pending" / f"{record_id}.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")

    result = check_qr_payload_record_bridge(payload, repo_root=tmp_path)
    combined = run_qr_public_validator(payload, repo_root=tmp_path)

    assert result["record_lookup_status"] == "found"
    assert result["bridge_status"] == "bridge_not_checked"
    assert result["content_hash_match"] is None
    assert any(
        "legacy_structured_content_algorithm_ambiguous" in error
        for error in result["errors"]
    )
    assert combined["status"] == "validation_not_checked"


@pytest.mark.parametrize("field", ["record_id", "payload_hash", "content_hash"])
def test_duplicate_security_properties_are_rejected(field: str) -> None:
    payload = _shared_payload()
    encoded = canonicalize_json(payload).decode("utf-8")
    needle = f'"{field}":'
    duplicate_value = '"attacker",' if field == "record_id" else '"0",'
    duplicate = encoded.replace("{", "{" + needle + duplicate_value, 1)

    parser_result = parse_qr_payload(duplicate)
    bridge_result = check_qr_payload_record_bridge(duplicate)
    spoof_result = inspect_qr_spoof_protection(record_id=str(payload["record_id"]), qr_input=duplicate)

    assert parser_result["status"] == MALFORMED_PAYLOAD
    assert bridge_result["bridge_status"] == "malformed_payload"
    assert spoof_result.structured_payload is True
    assert spoof_result.risk_level is QRRiskLevel.HIGH
    assert "structured_payload_invalid" in spoof_result.risk_reasons


@pytest.mark.parametrize("unsafe", ["NaN", "Infinity", "1e400", "9007199254740992"])
def test_unsafe_json_number_never_falls_back_to_clean_unstructured_result(unsafe: str) -> None:
    payload = _shared_payload()
    encoded = canonicalize_json(payload).decode("utf-8")
    unsafe_payload = encoded[:-1] + f',"unsafe":{unsafe}' + "}"

    parser_result = parse_qr_payload(unsafe_payload)
    spoof_result = inspect_qr_spoof_protection(record_id=str(payload["record_id"]), qr_input=unsafe_payload)

    assert parser_result["status"] == MALFORMED_PAYLOAD
    assert spoof_result.structured_payload is True
    assert spoof_result.risk_level is QRRiskLevel.HIGH
    assert "structured_payload_invalid" in spoof_result.risk_reasons


def test_structured_content_without_profile_is_unverifiable_not_mismatched() -> None:
    payload = _shared_payload()
    payload.pop("content_hash_profile")
    payload["payload_hash"] = calculate_qr_payload_hash(payload)

    result = inspect_qr_spoof_protection(
        record_id=str(payload["record_id"]),
        qr_input=canonicalize_json(payload).decode("utf-8"),
    )

    assert "content_hash_unverifiable" in result.risk_reasons
    assert "content_hash_mismatch" not in result.risk_reasons


def test_string_content_with_explicit_null_profile_is_unverifiable() -> None:
    payload = _shared_payload()
    content = "legacy-compatible text"
    payload["content"] = content
    payload["content_hash"] = calculate_content_hash(content)
    payload["content_hash_profile"] = None
    payload["payload_hash"] = calculate_qr_payload_hash(payload)

    result = inspect_qr_spoof_protection(
        record_id=str(payload["record_id"]),
        qr_input=canonicalize_json(payload).decode("utf-8"),
    )

    assert result.risk_level is QRRiskLevel.HIGH
    assert "content_hash_unverifiable" in result.risk_reasons
    assert "content_hash_mismatch" not in result.risk_reasons


@pytest.mark.parametrize("profile_case", ["missing", "null", "unknown"])
def test_structured_content_profile_is_checked_even_when_content_hash_is_missing(
    profile_case: str,
) -> None:
    payload = _shared_payload()
    payload.pop("content_hash")
    if profile_case == "missing":
        payload.pop("content_hash_profile")
    elif profile_case == "null":
        payload["content_hash_profile"] = None
    else:
        payload["content_hash_profile"] = "unknown-profile"
    payload["payload_hash"] = calculate_qr_payload_hash(payload)

    result = inspect_qr_spoof_protection(
        record_id=str(payload["record_id"]),
        qr_input=canonicalize_json(payload).decode("utf-8"),
    )

    assert result.risk_level is QRRiskLevel.HIGH
    assert "content_hash_unverifiable" in result.risk_reasons
    assert "content_hash_missing" in result.risk_reasons


def test_optional_actual_content_mismatch_blocks_parser_bridge_and_combined_success(
    tmp_path: Path,
) -> None:
    payload = _shared_payload()
    record_id = str(payload["record_id"])
    canonical_content = payload["content"]
    payload["content"] = {"attacker": "different content"}
    payload["payload_hash"] = calculate_qr_payload_hash(payload)
    encoded = canonicalize_json(payload).decode("utf-8")

    record = {
        "record_id": record_id,
        "content": canonical_content,
        "content_hash": payload["content_hash"],
        "content_hash_profile": HC_CONTENT_HASH_PROFILE,
    }
    path = tmp_path / "records" / "pending" / f"{record_id}.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")

    parser_result = parse_qr_payload(encoded)
    bridge_result = check_qr_payload_record_bridge(encoded, repo_root=tmp_path)
    combined_result = run_qr_public_validator(encoded, repo_root=tmp_path)

    assert parser_result["status"] != VALID_PAYLOAD
    assert any("content_hash" in error for error in parser_result["errors"])
    assert bridge_result["bridge_status"] == "invalid_payload"
    assert bridge_result["content_hash_match"] is None
    assert combined_result["status"] == "invalid_payload"


@pytest.mark.parametrize("profile_case", ["missing", "null", "unknown"])
def test_structured_actual_content_requires_v2_profile_across_parser_and_bridge(
    profile_case: str,
) -> None:
    payload = _shared_payload()
    if profile_case == "missing":
        payload.pop("content_hash_profile")
    elif profile_case == "null":
        payload["content_hash_profile"] = None
    else:
        payload["content_hash_profile"] = "unknown-profile"
    payload["payload_hash"] = calculate_qr_payload_hash(payload)
    encoded = canonicalize_json(payload).decode("utf-8")

    parser_result = parse_qr_payload(encoded)
    bridge_result = check_qr_payload_record_bridge(encoded)

    assert parser_result["status"] != VALID_PAYLOAD
    assert any("content hash" in error.lower() for error in parser_result["errors"])
    assert bridge_result["bridge_status"] == "invalid_payload"
    assert bridge_result["content_hash_match"] is None


def test_string_actual_content_without_profile_keeps_legacy_compatibility() -> None:
    payload = _shared_payload()
    content = "legacy-compatible text"
    payload["content"] = content
    payload["content_hash"] = calculate_content_hash(content)
    payload.pop("content_hash_profile")
    payload["payload_hash"] = calculate_qr_payload_hash(payload)

    result = parse_qr_payload(canonicalize_json(payload).decode("utf-8"))

    assert result["status"] == VALID_PAYLOAD


def test_string_actual_content_with_explicit_v2_is_valid() -> None:
    payload = _shared_payload()
    content = "explicit v2 text"
    payload["content"] = content
    payload["content_hash"] = calculate_content_hash(content, HC_CONTENT_HASH_PROFILE)
    payload["content_hash_profile"] = HC_CONTENT_HASH_PROFILE
    payload["payload_hash"] = calculate_qr_payload_hash(payload)

    result = parse_qr_payload(canonicalize_json(payload).decode("utf-8"))

    assert result["status"] == VALID_PAYLOAD


def test_profile_without_actual_content_remains_an_unconsumed_unknown_field() -> None:
    payload = _shared_payload()
    payload.pop("content")
    payload["payload_hash"] = calculate_qr_payload_hash(payload)

    result = parse_qr_payload(canonicalize_json(payload).decode("utf-8"))

    assert result["status"] == VALID_PAYLOAD
    assert any(
        "content_hash_profile" in warning and "ignored" in warning
        for warning in result["warnings"]
    )


@pytest.mark.parametrize("encoded", ["[NaN]", "NaN", "9007199254740992"])
def test_unsafe_top_level_or_array_json_is_not_treated_as_clean_unstructured_input(
    encoded: str,
) -> None:
    result = inspect_qr_spoof_protection(record_id="unsafe-json", qr_input=encoded)

    assert result.structured_payload is True
    assert result.risk_level is QRRiskLevel.HIGH
    assert "structured_payload_invalid" in result.risk_reasons
    assert result.warnings


def test_bom_prefixed_json_is_visible_as_a_failed_structured_attempt() -> None:
    result = inspect_qr_spoof_protection(
        record_id="bom-json",
        qr_input='\ufeff{"record_id":"bom-json"}',
    )

    assert result.structured_payload is True
    assert result.warnings


def test_malformed_url_is_public_safe_across_parser_and_spoof_inspection() -> None:
    payload = _shared_payload()
    payload["canonical_url"] = "https://["
    payload["verification_url"] = "https://["
    payload["payload_hash"] = calculate_qr_payload_hash(payload)
    encoded = canonicalize_json(payload).decode("utf-8")

    parser_result = parse_qr_payload(encoded)
    spoof_result = inspect_qr_spoof_protection(
        record_id=str(payload["record_id"]),
        qr_input=encoded,
    )

    assert parser_result["status"] != VALID_PAYLOAD
    assert any("absolute https url" in error.lower() for error in parser_result["errors"])
    assert spoof_result.risk_level is QRRiskLevel.HIGH
    assert "verification_url_invalid" in spoof_result.risk_reasons
    assert spoof_result.warnings


def test_excessively_nested_qr_json_fails_closed_without_recursion_error() -> None:
    encoded = '{"unsafe":' + "[" * 2_000 + "null" + "]" * 2_000 + "}"

    parser_result = parse_qr_payload(encoded)
    spoof_result = inspect_qr_spoof_protection(record_id="deep-json", qr_input=encoded)

    assert parser_result["status"] == MALFORMED_PAYLOAD
    assert any("json_nesting_too_deep" in error for error in parser_result["errors"])
    assert spoof_result.structured_payload is True
    assert spoof_result.risk_level is QRRiskLevel.HIGH
    assert "structured_payload_invalid" in spoof_result.risk_reasons
    assert any("json_nesting_too_deep" in warning for warning in spoof_result.warnings)
