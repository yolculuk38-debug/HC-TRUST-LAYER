# Source and Social Verification Vision

> **Status:** Vision / planning
>
> **Scope:** Future-facing source, account, media, and social verification direction for HC://
>
> **Implementation status:** Not implemented. This document does not modify runtime behavior, validators, schemas, records, signing logic, federation behavior, QR behavior, workflows, policy, or governance enforcement.

## Purpose

HC-TRUST-LAYER currently focuses on records, hashes, QR-linked verification flows, provenance, witnesses, validator outputs, audit trails, and public-safe advisory results.

This vision document describes a future direction for verifying source and social context around public claims, posts, media, and institutional statements.

The goal is not to decide truth automatically. The goal is to make source chains, evidence chains, responsibility chains, contradictions, and missing evidence visible for human-supervised review.

## Problem Space

Online claims often fail because identity and evidence are collapsed into one weak signal.

Common questions include:

- Who published this first?
- Is the account authentic, impersonated, compromised, or unofficial?
- Is the source an individual, institution, government body, company, media outlet, or anonymous account?
- Has the content been edited, deleted, re-uploaded, clipped, translated, or reframed?
- Does the account identity match the claim authority?
- Is there supporting evidence outside the social post?
- Are there contradictory official records, archived copies, or independent witnesses?
- Is a viral post replaying old content in a new context?
- Is an image, video, document, or quote linked to a verifiable provenance trail?

HC:// should treat these as verification-context questions, not as automatic truth decisions.

## Core Distinction

Identity trust is not the same as evidence trust.

A post may come from a real account while still making an unsupported claim.

A post may come from an unofficial account while still linking to useful evidence.

A video may be authentic media while the surrounding caption is misleading.

A verified account may be compromised, spoofed, or used outside its authority scope.

Therefore, future HC:// source verification should separate:

- account identity signals;
- content provenance signals;
- evidence support signals;
- institutional authority signals;
- replay and edit-history signals;
- human review status.

## Conceptual Source Chain

A future source verification flow may represent:

```text
source account
↓
claimed identity
↓
content object
↓
first-seen timestamp
↓
archive snapshot
↓
related official source
↓
independent corroboration
↓
contradictions / missing evidence
↓
human-supervised advisory result
```

This chain should remain inspectable and should not collapse into a single opaque score.

## Example Questions HC:// Should Help Surface

### Social post

- Was this post made by the claimed account?
- Was the account official, personal, parody, fan-run, compromised, or unknown?
- Does the claim match a linked institutional source?
- Is the same claim visible on an official website, press release, registry, archive, or public record?

### Video / image

- Is there a content hash or provenance marker?
- Is the media original, clipped, edited, translated, re-captioned, or re-uploaded?
- Is the media older than the claim context?
- Are there C2PA-style provenance signals, platform metadata, archive copies, or independent witnesses?

### Public institution / company statement

- Is the statement on an official domain or only on social media?
- Is the person or account authorized to make that statement?
- Are there matching records, press releases, filings, public notices, or archived copies?
- Are later corrections, retractions, or supersession notices visible?

## Relationship to Existing HC:// Layers

This vision builds on existing HC:// concepts:

- canonical records;
- content hashes;
- QR verification;
- provenance timelines;
- witness attestations;
- validator advisory results;
- trust graph edges;
- replay lineage;
- audit trail continuity;
- human-supervised validation.

It does not replace validator identity architecture or signed validator identity research. Those documents focus on validator/operator identity. This document focuses on public source, account, media, and claim-context verification.

## Future Layer Model

A future implementation may require several separate layers:

1. **Account / source identity layer**
   - account profile evidence;
   - official-domain linkage;
   - declared authority scope;
   - impersonation and compromise risk flags.

2. **Content provenance layer**
   - hash references;
   - timestamps;
   - archive snapshots;
   - media provenance metadata;
   - edit and supersession signals.

3. **Evidence chain layer**
   - linked documents;
   - official records;
   - independent corroboration;
   - missing evidence;
   - conflicting evidence.

4. **Replay and distribution layer**
   - first-seen references;
   - re-post chains;
   - stale-context warnings;
   - copied or transformed content clusters.

5. **Advisory result layer**
   - public-safe summary;
   - uncertainty and warning fields;
   - human review requirement;
   - no truth guarantee.

## Public-Safe Result Shape

A future public result should preserve advisory boundaries:

```text
identity_trust: account appears official / unofficial / unknown / disputed
source_chain: visible / partial / missing / conflicting
evidence_chain: supported / partial / missing / conflicting
content_provenance: verified / partial / missing / disputed
human_review_required: true
truth_guarantee: false
public_safe: true
warnings: [...]
```

The result should explain why evidence is missing or conflicting instead of pretending certainty.

## Non-Goals

This document does not:

- implement source verification;
- implement social account verification;
- implement media forensics;
- modify QR behavior;
- modify validators;
- modify schemas;
- modify records;
- modify runtime behavior;
- modify signing logic;
- modify federation behavior;
- modify workflows;
- grant authority to any account, validator, institution, AI model, or reviewer;
- claim objective truth detection;
- replace human-supervised validation.

## Promotion Path

This vision may only move toward implementation through small, reviewed steps:

1. report-only gap review;
2. terminology and scope alignment;
3. example advisory result shape;
4. demo-only fixture;
5. local-only verification prototype;
6. public-safe UX draft;
7. security and abuse review;
8. implementation PRs with tests and human review.

Until then, source and social verification remains a future-facing HC:// vision layer.
