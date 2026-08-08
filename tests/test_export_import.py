import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

import pytest

from hc_trust.hashing import HC_CONTENT_HASH_PROFILE, calculate_content_hash
from src.export_package import build_export_package, export_package
from src.import_verify import verify_package_dict, verify_package_file


def _build_package_with_record(
    tmp_path: Path,
    record: dict[str, object],
) -> dict[str, object]:
    verified = tmp_path / "records" / "verified"
    verified.mkdir(parents=True)
    (verified / "record.json").write_text(
        json.dumps(record, ensure_ascii=False),
        encoding="utf-8",
    )
    return build_export_package(tmp_path)


def test_export_package_creation(tmp_path: Path):
    verified = tmp_path / "records" / "verified"
    verified.mkdir(parents=True)
    record = {
        "record_id": "HC-TEST-1",
        "content": "hello",
        "content_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
    }
    (verified / "record.json").write_text(json.dumps(record), encoding="utf-8")

    snapshots = tmp_path / "audit"
    snapshots.mkdir(parents=True)
    (snapshots / "snapshot.json").write_text(json.dumps({"snapshot_id": "s1"}), encoding="utf-8")

    package = build_export_package(tmp_path)
    assert package["records_count"] == 1
    assert package["snapshot_count"] == 1
    assert "package_hash" in package and len(package["package_hash"]) == 64


def test_package_hash_recalculation(tmp_path: Path):
    package = build_export_package(tmp_path)
    ok, errors = verify_package_dict(package)
    assert ok is True
    assert errors == []


def test_valid_import_verification(tmp_path: Path):
    out = tmp_path / "pkg.json"
    export_package(out, tmp_path)
    ok, errors = verify_package_file(out)
    assert ok is True
    assert errors == []


def test_tampered_package_fails(tmp_path: Path):
    out = tmp_path / "pkg.json"
    package = export_package(out, tmp_path)
    package["records_count"] = 999
    out.write_text(json.dumps(package), encoding="utf-8")

    ok, errors = verify_package_file(out)
    assert ok is False
    assert any("mismatch" in err or "does not match" in err for err in errors)


def test_missing_required_fields_fail():
    ok, errors = verify_package_dict({"package_id": "x"})
    assert ok is False
    assert any("missing required fields" in err for err in errors)


def test_structured_record_import_uses_shared_profile_aware_jcs_hashing(
    tmp_path: Path,
):
    content = {"n": 1.0}
    package = _build_package_with_record(
        tmp_path,
        {
            "record_id": "HC-IMPORT-2026-0001",
            "content": content,
            "content_hash": calculate_content_hash(
                content,
                HC_CONTENT_HASH_PROFILE,
            ),
            "content_hash_profile": HC_CONTENT_HASH_PROFILE,
        },
    )

    ok, errors = verify_package_dict(package)

    assert ok is True
    assert errors == []


def test_string_record_import_without_profile_keeps_legacy_compatibility(
    tmp_path: Path,
):
    content = "legacy-compatible text"
    package = _build_package_with_record(
        tmp_path,
        {
            "record_id": "HC-IMPORT-2026-0002",
            "content": content,
            "content_hash": calculate_content_hash(content),
        },
    )

    ok, errors = verify_package_dict(package)

    assert ok is True
    assert errors == []


@pytest.mark.parametrize(
    ("profile_case", "expected_reason"),
    [
        ("missing", "legacy_structured_content_algorithm_ambiguous"),
        ("null", "unknown_content_hash_profile"),
        ("unknown", "unknown_content_hash_profile"),
    ],
)
def test_record_import_fails_closed_when_content_hash_profile_is_unverifiable(
    tmp_path: Path,
    profile_case: str,
    expected_reason: str,
):
    content = {"n": 1.0}
    record: dict[str, object] = {
        "record_id": "HC-IMPORT-2026-0003",
        "content": content,
        "content_hash": calculate_content_hash(
            content,
            HC_CONTENT_HASH_PROFILE,
        ),
    }
    if profile_case == "null":
        record["content_hash_profile"] = None
    elif profile_case == "unknown":
        record["content_hash_profile"] = "unknown-profile"
    package = _build_package_with_record(tmp_path, record)

    ok, errors = verify_package_dict(package)

    assert ok is False
    assert errors == [
        f"record[0] content_hash unverifiable ({expected_reason})"
    ]
