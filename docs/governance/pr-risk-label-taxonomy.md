# HC:// PR Risk Label Taxonomy and Automation Decision Matrix

This document defines the governance baseline for classifying pull requests in HC-TRUST-LAYER so AI-generated pull requests can be triaged consistently before human review or limited safe auto-merge.

Scope boundaries:

- Documentation-only governance guidance.
- Human-supervised validation remains required for consequential trust interpretation.
- No runtime behavior, canonical schema, validator logic, signing/security workflow, federation behavior, or policy evaluator changes are introduced by this document.
- No autonomous governance claims are made.

## Purpose

Establish a transparent, auditable classification standard that supports:

- consistent PR triage labels,
- bounded automation decisions,
- preserved reviewer accountability,
- and clear block conditions for high-sensitivity changes.

## Label taxonomy

### Core risk labels

- `risk-low`: low-impact, narrow-scope changes with no protected-path impact and no runtime semantic changes.
- `risk-medium`: moderate-impact changes that may alter governance interpretation, review routing, or runtime-adjacent confidence surfaces without direct protected-path modification.
- `risk-high`: high-sensitivity changes, including protected-path updates or runtime semantic changes, requiring explicit human-supervised validation.

### Automation routing labels

- `docs-auto`: documentation-focused changes that can be considered for bounded low-risk automation after required checks pass.
- `deps-auto`: dependency patch updates that remain low-risk and do not cross protected boundaries.
- `tests-auto`: test-only hardening changes that remain low-risk and do not alter runtime semantics.
- `blocked-human-review`: explicit block marker indicating automation is disallowed and human-supervised review is mandatory.

## Classification rules

### LOW classification candidates (`risk-low`)

Classify as LOW when all changed files and claims remain within safe documentation and maintenance boundaries, including:

- docs-only changes,
- typo or clarity edits,
- dependency patch updates,
- test-only hardening.

### MEDIUM classification candidates (`risk-medium`)

Classify as MEDIUM for changes such as:

- runtime tests,
- telemetry documentation,
- governance policy changes,
- non-semantic runtime-adjacent documentation.

MEDIUM classification still requires human-supervised validation before merge unless a separate repository-approved process explicitly narrows scope with equivalent safeguards.

### HIGH classification triggers (`risk-high`)

Classify as HIGH when any of the following are touched or proposed:

- `schema/**`
- `validators/**`
- `signatures/**`
- `policy/**`
- `federation/**`
- `.github/workflows/**`
- runtime semantic changes.

HIGH classification implies `blocked-human-review`.

## Automation decision matrix

| Condition | Label outcome | Automation outcome |
|---|---|---|
| Docs-only or typo/clarity, all required checks pass, no protected paths, small scoped diff | `risk-low` + `docs-auto` | Eligible for limited safe auto-merge consideration |
| Dependency patch, all required checks pass, no protected paths, small scoped diff | `risk-low` + `deps-auto` | Eligible for limited safe auto-merge consideration |
| Test-only hardening, all required checks pass, no protected paths, small scoped diff | `risk-low` + `tests-auto` | Eligible for limited safe auto-merge consideration |
| Any MEDIUM condition | `risk-medium` | Human-supervised review required before merge |
| Any HIGH trigger or protected-path change | `risk-high` + `blocked-human-review` | Auto-merge disallowed |
| Failed or skipped required checks | `blocked-human-review` | Auto-merge disallowed |
| Unsafe claims language present | `blocked-human-review` | Auto-merge disallowed |

## Auto-merge eligibility (bounded)

Auto-merge may be considered only when all conditions are true:

1. classification is LOW,
2. all required checks are green,
3. no protected paths are changed,
4. diff is small and tightly scoped,
5. no unsafe claims or authority-overreach language is present.

This is bounded automation, not unrestricted automation.

## Hard block conditions

Apply `blocked-human-review` when any of the following occur:

- required checks failed or were skipped,
- protected paths were changed,
- unsafe claims are present,
- wording implies production/objective-truth/autonomous-governance guarantees.

Blocked PRs require explicit human-supervised validation and reviewer disposition before merge consideration.

## Terminology and safety guardrails

- Preserve HC:// and HC-TRUST-LAYER canonical terminology.
- Preserve advisory-only AI posture and reviewer accountability.
- Do not present automation as autonomous governance.
- Keep governance decisions traceable in the audit trail and canonical record process boundaries.

## Implementation notes

- This taxonomy is governance guidance and does not modify runtime code or protected trust-kernel surfaces.
- Repository controls, required checks, and branch protections remain authoritative.
