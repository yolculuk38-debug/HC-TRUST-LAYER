import hashlib
import json

from hc_trust.verification_package import _is_within_directory, verify_verification_package


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
        "issuer_proof_checked": False,
        "issuer_proof_present": False,
        "issuer_identity_verified": False,
        "timestamp_proof_checked": False,
        "timestamp_proof_present": False,
        "external_timestamp_verified": False,
        "witness_proof_checked": False,
        "witness_proof_present": False,
        "signatures_verified": False,
        "witnesses_verified": False,
    }
    assert result["issuer_proof"] == {
        "status": "NOT_PROVIDED",
        "checked": False,
        "path": None,
        "identity_verified": False,
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


def test_verification_package_hash_core_rejects_manifest_directory(tmp_path):
    package = tmp_path / "package"
    (package / "manifest.json").mkdir(parents=True)

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "manifest_json_not_file" in result["conflicting_evidence"]


def test_verification_package_hash_core_handles_non_utf8_manifest(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    (package / "manifest.json").write_bytes(b"\xff\xfe\x00")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "manifest_json_unreadable" in result["conflicting_evidence"]


def test_verification_package_issuer_proof_present(tmp_path):
    package = tmp_path / "package"
    metadata = package / "metadata" / "source-info.json"
    proof = package / "issuer-proof.json"
    metadata.parent.mkdir(parents=True)
    metadata.write_text("source-ok", encoding="utf-8")
    proof_text = json.dumps({"issuer": "HC-SAMPLE-ISSUER", "statement": "sample package issued"}, sort_keys=True)
    proof.write_text(proof_text, encoding="utf-8")

    _write_json(
        package / "manifest.json",
        {
            "package_id": "HC-PKG-ISSUER",
            "record_id": "HC-RECORD-ISSUER",
            "files": [
                {
                    "path": "metadata/source-info.json",
                    "sha256": _sha256_text("source-ok"),
                }
            ],
            "issuer_proof": {"path": "issuer-proof.json", "sha256": _sha256_text(proof_text)},
        },
    )

    result = verify_verification_package(package)

    assert result["status"] == "VERIFIED"
    assert result["checks"]["issuer_proof_checked"] is True
    assert result["checks"]["issuer_proof_present"] is True
    assert result["checks"]["issuer_identity_verified"] is False
    assert result["issuer_proof"]["status"] == "PRESENT"
    assert result["issuer_proof"]["issuer"] == "HC-SAMPLE-ISSUER"
    assert result["issuer_proof"]["identity_verified"] is False


def test_verification_package_issuer_proof_missing(tmp_path):
    package = tmp_path / "package"
    metadata = package / "metadata" / "source-info.json"
    metadata.parent.mkdir(parents=True)
    metadata.write_text("source-ok", encoding="utf-8")

    _write_json(
        package / "manifest.json",
        {
            "package_id": "HC-PKG-ISSUER-MISSING",
            "record_id": "HC-RECORD-ISSUER-MISSING",
            "files": [
                {
                    "path": "metadata/source-info.json",
                    "sha256": _sha256_text("source-ok"),
                }
            ],
            "issuer_proof": {"path": "issuer-proof.json", "sha256": _sha256_text("missing")},
        },
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["checks"]["issuer_proof_checked"] is True
    assert result["checks"]["issuer_proof_present"] is False
    assert result["checks"]["issuer_identity_verified"] is False
    assert result["issuer_proof"]["status"] == "MISSING"
    assert result["issuer_proof"]["identity_verified"] is False
    assert "file_missing:issuer-proof.json" in result["missing_evidence"]


def test_verification_package_issuer_proof_malformed(tmp_path):
    package = tmp_path / "package"
    metadata = package / "metadata" / "source-info.json"
    proof = package / "issuer-proof.json"
    metadata.parent.mkdir(parents=True)
    metadata.write_text("source-ok", encoding="utf-8")
    proof_text = "not-json"
    proof.write_text(proof_text, encoding="utf-8")

    _write_json(
        package / "manifest.json",
        {
            "package_id": "HC-PKG-ISSUER-BAD",
            "record_id": "HC-RECORD-ISSUER-BAD",
            "files": [
                {
                    "path": "metadata/source-info.json",
                    "sha256": _sha256_text("source-ok"),
                }
            ],
            "issuer_proof": {"path": "issuer-proof.json", "sha256": _sha256_text(proof_text)},
        },
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["checks"]["issuer_identity_verified"] is False
    assert result["issuer_proof"]["status"] == "INVALID"
    assert result["issuer_proof"]["identity_verified"] is False
    assert result["issuer_proof"]["reason"] == "issuer_proof_json_invalid"
    assert "issuer_proof_json_invalid:issuer-proof.json" in result["conflicting_evidence"]


def test_verification_package_issuer_proof_mismatch(tmp_path):
    package = tmp_path / "package"
    metadata = package / "metadata" / "source-info.json"
    proof = package / "issuer-proof.json"
    metadata.parent.mkdir(parents=True)
    metadata.write_text("source-ok", encoding="utf-8")
    proof.write_text("changed", encoding="utf-8")

    _write_json(
        package / "manifest.json",
        {
            "package_id": "HC-PKG-ISSUER-MISMATCH",
            "record_id": "HC-RECORD-ISSUER-MISMATCH",
            "files": [
                {
                    "path": "metadata/source-info.json",
                    "sha256": _sha256_text("source-ok"),
                }
            ],
            "issuer_proof": {"path": "issuer-proof.json", "sha256": _sha256_text("original")},
        },
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["checks"]["issuer_identity_verified"] is False
    assert result["issuer_proof"]["status"] == "MISMATCH"
    assert result["issuer_proof"]["identity_verified"] is False
    assert "sha256_mismatch:issuer-proof.json" in result["conflicting_evidence"]


def test_is_within_directory_rejects_sibling_paths(tmp_path):
    package = tmp_path / "package"
    sibling = tmp_path / "sibling" / "file.json"
    package.mkdir()
    sibling.parent.mkdir()
    sibling.write_text("not package evidence", encoding="utf-8")

    assert _is_within_directory(sibling.resolve(), package.resolve()) is False
