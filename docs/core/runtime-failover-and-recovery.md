# Runtime Failover and Recovery Orchestration Model

## Scope and Intent

This document defines an advisory-only HC:// runtime failover and recovery orchestration model for HC-TRUST-LAYER.

It describes how runtime orchestration should preserve auditability, transparency, and human-supervised validation during partial outages and recovery operations.

This document does not modify schemas, validators, federation logic, policy behavior, signing logic, or workflow behavior.

## Failure State Baseline

Runtime orchestration uses the following failure states for operator-facing and audit-visible handling:

- **NODE_UNAVAILABLE**
- **DEGRADED_RUNTIME**
- **FEDERATION_FALLBACK_ACTIVE**
- **RECOVERY_ROUTING_ACTIVE**
- **QUEUE_REDISTRIBUTION_ACTIVE**
- **PUBLIC_WARNING_REQUIRED**

State transitions should be timestamped, reason-linked, and attached to a canonical audit trail entry for review continuity.

## 1) Validator Outage Handling

When validator runtime dependencies become unavailable:

1. Set state to **NODE_UNAVAILABLE**.
2. Preserve incoming request provenance and correlation identifiers.
3. Pause non-essential verification execution on the affected node.
4. Route unresolved or high-risk requests to human-supervised validation queues.
5. Emit an audit-visible outage event with impacted surface and detection time.

Outage handling remains advisory-only and must not imply autonomous finality or hidden override behavior.

## 2) Degraded Node Routing

When runtime health remains available but materially impaired:

1. Set state to **DEGRADED_RUNTIME**.
2. Activate **RECOVERY_ROUTING_ACTIVE** for constrained routing.
3. Prioritize low-risk and already-partially-evaluated requests for continuity.
4. Delay or escalate high-ambiguity requests to protect verification clarity.
5. Preserve deterministic routing reason codes for audit trail continuity.

Routing decisions should remain explainable to operators and reviewable by human supervisors.

## 3) Federation Fallback Behavior

If local runtime capacity cannot maintain expected advisory response continuity:

1. Set state to **FEDERATION_FALLBACK_ACTIVE**.
2. Route eligible advisory review paths through federation fallback coordination.
3. Preserve request provenance continuity across fallback boundaries.
4. Mark fallback-assisted outputs as advisory and review-dependent.
5. Keep dispute and escalation visibility intact for public-safe interpretation.

Fallback behavior must not claim live federation guarantees beyond repository-defined evidence.

## 4) Queue Redistribution

When queue pressure or node failure requires workload rebalancing:

1. Set state to **QUEUE_REDISTRIBUTION_ACTIVE**.
2. Reassign pending work using deterministic priority and fairness rules.
3. Preserve ordering metadata, queue provenance, and handoff timestamps.
4. Prevent silent drops by producing queue transfer audit events.
5. Route time-sensitive unresolved items to escalation-aware review queues.

Queue redistribution should be bounded, reversible, and explicitly auditable.

## 5) Recovery Escalation Path

Recovery escalation defines how unresolved risk is routed during failover:

1. Detect unresolved outage impact on active verification requests.
2. Trigger **RECOVERY_ROUTING_ACTIVE** when normal routing is insufficient.
3. Escalate high-risk, disputed, or continuity-warning outcomes to human-supervised validation.
4. Track reviewer handoff state, escalation reason, and expected follow-up checkpoints.
5. Close escalation state only after review-visible recovery confirmation.

Escalation remains required for non-trivial trust-kernel-impacting uncertainty.

## 6) Continuity Checkpoint Restoration

Recovery orchestration should restore processing from continuity checkpoints:

1. Locate latest valid checkpoint references for affected requests.
2. Verify checkpoint provenance integrity before resume.
3. Resume from checkpoint-aligned stage boundaries rather than reprocessing blindly.
4. Record restoration source, resume timestamp, and result divergence notes.
5. Preserve unresolved markers when restoration confidence is incomplete.

Checkpoint restoration should favor transparent continuity over speed-only optimization.

## 7) Public Warning Behavior During Partial Outage

When partial outage conditions may affect public interpretation:

1. Set state to **PUBLIC_WARNING_REQUIRED**.
2. Expose concise public-safe warning text describing degraded advisory reliability.
3. Show whether failover, fallback, or queue redistribution is active.
4. Preserve dispute path visibility and expected recovery update cadence.
5. Remove warning only after auditable recovery state confirmation.

Public warning behavior must be transparent, non-alarmist, and challengeable.

## 8) Audit-Visible Recovery Events

All failover and recovery steps should create audit-visible events including:

- failure state entered and exited
- state transition reason codes
- impacted runtime surfaces
- queue redistribution actions
- checkpoint restoration actions
- escalation routing decisions
- public warning activation and deactivation markers

Audit events should preserve provenance continuity and support post-incident review without implying unsupported certainty.

## Operational Principles

This runtime failover and recovery model follows these principles:

- **advisory-only behavior:** failover outputs remain advisory and review-dependent.
- **human-supervised validation:** unresolved or high-risk outcomes require explicit human oversight.
- **auditability by default:** every material recovery decision is traceable and review-visible.
- **transparent partial outage posture:** public-safe warning visibility is maintained when needed.
- **bounded orchestration:** recovery routing and queue redistribution remain deterministic and reversible.

## Verification and Governance Boundary Note

This document is documentation-only guidance for HC:// runtime orchestration.

It does not introduce production guarantees or modify canonical records, schemas, validators, federation logic, policy logic, signing behavior, or workflow automation.
