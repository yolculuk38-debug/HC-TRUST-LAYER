"""P0-3 acceptance coverage for the canonical HC:// record schema boundary."""

from __future__ import annotations

import json
import tomllib
from pathlib import Path

import pytest

from hc_runtime.runtime import ValidatorPipeline
from hc_trust.hashing import HC_CONTENT_HASH_PROFILE, calculate_content_hash
from hc_trust.verification import (
    _resolve_default_record_schema_path,
    validate_record,
    validate_record_payload,
)


ROOT = Path(__file__).resolve().parents[2]
CANONICAL_SCHEMA = ROOT / "schema" / "record-v1.schema.json"
LEGACY_SCHEMA = ROOT / "schema" / "record-v1.json"


def _record(
    record_id: str = "HC-SCHEMA-2026-0001",
    *,
    content: object = "P0-3 schema contract",
) -> dict[str, object]:
    return {
        "schema_version": "hc-record-v1",
        "record_id": record_id,
        "created_at": "2026-08-08T12:00:00Z",
        "title": "P0-3 schema contract",
        "record_type": "protocol_note",
        "witness_type": "human",
        "author": "HC-TRUST-LAYER tests",
        "content": content,
        "content_hash": calculate_content_hash(content, HC_CONTENT_HASH_PROFILE),
        "content_hash_profile": HC_CONTENT_HASH_PROFILE,
        "archive_ref": "pending_archive",
        "verification_status": "draft",
    }


def _validate_tmp_record(tmp_path: Path, record: dict[str, object]) -> tuple[bool, str]:
    path = tmp_path / "record.json"
    path.write_text(json.dumps(record), encoding="utf-8")
    return validate_record(path, CANONICAL_SCHEMA)


def test_only_one_executable_record_schema_remains() -> None:
    assert CANONICAL_SCHEMA.is_file()
    assert not LEGACY_SCHEMA.exists()


def test_wheel_packages_the_single_canonical_schema_source() -> None:
    configuration = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert configuration["tool"]["setuptools"]["data-files"] == {
        "share/hc-trust-layer/schema": ["schema/record-v1.schema.json"]
    }


@pytest.mark.parametrize(
    "module_relative_path",
    [
        Path("custom-target/hc_trust/verification.py"),
        Path("custom-prefix/lib/python3.14/site-packages/hc_trust/verification.py"),
    ],
)
def test_installed_schema_resolution_uses_the_actual_distribution_root(
    tmp_path: Path,
    module_relative_path: Path,
) -> None:
    module_path = tmp_path / module_relative_path
    module_path.parent.mkdir(parents=True)
    module_path.touch()
    install_root = tmp_path / module_relative_path.parts[0]
    installed_schema = (
        install_root
        / "share"
        / "hc-trust-layer"
        / "schema"
        / "record-v1.schema.json"
    )
    installed_schema.parent.mkdir(parents=True)
    installed_schema.write_text(CANONICAL_SCHEMA.read_text(encoding="utf-8"), encoding="utf-8")

    assert _resolve_default_record_schema_path(module_path) == installed_schema


def test_canonical_schema_declares_draft_2020_id_and_versioned_hash_contract() -> None:
    schema = json.loads(CANONICAL_SCHEMA.read_text(encoding="utf-8"))

    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["$id"].endswith("/schema/record-v1.schema.json")
    assert {
        "schema_version",
        "record_id",
        "created_at",
        "content",
        "content_hash",
        "content_hash_profile",
    } <= set(schema["required"])
    assert schema["properties"]["schema_version"]["const"] == "hc-record-v1"
    assert (
        schema["properties"]["content_hash_profile"]["const"]
        == HC_CONTENT_HASH_PROFILE
    )


@pytest.mark.parametrize(
    ("mutation", "expected_rule"),
    [
        (lambda record: record.pop("content"), "required"),
        (lambda record: record.__setitem__("created_at", "not-a-date"), "format"),
        (lambda record: record.__setitem__("schema_version", "record-v0"), "const"),
        (lambda record: record.__setitem__("content_hash_profile", "unknown-profile"), "const"),
        (lambda record: record.__setitem__("record_id", "not a canonical id"), "pattern"),
    ],
)
def test_shared_record_validator_enforces_required_format_and_profile_rules(
    tmp_path: Path,
    mutation,
    expected_rule: str,
) -> None:
    record = _record()
    mutation(record)

    passed, message = _validate_tmp_record(tmp_path, record)

    assert passed is False
    assert expected_rule in message.lower()


def test_runtime_uses_full_schema_instead_of_three_field_partial_check() -> None:
    record_id = "HC-RUNTIME-2026-0001"
    record = _record(record_id)
    record["created_at"] = "not-a-date"

    result = ValidatorPipeline(canonical_records={record_id: record}).run(
        record_id=record_id,
        qr_input=f"hc://{record_id}",
    )

    assert result["canonical_bridge"]["record_id_match"] is True
    assert result["canonical_bridge"]["schema_valid"] is False
    assert result["canonical_bridge"]["lookup_status"] == "schema_invalid"
    assert result["schema_result"]["checked"] is True
    assert result["schema_result"]["valid"] is False


def test_default_schema_cannot_be_shadowed_by_the_current_directory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    attacker_schema = tmp_path / "schema" / "record-v1.schema.json"
    attacker_schema.parent.mkdir(parents=True)
    attacker_schema.write_text(
        json.dumps(
            {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$id": "https://attacker.invalid/record-v1.schema.json",
                "type": "object",
            }
        ),
        encoding="utf-8",
    )
    record = _record()
    record["created_at"] = "not-a-date"
    record_path = tmp_path / "record.json"
    record_path.write_text(json.dumps(record), encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    passed, message = validate_record(record_path)

    assert passed is False
    assert "format" in message.lower()


@pytest.mark.parametrize(
    ("mutation", "expected_reason"),
    [
        (
            lambda schema: schema.__setitem__(
                "$id", "https://attacker.invalid/record-v1.schema.json"
            ),
            "record_schema_id_mismatch",
        ),
        (
            lambda schema: schema["properties"]["schema_version"].__setitem__(
                "const", "hc-record-v0"
            ),
            "record_schema_version_mismatch",
        ),
        (
            lambda schema: schema["properties"]["content_hash_profile"].__setitem__(
                "const", "unknown-profile"
            ),
            "record_schema_hash_profile_mismatch",
        ),
    ],
)
def test_explicit_schema_must_match_the_canonical_identity_and_profiles(
    tmp_path: Path,
    mutation,
    expected_reason: str,
) -> None:
    schema = json.loads(CANONICAL_SCHEMA.read_text(encoding="utf-8"))
    mutation(schema)
    schema_path = tmp_path / "record-v1.schema.json"
    schema_path.write_text(json.dumps(schema), encoding="utf-8")

    passed, errors = validate_record_payload(_record(), schema_path)

    assert passed is False
    assert errors == [f"$: schema unavailable ({expected_reason})"]


def test_schema_conformance_and_requested_record_binding_are_separate_checks() -> None:
    requested_id = "HC-REQUESTED-2026-0001"
    record = _record("HC-DIFFERENT-2026-0001")

    result = ValidatorPipeline(canonical_records={requested_id: record}).run(
        record_id=requested_id,
        qr_input=f"hc://{requested_id}",
    )

    assert result["canonical_bridge"]["schema_valid"] is True
    assert result["canonical_bridge"]["record_id_match"] is False
    assert result["canonical_bridge"]["lookup_status"] == "record_id_mismatch"


@pytest.mark.parametrize(
    "unsafe_value",
    [float("nan"), object()],
)
def test_shared_validator_rejects_non_i_json_values(unsafe_value: object) -> None:
    record = _record()
    record["extension"] = unsafe_value

    passed, errors = validate_record_payload(record)

    assert passed is False
    assert any("strict_json" in error for error in errors)


def test_shared_validator_rejects_cyclic_in_memory_records() -> None:
    record = _record()
    record["extension"] = record

    passed, errors = validate_record_payload(record)

    assert passed is False
    assert any("cyclic_json_value" in error for error in errors)


def test_checked_in_canonical_json_records_declare_and_pass_one_schema() -> None:
    paths = sorted(
        path
        for directory in ("pending", "verified", "archived")
        for path in (ROOT / "records" / directory).glob("*.json")
    )
    assert paths

    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        assert payload["schema_version"] == "hc-record-v1"
        assert payload["content_hash_profile"] == HC_CONTENT_HASH_PROFILE
        passed, message = validate_record(path, CANONICAL_SCHEMA)
        assert passed, message
