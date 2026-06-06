import json
import subprocess
import sys
from pathlib import Path

from hc_runtime.public_validator_lookup import SAFETY_MARKERS, lookup_public_validator_record

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run_public_validator_lookup.py"
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
}


def _write_record(path: Path, record_id: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"record_id": record_id, "content": "public validator lookup test"}), encoding="utf-8")


def _assert_public_safe_shape(result: dict[str, object]) -> None:
    assert REQUIRED_FIELDS.issubset(result)
    for key, value in SAFETY_MARKERS.items():
        assert result[key] is value
    assert isinstance(result["warnings"], list)
    assert isinstance(result["errors"], list)
    assert result["checked_paths"] == [
        "records/pending/*.json",
        "records/verified/*.json",
        "records/archived/*.json",
    ]


def test_existing_record_id_found_from_allowed_records_directory() -> None:
    result = lookup_public_validator_record("HC-EXAMPLE-2026-0001", root=ROOT)

    _assert_public_safe_shape(result)
    assert result["status"] == "found"
    assert result["found"] is True
    assert result["source_path"] == "records/pending/HC-EXAMPLE-2026-0001.json"


def test_unknown_record_id_returns_not_found(tmp_path: Path) -> None:
    result = lookup_public_validator_record("HC-UNKNOWN-2026-0001", root=tmp_path)

    _assert_public_safe_shape(result)
    assert result["status"] == "not_found"
    assert result["found"] is False
    assert result["source_path"] is None


def test_invalid_empty_record_id_returns_invalid_record_id(tmp_path: Path) -> None:
    for record_id in ["", " ", "../records/pending/HC-EXAMPLE-2026-0001.json", "https://example.test/HC-1"]:
        result = lookup_public_validator_record(record_id, root=tmp_path)
        _assert_public_safe_shape(result)
        assert result["status"] == "invalid_record_id"
        assert result["found"] is False
        assert result["errors"]


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
