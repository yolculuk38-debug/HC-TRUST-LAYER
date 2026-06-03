# Maintainer Triage Guide

> **Documentation Status**
> - **status:** ACTIVE
> - **scope:** Maintainer-facing guidance for GitHub Issue and pull request triage.
> - **canonical relevance:** Advisory governance workflow guidance only; does not define canonical records, schemas, validators, signing, federation, policy, or trust-kernel indexes.
> - **runtime relevance:** None; this guide does not change runtime verification behavior.

## 1. Purpose

This guide helps HC-TRUST-LAYER maintainers triage public issues and pull requests consistently, safely, and with clear review boundaries.

Repository evidence is authoritative. Triage should preserve HC:// terminology, provenance, audit trail continuity, and documented trust-kernel boundaries. Triage is not approval authority. Labels are not merge authority.

## 2. Authority Boundary

Maintainer triage organizes review; it does not approve implementation, validate sensitive claims, or override repository-defined checks.

Maintainers should:

- use repository evidence as the source of truth
- classify scope, status, and sensitivity without expanding claims
- route sensitive or cross-domain work to appropriate reviewers
- keep issue and PR handling auditable
- require validation evidence before treating a change as ready for merge review

Maintainers must not use triage outcomes, issue comments, or labels as substitutes for required review, required checks, or human-supervised validation.

## 3. Triage Goals

Triage should make each item easier to review by identifying:

- whether the report or PR is in scope for HC-TRUST-LAYER
- whether it duplicates existing work or documentation
- what repository evidence supports or limits the request
- whether the item is documentation-only, behavioral, governance, research, or question-oriented
- whether protected surfaces or trust-kernel-sensitive areas may be affected
- which validation path and reviewers are needed
- whether public discussion is appropriate or private routing is required

## 4. New Issue Intake

For each new issue:

1. Confirm the issue describes an HC:// or HC-TRUST-LAYER concern.
2. Check whether the report includes enough evidence to understand the request.
3. Confirm public discussion is safe. If the issue includes security-sensitive details, route according to the repository security process and avoid amplifying sensitive information in public comments.
4. Compare the report with existing repository documentation before inferring missing behavior.
5. Apply initial labels for type, status, and sensitivity.
6. Ask for focused missing information when needed.
7. Document uncertainty rather than making unsupported production, security, truth, forensic, or governance claims.

If the issue lacks enough detail, use `status:needs-info` and ask for reproducible steps, affected files, expected outcome, actual outcome, and relevant repository evidence.

## 5. Duplicate Detection

Before accepting a new issue as distinct, search for related issues, PRs, documentation, roadmap notes, and known limitations.

A duplicate may point to:

- an existing open issue
- a closed issue with an applicable decision
- documented behavior in the verification map, protocol graph, or related guide
- an existing PR already addressing the same scope

When marking a duplicate:

- apply `status:duplicate`
- link the most relevant canonical discussion or active issue
- explain whether the duplicate is exact, partial, or related
- avoid implying that the linked item is approved unless it has completed required review

## 6. Evidence Review

Review evidence in this order:

1. repository files, documentation, and validation outputs
2. open and closed issues or PRs with maintainer decisions
3. referenced reproducible commands or logs
4. external references only when they are needed to understand context and do not override repository evidence

Repository evidence is authoritative. If repository evidence conflicts with an issue claim, triage should cite the repository evidence and ask whether the reporter is proposing a documentation clarification, implementation change, or research discussion.

Do not infer implementation status from aspirations, roadmap language, comments, or labels. Use explicit repository files and passing checks when discussing current behavior.

## 7. Issue Classification

Classify the issue by primary intent:

- bug report: alleged defect, regression, or mismatch between documented and observed behavior
- documentation request: clarification, navigation, terminology, or example improvement
- research proposal: exploratory idea, future capability, or open design question
- governance request: process, authority, validation, reviewer routing, or policy-boundary discussion
- question: request for explanation without a proposed repository change

If an issue spans multiple categories, choose the label that reflects the next maintainer action and add a comment noting secondary concerns.

## 8. Label Classification

Use labels to communicate triage state, not approval. Labels are not merge authority.

### Type

- `type:bug` — alleged defect or regression requiring evidence review
- `type:docs` — documentation, navigation, wording, examples, or non-behavioral clarification
- `type:research` — exploratory proposal or future capability discussion
- `type:governance` — review process, authority boundary, validation, or policy-adjacent workflow discussion
- `type:question` — explanation request without a confirmed change request

### Status

- `status:needs-triage` — item has not completed initial maintainer classification
- `status:needs-info` — more evidence, reproduction detail, or scope clarification is required
- `status:accepted` — maintainers agree the item is in scope for work or review; this is not merge approval
- `status:deferred` — item is in scope but not ready for current work
- `status:duplicate` — item overlaps an existing issue, PR, or documented decision
- `status:closed-no-action` — item is closed without repository change

### Sensitivity

- `sensitivity:public-safe` — public discussion is acceptable and no sensitive surface is apparent
- `sensitivity:security-sensitive` — public detail may expose misuse, vulnerability, operational risk, or sensitive security context
- `sensitivity:trust-kernel-sensitive` — item may affect trust-kernel behavior, interpretation, canonical record continuity, provenance, audit trail continuity, policy routing, validation semantics, or protected review boundaries

## 9. Trust-Kernel-Sensitive Assessment

Assess trust-kernel sensitivity before encouraging implementation.

Treat an issue or PR as trust-kernel-sensitive when it may affect:

- canonical record identity or provenance continuity
- verification map interpretation
- protocol graph semantics
- validator behavior or validation outputs
- schema contracts or deterministic serialization assumptions
- signing, trust anchor, or signature handling
- federation behavior or interoperability boundaries
- policy evaluator behavior or decision-path routing
- reviewer handoff, audit trail continuity, or human-supervised validation requirements

Human-supervised validation remains required for sensitive trust-kernel-impacting changes. If sensitivity is uncertain, label conservatively, explain the uncertainty, and route for reviewer assessment.

## 10. Protected Surface Assessment

Protected surfaces require heightened review and should not be modified through routine triage.

Protected surfaces include, but are not limited to:

- workflows and CI guardrails
- runtime verification behavior
- schemas
- validators
- records and canonical record artifacts
- policy files and policy evaluator behavior
- federation behavior
- signing and trust anchor semantics
- trust-kernel indexes
- `hc_context`
- agent workspace files

For PRs, compare the diff against the stated scope. If a docs-only PR touches a protected surface, stop routine triage, request explanation, and route for explicit maintainer review. Do not reclassify protected-path changes as documentation-only.

## 11. Human-Supervised Validation Routing

Route for human-supervised validation when an item is sensitive, trust-kernel-impacting, or protected-surface-adjacent.

The routing note should identify:

- affected files or areas
- expected behavior or interpretation change
- relevant validation commands and outputs
- unresolved evidence gaps
- reviewer expertise needed
- whether public discussion is appropriate

Human-supervised validation should occur before merge or before maintainers present a sensitive decision as accepted. Automation, labels, and AI-assisted summaries may support review but do not replace reviewer judgment.

## 12. PR Review Routing

For each PR, confirm:

- the stated scope matches the diff
- docs-only claims are accurate
- protected paths are not touched unless explicitly authorized
- terminology is consistent with HC-TRUST-LAYER and HC:// usage
- required checks are listed and results are reported
- trust-kernel impact is declared
- screenshots are included for perceptible web UI changes when applicable
- claims are limited to what repository evidence supports

Route PRs as follows:

- documentation-only, public-safe clarification: standard maintainer review after required docs checks
- governance or process change: maintainer review with attention to authority boundaries
- security-sensitive item: private or restricted review path as appropriate
- protected-surface or trust-kernel-sensitive item: human-supervised validation and appropriate domain reviewers before merge consideration

## 13. Status Lifecycle

A typical issue lifecycle is:

1. `status:needs-triage`
2. `status:needs-info`, `status:accepted`, `status:deferred`, `status:duplicate`, or `status:closed-no-action`
3. linked PR review when work is proposed
4. closure after merge, duplicate resolution, deferral, or no-action decision

A typical PR lifecycle is:

1. initial scope and sensitivity review
2. required checks and protected-path review
3. reviewer routing
4. requested changes, approval, closure, or merge according to repository rules

Status changes should include enough explanation for later audit trail review.

## 14. Closure Reasons

Use clear closure reasons so contributors understand the outcome.

Common closure reasons include:

- duplicate of an existing issue or PR
- resolved by a merged PR
- insufficient information after follow-up
- out of scope for HC-TRUST-LAYER
- documented behavior, no repository change needed
- deferred to future roadmap or research discussion
- unsafe for public issue handling
- too broad for safe review
- closed because protected-surface changes require a different review path

Closure does not necessarily reject the underlying idea. Maintainers may invite a narrower issue, a documentation clarification, private security report, or a new PR with required validation.

## 15. Escalation Rules

Escalate instead of continuing routine triage when:

- security-sensitive details appear in a public issue or PR
- a PR changes protected surfaces without explicit authorization
- an item may affect trust-kernel-sensitive behavior or interpretation
- repository evidence conflicts with the requested claim
- required validation fails or cannot run
- a proposed fix would weaken guardrails, checks, policy, or validation logic
- the item requires cross-domain review across documentation, policy, validators, signing, federation, schemas, or records
- a contributor asks maintainers to confirm production readiness, security certification, forensic certainty, truth finality, or autonomous governance

Escalation should preserve evidence and avoid expanding claims.

## 16. What Not To Claim

Maintainers do not create production-readiness, security-certification, forensic-certainty, truth-finality, or autonomous-governance claims.

Do not claim:

- production readiness
- security certification
- forensic certainty
- truth finality or objective-truth finality
- autonomous governance finality
- live federation guarantees
- complete dispute automation
- cryptographic or policy guarantees not backed by repository tests and documentation
- validation success for checks that were not run
- implementation status not supported by repository evidence

Use bounded language such as "documents," "supports review," "routes for review," "requires validation," or "is supported by repository evidence" when accurate.

## 17. Related Documents

- [Contributor Start Here](contributor-start-here.md)
- [Issue Workflow Guide](issue-workflow.md)
- [PR Workflow Guide](pr-workflow.md)
- [Trust Review Workflow](trust-review-workflow.md)
- [Trust Impact Analysis](trust-impact-analysis.md)
- [Verification Map](verification-map.md)
- [Protocol Graph](protocol-graph.md)
- [Protocol Graph Integrity](protocol-graph-integrity.md)
- [Anti-Spoofing Foundations](anti-spoofing-foundations.md)
- [Trusted Relationship Model](trusted-relationship-model.md)
- [Trust Workflow Model](trust-workflow-model.md)
