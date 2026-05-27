# HC:// Runtime State Persistence and Event-Store Architecture

This document defines the runtime state persistence and event-store architecture for HC:// operational trust runtime in HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only architecture definition.
- Human-supervised validation remains required for non-trivial trust-kernel-impacting changes.
- No schema changes.
- No validator changes.
- No workflow changes.
- No production-readiness, autonomous-finality, or forensic-certainty claims.

## Event-store purpose

The runtime event store is the append-style persistence surface that records runtime events needed for continuity, reviewability, and recovery reconstruction in HC://. It provides a canonical operational chronology for trust-state movement, escalation pathways, federation-facing runtime context, and observability signals.

## Runtime state persistence lifecycle

1. **Runtime event emitted**
   - Runtime emits a structured event describing a state change, escalation, federation signal, or observability condition.
2. **Event persisted**
   - Event is stored in the runtime event store and enters `EVENT_PERSISTED`.
3. **Continuity chain recorded**
   - Continuity-link metadata is recorded to preserve lineage traceability and enters `CONTINUITY_RECORDED`.
4. **Trust history updated**
   - Trust-state history receives the event-linked transition and enters `TRUST_HISTORY_UPDATED`.
5. **Federation event captured when applicable**
   - Federation-relevant runtime activity is recorded and enters `FEDERATION_EVENT_RECORDED`.
6. **Public-safe history projection published when allowed**
   - Public audit/history layer exposes approved history metadata and enters `PUBLIC_HISTORY_AVAILABLE`.
7. **Replay or tamper warning recorded when detected**
   - Replay/timeline anomalies are persisted as visible warning events and enter `REPLAY_WARNING_RECORDED`.
8. **Recovery reconstruction activated when needed**
   - Recovery reconstruction layer begins auditable reconstruction workflow and enters `RECOVERY_RECONSTRUCTION_ACTIVE`.

## Continuity-chain persistence

Continuity persistence stores event-link references that make the runtime chronology traceable across state transitions, dispute paths, and recovery boundaries. Continuity-chain persistence must preserve ordering context, attributable origin, and challengeable lineage visibility.

## Trust-state history persistence

Trust-state history persistence records each trust-state transition as an append-style historical update instead of hidden replacement. Each persisted transition should preserve prior/next context, event attribution, rationale surface, and reviewer-visible uncertainty markers.

## Escalation history persistence

Escalation history persistence records elevated-risk routing and dispute-triggered review paths as attributable runtime events. Escalation entries should preserve who initiated escalation, why escalation was triggered, and which review boundary accepted ownership.

## Federation event persistence

Federation event history persistence records federation-relevant synchronization, divergence markers, and cross-boundary comparison events without claiming live federation guarantees. Federation persistence must keep divergence evidence visible for human-supervised validation.

## Observability event persistence

Observability persistence stores runtime telemetry events that support diagnosability, review routing, and audit trail interpretation. Observability events should preserve warning chronology, signal provenance, and confidence/uncertainty context where applicable.

## Recovery reconstruction flow

1. Detect continuity gap, replay indicator, or partial state-loss condition.
2. Persist a recovery initiation event and enter `RECOVERY_RECONSTRUCTION_ACTIVE`.
3. Reconstruct state from append-style persisted event history and continuity links.
4. Record reconstruction checkpoints, unresolved segments, and reviewer notes.
5. Publish reconstruction outcome as auditable history events without erasing prior warnings.

Recovery reconstruction remains advisory and reviewer-supervised; it does not imply autonomous finality.

## Replay-aware persistence behavior

Replay-aware persistence behavior ensures replay/tamper indicators remain explicit, queryable, and historically visible. When chronology anomalies are detected, runtime should persist warning entries, preserve original ordering evidence, and avoid silent normalization that conceals anomaly context.

## Persistence participants

- **runtime event store:** Primary append-style event persistence surface.
- **continuity persistence layer:** Maintains continuity-link lineage and ordering traceability.
- **trust-state history layer:** Persists trust-state transition history with attribution context.
- **federation event history:** Persists federation-relevant runtime and divergence history.
- **observability persistence layer:** Persists telemetry, warnings, and diagnostic signals.
- **recovery reconstruction layer:** Executes and records auditable reconstruction workflows.
- **public audit/history layer:** Exposes public-safe history summaries and warning visibility.

## Persistence states

- `EVENT_PERSISTED`
- `CONTINUITY_RECORDED`
- `TRUST_HISTORY_UPDATED`
- `FEDERATION_EVENT_RECORDED`
- `RECOVERY_RECONSTRUCTION_ACTIVE`
- `REPLAY_WARNING_RECORDED`
- `PUBLIC_HISTORY_AVAILABLE`

State usage reminders:

- States are operational trace labels, not autonomous adjudication outcomes.
- State transitions must remain attributable and reviewable.
- Warning-oriented states should remain visible in downstream audit/history views.

## Safeguards

- **no hidden history mutation:** Runtime must not conceal history replacement behavior.
- **append-style persistence behavior:** Runtime should append events instead of silently rewriting chronology.
- **continuity chain remains traceable:** Lineage references must remain review-visible.
- **replay/tamper indicators remain visible:** Warning signals must persist through later transitions.
- **public-safe audit visibility preserved:** Public history should expose safe audit context and caution signals.
- **recovery reconstruction remains auditable:** Reconstruction actions and outcomes must remain attributable.

## Operational examples

### QR verification persistence chain

A QR verification request emits a verification event, persists to the runtime event store (`EVENT_PERSISTED`), records continuity linkage (`CONTINUITY_RECORDED`), updates trust-state history (`TRUST_HISTORY_UPDATED`), and exposes public-safe verification history (`PUBLIC_HISTORY_AVAILABLE`) when disclosure policy permits.

### Disputed media event history

A disputed media signal triggers escalation history persistence with dispute reason, source context, and review assignment. The escalation sequence remains append-visible so reviewers can inspect pre-dispute and post-dispute trust-state context without hidden history mutation.

### Federation divergence event recording

A divergence signal between local and federation-facing runtime context is persisted in federation event history (`FEDERATION_EVENT_RECORDED`) with comparison metadata and caution visibility, supporting human-supervised validation before any downstream trust interpretation.

### Replay-warning persistence

A chronology anomaly is detected during event ingestion, and runtime records a replay warning event (`REPLAY_WARNING_RECORDED`) while preserving original ordering evidence and continuity references for audit trail review.

### Recovery reconstruction scenario

After partial runtime state-loss, recovery reconstruction activates (`RECOVERY_RECONSTRUCTION_ACTIVE`), rebuilds trust-state context from persisted events and continuity links, records reconstruction checkpoints, and preserves both unresolved gaps and final reviewer-approved reconstruction notes.

## Alignment with related core architecture docs

This document is aligned with:

- `docs/core/reference-event-driven-runtime-architecture.md`
- `docs/core/trust-state-persistence-and-audit-runtime.md`
- `docs/core/distributed-trust-propagation.md`
- `docs/core/runtime-failover-and-recovery.md`
- `docs/core/runtime-observability-and-telemetry-model.md`
- `docs/core/operational-trust-fabric-coordination.md`

## Boundary reminder

This architecture guidance is documentation-only for HC-TRUST-LAYER and does not alter canonical records, schemas, validators, signing logic, federation logic, policy evaluators, or workflow enforcement.
