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
    assert result["files"] == [
        {
            "path": "metadata/source-info.txt",
            "status": "MATCH",
            "expected_sha256": "4994673c753f193e845060f0ed8a3785c9293443584b8f1d192d6d17c44a5f71",
            "actual_sha256": "4994673c753f193e845060f0ed8a3785c9293443584b8f1d192d6d17c44a5f71",
        }
    ]
