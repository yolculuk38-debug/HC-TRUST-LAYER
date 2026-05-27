# HC:// Operational Core Runtime State Model

This document defines the deterministic runtime state model for HC:// Operational Core in HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only runtime model.
- Advisory-only verification posture is preserved.
- Human-supervised validation remains required.
- No canonical schema changes.
- No validator or guard weakening.
- Conditional federation routing is preserved.
- No blockchain, token, production-readiness, or truth-guarantee claims.

## Purpose

Provide a deterministic, auditable runtime-state lifecycle to guide autonomous validator runtime architecture planning while preserving trust-kernel safety boundaries and review authority.

## Core runtime lifecycle states

1. **INTAKE**
   - Verification input is received and routed into the runtime lifecycle.
2. **SCHEMA_VALIDATION**
   - Input is checked against existing canonical schema requirements.
3. **INTEGRITY_VERIFICATION**
   - Hash/provenance integrity checks execute for lifecycle continuity.
4. **LOCAL_REVIEW**
   - Local validator analysis and human-supervised review context are prepared.
5. **TRUST_STATE_ASSIGNMENT**
   - A stable trust-state assignment is produced for the record lifecycle.
6. **PUBLIC_VERIFICATION_READY**
   - Public verification exposure is allowed after stable assignment and required review closure.
7. **ARCHIVED**
   - Lifecycle outcome and trace evidence are retained for audit trail continuity.

## Conditional states

- **AI_ADVISORY_REVIEW**
- **HUMAN_REVIEW_REQUIRED**
- **FEDERATION_REVIEW**
- **DISPUTE_ESCALATION**
- **CONTINUITY_WARNING**
- **EVIDENCE_MISSING**
- **RECOVERY_REVIEW**
- **EMERGENCY_INTEGRITY_REVIEW**

These states are conditional and activate only when qualifying runtime signals are present.

## Deterministic transition flows

### 1) Normal low-risk verification flow

`INTAKE -> SCHEMA_VALIDATION -> INTEGRITY_VERIFICATION -> LOCAL_REVIEW -> TRUST_STATE_ASSIGNMENT -> PUBLIC_VERIFICATION_READY -> ARCHIVED`

### 2) Conditional AI review flow

`LOCAL_REVIEW -> AI_ADVISORY_REVIEW -> LOCAL_REVIEW -> TRUST_STATE_ASSIGNMENT`

- AI output remains advisory-only.
- Consequential interpretation remains human-supervised.

### 3) Conditional human review flow

`LOCAL_REVIEW -> HUMAN_REVIEW_REQUIRED -> LOCAL_REVIEW -> TRUST_STATE_ASSIGNMENT`

- Human-supervised validation is required for unresolved or elevated-risk interpretation states.

### 4) Dispute escalation flow

`LOCAL_REVIEW -> DISPUTE_ESCALATION -> HUMAN_REVIEW_REQUIRED -> LOCAL_REVIEW -> TRUST_STATE_ASSIGNMENT`

- Dispute routing is not default runtime behavior.

### 5) Federation review flow

`LOCAL_REVIEW -> FEDERATION_REVIEW -> HUMAN_REVIEW_REQUIRED -> LOCAL_REVIEW -> TRUST_STATE_ASSIGNMENT`

- Federation routing is conditional and not mandatory for normal records.

### 6) Evidence recovery flow

`INTEGRITY_VERIFICATION -> CONTINUITY_WARNING -> EVIDENCE_MISSING -> RECOVERY_REVIEW -> LOCAL_REVIEW -> TRUST_STATE_ASSIGNMENT`

- Recovery remains traceable and linked to the same lifecycle provenance.

### 7) Emergency integrity flow

`INTEGRITY_VERIFICATION -> EMERGENCY_INTEGRITY_REVIEW -> HUMAN_REVIEW_REQUIRED -> DISPUTE_ESCALATION (if unresolved) -> LOCAL_REVIEW -> TRUST_STATE_ASSIGNMENT`

- Emergency signals remain visible, auditable, and publicly accountable.

## State separation model

The runtime model separates lifecycle lanes to preserve deterministic interpretation:

- **normal verification lane:** baseline low-risk progression.
- **escalation lane:** dispute and elevated-risk handling.
- **federation lane:** independent cross-context comparison.
- **recovery lane:** continuity and missing-evidence remediation.
- **emergency integrity lane:** high-priority integrity anomaly handling.

## Transition rules

1. Federation review must not be mandatory for normal records.
2. Dispute escalation must only occur after qualifying conflict, divergence, elevated risk, or unresolved review state.
3. Public verification exposure requires stable trust-state assignment.
4. Recovery states must remain traceable across continuity and evidence handling.
5. Emergency states must remain public and auditable.

## Examples

### Example A: normal text/hash verification

- Runtime enters `INTAKE`, `SCHEMA_VALIDATION`, and `INTEGRITY_VERIFICATION`.
- No elevated-risk signal is raised in `LOCAL_REVIEW`.
- Runtime assigns trust state and reaches `PUBLIC_VERIFICATION_READY`, then `ARCHIVED`.

### Example B: disputed media artifact

- Runtime reaches `LOCAL_REVIEW` with conflicting reviewer interpretation.
- Runtime enters `DISPUTE_ESCALATION`, then `HUMAN_REVIEW_REQUIRED`.
- After documented resolution, flow returns to `TRUST_STATE_ASSIGNMENT` and archival.

### Example C: missing evidence case

- Integrity checks trigger `CONTINUITY_WARNING` and `EVIDENCE_MISSING`.
- Runtime enters `RECOVERY_REVIEW` for evidence re-linking and provenance continuity checks.
- Record returns to `LOCAL_REVIEW` only after traceable recovery steps.

### Example D: federation divergence case

- Local review and federation comparison produce trust-state divergence.
- Runtime enters `FEDERATION_REVIEW` and then `HUMAN_REVIEW_REQUIRED`.
- Runtime returns to local closure with explicit divergence trace before trust-state assignment.

## Implementation and boundary reminder

This model is an architecture and governance reference only. It does not modify canonical schema contracts, validator logic, signing semantics, federation runtime behavior, policy evaluator behavior, or workflow security controls.

## Related references

- `docs/architecture/operational-core-transition-map.md`
- `docs/core/validator-orchestration-architecture.md`
- `docs/governance/governance-structure-map.md`
- `docs/security/threat-model-master-map.md`
- `docs/HC_CONTROL_PANEL.md`
