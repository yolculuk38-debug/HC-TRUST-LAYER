# HC:// Runtime Storage Contracts and Event-Store Schema Blueprint

## Scope and posture

This document defines a documentation-only runtime storage contract and event-store schema blueprint for HC:// operational trust runtime in HC-TRUST-LAYER.

Constraints preserved in this scope:

- no canonical schema changes
- no validator changes
- no workflow changes
- no production-readiness, autonomous-finality, or forensic-certainty claims
- no blockchain or token claims

Human-supervised validation remains required for non-trivial trust-kernel-impacting interpretation.

## 1) Storage contract purpose

The runtime storage contract defines how HC:// runtime persistence should remain append-style, attributable, and reviewable across verification, trust-state movement, continuity checkpoints, federation synchronization, and recovery workflows.

Purpose outcomes:

- preserve traceable runtime chronology
- preserve provenance and audit trail continuity
- keep warning history visible instead of hidden mutation
- keep public-safe history exposure bounded and understandable
- support reconstruction from persisted history when recovery is required

## 2) Runtime event-store contract

The runtime event-store contract is the primary append-style persistence surface for operational runtime events.

Contract expectations:

- each event is written as a new entry with stable event identity
- event lineage references remain queryable for chronology inspection
- event writes preserve attributable origin and runtime phase context
- warning-bearing events remain visible through later transitions
- event storage remains advisory and reviewable under human-supervised validation

## 3) Trust-state history storage contract

The trust-state history storage contract preserves trust-state transitions as explicit historical entries.

Contract expectations:

- transitions include prior and next advisory trust-state values
- transitions include rationale and uncertainty markers
- transitions include source event references and actor boundary metadata
- transitions are append-visible and challengeable
- historical transitions are not silently replaced

## 4) Continuity checkpoint storage contract

The continuity checkpoint storage contract records replay-aware checkpoints used to evaluate lineage continuity over time.

Contract expectations:

- checkpoints include chronology anchors and checkpoint class
- checkpoints preserve prior-link references for continuity review
- checkpoint status can express normal, warning, and recovery-sensitive context
- checkpoint records remain visible during escalation and recovery
- checkpoint history supports replay/tamper warning analysis

## 5) Federation event storage contract

The federation event storage contract records federation synchronization and divergence context without claiming live federation guarantees.

Contract expectations:

- federation entries include participant attribution and synchronization scope
- divergence signals are persisted as explicit events
- unresolved federation divergence remains visible for reviewer lanes
- federation history remains auditable and attributable
- federation persistence remains advisory and human-supervised

## 6) Recovery reconstruction storage contract

The recovery reconstruction storage contract records reconstruction pathways when continuity gaps, partial state loss, or replay-risk conditions are observed.

Contract expectations:

- recovery traces include reconstruction stage and evidence references
- unresolved recovery segments remain explicit in history
- reconstruction checkpoints remain linked to source continuity events
- recovery completion does not erase prior warning history
- reconstruction remains challengeable and review-visible

## 7) Public audit/history storage contract

The public audit/history storage contract defines public-safe projection of runtime history metadata.

Contract expectations:

- public history records expose safe, bounded summary metadata only
- advisory and warning context remains clear and non-authoritative
- sensitive internal diagnostics remain excluded
- public history records keep provenance pointers and timeline context
- public exposure remains consistent with human-supervised validation posture

## 8) Replay/tamper warning storage contract

The replay/tamper warning storage contract preserves anomaly evidence as first-class runtime history.

Contract expectations:

- replay/tamper indicators are persisted as explicit warning events
- warning events include affected scope and continuity references
- downstream transitions cannot silently suppress warning visibility
- warning events remain linked to escalation and recovery traces
- warning closure preserves historical warning lineage

## Reference storage objects

The following reference objects define a shared naming baseline for runtime storage surfaces:

- `runtime_event`: base append event object for operational runtime chronology
- `trust_state_transition`: trust-state movement object with rationale and attribution
- `continuity_checkpoint`: replay-aware continuity anchor and checkpoint status object
- `federation_sync_event`: federation synchronization or divergence visibility object
- `escalation_event`: dispute/elevated-risk routing object
- `recovery_trace`: recovery reconstruction stage and lineage object
- `replay_warning`: replay/tamper warning event object
- `public_history_reference`: public-safe audit/history projection reference object

## Storage safeguards

This blueprint preserves the following storage safeguards:

- append-style event storage
- no hidden mutation
- traceable transition history
- replay-aware checkpoints
- public-safe audit exposure
- recovery reconstruction support
- no blockchain/token claims

Additional guardrails:

- disputed or unresolved history must not be silently relabeled as resolved
- trust-kernel-impacting interpretation remains human-supervised
- warning-bearing history remains visible through public-safe and internal audit views

## Example JSON-like payloads

### Verification event

```json
{
  "object_type": "runtime_event",
  "event_id": "evt_2026_05_27_0001",
  "event_class": "verification_event",
  "state": "EVENT_PERSISTED",
  "request_id": "req_qr_9ad2",
  "record_reference": "hc://record/sample-001",
  "provenance_ref": "prov_7ab1",
  "created_at": "2026-05-27T09:12:44Z",
  "actor_surface": "validator_runtime",
  "advisory_note": "Verification remains advisory pending human-supervised validation."
}
```

### Trust-state transition

```json
{
  "object_type": "trust_state_transition",
  "transition_id": "tst_2026_05_27_0015",
  "event_ref": "evt_2026_05_27_0001",
  "prior_state": "UNRESOLVED",
  "next_state": "ADVISORY",
  "reason": "Bounded verification checks completed with partial confidence.",
  "uncertainty_marker": "REVIEW_RECOMMENDED",
  "actor_surface": "trust_state_engine",
  "created_at": "2026-05-27T09:12:49Z"
}
```

### Continuity checkpoint

```json
{
  "object_type": "continuity_checkpoint",
  "checkpoint_id": "ccp_2026_05_27_004",
  "event_ref": "evt_2026_05_27_0001",
  "checkpoint_class": "TRUST_HISTORY_BOUNDARY",
  "continuity_status": "CONTINUITY_RECORDED",
  "prior_checkpoint_ref": "ccp_2026_05_27_003",
  "lineage_hash_ref": "lineage_hash_1f2a",
  "replay_scan_status": "NO_REPLAY_SIGNAL",
  "created_at": "2026-05-27T09:12:52Z"
}
```

### Replay warning

```json
{
  "object_type": "replay_warning",
  "warning_id": "rpl_2026_05_27_002",
  "event_ref": "evt_2026_05_27_0110",
  "warning_state": "POSSIBLE_REPLAY",
  "affected_scope": "trust_path/media-dispute-lane",
  "checkpoint_ref": "ccp_2026_05_27_009",
  "escalation_ref": "esc_2026_05_27_004",
  "review_status": "UNRESOLVED",
  "created_at": "2026-05-27T10:03:12Z"
}
```

### Federation divergence event

```json
{
  "object_type": "federation_sync_event",
  "sync_event_id": "fed_2026_05_27_007",
  "event_class": "federation_divergence",
  "local_participant": "participant_alpha",
  "peer_participant": "participant_beta",
  "divergence_marker": "TRUST_STATE_MISMATCH",
  "comparison_window": "2026-05-27T09:40:00Z/2026-05-27T10:00:00Z",
  "review_route": "FEDERATION_REVIEW_ACTIVE",
  "created_at": "2026-05-27T10:06:35Z"
}
```

### Recovery trace

```json
{
  "object_type": "recovery_trace",
  "recovery_trace_id": "rec_2026_05_27_003",
  "activation_event_ref": "evt_2026_05_27_0115",
  "reconstruction_stage": "STATE_REBUILD_IN_PROGRESS",
  "source_window": "evt_2026_05_27_0001..evt_2026_05_27_0114",
  "checkpoint_refs": [
    "ccp_2026_05_27_007",
    "ccp_2026_05_27_008",
    "ccp_2026_05_27_009"
  ],
  "unresolved_segments": [
    "trust_path/media-dispute-lane"
  ],
  "review_status": "RECOVERY_REVIEW_REQUIRED",
  "created_at": "2026-05-27T10:09:58Z"
}
```

## Alignment with related core architecture docs

This blueprint is aligned with:

- `docs/core/runtime-state-persistence-and-event-store.md`
- `docs/core/reference-event-driven-runtime-architecture.md`
- `docs/core/runtime-api-contract-architecture.md`
- `docs/core/trust-state-persistence-and-audit-runtime.md`
- `docs/core/reference-operational-data-flow.md`

## Boundary reminder

This document is architecture guidance only and does not modify canonical records, schema contracts, validator logic, federation logic, policy evaluator behavior, signing semantics, or workflow enforcement.
