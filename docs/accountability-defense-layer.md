# HC Accountability and Defense Layer Model

This document defines the HC:// accountability and defense layer model for HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only model.
- Advisory-only verification posture.
- No canonical schema changes.
- No validator or guard weakening.
- Human-supervised validation remains required.
- No repository-stored secrets.

## Purpose

Provide a clear, auditable model for protecting trust integrity against internal abuse, external attacks, spoofing, manipulation attempts, and reviewer/validator misuse.

## Protected roles

### HC maintainers

- Maintain repository guardrails, review boundaries, and canonical record protection.
- Must preserve audit trail continuity for trust-kernel-impacting discussions and actions.

### human reviewers

- Perform human-supervised validation for consequential interpretation and approval decisions.
- Must keep reviewer identity, rationale, and conflict handling traceable.

### AI validators

- Provide advisory AI-assisted analysis with validator trace continuity.
- Must never be treated as autonomous final authority.

### automation agents

- Support bounded, reviewable operations and documentation workflows.
- Must not bypass required validation, reviewer oversight, or canonical boundaries.

### federation participants

- Exchange verification and provenance context using declared trust boundaries.
- Must preserve traceability and avoid overclaiming authority.

### external users

- Consume public verification signals with explicit advisory limits.
- Must be able to inspect uncertainty and continuity signals without hidden assumptions.

## Threat model coverage

### fake verified record

- Risk: a non-canonical or tampered artifact is presented as verified.
- Defense: enforce canonical record boundary checks, continuity checks, and reviewer verification against canonical paths.

### fake validator identity

- Risk: attacker claims a validator identity without recognized traceability.
- Defense: require authenticated validator identity mapping and validator trace references.

### fake AI approval

- Risk: fabricated "AI approved" wording or badge is used to bypass review.
- Defense: require explicit advisory state labels and traceable validator-run evidence.

### bribed reviewer

- Risk: reviewer decisions are influenced by undisclosed external incentives.
- Defense: enforce multi-party review escalation and auditable review notes for sensitive outcomes.

### biased reviewer

- Risk: reviewer bias distorts interpretation without transparent challenge path.
- Defense: require conflict escalation and cross-review when material disagreement or risk indicators appear.

### compromised maintainer

- Risk: privileged maintainer account or workflow is abused.
- Defense: preserve branch protections, reviewer oversight, and immutable-style commit history with audit trail checks.

### manipulated generated artifact

- Risk: generated output is edited to imitate canonical authority.
- Defense: keep generated artifact warnings persistent and require canonical-reference verification.

### replay attack

- Risk: prior valid validator exchange is replayed as a current approval.
- Defense: require nonce/time-bound authentication context and audit-log replay detection.

### QR spoofing

- Risk: malicious QR destination imitates trusted verification routes.
- Defense: require route/domain checks, anti-spoof warnings, and state-based caution signaling.

### unauthorized record modification

- Risk: canonical record surfaces are modified outside approved workflow.
- Defense: enforce canonical artifact guardrails, provenance checks, and reviewer escalation.

### fake public verification page

- Risk: copied or hostile page impersonates HC:// verification UX.
- Defense: require visible boundaries, advisory state signals, and continuity references that reviewers can inspect.

## Defense principles

- transparency by default
- signed/traceable reviewer identity
- authenticated AI validator access
- multi-layer verification
- audit logs
- immutable-style history
- canonical record boundaries
- generated artifact warnings
- human + AI cross-check
- conflict escalation
- public accountability

## Safe system states

Use these states to preserve visible safety posture:

- `VERIFIED WITH TRACE`
- `REVIEW REQUIRED`
- `CONFLICT DETECTED`
- `VALIDATOR TRACE MISSING`
- `POSSIBLE SPOOF`
- `HUMAN OVERRIDE REQUIRED`
- `AUDIT TRAIL PRESENT`
- `CANONICAL RECORD PROTECTED`

State usage guidance:

- Display meaning and limitation together.
- Preserve advisory-only language.
- Never hide uncertainty.
- Route high-risk conflict states to human-supervised validation.

## Accountability and authority boundaries

### HC:// verifies records and validators

HC:// verification checks integrity, provenance continuity, and validator traceability within declared boundaries. It does not replace human institutional judgment.

### no single reviewer or AI has unchecked final authority

No single reviewer, maintainer, validator, or automation agent should have final unchecked authority for consequential trust outcomes.

### every important action must be traceable

Material actions (review decisions, validator-run claims, state transitions, and escalation outcomes) must be attributable to a traceable audit trail.

### abuse attempts must be visible and auditable

Abuse or manipulation signals must surface as explicit state indicators and audit references rather than hidden or silently auto-resolved outcomes.

### trust signals must not hide uncertainty

Trust signals must communicate uncertainty, boundary conditions, and review requirements clearly and persistently.

## Implementation notes

- This model does not modify canonical records, schema contracts, validator logic, signing semantics, federation behavior, policy evaluator behavior, or GitHub workflow security controls.
- This model defines accountability and defense language for review routing, anti-spoof posture, and trust integrity communication.

## Related documents

- `docs/verified-ai-validator-model.md`
- `docs/authenticated-ai-validator-access.md`
- `docs/verification-result-states.md`
- `docs/public-verification-boundaries.md`
- `docs/anti-spoof-verification-signals.md`
- `docs/qr-verification-security-model.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/federated-oversight-model.md`
- `docs/public-verification-disputes.md`
- `docs/immutable-state-history-model.md`
- `docs/maintainer-accountability-model.md`
