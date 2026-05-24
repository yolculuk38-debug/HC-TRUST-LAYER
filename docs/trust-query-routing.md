# HC-TRUST-LAYER Trust Query Routing Foundation

## Status

- documentation-only architecture foundation
- no production query-routing service implementation in this phase

## Trust Query Routing Overview

Trust query routing in HC-TRUST-LAYER describes how HC:// verification infrastructure can route read paths across provenance, audit trail, federation, dispute, and snapshot artifacts.

Routing foundations emphasize reproducibility, canonical record anchoring, and human-supervised validation context.

## Trust Graph Query Concepts

Trust graph query concepts include:

- canonical record-centric graph traversal
- node/edge filtering by provenance scope
- conflict edge surfacing for contradictory evidence
- timeline-aware query modes for historical interpretation

## Verification Routing Concepts

Verification routing should map query intent to appropriate evidence surfaces.

Examples:

- current verification summary lookup
- historical verification snapshot comparison
- revocation/supersession path resolution
- policy-context retrieval for interpretation

Routing should prefer explicit provenance and audit trail linkage over opaque aggregation.

## Provenance Lookup Concepts

Provenance lookup routes can include:

- source lineage lookup by canonical record identifier
- transformation chain retrieval
- witness and validator provenance joins
- provenance anomaly flag queries

Provenance lookup results should remain attributable and version-aware.

## Validator Query Concepts

Validator query concepts include:

- validator identity and key lineage lookup
- validator decision history retrieval
- disagreement query across validators for one canonical record
- validator revocation status query

## Federation Query Concepts

Federation query routing can include:

- participant discovery metadata lookup
- per-node verification result comparison
- federation divergence query surfaces
- sync freshness and stale-source query checks

Federation queries should preserve participant-level rationale differences.

## Snapshot Lookup Concepts

Snapshot lookup should support:

- time-bound verification context retrieval
- snapshot hash and chain continuity checks
- delta comparison between snapshots
- snapshot-to-dispute linkage lookup

## Dispute Lookup Concepts

Dispute lookup concepts include:

- open/resolved dispute retrieval by canonical record
- challenge evidence bundle lookup
- escalation history and rationale query
- outcome-to-revocation linkage query

## Audit Query Concepts

Audit query routing should support:

- append-only event timeline retrieval
- policy change trace lookup
- verification execution trace lookup
- custody transition query for evidence lifecycle steps

## Public Verification Explorer Concepts

A public verification explorer can expose a policy-constrained subset of trust query routing.

Explorer query concepts:

- public canonical record view
- provenance and audit trail timeline panels
- revocation/supersession visibility
- dispute state summaries without sensitive payload leakage

## Future API Query Routing

Future API routing concepts can include:

- query namespaces by artifact class (`/records`, `/provenance`, `/disputes`, `/snapshots`)
- deterministic pagination and ordering semantics
- signed query receipts for reproducibility workflows
- federation-aware fallback routing with explicit source labeling

These are architecture concepts only and not active API guarantees in this phase.

## Terminology Alignment

This foundation explicitly aligns with:

- HC-TRUST-LAYER
- HC://
- provenance
- archival integrity
- evidence lifecycle
- trust query
- verification infrastructure
- audit trail
- human-supervised validation
- federation
- canonical record
