# Future to Active Promotion Workflow

## Status and Scope

- advisory_only=true
- public_safe=true
- human_final_authority=true
- governance_protected=true
- traceability_first=true
- documentation-only process
- no runtime behavior changes
- no validator changes
- no schema changes
- no workflow changes
- no signing logic changes
- no federation runtime changes
- no governance enforcement changes

This workflow is an advisory process document for HC-TRUST-LAYER and HC:// future-facing concepts. It does not promote any concept by itself and does not create protocol, runtime, validator, schema, signing, federation, workflow, governance, release, or production behavior.

## Purpose

The purpose of this workflow is to define how exploratory materials in `docs/future/` may move toward active repository work without being mistaken for active HC:// behavior.

Future documents are non-canonical until explicitly promoted through linked issues, scoped plans, pull requests, checks, review, merge, and release handling. Promotion requires human-supervised review and human final approval before any concept can be treated as active repository direction.

This workflow extends the [Contribution Traceability Policy](contribution-traceability.md) by adding stage and gate expectations for future-facing concepts.

## Authority Boundary

Promotion does not grant authority to contributors, sponsors, supporters, AI agents, validators, or external organizations. Promotion creates a reviewable audit trail only. Repository-defined maintainers and reviewers retain final decision authority through human-supervised validation.

Future-facing discussion, funding, endorsement, implementation assistance, validator participation, or organizational support must not be described as governance control, signing authority, validator authority, federation authority, release authority, or canonical record authority.

## Promotion Stages

A future-facing concept may move through these stages:

1. **Future**: the concept lives in `docs/future/` and remains exploratory, advisory, and non-canonical.
2. **Candidate**: reviewers agree the concept is mature enough to be discussed as possible active work, while still non-canonical.
3. **Scoped Issue**: an issue links the future document, states scope, records non-goals, classifies risk, identifies affected paths, and names required checks.
4. **Implementation Plan**: a plan describes the proposed documentation, tests, code, or operational work and calls out security, governance, trust kernel, protocol graph, verification map, and canonical record boundary impact.
5. **PR**: a pull request links the future document and scoped issue, limits changes to the approved scope, and preserves advisory and public-safe status where applicable.
6. **Checks**: applicable checks run and results are reported, including terminology guard, docs drift guard, canonical artifact guard, and any relevant test subsets.
7. **Review**: reviewers evaluate terminology, traceability, risk, non-goals, affected paths, governance/security review needs, audit trail continuity, and human-supervised validation requirements.
8. **Merge**: authorized maintainers merge only after required review and final human approval are recorded.
9. **Release**: release notes or release artifacts reference the merged work when it becomes part of a release boundary; unreleased work remains unreleased even after merge.

A concept may stop, return to a prior stage, remain archived, or stay in `docs/future/` indefinitely. There is no autonomous promotion path.

## Required Promotion Gates

Before a future concept can be treated as active work, the promotion record must include:

- **Linked future document**: the originating `docs/future/` document or section.
- **Linked issue**: the issue that scopes the candidate work and records discussion.
- **Scope statement**: what is proposed to change and why.
- **Non-goals**: explicit boundaries for what the promotion does not change.
- **Risk classification**: documentation-only, trust-kernel-impacting, security-sensitive, federation-impacting, schema-impacting, validator-impacting, signing-impacting, workflow-impacting, governance-impacting, or another reviewer-defined class.
- **Affected paths**: files, directories, documents, tests, scripts, or canonical record surfaces expected to be touched or explicitly avoided.
- **Required checks**: terminology guard, docs drift guard, canonical artifact guard, relevant tests, and any specialized validation required by the affected scope.
- **Governance/security review need**: whether governance, security, federation, signing, validator, schema, policy, or canonical record reviewers are required.
- **Human final approval**: explicit reviewer or maintainer approval confirming that the promotion is acceptable for the proposed scope.

Missing gates keep the concept in Future or Candidate status. A PR cannot silently convert exploratory material into active behavior.

## Non-Canonical Future Status

Documents in `docs/future/` are non-canonical until promoted. They may describe ideas, risks, questions, possible architectures, and candidate vocabulary, but they do not define active protocol, runtime, validator, schema, signing, federation, workflow, governance, or release behavior.

Future documents must not be cited as proof that a feature exists, that a validator must behave in a particular way, that a schema has changed, that federation is active, that governance enforcement exists, or that a release contains the concept.

## Review Expectations

Human-supervised review must confirm that the promotion record:

- preserves HC-TRUST-LAYER and HC:// terminology;
- distinguishes future, candidate, active, merged, and released status;
- preserves audit trail continuity from future document to issue, PR, checks, review, merge, and release;
- avoids production-readiness claims unless implemented and validated in-repo;
- avoids truth guarantee, forensic certainty, autonomous governance finality, and unsupported cryptographic or policy guarantee language;
- routes security, governance, validator, schema, signing, federation, policy, workflow, trust kernel, protocol graph, verification map, and canonical record questions to the proper reviewers; and
- documents any check that could not run without implying success.

## Example Flows

### Trust Ladder future concept to documentation PR

```text
docs/future/trust-ladder.md
→ Candidate issue for terminology and review boundaries
→ Documentation-only scope statement
→ PR updating active documentation guidance
→ terminology guard, docs drift guard, canonical artifact guard
→ human-supervised review
→ merge
→ release note if included in a release
```

This flow is suitable when the change clarifies language or review routing without modifying runtime behavior, validators, schemas, workflows, signing logic, federation runtime, canonical records, or governance enforcement.

### Signed Validator Identity future concept to security-reviewed implementation plan

```text
docs/future/signed-validator-identity.md
→ Candidate issue with signing and validator risk classification
→ Security review need recorded
→ Implementation plan drafted with affected paths and non-goals
→ required checks identified before any implementation PR
→ human final approval required before active implementation work
```

This flow does not authorize signing logic, validator behavior, schema contracts, security policy, or canonical record changes. It only creates a reviewed plan when security-sensitive reviewers accept the scoped direction.

### Trust Exchange future concept to federation-reviewed roadmap item

```text
docs/future/trust-exchange.md
→ Candidate issue with federation risk classification
→ Federation review need recorded
→ Active roadmap item proposed with non-goals and affected paths
→ checks and review requirements documented
→ human-supervised review
→ merge as roadmap documentation if approved
```

This flow does not activate federation runtime behavior, external organization authority, validator authority, or governance enforcement. It records a possible active roadmap item only after federation-aware review.

## Explicit Non-Goals

This workflow does not make or authorize:

- runtime behavior changes;
- validator changes;
- schema changes;
- workflow changes;
- signing logic changes;
- federation runtime changes;
- governance enforcement changes;
- canonical record changes;
- autonomous promotion;
- autonomous approval;
- production-readiness claims;
- live federation guarantees;
- truth guarantees;
- forensic certainty claims; or
- authority transfer to contributors, sponsors, supporters, AI agents, validators, or external organizations.

## Relationship to Contribution Traceability

The Contribution Traceability Policy defines the repository-wide audit trail for ideas, documents, issues, PRs, checks, reviews, merges, and releases. This workflow applies that traceability model to future-facing concepts by requiring explicit promotion stages and gates before active work begins.

Promotion records should preserve enough public-safe references for reviewers to reconstruct:

- which future document started the promotion;
- which issue scoped the candidate work;
- which implementation plan, if any, described the active path;
- which PR changed repository content;
- which checks ran or could not run;
- which reviewers evaluated the risk;
- which human final approval accepted the scope;
- which merge introduced the change; and
- which release first referenced the change, if any.
