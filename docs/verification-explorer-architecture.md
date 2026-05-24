# HC-TRUST-LAYER HC:// Verification Explorer Architecture Foundation

## Status

- documentation-only foundation
- no frontend implementation in this phase
- no runtime explorer implementation in this phase
- no production readiness claim
- no automatic trust decisions

## Verification Explorer Overview

The **verification explorer** is a planned public-facing navigation surface for HC-TRUST-LAYER and HC:// verification artifacts.

Its purpose is to make verification evidence easier to inspect without changing trust-kernel behavior.

The verification explorer is an interpretability layer for provenance and audit trail visibility, not a replacement for validator outputs or human-supervised validation.

## Public Verification Flow

The verification explorer should align with the public verification path:

1. user starts with a record identifier, hash, or QR payload
2. system resolves canonical record context
3. system surfaces verification package and related provenance
4. system shows trust graph relationships
5. system exposes replay/dispute and validator visibility indicators
6. user escalates uncertain/high-impact outcomes to human-supervised validation

## Verification Lookup Concepts

Verification lookup should support multiple entry points while preserving deterministic linkage to canonical evidence:

- record identifier lookup
- canonical record lookup
- hash verification lookup
- verification package lookup
- trust graph relationship lookup

All lookup views should preserve clear boundaries between canonical record data and derived explorer presentation.

## Canonical Record Lookup

Canonical record lookup should:

- resolve exact canonical record identity
- show deterministic record metadata boundaries
- link to provenance and audit trail references
- show related verification package references without replacing canonical source authority

## Hash Verification Lookup

Hash verification lookup should:

- accept explicit hash inputs
- show hash-to-canonical-record match status
- expose mismatch/ambiguity states clearly
- display replay/dispute flags when hash reuse appears across conflicting provenance contexts

## Verification Package Inspection

Verification package inspection should provide:

- package identifier and package version context
- canonical record linkage references
- validator summary visibility
- provenance references included in package scope
- audit trail snapshot references used during packaging

Verification package inspection is a review aid and must not be presented as autonomous trust finality.

## Trust Graph Navigation

Trust graph navigation in the verification explorer should support:

- canonical record–centric graph entry
- node/edge traversal across provenance and validator relationships
- selective expansion of federation relationship indicators
- replay/dispute relationship markers for contested edges

Trust graph navigation should remain explanatory and should not imply automatic trust decisions.

## Provenance Chain Viewing

Provenance chain viewing should surface:

- chronological provenance events
- supersession and revision transitions
- witness and validator touchpoints
- associated audit trail entries

The chain should be inspectable for continuity gaps and contradictory lineage signals.

## Replay/Dispute Visibility

The verification explorer should include explicit replay/dispute visibility concepts:

- replay warning badges when repeated payload/context patterns appear
- dispute state markers for challenged canonical records
- links to dispute documentation or governance pathway references
- unresolved-state indicators that require human-supervised validation

## Validator Visibility Concepts

Validator visibility should include:

- validator identity references
- validation timestamp context
- outcome category visibility (pass/warning/fail/unknown)
- rationale/evidence pointers where available

Validator visibility is interpretive context and should not be treated as infallible authority.

## Verification Snapshot Visibility

Verification explorer views should support verification snapshot visibility:

- snapshot timestamp and scope
- snapshot-to-canonical-record linkage
- snapshot-to-verification-package linkage
- drift indicators when newer provenance or audit trail entries exist

## Federation Visibility Concepts

Federation visibility should remain bounded and transparent:

- identify whether evidence arrived through local or federated pathways
- show federation node/source metadata where documented
- expose sync staleness indicators when federation data is delayed
- avoid implying live federation guarantees

## Explorer Privacy Considerations

Explorer privacy considerations should include:

- minimized exposure of sensitive metadata fields
- role-based redaction compatibility for future policy controls
- explicit display of redacted/withheld evidence states
- separation of public visibility from internal reviewer-only data

Privacy handling must preserve audit trail continuity and provenance interpretability while respecting human-supervised validation boundaries.

## Related Foundations

- `docs/verification-scenarios.md`
- `docs/demo-verification-flow.md`

## Terminology Alignment

This foundation aligns with HC-TRUST-LAYER and HC:// terminology and preserves these core terms:

- verification explorer
- provenance viewer
- trust graph
- provenance
- audit trail
- verification package
- canonical record
- human-supervised validation
