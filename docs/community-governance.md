# Community Governance Summary

> **Documentation Status**
> - **status:** GUIDE
> - **scope:** Public-facing contributor governance summary for HC-TRUST-LAYER.
> - **canonical relevance:** Advisory governance documentation; not a canonical record, schema, validator, policy, signing, federation, runtime, or trust-kernel index surface.
> - **runtime relevance:** None; this document does not define runtime enforcement logic.

## 1. Purpose

This document summarizes how community governance works for HC-TRUST-LAYER contributors, maintainers, reviewers, and AI-assisted participants.

It is intended to help contributors understand review expectations, evidence boundaries, protected surfaces, and when human-supervised validation is required.

Governance is advisory and documentation-oriented. It helps route discussion and review, but it does not replace repository checks, maintainer review, or repository-defined validation.

## 2. Governance Philosophy

HC-TRUST-LAYER governance is based on transparent documentation, scoped review, provenance-aware discussion, and respect for repository evidence.

Contributors should prefer small, auditable, reversible changes. Documentation-first clarification is preferred before changes that could alter HC:// behavior, trust kernel boundaries, verification map meaning, protocol graph interpretation, or audit trail continuity.

Governance does not create autonomous governance. It provides contributor-facing expectations for review, escalation, and responsible participation.

## 3. Repository Evidence Principle

Repository evidence is authoritative.

Public discussion, AI output, external assumptions, and informal interpretation must not override in-repository documentation, implementation status, validation outputs, provenance records, or documented boundary language.

When repository evidence is incomplete or ambiguous, contributors should surface the uncertainty, cite the relevant files or checks, and ask for review rather than inventing unsupported guarantees.

## 4. Roles and Responsibilities

HC-TRUST-LAYER participation may involve several roles:

- **Contributors** propose scoped changes, report issues, improve documentation, and preserve repository terminology.
- **Maintainers** triage issues and pull requests, preserve guardrails, coordinate review, and clarify repository direction.
- **Reviewers** evaluate changes against repository evidence, validation results, trust-kernel sensitivity, and contributor expectations.
- **AI-assisted contributors** may draft, summarize, inspect, or propose changes, but their output remains advisory and requires review.

A participant may hold more than one role, but role overlap does not remove the need for review, checks, or human-supervised validation where required.

## 5. Contributor Expectations

Contributors are expected to:

- Preserve HC-TRUST-LAYER and HC:// terminology.
- Keep changes small, scoped, reviewable, and reversible.
- Cite repository evidence when proposing changes to architecture, governance, verification flow, provenance, or audit trail language.
- Run applicable checks before requesting review.
- Avoid modifying protected surfaces unless the task explicitly requires it and the review path is clear.
- Avoid production readiness, forensic certainty, truth finality, autonomous governance, or unsupported security claims.
- Ask for review when a change may affect the trust kernel, protocol graph, verification map, canonical record continuity, policy interpretation, signing semantics, federation behavior, schema contracts, validators, or runtime verification behavior.

## 6. Maintainer Expectations

Maintainers are expected to:

- Preserve repository guardrails and review boundaries.
- Route changes to appropriate reviewers when scope crosses documentation, policy, security, runtime, validator, signing, federation, schema, or canonical record surfaces.
- Require checks appropriate to the touched scope.
- Keep governance decisions tied to repository evidence.
- Identify when human-supervised validation remains required for sensitive trust-kernel-impacting changes.
- Avoid presenting governance discussion as security certification, production approval, forensic certainty, truth finality, or autonomous governance.

## 7. Reviewer Expectations

Reviewers are expected to:

- Evaluate whether the change matches its stated scope.
- Confirm that repository terminology and boundary language are preserved.
- Check whether protected surfaces or trust-kernel-sensitive boundaries are affected.
- Review validation results without implying that advisory checks provide broader guarantees than they do.
- Request clarification when evidence, scope, or expected impact is unclear.
- Preserve audit trail continuity by keeping review comments tied to concrete files, checks, and decisions.

Reviewer approval is a repository review action. It is not a claim of production readiness, security certification, truth finality, or forensic certainty.

## 8. AI-Assisted Contribution Expectations

AI-assisted contributions are advisory and require review.

AI tools may help draft documentation, summarize repository evidence, identify candidate checks, or propose scoped changes. AI output must not be treated as merge authority, approval authority, autonomous governance, or a substitute for maintainer and reviewer judgment.

AI-assisted work should:

- Preserve HC:// and HC-TRUST-LAYER terminology.
- Avoid unsupported claims about security, policy, production status, or forensic certainty.
- Identify uncertainty instead of filling gaps with assumptions.
- Keep generated changes small enough for human review.
- Run and report applicable repository checks when changes are proposed.

## 9. Human-Supervised Validation

Human-supervised validation remains required for sensitive trust-kernel-impacting changes.

This includes non-trivial changes that may affect canonical record continuity, deterministic serialization assumptions, validator logic, schema contracts, signing or trust anchor semantics, policy evaluator behavior, federation behavior, runtime verification behavior, or governance controls that protect those surfaces.

Human-supervised validation should be explicit, evidence-based, and tied to repository-defined checks and review records.

## 10. Trust-Kernel-Sensitive Changes

Trust-kernel-sensitive changes include direct or indirect updates that may affect:

- verification map interpretation
- trust kernel boundaries
- protocol graph meaning
- canonical record identity or provenance continuity
- audit trail continuity
- schema definitions or deterministic serialization assumptions
- validator behavior
- policy interpretation or routing
- signing and trust anchor semantics
- federation behavior
- runtime verification behavior

When in doubt, treat the change as trust-kernel-sensitive and ask for review before proceeding.

## 11. Protected Surfaces

Protected surfaces include, but are not limited to:

- workflows
- runtime
- schemas
- validators
- records
- policy
- federation
- signing
- trust-kernel indexes
- `hc_context`
- agent context documentation and agent workspaces
- canonical record surfaces

Governance documentation should not weaken controls over protected surfaces. Changes to protected surfaces require explicit scope, relevant checks, and appropriate human review.

## 12. Decision Boundaries

This governance summary helps contributors understand review and escalation paths, but it does not define final repository authority by itself.

Decision boundaries are determined by repository-maintained documentation, required checks, code ownership or maintainer review practices, and applicable human-supervised validation for sensitive changes.

A governance discussion may recommend a direction, but merge decisions and sensitive boundary changes must remain tied to repository evidence, checks, and reviewer oversight.

## 13. What Governance Is Not

Governance is advisory and documentation-oriented.

Governance does not create:

- merge authority
- approval authority
- security certification
- production readiness
- forensic certainty
- truth finality
- autonomous governance

Governance also does not replace validation, review, audit trail preservation, contributor responsibility, or maintainer judgment.

## 14. What Not To Claim

Do not claim that HC-TRUST-LAYER governance provides:

- merge authority
- approval authority
- security certification
- production readiness
- forensic certainty
- truth finality
- autonomous governance
- complete dispute automation
- live federation guarantees
- cryptographic or policy guarantees not backed by repository evidence and validation

Contributors should describe repository status using evidence from the repository and should avoid broader claims not supported by implemented and validated in-repository behavior.

## 15. Related Documents

Use this document alongside:

- [`README.md`](../README.md)
- [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- [`docs/contributor-start-here.md`](contributor-start-here.md)
- [`docs/pr-workflow.md`](pr-workflow.md)
- [`docs/issue-workflow.md`](issue-workflow.md)
- [`docs/maintainer-triage.md`](maintainer-triage.md)
- [`docs/pr-scope-boundaries.md`](pr-scope-boundaries.md)
- [`docs/limitations-and-risks.md`](limitations-and-risks.md)
- [`docs/verification-map.md`](verification-map.md)
- [`docs/protocol-graph-index.md`](protocol-graph-index.md)
- [`docs/trust-kernel-index.md`](trust-kernel-index.md)
- [`docs/trust-review-workflow.md`](trust-review-workflow.md)
- [`docs/ai-assisted-review.md`](ai-assisted-review.md)
- [`docs/ai-collaboration-workflow.md`](ai-collaboration-workflow.md)
