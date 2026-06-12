# Verification Next Layer Proposal

Status: advisory proposal only  
Scope: planning before implementation

## Current working core

The current working core verifies local package integrity:

- `manifest.json` exists and is readable;
- listed files exist;
- listed SHA-256 digests match actual files;
- missing evidence and conflicting evidence are reported;
- `hc-trust verify-package <package_path>` provides a local CLI entry point;
- a minimal sample package and quickstart exist.

This proves local file-to-manifest integrity only.

## Recommended next layer

Recommended next layer: package issuer proof planning before implementation.

Why this comes next:

- It builds on the existing package manifest.
- It can remain local and advisory.
- It does not require changing workflows, schemas, validators, or records first.
- It prepares the package boundary for later QR, timestamp, media, and network references.

## Proposed first implementation slice, later PR

A later implementation PR should be small:

- define a minimal issuer proof file shape;
- report whether issuer proof checking was attempted;
- keep `truth_guarantee=false`;
- keep human review authority;
- add tests for present, missing, malformed, and mismatching proof evidence.

## Files that should remain untouched in the first slice

Do not touch these in the first implementation slice unless a separate approval exists:

- `.github/workflows/**`
- `schema/**`
- `validators/**`
- `records/**`
- `generated/**`
- `policy/**`
- `federation/**`

## Safe next action

Open an implementation PR only after this proposal is reviewed. The first implementation should remain local-only, advisory-only, public-safe, and test-backed.
