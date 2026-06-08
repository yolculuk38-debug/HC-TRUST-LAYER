# Public Explorer Navigation Note

> **Mode:** DOCUMENTATION ONLY
>
> **Scope:** Navigation note for existing Public Explorer planning and architecture documents.
>
> **Boundary:** This note does not modify runtime behavior, validators, schemas, records, generated artifacts, QR behavior, signing, federation, policy, workflows, or governance enforcement.

## Purpose

This note makes the existing Public Explorer planning surface easier to find without rewriting larger navigation files.

The Public Explorer is a read-only, advisory, public-facing review aid for HC:// verification context. It must remain non-canonical, human-supervised, and separate from trust-kernel behavior.

## Start Here

Read the existing documents in this order:

1. [`docs/public-explorer-mvp.md`](../public-explorer-mvp.md) — read-only Public Verification Explorer MVP scope and generated-index boundary.
2. [`docs/verification-explorer-architecture.md`](../verification-explorer-architecture.md) — verification explorer architecture foundation.
3. [`docs/explorer/README.md`](../explorer/README.md) — static browser-only explorer scope and empty/error-state behavior.
4. [`docs/api/explorer-api-v1.md`](../api/explorer-api-v1.md) — experimental explorer API notes and non-production contract.
5. [`docs/public-verification-routing.md`](../public-verification-routing.md) — public verification routing context.
6. [`docs/public-verification-boundaries.md`](../public-verification-boundaries.md) — public verification boundary language.

## Current Repository Evidence

The repository already contains:

- Public Explorer MVP documentation.
- Verification Explorer architecture foundation.
- Static browser-only explorer documentation.
- Experimental Explorer API documentation.
- Public verification routing and boundary documents.
- Source files for public explorer-related helpers.

Because these documents already exist, the next safe work is navigation alignment and gap review, not a duplicate Public Explorer plan.

## Boundary Rules

Public Explorer planning must preserve these limits:

- read-only review aid;
- advisory-only result interpretation;
- generated index is non-canonical;
- no truth guarantee;
- no production-readiness claim;
- no autonomous governance finality;
- no record mutation;
- no schema, validator, signing, federation, policy, workflow, or governance enforcement changes;
- human-supervised validation remains final authority.

## Suggested Next Review

A future report-only review may compare the current Public Explorer documents against:

- public user paths;
- evidence boundaries;
- generated index assumptions;
- local/static-only assumptions;
- public-safe output language;
- human-review escalation points;
- non-goals and deferred implementation work.

Do not implement explorer behavior from this note.
