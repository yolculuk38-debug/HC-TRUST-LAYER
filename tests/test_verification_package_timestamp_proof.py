import hashlib
import json

from hc_trust.verification_package import verify_verification_package


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _write_package(package, timestamp_entry=None, timestamp_text=None):
    artifact = package / "metadata" / "source-info.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_text("source-ok", encoding="utf-8")
    manifest = {
        "package_id": "HC-PKG-TIME",
        "record_id": "HC-RECORD-TIME",
        "files": [
            {
                "path": "metadata/source-info.json",
                "sha256": _sha256_text("source-ok"),
            }
        ],
    }
    if timestamp_entry is not None:
        manifest["timestamp_proof"] = timestamp_entry
    if timestamp_text is not None:
        (package / "timestamp-proof.json").write_text(timestamp_text, encoding="utf-8")
    (package / "manifest.json").write_text(json.dumps(manifest, sort_keys=True), encoding="utf-8")


def test_timestamp_proof_not_provided(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    _write_package(package)

    result = verify_verification_package(package)

    assert result["status"] == "VERIFIED"
    assert result["timestamp_proof"]["status"] == "NOT_PROVIDED"
    assert result["checks"]["timestamp_proof_checked"] is False
    assert result["checks"]["timestamp_proof_present"] is False
    assert result["checks"]["external_timestamp_verified"] is False
    assert result["truth_guarantee"] is False


def test_timestamp_proof_present(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    subject_hash = _sha256_text("source-ok")
    timestamp_text = json.dumps(
        {"claimed_at": "2026-06-12T00:00:00Z", "subject_sha256": subject_hash},
        sort_keys=True,
    )
    _write_package(
        package,
        timestamp_entry={"path": "timestamp-proof.json", "sha256": _sha256_text(timestamp_text)},
        timestamp_text=timestamp_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "VERIFIED"
    assert result["timestamp_proof"]["status"] == "PRESENT"
    assert result["timestamp_proof"]["claimed_at"] == "2026-06-12T00:00:00Z"
    assert result["timestamp_proof"]["subject_sha256"] == subject_hash
    assert result["timestamp_proof"]["external_verified"] is False
    assert result["checks"]["timestamp_proof_checked"] is True
    assert result["checks"]["timestamp_proof_present"] is True
    assert result["checks"]["external_timestamp_verified"] is False
    assert result["truth_guarantee"] is False


def test_timestamp_proof_rejects_invalid_claimed_at(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    timestamp_text = json.dumps(
        {"claimed_at": "not-a-timestamp", "subject_sha256": _sha256_text("source-ok")},
        sort_keys=True,
    )
    _write_package(
        package,
        timestamp_entry={"path": "timestamp-proof.json", "sha256": _sha256_text(timestamp_text)},
        timestamp_text=timestamp_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["timestamp_proof"]["status"] == "INVALID"
    assert result["timestamp_proof"]["reason"] == "timestamp_proof_claimed_at_invalid"
    assert "timestamp_proof_claimed_at_invalid:timestamp-proof.json" in result["conflicting_evidence"]


def test_timestamp_proof_rejects_unrelated_subject_hash(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    unrelated_hash = _sha256_text("unrelated-subject")
    timestamp_text = json.dumps(
        {"claimed_at": "2026-06-12T00:00:00Z", "subject_sha256": unrelated_hash},
        sort_keys=True,
    )
    _write_package(
        package,
        timestamp_entry={"path": "timestamp-proof.json", "sha256": _sha256_text(timestamp_text)},
        timestamp_text=timestamp_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["timestamp_proof"]["status"] == "INVALID"
    assert result["timestamp_proof"]["reason"] == "timestamp_proof_subject_sha256_mismatch"
    assert result["timestamp_proof"]["subject_sha256"] == unrelated_hash
    assert "timestamp_proof_subject_sha256_mismatch:timestamp-proof.json" in result["conflicting_evidence"]


def test_timestamp_proof_missing(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    _write_package(
        package,
        timestamp_entry={"path": "timestamp-proof.json", "sha256": _sha256_text("missing")},
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["timestamp_proof"]["status"] == "MISSING"
    assert "file_missing:timestamp-proof.json" in result["missing_evidence"]


def test_timestamp_proof_mismatch(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    timestamp_text = json.dumps(
        {"claimed_at": "2026-06-12T00:00:00Z", "subject_sha256": _sha256_text("source-ok")},
        sort_keys=True,
    )
    _write_package(
        package,
        timestamp_entry={"path": "timestamp-proof.json", "sha256": _sha256_text("other")},
        timestamp_text=timestamp_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["timestamp_proof"]["status"] == "MISMATCH"
    assert "sha256_mismatch:timestamp-proof.json" in result["conflicting_evidence"]


def test_timestamp_proof_invalid_json(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    timestamp_text = "not json"
    _write_package(
        package,
        timestamp_entry={"path": "timestamp-proof.json", "sha256": _sha256_text(timestamp_text)},
        timestamp_text=timestamp_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["timestamp_proof"]["status"] == "INVALID"
    assert "timestamp_proof_json_invalid:timestamp-proof.json" in result["conflicting_evidence"]
