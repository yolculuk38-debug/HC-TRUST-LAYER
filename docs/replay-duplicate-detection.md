# HC-TRUST-LAYER Replay and Duplicate Detection

## Purpose

This document defines replay detection and duplicate-detection concepts for HC-TRUST-LAYER verification infrastructure.

It is architecture guidance only and does not claim automatic authenticity determination.

## Replay Attack Overview

A replay attack occurs when previously valid verification artifacts are reintroduced in a misleading context.

In HC://, replay risk is not limited to payload bytes; it also includes provenance context, sequence interpretation, and policy scope reuse.

## Duplicate Verification Scenarios

Duplicate events can occur in normal operations and adversarial operations.

Examples:
- expected duplicates from mirrored federation transport
- re-issued verification package snapshots for archival export
- adversarial duplicate submission to inflate perceived corroboration

Duplicate detection should classify intent as unknown unless corroborated by additional audit trail evidence.

## Metadata Replay Scenarios

Metadata replay includes reuse of old timestamps, headers, or witness descriptors.

Risks:
- false freshness signals
- context transfer from one canonical record to another
- policy confusion from outdated metadata envelopes

## Provenance Replay Risks

Provenance replay can make an old chain appear current.

Risks include:
- stale lineage presented as active verification
- missing revocation overlays in replayed bundles
- forged parent-child references attached to valid historical nodes

## Witness Replay Concepts

Witness replay occurs when old witness artifacts are presented as if newly witnessed.

Controls to consider:
- witness event identifiers
- witness timestamp correlation with validator events
- witness scope binding to canonical record and provenance context

## Replay-Chain Manipulation

Replay-chain manipulation may involve reordering or selective omission.

Patterns:
- branch splitting to hide contradiction
- insertion of synthetic intermediary events
- suppression of negative evidence links

Trust graph ingestion should preserve ordering provenance and contradiction markers.

## Canonical Payload Comparison Concepts

Canonical payload comparison is a baseline replay control.

Concepts:
- deterministic canonical record serialization
- hash comparison with canonical boundary constraints
- context hash for provenance-critical fields
- replay flags when payload equivalence conflicts with lifecycle state

## Future Replay Detection Heuristics

Potential heuristic directions:
- temporal anomaly scoring across repeated validator_id activity
- source-channel mismatch detection
- signature reuse clustering
- federation divergence alerts for same canonical record ID

These heuristics are assistive signals for human-supervised validation, not automated truth judgment.

## Replay Audit Trail Concepts

Replay detection should be visible in audit trail records.

Concepts:
- replay event class and severity
- duplicate cluster references
- first-seen and last-seen timestamps
- related verification package references
- manual adjudication notes

## Terminology Alignment

This document aligns with:
- HC-TRUST-LAYER
- HC://
- provenance
- verification infrastructure
- replay detection
- verification package
- audit trail
- trust graph
- canonical record
- human-supervised validation
