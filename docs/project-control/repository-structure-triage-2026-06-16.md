# Repository Structure Triage — 2026-06-16

Status: advisory structure triage.

This document explains why the repository currently looks crowded from the GitHub mobile file browser and records a safe cleanup path before any file moves, deletions, archive work, branch cleanup, or navigation rewrite.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This document does not authorize deleting, moving, renaming, archiving, disabling, or rewriting files.
- Historical/evidence-bearing material must not be silently rewritten.
- Generated artifacts are advisory evidence, not canonical records.

## Current problem

The repository now mixes multiple layers in one visible tree:

1. active trust-layer implementation,
2. operating/governance layer,
3. public validator/demo layer,
4. historical/legacy evidence,
5. future/vision/design documents,
6. workflow/security automation,
7. generated/reference artifacts,
8. tests and local tooling.

That structure is explainable, but it is not yet easy to read from the GitHub mobile UI. A new maintainer, contributor, AI assistant, or reviewer can see many files but cannot quickly tell which ones are active, historical, protected, generated, or planning-only.

## Repository layer map

### 1. Active trust kernel / implementation surface

Purpose: verification, runtime, record identity, hash/QR behavior, schema, and tests.

Examples:

- `src/`
- `tests/`
- `scripts/`
- `schema/`
- `records/`
- `hash/`
- `qr/`
- `generated/`
- `examples/`
- `requirements.txt`
- `requirements-test.txt`
- `pyproject.toml`
- `protocol-graph.json`
- `verification-map.json`
- `trust-kernel-index.json`

Notes:

- These are not cleanup targets by default.
- `generated/` and generated JSON indexes are advisory/reference outputs, not canonical records.
- Runtime/schema/record/QR/hash behavior changes require focused PRs, tests, and human review.

### 2. Operating layer / repo control surface

Purpose: keep human, AI, CI, and governance work coordinated.

Examples:

- `AGENTS.md`
- `HC_BOOTSTRAP.md`
- `CODEOWNERS`
- `CONTRIBUTING.md`
- `.github/`
- `docs/project-control/`
- `docs/operations/`
- `docs/hc-engineer/`

Notes:

- This layer explains how work is done.
- It should not grow into a second product.
- Project-control files should guide active work, not repeat every completed PR.

### 3. Governance and security surface

Purpose: authority boundaries, policy, risk, audit, protected paths, and security review.

Examples:

- `GOVERNANCE.md`
- `HC_CONSTITUTION.md`
- `SECURITY.md`
- `docs/governance/`
- `docs/security/`
- `policy/`

Notes:

- These files are not casual cleanup targets.
- Governance/security docs can be clarified, but authority language must not be weakened.
- AI remains advisory; human final authority remains required.

### 4. Public validator / demo / user-facing layer

Purpose: make HC:// understandable and demonstrable without claiming production truth verification.

Examples:

- `README.md`
- `docs/START_HERE.md`
- `docs/demo/`
- `docs/public/`
- `docs/explorer/`
- `docs/api/`
- `docs/verification/`
- public validator quickstarts and static viewer files.

Notes:

- This is the next area that should become easier to use.
- Public demo work must remain local/demo-only unless a later deployment PR explicitly changes that boundary.
- `truth_guarantee=false` remains required.

### 5. Historical, witness, legacy, and provenance layer

Purpose: preserve origin, witness, migration, and historical context.

Examples:

- `PROJECT_ORIGIN_RECORD.md`
- `witness-archive/`
- `witness/`
- `timeline/`
- `council/`
- `media/`
- older `docs/*.md` files that record early architecture, verification models, witness ideas, or legacy naming.

Notes:

- These files can look messy from a flat browser view, but many are evidence/provenance references.
- They should be indexed before any archive/move/delete proposal.
- Legacy source-project and legacy repository names can remain when they preserve historical provenance.

### 6. Planning, vision, and future design layer

Purpose: preserve future models and product direction without implying implementation.

Examples:

- `docs/vision/`
- `docs/future/`
- `docs/architecture/`
- `docs/spec/`
- older design files under `docs/` such as verification, witness, API, UI, trust, and provenance notes.

Notes:

- These should be clearly marked as planning/reference when not implemented.
- They should not be confused with runtime behavior, schema, validators, or production readiness.

## Why the tests look unsorted

The tests are mostly organized by technical boundary rather than by user story:

- runtime response contracts,
- telemetry payloads,
- replay/continuity behavior,
- degraded runtime recovery,
- validator pipeline consistency,
- QR spoof protection,
- HC Control Bot / assistant command behavior,
- verification package behavior.

That is acceptable for engineering, but the repo needs a short test index that explains which test group protects which trust boundary.

## What not to do next

Do not immediately:

- delete old docs,
- move root files,
- move historical records,
- rename legacy files,
- collapse all verification docs into one file,
- disable tests,
- delete branches based only on count,
- change protected paths,
- treat generated artifacts as canonical records,
- remove workflow evidence runs without a separate risk review.

## Safe cleanup sequence

### Phase A — map before moving

Create and maintain lightweight maps:

1. repository structure triage — this document;
2. root file purpose index;
3. docs directory purpose index;
4. test coverage index;
5. historical/legacy evidence index.

### Phase B — classify, do not delete

Classify each confusing file or folder as one of:

- `ACTIVE_IMPLEMENTATION`,
- `OPERATING_LAYER`,
- `GOVERNANCE_SECURITY`,
- `PUBLIC_DEMO`,
- `HISTORICAL_EVIDENCE`,
- `VISION_REFERENCE`,
- `GENERATED_REFERENCE`,
- `CLEANUP_CANDIDATE_REPORT_ONLY`.

### Phase C — link first

Before moving files, add navigation links from:

- `README.md`,
- `docs/START_HERE.md`,
- `docs/project-control/operator-entry-map.md`.

### Phase D — move/archive only with explicit approval

Only after classification and human review:

- move planning-only docs into clearer subfolders,
- add archive index files,
- leave redirect notes if useful,
- never rewrite evidence-bearing history silently.

## Immediate next safe work

1. Add a root file purpose index.
2. Add a docs directory purpose index.
3. Add a test coverage index.
4. Review branch count separately with complete branch-list evidence before any branch deletion proposal.
5. Return to Public Validator UX only after the navigation surface is understandable enough for a new reader.
