# Verification Package CLI Quickstart

This quickstart demonstrates the implemented local HC verification package hash core.

It compares package files listed by the local manifest with their declared SHA-256 digests and reports missing, conflicting, or malformed inputs. `VERIFIED` means these implemented package checks passed for this invocation. It does not authenticate the manifest author or prove legal truth, signer identity, witness authority, media provenance, an external timestamp, federation state, or production readiness. Consequential use still requires human-supervised validation.

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

## Run the verifier

From a Python 3.14+ repository checkout, install the package once and run the included example from the repository root:

```bash
python -m pip install .
hc-trust verify-package examples/verification-package/valid
```

For a valid package, the command returns exit code `0` and prints JSON with:

```json
{
  "status": "VERIFIED",
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

If a listed file is missing, changed, malformed, or outside the package boundary, the command returns non-zero and reports `missing_evidence` or `conflicting_evidence`.

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
