# HC-TRUST-LAYER Agent Workspace Workflow

## Task Lifecycle

1. idea
2. analysis
3. scoped task
4. PR
5. checks
6. human review
7. merge
8. audit

Reference model: `docs/idea-to-pr-pipeline.md`.

This lifecycle preserves provenance, audit trail continuity, and human-supervised validation across HC:// changes.

## PR Risk Classes

- docs-only
- index/map
- workflow
- schema
- validator
- signing
- federation
- public API

## Review Expectations by Risk Class

- **docs-only**
  - Documentation maintainers review terminology, protocol graph alignment, verification map consistency, and clarity.
- **index/map**
  - Documentation and architecture reviewers confirm protocol graph and agent context mapping accuracy and cross-reference integrity.
- **workflow**
  - CI/governance reviewers confirm guard continuity, audit trail expectations, and non-bypass of human-supervised validation.
- **schema**
  - Canonical record and validator reviewers confirm deterministic compatibility, provenance continuity, and migration safety.
- **validator**
  - Validator and policy reviewers confirm decision-path integrity, explainability, and verification output continuity.
- **signing**
  - Signing/trust-anchor reviewers confirm cryptographic boundary handling, key-material expectations, and high-sensitivity controls.
- **federation**
  - Federation and routing reviewers confirm interoperability boundaries, consistency assumptions, and multi-node audit trail continuity.
- **public API**
  - API contract reviewers confirm backward compatibility, consumer impact, and versioning expectations.
- `docs/trust-pr-engine.md`
- `docs/trust-impact-analysis.md`
- `docs/verification-proposal-model.md`
- `docs/trust-review-workflow.md`
