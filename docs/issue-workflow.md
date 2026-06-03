# Issue Workflow Guide

> **Documentation Status**
> - **status:** ACTIVE
> - **scope:** Contributor guidance for GitHub Issues, private vulnerability reporting, duplicate prevention, evidence collection, and maintainer triage.
> - **canonical relevance:** Advisory workflow guidance only; does not define canonical records, schemas, validators, signing, federation, policy, or trust-kernel indexes.
> - **runtime relevance:** None; this guide does not change runtime verification behavior.

## 1. Purpose

This guide helps contributors decide whether to open a public GitHub Issue, use private vulnerability reporting, choose an issue template, or continue checking existing repository evidence before posting. It supports HC-TRUST-LAYER contributors without overstating authority or exposing sensitive information.

Use it before opening a public GitHub Issue. Repository evidence is authoritative. Public issues are not validation. Issue triage is not approval. Issue labels are not merge authority. Human-supervised validation remains required for sensitive trust-kernel-impacting work.

## 2. Before Opening an Issue

Before opening an issue:

1. Confirm the concern is in scope for HC-TRUST-LAYER and HC:// verification infrastructure.
2. Decide whether the report can safely be public.
3. Check whether the topic is already documented, planned, implemented, partial, research-only, or out of scope.
4. Choose the closest issue template instead of forcing a topic into an unrelated template.
5. Keep claims tied to repository evidence, reproducible observations, and affected files or commands.

If the concern includes sensitive vulnerability details or uncertainty about safe disclosure, do not open a public issue. Use the private reporting path described in the top-level [`SECURITY.md`](../SECURITY.md).

## 3. Security-Sensitive Reports

Sensitive vulnerability reports must not be posted publicly.

Use the private reporting path described in the top-level [`SECURITY.md`](../SECURITY.md) for reports involving:

- exploit steps or proof-of-concept material
- private records, personal information, or non-public provenance material
- secrets, tokens, keys, credentials, or authentication material
- validator bypass concerns
- policy-routing weakness details
- signing or trust-anchor concerns
- GitHub Actions, dependency, package, or supply-chain vulnerability details
- active abuse details that could increase harm if public
- uncertainty about whether public disclosure is safe

If a private reporting path is unavailable, open only a minimal public issue asking maintainers for a private security contact. Do not include sensitive details in that request.

## 4. Which Template Should I Use?

Use the template that best matches the primary concern:

| Concern | Recommended template |
| --- | --- |
| Reproducible defect in documented HC:// verification infrastructure behavior | Bug Report |
| Documentation wording, navigation, governance clarity, or contributor guidance | Docs Governance |
| Research-only concept, open question, or future exploration | Research Idea |
| Canonical record boundary, record identity, or provenance continuity question | Core Record Layer |
| Trust protocol, verification map, protocol graph, or trust kernel routing concern | Trust Protocol |
| Public verification, QR, viewer, or public evidence review flow concern | Public Verification |
| Federation or interoperability proposal | Federation |
| Non-sensitive security hardening idea without exploit details | Security Hardening |

If no template fits, review the related documents first and choose the closest available template. Blank issues are disabled; the selected template should explain why the issue belongs there and what repository evidence supports the request.

## 5. Bug Reports

Use a bug report for a reproducible defect in existing repository behavior, documentation-backed workflows, scripts, or public verification guidance.

A useful bug report should include:

- a concise summary
- affected component or file path
- expected behavior based on repository evidence
- actual behavior observed
- reproduction steps
- command output or screenshots when relevant
- implementation status if known
- validator, canonical record, provenance, or audit trail impact if applicable
- whether sensitive details were omitted for private reporting

Do not use a public bug report for exploit instructions, private records, secrets, validator bypass details, or uncertain security disclosures.

## 6. Documentation Issues

Use a documentation issue for unclear wording, broken links, duplicate guidance, missing navigation, terminology drift, or contributor workflow confusion.

Documentation reports should identify:

- the affected file and section
- the confusing or outdated statement
- the repository evidence that should control the correction
- any HC://, verification map, trust kernel, protocol graph, provenance, audit trail, canonical record, or human-supervised validation terminology impact

Documentation issues should not introduce production-readiness claims or imply guarantees that are not implemented and validated in-repo.

## 7. Research Ideas

Use a research idea when the topic is exploratory, not implemented, or intended to test a possible future direction.

Research ideas should:

- clearly mark the work as research-only or exploratory
- describe the hypothesis or question
- identify affected documentation or architecture surfaces
- avoid implying implementation status
- avoid expanding runtime, policy, federation, signing, schema, validator, or canonical record scope without explicit review

Research discussion can inform future work, but it does not validate a capability or authorize implementation.

## 8. Governance Questions or Proposals

Use a governance-oriented issue when the question concerns review boundaries, maintainer process, contributor policy, escalation paths, or interpretation of repository guidance.

Governance proposals should include:

- the current repository evidence or policy text
- the ambiguity or proposed clarification
- who may be affected
- whether the proposal changes reviewer expectations, issue routing, labels, or merge boundaries
- whether human-supervised validation is required before adoption

Issue triage is not approval. Maintainers may route governance questions to documentation updates, follow-up discussion, or a pull request, but the issue itself does not change repository policy.

## 9. Public Integrity Concerns

Use a public issue only for non-sensitive integrity concerns that can be discussed without increasing risk.

Appropriate public integrity concerns may include:

- broken public verification links
- public documentation inconsistencies
- public record-reference mismatch reports that do not reveal private data
- public hash or QR reference concerns without exploit details
- misleading public attribution or provenance context

Include only public, non-sensitive evidence. If the concern might expose exploit steps, private data, active abuse details, validator bypasses, signing weaknesses, trust-anchor weaknesses, or policy-routing weaknesses, use the private reporting path in top-level [`SECURITY.md`](../SECURITY.md).

## 10. Trust-Kernel-Sensitive Proposals

A proposal is trust-kernel-sensitive if it may affect any of the following:

- canonical records
- schemas
- validators
- signing or trust anchors
- federation
- policy interpretation
- runtime verification behavior
- provenance continuity
- protected paths
- trust-kernel indexes

For these proposals, state the expected impact clearly and avoid unsupported guarantees. Human-supervised validation remains required for sensitive trust-kernel-impacting work. Public discussion, issue labels, maintainer comments, and triage outcomes are not merge authority.

## 11. Support or Usage Questions

Use public support channels only for non-sensitive usage questions, implementation guidance, or contributor help.

Include:

- what you are trying to do
- the files, commands, or records involved
- what you expected
- what happened instead
- any relevant environment details

For sensitive reports, follow [`SECURITY.md`](../SECURITY.md) instead of public support channels. For general support expectations, see [`SUPPORT.md`](../SUPPORT.md).

## 12. Duplicate Prevention

Before opening an issue, check for duplicates and existing repository evidence:

- open and closed GitHub Issues
- related pull requests
- [`README.md`](../README.md)
- [`docs/contributor-start-here.md`](contributor-start-here.md)
- [`docs/capability-status.md`](capability-status.md)
- [`docs/implementation-map.md`](implementation-map.md)
- [`docs/project-control/task-ledger.md`](project-control/task-ledger.md)
- [`docs/project-control/active-work-registry.md`](project-control/active-work-registry.md)

If you find related work, link it in the new issue and explain what is different. If the existing record already resolves the question, avoid opening a duplicate issue.

## 13. Evidence to Include

Good issues include enough evidence for maintainers to triage without guessing:

- affected file paths, sections, issue links, pull request links, or commands
- expected behavior based on repository evidence
- actual behavior or observed inconsistency
- reproduction steps when applicable
- screenshots only when they add clarity and do not expose sensitive information
- relevant check output, version, branch, or environment details
- trust-kernel sensitivity statement when applicable
- clear note if sensitive details were intentionally omitted for private reporting

Do not include private records, credentials, exploit details, or non-public provenance material in public issues.

## 14. Issue Lifecycle

A typical issue may move through these stages:

1. **Opened:** Contributor submits a scoped report, question, or proposal.
2. **Initial screening:** Maintainers check scope, sensitivity, duplicates, and template completeness.
3. **Triage:** Maintainers may add labels, ask for evidence, route to private reporting, or link related work.
4. **Review:** Maintainers or contributors evaluate repository evidence and proposed next steps.
5. **Resolution path:** The issue may become a documentation update, pull request, research note, support answer, duplicate closure, or private security process.
6. **Closure:** Maintainers close the issue when the question is resolved, superseded, duplicated, out of scope, unsafe for public discussion, or moved to another path.

Public issues are not validation, and closing or labeling an issue does not imply implementation approval.

## 15. Maintainer Triage Overview

During triage, maintainers may:

- request additional evidence or reproduction steps
- remove or redact sensitive public details when possible
- route sensitive concerns to the private vulnerability reporting path
- mark issues as duplicates or link related work
- clarify implementation status using repository evidence
- change labels or templates for better routing
- split broad issues into smaller, auditable work items
- close issues that are out of scope, unsafe, unsupported by evidence, or already resolved
- ask for human-supervised validation before trust-kernel-impacting work proceeds

Triage decisions are workflow management decisions. They are not approval to merge, validation of claims, or authorization to bypass repository guardrails.

## 16. Labels and Status Meanings

Labels help route work, but they do not grant authority.

Common label meanings may include:

- `type:bug`: report of a defect or unexpected behavior
- `type:workflow`: workflow, process, or area-tracking issue
- `type:research`: exploratory or research-only idea
- `status:research-only`: not represented as an implemented capability
- `area:docs-governance`: documentation or governance clarity
- `area:record-core`: canonical record or record-layer routing
- `area:trust-protocol`: trust protocol, verification map, protocol graph, or trust kernel routing
- `area:public-verification`: public verification or viewer-facing review flow
- `area:federation`: federation or interoperability routing
- `area:security`: non-sensitive security hardening routing

Issue labels are not merge authority. Repository-defined checks, maintainer review, and human-supervised validation requirements still apply.

## 17. What Not To Claim

Do not claim any of the following in issues, comments, titles, labels, or proposals:

- production readiness
- security certification
- forensic certainty
- truth finality
- autonomous governance

Also avoid implying complete dispute automation, live federation guarantees, cryptographic guarantees, policy guarantees, or objective-truth determination unless the claim is implemented, documented, and validated in the repository.

## 18. Related Documents

- [`README.md`](../README.md)
- [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- [`SUPPORT.md`](../SUPPORT.md)
- [`SECURITY.md`](../SECURITY.md)
- [`docs/contributor-start-here.md`](contributor-start-here.md)
- [`docs/capability-status.md`](capability-status.md)
- [`docs/implementation-map.md`](implementation-map.md)
- [`docs/project-control/task-ledger.md`](project-control/task-ledger.md)
- [`docs/project-control/active-work-registry.md`](project-control/active-work-registry.md)
- [`docs/verification-map.md`](verification-map.md)
- [`docs/protocol-graph-index.md`](protocol-graph-index.md)
- [`docs/trust-kernel-index.md`](trust-kernel-index.md)
- [`docs/trust-review-workflow.md`](trust-review-workflow.md)
