# Label Taxonomy Guide

> **Documentation Status**
> - **status:** ACTIVE
> - **scope:** Advisory label meanings for GitHub Issue and pull request triage.
> - **canonical relevance:** Advisory workflow guidance only; does not define canonical records, schemas, validators, signing, federation, policy, trust-kernel indexes, or automation.
> - **runtime relevance:** None; this guide does not change runtime verification behavior.

## 1. Purpose

This guide standardizes the meaning of labels used for HC-TRUST-LAYER issue and pull request triage. It helps maintainers and contributors describe scope, status, sensitivity, priority, validation state, and governance routing without creating automation or enforcement.

Repository evidence is authoritative. Labels are advisory triage metadata. Labels are not approval authority. Labels are not merge authority. Labels are not security validation. Labels are not production-readiness validation.

## 2. Authority Boundary

Labels organize review; they do not override repository evidence, maintainer review, required checks, or human-supervised validation.

A label may help route work, but it must not be used to claim:

- production readiness
- security certification
- forensic certainty
- truth finality
- autonomous governance

Do not claim production readiness, security certification, forensic certainty, truth finality, or autonomous governance. Human-supervised validation remains required for sensitive trust-kernel-impacting work.

## 3. Label Principles

Use labels to make triage clearer and more auditable:

- Prefer the smallest useful label set.
- Apply labels based on repository evidence, not external assumptions.
- Keep public labels free of sensitive details.
- Use conservative sensitivity labels when impact is uncertain.
- Update labels when evidence changes.
- Explain non-obvious labels in a comment when needed.
- Do not use labels to bypass checks, reviewers, or protected-path review.

Labels should support HC:// review boundaries, provenance reasoning, audit trail continuity, and human-supervised validation without implying guarantees beyond repository evidence.

## 4. Type Labels

Type labels identify the primary intent of an issue or PR.

| Label | Meaning |
| --- | --- |
| `type:bug` | Alleged defect, regression, mismatch, or unexpected behavior requiring evidence review. |
| `type:docs` | Documentation, navigation, wording, examples, terminology, or non-behavioral clarification. |
| `type:research` | Exploratory question, future direction, hypothesis, or non-implemented concept. |
| `type:governance` | Review process, authority boundary, validation routing, policy-adjacent workflow, or repository governance question. |
| `type:question` | Request for explanation or clarification without a confirmed change request. |
| `type:workflow` | Contributor, maintainer, triage, release, or project-control workflow guidance. |

Use one primary type label when possible. If an item spans multiple types, choose the label that reflects the next maintainer action and note secondary concerns in a comment.

## 5. Status Labels

Status labels describe current triage state. They are not approval, merge readiness, or validation results.

| Label | Meaning |
| --- | --- |
| `status:needs-triage` | Initial classification has not been completed. |
| `status:needs-info` | More evidence, reproduction detail, scope clarification, or repository references are needed. |
| `status:accepted` | Maintainers agree the item is in scope for work or review; this is not merge approval. |
| `status:deferred` | Item is in scope but not ready for current work. |
| `status:duplicate` | Item overlaps an existing issue, PR, documented decision, or active work item. |
| `status:blocked` | Progress depends on a missing prerequisite, unresolved decision, unavailable evidence, or failed check. |
| `status:parked` | Item is intentionally set aside without rejecting the idea, usually because timing, evidence, or scope is not ready. |
| `status:closed-no-action` | Item is closed without repository change. |

Use status labels with clear comments when closure, blocking, parking, or deferral could affect later audit trail review.

## 6. Area Labels

Area labels identify the repository surface or review domain most relevant to the item.

| Label | Meaning |
| --- | --- |
| `area:record-core` | Canonical record concepts, record identity, provenance continuity, or record-layer documentation. |
| `area:trust-protocol` | HC:// trust protocol, verification map, protocol graph, trust kernel, or related routing semantics. |
| `area:public-verification` | Public verification, QR review, viewer-facing evidence review, or public verification walkthroughs. |
| `area:docs-governance` | Documentation governance, contributor guidance, terminology, issue workflow, or PR workflow. |
| `area:security` | Security guidance, vulnerability reporting boundaries, non-sensitive hardening, or security review routing. |
| `area:federation` | Federation concepts, interoperability boundaries, future federation notes, or federation review routing. |
| `area:tooling` | Scripts, checks, local tools, reporting utilities, or non-runtime developer tooling. |
| `area:onboarding` | Contributor orientation, maintainer orientation, first-time workflows, or learning paths. |
| `area:project-control` | Project-control documentation, task organization, roadmap routing, or operational review coordination. |

Area labels do not authorize changes to protected paths. If an area label touches a protected surface, use the relevant sensitivity and governance routing labels as advisory metadata only.

## 7. Sensitivity Labels

Sensitivity labels communicate review risk and public-discussion boundaries.

| Label | Meaning |
| --- | --- |
| `sensitivity:public-safe` | Public discussion appears acceptable based on available evidence, with no sensitive details apparent. |
| `sensitivity:security-sensitive` | Public detail may expose misuse, vulnerability, operational risk, or sensitive security context. |
| `sensitivity:trust-kernel-sensitive` | Item may affect trust kernel behavior, validation semantics, verification map interpretation, protocol graph semantics, provenance continuity, audit trail continuity, policy routing, or protected review boundaries. |
| `sensitivity:protected-path-adjacent` | Item does not directly change a protected path but is close enough to require careful reviewer routing. |
| `sensitivity:canonical-record-adjacent` | Item may affect canonical record assumptions, deterministic serialization assumptions, record identity, hash-linked artifacts, or provenance continuity. |

When sensitivity is uncertain, label conservatively and explain the uncertainty. Human-supervised validation remains required for sensitive trust-kernel-impacting work.

## 8. Priority Labels

Priority labels communicate relative scheduling and attention. They do not create emergency authority, merge authority, or validation status.

| Label | Meaning |
| --- | --- |
| `priority:low` | Useful but not time-sensitive; can wait behind higher-impact work. |
| `priority:normal` | Standard review priority for in-scope work. |
| `priority:high` | Important work that should be reviewed soon because it affects contributors, review clarity, or important repository surfaces. |
| `priority:urgent` | Time-sensitive maintainer attention is requested; this still does not bypass safety, security, or human-supervised validation requirements. |

Use priority labels sparingly. Avoid using priority labels to imply production readiness, security certification, forensic certainty, truth finality, or autonomous governance.

## 9. Validation Labels

Validation labels describe reported check state for the item. They are advisory and should be backed by command output, reviewer notes, or clear explanation.

| Label | Meaning |
| --- | --- |
| `validation:not-run` | Relevant checks have not been run or no validation evidence has been provided. |
| `validation:passed` | Reported checks passed for the stated scope; this is not security validation or production-readiness validation. |
| `validation:failed` | A relevant check failed or reported errors that need review. |
| `validation:human-required` | Human-supervised validation is required before the work can be treated as ready for sensitive review or merge consideration. |
| `validation:pending` | Checks or reviewer validation are in progress or expected but not complete. |

Validation labels do not replace logs, check output, reviewer assessment, or repository-defined validation gates.

## 10. Governance Labels

Governance labels identify review routing and authority-boundary needs. They are advisory metadata and do not decide outcomes.

| Label | Meaning |
| --- | --- |
| `governance:maintainer-review` | Maintainer review is needed for workflow, scope, or repository stewardship. |
| `governance:human-supervised-validation` | Human-supervised validation is needed because the item may affect sensitive HC:// review boundaries. |
| `governance:security-review` | Security-oriented reviewer routing is needed; public labels must not expose sensitive details. |
| `governance:cross-domain-review` | Review spans more than one domain, such as docs, policy, validators, signing, federation, schemas, or records. |
| `governance:decision-needed` | Maintainers need to make or document a decision before work can proceed. |

Governance labels must not be treated as approval authority, merge authority, security validation, or production-readiness validation.

## 11. When To Apply Labels

Apply labels when they make the next review step clearer:

- during initial issue or PR triage
- after confirming public discussion is safe or sensitive routing is needed
- when evidence indicates the type, area, status, validation state, or sensitivity
- when a PR claims docs-only scope and needs protected-path confirmation
- when required checks pass, fail, are pending, or were not run
- when human-supervised validation is needed for sensitive trust-kernel-impacting work
- when an item is duplicate, blocked, deferred, parked, or closed with no action

Label changes should preserve audit trail clarity. If a label could be misunderstood, add a short comment explaining the repository evidence behind it.

## 12. When Not To Apply Labels

Do not apply labels to imply authority or validated claims.

Avoid labels when:

- the label would expose sensitive security details publicly
- the evidence is too incomplete to classify without a `status:needs-info` comment
- the label would imply approval, merge readiness, security validation, or production-readiness validation
- the label would replace required checks, reviewer approval, or human-supervised validation
- the label would obscure protected-path impact
- the label would make unsupported claims about HC:// behavior or repository implementation status

If a label creates ambiguity, prefer a clarifying comment and conservative routing.

## 13. Label Examples

Examples:

- Documentation typo in contributor guidance: `type:docs`, `area:docs-governance`, `status:needs-triage`, `sensitivity:public-safe`.
- Question about public QR verification wording: `type:question`, `area:public-verification`, `status:needs-info`, `sensitivity:public-safe`.
- Research proposal for future federation documentation: `type:research`, `area:federation`, `status:deferred`, `sensitivity:public-safe`.
- PR updating issue workflow guidance: `type:workflow`, `area:docs-governance`, `validation:pending`, `sensitivity:public-safe`.
- Concern near canonical record identity semantics: `area:record-core`, `sensitivity:canonical-record-adjacent`, `sensitivity:trust-kernel-sensitive`, `validation:human-required`.
- Public report containing possible vulnerability detail: `area:security`, `sensitivity:security-sensitive`, `governance:security-review`, with sensitive details routed through the private reporting path instead of public comments.

These examples are not exhaustive and do not authorize changes. They illustrate advisory triage metadata only.

## 14. Relationship to Issue Workflow

The issue workflow explains how contributors choose public issues, private vulnerability reporting, templates, evidence, duplicate checks, and issue lifecycle steps. This taxonomy supplies consistent label meanings for that workflow.

Issue labels should help maintainers route the item, request information, mark duplicates, identify sensitivity, and preserve audit trail clarity. Issue labels do not validate the issue, approve implementation, or authorize merge.

## 15. Relationship to PR Workflow

The PR workflow explains scope control, protected-path review, docs-only claims, required checks, sensitive review, and merge boundaries. This taxonomy supplies consistent label meanings for PR triage.

PR labels should help reviewers understand scope, area, validation state, priority, and sensitivity. PR labels do not replace checks, review approval, protected-path assessment, or human-supervised validation.

## 16. Relationship to Maintainer Triage

The maintainer triage guide explains how maintainers classify issues and PRs, route sensitive work, handle duplicates, assess protected surfaces, and escalate when needed. This taxonomy gives maintainers a shared vocabulary for those triage decisions.

Maintainers should use labels as advisory metadata and explain uncertainty when repository evidence is incomplete. Maintainer triage remains bounded by repository evidence, required checks, reviewer oversight, and human-supervised validation.

## 17. What Labels Do Not Mean

Labels do not mean:

- approval authority
- merge authority
- security validation
- production-readiness validation
- human-supervised validation completion
- protected-path authorization
- reviewer approval
- policy approval
- cryptographic assurance
- forensic certainty
- truth finality
- autonomous governance

Labels may support review, but they cannot make claims that repository evidence does not support.

## 18. Related Documents

- [`docs/issue-workflow.md`](issue-workflow.md)
- [`docs/pr-workflow.md`](pr-workflow.md)
- [`docs/maintainer-triage.md`](maintainer-triage.md)
- [`docs/trust-review-workflow.md`](trust-review-workflow.md)
- [`docs/trust-impact-analysis.md`](trust-impact-analysis.md)
- [`docs/verification-map.md`](verification-map.md)
- [`docs/protocol-graph-index.md`](protocol-graph-index.md)
- [`docs/trust-kernel-index.md`](trust-kernel-index.md)
- [`SECURITY.md`](../SECURITY.md)
- [`CONTRIBUTING.md`](../CONTRIBUTING.md)
