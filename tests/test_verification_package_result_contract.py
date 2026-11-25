import hashlib
import json
from pathlib import Path
import shutil

import pytest

from hc_trust.cli import main
from hc_trust.verification_package import verify_verification_package


@pytest.mark.parametrize(
    "scenario,integrity",
    [
        ("issuer-and-time", "VERIFIED"),
        ("witness-and-opaque-signature", "VERIFIED"),
        ("no-proofs", "VERIFIED"),
        ("changed-payload", "INVALID"),
        ("malformed-proof-with-matching-hash", "INVALID"),
        ("missing-package", "INVALID"),
    ],
)
def test_local_result_agrees_across_sdk_json_and_summary(tmp_path, capsys, scenario, integrity):
    package = tmp_path / "package"
    if scenario != "missing-package":
        fixture = "signature-witness-fixture" if scenario == "witness-and-opaque-signature" else "valid"
        shutil.copytree(Path("examples/verification-package") / fixture, package)
        manifest_path = package / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if scenario == "no-proofs":
            for key in ("issuer_proof", "timestamp_proof"):
                (package / manifest.pop(key)["path"]).unlink()
        elif scenario == "changed-payload":
            (package / manifest["files"][0]["path"]).write_bytes(b"changed")
        elif scenario == "malformed-proof-with-matching-hash":
            proof = manifest["issuer_proof"]
            (package / proof["path"]).write_bytes(b"{}")
            proof["sha256"] = hashlib.sha256(b"{}").hexdigest()
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    sdk = verify_verification_package(package)
    assert sdk["result_contract_version"] == "HC-LOCAL-VERIFICATION-RESULT-V1"
    assert sdk["result_dimensions"] == {
        "integrity": integrity,
        "authentication": "NOT_PERFORMED",
        "identity_trust": "NOT_ESTABLISHED",
        "time": "NOT_AUTHENTICATED",
        "policy": "NOT_EVALUATED",
    }
    assert sdk["human_final_authority"] is True
    assert sdk["truth_guarantee"] is False
    assert sdk["status"] == integrity
    assert sdk["verified"] is (integrity == "VERIFIED")
    if scenario == "issuer-and-time":
        assert sdk["issuer_proof"]["status"] == sdk["timestamp_proof"]["status"] == "PRESENT"
    if scenario == "witness-and-opaque-signature":
        assert sdk["witness_proof"]["status"] == "PRESENT"
        assert sdk["checks"]["signatures_verified"] is False
    expected_exit = 0 if sdk["verified"] else 1
    assert main(["verify-package", str(package)]) == expected_exit
    assert json.loads(capsys.readouterr().out) == sdk
    assert main(["verify-package", str(package), "--summary"]) == expected_exit
    lines = capsys.readouterr().out.splitlines()
    assert "human_final_authority: true" in lines
    assert f"result_contract_version: {sdk['result_contract_version']}" in lines
    for name, value in sdk["result_dimensions"].items():
        assert f"{name}: {value}" in lines
