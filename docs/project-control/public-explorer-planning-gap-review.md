# Public Explorer Planning Gap Review

> **Mode:** REPORT ONLY
>
> **Scope:** Public Explorer planning-surface review after Public Validator and Public Explorer navigation alignment.
>
> **Boundary:** This review does not modify runtime behavior, validators, schemas, records, generated artifacts, QR behavior, signing, federation, policy, workflows, governance enforcement, APIs, or explorer implementation.

## Executive Summary

The Public Explorer planning surface is already substantial. The repository contains a read-only Explorer MVP, an architecture foundation, an experimental Explorer API note, a static explorer README, public verification routing, public verification boundaries, and a project-control navigation note.

The current gap is not the absence of planning. The current gap is consolidation: the existing documents describe overlapping public explorer concerns, but they are not yet summarized into one compact reviewer-facing checklist for user paths, evidence boundaries, generated-index assumptions, static/local assumptions, public-safe result language, and human-review escalation points.

Recommended next step: add a small checklist or status matrix that maps existing Public Explorer documents to review questions. Do not implement explorer behavior from this review.

## Repository Evidence Reviewed

- `docs/project-control/public-explorer-navigation.md`
- `docs/public-explorer-mvp.md`
- `docs/verification-explorer-architecture.md`
- `docs/explorer/README.md`
- `docs/api/explorer-api-v1.md`
- `docs/public-verification-routing.md`
- `docs/public-verification-boundaries.md`

## What Is Already Covered

### 1. Read-only Explorer MVP boundary

Covered.

`docs/public-explorer-mvp.md` defines the Explorer MVP as a read-only, user-facing view over `generated/explorer_index.json`. It explicitly describes advisory-only, read-only, human-supervised, local/static-data-oriented boundaries.

### 2. Generated index boundary

Covered.

The Explorer MVP states that `generated/explorer_index.json` is an advisory navigation surface and is not itself a canonical record. Missing records in the Explorer do not create a trust-kernel decision.

### 3. Static browser-only explorer surface

Covered.

`docs/explorer/README.md` defines the static browser-only explorer surface, states that it attempts to load generated explorer index data, supports exact search by `record_id` and `content_hash`, and preserves advisory-only boundaries.

### 4. Architecture foundation

Covered.

`docs/verification-explorer-architecture.md` defines the verification explorer as a planned public-facing navigation surface and interpretability layer for provenance and audit trail visibility. It explicitly says the explorer should not replace validator outputs or human-supervised validation.

### 5. Lookup concepts

Partially covered.

Architecture and routing documents cover record lookup, hash lookup, verification package lookup, trust graph lookup, witness lookup, revision lookup, and federation source lookup concepts.

Remaining gap: the repository could use a compact matrix showing which lookup paths are MVP-ready, demo-only, architecture-only, or deferred.

### 6. Experimental Explorer API note

Covered but needs caution.

`docs/api/explorer-api-v1.md` defines an experimental, non-production explorer runtime layer and lists runtime functions such as record lookup, verification receipt lookup, and federation status summary.

Remaining gap: this API note should remain clearly separated from the static/read-only MVP so readers do not assume hosted production API readiness.

### 7. Public verification routing

Covered but stronger than current MVP.

`docs/public-verification-routing.md` describes canonical routes such as `/verify/{record_id}`, `/trust/{record_id}`, `/history/{record_id}`, `/revision/{record_id}`, and `/witness/{witness_id}`. It also describes trust-state semantics and canonical backend expectations.

Remaining gap: this routing language should be labeled against implementation maturity, because parts of it describe future or production-oriented routing that may exceed the current static/local MVP.

### 8. Public verification boundaries

Covered.

`docs/public-verification-boundaries.md` defines what public verification checks and does not check. It clearly separates integrity and continuity diagnostics from truth adjudication.

## Gaps Identified

### Gap 1: No compact maturity matrix

Existing documents describe many explorer capabilities, but there is no single table that marks each capability as one of:

- implemented static MVP;
- demo/local only;
- documentation-only architecture;
- experimental API note;
- deferred future work.

This may confuse new AI agents, maintainers, or external reviewers.

### Gap 2: Static Explorer vs Experimental API boundary needs a summary

The static explorer documentation and experimental API documentation both exist. A compact boundary note should clarify:

- static explorer is browser/local/static-data oriented;
- Explorer API is experimental/non-production;
- neither is a hosted production service;
- neither creates truth finality or autonomous governance authority.

### Gap 3: Generated-index assumptions need a reviewer checklist

The generated index is repeatedly described as non-canonical. A reviewer checklist should make this operational:

- generated index missing record means lookup absence only;
- generated index match is navigation evidence only;
- canonical record boundaries remain authoritative;
- generated artifacts must not be manually promoted to records.

### Gap 4: Public user paths are documented but not consolidated

User paths appear across MVP, architecture, routing, and README documents. A compact list should distinguish:

- record ID search;
- content hash search;
- source path/status search;
- QR-to-route entry;
- verification package inspection;
- trust graph/provenance navigation;
- witness/revision/federation views.

### Gap 5: Human-review escalation points are present but distributed

Human-supervised validation is consistently stated, but the exact escalation triggers are distributed across documents. A compact checklist should include:

- missing index;
- malformed index;
- ambiguous match;
- missing canonical record;
- hash mismatch;
- provenance gap;
- dispute/replay marker;
- federation staleness;
- non-public or redacted evidence.

## Recommended Next Small PR

Add one documentation-only checklist:

```text
docs/project-control/public-explorer-maturity-checklist.md
```

Recommended contents:

- capability maturity matrix;
- static MVP vs experimental API boundary;
- generated-index reviewer checklist;
- public user path checklist;
- human-review escalation checklist;
- non-goals and protected-path reminder.

## Do Not Do Yet

Do not modify:

- `src/**`;
- `schema/**`;
- `validators/**`;
- `.github/workflows/**`;
- `records/**`;
- `hash/**`;
- `qr/**`;
- `generated/**`;
- `signing/**`;
- `federation/**`;
- `policy/**`.

Do not implement new explorer behavior from this review.

## Decision Language

Recommended project-control decision language:

```text
PUBLIC EXPLORER GAP REVIEW COMPLETE
```

The Explorer planning surface exists and is sufficient for navigation, but it needs a compact maturity/checklist document before any implementation expansion.
