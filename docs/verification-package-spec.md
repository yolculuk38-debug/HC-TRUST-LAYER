# Verification Package Specification

## Purpose

This document defines the baseline package architecture for exporting and validating HC-TRUST-LAYER verification data. The package is designed for portable verification, deterministic integrity checks, and replay-resistant workflows.

## Scope and Principles

- Modular package layout for incremental verifier implementation.
- Deterministic structure for archive portability.
- Backward-compatible evolution using additive metadata.
- Production-oriented verification behavior.

## Package Structure

A verification package should contain the following top-level entries:

- `manifest.json`
- `signatures/`
- `witness/`
- `revision/`
- `hashes/`
- `metadata/`

Example layout:

```text
verification-package/
  manifest.json
  signatures/
    record.sig
    revision.sig
  witness/
    witness-index.json
    attestations.json
  revision/
    revision-head.json
    revision-chain.json
  hashes/
    content.sha256
    package.sha256
  metadata/
    export-info.json
    source-info.json
```

## Component Definitions

### `manifest.json`

The manifest is the canonical package index and must include:

- package identifier and schema version
- record identifier
- revision identifier (or revision head reference)
- file inventory with relative paths and expected digests
- export timestamp
- issuer/exporter identity reference
- replay-protection nonce or export sequence value

### `signatures/`

Contains detached signatures over required package artifacts.

Recommended minimum:

- signature over `manifest.json`
- signature over revision head material
- signature metadata describing algorithm and key identifier

### `witness/`

Contains witness-related evidence used for trust evaluation.

Expected content:

- witness index (witness IDs and participation references)
- attestation list with revision associations
- optional witness policy evaluation outputs

### `revision/`

Contains revision graph artifacts required to verify authoritative state.

Expected content:

- revision head record
- revision chain history or checkpoints
- state markers for superseded/disputed/revoked transitions

### `hashes/`

Contains deterministic digest material for package and payload validation.

Expected content:

- content digests for included artifacts
- package-level digest over canonical file ordering
- optional digest algorithm registry for multi-hash compatibility

### `metadata/`

Contains operational metadata that does not override cryptographic truth.

Expected content:

- export tooling/version details
- source environment identifiers
- federation source references (if applicable)
- compatibility hints for consumers

## Export Package Behavior

1. Resolver selects target record and authoritative revision head.
2. Exporter gathers required signatures, witness attestations, revision artifacts, and metadata.
3. Exporter generates `manifest.json` with deterministic file inventory.
4. Exporter computes package digests and writes `hashes/` entries.
5. Exporter signs required artifacts and writes `signatures/`.
6. Exporter emits package as deterministic archive (or directory format with canonical ordering contract).

## Verification Package Integrity Rules

A package is valid only when all required checks pass:

- every manifest-listed file exists and matches its expected digest
- manifest signature verifies against allowed key policy
- revision head and chain are internally consistent
- witness attestations resolve to declared revisions
- package-level digest matches canonical file ordering
- required metadata fields are present for traceability

Failure in any required check should produce a non-verified state (`suspicious`, `disputed`, `revoked`, or `unavailable`) based on policy mapping.

## Replay Protection Notes

Verification packages should include replay controls to prevent stale or context-swapped reuse.

Recommended controls:

- package nonce or monotonic export sequence in `manifest.json`
- export timestamp with verifier freshness policy thresholds
- source binding fields (origin identifier, federation source marker)
- optional audience/context binding for institution-specific workflows

Verifier behavior:

- detect duplicate nonce/sequence where storage permits
- flag freshness violations as `suspicious` or `unavailable` per policy
- reject packages with inconsistent source binding relative to requested context

## Backward Compatibility and Evolution

- Add new optional fields via schema-versioned manifest extension.
- Avoid renaming existing required fields in place.
- Treat top-level directory names as stable public contract.
- Support additive hash/signature algorithms without removing prior accepted algorithms immediately.

## Future Compatibility Targets

The package architecture should support adapters for:

- browser extension verification import
- mobile verification package ingestion
- C2PA bridge packaging/mapping
- external API handoff payloads
- institutional audit pipelines
- social platform proof surfaces

All adapters should preserve manifest-first verification semantics and must not bypass integrity or witness validation steps.
