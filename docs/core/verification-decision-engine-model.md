# HC:// Operational Core Verification Decision Engine Model

This document defines a documentation-only decision engine model for how HC:// Operational Core evaluates verification inputs and produces consistent, advisory, and challengeable trust-state decisions in HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture is preserved.
- Human-supervised validation remains required.
- No schema, validator, federation, policy, workflow, or signing behavior changes.
- No production-readiness, truth-certification, or certainty claims.

## Decision engine purpose

The verification decision engine exists to:

- convert runtime verification signals into consistent trust-state outputs;
- preserve advisory-only semantics for all automated and AI-supported interpretation;
- prevent false certainty by keeping unresolved, disputed, and missing-evidence states explicit;
- support challengeable decisions with durable provenance and audit trail visibility.

The engine is a trust-kernel-aligned interpretation layer, not a source of autonomous final authority.

## Input signals

The engine evaluates a bounded signal set from runtime and review surfaces:

1. **schema validation result**
   - Indicates whether input structure and required fields match approved schema expectations.
2. **hash/integrity result**
   - Indicates whether integrity checks align with expected provenance references.
3. **continuity state**
   - Indicates whether record lineage continuity is intact, interrupted, or uncertain.
4. **audit history state**
   - Indicates whether prior trust-state transitions and review evidence are present and coherent.
5. **reviewer signal**
   - Human-supervised interpretation, concern notes, and acceptance/rejection observations.
6. **AI advisory signal**
   - Non-authoritative analytical input that may highlight ambiguity, risk, or inconsistency.
7. **federation signal**
   - Conditional cross-context comparison signal that may align, diverge, or remain inconclusive.
8. **dispute state**
   - Presence of active challenge, unresolved objection, or formal dispute transition.
9. **evidence preservation state**
   - Presence, retrievability, and continuity of linked verification evidence.
10. **replay/tamper warning**
    - Signal that indicates possible replay, tampering, duplication, or suspicious continuity behavior.

## Decision outputs

The engine may assign one or more compatible trust-state outputs:

- **VERIFIED**
- **ADVISORY**
- **REVIEW REQUIRED**
- **DISPUTED**
- **ESCALATION ACTIVE**
- **CONTINUITY WARNING**
- **EVIDENCE MISSING**
- **UNRESOLVED**
- **PUBLIC SAFE RESPONSE READY**

Output composition is stateful and auditable. For example, `ADVISORY + REVIEW REQUIRED` or `DISPUTED + ESCALATION ACTIVE` remain valid compound outcomes.

## Decision rules

1. **Hash match alone is not truth**
   - `hash/integrity result = match` does not bypass continuity, dispute, or evidence-preservation checks.
2. **AI advisory alone is not final authority**
   - AI advisory signals may inform triage but cannot produce autonomous final trust closure.
3. **Federation is conditional**
   - Federation inputs may contribute to interpretation when available, but normal local verification must remain possible without mandatory federation dependency.
4. **Disagreement remains visible**
   - Human, AI, validator, and federation disagreements remain auditable and must not be collapsed into silent certainty states.
5. **High-risk signals trigger review/escalation**
   - Replay/tamper warnings, continuity breaks, unresolved dispute states, or severe divergence trigger `REVIEW REQUIRED` and/or `ESCALATION ACTIVE`.
6. **Missing evidence must remain visible**
   - Missing or unlinked evidence requires explicit `EVIDENCE MISSING` and cannot be represented as settled verification.
7. **Public response must remain safe and inspectable**
   - Public-safe responses require auditable transition context, provenance references, and explicit advisory boundaries.

## Decision flow examples

### 1) Normal text hash verification

- Schema validation passes.
- Hash/integrity checks match.
- Continuity and audit history remain coherent.
- No dispute, replay, or federation divergence signal appears.
- Engine outputs: `VERIFIED + ADVISORY + PUBLIC SAFE RESPONSE READY`.

### 2) Disputed image/media record

- Integrity checks may pass, but reviewer signal raises provenance interpretation conflict.
- Dispute state is active with unresolved objection.
- Engine outputs: `DISPUTED + ESCALATION ACTIVE + REVIEW REQUIRED`.
- Public-safe output excludes certainty language and keeps dispute visibility explicit.

### 3) Missing evidence case

- Schema validation passes, but linked evidence is unavailable or continuity breaks.
- Engine outputs: `EVIDENCE MISSING + CONTINUITY WARNING + UNRESOLVED`.
- Record remains challengeable and cannot be represented as verified closure.

### 4) AI/human disagreement

- AI advisory recommends lower-risk interpretation.
- Reviewer signal identifies unresolved contextual risk.
- Engine preserves disagreement and assigns: `ADVISORY + REVIEW REQUIRED` (and `UNRESOLVED` if no documented closure).

### 5) Federation divergence

- Local verification and conditional federation signal disagree on trust-state interpretation.
- Engine assigns: `REVIEW REQUIRED + ESCALATION ACTIVE` with divergence trace retained in audit history.
- Federation does not silently override local reviewer authority.

### 6) Replay suspicion

- Replay/tamper warning is triggered despite partial integrity alignment.
- Engine assigns: `CONTINUITY WARNING + REVIEW REQUIRED + ESCALATION ACTIVE`.
- Decision remains advisory and challengeable until human-supervised validation resolves the warning.

## Safety constraints

The decision engine must preserve these runtime safety constraints:

- **no silent override**
  - No critical signal may be hidden or auto-suppressed without audit trail visibility.
- **no hidden upgrade/downgrade**
  - Trust-state changes require explicit, auditable transition events.
- **no "truth certified" output**
  - Output language must remain advisory and avoid certainty or final-truth claims.
- **no private data exposure**
  - Public-safe responses must avoid private or sensitive verification payload disclosure.
- **all important decision transitions remain auditable**
  - High-impact transitions (dispute, escalation, continuity warning, evidence missing, unresolved closure) must persist with provenance continuity.

## Runtime links

This model aligns with and should be interpreted alongside:

- `docs/core/runtime-state-model.md`
- `docs/core/operational-verification-response-lifecycle.md`
- `docs/core/trust-state-persistence-and-audit-runtime.md`
- `docs/core/distributed-validator-consensus-coordination.md`
- `docs/core/public-qr-verification-gateway.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/core/trust-state-scoring-and-confidence-model.md`

## Implementation reminder

This document is a governance and architecture reference for HC:// Operational Core only. It does not modify canonical records, schema contracts, validator logic, federation logic, policy evaluator behavior, signing semantics, or workflow controls.
