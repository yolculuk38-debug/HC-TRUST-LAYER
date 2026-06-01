# Branch Protection Enforcement Baseline

This document records the protected-branch enforcement model identified during governance review for HC-TRUST-LAYER and HC://. It is documentation only and does not change workflows, repository settings, schemas, validators, runtime behavior, policy interpretation, signing semantics, federation behavior, or canonical records.

## 1. Branch protection goals

Protected branches should preserve a reviewable audit trail by requiring pull request review, required status checks, and human-supervised validation before merge. The baseline supports these goals:

- prevent unsupervised direct changes to protected branches;
- keep trust-kernel-adjacent changes visible to maintainers;
- preserve canonical record, verification map, and protocol graph review boundaries;
- keep CI and governance guardrails intact before merge; and
- maintain human-controlled merge authority for consequential changes.

## 2. Recommended required status checks

The following checks are recommended as required protected-branch status checks when configured in repository CI:

- `terminology`
- `docs-drift`
- `canonical-artifacts`
- `automation-gate`
- `governance-preflight`
- `verification-package-schema`

`validate.yml` is scope-dependent. It should be required for changes in the paths or file types covered by that workflow, but this document does not expand its trigger scope or require it for unrelated documentation-only changes.

## 3. Advisory checks

The following checks provide advisory signal for review, routing, or repair guidance and should not replace required human review:

- `policy-evaluation`
- `pr-scope-guard`
- `terminology-autofix-suggest`

Advisory checks may help reviewers identify policy, scope, or terminology issues, but they do not grant autonomous governance finality.

## 4. Review requirements

Protected branches should require pull request review before merge. Review should confirm that the change scope is accurate, required checks have reported, and trust-kernel-impacting changes receive explicit human-supervised validation.

Stale approvals should be dismissed after material updates when the diff changes review assumptions, protected paths, or canonical record boundaries.

## 5. Auto-merge restrictions

Auto-merge must remain bounded and human-supervised. It is not appropriate when a pull request:

- touches protected paths;
- changes runtime verification behavior, schemas, validators, signing, federation, or policy evaluation;
- has failing, missing, or skipped required checks;
- has unresolved reviewer concerns; or
- expands beyond a small, auditable scope.

Documentation-only changes may be considered low risk only when required checks pass and reviewers confirm that no protected branch, trust kernel, or canonical record boundary is affected.

## 6. Protected paths

The following paths should be treated as protected review surfaces for branch protection and merge routing:

- `.github/workflows/**`
- `schema/**`
- `validators/**`
- `signatures/**`
- `policy/**`
- `federation/**`
- `src/hc_runtime/**`

Changes touching these paths require explicit maintainer review and are not eligible for unattended auto-merge.

## 7. Human-controlled merge authority

Maintainers retain final merge authority for protected branches. CI status, automation labels, and advisory checks inform review, but they do not replace human-supervised validation or reviewer judgment.

This baseline preserves HC-TRUST-LAYER governance boundaries without making production-readiness claims or adding new repository rules beyond the documented governance review model.
