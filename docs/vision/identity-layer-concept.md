# Identity Layer Concept

> **Status:** Vision / architecture concept
>
> **Scope:** Future-facing account, claimed identity, authority-scope, and identity-evidence layer for HC://
>
> **Implementation status:** Not implemented. This document does not modify runtime behavior, validators, schemas, records, signing logic, federation behavior, QR behavior, workflows, policy, or governance enforcement.

## Purpose

This document defines a future-facing Identity Layer concept for HC-TRUST-LAYER.

It extends the source and social verification vision by describing how HC:// may represent identity-related evidence without turning identity into automatic trust, truth, authority, or governance power.

The core principle is:

```text
Identity evidence is not truth.
```

An account may be real while its claim remains unsupported.

An account may be anonymous while its evidence remains useful.

A verified profile may be compromised, spoofed, or used outside its authority scope.

## Problem Space

Public verification often fails when identity is treated as a single binary signal.

Common risks include:

- impersonation;
- lookalike accounts;
- compromised accounts;
- parody or fan accounts presented as official;
- unofficial accounts making institutional claims;
- official accounts sharing unsupported claims;
- anonymous sources with evidence but unclear identity;
- AI-generated agents or bots presenting unclear authorship;
- authority mismatch between the speaker and the claim.

HC:// should make identity context inspectable without deciding truth automatically.

## Core Distinction

Future HC:// identity work should separate:

- **account identity:** what account or actor appears to be speaking;
- **claimed identity:** who the account claims to represent;
- **authority scope:** what the actor appears authorized to claim;
- **identity evidence:** records, links, signatures, archives, or references supporting identity context;
- **claim evidence:** evidence supporting the content of the claim itself;
- **review outcome:** human-supervised advisory interpretation.

Identity signals should never replace evidence signals.

## Conceptual Identity Chain

A future identity layer may represent:

```text
account / actor
↓
claimed identity
↓
identity evidence
↓
authority scope
↓
claim object
↓
claim evidence
↓
verification context
↓
human-supervised advisory result
```

Each step should remain inspectable.

## Identity Classes

Possible identity classes include:

- individual;
- organization;
- government or public institution;
- media outlet;
- research institution;
- company;
- platform account;
- AI system or automated agent;
- anonymous or pseudonymous source;
- unknown or disputed source.

Class labels are descriptive only. They do not create authority by themselves.

## Authority Scope

Authority scope describes what an actor is plausibly authorized to speak about.

Examples:

- a government account may be authoritative for its own public notices, but not for unrelated private claims;
- a company account may be authoritative for product statements, but not for independent scientific conclusions;
- a journalist may report evidence, but the account identity alone does not prove the reported event;
- an AI system may summarize or analyze, but it does not become a final authority.

Authority scope should be treated as advisory context, not automatic truth.

## Identity Evidence Examples

Future HC:// identity records may reference:

- official website links;
- domain ownership signals;
- signed statements;
- archived profile snapshots;
- public registry entries;
- verified organization references;
- historical account continuity;
- key or signature fingerprints where available;
- previous trusted relationship records;
- witness or reviewer observations.

Evidence may be missing, stale, conflicting, or disputed.

## Risk Flags

Future identity-layer outputs may surface risk flags such as:

- `identity_unknown`;
- `identity_disputed`;
- `possible_impersonation`;
- `possible_compromise`;
- `unofficial_account`;
- `authority_scope_unclear`;
- `missing_identity_evidence`;
- `conflicting_identity_evidence`;
- `stale_identity_reference`;
- `anonymous_source`.

Risk flags should explain uncertainty instead of hiding it.

## Relationship to Source and Social Verification

This concept supports `docs/vision/source-and-social-verification.md`.

Source and social verification asks:

- Who published first?
- Is the source account official, unofficial, compromised, or unknown?
- Is there a visible evidence chain?
- Is the content being replayed or reframed?

The Identity Layer focuses on the actor/account side of that chain.

It does not replace content provenance, evidence-chain review, trust graph edges, validator identity architecture, or signed validator identity research.

## Relationship to Existing Validator Identity Work

Existing validator identity documents focus on validators, reviewer-facing validator roles, signing authority concepts, lifecycle, revocation, and federation-facing validator context.

This document focuses on public source identity and claim-context identity.

In short:

```text
validator identity = who produced a verification output
source identity = who appears to have made or carried a public claim
```

Both should preserve human-supervised validation and avoid automatic authority claims.

## Public-Safe Result Shape

A future advisory output could include:

```text
identity_class: organization / individual / government / media / ai-system / unknown
claimed_identity: visible / partial / missing / disputed
identity_evidence: supported / partial / missing / conflicting
authority_scope: clear / limited / unclear / disputed
account_risk: none-visible / possible-impersonation / possible-compromise / unknown
claim_evidence: supported / partial / missing / conflicting
human_review_required: true
truth_guarantee: false
public_safe: true
```

This shape is conceptual only and does not define a schema.

## Non-Goals

This document does not:

- implement identity verification;
- define an identity schema;
- modify validators;
- modify records;
- modify runtime behavior;
- modify signing logic;
- modify federation behavior;
- modify workflows;
- create authority for any identity;
- certify official accounts;
- prove legal identity;
- determine objective truth;
- replace human review.

## Promotion Path

This concept may only move toward implementation through small, reviewed steps:

1. report-only gap review;
2. terminology and scope alignment;
3. example advisory identity result shape;
4. demo-only identity fixture;
5. abuse and impersonation review;
6. local-only prototype;
7. security review;
8. implementation plan;
9. reviewed PRs with tests and human validation.

Until then, Identity Layer remains a future-facing HC:// concept.
