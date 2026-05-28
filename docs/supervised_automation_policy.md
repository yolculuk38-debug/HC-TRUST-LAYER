# Supervised Automation and Safe Auto-Merge Policy

> **Status:** Draft policy baseline (documentation-only)
> 
> **Scope:** HC-TRUST-LAYER repository contribution workflow
> 
> **Boundary:** Advisory governance policy for AI-assisted pull-request flow; no runtime enforcement changes

## Purpose

This policy defines how HC-TRUST-LAYER can use controlled AI-assisted pull request support while preserving HC:// human-supervised validation boundaries.

The policy enables limited safe auto-merge for clearly low-risk changes and blocks or escalates changes that can affect trust-kernel boundaries, provenance continuity, canonical record assumptions, validator behavior, or security posture.

## Non-Goals and Guardrails

This policy does **not**:

- enable unrestricted auto-merge
- authorize autonomous governance
- alter runtime behavior
- alter canonical schema contracts
- alter validator logic
- alter signing or trust-anchor semantics
- alter federation behavior
- bypass required checks or reviewer oversight

## Allowed Low-Risk Safe Auto-Merge Categories

A PR may be considered a safe automation candidate only when it is fully contained within one or more of these categories:

1. **Docs-only typo/clarity updates**
   - spelling, grammar, wording clarity, navigation links
   - no semantic changes to protected policy/runtime/security boundaries

2. **Dependency patch updates**
   - patch-version dependency bumps only
   - no major/minor jumps without human review
   - no security workflow or signing-path impact

3. **Test-only hardening**
   - improved test coverage, fixtures, or assertions
   - no production runtime semantic changes

4. **Guardrail documentation updates**
   - clearer contribution guidance, risk routing, and verification workflow instructions
   - preserves existing guardrail intent and review requirements

## Forbidden Auto-Merge Areas

Any PR touching the following areas is **not** eligible for safe auto-merge and requires human-supervised validation:

- `schema/**`
- `validators/**`
- `signatures/**`
- `policy/**`
- `federation/**`
- `.github/workflows/**`
- runtime semantic changes (regardless of file path)
- security- or secret-related changes (regardless of file path)

## Protected Path Ownership Policy

HC-TRUST-LAYER uses `CODEOWNERS` as a governance boundary for protected protocol/runtime/security areas.

- Protected paths must include an explicit owner assignment.
- Changes in protected paths require explicit human review and must not be treated as autonomous governance.
- Low-risk docs/test/dependency patch changes outside protected paths may be considered safe automation candidates when all required checks pass.
- Runtime, schema, validator, signing/security, policy, federation, and workflow paths remain manual-approval routes under human-supervised validation.

## Required Gates Before Any Safe Auto-Merge

All gates below must pass for a PR to be eligible for safe auto-merge:

1. **All required checks pass**.
2. **No protected paths changed**.
3. **`advisory_only` semantics are preserved**.
4. **`truth_guarantee=false` semantics are preserved**.
5. **`public_safe` behavior is preserved**.
6. **No claims of production readiness, objective truth, or autonomous governance**.
7. **PR diff is small and tightly scoped**.

If any gate fails, is skipped, or is inconclusive, safe auto-merge is disabled and manual review is required.

## Human Approval Required Cases

Human approval is mandatory for PRs that include any of the following:

- runtime behavior changes
- validator or schema changes
- federation changes
- security-sensitive changes
- failed, skipped, or missing required checks

These cases are outside safe automation boundaries and must remain under explicit human-supervised validation.

## PR Risk Classification

| Risk Level | Definition | Merge Routing |
|---|---|---|
| **LOW** | Safe automation candidate: allowed low-risk category only, all gates pass, no protected paths changed. | May be auto-merged under this policy. |
| **MEDIUM** | Non-protected but non-trivial change, ambiguous impact, or scope larger than safe baseline. | Human review required before merge. |
| **HIGH** | Protected-path touch, runtime semantic impact, security-sensitive impact, or required-check failure/skip. | Block auto-merge; manual review required. |

## AI-Assisted Workflow Expectations

AI-assisted authoring and review support are advisory tools only.

- Maintain clear audit trail continuity in commit/PR history.
- Keep PR scope small, reversible, and reviewer-readable.
- Preserve HC:// and HC-TRUST-LAYER terminology.
- Route trust-kernel-impacting or cross-domain changes to appropriate human reviewers.

## Enforcement Posture

This document defines policy expectations for supervised automation design and reviewer operation.

Implementation of enforcement mechanisms should be incremental, bounded, explainable, and reversible, with human-supervised validation retained as the controlling merge authority outside LOW-risk safe automation categories.
