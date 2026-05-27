# HC:// Trust Taxonomy and Terminology Model

This document standardizes HC:// trust language, canonical artifact boundaries, and verification terminology across HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator or guard weakening.
- Human-supervised validation remains required.
- No incompatible redefinition of existing trust-kernel semantics.

## Purpose

Define a shared terminology and trust-state baseline so governance, validation, federation, audit, AI review, and public verification layers remain aligned, traceable, and reviewable.

## Canonical boundary model

### canonical record

A **canonical record** is a repository-defined source-of-truth record within canonical record boundaries.

Canonical records are authoritative for continuity evaluation within scope, but they are still interpreted through advisory verification and human-supervised validation.

### generated artifact

A **generated artifact** is machine-produced or tool-produced support output (for example: index material, reports, previews, helper manifests, or derived summaries).

Generated artifacts are not automatically canonical and must not be treated as canonical record substitutes.

### advisory output

An **advisory output** is a verification, validator, reviewer-assist, or analysis result that supports interpretation but does not establish conclusive truth claims or autonomous final authority.

### federation mirror

A **federation mirror** is a replicated or synchronized representation of trust-relevant material across federation participants.

Federation mirrors may diverge from canonical continuity and therefore require continuity checks, provenance comparison, and reviewer oversight.

### audit snapshot

An **audit snapshot** is a point-in-time capture used for review, diagnostics, or audit packaging.

An audit snapshot is evidence support, not a canonical continuity replacement.

### derived visualization

A **derived visualization** is a rendered representation (charts, dashboards, screenshots, previews, explorer views) created from underlying records or artifacts.

Derived visualizations are interpretive aids and may not contain full state context.

### exported artifact

An **exported artifact** is a packaged output prepared for transfer, sharing, interoperability, or external inspection.

Exported artifacts remain boundary-scoped and should be verified against canonical continuity before consequential interpretation.

### public verification artifact

A **public verification artifact** is a user-facing verification output intended for transparent communication to non-expert audiences.

Public verification artifacts should remain traceable to canonical continuity references and advisory limitations.

## Boundary interpretation guidance

- Generated artifacts are not automatically canonical.
- Advisory analysis is not conclusive proof.
- Federation mirrors may diverge from canonical continuity.
- Screenshots and previews may not represent full audit state.
- Public trust signals should remain traceable to inspectable references.

## Trust-state taxonomy

Use the following standardized trust-state labels for advisory communication and review routing:

- `VERIFIED`
- `REVIEW REQUIRED`
- `DISPUTED`
- `CONSENSUS PARTIAL`
- `CONSENSUS NOT REACHED`
- `POSSIBLE TAMPERING`
- `CONTINUITY GAP DETECTED`
- `EVIDENCE MISSING`
- `TRACE AVAILABLE`
- `HISTORY INCOMPLETE`
- `EMERGENCY INTEGRITY REVIEW`

State usage expectations:

- Keep limitation language visible for each state.
- Avoid truth-guarantee wording.
- Preserve human-supervised validation requirements for consequential use.
- Keep dispute and escalation pathways explicit.

## Terminology model

### advisory verification

**Advisory verification** is verification guidance designed to inform review, not replace human-supervised validation.

### trust signal

A **trust signal** is a state or indicator that helps communicate verification posture, continuity condition, or review need.

### continuity

**Continuity** is the traceable linkage of provenance, record lineage, and review-relevant transitions over time.

### traceability

**Traceability** is the ability to inspect and follow evidence, decisions, and state transitions through documented references.

### validator

A **validator** is a system or process component that checks inputs or evidence against defined rules and emits advisory outputs.

### reviewer

A **reviewer** is a human oversight actor responsible for contextual interpretation, challenge handling, and consequential trust decisions.

### federation review

**Federation review** is multi-party, cross-organization review of trust-relevant evidence with visible comparison of interpretations.

### audit divergence

**Audit divergence** is a mismatch between expected and observed audit continuity, requiring investigation and visible caution labeling.

### replay artifact

A **replay artifact** is reused prior output or evidence presented in a new context; it requires context and continuity checks to prevent misinterpretation.

### override event

An **override event** is a documented human action that changes review interpretation or workflow direction with explicit rationale and trace continuity.

### immutable-style history

**Immutable-style history** is an append-oriented, continuity-preserving chronology model where changes remain visible and challengeable.

## Public explanation guidance

- Terminology should remain understandable to non-experts.
- Trust language should avoid false certainty.
- Uncertainty should remain visible.
- Public explanations should distinguish review from proof.
- Public-facing summaries should map each trust signal to evidence scope and limitation.

## Operational philosophy

HC:// trust operations in HC-TRUST-LAYER should preserve:

- trust through traceability
- accountability before authority
- visibility over hidden control
- challengeable verification
- inspectable governance

## Implementation notes

- This model is documentation guidance and does not alter canonical records, schema contracts, validator logic, signing semantics, federation runtime behavior, policy evaluator behavior, or workflow security controls.
- This model preserves advisory-only verification and human-supervised validation as mandatory boundaries.
- This model should be read alongside protocol graph, verification map, and trust kernel index references for routing and review context.

## Related documents

- `HC_CONSTITUTION.md`
- `docs/FOUNDATION_STATUS.md`
- `docs/verification-result-states.md`
- `docs/immutable-state-history-model.md`
- `docs/federated-oversight-model.md`
- `docs/HC_CONTROL_PANEL.md`
