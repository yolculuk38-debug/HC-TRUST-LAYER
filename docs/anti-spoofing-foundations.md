# HC-TRUST-LAYER Anti-Spoofing Foundations

## Purpose

This document defines anti-spoofing foundations for HC-TRUST-LAYER and HC:// verification infrastructure.

It provides documentation-only safeguards for provenance and trust graph interpretation and does not introduce runtime enforcement or production security guarantees.

## Spoofing Overview

Spoofing is the deceptive presentation of identity, provenance, or verification context to influence trust outcomes.

In HC://, spoofing risk spans validator identity, witness claims, verification packages, metadata, federation interactions, and public verification presentation.

## Fake Validator Risks

Fake validator risks include cloned validator identifiers, fabricated capability declarations, and deceptive routing metadata intended to appear legitimate.

## Fake Witness Risks

Fake witness risks include fabricated witness identities, manipulated attestation scope, and replayed witness artifacts without valid context.

## Replayed Provenance Risks

Replayed provenance risks include old lineage artifacts presented as current, missing revocation context, and reattached lineage branches.

## Forged Verification Package Risks

Forged verification package risks include package substitution, synthetic evidence bundles, and manipulated relationship metadata between package and canonical record.

## Metadata Spoofing

Metadata spoofing includes false timestamps, channel labels, role declarations, or federation origin tags that distort audit trail interpretation.

## QR Spoofing

QR spoofing includes deceptive QR artifacts that reference counterfeit records, altered package endpoints, or misleading verification paths.

## Federation Impersonation

Federation impersonation includes fake peer identities, fraudulent exchange claims, or deceptive node-role declarations in HC:// trust routing.

## Public Verification Deception Risks

Public verification deception risks include interfaces that present partial or misleading trust graph context, obscuring dispute status or revocation signals.

## Trust Graph Poisoning Risks

Trust graph poisoning risks include adversarial insertion of fake nodes and forged edges that appear plausible without proper provenance review.

## Anti-Spoofing Principles

Anti-spoofing principles for this phase:
- preserve canonical record boundaries and identity continuity
- require provenance visibility for trust-relevant relationships
- keep audit trail evidence complete and reviewable
- isolate contested artifacts for explicit review
- avoid automatic trust decisions from unvalidated inputs

## Human-Supervised Review Requirements

Anti-spoofing interpretation requires human-supervised validation for non-trivial or high-impact trust decisions.

Review should include:
- identity plausibility checks
- provenance continuity checks
- dispute and revocation context checks
- cross-reference checks against repository-defined policy and architecture docs

## Terminology Alignment

This foundation aligns with:
- HC-TRUST-LAYER
- HC://
- anti-spoofing
- protocol graph integrity
- provenance
- trust graph
- trusted relationship
- audit trail
- canonical record
- human-supervised validation
