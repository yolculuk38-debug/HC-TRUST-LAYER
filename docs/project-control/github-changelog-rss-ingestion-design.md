# GitHub Changelog RSS Ingestion Design

> Status: design proposal
> Scope: GitHub Changelog/RSS signal intake for HC Signal Watch v3
> Authority: advisory only; humans remain final decision makers
> Boundaries: docs-only design; no workflow change; no external network call; no issue, comment, approval, or merge automation

## Purpose

This document describes a future design for ingesting GitHub Changelog RSS items into HC GitHub Signal Watch without changing current workflow behavior.

The design preserves the HC-TRUST-LAYER operating boundary:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
```

RSS-derived findings would be treated as review signals only. They would not establish production readiness, legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, or guaranteed correctness.

## Current boundary

This design does not implement ingestion. It does not modify GitHub Actions, validators, schemas, records, protected paths, signing logic, federation logic, security workflows, policy enforcement, issue automation, comments, labels, reviewers, approvals, merges, or branch protection.

Until a separately reviewed implementation exists, operators should continue using the existing report-only Signal Watch process and manually collected changelog notes.

## Signal intake model

A future ingestion step can collect GitHub Changelog signals through a bounded intake pipeline:

1. **Fetch source**: read the official GitHub Changelog RSS feed from a workflow or local operator command in a separately approved implementation.
2. **Normalize entries**: store only public-safe metadata needed for triage, such as title, publication date, category or tag when present, URL, and a short operator-readable summary.
3. **Classify relevance**: map each entry to HC impact categories using deterministic keyword and category matching before any human interpretation.
4. **Deduplicate**: compare stable identifiers such as URL, title, and publication date to avoid repeating the same item in multiple reports.
5. **Render advisory report**: emit a local report section with impact, risk, recommended action, automation boundary, and evidence gaps.
6. **Human review**: require an operator or reviewer to decide whether a docs PR, config PR, workflow PR, dependency review, or no-action note is appropriate.

The intake should prefer minimal stored data and should avoid copying full changelog text into repository artifacts.

## HC-relevant categories

GitHub Changelog items are most relevant to HC-TRUST-LAYER when they can affect repository safety, dependency review, governance boundaries, or public-facing verification workflows.

| Category | Why it matters for HC | Default action |
| --- | --- | --- |
| GitHub Actions runtime, runner images, action versions, or deprecations | May affect CI reliability, validation reporting, or scheduled advisory reports. | Inspect workflow assumptions in a separate reviewed PR if needed. |
| Dependabot, dependency review, package ecosystems, or advisory database changes | May affect dependency update triage and supply-chain review boundaries. | Compare with dependency update policy and report evidence gaps. |
| CodeQL, code scanning, secret scanning, or application security changes | May affect advisory security signals and check annotations. | Inspect security signal interpretation without treating alerts as final proof. |
| Pull request permissions, fork behavior, bot-created PR behavior, reviews, or approvals | May affect human-supervised validation and governance boundaries. | Review contributor-risk and approval-boundary language before changing configuration. |
| Repository rules, branch protection, environments, organization policy, or token permissions | May affect write access, workflow execution, or protected operations. | Require explicit human review before any configuration change. |
| Copilot, agents, automation, or AI-assisted development changes | May affect report-only boundaries and agent supply-chain assumptions. | Keep outputs advisory and verify no autonomous governance authority is introduced. |
| Pages, artifacts, releases, provenance, or package publication changes | May affect public-safe verification surfaces or release evidence handling. | Inspect documentation and release-evidence expectations. |
| Accessibility, mobile UI, or collaboration features | May affect operator experience and public verification readability. | Consider docs or UX follow-up only when relevant to HC:// flows. |
| Unrelated product announcements | No expected HC impact. | Record as no action or omit from report after deduplication. |

## False-positive reduction

The design should reduce noise before asking humans to review a signal:

- Match against an allowlist of HC-relevant categories before keyword expansion.
- Use keyword groups tied to clear impact areas, such as `actions`, `runner`, `dependabot`, `code scanning`, `secret scanning`, `branch protection`, `ruleset`, `approval`, `fork`, `token`, `artifact`, `release`, `pages`, `copilot`, and `agent`.
- Require at least one category match or two independent keyword matches before raising a non-low priority finding.
- Deduplicate entries by canonical URL first, then by normalized title and publication date.
- Suppress repeated items already included in a recent advisory report unless the newer entry changes the impact category.
- Keep unrelated product news out of high-priority output even when general terms such as `release` or `security` appear without repository-operation impact.
- Include an `evidence_gap` field when the report cannot determine whether the changelog item affects HC-TRUST-LAYER.
- Prefer `recommended_action=inspect` over direct change recommendations when impact is uncertain.

False-positive filtering must not hide evidence needed for human review. Suppressed entries should remain explainable in local debug output or an operator-visible summary if implemented later.

## Human approval boundary

Human final authority remains outside the ingestion step.

RSS ingestion may recommend that humans inspect or prepare a follow-up, but it must not:

- approve pull requests;
- reject pull requests;
- merge pull requests;
- close issues or pull requests;
- create issues or comments;
- request reviewers;
- assign users;
- apply labels;
- change branch protection or repository settings;
- change workflows, validators, schemas, records, signing, federation, or policy enforcement.

A human reviewer remains responsible for deciding whether a signal needs no action, a documentation update, a dependency/configuration review, a workflow change, or escalation to protected-path review.

## Future workflow connection

A later PR may connect this design to the existing Signal Watch reporting path without granting repository mutation authority.

Recommended sequence for a separate implementation PR:

1. Add a local parser module or script that accepts a saved RSS/XML fixture and emits normalized signal JSON.
2. Add fixtures and tests for relevant, unrelated, duplicate, and ambiguous changelog entries.
3. Extend the existing local report generator to accept normalized changelog signal JSON.
4. Keep network access disabled by default for local tests.
5. If a workflow is later proposed, make it report-only with read-only permissions and no issue/comment/label/reviewer/approval/merge operations.
6. Require a human to inspect the generated report before opening any follow-up PR that touches workflows, security configuration, protected paths, or runtime behavior.

Any workflow connection should be a separate, small, reversible PR with explicit reviewer attention because it would move beyond this docs-only design.

## Open questions for the next PR

- Which official RSS source URL should be used, and how should feed failures be reported without creating noisy failures?
- What retention window should be used for deduplication?
- Should normalized signal JSON be stored only as a workflow artifact, or can an operator keep it locally under ignored temporary paths?
- Which tests are required before enabling scheduled report generation?
- How should the report distinguish `no HC impact found` from `impact unknown because evidence was unavailable`?

## Non-goals

This design does not create or imply:

- production readiness;
- legal truth;
- identity finality;
- forensic certainty;
- certification authority;
- autonomous governance authority;
- guaranteed correctness;
- automatic issue or comment creation;
- automatic approval, merge, labeling, assignment, or reviewer routing;
- live federation guarantees;
- changes to canonical records, schemas, validators, signing, federation, security workflows, policy enforcement, records, or generated artifacts.
