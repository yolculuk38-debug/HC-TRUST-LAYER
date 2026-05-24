# HC-TRUST-LAYER Agent Governance

## Status

- documentation-only governance foundation
- no runtime agent implementation in this phase
- no autonomous governance behavior
- no AI-origin final authority over HC:// trust decisions

## Purpose

This document defines the agent governance baseline for HC-TRUST-LAYER verification infrastructure.

The goal is to support AI-assisted verification, development, validation, and federation workflows while preserving human-supervised authority at every trust-sensitive boundary.

## Agent Identity Model

All agent activity in HC-TRUST-LAYER should be mapped to an explicit, auditable identity model:

- `agent_type`: assistant, implementation, validator, reviewer, federation, monitoring
- `agent_instance_id`: unique run/session identifier
- `execution_origin`: workflow, local tooling, or supervised operator session
- `policy_context_version`: policy bundle or rule snapshot identifier
- `human_owner`: accountable human operator or approver for the action scope

Identity metadata is part of operational provenance and must be retained for execution audit trail continuity.

## Agent Types and Roles

### 1) Assistant agent

- supports documentation, triage, and workflow preparation
- may draft suggestions, summaries, and proposed actions
- does not perform authoritative trust decisions

### 2) Implementation agent

- supports controlled code or docs modifications under defined scope
- must remain constrained by branch, policy, and permission boundaries
- requires approval checkpoint compliance before trust-sensitive changes proceed

### 3) Validator agent

- executes defined validation routines and reports outcomes
- may provide AI-assisted analysis of validation outputs
- does not replace human-supervised validation for critical outcomes

### 4) Reviewer agent

- supports structured review for policy, consistency, and risk signals
- produces advisory findings linked to evidence
- does not provide final merge authority

### 5) Federation agent

- supports federation-oriented checks, sync diagnostics, and metadata analysis
- must operate within explicit federation semantics and policy scope
- cannot unilaterally elevate trust state across HC:// federation surfaces

### 6) Monitoring agent

- supports telemetry interpretation, anomaly surfacing, and status reporting
- contributes to operational provenance and audit visibility
- must route trust-sensitive alerts to human-supervised validation

## Execution Scope

Agent execution scope must be explicit before action:

- allowed repositories/paths
- allowed command classes
- allowed artifact mutation boundaries
- allowed policy evaluation pathways
- explicit trust kernel protection boundaries

Any action outside declared scope is treated as policy deviation and must trigger escalation.

## Approval Checkpoints

Agent operations must route through approval checkpoint controls for trust-sensitive domains.

Minimum checkpoint expectations:

- pre-execution scope confirmation
- in-flight policy gate checks
- post-execution human review where required
- merge/deploy final human authorization

See: `docs/approval-checkpoints.md`.

## Human-Supervised Validation

HC-TRUST-LAYER requires human-supervised validation for trust-sensitive outcomes.

This includes:

- interpreting ambiguous validation signals
- approving policy exceptions
- accepting or rejecting trust-impacting changes
- validating rollback decisions for safety-critical failures

AI assistance can accelerate analysis, but humans remain final authority.

## AI-Assisted but Non-Authoritative Behavior

Agent behavior in HC-TRUST-LAYER must remain AI-assisted and non-authoritative:

- no autonomous governance claims
- no AI-origin final trust verdicts
- no unsupervised merge or deploy authority
- no objective-truth determination claims

HC:// verification outputs remain bounded to integrity, provenance, and policy-scoped evaluation semantics.

## Rollback Expectations

Every trust-relevant agent workflow should include rollback expectations:

- rollback trigger conditions
- rollback authority chain
- rollback evidence capture
- rollback verification after restore

Rollback readiness is required to preserve trust kernel stability during failure or policy drift events.

## Permission Boundaries

Permission boundaries should be explicitly encoded and auditable:

- least-privilege access per agent type
- write restrictions by path and operation class
- signing/key boundaries isolated from generic agent execution
- production deployment rights separated from routine automation

Boundary violations must be recorded and escalated.

## Audit Requirements

Agent governance in HC-TRUST-LAYER requires a durable execution audit trail with:

- operational provenance for each agent action
- policy evaluation records and outcomes
- human approval traceability
- failure/retry history
- rollback trail continuity

See: `docs/execution-audit-trail.md`.

## Verification Infrastructure Alignment

This foundation aligns agent governance with HC-TRUST-LAYER verification infrastructure principles:

- trust kernel protection first
- transparent auditability
- policy-constrained execution
- human-supervised validation
- conservative trust escalation

These constraints prepare HC:// workflows for controlled AI assistance without transferring authority from accountable human governance.
