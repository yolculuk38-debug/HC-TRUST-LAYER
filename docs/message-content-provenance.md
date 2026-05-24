# Message and Content Provenance Foundation

## Status

- documentation/specification only
- no Gmail/API integration in this phase
- no browser extension implementation in this phase
- no production deployment claim in this phase

## Purpose

This document defines a foundation for **message provenance** and **content provenance** within HC-TRUST-LAYER and HC:// verification infrastructure.

It prepares a future Message Trust Layer so verification can extend to messages, emails, screenshots, documents, AI-generated content, and social/media content.

This is an architecture and policy context document, not a production integration announcement.

## Message Provenance Overview

Message provenance in HC-TRUST-LAYER means tracing how a message instance is represented as a canonical record and linked to evidence context over time.

Baseline components:

- canonical record reference for the message artifact
- message content hash
- provenance context (source channel, timing context, transformation/forwarding context)
- witness context where available
- audit trail events for revisions, supersession, or dispute markers

Message provenance supports reproducible checks, not narrative authority.

## Content Provenance Overview

Content provenance in HC-TRUST-LAYER extends beyond message text to attached or associated artifacts such as:

- screenshots
- documents
- exported email payloads
- social/media captures
- AI-generated text artifacts

Content provenance links each artifact to canonical record boundaries, hash evidence, and traceable verification events.

## Email/Message Trust Context

Future email and messaging workflows (including Gmail-oriented research directions) are treated as Message Trust Layer use cases.

HC-TRUST-LAYER verification infrastructure can evaluate whether captured message artifacts remain consistent with their registered canonical record and provenance context.

This does not imply inbox-level platform integration at current phase.

## Screenshot Verification Context

Screenshots are high-risk because visual captures can be cropped, recompressed, or edited.

For HC://, screenshot verification context should include:

- hash binding of captured artifact
- capture metadata availability (if present)
- provenance notes describing capture path
- witness context when independent review exists
- linkage to canonical record and revision history

## Document Provenance Context

Document provenance applies to exported files (PDF, text, report bundles) and institutional records.

Verification should preserve:

- canonical record linkage
- content hash match evidence
- provenance context and source path
- audit trail continuity for revisions/supersession

## AI-Generated Content Context

AI-generated text or media can be included as provenance-scoped artifacts.

HC-TRUST-LAYER does not treat AI output as autonomous authority.

Instead, AI-generated content verification focuses on:

- whether the registered artifact matches expected hash/material
- whether provenance and witness context are visible
- whether audit trail continuity is preserved

## Forwarded-Message Risk

Forwarded messages may lose original headers, timestamps, or contextual boundaries.

HC-TRUST-LAYER should represent forwarding as provenance events so downstream verification can distinguish:

- original artifact context
- forwarded representation context
- missing metadata warnings

## Metadata Loss Risk

Metadata may be stripped during copy/paste, screenshot conversion, platform export, or reposting.

Verification outputs should preserve explicit visibility when metadata is incomplete so users can interpret provenance limits.

## Content Hash and Record Linkage

A content hash alone is insufficient without canonical record linkage.

HC:// verification for message/content provenance should require:

- hash evidence
- canonical record identifier linkage
- provenance context linkage
- revision and supersession linkage where available

## Witness Context

Witness context can include human-supervised review, process attestations, and model-assisted observations.

Witness context improves interpretability but does not replace evidence-bound verification checks.

## Public Verification Linkage

Public verification surfaces should expose message/content provenance signals in reproducible categories (PASS/WARNING/FAIL/UNKNOWN) without overstating certainty.

Public verification is a visibility mechanism for evidence-bound checks, not a truth declaration.

## QR Verification Bridge

QR linkage can bridge distributed message/content captures to canonical record verification routes.

Future QR verification bridges should include anti-spoofing safeguards and clear canonical path mapping.

## Verification Package Relationship

Verification packages are derived artifacts that can transport message/content provenance evidence across systems.

A verification package must remain subordinate to canonical record authority and should include:

- canonical record references
- content hash references
- provenance context fields
- witness context fields
- audit trail excerpts or pointers

## Future Use Cases

The following are future-oriented use cases for HC-TRUST-LAYER message/content provenance:

- Gmail / email trust layer
- browser extension verification
- social media post verification
- screenshot/document verification
- AI-generated text verification
- forwarded message provenance
- archive verification
- institutional document lookup

These are planning targets and do not imply current production integration.

## What HC-TRUST-LAYER Verifies

Within message/content provenance scope, HC-TRUST-LAYER verifies:

- record integrity
- content hash match
- provenance context visibility
- witness context visibility
- audit trail continuity
- revision history linkage
- verification package consistency with canonical record boundaries

## What HC-TRUST-LAYER Does Not Verify

HC-TRUST-LAYER does not verify:

- absolute
  truth
- intent
- legal validity
- institutional endorsement
- full authenticity without source evidence

## Risk Section

Major risks for message/content provenance include:

- forged screenshots
- copied messages represented as originals
- metadata stripping during forwarding/export
- fake forward chains
- QR spoofing
- replayed content in altered context
- AI-generated impersonation artifacts
- platform API dependency and upstream instability
- privacy risks from over-collection or overexposure of provenance metadata

Risk treatment requires layered controls, transparent warnings, and human-supervised escalation for high-impact decisions.

## Future Architecture Notes

Planned architecture directions:

- Message Trust Layer as a dedicated verification surface
- C2PA bridge exploration for compatible provenance exchange
- browser extension verification surface
- public verification API extension for message/content provenance
- verification packages with richer provenance bundles
- trust graph linkage for replay lineage and witness relationships
- signing and witness integration for stronger attribution paths

All items above are forward-looking architecture notes for HC-TRUST-LAYER verification infrastructure.


## Related Foundations

- Federation discovery foundation: `docs/federation-discovery.md`
- Offline verification foundation: `docs/offline-verification.md`
- Verification snapshot foundation: `docs/verification-snapshots.md`
- AI model provenance foundation: `docs/ai-model-provenance.md`
