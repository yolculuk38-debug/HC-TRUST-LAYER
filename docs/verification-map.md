# HC-TRUST-LAYER HC:// Verification Map Foundation

## Purpose

This verification map provides a documentation-first foundation for navigating HC-TRUST-LAYER and HC:// trust-kernel domains.

The goal is to reduce repeated rediscovery by AI agents and human contributors while preserving audit trail continuity, provenance expectations, and human-supervised validation boundaries.

## Verification Map Overview

The verification map is a structured orientation layer that connects trust-kernel domains, canonical records, validators, policy evaluation, and review routing.

The machine-readable companion index is available at `verification-map.json` with guidance at `docs/verification-map-index.md`.

It is a documentation artifact only in this phase.

## Trust Kernel Map

The trust kernel map currently covers:

1. canonical record boundaries
2. validator execution surfaces
3. policy evaluator decision boundaries
4. verification package artifacts
5. trust graph and protocol graph context
6. signing and trust anchor boundaries
7. dispute and challenge pathways
8. message/content and model provenance surfaces
9. federation discovery and routing boundaries
10. public verification API surfaces

## Canonical Records

Canonical record boundaries include schema, deterministic structure assumptions, and hash-linked continuity paths.

Reference:

- `docs/canonical-record-boundary.md`
- `docs/record-format.md`
- `schema/record-v1.schema.json`

## Validators

Validator responsibilities include deterministic verification outcomes, clear result normalization, and stable audit trail visibility.

Reference:

- `docs/public-validator.md`
- `docs/validator-capability-model.md`
- `docs/verify.md`

## Policy Evaluator

The policy evaluator governs rule interpretation and policy-bound decision logic across verification outcomes.

Reference:

- `docs/policy-evaluator.md`
- `docs/policy-engine-architecture.md`
- `docs/policy-rules.md`

## Verification Packages

Verification packages define portable evidence and export boundaries for reproducible verification.

Reference:

- `docs/verification-package-spec.md`
- `docs/verification-package-format.md`
- `docs/verification-package-validation.md`
- `docs/verification-package-generation.md`

## Trust Graph

The trust graph domain maps confidence-relevant relationships and routing context without replacing canonical record verification.

Reference:

- `docs/trust-graph.md`
- `docs/trust-graph-viewer.md`
- `docs/trust-graph-data-model.md`
- `docs/trust-query-routing.md`

## Signing Architecture

Signing architecture defines trust-anchor expectations, signature envelope boundaries, and key-management assumptions.

Reference:

- `docs/signing-architecture.md`
- `docs/signed-witness-model.md`
- `docs/witness-layer.md`

## Dispute and Challenge Layer

The dispute/challenge layer covers contested-record handling, review paths, and supersession semantics.

Reference:

- `docs/dispute-challenge-architecture.md`
- `docs/GOVERNANCE.md`
- `docs/reviewer-selection.md`

## Message and Content Provenance

Message/content provenance tracks lineage and transformation context for verification interpretation.

Reference:

- `docs/message-content-provenance.md`
- `docs/PROVENANCE.md`

## Federation Discovery

Federation discovery defines multi-node visibility and trust-routing discovery boundaries.

Reference:

- `docs/federation-discovery.md`
- `docs/federation-architecture.md`
- `docs/federation-sync.md`

## Offline Verification

Offline verification defines verification continuity constraints without live network dependency.

Reference:

- `docs/offline-verification.md`

## Verification Snapshots

Verification snapshots support reproducible state checkpoints for later audit and comparison.

Reference:

- `docs/verification-snapshots.md`

## AI Model Provenance

AI model provenance captures model-context lineage assumptions relevant to verification interpretation.

Reference:

- `docs/ai-model-provenance.md`

## Protocol Graph / Agent Context

Protocol graph and agent context documentation provide change-impact orientation before implementation edits.

Reference:

- `docs/protocol-graph-agent-context.md`
- `docs/protocol-graph-index.md`
- `protocol-graph.json`

## Public Verification API Path

Public verification API path documents external verification-facing contracts and boundary expectations.

Reference:

- `docs/public-verification-api.md`
- `docs/public-verification-flow.md`
- `docs/trust-workflow-model.md`
- `docs/verification-explorer-architecture.md`
- `docs/provenance-viewer.md`
- `docs/mvp-1-verification-package-viewer.md`
- `docs/mvp-1-user-flow.md`
- `docs/mvp-1-ui-principles.md`
- `docs/mvp-1-boundaries.md`
- `docs/verification-scenarios.md`
- `docs/demo-verification-flow.md`
- `docs/api/verification-api-v1.md`

## Agent Task Routing

Before merge, apply routing based on dominant scope:

- **docs-only** → documentation maintainers + trust-kernel terminology review
- **workflow** → CI/governance reviewers for guard continuity
- **schema** → canonical record + validator compatibility review
- **validator** → validator + policy evaluator review
- **signing** → signing/trust-anchor review with human-supervised validation
- **federation** → federation/consensus + audit trail review
- **public API** → contract compatibility + versioning review
- **trust graph** → trust graph/routing model review
- **dispute** → governance/dispute lifecycle review
- **provenance** → provenance continuity and evidence review

## Verification Impact Checklist

Complete this checklist for every non-trivial change:

- Does this affect canonical records?
- Does this affect hash validation?
- Does this affect policy evaluation?
- Does this affect signing/trust anchors?
- Does this affect federation routing?
- Does this affect public verification?
- Does this affect privacy/redaction?
- Does this affect dispute or replay handling?

If any answer is yes, require explicit human-supervised validation before merge.

## Scope and Constraints

- documentation only
- no runtime implementation
- no workflow changes
- no schema changes
- no validator changes
- no production claims

## Protocol Graph Integrity and Anti-Spoofing

Reference:

- `docs/protocol-graph-integrity.md`
- `docs/anti-spoofing-foundations.md`
- `docs/trusted-relationship-model.md`

## Agent Workspace References

Reference:

- `agents/README.md`
- `agents/chatgpt.md`
- `agents/codex.md`
- `agents/workflow.md`
- `agents/task-template.md`
- `docs/idea-to-pr-pipeline.md`
- `docs/trust-pr-engine.md`
- `docs/trust-impact-analysis.md`
- `docs/verification-proposal-model.md`
- `docs/trust-review-workflow.md`

- `docs/core-stabilization-plan.md`
- `docs/mvp-priority-roadmap.md`
- `docs/trust-ux-principles.md`
- `docs/architecture-consolidation.md`