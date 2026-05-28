# HC-TRUST-LAYER Governance Enforcement Baseline

This document defines repository-management enforcement guidance for HC:// in HC-TRUST-LAYER while preserving advisory-only runtime semantics and human-supervised control.

## Scope and non-goals

This baseline is governance and process guidance for protected-branch operation.

Non-goals:

- no canonical schema updates
- no validator behavior changes
- no signing or security workflow changes
- no runtime semantic changes
- no unrestricted autonomous merge behavior
- no production-readiness or autonomous-authority claims

## Branch protection baseline

Protected branches should enforce:

- required pull request review before merge
- required status checks before merge
- blocking of direct pushes except maintainers with emergency procedures
- dismissal of stale approvals after material updates
- linear, auditable merge history where feasible

This baseline preserves human-supervised validation for consequential changes and keeps merge authority human-controlled.

## Required status checks for protected branches

Protected branches should require the following checks when available in CI:

- runtime tests
- terminology guard (`python scripts/check_terminology.py`)
- docs drift guard (`python scripts/check_docs_drift.py`)
- canonical artifact guard (`python scripts/check_canonical_artifacts.py`)
- CodeQL/security checks (if configured)

A pull request is not merge-eligible when required checks are skipped, missing, or failing.

## Required human review boundaries for protected paths

Changes touching the following paths require explicit human-supervised review and are not low-risk auto-merge eligible:

- `schema/**`
- `validators/**`
- `signatures/**`
- `policy/**`
- `federation/**`
- `.github/workflows/**`
- `src/hc_runtime/**`

Repository CODEOWNERS boundaries should align with these protected paths so review routing remains explicit and auditable.

## Low-risk auto-merge eligibility (bounded)

Auto-merge may be considered only when all required checks pass and the pull request is clearly low-risk, including:

- docs-only changes
- dependency patch updates with no trust-kernel behavior impact
- test-only hardening that does not alter runtime semantics
- non-semantic governance documentation updates

Even in low-risk cases, auto-merge remains supervised automation under repository policy, not unrestricted autonomous governance.

## Auto-merge blocking rules

Auto-merge must be blocked when any of the following applies:

- required checks are skipped
- required checks fail
- runtime semantics are modified
- validator, schema, signing/security, policy, or federation surfaces are changed
- diff scope is large, scattered, or insufficiently auditable

When blocked, merge authority remains with maintainers through explicit human-supervised approval.

## PR risk classification guidance

### LOW

Typical signals:

- docs-only or non-semantic governance updates
- small, focused dependency patch updates
- test-only hardening with no runtime semantic impact

Expected handling:

- required checks pass
- at least one human reviewer confirms low-risk scope

### MEDIUM

Typical signals:

- multi-file operational updates without protected-path modifications
- moderate implementation or refactor scope with bounded trust-kernel exposure

Expected handling:

- required checks pass
- expanded reviewer attention on provenance and audit trail continuity
- optional escalation when trust-kernel adjacency is unclear

### HIGH

Typical signals:

- touches protected paths or trust-kernel-adjacent boundaries
- affects policy interpretation, validator behavior, runtime semantics, or security-sensitive controls
- includes large/scattered change sets with elevated audit complexity

Expected handling:

- required checks pass
- explicit multi-reviewer human-supervised validation
- no autonomous merge pathway

## Minimal maintainer workflow

1. AI-assisted contributors generate pull requests with scoped, auditable changes.
2. CI validates required checks and reports results.
3. Human reviewers supervise scope, risk, and policy alignment.
4. Maintainers retain human-controlled merge authority.

This workflow keeps AI output advisory and preserves human-supervised validation for consequential decisions.

## Governance linkage map

Apply this baseline together with:

- supervised automation policy: `docs/supervised_automation_policy.md`
- CODEOWNERS review boundaries: `CODEOWNERS`
- runtime stabilization audit note: `docs/runtime-stabilization-post-audit-note.md`
- local runtime runbook: `docs/local_runtime_runbook.md`

## Implementation note

This document is governance guidance only. It does not change canonical records, schemas, validators, signing semantics, federation behavior, policy evaluator semantics, or runtime behavior.
