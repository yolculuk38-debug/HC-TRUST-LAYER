# Public Verification Routing

## Purpose

This document defines a stable public verification routing model for HC-TRUST-LAYER. It specifies canonical URL patterns, expected user flows, response state semantics, and explorer lookup behavior. The goal is consistent verification infrastructure that can be implemented incrementally without breaking existing records.

## Scope and Design Principles

- Modular routing that supports multiple clients (web, API, future mobile).
- Backward-compatible URL behavior for existing verification links.
- Deterministic lookup paths for record, revision, and witness verification.
- Production-oriented architecture language (no marketing semantics).

## Canonical Verification URL Patterns

The following patterns are canonical and should be treated as stable public entry points:

- `/verify/{record_id}`
- `/trust/{record_id}`
- `/history/{record_id}`
- `/revision/{record_id}`
- `/witness/{witness_id}`

### URL Pattern Semantics

- `/verify/{record_id}`: Primary public verification route for record integrity and trust state.
- `/trust/{record_id}`: Trust-focused view for the same record (trust score, witness coverage, disputes).
- `/history/{record_id}`: Record-level revision history and state transitions.
- `/revision/{record_id}`: Direct resolution to the currently active revision context for a record.
- `/witness/{witness_id}`: Witness identity, signature material status, and relation coverage.

### Examples

- `/verify/rec_01JX9W4C9G2A5M6Q8R7S`
- `/trust/rec_01JX9W4C9G2A5M6Q8R7S`
- `/history/rec_01JX9W4C9G2A5M6Q8R7S`
- `/revision/rec_01JX9W4C9G2A5M6Q8R7S`
- `/witness/wit_01JX9WJVV83A2KFQYZE4`

## Public Verification Flow

1. Client resolves `/verify/{record_id}`.
2. Resolver fetches canonical record metadata and latest accepted revision pointer.
3. Verification engine checks integrity hashes, signature chains, and witness attestations.
4. Dispute and revocation overlays are applied.
5. Public response model is returned with a final trust state and supporting metrics.

### Response Model States

Public verification must return one of the following states:

- `verified`: record integrity and required witness constraints are satisfied.
- `suspicious`: validation succeeded but anomaly conditions exist (for example, weak witness diversity or timing anomalies).
- `disputed`: an active dispute process exists for this record or revision.
- `revoked`: record or revision has been revoked by a valid governance path.
- `superseded`: record exists but an updated revision is now authoritative.
- `unavailable`: record cannot be resolved or verified due to missing/invalid data sources.

### Required Response Fields

- `trust_score`: normalized trust signal used for ranking and display.
- `witness_count`: number of accepted witness attestations contributing to state.
- `verification_timestamp`: timestamp of this verification result.
- `revision_state`: current revision status (active, archived, superseded).
- `provenance_state`: provenance graph completeness/consistency state.

## QR Verification Flow

1. QR payload encodes a canonical route (preferred: `/verify/{record_id}`).
2. Scanner resolves route and extracts record identifier.
3. Resolver executes the same verification pipeline as direct URL access.
4. Client displays verification state plus provenance and witness summary.

Routing requirement: QR verification must not use a separate trust-state algorithm; only transport and route acquisition differ.

## Explorer Lookup Flow

Explorer routes should map to the same canonical verification backend while supporting search and graph views.

### Search Behavior

- Accept record IDs, witness IDs, and known aliases.
- Normalize identifiers before lookup.
- Return deterministic redirect to canonical route when an exact match exists.

### Trust Lookup

- Use the same trust-state computation as `/trust/{record_id}`.
- Include trust score and witness count in result summaries.

### Provenance Graph Lookup

- Resolve record lineage, revision ancestry, and witness linkage edges.
- Flag missing or inconsistent graph segments in `provenance_state`.

### Federation Source Lookup

- Resolve whether verification evidence came from local node, federation peer, or both.
- Surface source availability/freshness constraints when producing final state.

### Witness Relation Lookup

- Show which witnesses attest to which revisions.
- Mark witness attestations excluded by policy or invalid signature checks.

## Revision Lookup Flow

1. Client resolves `/history/{record_id}` for full timeline or `/revision/{record_id}` for current revision resolution.
2. Resolver retrieves revision chain and canonical head.
3. Each revision is evaluated for integrity and policy status.
4. Output labels revision states (active, superseded, disputed, revoked, archived).

## Witness Verification Flow

1. Client resolves `/witness/{witness_id}`.
2. Resolver fetches witness profile, cryptographic key references, and attestation participation.
3. System validates witness signatures against referenced revisions.
4. Output includes relation summary and policy status flags.

## Verification Lifecycle Reference

The verification lifecycle should follow this sequence:

`record -> validation -> witness review -> verification -> revision -> archive -> federation sync -> public verification`

Each stage should emit machine-readable status transitions so explorer and API surfaces remain consistent.

## Terminology Consistency

Use the following terms consistently across APIs, docs, and UI:

- **verification**: cryptographic and policy evaluation of a record/revision.
- **provenance**: lineage and source graph for a record and its revisions.
- **integrity**: hash/signature consistency and content immutability guarantees.
- **witness**: attestor entity signing or affirming verification-relevant evidence.
- **validator**: component or authority executing validation rules.
- **revision**: versioned update in an append-only record lineage.
- **dispute**: formal challenge state attached to a record or revision.
- **superseded**: no longer authoritative due to a later accepted revision.
- **trust state**: final externally visible verification outcome classification.

## Future Compatibility Targets

This routing architecture should remain compatible with:

- Browser extension verification surfaces.
- Mobile verification interfaces.
- C2PA bridge adapters.
- External verification APIs.
- Institutional verification workflows.
- Social platform verification integrations.

Compatibility requirement: new channels must consume canonical routes and shared verification state semantics rather than introducing parallel trust taxonomies.

## Backward Compatibility Notes

- Existing verification links should continue resolving through redirect or alias mapping to canonical patterns.
- State names and core response fields should be treated as public contract once released.
- Additional fields may be added in a backward-compatible way; existing fields should not be repurposed.
