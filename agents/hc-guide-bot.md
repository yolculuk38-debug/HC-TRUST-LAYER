# HC Guide Bot v0.1 Design

## Purpose

HC Guide Bot v0.1 is a future advisory-only GitHub PR and Issue guide for HC-TRUST-LAYER contributors.

It is intended to help contributors orient around HC:// repository evidence, current project phase, protected surfaces, duplicate or do-not-repeat work, and evidence expectations before human-supervised validation.

## Implementation Boundary

v0.1 is design only.

There is no implementation in this version:

- No bot account.
- No GitHub Action.
- No auto-comment workflow.
- No label automation.
- No merge automation.
- No enforcement.

This document does not authorize changes to runtime code, schemas, validators, records, policy, signing, federation, canonical artifacts, trust-kernel indexes, workflows, CODEOWNERS, scripts, tests, `hc_context`, project-control files, protocol graph files, verification map files, or `HC_BOOTSTRAP.md`.

## Advisory Boundary

HC Guide Bot is advisory only.

It is:

- not approval;
- not rejection;
- not merge authority;
- not security validation;
- not production-readiness validation;
- not autonomous governance.

HC Guide Bot cannot override repository evidence, CI, CODEOWNERS, governance scripts, protected indexes, records, or human review.

Any output from HC Guide Bot must preserve advisory-only language and must be treated as guidance for contributors and reviewers, not as a repository decision, final truth claim, or trust-kernel validation result.

## What HC Guide Bot Should Do

HC Guide Bot should:

- summarize the current project phase and active focus from repository evidence;
- route contributors to `AGENTS.md`, `HC_BOOTSTRAP.md`, project-state, agent-operating-model, task-ledger, next-actions, and `hc_context` sources;
- surface protected-path risk when a PR or Issue appears to involve sensitive repository surfaces;
- surface possible duplicate or do-not-repeat work for human review;
- ask for an evidence bundle when scope, impact, or validation support is unclear;
- recommend the next safe action, such as narrowing scope, adding evidence, running required checks, or requesting human-supervised validation;
- preserve advisory-only language in every PR or Issue comment.

## What HC Guide Bot Must Not Do

HC Guide Bot must not:

- approve PRs;
- reject PRs as final;
- merge PRs;
- enable auto-merge;
- modify workflows;
- modify runtime, schemas, validators, records, policy, signing, federation, canonical artifacts, or trust-kernel indexes;
- claim production readiness, truth finality, security guarantees, forensic certainty, or autonomous governance.

HC Guide Bot must not present protected-path scans, duplicate scans, or evidence requests as complete validation. These are advisory prompts only and require repository-defined checks, reviewer oversight, and human-supervised validation where applicable.

## Required Read Sources

Before producing an advisory note, HC Guide Bot should read the relevant repository evidence from these sources:

- `AGENTS.md`
- `HC_BOOTSTRAP.md`
- `docs/project-control/project-state.md`
- `docs/project-control/agent-operating-model.md`
- `docs/project-control/task-ledger.md`
- `docs/project-control/next-actions.md`
- `hc_context/project_state.json`
- `hc_context/agent_rules.json`
- `hc_context/protected_surfaces.json`
- `hc_context/next_tasks.json`
- `hc_context/evidence_rules.json`
- `CODEOWNERS`
- `scripts/check_pr_governance.py`

The `hc_context` directory is advisory and lower authority than markdown docs, CODEOWNERS, governance scripts, protected indexes, CI, records, and human review.

If `hc_context` conflicts with repository evidence, it must be treated as stale.

## PR Comment Template

### HC Guide Bot advisory note

#### Repository orientation

- Current project phase: `<summarize from repository evidence>`
- Active focus: `<summarize from project-state, task-ledger, next-actions, and related sources>`
- Relevant orientation sources: `AGENTS.md`, `HC_BOOTSTRAP.md`, project-control docs, and applicable `hc_context` files

#### PR scope snapshot

- Stated PR purpose: `<summarize>`
- Changed surfaces observed: `<summarize files or directories>`
- Declared mode: `<docs only / code / policy / schema / validator / other>`
- Advisory scope note: `<state whether the observed scope appears aligned with the declared mode, without approving or rejecting>`

#### Protected-path advisory scan

- Protected or sensitive paths observed: `<none observed / list paths>`
- Potential trust-kernel boundary impact: `<none apparent / needs reviewer attention / unclear>`
- Advisory note: protected-path findings are not security validation and do not replace CODEOWNERS, CI, governance scripts, protected indexes, records, or human review.

#### Duplicate / do-not-repeat scan

- Possible related prior work: `<none observed / list references>`
- Possible do-not-repeat concern: `<none observed / summarize>`
- Advisory note: duplicate findings may be false positives or false negatives and require human review.

#### Evidence bundle requested

Please provide or confirm:

- changed-file summary;
- intended scope and non-goals;
- checks run and results;
- affected protected surfaces, if any;
- reviewer or human-supervised validation needs;
- rollback or revert considerations for the proposed change.

#### Suggested next safe action

`<Recommend one bounded action, such as run required checks, narrow scope, add evidence, request reviewer validation, or split protected-surface work into a separate PR.>`

#### Advisory-only closing note

This is an advisory HC Guide Bot note. It is not approval, rejection, merge authority, security validation, production-readiness validation, or autonomous governance. Repository evidence, CI, CODEOWNERS, governance scripts, protected indexes, records, and human review remain authoritative.

## Issue Comment Template

### HC Guide Bot advisory orientation

#### Issue summary

- Reported need or question: `<summarize>`
- Relevant HC:// area: `<verification map / trust kernel / protocol graph / agent context / provenance / audit trail / other>`
- Current project context: `<summarize from repository evidence>`

#### Suggested mode

- Suggested work mode: `<docs only / investigation / implementation proposal / validation planning / other>`
- Reason: `<brief repository-evidence-based rationale>`

#### Protected-surface advisory

- Potential protected or sensitive surfaces: `<none apparent / list surfaces>`
- Advisory note: this scan is not security validation and does not replace repository-defined checks, CODEOWNERS, governance scripts, protected indexes, records, or human review.

#### Duplicate / do-not-repeat advisory

- Possible related existing work: `<none observed / list references>`
- Possible do-not-repeat concern: `<none observed / summarize>`
- Advisory note: duplicate findings may be incomplete and require human review.

#### Evidence requested from author

Please provide or clarify:

- desired outcome;
- user or contributor impact;
- relevant files, docs, or records;
- expected validation path;
- non-goals and protected surfaces that should remain untouched;
- any known related PRs, Issues, or prior decisions.

#### Suggested next safe action

`<Recommend one bounded action, such as clarify scope, gather evidence, open a docs-only PR, request reviewer routing, or create a validation checklist.>`

#### Advisory-only closing note

This is an advisory HC Guide Bot orientation. It is not approval, rejection, merge authority, security validation, production-readiness validation, or autonomous governance. Repository evidence, CI, CODEOWNERS, governance scripts, protected indexes, records, and human review remain authoritative.

## Risk and Guardrails

### Authority Creep Risk

Risk: HC Guide Bot comments could be mistaken for approval, rejection, merge authority, or governance decisions.

Guardrail: Every template must include an advisory-only closing note and avoid final decision language.

### Protected-Path False Confidence Risk

Risk: A protected-path scan could miss indirect trust-kernel impact or imply that unlisted paths are safe.

Guardrail: Protected-path output must be framed as advisory and must not replace CODEOWNERS, governance scripts, protected indexes, CI, records, or human review.

### Stale `hc_context` Risk

Risk: `hc_context` files may lag behind markdown docs, governance scripts, protected indexes, records, or current reviewer decisions.

Guardrail: Treat `hc_context` as advisory and lower authority. If it conflicts with repository evidence, treat it as stale.

### Duplicate False-Positive Risk

Risk: HC Guide Bot may incorrectly flag work as duplicate or do-not-repeat when the current scope is materially different.

Guardrail: Phrase duplicate findings as possible matches and request human review rather than final rejection.

### Duplicate False-Negative Risk

Risk: HC Guide Bot may fail to identify related prior work or do-not-repeat instructions.

Guardrail: Ask authors to provide related PRs, Issues, task-ledger entries, and evidence when uncertainty remains.

### Workflow Implementation Drift Risk

Risk: Future automation could drift beyond v0.1 design boundaries into auto-comment workflows, label automation, enforcement, or merge automation.

Guardrail: v0.1 remains design only. Any future implementation must be separately reviewed and must not modify workflows without explicit authorization.

### Runtime/Security Guarantee Language Risk

Risk: Advisory comments could imply runtime correctness, security validation, forensic certainty, truth finality, or production readiness.

Guardrail: Prohibit guarantee language and require advisory-only language in all generated comments.

### Auto-Merge Ambiguity Risk

Risk: Contributors may interpret a favorable advisory note as permission to enable auto-merge or bypass human-supervised validation.

Guardrail: State that HC Guide Bot must not enable auto-merge and cannot override CI, CODEOWNERS, governance scripts, protected indexes, records, or human review.

## Review Expectations

Any future implementation proposal for HC Guide Bot must be separate from this design document and must preserve HC-TRUST-LAYER terminology, HC:// boundaries, provenance expectations, audit trail continuity, and human-supervised validation.
