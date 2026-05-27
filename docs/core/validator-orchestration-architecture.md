# HC:// Validator Orchestration Architecture

This document defines the validator orchestration routing architecture for HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only architecture guidance.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator or guard weakening.
- Human-supervised validation remains required.
- No mandatory federation escalation for low-risk verification.

## Purpose

Provide an inspectable orchestration routing model that preserves modular Operational Core architecture while ensuring federation cross-review and dispute escalation are conditional, not mandatory linear steps.

## Routing baseline

Normal verification remains lightweight and local-first. Uncontested records can complete verification without mandatory federation cross-review or dispute escalation.

Core baseline sequence:

1. intake
2. schema validation
3. integrity verification
4. local validator review
5. public verification

## Conditional branches

Federation cross-review, dispute escalation, and continuity escalation activate only after qualifying review signals:

- qualifying dispute
- unresolved conflict
- audit divergence
- elevated-risk review state

If none of these qualifying signals are present, orchestration remains on the baseline sequence.

Lifecycle routing consistency:

- Conditional branches are side-paths from the baseline sequence and do not replace the baseline for low-risk verification.
- After a conditional path completes, routing returns to local validator review closure and human-supervised verification confirmation before public verification.

## Conditional federation routing

Federation cross-review is conditional and is routed only when independent cross-context review is required to address unresolved or elevated-risk interpretation boundaries.

Trigger examples:

- local review cannot resolve material conflicting analysis
- consequential interpretation risk remains elevated after local review
- audit continuity indicates unresolved divergence requiring independent comparison

## Conditional dispute escalation routing

Dispute escalation is conditional and is routed only when dispute handling cannot be safely resolved in the current review scope.

Trigger examples:

- qualifying dispute remains unresolved after documented re-review
- conflicting analysis persists with consequential decision-path impact
- audit divergence remains open across checkpoints or review snapshots


## Conditional continuity escalation routing

Continuity escalation is conditional and is routed only when continuity integrity cannot be resolved within baseline local validator review.

Trigger examples:

- continuity chain gaps remain unresolved after local evidence re-check
- provenance linkage divergence affects review closure for the current verification lifecycle
- unresolved continuity ambiguity prevents transparent audit trail closure

## Orchestration safety constraints

- Preserve advisory-only verification.
- Preserve human-supervised validation for consequential interpretation.
- Preserve inspectability and accountability through traceable routing states.
- Preserve modular and extensible Operational Core boundaries.
- Do not alter canonical record boundaries, schema contracts, validator logic, signing semantics, federation runtime behavior, policy evaluator behavior, or workflow security controls.

## Related documents

- `docs/public-verification-disputes.md`
- `docs/multi-layer-consensus-model.md`
- `docs/governance/governance-structure-map.md`
- `docs/architecture/operational-core-transition-map.md`
- `docs/core/runtime-state-model.md`
