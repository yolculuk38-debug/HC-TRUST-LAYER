# HC-TRUST-LAYER Approval Checkpoints

## Status

- documentation-only control baseline
- no runtime workflow enforcement changes in this phase

## Purpose

This document defines required approval checkpoint controls for trust-sensitive HC-TRUST-LAYER operations.

Approval checkpoints preserve human-supervised validation and prevent unsupervised trust-impacting changes across HC:// verification infrastructure.

## Approval Authority Baseline

For all checkpoint categories below:

- AI systems may assist analysis but cannot provide final authority.
- Final approval must be recorded by accountable human reviewers.
- Policy outcomes requiring escalation must remain blocked until human disposition.

## Required Human Approval Checkpoints

### 1) Schema changes

Human approval required for any change to canonical schema boundaries, schema semantics, or validation-critical schema definitions.

### 2) Validator logic

Human approval required for changes affecting verification logic, validation outcomes, or trust-sensitive validator routing.

### 3) Signing/key management

Human approval required for key lifecycle changes, signing behavior changes, revocation semantics, or trust anchor updates.

### 4) Federation semantics

Human approval required for federation trust rules, sync semantics, conflict resolution behavior, or cross-node trust interpretation.

### 5) Trust scoring

Human approval required for trust scoring model updates, score weighting changes, threshold modifications, or explanation-surface semantics.

### 6) Security workflows

Human approval required for security policy changes, access-control modifications, incident-response workflow updates, and workflow-permission hardening updates.

### 7) Public verification behavior

Human approval required for public verification output semantics, status model behavior, policy-to-user exposure, and trust explanation changes.

### 8) Production deployment

Human approval required before production deployment, including confirmation of policy checks, verification status, and rollback readiness.

## Checkpoint Flow Expectations

Each checkpoint should include:

1. scope declaration
2. policy evaluation evidence
3. AI-assisted analysis (optional)
4. human-supervised validation decision
5. auditable decision record in execution audit trail

## Escalation Rules

If any checkpoint condition is ambiguous, conflicting, or high-risk:

- route to explicit human escalation
- block automatic progression for affected scope
- document rationale and decision path in audit artifacts

## Relationship to Governance and Audit Documents

- Agent governance baseline: `docs/agent-governance.md`
- Execution audit requirements: `docs/execution-audit-trail.md`
- Policy engine architecture context: `docs/policy-engine-architecture.md`

## Trust Kernel Alignment

Approval checkpoints protect the HC-TRUST-LAYER trust kernel by ensuring:

- authority remains human-accountable
- verification infrastructure changes remain auditable
- trust-sensitive transitions remain conservative
- rollback decisions remain explicit and traceable
