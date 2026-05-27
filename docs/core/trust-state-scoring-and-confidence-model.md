# HC:// Trust-State Scoring and Confidence Model

This document defines an advisory trust-state scoring and confidence model for HC:// Operational Core in HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture is preserved.
- Human-supervised validation remains required.
- No schema changes.
- No validator modifications.
- No workflow changes.
- No signing, federation, policy, or canonical record behavior changes.
- No production-readiness, truth-certification, or forensic-certainty claims.

## 1) Scoring model purpose

The trust-state scoring and confidence model exists to:

- support advisory trust evaluation;
- preserve uncertainty visibility;
- reduce false confidence amplification;
- improve explainable trust signaling.

This model is not a truth engine. It is a structured interpretation layer that helps reviewers understand confidence, uncertainty, and escalation needs.

## 2) Trust-signal categories

HC:// Operational Core may evaluate confidence using the following trust-signal categories:

1. **integrity signals**
   - hash alignment status, integrity mismatch markers, and integrity continuity indicators.
2. **continuity signals**
   - lineage continuity quality, sequence coherence, and continuity-gap presence.
3. **reviewer confidence signals**
   - human-supervised validation notes, reviewer confidence statements, and review closure quality.
4. **AI advisory confidence**
   - non-authoritative AI advisory interpretation confidence and uncertainty flags.
5. **federation consistency signals**
   - cross-boundary advisory consistency, divergence indicators, and unresolved federation mismatch.
6. **audit visibility signals**
   - audit trail completeness, traceability depth, and transition observability.
7. **escalation severity signals**
   - severity classification for disputes, continuity breaks, and high-impact risk transitions.
8. **evidence quality signals**
   - evidence completeness, retrievability, provenance coherence, and integrity of supporting artifacts.
9. **replay/tamper warning signals**
   - replay suspicion markers, tamper indicators, and suspicious timeline/context reuse signals.

## 3) Confidence classifications

The model uses bounded, explainable confidence classes instead of absolute certainty states:

- **HIGH CONFIDENCE**
  - Strong multi-signal alignment, no active high-severity warnings, and clear audit visibility.
- **MODERATE CONFIDENCE**
  - Useful signal alignment with bounded uncertainty or partial caution markers.
- **LOW CONFIDENCE**
  - Significant uncertainty, weak evidence quality, or unresolved signal conflict.
- **UNRESOLVED CONFIDENCE**
  - Insufficient, contradictory, or incomplete evidence prevents stable confidence interpretation.
- **ESCALATION CONFIDENCE REVIEW**
  - High-risk, disputed, or consequential conflict requires explicit escalation and human-supervised validation.

## 4) Trust-state weighting principles

The model applies these weighting principles:

1. **no single signal determines truth**
   - no individual integrity, AI, reviewer, or federation signal can independently establish final authority.
2. **continuity improves confidence**
   - coherent continuity and stable provenance increase confidence reliability.
3. **unresolved disputes reduce confidence**
   - active disputes and unresolved objections reduce confidence classification.
4. **federation divergence reduces confidence**
   - unresolved cross-boundary divergence lowers confidence and increases review priority.
5. **missing evidence reduces confidence**
   - absent or inaccessible evidence constrains confidence and may force unresolved states.
6. **replay suspicion heavily impacts confidence**
   - replay/tamper suspicion is treated as high-impact and can trigger escalation confidence review.
7. **human review visibility increases explainability**
   - attributable reviewer input improves confidence explainability and challengeability.

## 5) Runtime scoring examples

### A) Verified low-risk document

- Integrity, continuity, audit visibility, and evidence quality signals align.
- No active dispute or replay warning.
- Reviewer confidence is documented as stable.
- Advisory classification: **HIGH CONFIDENCE** with advisory-only language.

### B) Disputed media artifact

- Integrity may align, but reviewer and contextual evidence disagree.
- Dispute and escalation severity signals are active.
- Advisory classification: **ESCALATION CONFIDENCE REVIEW**.

### C) Continuity-gap case

- Integrity may partially align, but continuity signals show lineage gap.
- Audit visibility is partial and evidence chain is incomplete.
- Advisory classification: **LOW CONFIDENCE** or **UNRESOLVED CONFIDENCE** depending on recovery state.

### D) Federation disagreement

- Local and federation consistency signals diverge without closure.
- Disagreement remains traceable and challengeable.
- Advisory classification: **LOW CONFIDENCE** with escalation pathway visibility.

### E) Incomplete evidence recovery

- Evidence recovery remains in progress and key artifacts are unavailable.
- Confidence cannot be stabilized without new evidence.
- Advisory classification: **UNRESOLVED CONFIDENCE**.

### F) Replay warning scenario

- Replay/tamper warning signals are triggered.
- Continuity and escalation severity signals indicate elevated risk.
- Advisory classification: **ESCALATION CONFIDENCE REVIEW** until human-supervised validation closes the warning.

## 6) Public-safe confidence exposure

### What users may see

Public-safe confidence exposure may include:

- current confidence classification label;
- high-level reason categories (integrity, continuity, dispute, evidence, replay warning);
- visible advisory status and escalation recommendation state;
- challenge-path and review-handoff guidance.

### What remains internal

Internal-only confidence materials include:

- sensitive reviewer identity details;
- internal routing metadata and protected escalation notes;
- private policy interpretation internals not intended for public channels;
- infrastructure-sensitive traces and non-public evidence payloads.

### Uncertainty display principles

- uncertainty must be explicit, not implied;
- unresolved conditions must remain visible;
- confidence downgrades must not be hidden;
- disagreement visibility must remain auditable.

### Advisory confidence language

Public language must preserve advisory-only boundaries, for example:

- "Confidence indicates advisory reliability, not proof."
- "This confidence state supports review and challengeability."
- "Additional human-supervised validation may be required."

## 7) Safeguards

The confidence model preserves these safeguards:

- no fake precision scoring;
- no hidden trust amplification;
- no "guaranteed true" state;
- all scoring transitions remain auditable;
- confidence changes remain traceable.

## 8) Explanation and review boundary

- confidence is not proof;
- trust scoring supports review, not authority;
- transparency is more important than perfect automation;
- challengeability must remain preserved.

HC:// trust-state scoring is an explainability aid for reviewers and operators. It does not replace human-supervised validation, canonical record boundaries, or dispute pathways.

## 9) Runtime links

This model should be interpreted alongside:

- `docs/core/verification-decision-engine-model.md`
- `docs/core/operational-verification-response-lifecycle.md`
- `docs/core/distributed-validator-consensus-coordination.md`
- `docs/core/trust-state-persistence-and-audit-runtime.md`
- `docs/core/public-verification-runtime-flow.md`
- `docs/HC_CONTROL_PANEL.md`

- `docs/core/runtime-observability-and-telemetry-model.md`

## Implementation reminder

This document is architecture and governance guidance only. It does not modify canonical records, schema contracts, validator logic, federation logic, policy evaluator behavior, signing semantics, or workflow controls.
