# HC:// Evidence Preservation and Continuity Recovery Model

This document defines the HC:// evidence preservation and continuity recovery model for HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator or guard weakening.
- Human-supervised validation remains required.
- No impossible permanence or forensic certainty claims.

## Purpose

Define how HC:// preserves continuity, detects missing evidence, and supports recovery and reconstruction of traceability when records, artifacts, reviews, or audit history are lost, deleted, corrupted, or disputed.

## Core definitions

### evidence preservation

**Evidence preservation** is the set of documentation and workflow expectations that keep verification-relevant references, continuity signals, and accountability context visible over time.

### continuity recovery

**Continuity recovery** is the documented process for re-establishing inspectable trace links after continuity loss, corruption, deletion, or disputed evidence removal.

### missing artifact state

A **missing artifact state** is an explicit condition indicating that a referenced artifact cannot be retrieved in its expected location or form.

### deleted evidence trace

A **deleted evidence trace** is the remaining continuity signal that a previously referenced artifact or record existed, even if underlying content is no longer directly available.

### continuity checkpoint

A **continuity checkpoint** is a bounded, timestamped, reviewable reference point used to compare later state continuity and detect divergence.

### audit snapshot

An **audit snapshot** is an immutable-style, inspectable capture of verification-relevant references and context at a specific review moment.

### federation mirror

A **federation mirror** is a secondary, independently managed reference surface that may preserve continuity signals when a primary surface loses evidence.

### recovery escalation

**Recovery escalation** is routing continuity failure or evidence-loss events to broader human-supervised validation and reviewer oversight.

### trace reconstruction

**Trace reconstruction** is the documented, challengeable attempt to rebuild continuity visibility using available references, prior snapshots, federation mirrors, and audit trail fragments.

## Continuity visibility expectations

- Deleted content may still leave continuity traces through prior references, checkpoints, snapshots, and mirrored evidence paths.
- Systems should preserve accountability signals where possible, even when full artifact recovery is not possible.
- Evidence disappearance should remain visible as an explicit state, not silently absorbed.
- Continuity gaps should remain inspectable with timestamped indicators and reviewer notes.
- Recovery attempts should remain traceable, attributed, and reviewable.

These expectations preserve advisory-only verification and human-supervised validation boundaries.

## Risk scenarios

### deleted records

- Risk: record files are removed from expected continuity locations.
- Visibility expectation: missing-record signals and prior continuity references should remain inspectable.

### removed media

- Risk: supporting media is deleted, moved, or made inaccessible.
- Visibility expectation: deleted evidence trace markers should preserve accountability context.

### corrupted audit trail

- Risk: audit history segments become unreadable, inconsistent, or partially overwritten.
- Visibility expectation: continuity checkpoint mismatches and trace incompleteness signals should surface.

### missing validator history

- Risk: validator run history is unavailable or incomplete for a consequential result.
- Visibility expectation: explicit continuity warning states should prevent hidden confidence inflation.

### lost dispute history

- Risk: dispute chronology is missing, reducing challengeability of prior outcomes.
- Visibility expectation: dispute preservation expectations should signal unresolved history loss.

### silent evidence removal

- Risk: evidence disappears without explicit event disclosure.
- Visibility expectation: continuity controls should mark possible removal rather than imply normal continuity.

### federation mismatch

- Risk: local continuity references do not align with federation mirror references.
- Visibility expectation: cross-reference divergence should be visible and escalated for review.

### continuity divergence

- Risk: expected lineage progression conflicts with observed artifacts and checkpoints.
- Visibility expectation: divergence should be represented as a caution state and investigation path.

### manipulated recovery attempt

- Risk: a reconstruction process is altered to hide prior loss, failure, or tampering.
- Visibility expectation: recovery audit logging and reviewer attribution should make manipulation attempts inspectable.

## Defensive principles

- append-style audit continuity
- distributed checkpoint visibility
- federation cross-reference
- public traceability
- recovery audit logging
- dispute preservation
- continuity warning states

## Safe public states

Use these states to preserve transparent, challengeable continuity and recovery signaling:

- `EVIDENCE MISSING`
- `CONTINUITY GAP DETECTED`
- `RECOVERY IN PROGRESS`
- `TRACE PARTIALLY RECOVERED`
- `FEDERATION MIRROR AVAILABLE`
- `AUDIT SNAPSHOT AVAILABLE`
- `POSSIBLE EVIDENCE REMOVAL`
- `HISTORY INCOMPLETE`

State usage guidance:

- Show meaning and limitation together.
- Preserve advisory-only interpretation boundaries.
- Keep missing history and continuity gaps visible instead of hidden.
- Preserve human-supervised validation for consequential interpretation.

## Accountability during failure conditions

- HC:// should preserve accountability even during failures, deletions, corruption, or dispute pressure.
- Silent disappearance of important traces should be discouraged by continuity checkpoints, snapshot references, and explicit warning states.
- Recovery attempts must remain inspectable through attributable logging and escalation references.
- Missing history should remain visible instead of hidden so reviewers can assess uncertainty and residual risk.

## Recovery and reconstruction guidance

- Recovery and reconstruction should prefer documented, reversible steps with clear provenance.
- When full evidence cannot be restored, systems should preserve continuity metadata and caution states.
- Reconstruction outcomes should distinguish between confirmed recovery, partial recovery, and unresolved loss.
- Human-supervised validation remains required before consequential interpretation changes.

## Implementation notes

- This model does not modify canonical records, schema contracts, validator logic, signing semantics, federation runtime behavior, policy evaluator behavior, or workflow security controls.
- This model defines documentation guidance for evidence preservation, continuity gap visibility, and trace reconstruction accountability.

## Related documents

- `docs/immutable-state-history-model.md`
- `docs/maintainer-accountability-model.md`
- `docs/public-verification-disputes.md`
- `docs/federated-oversight-model.md`
- `docs/verification-result-states.md`
- `docs/HC_CONTROL_PANEL.md`
