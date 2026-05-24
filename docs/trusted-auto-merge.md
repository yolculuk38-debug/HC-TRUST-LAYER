# HC-TRUST-LAYER Trusted Auto-Merge Governance Model

## Status

- governance/documentation only
- no policy engine implementation in this phase
- no branch protection changes in this phase
- no autonomous merge systems in this phase

## Purpose

This document defines a trusted auto-merge governance model for HC-TRUST-LAYER.

The goal is controlled automation for low-risk pull requests while preserving trust kernel integrity, protocol semantics, canonical record boundaries, and human-supervised validation.

This model supports verification infrastructure maturity through explicit policy enforcement and clear governance boundaries.

## Governance Scope

Trusted auto-merge applies only to bounded repository change classes and only when required protections pass.

Humans remain final authority for merge decisions, policy interpretation, and trust-sensitive adjudication.

## Merge Trust Levels

### Level 1 — Safe Automatic Merge

Low-risk changes that do not alter protocol semantics, trust kernel behavior, canonical record handling, or verification logic.

Examples:
- docs wording fixes
- typo fixes
- markdown cleanup
- comments
- non-semantic documentation updates

### Level 2 — Conditional Merge

Moderate-risk changes that may affect governance, workflow behavior, or validation operations but do not directly alter trust kernel semantics.

Examples:
- CI workflow updates
- terminology guard updates
- docs drift logic
- package validation scripts
- exporter skeleton updates

### Level 3 — Manual Human Review Required

High-risk or trust-critical changes that require explicit human adjudication before merge.

Examples:
- canonical record schema changes
- validator logic
- signature systems
- federation semantics
- verification state changes
- trust scoring semantics
- security-sensitive workflows

## Required Auto-Merge Conditions

Trusted auto-merge is allowed only when all applicable checks are satisfied:

- all Actions green
- terminology guard pass
- docs drift pass
- canonical artifact guard pass
- CodeQL pass (if applicable)
- no unresolved review threads

If any required condition fails, trusted auto-merge must not proceed.

## Merge Blockers

The following changes and outcomes block trusted auto-merge:

- schema modifications
- validator modifications
- security workflow changes
- canonical boundary violations
- forbidden terminology
- unresolved high-risk review comments

Blockers should route the PR to manual human review and explicit governance decision.

## Human Oversight Principles

- humans remain final authority
- AI-assisted review is advisory
- no autonomous governance
- no automatic trust escalation

These principles prevent improper AI decision-role inflation and preserve human-governed trust decisions.

## Future Governance Concepts (Planned)

Planned extensions for policy maturity:

- risk scoring
- policy engine
- federation-aware merge policies
- multi-review consensus
- signed releases
- protected trust kernel workflows

These are roadmap concepts only and are not implemented in this phase.

## Example Classification Scenarios

### Example A: Safe Docs PR (Level 1)

Change set:
- grammar cleanup in docs
- typo fixes
- markdown formatting normalization

Result:
- eligible for trusted auto-merge if all required checks pass and no review threads remain unresolved.

### Example B: Conditional Workflow PR (Level 2)

Change set:
- update docs drift workflow behavior
- adjust terminology guard allowlist/rules

Result:
- conditional merge path; requires full green checks and no unresolved threads.
- may still be escalated to manual review when policy enforcement risk is non-trivial.

### Example C: Blocked Validator PR (Level 3)

Change set:
- edits to validator logic and verification state handling

Result:
- auto-merge blocked.
- explicit human review required due to trust kernel and canonical record risk.

## Policy Enforcement Notes

Trusted auto-merge is a governance control within HC-TRUST-LAYER verification infrastructure.

It does not assert truth guarantees, does not grant autonomous AI decision authority, and does not replace human-supervised validation.

Policy enforcement must remain transparent, auditable, and bounded by canonical record discipline.

## Related Architecture Reference

- Policy engine architecture: `docs/policy-engine-architecture.md`
