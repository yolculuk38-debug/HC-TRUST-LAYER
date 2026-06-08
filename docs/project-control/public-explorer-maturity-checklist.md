# Public Explorer Maturity Checklist

> **Mode:** DOCUMENTATION ONLY
>
> **Scope:** Follow-up checklist for `docs/project-control/public-explorer-planning-gap-review.md`.
>
> **Boundary:** This checklist does not modify runtime behavior, validators, schemas, records, generated artifacts, QR behavior, signing, federation, policy, workflows, governance enforcement, APIs, or explorer implementation.

## Purpose

This checklist turns the Public Explorer planning gap review into a compact reviewer-facing maturity map.

It helps maintainers, AI agents, and external reviewers distinguish between:

- implemented static MVP behavior;
- demo/local-only behavior;
- documentation-only architecture;
- experimental API notes;
- deferred future work.

This checklist is advisory and does not authorize implementation.

## Source Documents

- `docs/project-control/public-explorer-navigation.md`
- `docs/project-control/public-explorer-planning-gap-review.md`
- `docs/public-explorer-mvp.md`
- `docs/verification-explorer-architecture.md`
- `docs/explorer/README.md`
- `docs/api/explorer-api-v1.md`
- `docs/public-verification-routing.md`
- `docs/public-verification-boundaries.md`

## Maturity Labels

| Label | Meaning |
| --- | --- |
| `static-mvp` | Present in the current static/read-only Explorer MVP or documented as the immediate static surface. |
| `demo-local` | Safe for local/demo review only; not a hosted production service. |
| `architecture-only` | Described as a future/architecture concept, not current behavior. |
| `experimental-api` | Described in API/runtime notes but explicitly non-production. |
| `deferred` | Future work; do not implement without a separate reviewed plan. |
| `blocked` | Must not proceed without explicit maintainer approval and human-supervised validation. |

## Capability Maturity Matrix

| Capability | Current maturity | Evidence | Notes |
| --- | --- | --- | --- |
| Static Explorer page | `static-mvp` | `docs/explorer/README.md`, `docs/public-explorer-mvp.md` | Browser-only, read-only, generated-index backed. |
| Record ID search | `static-mvp` | `docs/explorer/README.md`, `docs/public-explorer-mvp.md` | Exact/partial lookup over loaded generated index. |
| Content hash search | `static-mvp` | `docs/explorer/README.md`, `docs/public-explorer-mvp.md` | Search aid only; not canonical proof by itself. |
| Verification status search | `static-mvp` | `docs/public-explorer-mvp.md` | Generated-index navigation only. |
| Source path search | `static-mvp` | `docs/public-explorer-mvp.md` | Generated-index navigation only. |
| Raw generated index preview | `static-mvp` | `docs/public-explorer-mvp.md` | Audit visibility only; non-canonical. |
| Missing/malformed index handling | `static-mvp` | `docs/explorer/README.md` | Deterministic unavailable state; no writes. |
| QR route entry | `demo-local` | `docs/public-verification-routing.md`, `docs/public-verification-boundaries.md` | Routing concept exists; do not imply signed QR authenticity. |
| Canonical route set | `architecture-only` | `docs/public-verification-routing.md` | `/verify`, `/trust`, `/history`, `/revision`, `/witness` are planned public patterns. |
| Verification package inspection | `architecture-only` | `docs/verification-explorer-architecture.md` | Review aid only; not autonomous trust finality. |
| Trust graph navigation | `architecture-only` | `docs/verification-explorer-architecture.md` | Explanatory only; no automatic trust decisions. |
| Provenance chain viewing | `architecture-only` | `docs/verification-explorer-architecture.md` | Future inspectability concept. |
| Replay/dispute visibility | `architecture-only` | `docs/verification-explorer-architecture.md` | Requires human-supervised escalation. |
| Validator visibility | `architecture-only` | `docs/verification-explorer-architecture.md` | Interpretive context, not infallible authority. |
| Federation visibility | `architecture-only` | `docs/verification-explorer-architecture.md` | Avoid live federation guarantees. |
| Explorer record lookup API | `experimental-api` | `docs/api/explorer-api-v1.md` | Non-production runtime note. |
| Explorer receipt lookup API | `experimental-api` | `docs/api/explorer-api-v1.md` | Non-production runtime note. |
| Federation status summary API | `experimental-api` | `docs/api/explorer-api-v1.md` | Non-production runtime note. |
| Hosted production Explorer | `deferred` | Boundary documents | No production-readiness claim. |
| Record mutation from Explorer | `blocked` | Boundary documents | Must not happen. |
| Generated artifact promotion to canonical record | `blocked` | Boundary documents | Must not happen. |
| Runtime, schema, validator, workflow, signing, federation, policy, or governance changes | `blocked` | Project-control boundaries | Requires explicit task and human-supervised validation. |

## Static MVP vs Experimental API Boundary

The current static Public Explorer surface and the experimental Explorer API notes must remain separate.

### Static Explorer

- browser/local/static-data oriented;
- read-only;
- generated-index backed;
- public-safe navigation aid;
- no backend dependency requirement;
- no production-readiness claim.

### Experimental Explorer API

- non-production;
- experimental runtime contract;
- not proof of hosted service readiness;
- not a final public API commitment;
- not an authority or truth engine.

## Generated-Index Reviewer Checklist

When reviewing Explorer output, confirm:

- [ ] The result is treated as navigation evidence only.
- [ ] `generated/explorer_index.json` is not treated as a canonical record.
- [ ] Missing lookup results are not treated as trust-kernel decisions.
- [ ] Generated index matches do not replace canonical record review.
- [ ] Generated artifacts are not manually promoted to verified records.
- [ ] Public Explorer language avoids truth-finality claims.
- [ ] Human-supervised validation remains required for consequential decisions.

## Public User Path Checklist

Public Explorer planning should clearly identify which path a user is taking:

- [ ] Search by Record ID.
- [ ] Search by content hash.
- [ ] Search by verification status.
- [ ] Search by source path.
- [ ] Start from a QR or public verification route.
- [ ] Inspect generated index metadata.
- [ ] Inspect verification package context.
- [ ] Inspect provenance or trust graph context.
- [ ] Inspect witness, revision, replay, dispute, or federation context.

Each path should show whether it is static MVP, demo/local-only, architecture-only, experimental API, or deferred.

## Human-Review Escalation Checklist

Escalate to human-supervised review when any of the following appear:

- [ ] generated index is missing;
- [ ] generated index is malformed;
- [ ] lookup result is ambiguous;
- [ ] canonical record cannot be found;
- [ ] content hash does not match expected context;
- [ ] provenance chain has gaps;
- [ ] replay or dispute markers appear;
- [ ] federation data is stale, unavailable, or conflicting;
- [ ] evidence is redacted, withheld, or non-public;
- [ ] output could affect legal, safety, institutional, or public-trust decisions.

## Non-Goals

This checklist does not:

- implement Explorer behavior;
- create a hosted Explorer service;
- define a production API;
- modify runtime behavior;
- modify schemas or validators;
- modify records or generated artifacts;
- prove truth;
- certify legal, security, or safety outcomes;
- replace human review.

## Decision Language

Recommended project-control decision language:

```text
PUBLIC EXPLORER MATURITY CHECKLIST ADDED
```

After this checklist, the safe next step is to refresh `docs/project-control/next-actions.md` so it does not continue recommending the completed gap-review/checklist sequence.
