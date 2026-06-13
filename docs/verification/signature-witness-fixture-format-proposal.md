# Signature and Witness Fixture Format Proposal

Status: proposal only.
Scope: documentation-only fixture planning for HC:// verification packages.

## Current repository evidence

The repository already has a local `witness_proof` slice in the verification package core. It checks a manifest-listed witness proof file, validates local SHA-256 integrity, parses minimal JSON fields, binds `subject_sha256` to local package evidence, and reports advisory output without verifying witness authority or cryptographic signatures.

The repository does not currently define or implement a `signature_proof` fixture layer. This proposal records a narrow future fixture shape before any protected implementation work.

## Boundaries

This proposal does not change schemas, validators, signing logic, federation logic, policy files, canonical records, runtime code, generated artifacts, records, or GitHub Actions.

The fixture format must preserve:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- human final authority

It must not claim legal truth, identity finality, witness authority, production readiness, forensic certainty, or autonomous governance authority.

## Proposed manifest entries

```json
{
  "signature_proof": {
    "path": "signature-proof.json",
    "sha256": "..."
  },
  "witness_proof": {
    "path": "witness-proof.json",
    "sha256": "..."
  }
}
```

`witness_proof` already exists as a local advisory slice. `signature_proof` is future-facing and should remain proposal-only until explicitly implemented in a small, test-backed PR.

## Proposed `signature-proof.json`

```json
{
  "signer_id": "HC-SIGNER-SAMPLE",
  "statement": "sample package signed",
  "subject_sha256": "...",
  "signature_algorithm": "UNVERIFIED_LOCAL_FIXTURE",
  "signature_value": "UNVERIFIED_PLACEHOLDER"
}
```

Initial handling should treat this as local fixture evidence only. A digest-valid signature proof may be reported as `PRESENT` or `UNVERIFIED_SIGNATURE` only after subject binding is explicit. It must not report cryptographic verification until a separate signing implementation exists.

## Existing `witness-proof.json` shape

```json
{
  "witness_id": "HC-WITNESS-SAMPLE",
  "statement": "sample package witnessed",
  "subject_sha256": "..."
}
```

The witness proof must remain bound to local package evidence through `subject_sha256`. If the witness points to a different subject, the result must remain a mismatch state rather than present evidence for the current package.

## Suggested local states

- `NOT_PROVIDED`
- `PRESENT`
- `MISSING`
- `MISMATCH`
- `INVALID`
- `SUBJECT_MISMATCH`
- `UNVERIFIED_SIGNATURE`

## Safe next step

The next implementation step, if explicitly authorized, should be limited to a docs/test/sample PR that adds a non-canonical example package for `signature_proof` and `witness_proof` fixture shapes. It should not touch protected paths or claim real signature, identity, witness, C2PA, OpenTimestamps, W3C VC, federation, or production verification.
