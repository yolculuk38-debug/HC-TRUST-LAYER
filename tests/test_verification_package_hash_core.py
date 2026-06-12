import hashlib
import json

from hc_trust.verification_package import verify_verification_package


def _write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def test_verification_package_hash_core_verifies_manifest_files(tmp_path):
    package = tmp_path / "package"
    metadata = package / "metadata" / "source-info.json"
    metadata.parent.mkdir(parents=True)
    metadata.write_text("source-ok", encoding="utf-8")

    _write_json(
        package / "manifest.json",
        {
            "package_id": "HC-PKG-1",
            "schema_version": "verification-package-v1",
            "record_id": "HC-RECORD-1",
            "files": [
                {
                    "path": "metadata/source-info.json",
                    "sha256": _sha256_text("source-ok"),
                }
            ],
        },
    )

    result = verify_verification_package(package)

    assert result["status"] == "VERIFIED"
    assert result["verified"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is False
    assert result["checks"] == {
        "manifest_present": True,
        "manifest_files_checked": 1,
        "sha256_only": True,
        "signatures_verified": False,
        "witnesses_verified": False,
    }
    assert result["files"] == [
        {
            "path": "metadata/source-info.json",
            "status": "MATCH",
            "expected_sha256": _sha256_text("source-ok"),
            "actual_sha256": _sha256_text("source-ok"),
        }
    ]


def test_verification_package_hash_core_flags_tampering(tmp_path):
    package = tmp_path / "package"
    artifact = package / "revision" / "revision-head.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_text("changed", encoding="utf-8")

    _write_json(
        package / "manifest.json",
        {
            "package_id": "HC-PKG-TAMPERED",
            "record_id": "HC-RECORD-TAMPERED",
            "files": [
                {
                    "path": "revision/revision-head.json",
                    "sha256": _sha256_text("original"),
                }
            ],
        },
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["verified"] is False
    assert result["human_review_required"] is True
    assert "sha256_mismatch:revision/revision-head.json" in result["conflicting_evidence"]
    assert result["files"][0]["status"] == "MISMATCH"


def test_verification_package_hash_core_rejects_path_traversal(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    _write_json(
        package / "manifest.json",
        {
            "package_id": "HC-PKG-UNSAFE",
            "record_id": "HC-RECORD-UNSAFE",
            "files": [
                {
                    "path": "../outside.json",
                    "sha256": _sha256_text("outside"),
                }
            ],
        },
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "unsafe_manifest_file_path:../outside.json" in result["conflicting_evidence"]
    assert result["files"][0] == {
        "path": "../outside.json",
        "status": "INVALID",
        "reason": "unsafe_path",
    }


def test_verification_package_hash_core_requires_manifest(tmp_path):
    package = tmp_path / "package"
    package.mkdir()

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["checks"]["manifest_present"] is False
    assert "manifest_json_missing" in result["missing_evidence"]
