# HC:// Validator Health-State and Federation Heartbeat Model

This document defines an architecture model for validator health-state tracking and federation heartbeat propagation in HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only architecture guidance.
- Advisory-only verification posture is preserved.
- Human-supervised validation remains required.
- No canonical schema, validator, signing, federation, or policy behavior changes.
- No blockchain, token, financial, or production-readiness claims.

## Purpose

Define a consistent, auditable health-state model for validator participants so HC:// orchestration can route recovery, escalation, and human-supervised validation decisions with clear provenance.

## Validator health states

Validator health state is an operational coordination signal and not an authority claim.

- **active:** validator is responsive, heartbeat is current, and routine orchestration participation is available.
- **degraded:** validator is responsive but exhibiting delay, partial capability loss, or repeated transient errors.
- **isolated:** validator is not receiving or propagating expected federation heartbeat updates for the configured detection window.
- **recovery:** validator has rejoined heartbeat flow and is undergoing staged revalidation before full participation.
- **suspended:** validator participation is intentionally paused through supervised operational routing pending investigation or remediation.

## Federation heartbeat propagation flow

1. **heartbeat emit:** each validator emits periodic signed runtime heartbeat metadata to federation peers through existing runtime communication channels.
2. **peer receipt tracking:** receiving validators record receipt time, source validator identity, and last-known state in local operational memory.
3. **state fan-out:** validators propagate local health-state transitions to peers with attributable reason markers.
4. **audit linkage:** heartbeat and health-state transition events are linked into provenance and audit trail continuity artifacts.
5. **supervised escalation trigger:** unresolved divergence, stale peer state, or repeated state flapping routes to human-supervised validation workflows.

## Timeout and stale-validator detection logic

Detection logic is model guidance for orchestration planning and must be finalized through human-supervised validation before runtime adoption.

- **heartbeat interval (T):** expected baseline interval for peer heartbeat updates.
- **warning threshold (2T):** if no heartbeat is observed for two intervals, peer state transitions from `active` to `degraded`.
- **stale threshold (3T):** if no heartbeat is observed for three intervals, peer state transitions from `degraded` to `isolated`.
- **suspension candidate window (N cycles):** repeated isolated cycles or unresolved stale state can be routed as a `suspended` candidate for human review.
- **anti-flap damping:** frequent state toggling should be damped with minimum-state-duration windows before outward propagation.

## Recovery routing behavior

When an `isolated` or `suspended` validator reappears:

1. mark validator as `recovery` and limit orchestration role to supervised verification subsets.
2. require consecutive heartbeat stability windows before re-entering `active` participation.
3. route recent verification outputs for focused audit trail inspection.
4. preserve prior degraded/isolated chronology; do not overwrite historical health-state transitions.
5. escalate to human-supervised validation if recovery signals conflict with peer observations.

## Quorum-awareness notes (future distributed consensus alignment)

For future distributed-validator consensus coordination:

- track health-state distribution across validator sets as advisory quorum-awareness context.
- avoid treating heartbeat majority as autonomous finality; final interpretation remains human-supervised.
- require visibility of minority-isolated validators to preserve dispute-awareness and audit continuity.
- preserve compatibility with `docs/core/distributed-validator-consensus-coordination.md` without introducing new consensus guarantees.

## Operational alignment notes

- Health-state signals support HC:// runtime orchestration and do not replace verification outcomes.
- Federation heartbeat visibility should strengthen provenance continuity and review routing clarity.
- Any trust-kernel-impacting implementation change derived from this model requires explicit reviewer escalation and human-supervised validation.

## Related references

- `docs/core/runtime-communication-and-sync-model.md`
- `docs/core/validator-orchestration-architecture.md`
- `docs/core/distributed-validator-consensus-coordination.md`
- `docs/core/runtime-observability-and-telemetry-model.md`
- `docs/trust-review-workflow.md`
