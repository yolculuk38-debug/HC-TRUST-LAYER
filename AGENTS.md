# AGENTS.md — HC-TRUST-LAYER Contributor and Agent Guide

## Project Identity

HC-TRUST-LAYER is the canonical repository for the HC:// verification infrastructure.

HC:// is a verification and provenance protocol surface focused on integrity, reproducibility, and transparent review boundaries.

## Terminology Baseline

Use and preserve these terms consistently:

- HC-TRUST-LAYER
- HC://
- verification map
- trust kernel
- protocol graph
- agent context
- provenance
- audit trail
- canonical record
- human-supervised validation

## Core Rule

The repository is the source of truth for architecture, policy baselines, implementation status, and verification documentation.

Do not override repository evidence with external assumptions.

## Human-Supervised Validation

All non-trivial trust-kernel-impacting changes require explicit human-supervised validation.

Agent output is advisory unless validated through repository-defined checks and reviewer oversight.

## Agent Behavior Rules

- Prefer documentation-first clarification before behavior changes.
- Preserve canonical terminology and boundary semantics.
- Surface uncertainty instead of inferring unsupported production guarantees.
- Route cross-domain changes to the proper reviewers.
- Keep change scope minimal and auditable.

## Safe Task Boundaries

Safe tasks include:

- documentation improvements
- navigation aids
- reference linking and map maintenance
- non-behavioral clarification of trust-kernel boundaries

Escalate before changing:

- runtime verification behavior
- schema contracts
- validator logic
- signing and trust anchor semantics
- federation behavior
- policy evaluator behavior

## Forbidden Claims

Do not claim any of the following unless implemented and validated in-repo:

- production readiness
- live federation guarantees
- complete dispute automation
- autonomous governance finality
- cryptographic or policy guarantees not backed by tests/docs

## Required Checks Before PR

Run applicable guards and checks before proposing merge:

- terminology guard
- docs drift guard
- canonical artifact guard
- relevant test subsets when touched scope requires

If a check cannot run, document the reason and do not imply success.

## Canonical Record Boundaries

Treat canonical record surfaces as high-sensitivity boundaries:

- schema definitions
- deterministic serialization assumptions
- hash-linked artifacts
- record identity and provenance continuity

Any direct or indirect boundary impact requires explicit reviewer escalation.

## Policy Evaluator Expectations

Changes that affect policy interpretation or routing must:

- identify affected policy rules
- declare expected decision-path differences
- preserve audit trail continuity
- receive human-supervised validation prior to merge

## Workflow Safety Rules

- Keep CI and governance guardrails intact unless intentionally updated with approval.
- Do not bypass terminology/docs/canonical artifact controls.
- Do not merge trust-kernel-impacting changes without explicit impact checklist coverage.
- Prefer reversible, well-scoped changes with clear provenance in commit history.

## Machine-readable Protocol Graph Index

- `protocol-graph.json`
- `docs/protocol-graph-index.md`

Use these as advisory navigation aids alongside the verification map and protocol graph documentation.

## Protocol Graph Integrity and Anti-Spoofing References

- `docs/protocol-graph-integrity.md`
- `docs/anti-spoofing-foundations.md`
- `docs/trusted-relationship-model.md`
