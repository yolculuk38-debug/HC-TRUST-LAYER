# Public Explorer Navigation Note

> **Mode:** DOCUMENTATION ONLY
>
> **Scope:** Navigation note for existing Public Explorer planning and architecture documents.
>
> **Boundary:** This note does not change implementation behavior or canonical artifacts.

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
7. [`docs/project-control/public-explorer-planning-gap-review.md`](public-explorer-planning-gap-review.md) — report-only consolidation gap review.
8. [`docs/project-control/public-explorer-maturity-checklist.md`](public-explorer-maturity-checklist.md) — maturity labels, capability matrix, and reviewer checklists.

## Current Repository Evidence

The repository already contains:

- Public Explorer MVP documentation.
- Verification Explorer architecture foundation.
- Static browser-only explorer documentation.
- Experimental Explorer API documentation.
- Public verification routing and boundary documents.
- Public Explorer planning gap review.
- Public Explorer maturity checklist.
- Source files for public explorer-related helpers.

Because these documents already exist, the next safe work is checklist navigation alignment and future evidence-triggered review, not a duplicate Public Explorer plan.

## Boundary Rules

Public Explorer planning must preserve these limits:

- read-only review aid;
- advisory-only result interpretation;
- generated index is non-canonical;
- no truth guarantee;
- no production-readiness claim;
- no autonomous finality;
- no record mutation;
- human-supervised validation remains final authority.

## Review Checklists

Use the gap review and maturity checklist before proposing any new Public Explorer work:

- [`docs/project-control/public-explorer-planning-gap-review.md`](public-explorer-planning-gap-review.md) identifies consolidation gaps and recommends checklist-based review before implementation expansion.
- [`docs/project-control/public-explorer-maturity-checklist.md`](public-explorer-maturity-checklist.md) classifies capabilities as `static-mvp`, `demo-local`, `architecture-only`, `experimental-api`, `deferred`, or `blocked`.

## Suggested Next Review

Future review should be evidence-triggered only. Do not repeat the Public Explorer gap review or maturity checklist unless new repository evidence appears.

When new evidence appears, compare it against:

- public user paths;
- evidence boundaries;
- generated index assumptions;
- local/static-only assumptions;
- public-safe output language;
- human-review escalation points;
- non-goals and deferred implementation work;
- maturity labels in `docs/project-control/public-explorer-maturity-checklist.md`.

Do not implement explorer behavior from this note.
