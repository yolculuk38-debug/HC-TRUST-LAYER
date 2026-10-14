import hashlib
import json
import os

import pytest

from hc_trust.verification_package import (
    VERIFICATION_PACKAGE_MANIFEST_SCHEMA_VERSION,
    _manifest_validator,
    verify_verification_package,
)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _package(tmp_path, manifest_overrides=None):
    package = tmp_path / "package"
    package.mkdir()
    artifact = package / "payload.bin"
    artifact.write_bytes(b"payload bytes")
    manifest = {
        "schema_version": VERIFICATION_PACKAGE_MANIFEST_SCHEMA_VERSION,
        "package_id": "HC-PKG-TEST",
        "record_id": "HC-RECORD-TEST",
        "files": [{"path": "payload.bin", "sha256": _sha256(artifact.read_bytes()), "role": "payload"}],
    }
    if manifest_overrides:
        manifest.update(manifest_overrides)
    (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return package, manifest


def test_local_manifest_v1_accepts_namespaced_opaque_extensions_and_empty_directories(tmp_path):
    package, manifest = _package(
        tmp_path,
        {"extensions": {"urn:example:label": {"arbitrary": [1, 2, 3]}}},
    )
    (package / "empty" / "nested").mkdir(parents=True)

    result = verify_verification_package(package)

    assert result["status"] == "VERIFIED"
    assert result["schema_version"] == manifest["schema_version"]
    assert result["package_id"] == "HC-PKG-TEST"


@pytest.mark.parametrize(
    "changes",
    [
        {"schema_version": None},
        {"schema_version": "unknown-v9"},
        {"package_id": ""},
        {"record_id": "   "},
        {"extra_hash": "a" * 64},
        {"signature_proof": {"path": "payload.bin", "sha256": "a" * 64}},
        {"files": [{"path": "payload.bin", "digest": "a" * 64}]},
        {"files": [{"path": "payload.bin", "hash": "a" * 64}]},
        {"files": [{"path": "payload.bin", "sha256": "a" * 64, "algorithm": "md5"}]},
        {"files": [{"path": "payload.bin", "sha256": "a" * 64, "role": "signature"}]},
    ],
)
def test_local_manifest_v1_rejects_missing_or_unsupported_contract_fields(tmp_path, changes):
    package, manifest = _package(tmp_path)
    manifest.update(changes)
    if changes.get("schema_version") is None:
        manifest.pop("schema_version")
    (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert any(item.startswith("manifest_schema_invalid:") for item in result["conflicting_evidence"])


def test_local_manifest_v1_rejects_duplicate_file_paths(tmp_path):
    package, manifest = _package(tmp_path)
    manifest["files"].append(dict(manifest["files"][0], role="opaque"))
    (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "manifest_file_path_duplicate:payload.bin" in result["conflicting_evidence"]


@pytest.mark.parametrize("field", ["package_id", "record_id", "schema_version"])
def test_local_manifest_v1_requires_each_identity_and_version_field(tmp_path, field):
    package, manifest = _package(tmp_path)
    manifest.pop(field)
    (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert any(item.startswith("manifest_schema_invalid:") for item in result["conflicting_evidence"])


def test_local_manifest_v1_rejects_a_proof_reference_reusing_a_file_path(tmp_path):
    package, manifest = _package(tmp_path)
    manifest["issuer_proof"] = {"path": "payload.bin", "sha256": _sha256(b"payload bytes")}
    (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "manifest_file_path_duplicate:payload.bin" in result["conflicting_evidence"]


def test_local_manifest_v1_rejects_duplicate_json_object_keys(tmp_path):
    package, manifest = _package(tmp_path)
    text = json.dumps(manifest)
    text = text.replace('"package_id": "HC-PKG-TEST"', '"package_id": "HC-PKG-TEST", "package_id": "HC-PKG-OTHER"')
    (package / "manifest.json").write_text(text, encoding="utf-8")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "manifest_json_duplicate_key" in result["conflicting_evidence"]


def test_local_manifest_v1_rejects_nonstandard_json_constants(tmp_path):
    package, manifest = _package(tmp_path)
    manifest["extensions"] = {"urn:example:measurement": float("nan")}
    (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "manifest_json_invalid" in result["conflicting_evidence"]


def test_local_manifest_v1_rejects_unlisted_regular_files(tmp_path):
    package, _ = _package(tmp_path)
    (package / "unlisted.bin").write_bytes(b"not committed in manifest")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "package_file_unlisted:unlisted.bin" in result["conflicting_evidence"]


def test_local_manifest_v1_rejects_duplicate_keys_in_parsed_proof_json(tmp_path):
    package, manifest = _package(tmp_path)
    proof_text = '{"claimed_at":"2026-06-12T00:00:00Z","claimed_at":"2026-06-13T00:00:00Z","subject_sha256":"' + _sha256(b"payload bytes") + '"}'
    proof_path = package / "time-proof.json"
    proof_path.write_text(proof_text, encoding="utf-8")
    manifest["timestamp_proof"] = {"path": "time-proof.json", "sha256": _sha256(proof_path.read_bytes())}
    (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "timestamp_proof_json_duplicate_key:time-proof.json" in result["conflicting_evidence"]


def test_local_manifest_v1_rejects_unknown_parsed_proof_fields(tmp_path):
    package, manifest = _package(tmp_path)
    proof = {
        "claimed_at": "2026-06-12T00:00:00Z",
        "subject_sha256": _sha256(b"payload bytes"),
        "trusted": True,
    }
    proof_text = json.dumps(proof)
    proof_path = package / "time-proof.json"
    proof_path.write_text(proof_text, encoding="utf-8")
    manifest["timestamp_proof"] = {"path": "time-proof.json", "sha256": _sha256(proof_path.read_bytes())}
    (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "timestamp_proof_json_unknown_fields:time-proof.json" in result["conflicting_evidence"]


@pytest.mark.parametrize("link_name", ["manifest.json", "payload.bin"])
def test_local_manifest_v1_rejects_symlinks(tmp_path, link_name):
    package, manifest = _package(tmp_path)
    outside = tmp_path / "outside"
    if link_name == "manifest.json":
        outside.write_text(json.dumps(manifest), encoding="utf-8")
        (package / "manifest.json").unlink()
        target = outside
    else:
        outside.write_bytes(b"payload bytes")
        (package / "payload.bin").unlink()
        target = outside
    try:
        (package / link_name).symlink_to(target)
    except (NotImplementedError, OSError):
        pytest.skip("symlinks are unavailable on this platform")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert any("symlink_not_allowed" in item for item in result["conflicting_evidence"])


def test_local_manifest_v1_rejects_symlink_package_root(tmp_path):
    package, _ = _package(tmp_path)
    package_link = tmp_path / "package-link"
    try:
        package_link.symlink_to(package, target_is_directory=True)
    except (NotImplementedError, OSError):
        pytest.skip("symlinks are unavailable on this platform")

    result = verify_verification_package(package_link)

    assert result["status"] == "INVALID"
    assert "package_path_symlink_not_allowed" in result["conflicting_evidence"]


def test_local_manifest_v1_rejects_unlisted_symlink(tmp_path):
    package, _ = _package(tmp_path)
    outside = tmp_path / "outside.bin"
    outside.write_bytes(b"external bytes")
    try:
        (package / "unlisted-link").symlink_to(outside)
    except (NotImplementedError, OSError):
        pytest.skip("symlinks are unavailable on this platform")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "package_symlink_not_allowed:unlisted-link" in result["conflicting_evidence"]


def test_local_manifest_v1_rejects_special_files(tmp_path):
    if not hasattr(os, "mkfifo"):
        pytest.skip("named pipes are unavailable on this platform")
    package, _ = _package(tmp_path)
    os.mkfifo(package / "unexpected-pipe")

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert "package_special_file_not_allowed:unexpected-pipe" in result["conflicting_evidence"]


def test_local_manifest_v1_schema_is_available_as_a_package_resource():
    schema = _manifest_validator().schema

    assert schema["properties"]["schema_version"]["const"] == VERIFICATION_PACKAGE_MANIFEST_SCHEMA_VERSION
