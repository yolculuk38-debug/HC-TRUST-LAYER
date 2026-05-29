# Runtime Contract Risk Notes

Metadata:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- Runtime behavior change: none.
- Schema mutation: none.
- Workflow mutation: none.
- Human final authority: required.

## Purpose

These notes summarize runtime contract risks for HC:// reference runtime review without changing HC-TRUST-LAYER behavior.

## Verified repo findings

- Public runtime response builders include `advisory_only`, `public_safe`, `traceable`, and `truth_guarantee` fields.
- Runtime routes use advisory messages and warnings instead of production-readiness or final-truth claims.
- Runtime tests cover advisory response contracts, replay visibility, degraded recovery visibility, and public-safe redaction expectations.

## Contract risks to keep visible

- New routes could accidentally omit `advisory_only=true`, `public_safe=true`, or `truth_guarantee=false`.
- New warning text could imply final authority instead of human-supervised validation.
- New diagnostics could expose raw secret-bearing input, replay material, or credentials in public responses.
- New hardening controls could drift into schema, validator, signing, federation, policy, workflow, or governance mutation if scope is not reviewed.
- New blocking behavior could create autonomous enforcement semantics not approved by human reviewers.

## Runtime contract review checklist

- [ ] Public responses preserve `advisory_only=true`.
- [ ] Public responses preserve `public_safe=true`.
- [ ] Public responses preserve `truth_guarantee=false`.
- [ ] Warnings remain public-safe and concise.
- [ ] Human-supervised validation remains visible for consequential uncertainty.
- [ ] No runtime behavior change is introduced by documentation-only PRs.
- [ ] No schema mutation is introduced.
- [ ] No workflow mutation is introduced.
- [ ] No signing, validator, federation, or policy evaluator behavior changes are introduced.

## Relationship to security gap report

For the broader advisory-only gap report, checklist, secret handling review, and future-option tracking, see `docs/security/runtime-hardening-gap-report.md`.
