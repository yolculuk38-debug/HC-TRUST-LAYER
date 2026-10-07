"""Exercise an installed wheel outside the checkout; write success evidence last."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wheel", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()
    require(bool(re.fullmatch(r"[0-9a-f]{40}", args.source_commit)), "A full source commit SHA is required")
    require(sys.flags.isolated == 1, "Run the installed interpreter with -I")
    require(sys.prefix != sys.base_prefix, "A dedicated virtual environment is required")
    source_root = Path(__file__).resolve().parents[1]
    require(not Path.cwd().resolve().is_relative_to(source_root), "Run outside the checkout")
    wheel = args.wheel.resolve(strict=True)
    require(wheel.suffix == ".whl", "A wheel artifact is required")
    wheel_sha256 = hashlib.sha256(wheel.read_bytes()).hexdigest()
    distribution = importlib.metadata.distribution("hc-trust-layer")
    direct_url = json.loads(distribution.read_text("direct_url.json") or "{}")
    require(
        direct_url.get("archive_info", {}).get("hashes", {}).get("sha256") == wheel_sha256,
        "Installed distribution does not match the supplied wheel SHA-256",
    )

    import hc_trust
    import hc_runtime
    from hc_runtime.app import create_app
    from hc_trust.verification import DEFAULT_RECORD_SCHEMA_PATH, validate_record, verify_record_hash
    from hc_trust.verification_package import verify_verification_package

    prefix = Path(sys.prefix).resolve()
    for module in (hc_trust, hc_runtime):
        require(Path(module.__file__).resolve().is_relative_to(prefix), "Import escaped the installed environment")
    schema_path = Path(DEFAULT_RECORD_SCHEMA_PATH).resolve(strict=True)
    require(schema_path.is_relative_to(prefix), "Schema was loaded from outside the installation")
    require(create_app().title == "HC:// Reference Runtime", "Installed runtime app import failed")
    console = Path(sys.executable).parent / ("hc-trust.exe" if os.name == "nt" else "hc-trust")
    require(console.is_file(), "Installed console entry point is missing")
    env = {key: value for key, value in os.environ.items() if key not in {"PYTHONPATH", "PYTHONHOME"}}
    checks: list[str] = ["installed_archive_hash_binding", "installed_runtime_import"]

    with tempfile.TemporaryDirectory(prefix="hc-installed-smoke-") as temporary:
        cwd = Path(temporary)

        def run_cli(arguments: list[str], expected: int = 0) -> str:
            completed = subprocess.run(
                [str(console), *arguments], cwd=cwd, env=env,
                capture_output=True, text=True, timeout=30, check=False,
            )
            require(completed.returncode == expected, f"CLI exit mismatch for {arguments}: {completed.stderr}")
            return completed.stdout

        require("verify-package" in run_cli(["--help"]), "Installed CLI help is incomplete")
        checks.append("installed_console_help")
        record_path = cwd / "records/pending/HC-INSTALL-2026-0001.json"
        record_path.parent.mkdir(parents=True)
        content = "Installed distribution integrity smoke"
        record = {
            "schema_version": "hc-record-v1", "record_id": "HC-INSTALL-2026-0001",
            "created_at": "2026-10-07T00:00:00Z", "title": "Installed wheel smoke",
            "record_type": "protocol_note", "witness_type": "human", "author": "test fixture",
            "content": content, "content_hash": hashlib.sha256(content.encode()).hexdigest(),
            "content_hash_profile": "hc-content-sha256-v2", "archive_ref": "pending_archive",
            "verification_status": "draft",
        }
        record_path.write_text(json.dumps(record), encoding="utf-8")
        require(validate_record(record_path)[0], "Installed record schema rejected a valid record")
        require(verify_record_hash(record_path)[0], "Installed record hash check failed")
        run_cli(["validate-records", str(record_path)])
        run_cli(["verify", str(record_path)])
        record["created_at"] = "invalid"
        record_path.write_text(json.dumps(record), encoding="utf-8")
        run_cli(["validate-records", str(record_path)], expected=1)
        checks.append("installed_schema_and_record_negative_path")

        package = cwd / "package"
        package.mkdir()
        evidence = package / "evidence.bin"
        evidence.write_bytes(b"Actual local evidence bytes\x00\xff\n")
        manifest = {
            "package_id": "HC-INSTALL-PACKAGE", "record_id": "HC-INSTALL-2026-0001",
            "schema_version": "verification-package-sample-v1",
            "files": [{"path": "evidence.bin", "sha256": hashlib.sha256(evidence.read_bytes()).hexdigest()}],
        }
        (package / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        sdk = verify_verification_package(package)
        result = json.loads(run_cli(["verify-package", str(package)]))
        require(result == sdk and result["status"] == "VERIFIED", "Installed SDK/CLI integrity result differs")
        require(result["checks"]["signatures_verified"] is False, "File integrity must not grant signature authority")
        require(result["truth_guarantee"] is False, "File integrity must not grant truth authority")
        require("status: VERIFIED" in run_cli(["verify-package", str(package), "--summary"]), "Summary output failed")
        checks.append("real_file_package_sdk_json_summary")

        evidence.write_bytes(b"tampered")
        result = json.loads(run_cli(["verify-package", str(package)], expected=1))
        require(result["verified"] is False and result["status"] == "INVALID", "Tampered evidence was accepted")
        evidence.unlink()
        result = json.loads(run_cli(["verify-package", str(package)], expected=1))
        require(result["verified"] is False and result["status"] == "INVALID", "Missing evidence was accepted")
        checks.append("tampered_and_missing_file_exit_codes")

    report = {
        "report_version": 1, "status": "passed", "source_commit": args.source_commit,
        "wheel_filename": wheel.name, "wheel_sha256": wheel_sha256,
        "distribution_version": distribution.version, "python_version": sys.version.split()[0],
        "checks": checks, "isolated_interpreter": True, "outside_checkout": True,
        "advisory_only": True, "truth_guarantee": False,
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
