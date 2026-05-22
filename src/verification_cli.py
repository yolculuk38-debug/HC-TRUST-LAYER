"""HC:// verification CLI foundation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from portable_package_v2 import validate_portable_package_v2
from provenance_integrity_scanner import scan_provenance_integrity
from schema_hardening import validate_hardened_package


CLI_VERSION = "HC-VERIFICATION-CLI-V1"


def load_json_file(path: str) -> dict[str, Any]:
    """Load a JSON file for CLI verification."""

    return json.loads(Path(path).read_text(encoding="utf-8"))


def verify_package_file(path: str) -> dict[str, Any]:
    """Verify a portable package file."""

    package = load_json_file(path)
    shape = validate_portable_package_v2(package)
    hardened = validate_hardened_package(package)

    return {
        "cli_version": CLI_VERSION,
        "package_shape": shape,
        "schema_hardening": hardened,
        "valid": bool(shape.get("valid")) and bool(hardened.get("valid")),
    }


def scan_provenance_file(path: str) -> dict[str, Any]:
    """Scan a provenance JSON file."""

    provenance = load_json_file(path)
    return {
        "cli_version": CLI_VERSION,
        "provenance_scan": scan_provenance_integrity(provenance),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="HC:// verification CLI")
    parser.add_argument("command", choices=["verify-package", "scan-provenance"])
    parser.add_argument("path")
    args = parser.parse_args()

    if args.command == "verify-package":
        result = verify_package_file(args.path)
    else:
        result = scan_provenance_file(args.path)

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()


__all__ = [
    "CLI_VERSION",
    "load_json_file",
    "verify_package_file",
    "scan_provenance_file",
]
