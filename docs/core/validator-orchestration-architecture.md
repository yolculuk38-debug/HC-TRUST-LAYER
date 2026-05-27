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

Normal low-risk verification can proceed from review/trust-state assignment toward continuity snapshot and public verification exposure without mandatory federation cross-review or dispute escalation.

Core baseline sequence:

1. verification intake and scope framing
2. validator execution and evidence linkage
3. human-supervised review and trust-state assignment
4. continuity snapshot capture
5. public verification exposure

## Conditional branches

Federation cross-review and dispute escalation activate only after qualifying review signals:

- qualifying dispute
- unresolved conflict
- audit divergence
- elevated-risk review state

If none of these qualifying signals are present, orchestration remains on the baseline sequence.

Lifecycle routing consistency:

- Conditional branches are side-paths from the baseline sequence and do not replace the baseline for low-risk verification.
- After conditional federation cross-review or dispute escalation completes, routing returns to human-supervised trust-state confirmation and continuity snapshot capture before public verification exposure.

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
