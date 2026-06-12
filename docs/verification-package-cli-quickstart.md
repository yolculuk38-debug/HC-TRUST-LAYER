# Verification Package CLI Quickstart

This quickstart demonstrates the local HC verification package hash core.

It is local-only and advisory-only. It checks package integrity; it does not prove legal truth, identity, witness authority, media provenance, timestamp attestations, federation state, or production readiness.

## Example package

The repository includes a minimal sample package:

```text
examples/verification-package/valid/
├── manifest.json
└── metadata/source-info.txt
```

The manifest lists the file path and expected SHA-256 digest.

## Run the verifier

From the repository root:

```bash
hc-trust verify-package examples/verification-package/valid
```

For a valid package, the command returns exit code `0` and prints JSON with:

```json
{
  "status": "VERIFIED",
  "verified": true,
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false
}
```

If a listed file is missing, changed, malformed, or outside the package boundary, the command returns non-zero and reports `missing_evidence` or `conflicting_evidence`.

## What this proves

This proves only that the local files still match the manifest SHA-256 digest.

## What this does not prove

This does not verify:

- legal truth;
- identity;
- witness authority;
- QR authenticity;
- media provenance;
- timestamp attestations;
- federation state;
- production readiness.

Those are later layers.
