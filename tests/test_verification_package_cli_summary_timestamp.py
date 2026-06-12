import hashlib
import json

from hc_trust.cli import main


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def test_verify_package_cli_summary_reports_present_timestamp_proof(tmp_path, capsys):
    package = tmp_path / "package"
    artifact = package / "metadata" / "source-info.json"
    proof = package / "timestamp-proof.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_text("source-ok", encoding="utf-8")
    proof_text = json.dumps(
        {
            "claimed_at": "2026-06-12T00:00:00Z",
            "subject_sha256": _sha256_text("source-ok"),
        },
        sort_keys=True,
    )
    proof.write_text(proof_text, encoding="utf-8")
    manifest = {
        "package_id": "HC-PKG-TIME-CLI",
        "record_id": "HC-RECORD-TIME-CLI",
        "files": [
            {
                "path": "metadata/source-info.json",
                "sha256": _sha256_text("source-ok"),
            }
        ],
        "timestamp_proof": {"path": "timestamp-proof.json", "sha256": _sha256_text(proof_text)},
    }
    (package / "manifest.json").write_text(json.dumps(manifest, sort_keys=True), encoding="utf-8")

    exit_code = main(["verify-package", str(package), "--summary"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "status: VERIFIED" in output
    assert "verified: true" in output
    assert "timestamp_proof: PRESENT" in output
    assert "truth_guarantee: false" in output
