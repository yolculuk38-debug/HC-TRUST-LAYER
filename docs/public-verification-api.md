# HC-TRUST-LAYER Public Verification API Architecture Draft

## Status

- documentation/specification only
- no API server implementation in this phase
- no production backend integration in this phase
- no authentication system additions in this phase
- no validator/schema mutation in this phase

## Purpose

This draft defines future-facing **public verification** semantics for HC-TRUST-LAYER and HC://.

It prepares a stable external verification surface while preserving trust kernel discipline, canonical record boundaries, and derived artifact boundaries.

This document is architecture guidance for future interoperability and is not a deployment claim.

## API Goals

The future public verification API should support:

- public integrity verification
- provenance lookup
- audit visibility
- verification package retrieval
- witness context lookup
- revision visibility

## Authority and Scope Boundaries

HC-TRUST-LAYER verification is bounded and evidence-oriented.

HC-TRUST-LAYER does **not**:

- guarantee truth
- replace human judgment
- provide authoritative AI verdicts
- guarantee content authenticity beyond verification scope

Verification outputs represent protocol-evaluated integrity/provenance signals under declared rules.

## Canonical and Derived Artifact Discipline

A **canonical record** remains authoritative.

A **verification package** is a **derived artifact** for transport and interoperability.

Public verification APIs must not mutate canonical state and must not elevate derived artifacts above canonical records.

## Candidate Endpoint Surface (Future)

Potential public endpoints:

- `GET /verify/{record_id}`
- `GET /package/{package_id}`
- `GET /record/{record_id}`
- `GET /provenance/{record_id}`
- `GET /audit/{record_id}`
- `GET /witness/{record_id}`

These endpoint names are architecture placeholders for compatibility planning.

## Expected Response Categories

Standard response categories for future external consumers:

- **PASS**
- **WARNING**
- **FAIL**
- **UNKNOWN**

`UNKNOWN` is used when required data is unavailable, unresolved, or out-of-scope for deterministic classification.

## Verification Semantics

Public verification semantics should expose the following classes of checks and visibility:

1. **integrity verification**
   - deterministic verification of record hash/material consistency under HC-TRUST-LAYER rules
2. **canonical path validation**
   - explicit check that declared canonical record path remains in valid canonical scope
3. **provenance visibility**
   - transparent provenance context for source, transformation lineage, and linked evidence
4. **witness context visibility**
   - structured witness context exposure for review attribution and confidence interpretation
5. **audit consistency**
   - auditable trail continuity checks across available evidence entries
6. **revision chain visibility**
   - explicit mapping of prior/superseding revision relationships where available

## API Safety Principles

Future public verification API behavior should follow these principles:

- read-only verification
- no canonical mutation
- deterministic responses where possible
- explicit warning visibility
- non-authoritative AI context
- reproducible validation behavior

Safety intent: maximize transparency and reproducibility while minimizing accidental authority inflation.

## Rate-Limit and Security Considerations

Future implementation planning should include:

- abuse protection
  - bounded query rates and anti-scraping controls to preserve service availability
- cache boundaries
  - clear caching semantics for mutable vs immutable verification views
- export limits
  - constrained response sizes/pagination for large audit/provenance payloads
- mirror trust assumptions
  - explicit treatment of mirror-origin uncertainty and stale data risk
- replay considerations
  - timestamp/context exposure to reduce stale-response misuse in downstream workflows

## Non-Goals

This API is not:

- a social network
- a truth oracle
- autonomous governance
- a replacement for institutional review
- a moderation authority

## Future Compatibility

Planned compatibility directions:

- Ed25519 signing
- federation verification
- external mirrors
- verification explorer integration
- browser extension
- archive verification
- Message Trust Layer
- message/content provenance architecture linkage

These are forward-compatibility targets and do not imply production completion timelines.

## Implementation Constraint Reminder

This phase remains documentation-only architecture.

No API server code is added here.

No production backend is added here.

No authentication subsystem is added here.

No validator or schema semantics are modified here.

## Related Documentation

- Verification explorer architecture foundation: `docs/verification-explorer-architecture.md`
- Provenance viewer foundation: `docs/provenance-viewer.md`
- Public verification flow foundation: `docs/public-verification-flow.md`
- Trust graph viewer foundation: `docs/trust-graph-viewer.md`
- Message and content provenance foundation: `docs/message-content-provenance.md`
- Trust graph foundation: `docs/trust-graph.md`
- Verification package generation architecture: `docs/verification-package-generation.md`

## Related Governance Reference

- Trusted auto-merge governance model: `docs/trusted-auto-merge.md`
- Policy engine architecture: `docs/policy-engine-architecture.md`

