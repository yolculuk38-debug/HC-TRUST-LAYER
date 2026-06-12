import hashlib
import json

from hc_trust.cli import main


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _write_manifest(package, files):
    (package / "manifest.json").write_text(
        json.dumps(
            {
                "package_id": "HC-PKG-CLI",
                "record_id": "HC-RECORD-CLI",
                "files": files,
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )


def test_verify_package_cli_returns_zero_for_verified_package(tmp_path, capsys):
    package = tmp_path / "package"
    artifact = package / "metadata" / "source-info.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_text("source-ok", encoding="utf-8")
    _write_manifest(
        package,
        [
            {
                "path": "metadata/source-info.json",
                "sha256": _sha256_text("source-ok"),
            }
        ],
    )

    exit_code = main(["verify-package", str(package)])
    output = json.loads(capsys.readouterr().out)

    assert exit_code == 0
    assert output["status"] == "VERIFIED"
    assert output["verified"] is True
    assert output["advisory_only"] is True
    assert output["public_safe"] is True
    assert output["truth_guarantee"] is False


def test_verify_package_cli_returns_one_for_invalid_package(tmp_path, capsys):
    package = tmp_path / "package"
    artifact = package / "metadata" / "source-info.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_text("changed", encoding="utf-8")
    _write_manifest(
        package,
        [
            {
                "path": "metadata/source-info.json",
                "sha256": _sha256_text("original"),
            }
        ],
    )

    exit_code = main(["verify-package", str(package)])
    output = json.loads(capsys.readouterr().out)

    assert exit_code == 1
    assert output["status"] == "INVALID"
    assert output["verified"] is False
    assert "sha256_mismatch:metadata/source-info.json" in output["conflicting_evidence"]
