# HC:// Multi-Layer Consensus and Conflict Resolution Model

This document defines the HC:// multi-layer consensus and conflict resolution model for HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator or guard weakening.
- Human-supervised validation remains required.
- No objective-certainty or infallible-consensus claims.

## Purpose

Define how HC:// handles conflicting verification outcomes across AI systems, human reviewers, federation validators, audit history, and public review layers while preserving transparency, accountability, and dispute visibility.

## Consensus layers

### AI consensus

**AI consensus** is the alignment or divergence pattern across one or more AI-assisted validator outputs over the same verification scope.

AI consensus is advisory-only and cannot independently finalize consequential outcomes.

### human reviewer consensus

**Human reviewer consensus** is a documented convergence among assigned human reviewers regarding interpretation, confidence, and recommended state assignment.

Human reviewer consensus requires attributable rationale and remains challengeable.

### federation cross-review

**Federation cross-review** is independent cross-organization or cross-context review of the same evidence package to reduce single-context interpretation risk.

Federation cross-review is conditional and is activated after qualifying dispute, unresolved conflict, audit divergence, or elevated-risk review state.

Federation cross-review may confirm, refine, or dispute local interpretations.

### conflicting analysis

**Conflicting analysis** exists when two or more review layers produce materially different conclusions from overlapping evidence, provenance, or policy context.

### disagreement escalation

**Disagreement escalation** is the explicit routing process used when conflicting analysis remains unresolved after initial review.

Escalation must preserve prior rationale, states, and audit chronology.

### consensus weighting

**Consensus weighting** is the documented method for comparing confidence and traceability signals across review layers without granting silent authority to any single actor.

Weighting is bounded by advisory-only interpretation and human-supervised validation requirements.

### unresolved dispute state

An **unresolved dispute state** is the explicit representation that material disagreement remains open and has not been safely collapsed into a forced single outcome.

### review divergence

**Review divergence** is a traceable difference in interpretation, confidence, or policy application between reviewers, validators, or federation participants.

### confidence layering

**Confidence layering** is the practice of showing confidence signals per layer (AI, human, federation, audit continuity) instead of presenting one opaque aggregate score.

## Conflict visibility expectations

- Different reviewers may reach different conclusions from the same evidence.
- Disagreement should remain visible instead of hidden behind forced certainty.
- No single reviewer, validator, or AI system should silently dominate outcomes.
- Unresolved conflicts should remain inspectable with traceable rationale.
- Escalation paths should remain attributable and auditable.

These expectations preserve advisory-only verification and human-supervised validation boundaries.

## Confidence and weighting guidance

### no silent dominance

Consensus weighting must not silently privilege one reviewer or AI output without documented rationale.

### rationale-linked weighting

Any confidence adjustment should be linked to traceability, reviewer attribution, evidence continuity, and policy interpretation notes.

### layer-specific confidence

Confidence should be presented per layer so reviewers can inspect where alignment is strong, weak, or disputed.

### bounded interpretation

High confidence in one layer does not create objective certainty and does not remove dispute rights.

## Conflict scenarios

### AI says LOW RISK / human says HIGH RISK

- AI-assisted output indicates low risk while human reviewers identify high-risk indicators.
- Mark visible review conflict and route to disagreement escalation.
- Preserve both rationales with validator trace and reviewer attribution.

### federation disagreement

- Local reviewers reach one interpretation while federation cross-review reaches another.
- Preserve both interpretations and record cross-review divergence.
- Route to escalated review when consequential interpretation differs.

### disputed provenance

- Provenance continuity claims are challenged due to missing or inconsistent lineage references.
- Mark unresolved dispute state until continuity concerns are reviewed.
- Preserve dispute chronology and recovery references.

### manipulated evidence suspicion

- Reviewers suspect evidence manipulation, truncation, or context laundering.
- Preserve suspicion markers, affected artifacts, and reviewer rationale in the audit trail.
- Route to escalated review instead of silent reclassification.

### conflicting audit continuity

- Audit history and current evidence references conflict or cannot be reconciled.
- Mark continuity conflict and keep uncertainty visible.
- Preserve trace links to all conflicting checkpoints and snapshots.

### policy interpretation conflict

- Reviewers or validator outputs disagree on policy interpretation boundaries.
- Record affected policy-routing context and decision-path differences.
- Use escalation paths for human-supervised validation before consequential interpretation changes.

### validator reputation conflict

- Participants challenge whether a validator output should be trusted due to reputation concerns.
- Preserve challenge evidence and validator traceability context.
- Prevent reputation-only override without inspectable rationale.

## Defensive principles

- visible disagreement
- escalation instead of silent override
- federation cross-checking
- reviewer accountability
- confidence transparency
- dispute preservation
- traceable consensus evolution

## Safe public states

Use these states to preserve transparent, challengeable consensus visibility:

- `CONSENSUS PARTIAL`
- `CONSENSUS NOT REACHED`
- `REVIEW CONFLICT DETECTED`
- `FEDERATION DISAGREEMENT`
- `ESCALATED REVIEW`
- `HUMAN REVIEW REQUIRED`
- `AI CONSENSUS LIMITED`
- `TRACE AVAILABLE`

State usage guidance:

- Show meaning and limitation together.
- Keep conflicting analysis visible through state transitions.
- Preserve advisory-only interpretation boundaries.
- Maintain human-supervised validation for consequential interpretation.

## Interpretation guidance

### expose uncertainty

HC:// should expose uncertainty instead of hiding it behind implied certainty.

### consensus is not objective certainty

Consensus signals represent review alignment conditions, not objective or infallible certainty.

### visible conflict is healthier than fake certainty

Visible conflict can be safer than forced consensus because it preserves challengeability and reduces hidden authority risk.

### preserve inspectable disagreement

Trust systems should preserve inspectable disagreement so reviewers and external participants can evaluate unresolved risk boundaries.

## Implementation notes

- This model does not modify canonical records, schema contracts, validator logic, signing semantics, federation runtime behavior, policy evaluator behavior, or workflow security controls.
- This model defines documentation guidance for multi-layer consensus visibility, disagreement escalation, and conflict preservation.

## Related documents

- `docs/evidence-preservation-recovery-model.md`
- `docs/public-verification-disputes.md`
- `docs/verified-ai-validator-model.md`
- `docs/federated-oversight-model.md`
- `docs/verification-result-states.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/governance/validator-ethics-and-conduct.md`
- `docs/governance/governance-structure-map.md`
