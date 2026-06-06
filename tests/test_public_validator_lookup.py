import json
import shutil
import subprocess
import sys
from pathlib import Path

from hc_runtime.public_validator_lookup import SAFETY_MARKERS, lookup_public_validator_record

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run_public_validator_lookup.py"
GOLDEN_OUTPUT_FIXTURES = ROOT / "docs" / "demo" / "fixtures" / "local-validator-output"
REQUIRED_FIELDS = {
    "record_id",
    "status",
    "found",
    "source_path",
    "advisory_only",
    "public_safe",
    "truth_guarantee",
    "human_review_required",
    "warnings",
    "errors",
    "checked_paths",
    "schema_validation",
    "hash_validation",
    "validation_summary",
}
REQUIRED_VALIDATION_FIELDS = {"status", "errors"}
REQUIRED_SUMMARY_FIELDS = {"schema_passed", "hash_passed", "canonical_record_checked"}
ALLOWED_LOOKUP_STATUSES = {"found", "not_found", "duplicate_record_id", "invalid_record_id", "lookup_error"}
ALLOWED_VALIDATION_STATUSES = {"pass", "fail", "not_checked"}
DETERMINISTIC_CHECKED_PATHS = [
    "records/pending/*.json",
    "records/verified/*.json",
    "records/archived/*.json",
]


def _valid_record_payload(record_id: str, *, content: str = "public validator lookup test") -> dict[str, object]:
    import hashlib

    return {
        "record_id": record_id,
        "created_at": "2026-05-14T10:35:00Z",
        "title": "Public Validator Lookup Test Record",
        "record_type": "ai_witness",
        "witness_type": "ai",
        "author": "HC-TRUST-LAYER tests",
        "content": content,
        "content_hash": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        "archive_ref": "pending_archive",
        "verification_status": "draft",
    }


def _write_record(path: Path, record_id: str, payload: dict[str, object] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload or _valid_record_payload(record_id)), encoding="utf-8")


def _copy_record_schema(root: Path) -> None:
    schema_dir = root / "schema"
    schema_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / "schema" / "record-v1.schema.json", schema_dir / "record-v1.schema.json")


def _assert_public_safe_shape(result: dict[str, object]) -> None:
    assert set(result) == REQUIRED_FIELDS
    assert result["status"] in ALLOWED_LOOKUP_STATUSES
    for key, value in SAFETY_MARKERS.items():
        assert result[key] is value
    assert isinstance(result["warnings"], list)
    assert isinstance(result["errors"], list)
    assert result["checked_paths"] == DETERMINISTIC_CHECKED_PATHS
    assert set(result["schema_validation"]) == REQUIRED_VALIDATION_FIELDS
    assert set(result["hash_validation"]) == REQUIRED_VALIDATION_FIELDS
    assert result["schema_validation"]["status"] in ALLOWED_VALIDATION_STATUSES
    assert result["hash_validation"]["status"] in ALLOWED_VALIDATION_STATUSES
    assert isinstance(result["schema_validation"]["errors"], list)
    assert isinstance(result["hash_validation"]["errors"], list)
    assert set(result["validation_summary"]) == REQUIRED_SUMMARY_FIELDS
    for value in result["validation_summary"].values():
        assert isinstance(value, bool)


def _schema_validation_supported() -> bool:
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        return False
    return True


def _load_golden_fixture(fixture_name: str) -> dict[str, object]:
    return json.loads((GOLDEN_OUTPUT_FIXTURES / fixture_name).read_text(encoding="utf-8"))


def _run_lookup_cli(record_id: str) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(RUNNER), record_id],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def _assert_cli_result_matches_golden_contract(payload: dict[str, object], fixture: dict[str, object]) -> None:
    _assert_public_safe_shape(payload)
    _assert_public_safe_shape(fixture)
    assert set(payload) == set(fixture)
    assert payload["record_id"] == fixture["record_id"]
    assert payload["status"] == fixture["status"]
    assert payload["found"] is fixture["found"]
    assert (payload["source_path"] is None) is (fixture["source_path"] is None)
    assert payload["checked_paths"] == fixture["checked_paths"]

    for key in SAFETY_MARKERS:
        assert payload[key] is fixture[key]

    for key in ("schema_validation", "hash_validation"):
        assert set(payload[key]) == set(fixture[key])
        assert isinstance(payload[key]["errors"], list)

    assert set(payload["validation_summary"]) == set(fixture["validation_summary"])
    assert isinstance(payload["warnings"], list)
    assert isinstance(payload["errors"], list)


def test_existing_record_id_found_from_allowed_records_directory() -> None:
    result = lookup_public_validator_record("HC-EXAMPLE-2026-0001", root=ROOT)

    _assert_public_safe_shape(result)
    assert result["status"] == "found"
    assert result["found"] is True
    assert result["source_path"] == "records/pending/HC-EXAMPLE-2026-0001.json"
    if _schema_validation_supported():
        assert result["schema_validation"] == {"status": "pass", "errors": []}
        assert result["validation_summary"]["schema_passed"] is True
    else:
        assert result["schema_validation"]["status"] == "not_checked"
        assert result["validation_summary"]["schema_passed"] is False
    assert result["hash_validation"] == {"status": "pass", "errors": []}
    assert result["validation_summary"]["hash_passed"] is True
    assert result["validation_summary"]["canonical_record_checked"] is True


def test_found_record_includes_advisory_schema_and_hash_validation_fields(tmp_path: Path) -> None:
    record_id = "HC-VALID-2026-0001"
    _copy_record_schema(tmp_path)
    _write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id)

    result = lookup_public_validator_record(record_id, root=tmp_path)

    _assert_public_safe_shape(result)
    assert result["status"] == "found"
    if _schema_validation_supported():
        assert result["schema_validation"] == {"status": "pass", "errors": []}
    else:
        assert result["schema_validation"]["status"] == "not_checked"
    assert result["hash_validation"] == {"status": "pass", "errors": []}
    assert result["validation_summary"]["canonical_record_checked"] is True


def test_malformed_record_shape_returns_schema_fail_without_crashing(tmp_path: Path) -> None:
    record_id = "HC-BADSHAPE-2026-0001"
    _copy_record_schema(tmp_path)
    _write_record(
        tmp_path / "records" / "pending" / f"{record_id}.json",
        record_id,
        {"record_id": record_id, "content": "missing canonical schema fields"},
    )

    result = lookup_public_validator_record(record_id, root=tmp_path)

    _assert_public_safe_shape(result)
    assert result["status"] == "found"
    assert result["found"] is True
    if _schema_validation_supported():
        assert result["schema_validation"]["status"] == "fail"
    else:
        assert result["schema_validation"]["status"] == "not_checked"
    assert result["validation_summary"]["schema_passed"] is False
    assert result["validation_summary"]["canonical_record_checked"] is True
    assert result["warnings"]
    assert result["errors"]


def test_wrong_content_hash_returns_hash_fail_without_crashing(tmp_path: Path) -> None:
    record_id = "HC-BADHASH-2026-0001"
    _copy_record_schema(tmp_path)
    payload = _valid_record_payload(record_id)
    payload["content_hash"] = "0" * 64
    _write_record(tmp_path / "records" / "pending" / f"{record_id}.json", record_id, payload)

    result = lookup_public_validator_record(record_id, root=tmp_path)

    _assert_public_safe_shape(result)
    assert result["status"] == "found"
    assert result["found"] is True
    if _schema_validation_supported():
        assert result["schema_validation"]["status"] == "pass"
    else:
        assert result["schema_validation"]["status"] == "not_checked"
    assert result["hash_validation"]["status"] == "fail"
    assert result["validation_summary"]["hash_passed"] is False
    assert result["validation_summary"]["canonical_record_checked"] is True
    assert result["warnings"]
    assert result["errors"]


def test_unknown_record_id_returns_not_found(tmp_path: Path) -> None:
    result = lookup_public_validator_record("HC-UNKNOWN-2026-0001", root=tmp_path)

    _assert_public_safe_shape(result)
    assert result["status"] == "not_found"
    assert result["found"] is False
    assert result["source_path"] is None
    assert result["validation_summary"]["canonical_record_checked"] is False


def test_invalid_empty_record_id_returns_invalid_record_id(tmp_path: Path) -> None:
    for record_id in ["", " ", "../records/pending/HC-EXAMPLE-2026-0001.json", "https://example.test/HC-1"]:
        result = lookup_public_validator_record(record_id, root=tmp_path)
        _assert_public_safe_shape(result)
        assert result["status"] == "invalid_record_id"
        assert result["found"] is False
        assert result["errors"]
        assert result["validation_summary"]["canonical_record_checked"] is False


def test_duplicate_record_id_across_allowed_directories_returns_duplicate_record_id(tmp_path: Path) -> None:
    record_id = "HC-DUPLICATE-2026-0001"
    _write_record(tmp_path / "records" / "pending" / "one.json", record_id)
    _write_record(tmp_path / "records" / "verified" / "two.json", record_id)

    result = lookup_public_validator_record(record_id, root=tmp_path)

    _assert_public_safe_shape(result)
    assert result["status"] == "duplicate_record_id"
    assert result["found"] is False
    assert result["source_path"] is None
    assert sorted(result["warnings"]) == ["records/pending/one.json", "records/verified/two.json"]
    assert result["errors"]
    assert result["validation_summary"]["canonical_record_checked"] is False


def test_demo_fixture_ids_do_not_resolve_from_docs_demo_fixtures(tmp_path: Path) -> None:
    record_id = "HC-DEMO-PV-FIXTURE-FOOD-0001"
    _write_record(tmp_path / "docs" / "demo" / "fixtures" / "results" / "banana.json", record_id)

    result = lookup_public_validator_record(record_id, root=tmp_path)

    _assert_public_safe_shape(result)
    assert result["status"] == "not_found"
    assert result["found"] is False


def test_generated_index_manifest_cache_and_export_paths_are_ignored(tmp_path: Path) -> None:
    record_id = "HC-IGNORED-2026-0001"
    _write_record(tmp_path / "generated" / "explorer_index.json", record_id)
    _write_record(tmp_path / "records" / "explorer_index.json", record_id)
    _write_record(tmp_path / "records" / "pending" / "cache" / f"{record_id}.json", record_id)
    _write_record(tmp_path / "records" / "pending" / f"{record_id}-index.json", record_id)
    _write_record(tmp_path / "exports" / "sample-package.json", record_id)
    _write_record(tmp_path / "federation" / "manifest.json", record_id)

    result = lookup_public_validator_record(record_id, root=tmp_path)

    _assert_public_safe_shape(result)
    assert result["status"] == "not_found"
    assert result["found"] is False


def test_runner_returns_deterministic_public_safe_json() -> None:
    first = subprocess.run(
        [sys.executable, str(RUNNER), "HC-EXAMPLE-2026-0001"],
        check=True,
        capture_output=True,
        text=True,
    )
    second = subprocess.run(
        [sys.executable, str(RUNNER), "HC-EXAMPLE-2026-0001"],
        check=True,
        capture_output=True,
        text=True,
    )

    first_payload = json.loads(first.stdout)
    second_payload = json.loads(second.stdout)
    _assert_public_safe_shape(first_payload)
    assert first_payload == second_payload
    assert first_payload["status"] == "found"


def test_all_non_found_statuses_keep_full_contract_and_null_source_path(tmp_path: Path) -> None:
    duplicate_id = "HC-DUP-CONTRACT-2026-0001"
    _write_record(tmp_path / "records" / "pending" / "one.json", duplicate_id)
    _write_record(tmp_path / "records" / "verified" / "two.json", duplicate_id)

    corrupt_id = "HC-LOOKUP-ERROR-2026-0001"
    corrupt_path = tmp_path / "records" / "pending" / f"{corrupt_id}.json"
    corrupt_path.parent.mkdir(parents=True, exist_ok=True)
    corrupt_path.write_text("{not-json", encoding="utf-8")

    cases = [
        lookup_public_validator_record("HC-MISSING-CONTRACT-2026-0001", root=tmp_path),
        lookup_public_validator_record("../records/pending/HC-BAD.json", root=tmp_path),
        lookup_public_validator_record(duplicate_id, root=tmp_path),
        lookup_public_validator_record(corrupt_id, root=tmp_path),
    ]

    assert {result["status"] for result in cases} == {
        "not_found",
        "invalid_record_id",
        "duplicate_record_id",
        "lookup_error",
    }
    for result in cases:
        _assert_public_safe_shape(result)
        assert result["found"] is False
        assert result["source_path"] is None
        assert result["schema_validation"] == {"status": "not_checked", "errors": []}
        assert result["hash_validation"] == {"status": "not_checked", "errors": []}
        assert result["validation_summary"] == {
            "schema_passed": False,
            "hash_passed": False,
            "canonical_record_checked": False,
        }


def test_canonical_record_checked_only_when_single_canonical_match_is_checked(tmp_path: Path) -> None:
    single_id = "HC-SINGLE-CHECKED-2026-0001"
    duplicate_id = "HC-DUP-CHECKED-2026-0001"
    _write_record(tmp_path / "records" / "pending" / f"{single_id}.json", single_id)
    _write_record(tmp_path / "records" / "pending" / "duplicate-one.json", duplicate_id)
    _write_record(tmp_path / "records" / "verified" / "duplicate-two.json", duplicate_id)

    single = lookup_public_validator_record(single_id, root=tmp_path)
    missing = lookup_public_validator_record("HC-MISSING-CHECKED-2026-0001", root=tmp_path)
    duplicate = lookup_public_validator_record(duplicate_id, root=tmp_path)
    invalid = lookup_public_validator_record("https://example.test/HC-SINGLE-CHECKED-2026-0001", root=tmp_path)

    _assert_public_safe_shape(single)
    assert single["status"] == "found"
    assert single["validation_summary"]["canonical_record_checked"] is True
    assert single["source_path"] == f"records/pending/{single_id}.json"

    for result in (missing, duplicate, invalid):
        _assert_public_safe_shape(result)
        assert result["status"] != "found"
        assert result["source_path"] is None
        assert result["validation_summary"]["canonical_record_checked"] is False


def test_local_validator_golden_fixtures_preserve_public_safe_contract() -> None:
    expected_statuses = {
        "found.json": "found",
        "not-found.json": "not_found",
        "invalid-record-id.json": "invalid_record_id",
    }

    for fixture_name, expected_status in expected_statuses.items():
        fixture = json.loads((GOLDEN_OUTPUT_FIXTURES / fixture_name).read_text(encoding="utf-8"))

        _assert_public_safe_shape(fixture)
        assert fixture["status"] == expected_status


def test_cli_output_matches_golden_fixture_contract_shapes() -> None:
    cases = [
        ("HC-EXAMPLE-2026-0001", "found.json"),
        ("HC-NOT-FOUND-2026-0001", "not-found.json"),
        ("../records/pending/example.json", "invalid-record-id.json"),
    ]

    for record_id, fixture_name in cases:
        payload = _run_lookup_cli(record_id)
        fixture = _load_golden_fixture(fixture_name)

        _assert_cli_result_matches_golden_contract(payload, fixture)


def test_cli_output_matches_result_contract_for_found_unknown_and_invalid() -> None:
    for record_id, expected_status in [
        ("HC-EXAMPLE-2026-0001", "found"),
        ("HC-NOT-FOUND-2026-0001", "not_found"),
        ("../records/pending/example.json", "invalid_record_id"),
    ]:
        payload = _run_lookup_cli(record_id)

        _assert_public_safe_shape(payload)
        assert payload["status"] == expected_status
