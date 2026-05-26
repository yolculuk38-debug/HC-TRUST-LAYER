# HC:// Public Verification Challenge and Dispute Model

This document defines the HC:// public verification challenge and dispute model for HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator or guard weakening.
- Human-supervised validation remains required.
- No autonomous machine-only final authority.

## Purpose

Define a transparent and accountable challenge pathway so users, reviewers, auditors, and external participants can dispute, escalate, or re-review HC:// verification outcomes while preserving provenance continuity and audit trail visibility.

## Core principles

- Users must be able to challenge verification outcomes.
- No verifier should be beyond review.
- Disagreements must remain visible.
- Uncertainty must remain inspectable.
- Disputed outcomes should remain traceable.

These principles preserve advisory-only verification and human-supervised validation boundaries in HC-TRUST-LAYER.

## Core definitions

### verification dispute

A **verification dispute** is a formal challenge to a published or shared HC:// verification outcome based on continuity concerns, provenance gaps, methodology disagreement, or interpretation risk.

### review challenge

A **review challenge** is a request to re-check reviewer interpretation, rationale, or evidence handling when a participant identifies a potential error, omission, or bias.

### escalation request

An **escalation request** is a documented demand to route a dispute to a higher-scope or broader review body when first-line review cannot safely resolve material disagreement.

### conflicting analysis

**Conflicting analysis** exists when two or more review paths produce materially different interpretations from overlapping evidence and neither interpretation can be dismissed without further review.

### disputed provenance

**Disputed provenance** is a state where provenance continuity claims are challenged due to missing links, ambiguous lineage, inconsistent artifact references, or continuity break indicators.

### disputed AI output

**Disputed AI output** is AI-assisted or automated analysis output that is challenged for traceability, interpretation quality, model disclosure gaps, or mismatch with human-reviewed evidence.

### reviewer disagreement

**Reviewer disagreement** is a documented divergence between qualified reviewers about evidence interpretation, confidence level, or state assignment.

### federation review escalation

**Federation review escalation** is dispute routing from one review context to independent cross-organization or cross-jurisdiction participants for additional oversight and challengeability.

## Participation and visibility requirements

### public challengeability

HC:// verification outputs should include a visible challenge path so users and external participants can request re-review without relying on private authority channels.

### no unchecked verifier authority

No verifier identity (human or AI-assisted) should be treated as exempt from challenge, re-check, or escalation.

### visible disagreement surfaces

When reviewer disagreement or conflicting analysis exists, disagreement should be represented as an explicit state, not hidden behind a forced single-outcome label.

### inspectable uncertainty

Uncertainty indicators, missing continuity signals, and unresolved interpretation conflicts should remain inspectable in reviewer-facing and user-facing summaries.

### traceable dispute continuity

Dispute initiation, re-review actions, escalation decisions, and outcome updates should preserve provenance and audit trail continuity.

## Safe dispute result states

Use these states to preserve transparency and review safety:

- `DISPUTED`
- `UNDER REVIEW`
- `CONFLICT DETECTED`
- `ESCALATED REVIEW`
- `REVIEW CONSENSUS NOT REACHED`
- `TRACE AVAILABLE`

State usage guidance:

- Display meaning and limitation together.
- Keep advisory-only language explicit.
- Preserve human-supervised validation for consequential interpretation.
- Keep historical state transitions visible for audit trail continuity.

## Dispute flow examples

### 1) user challenges verification result

- A user contests an outcome and files a verification dispute with supporting references.
- The case is marked `DISPUTED` and routed to initial human reviewer triage.
- The original advisory result remains visible with dispute context attached.

### 2) independent reviewer re-check

- A separate reviewer performs an independent re-check of provenance continuity and evidence scope.
- The case transitions to `UNDER REVIEW` with explicit reviewer attribution.
- Any divergence from the prior interpretation is recorded as conflicting analysis if unresolved.

### 3) AI/human disagreement

- AI-assisted analysis suggests one interpretation while human reviewer assessment identifies a different risk profile.
- The case is labeled `CONFLICT DETECTED` and must include validator trace and reviewer rationale references.
- The outcome remains advisory pending additional human-supervised validation.

### 4) federation cross-review

- Local review cannot resolve a material dispute with sufficient confidence.
- A federation review escalation routes the case to independent external participants.
- The case state is updated to `ESCALATED REVIEW` while preserving prior reasoning and dispute chronology.

### 5) policy conflict escalation

- Reviewers identify a policy interpretation conflict affecting outcome classification.
- The dispute records affected policy-routing context and unresolved interpretation boundaries.
- If no stable consensus is reached, mark `REVIEW CONSENSUS NOT REACHED` and preserve traceable decision history.

## Anti-abuse protections

### spam dispute prevention

- Apply bounded intake controls (rate limits, duplicate suppression, and minimal evidence requirements) to reduce low-signal flooding.
- Preserve legitimate challenge access by keeping criteria transparent and reviewable.

### fake reviewer challenge prevention

- Require traceable reviewer identity/role disclosure before accepting reviewer-authority challenge assertions.
- Flag unverifiable reviewer claims for additional scrutiny.

### malicious escalation flooding

- Require escalation requests to include documented unresolved issues and prior review context.
- Use queue controls and abuse heuristics without suppressing good-faith dispute rights.

### replayed dispute artifacts

- Detect reused or context-shifted dispute packages via timestamp/context checks and continuity comparisons.
- Mark replay indicators explicitly so reviewers can inspect potential misuse.

### fake consensus screenshots

- Treat screenshots as supporting artifacts, not consensus authority evidence.
- Require traceable audit references for consensus claims.
- Flag manipulated or context-truncated screenshot claims as potential spoofing indicators.

## Implementation notes

- This model does not modify canonical records, schema contracts, validator logic, signing semantics, federation runtime behavior, policy evaluator behavior, or workflow security controls.
- This model defines challenge/dispute language and routing expectations to preserve transparency, accountability, and auditability in advisory verification.

## Related documents

- `docs/federated-oversight-model.md`
- `docs/accountability-defense-layer.md`
- `docs/verified-ai-validator-model.md`
- `docs/verification-result-states.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/trust-review-workflow.md`
- `docs/immutable-state-history-model.md`
- `docs/maintainer-accountability-model.md`
- `docs/evidence-preservation-recovery-model.md`
