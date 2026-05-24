# HC-TRUST-LAYER Master Architecture

## Purpose

This document defines a protocol-first architecture baseline for HC-TRUST-LAYER based on the current strategy analysis.

HC-TRUST-LAYER is the primary project name. Humanity Chain is referenced only as historical origin context.

## Scope and Limitations

- This architecture describes verification of provenance and integrity signals.
- Verification output supports integrity verification and provenance verification; it does not establish objective truth.
- Some layers are currently implemented, while others remain partial, planned, or research.
- This document is a technical foundation, not a commitment of commercial rollout.

## Six Core Layers

### 1) Record Integrity Layer

Defines canonical record structure and deterministic integrity checks.

Core responsibilities:
- stable record identifiers
- canonical payload structure
- deterministic hashing rules
- tamper-evident change tracking

Expected output:
- reproducible pass/fail integrity results for the same record inputs.

### 2) Witness & Signature Layer

Provides cryptographic or procedural witness attribution around records.

Core responsibilities:
- witness metadata binding
- signature attachment and verification workflows
- witness identity context and auditability
- signer/witness revocation handling

Expected output:
- transparent evidence trail showing who attested, when, and under which rules.

### 3) Public Verification Layer

Exposes open verification paths for independent reviewers.

Core responsibilities:
- public verification endpoint and CLI pathways
- machine-readable verification output
- human-readable verification summary and status indicators
- reproducible checks for third parties

Expected output:
- independent parties can verify a record using the same public rules.

### 4) Federation & Sync Layer

Supports interoperability and synchronization across multiple nodes or repositories.

Core responsibilities:
- sync semantics for shared records
- conflict handling and convergence policy
- minimal federation metadata and node trust context
- continuity across mirrors and public repositories

Expected output:
- consistent verification records across federated environments.

### 5) External Integration Layer

Defines interfaces for ecosystem-level verification integrations.

Core responsibilities:
- URL/content linkage validation inputs
- API-based verification exchange
- packaging model for external distribution environments
- compatibility boundaries for institutional integration

Expected output:
- external systems can consume and produce verification artifacts with clear protocol contracts.

### 6) Governance & Dispute Layer

Sets policy boundaries for disputes, appeals, and operational governance.

Core responsibilities:
- dispute intake and triage workflows
- correction, revocation, and supersession rules
- governance role definitions and decision logging
- policy transparency and review traces

Expected output:
- documented, reviewable governance outcomes for contested records.

## Content Trust Badge Model

Badge states:
- `verified`
- `suspicious`
- `unverified`
- `disputed`
- `revoked`
- `superseded`

Interpretation principles:
- Badges express verification status under HC-TRUST-LAYER protocol rules.
- Badges verify provenance and integrity signals, not final truth claims.
- Badge results are time-bound and may change with new evidence, policy updates, or superseding records.

## External Ecosystem Roadmap

Planned integration paths:
- social media URL verification
- browser extension for public checks
- public verification API for third-party applications
- government/institution API adapters
- media/content hash packages for distribution pipelines
- verification receipts for machine and human audit trails

Roadmap note:
- These items define direction only; implementation timing and adoption are not guaranteed.

## Archival Resilience Model

Archival assumptions and controls:
- GitHub is important but not sufficient as a single archival dependency.
- Repositories should be mirrored across independent hosts where possible.
- Snapshot preservation through the Internet Archive should be included when practical.
- Future support should evaluate IPFS and Arweave publication paths.
- Local clone strategy should be maintained for continuity and independent re-verification.
- Timestamp preservation (commit timestamps, release tags, signed artifacts where available) should be retained as evidence context.

Resilience goal:
- reduce single-point archival failure and preserve long-term verification reproducibility.

## Business and Model Boundaries

Current model boundaries:
- protocol-first verification infrastructure comes before commercialization.
- future optional paid verification receipts/packages may be evaluated.
- no financial promise is made in this architecture.
- no guarantee of institutional adoption is made in this architecture.

## Implementation Status

| Layer | Current status | Notes |
|---|---|---|
| Record Integrity Layer | implemented | Core hash, record validation, and deterministic verification logic are active in repository workflows. |
| Witness & Signature Layer | partial | Witness and signature capabilities exist in evolving form and are under active refinement. |
| Public Verification Layer | implemented | Public verification documentation, CLI flow, and status surfaces are available. |
| Federation & Sync Layer | planned | Federation specifications exist; broader sync behavior and production hardening are pending. |
| External Integration Layer | research | External ecosystem adapters and API-facing package standards are in exploratory phase. |
| Governance & Dispute Layer | planned | Governance and dispute framework documents exist, with operational mechanics still being formalized. |

Status scale reference:
- implemented
- partial
- planned
- research

## Implementation Map

For a file-level layer mapping and gap-oriented priority plan, see [`implementation-map.md`](implementation-map.md).

For cross-capability status across implemented, partial, planned, research, and not implemented items, see [`capability-status.md`](capability-status.md).

For the verification package draft format and non-canonical transport boundary, see [`verification-package-format.md`](verification-package-format.md).

For AI-assisted governance contribution flow and authority boundaries, see [`ai-collaboration-workflow.md`](ai-collaboration-workflow.md).
