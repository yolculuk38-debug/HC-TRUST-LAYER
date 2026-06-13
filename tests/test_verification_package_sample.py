import json
from pathlib import Path

from hc_trust.verification_package import verify_verification_package


def test_sample_verification_package_is_verified():
    package_path = Path("examples/verification-package/valid")

    result = verify_verification_package(package_path)

    assert result["status"] == "VERIFIED"
    assert result["verified"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is False
    assert result["checks"]["issuer_proof_checked"] is True
    assert result["checks"]["issuer_proof_present"] is True
    assert result["issuer_proof"]["status"] == "PRESENT"
    assert result["issuer_proof"]["issuer"] == "HC-SAMPLE-ISSUER"
    assert result["issuer_proof"]["statement"] == "sample package issued"
    assert result["checks"]["timestamp_proof_checked"] is True
    assert result["checks"]["timestamp_proof_present"] is True
    assert result["checks"]["external_timestamp_verified"] is False
    assert result["timestamp_proof"]["status"] == "PRESENT"
    assert result["timestamp_proof"]["claimed_at"] == "2026-06-12T00:00:00Z"
    assert result["timestamp_proof"]["subject_sha256"] == "4994673c753f193e845060f0ed8a3785c9293443584b8f1d192d6d17c44a5f71"
    assert result["files"] == [
        {
            "path": "metadata/source-info.txt",
            "status": "MATCH",
            "expected_sha256": "4994673c753f193e845060f0ed8a3785c9293443584b8f1d192d6d17c44a5f71",
            "actual_sha256": "4994673c753f193e845060f0ed8a3785c9293443584b8f1d192d6d17c44a5f71",
        }
    ]


def test_signature_witness_fixture_package_is_local_only_and_advisory():
    package_path = Path("examples/verification-package/signature-witness-fixture")
    manifest = json.loads((package_path / "manifest.json").read_text(encoding="utf-8"))

    result = verify_verification_package(package_path)

    assert manifest["signature_proof"] == {
        "path": "signature-proof.json",
        "sha256": "622ddaba8d79249b9f85ed9310b0e86aad654fc6212606755b300a8d1d6b3d2c",
    }
    assert result["status"] == "VERIFIED"
    assert result["verified"] is True
    assert result["advisory_only"] is True
    assert result["public_safe"] is True
    assert result["truth_guarantee"] is False
    assert result["human_review_required"] is False
    assert result["checks"]["signatures_verified"] is False
    assert result["checks"]["witnesses_verified"] is False
    assert result["checks"]["witness_proof_checked"] is True
    assert result["checks"]["witness_proof_present"] is True
    assert result["witness_proof"]["status"] == "PRESENT"
    assert result["witness_proof"]["witness_id"] == "HC-WITNESS-SAMPLE"
    assert result["witness_proof"]["subject_sha256"] == "219be39a3ef201d61c23b11f91a69bc4f0793291aa2405347fab3a4534a60046"
    assert result["files"] == [
        {
            "path": "metadata/source-info.txt",
            "status": "MATCH",
            "expected_sha256": "219be39a3ef201d61c23b11f91a69bc4f0793291aa2405347fab3a4534a60046",
            "actual_sha256": "219be39a3ef201d61c23b11f91a69bc4f0793291aa2405347fab3a4534a60046",
        },
        {
            "path": "signature-proof.json",
            "status": "MATCH",
            "expected_sha256": "622ddaba8d79249b9f85ed9310b0e86aad654fc6212606755b300a8d1d6b3d2c",
            "actual_sha256": "622ddaba8d79249b9f85ed9310b0e86aad654fc6212606755b300a8d1d6b3d2c",
        },
    ]
