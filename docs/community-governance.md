# Community Governance Summary

> **Documentation Status**
> - **status:** GUIDE
> - **scope:** Public-facing contributor summary for HC-TRUST-LAYER governance expectations.
> - **canonical relevance:** Advisory governance orientation; not a canonical record, schema, validator, policy, signing, federation, or runtime surface.
> - **runtime relevance:** None; this guide does not define runtime enforcement logic.

## 1. Purpose

This guide explains how HC-TRUST-LAYER governance works for contributors, maintainers, reviewers, AI-assisted contributors, and future advisory bots or agents.

It is meant to be readable before a first contribution. It summarizes responsibilities, review expectations, sensitive boundaries, and the meaning of governance outcomes without creating new approval authority or runtime behavior.

Governance documentation is advisory and documentation-oriented. It helps people understand repository expectations, but it does not replace repository evidence, required checks, reviewer judgment, or human-supervised validation.

## 2. Governance Philosophy

HC-TRUST-LAYER governance is based on careful, evidence-based review of HC:// verification infrastructure.

The project prefers:

- small, scoped, reviewable changes
- documentation-first clarification before behavior changes
- clear provenance and audit trail continuity
- explicit review for protected surfaces
- human-supervised validation for sensitive trust-kernel-impacting changes
- careful language about what the repository does and does not prove

Governance requirements, evidence requirements, audit expectations, protected-path boundaries, and validation expectations apply consistently regardless of role.

## 3. Repository Evidence Principle

Repository evidence is authoritative.

Contributors should use the repository as the source of truth for architecture, implementation status, verification map entries, protocol graph references, policy baselines, audit trail expectations, and documented limitations.

Do not replace repository evidence with assumptions, external descriptions, generated summaries, aspirational roadmaps, or unsupported claims. If evidence is incomplete or unclear, say so and ask for review rather than filling the gap with certainty language.

## 4. Roles and Responsibilities

Different roles may have different responsibilities, permissions, authority scopes, and review obligations.

### Contributor

A Contributor proposes issues, documentation updates, examples, tests, or implementation changes. Contributors are responsible for keeping changes scoped, preserving HC:// and HC-TRUST-LAYER terminology, running applicable checks, and explaining evidence for their changes.

### Maintainer

A Maintainer helps guide repository direction, triage issues and pull requests, preserve review boundaries, coordinate required checks, and decide whether a change is ready for merge under repository rules.

### Reviewer

A Reviewer evaluates a proposed change for correctness, scope, terminology, evidence, protected-surface impact, audit trail continuity, and validation needs. Reviewers may request changes, identify missing evidence, or require human-supervised validation before a sensitive change proceeds.

### Founder / project steward

The Founder / project steward preserves project identity, long-term direction, terminology continuity, and high-level governance boundaries. This role may provide stewardship guidance, but governance still depends on repository evidence, documented review expectations, and required validation.

### AI-assisted contributor

An AI-assisted contributor uses AI tools to help draft, review, or organize a contribution. AI-assisted contributions are advisory and require review. The human contributor remains responsible for checking repository evidence, avoiding unsupported claims, and ensuring the contribution is suitable for maintainer and reviewer evaluation.

### Future advisory bot or agent

A future advisory bot or agent may help with navigation, checks, summaries, triage hints, or review preparation. Its output is advisory. It does not create merge authority, approval authority, governance finality, or validation by itself.

## 5. Contributor Expectations

Contributors can expect the project to favor transparent, evidence-based review over unsupported certainty.

Contributors should:

- keep changes small and easy to review
- explain what files and surfaces are affected
- preserve canonical terminology such as HC-TRUST-LAYER, HC://, verification map, trust kernel, protocol graph, provenance, audit trail, canonical record, and human-supervised validation
- run required checks for the touched scope
- avoid protected paths unless explicitly requested and clearly reviewed
- avoid production, security, forensic, truth-finality, or autonomous-governance claims unless supported by repository evidence and validation
- ask before changing runtime behavior, schemas, validators, records, policy, federation, signing, workflows, trust-kernel indexes, or other protected surfaces

Contributors can expect maintainers and reviewers to ask for evidence when claims are unclear or when a change may affect sensitive review boundaries.

## 6. Maintainer Expectations

Maintainers help keep the repository auditable and reviewable.

Maintainers should:

- triage changes according to documented scope and risk
- preserve CI and governance guardrails
- identify whether a pull request is documentation-only or touches protected surfaces
- route sensitive work to suitable reviewers
- require human-supervised validation when a sensitive trust-kernel-impacting change is proposed
- avoid implying production readiness, security certification, truth finality, forensic certainty, or autonomous governance
- ensure governance decisions are grounded in repository evidence

Maintainer action does not eliminate the need for checks, evidence, audit trail continuity, or reviewer attention where required.

## 7. Reviewer Expectations

Reviewers evaluate whether a contribution is accurate, scoped, and safe for the affected surface.

Reviewers should check:

- whether the change matches repository terminology
- whether claims are supported by repository evidence
- whether protected surfaces are touched directly or indirectly
- whether audit trail continuity or provenance continuity may be affected
- whether the contribution changes policy interpretation, verification behavior, schema contracts, validator logic, federation behavior, signing semantics, records, or trust-kernel indexes
- whether human-supervised validation is required
- whether required checks passed or were clearly documented as unable to run

Reviewer approval is not a claim of objective truth, forensic certainty, production readiness, or security certification.

## 8. AI-Assisted Contribution Expectations

AI-assisted contributions are advisory and require review.

AI-assisted contributors may use AI tools to:

- draft documentation
- improve readability
- identify broken links or terminology drift
- prepare summaries of repository evidence
- suggest review checklists
- assist with scoped, human-reviewed changes

AI-assisted contributors may not use AI output to:

- override repository evidence
- claim implementation status that is not documented in the repository
- bypass required checks
- bypass human-supervised validation
- alter protected surfaces without explicit scope and review
- create autonomous governance, merge approval, security certification, or final truth determinations

The person submitting the contribution remains accountable for reviewing AI output and correcting unsupported claims.

## 9. Human-Supervised Validation

Human-supervised validation remains required for sensitive trust-kernel-impacting changes.

Human-supervised validation means that qualified humans review the proposed change, repository evidence, check results, affected boundaries, and expected impact before the change is treated as acceptable for sensitive areas.

Human-supervised validation may be required when a change affects or could affect:

- runtime verification behavior
- schema contracts
- validator logic
- signing or trust anchor semantics
- federation behavior
- policy evaluator behavior
- canonical record identity
- provenance continuity
- audit trail continuity
- trust-kernel indexes or review routing

Automated checks and AI-generated summaries can support this process, but they do not replace it.

## 10. Trust-Kernel-Sensitive Changes

Trust-kernel-sensitive work means any change that can affect the boundaries used to evaluate HC:// verification behavior, provenance continuity, canonical record handling, policy interpretation, or audit trail expectations.

A change may be trust-kernel-sensitive even if it appears small. For example, a wording change that implies a new guarantee, a schema edit that changes record interpretation, or a validator adjustment that changes pass/fail behavior can affect trust kernel review boundaries.

If a contributor is unsure whether a change is trust-kernel-sensitive, they should treat it as review-required and ask for maintainer guidance before proceeding.

## 11. Protected Surfaces

Protected surfaces are paths, behaviors, or governance boundaries where changes may affect HC:// verification meaning, auditability, or trust-kernel review.

Protected surfaces include:

- `.github/workflows/**`
- `schema/**`
- `validators/**`
- `records/**`
- `policy/**`
- `federation/**`
- `signatures/**`
- `canonical/**`
- trust-kernel indexes
- runtime verification behavior
- schema definitions and deterministic serialization assumptions
- hash-linked artifacts
- record identity and provenance continuity
- validator logic
- signing and trust anchor semantics
- federation behavior
- policy evaluator behavior
- governance controls

Do not modify protected surfaces unless the task explicitly requests it and the review path is clear.

## 12. Decision Boundaries

Governance decisions document review outcomes inside the repository. They do not prove universal truth or external correctness.

A governance decision may indicate that:

- a change is acceptable for merge under repository rules
- a change needs more evidence
- a change is out of scope
- a change requires specialist review
- a change requires human-supervised validation
- a claim must be narrowed or removed
- a protected surface must not be changed in the current PR

A governance decision should remain tied to repository evidence, recorded checks, review comments, and the affected surface.

## 13. Governance Outcomes

Governance outcomes may include documentation clarification, issue triage, requested changes, maintainer review, reviewer approval, rejection, deferral, or a requirement for human-supervised validation.

A governance outcome can help create a clearer audit trail for why a change was accepted, changed, delayed, or rejected.

Governance outcomes are not guarantees that every future condition has been considered. They are scoped decisions based on the repository evidence available at the time of review.

## 14. What Governance Is Not

Governance does not create merge authority, approval authority, security certification, production readiness, forensic certainty, truth finality, or autonomous governance.

Governance documentation does not create independent legal, operational, cryptographic, or policy guarantees. It is not a substitute for repository checks, maintainer review, reviewer evaluation, or human-supervised validation where required.

Governance does not make AI-assisted output authoritative. AI-assisted summaries, draft text, review hints, or bot output remain advisory until reviewed through repository-defined processes.

## 15. What Not To Claim

Do not claim any of the following unless repository evidence and required validation explicitly support the claim:

- production readiness
- live federation guarantees
- complete dispute automation
- autonomous governance finality
- security certification
- forensic certainty
- objective truth finality
- cryptographic guarantees not backed by tests and documentation
- policy guarantees not backed by tests and documentation
- merge authority or approval authority created by governance text
- autonomous validation by an AI tool, bot, or agent

Use careful language such as "repository evidence indicates," "the current documentation describes," "requires review," "requires human-supervised validation," and "advisory" when describing HC:// governance outcomes.

## 16. Related Documents

- [`README.md`](../README.md)
- [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- [`docs/contributor-start-here.md`](contributor-start-here.md)
- [`docs/verification-map.md`](verification-map.md)
- [`docs/verification-map-index.md`](verification-map-index.md)
- [`docs/protocol-graph-index.md`](protocol-graph-index.md)
- [`docs/trust-kernel-index.md`](trust-kernel-index.md)
- [`docs/pr-scope-boundaries.md`](pr-scope-boundaries.md)
- [`docs/trust-impact-analysis.md`](trust-impact-analysis.md)
- [`docs/trust-review-workflow.md`](trust-review-workflow.md)
- [`docs/ai-assisted-review.md`](ai-assisted-review.md)
- [`docs/ai-collaboration-workflow.md`](ai-collaboration-workflow.md)
- [`docs/limitations-and-risks.md`](limitations-and-risks.md)
- [`SECURITY.md`](../SECURITY.md)
