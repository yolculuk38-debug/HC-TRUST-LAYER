# HC-TRUST-LAYER Protocol Graph and Agent Context Map Foundation

## Purpose

This document establishes a documentation-only **protocol graph** and **agent context map** baseline for HC-TRUST-LAYER and HC://.

The goal is to improve AI-agent assisted development by giving Codex and future agents a stable map of trust-layer components, relationships, and likely change-impact areas before proposing modifications.

This foundation does not introduce runtime indexing, production claims, workflow changes, or external integrations.

## Protocol Graph Overview

The HC:// protocol graph is a structured representation of trust-kernel components and their dependencies inside HC-TRUST-LAYER verification infrastructure.

At foundation scope, the protocol graph is a human-readable documentation model that:

- identifies core component nodes
- maps directional dependencies between nodes
- highlights canonical record and provenance boundaries
- clarifies human-supervised validation checkpoints
- improves review routing for cross-component changes

## Why Agents Need a Pre-defined Project Map

AI agents can generate fast diffs but may miss cross-layer trust implications without a stable project map.

A pre-defined agent context map helps agents:

- route changes to appropriate reviewers
- avoid accidental boundary drift across canonical record surfaces
- preserve audit trail continuity and provenance assumptions
- identify when validator, policy, signing, or federation logic is indirectly affected
- prioritize safe documentation-first transitions before runtime behavior changes

This keeps HC-TRUST-LAYER aligned with conservative trust kernel evolution and human-supervised validation.

## Trust Kernel Component Map

The protocol graph foundation currently references these component areas:

1. **Canonical record boundary**
   - Schema, deterministic serialization, and record identity boundaries.
2. **Validator layer**
   - Verification rules, validation paths, and result normalization.
3. **Policy engine**
   - Policy rule evaluation, governance constraints, and decision boundaries.
4. **Workflow and CI guardrails**
   - Terminology, docs drift, and canonical artifact continuity controls.
5. **Verification package layer**
   - Exportable verification artifacts and external verification packaging boundaries.
6. **Trust graph layer**
   - Trust relationship modeling, risk history, and query-routing foundations.
7. **Signing layer**
   - Signature envelopes, key handling expectations, and trust anchor semantics.
8. **Federation layer**
   - Multi-node discovery, sync, and consensus-oriented trust boundaries.
9. **Dispute and challenge layer**
   - Contested record handling, adjudication workflow, and supersession paths.
10. **Message and content provenance layer**
    - Source lineage, transformation context, and provenance continuity.
11. **Implementation transition layer**
    - Documentation-first migration sequencing and staged capability hardening.

## Reference Map by Domain

### Canonical Record Boundaries

- `docs/canonical-record-boundary.md`
- `docs/record-format.md`

### Validator Layer References

- `docs/validator-capability-model.md`
- `docs/public-validator.md`
- `docs/verify.md`

### Policy Engine References

- `docs/policy-engine-architecture.md`
- `docs/policy-rules.md`
- `docs/policy-evaluator.md`

### Workflow/CI References

- `.github/workflows/terminology.yml`
- `.github/workflows/docs-drift.yml`
- `.github/workflows/canonical-artifacts.yml`
- `scripts/check_terminology.py`
- `scripts/check_docs_drift.py`
- `scripts/check_canonical_artifacts.py`

### Verification Package References

- `docs/verification-package-spec.md`
- `docs/verification-package-format.md`
- `docs/verification-package-validation.md`
- `docs/verification-package-generation.md`
- `docs/verification-package-v2.md`

### Trust Graph References

- `docs/trust-graph.md`
- `docs/trust-graph-data-model.md`
- `docs/trust-query-routing.md`
- `docs/trust-decay-risk-history.md`

### Signing References

- `docs/signing-architecture.md`
- `docs/signed-witness-model.md`
- `docs/witness-layer.md`

### Federation References

- `docs/federation-architecture.md`
- `docs/federation-sync.md`
- `docs/federation-discovery.md`

### Dispute/Challenge References

- `docs/dispute-challenge-architecture.md`
- `docs/GOVERNANCE.md`
- `docs/reviewer-selection.md`

### Message/Content Provenance References

- `docs/message-content-provenance.md`
- `docs/ai-model-provenance.md`
- `docs/PROVENANCE.md`

### Implementation Transition References

- `docs/implementation-transition-plan.md`
- `docs/implementation-map.md`
- `docs/capability-status.md`
- `docs/trust-kernel-checkpoint-300.md`

## Agent Task Routing Rules

Use these routing rules before merge for any non-trivial HC:// change:

- **docs-only changes**
  - Route to documentation maintainers and trust-kernel reviewers for terminology and boundary consistency.
- **schema changes**
  - Require canonical record boundary review and validator compatibility review.
- **validator changes**
  - Require validator + policy engine review and public verification output impact review.
- **workflow changes**
  - Require CI governance review for terminology/docs/canonical artifact guard continuity.
- **signing/key changes**
  - Require signing architecture and trust anchor review with elevated human-supervised validation.
- **federation changes**
  - Require federation, consensus, and audit trail continuity review.
- **public API changes**
  - Require verification infrastructure contract review and backward-compatibility check.

## Change Impact Checklist

Before approving a change, confirm:

- Does this affect **canonical records**?
- Does this affect **validation**?
- Does this affect **policy evaluation**?
- Does this affect **public verification**?
- Does this affect **signing or trust anchors**?
- Does this affect **federation behavior**?
- Does this affect **audit trail continuity**?

If any answer is yes, escalate to explicit human-supervised validation across the impacted trust kernel domains.

## Future Machine-readable Index

A future documentation-to-runtime transition may add `protocol-graph.json`.

Planned index structure (not implemented in this phase):

- **protocol-graph.json**
- **component nodes**
- **dependency edges**
- **risk tags**
- **owner/review requirements**
- **agent routing hints**

This PR intentionally keeps the protocol graph and agent context map as documentation-only foundation.

## Scope and Constraints

- documentation only
- no runtime index in this phase
- no dependency installation
- no external tool integration
- no workflow changes
- no production claims

## Terminology Baseline

This foundation preserves HC-TRUST-LAYER and HC:// terminology and aligns with:

- protocol graph
- agent context map
- trust kernel
- verification infrastructure
- provenance
- audit trail
- canonical record
- human-supervised validation
