# PR Scope Boundaries for HC-TRUST-LAYER

This document defines an advisory boundary guard for HC:// pull requests so reviewers can quickly identify whether a change drifts into sensitive trust-kernel areas.

## Why scoped PRs matter

Scoped pull requests preserve review quality, reduce ambiguity, and keep the HC-TRUST-LAYER audit trail easier to interpret.

When a pull request only changes intended surfaces, human-supervised validation remains focused on the declared protocol graph and verification map impact.

## Why AI tools can drift outside scope

AI-assisted workflows can produce broad edits that include nearby files with related terminology, even when those files are out of task scope.

In HC-TRUST-LAYER, that drift can unintentionally touch high-sensitivity boundaries such as canonical record, policy, and federation areas that require explicit reviewer escalation.

## Protected path classes

The first-phase scope guard classifies these paths as protected:

- `schema/**`
- `validators/**`
- `federation/**`
- `signatures/**`
- `canonical/**`
- `policy/**`

## Docs-only PR boundary

For docs-only pull requests, allowed paths are intentionally narrow:

- `docs/**`
- approved guard script path: `scripts/check_pr_scope.py`

Any other changed path is reported as an unexpected scope violation.

## Safe vs unsafe automation boundaries

Safe automation boundary behavior:

- report changed protected files
- report allowed scope
- report unexpected scope violations
- preserve human review authority

Unsafe automation boundary behavior (not used in this phase):

- auto-merging despite unresolved protected boundary uncertainty
- replacing reviewer decision-making on trust-kernel-impacting scope
- asserting production or policy guarantees beyond repository evidence

## Phase status

Current phase is advisory-only reporting.

The guard surfaces findings but does not auto-block merge so reviewers retain final authority under human-supervised validation.
