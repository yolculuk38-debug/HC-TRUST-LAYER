# Repository Organization Standard — 2026-06-16

Status: advisory repository operating standard.

This document defines the professional method for bringing HC-TRUST-LAYER into a clean, navigable, evidence-preserving repository shape. It applies to root files, `src/`, `docs/`, `tests/`, workflows, scripts, records, generated artifacts, and historical evidence.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This standard does not authorize deleting, moving, archiving, renaming, disabling, or rewriting any file.
- Implementation happens through small PRs, one active PR at a time.
- Every move/delete/archive/consolidation requires prior classification, evidence, and human review.

## Operating principle

HC-TRUST-LAYER should not become a random pile of files. It should behave like a trust infrastructure repository:

1. every file has an owner layer;
2. every file has a purpose;
3. every file is active, historical, generated, demo, future, or cleanup-candidate;
4. protected files are not casually moved;
5. tests map to trust boundaries, not just filenames;
6. workflows prove evidence but do not become autonomous authority;
7. public-facing docs are simple;
8. evidence-bearing history is preserved;
9. cleanup is staged and auditable;
10. human final authority stays visible.

## External model adapted for HC

HC should adapt the control patterns used by serious software, provenance, identity, timestamp, and institutional trust systems:

- GitHub-style repository health: README, CONTRIBUTING, SECURITY, CODEOWNERS, dependency alerts, code scanning, secret scanning, branch/ruleset gates, and clear contribution paths.
- OpenSSF-style security posture: machine-checkable security habits, recurring checks, dependency review, and no silent risk acceptance.
- C2PA-style provenance thinking: content should carry a verifiable history, but provenance must not be overstated as truth.
- W3C Verifiable Credentials-style role separation: issuer/holder/verifier roles stay separate and the verifier decides trust.
- OpenTimestamps-style evidence anchoring: hashes, timestamps, and proofs support existence/integrity evidence without exposing unnecessary content or relying on a single narrative.
- Banking / SSL / e-government-style trust layering: policy, identity, cryptographic evidence, audit logs, certificate/trust anchors, human escalation, and incident handling are separate layers.

HC-specific translation:

```text
record evidence > narrative claim
hash/QR/witness/audit > platform assertion
CI evidence > AI confidence
human final authority > autonomous merge
public-safe advisory output > truth guarantee
```

## Repository target layout model

This is the intended logical map. It is not an immediate move plan.

### Root

Purpose: canonical entry points only.

Expected root files:

- `README.md` — public overview and fastest demo path;
- `CONTRIBUTING.md` — contribution workflow;
- `SECURITY.md` — vulnerability reporting;
- `GOVERNANCE.md` — authority and decision boundaries;
- `HC_CONSTITUTION.md` — immutable principle layer;
- `AGENTS.md` — agent and automation operating rules;
- `HC_BOOTSTRAP.md` — agent/operator startup protocol;
- `CODEOWNERS` — review/ownership routing;
- `LICENSE`, `VERSION`, `CHANGELOG.md`, `ROADMAP.md` — project metadata and release continuity;
- machine-readable reference indexes such as `protocol-graph.json`, `verification-map.json`, and `trust-kernel-index.json`.

Root should not become a dumping ground for every historical concept or design note. If a root file is planning-only, legacy-only, or archival, it should eventually be classified and linked from an index before any move is proposed.

### `src/`

Purpose: active implementation only.

Rules:

- Runtime and validator behavior lives here.
- No narrative-only planning docs belong here.
- Each module should map to a clear trust boundary: runtime, QR, public validator, package verification, redaction, events, policy, decision engine, or canonical bridge.
- Behavior changes require tests.

### `tests/`

Purpose: executable regression evidence.

Rules:

- Tests should map to trust boundaries, not just broad feature names.
- Similar names do not prove duplication.
- Test consolidation needs assertion-level comparison.
- Protected-domain tests remain high-review.
- A future test index can group tests logically even if files remain physically flat for import stability.

### `docs/`

Purpose: documentation grouped by reader and function.

Target docs classes:

- `docs/demo/` — demo and local quickstarts;
- `docs/public/` — public-facing validator/explorer docs;
- `docs/runtime/` — runtime behavior and contracts;
- `docs/security/` — threat models and security boundaries;
- `docs/governance/` — authority and policy;
- `docs/project-control/` — operator state and repo-management maps;
- `docs/vision/` and `docs/future/` — planning-only concepts;
- `docs/architecture/` and `docs/spec/` — architecture/spec references;
- historical root-style docs under `docs/` should be indexed before any archive proposal.

### `.github/`

Purpose: automation, workflows, issue/PR templates, Dependabot, and rules support.

Rules:

- Workflows are protected.
- Permission expansion requires review.
- `pull_request_target` workflows require extra review.
- Auto-merge remains bounded/report-only unless explicitly changed by human-reviewed governance.
- Workflows should be documented by workflow maps.

### `records/`, `hash/`, `qr/`, `witness/`, `witness-archive/`, `timeline/`

Purpose: evidence, provenance, witness, and historical continuity.

Rules:

- Not cleanup targets by default.
- Preserve historical names when they are evidence-bearing.
- Add indexes before moving or archiving.
- Do not rewrite evidence to make the repo look cleaner.

### `generated/`

Purpose: derived/reference artifacts.

Rules:

- Generated artifacts are advisory evidence, not canonical records.
- If regenerated, source and generator path must be clear.
- Generated outputs should not silently overwrite canonical evidence.

## File classification labels

Every confusing file should eventually receive one classification in an index:

- `ACTIVE_IMPLEMENTATION`
- `TEST_EVIDENCE`
- `PUBLIC_DEMO`
- `OPERATING_LAYER`
- `GOVERNANCE_SECURITY`
- `HISTORICAL_EVIDENCE`
- `VISION_REFERENCE`
- `SPEC_REFERENCE`
- `GENERATED_REFERENCE`
- `TOOLING`
- `CLEANUP_CANDIDATE_REPORT_ONLY`
- `DO_NOT_TOUCH_PROTECTED`

## Professional cleanup sequence

### Stage 0 — stop random cleanup

No deletion, move, archive, workflow disablement, or test consolidation from visual clutter alone.

### Stage 1 — map the repo

Create report-only indexes:

1. repository structure triage;
2. root file purpose index;
3. docs directory purpose index;
4. test coverage map;
5. src module purpose index;
6. script/tool purpose index;
7. workflow map;
8. historical/evidence index.

### Stage 2 — classify files

Classify files by layer and risk. Do not change file locations yet.

### Stage 3 — improve navigation first

Update only navigation docs:

- `README.md`,
- `docs/START_HERE.md`,
- `docs/project-control/operator-entry-map.md`,
- small local indexes.

### Stage 4 — consolidate only after evidence

Only after report-only review:

- merge duplicate docs;
- move planning-only docs into clearer folders;
- create archive indexes;
- add redirect notes;
- keep evidence-bearing history intact.

### Stage 5 — enforce with CI and ownership

After structure is clear:

- add or refine CODEOWNERS routes;
- add lightweight repository-structure checks;
- keep Dependabot, CodeQL/code scanning, secret scanning, branch protection, and required checks active;
- avoid autonomous approval/merge/close.

## Stop conditions

Stop and request human review if a proposal touches:

- schema,
- validators,
- records,
- signatures,
- federation,
- policy,
- canonical files,
- generated indexes,
- trust-kernel indexes,
- workflows,
- CODEOWNERS,
- AGENTS.md,
- HC_BOOTSTRAP.md,
- security/governance files,
- historical witness/provenance records,
- tests protecting QR, signing, federation, governance, policy, public validator, or runtime contracts.

## What “automatic” means here

Automatic does not mean blind authority.

Automatic means:

```text
scan -> classify -> report -> small PR -> CI -> review -> merge -> post-merge audit
```

Automatic does not mean:

```text
delete -> move -> rewrite -> disable -> approve itself -> merge itself
```

## Immediate next PRs after #1015

1. Root file purpose index.
2. Docs directory purpose index.
3. Src module purpose index.
4. Script/tool purpose index.
5. Branch-count triage with complete branch-list evidence.
6. Only then: proposal for any move/archive/delete/consolidation.

## Final HC rule

The repo should become easier to read without losing evidence.

```text
Clean structure.
Preserved audit.
Small PRs.
No silent deletion.
No trust overclaim.
Human final authority.
```
