# Verification Package CLI and Python Quickstart

This quickstart demonstrates the implemented local HC verification package hash core.

It compares the bytes of package files listed by the local manifest with their declared SHA-256 digests and reports missing, conflicting, or out-of-bound inputs. It parses the manifest and optional proof JSON structures that the hash core reads, but treats other listed payload contents as opaque bytes; matching their hash does not validate their format or meaning. `VERIFIED` means these implemented package checks passed for this invocation. It does not authenticate the manifest author or prove legal truth, signer identity, witness authority, media provenance, an external timestamp, federation state, or production readiness. Consequential use still requires human-supervised validation.

## Example package

The repository includes a minimal sample package:

```text
examples/verification-package/valid/
├── issuer-proof.json
├── manifest.json
├── metadata/source-info.txt
└── time-evidence.json
```

The manifest lists the file path and expected SHA-256 digest for package evidence. It also references optional issuer proof evidence and local time-existence evidence.

The local directory manifest uses `schema_version: "HC-LOCAL-VERIFICATION-MANIFEST-V1"`, non-empty `package_id` and `record_id`, and a non-empty `files` array. Each file entry uses a canonical relative `path` and lowercase `sha256`; an optional `role` can be `payload`, `proof`, `metadata`, `documentation`, or `opaque`. Optional proof references use the same `path` and `sha256` shape. For example:

```json
{
  "schema_version": "HC-LOCAL-VERIFICATION-MANIFEST-V1",
  "package_id": "HC-PKG-EXAMPLE",
  "record_id": "HC-RECORD-EXAMPLE",
  "files": [
    {"path": "payload.bin", "sha256": "<64 lowercase hex characters>", "role": "payload"}
  ],
  "extensions": {"urn:example:label": "opaque metadata"}
}
```

The verifier inventories the package directory: every regular file other than the root `manifest.json` must appear in `files[]` or in a recognized issuer, timestamp, or witness proof reference. Duplicate JSON keys or paths, unknown fields, non-canonical paths, symlinks, and special filesystem objects make the package invalid. Empty directories do not affect the result. Extension values and unparsed payload bytes remain opaque.

## Run the verifier

Open the repository root with Python 3.14 or newer. In a Bash shell, create a virtual environment beside the checkout, activate it, and install the package:

```bash
python -m venv ../hc-trust-venv
source ../hc-trust-venv/bin/activate
python -m pip install .
```

Run the installed CLI on the sample directory from the same repository root:

```bash
hc-trust verify-package examples/verification-package/valid
```

For a valid package, the command returns exit code `0` and prints JSON with:

```json
{
  "status": "VERIFIED",
  "result_contract_version": "HC-LOCAL-VERIFICATION-RESULT-V1",
  "result_dimensions": {
    "integrity": "VERIFIED",
    "authentication": "NOT_PERFORMED",
    "identity_trust": "NOT_ESTABLISHED",
    "time": "NOT_AUTHENTICATED",
    "policy": "NOT_EVALUATED"
  },
  "human_final_authority": true,
  "verified": true,
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "checks": {
    "manifest_files_checked": 1,
    "sha256_only": true,
    "issuer_identity_verified": false,
    "external_timestamp_verified": false,
    "signatures_verified": false,
    "witnesses_verified": false
  },
  "issuer_proof": {
    "status": "PRESENT",
    "issuer": "HC-SAMPLE-ISSUER"
  },
  "timestamp_proof": {
    "status": "PRESENT",
    "external_verified": false
  }
}
```

`issuer_proof.status: PRESENT` and `timestamp_proof.status: PRESENT` describe included files that were locally parsed and matched against the manifest. They do not mean issuer identity or an external clock was verified. The CLI can return exit code `0` while those stronger checks remain false.

## Run the operator summary

For a shorter human-readable view:

```bash
hc-trust verify-package examples/verification-package/valid --summary
```

Expected summary fields include:

```text
HC verification package summary
result_contract_version: HC-LOCAL-VERIFICATION-RESULT-V1
integrity: VERIFIED
authentication: NOT_PERFORMED
identity_trust: NOT_ESTABLISHED
time: NOT_AUTHENTICATED
policy: NOT_EVALUATED
human_final_authority: true
status: VERIFIED
verified: true
files_checked: 1
issuer_proof: PRESENT
timestamp_proof: PRESENT
advisory_only: true
public_safe: true
truth_guarantee: false
```

Exit code `0` is scoped to a `VERIFIED` local package-integrity result; exit code `1` is returned for `INVALID` or `REVIEW_REQUIRED`. The `human_review_required: false` field means this hash-core response did not flag the package as incomplete or conflicting. It does not remove human review for consequential interpretation.

SDK and JSON consumers can select the result contract using `result_contract_version`; `schema_version` identifies the input manifest. The legacy `status` field is the value of `result_dimensions.integrity`. For example, a manifest may match the bytes of a signed invoice, while the signer and the time of signing both remain unverified.

## Try a changed file

Copy the sample to a temporary directory and change one file in the copy:

```bash
scratch_dir=$(mktemp -d)
cp -R examples/verification-package/valid "$scratch_dir/package"
printf '\nchanged copy\n' >> "$scratch_dir/package/metadata/source-info.txt"
exit_code=0
hc-trust verify-package "$scratch_dir/package" --summary || exit_code=$?
printf 'Exit code: %s\n' "$exit_code"
```

The summary reports `integrity: INVALID` and `sha256_mismatch:metadata/source-info.txt`. The command exits with code `1`.

## Use the Python SDK

Run this from the repository root in the same environment. The SDK takes a
directory path and returns a dictionary with the same fields as the CLI JSON:

```python
from pathlib import Path

from hc_trust.verification_package import verify_verification_package

package = Path("examples/verification-package/valid")
result = verify_verification_package(package)
print(result["result_contract_version"])
print(result["result_dimensions"]["integrity"])
print(result["result_dimensions"]["authentication"])
```

The included example prints `HC-LOCAL-VERIFICATION-RESULT-V1`, `VERIFIED`, and
`NOT_PERFORMED` on separate lines.

## Inspect the signature/witness fixture package

A second non-canonical example package is available at:

```text
examples/verification-package/signature-witness-fixture/
```

Run the full JSON verifier output for this fixture package:

```bash
hc-trust verify-package examples/verification-package/signature-witness-fixture
```

This package demonstrates local fixture files for `signature-proof.json` and `witness-proof.json` without granting new verification authority. In the full JSON output, inspect the fixture-related checks for the expected boundary:

```text
advisory_only: true
public_safe: true
truth_guarantee: false
checks.signatures_verified: false
checks.witnesses_verified: false
```

Use `--summary` only when you need the shorter operator summary fields; the fixture-specific signature and witness check keys are visible in the full JSON output.

If a listed file is missing, its bytes do not match the declared digest, or its path is outside the package boundary, the command returns non-zero and reports `missing_evidence` or `conflicting_evidence`. Malformed manifest or parsed proof JSON also fails; other listed payload content is not parsed, so malformed payload bytes can still match their declared digest.

## What this proves

This shows only that the manifest-listed local files match their declared SHA-256 digests and that any optional issuer, local-time, or witness fixture file included in the package was present, well-formed for this local parser, and internally bound as described. These files and their declarations are not authenticated by an external issuer, timestamp service, or witness authority.

## What this does not prove

This does not verify:

- legal truth;
- identity;
- witness authority;
- QR authenticity;
- media provenance;
- external timestamp authority;
- signing validity;
- federation state;
- production readiness.

Those are later layers.
