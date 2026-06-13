# Witness Capability Boundary Status

Status: advisory checkpoint.

The current verification-package core supports one local `witness_proof` entry.

## Current behavior

The local verifier checks one manifest-listed witness proof file for local file presence, SHA-256 match, JSON readability, required local fields, and subject hash binding to local package evidence.

## Boundary

- `witness_proof.status=PRESENT` means one local witness proof file is present and structurally valid.
- It does not mean multiple witnesses were checked.
- It does not mean witness authority is verified.
- `checks.witnesses_verified=false` remains required.
- `truth_guarantee=false` remains required.

## Future work gate

Multi-witness support needs a separate explicit PR that defines the manifest shape, output contract, CLI summary behavior, regression tests, and advisory-only boundary.
