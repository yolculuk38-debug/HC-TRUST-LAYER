import hashlib
import json

from hc_trust.cli import main
from hc_trust.verification_package import verify_verification_package


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _write_package(package, proof_entry=None, proof_text=None, manifest_extra=None):
    artifact = package / "metadata" / "source-info.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_text("source-ok", encoding="utf-8")
    manifest = {
        "package_id": "HC-PKG-WITNESS",
        "record_id": "HC-RECORD-WITNESS",
        "files": [
            {
                "path": "metadata/source-info.json",
                "sha256": _sha256_text("source-ok"),
            }
        ],
    }
    if manifest_extra:
        manifest.update(manifest_extra)
    if proof_entry is not None:
        manifest["witness_proof"] = proof_entry
    if proof_text is not None:
        (package / "witness-proof.json").write_text(proof_text, encoding="utf-8")
    (package / "manifest.json").write_text(json.dumps(manifest, sort_keys=True), encoding="utf-8")


def _witness_text(subject_sha256=None):
    return json.dumps(
        {
            "witness_id": "HC-WITNESS-SAMPLE",
            "statement": "sample package witnessed",
            "subject_sha256": subject_sha256 or _sha256_text("source-ok"),
        },
        sort_keys=True,
    )


def test_witness_proof_not_provided(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    _write_package(package)

    result = verify_verification_package(package)

    assert result["status"] == "VERIFIED"
    assert result["witness_proof"]["status"] == "NOT_PROVIDED"
    assert result["checks"]["witness_proof_checked"] is False
    assert result["checks"]["witness_proof_present"] is False
    assert result["checks"]["witnesses_verified"] is False
    assert result["truth_guarantee"] is False


def test_witness_proof_present_with_subject_binding(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    proof_text = _witness_text()
    _write_package(
        package,
        proof_entry={"path": "witness-proof.json", "sha256": _sha256_text(proof_text)},
        proof_text=proof_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "VERIFIED"
    assert result["witness_proof"]["status"] == "PRESENT"
    assert result["witness_proof"]["witness_id"] == "HC-WITNESS-SAMPLE"
    assert result["witness_proof"]["subject_sha256"] == _sha256_text("source-ok")
    assert result["witness_proof"]["signature_verified"] is False
    assert result["checks"]["witness_proof_checked"] is True
    assert result["checks"]["witness_proof_present"] is True
    assert result["checks"]["witnesses_verified"] is False
    assert result["truth_guarantee"] is False


def test_witness_proof_missing(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    _write_package(
        package,
        proof_entry={"path": "witness-proof.json", "sha256": _sha256_text("missing")},
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["witness_proof"]["status"] == "MISSING"
    assert "file_missing:witness-proof.json" in result["missing_evidence"]


def test_witness_proof_mismatch(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    proof_text = _witness_text()
    _write_package(
        package,
        proof_entry={"path": "witness-proof.json", "sha256": _sha256_text("other")},
        proof_text=proof_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["witness_proof"]["status"] == "MISMATCH"
    assert "sha256_mismatch:witness-proof.json" in result["conflicting_evidence"]


def test_witness_proof_invalid_json(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    proof_text = "not json"
    _write_package(
        package,
        proof_entry={"path": "witness-proof.json", "sha256": _sha256_text(proof_text)},
        proof_text=proof_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["witness_proof"]["status"] == "INVALID"
    assert "witness_proof_json_invalid:witness-proof.json" in result["conflicting_evidence"]


def test_witness_proof_subject_mismatch(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    proof_text = _witness_text(subject_sha256=_sha256_text("unrelated"))
    _write_package(
        package,
        proof_entry={"path": "witness-proof.json", "sha256": _sha256_text(proof_text)},
        proof_text=proof_text,
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["witness_proof"]["status"] == "SUBJECT_MISMATCH"
    assert "witness_proof_subject_mismatch:witness-proof.json" in result["conflicting_evidence"]
    assert result["checks"]["witness_proof_present"] is False


def test_witness_proof_ignores_unrelated_manifest_hash_field(tmp_path):
    package = tmp_path / "package"
    package.mkdir()
    unrelated_hash = _sha256_text("unrelated")
    proof_text = _witness_text(subject_sha256=unrelated_hash)
    _write_package(
        package,
        proof_entry={"path": "witness-proof.json", "sha256": _sha256_text(proof_text)},
        proof_text=proof_text,
        manifest_extra={"content_hash": unrelated_hash},
    )

    result = verify_verification_package(package)

    assert result["status"] == "INVALID"
    assert result["witness_proof"]["status"] == "SUBJECT_MISMATCH"
    assert "witness_proof_subject_mismatch:witness-proof.json" in result["conflicting_evidence"]


def test_verify_package_summary_prints_witness_status(tmp_path, capsys):
    package = tmp_path / "package"
    package.mkdir()
    proof_text = _witness_text()
    _write_package(
        package,
        proof_entry={"path": "witness-proof.json", "sha256": _sha256_text(proof_text)},
        proof_text=proof_text,
    )

    exit_code = main(["verify-package", str(package), "--summary"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "status: VERIFIED" in output
    assert "witness_proof: PRESENT" in output
    assert "truth_guarantee: false" in output
