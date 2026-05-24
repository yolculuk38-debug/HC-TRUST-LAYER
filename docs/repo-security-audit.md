# HC-TRUST-LAYER Repository Security Audit Checklist

## Purpose

This security audit checklist captures the current repository-level security and governance posture for HC-TRUST-LAYER after policy evaluator and advisory policy workflow stabilization.

The checklist is documentation-only and supports human-supervised validation decisions in the trust kernel and broader verification infrastructure.

## Status Legend

- **Status**: `OK` | `Needs review` | `Planned` | `Blocked`
- **Risk**: `low` | `medium` | `high` | `critical`

## Audit Checklist

| Area | Status | Risk | Evidence / Notes |
|---|---|---|---|
| GitHub Actions permissions | Needs review | medium | Repository has multiple CI workflows; permission minimization and explicit `permissions:` scoping should be re-validated across all workflows as a periodic control. |
| workflow triggers | OK | low | Advisory policy workflow and docs guard workflows are scoped to expected events and paths, aligned to conservative change detection. |
| CodeQL coverage | Needs review | medium | CodeQL references exist in governance documents, but periodic confirmation of language coverage, query pack selection, and branch coverage is still recommended. |
| dependency usage | Needs review | medium | Dependency surfaces exist across Python tooling and CI execution paths; scheduled dependency review and pinning posture review should continue. |
| policy evaluator behavior | OK | low | Advisory `policy evaluator` behavior is deterministic and documented with conservative escalation semantics for unknown/failure routes. |
| advisory policy workflow | OK | low | Advisory-only workflow remains bounded and supports human-supervised validation without runtime merge enforcement. |
| auto-merge safety | Needs review | medium | Trusted auto-merge governance model is documented; operational safety depends on consistent guard check enforcement and unresolved-thread gating. |
| canonical record boundaries | OK | low | Canonical record boundary expectations are explicitly documented and reflected in schema/guard references. |
| generated artifact handling | Needs review | high | Generated artifact handling remains a high-sensitivity area; blocked-path discipline must remain strict and periodically validated. |
| schema safety | OK | low | Schema change sensitivity is documented, and schema-modification paths are treated as trust-critical for review routing. |
| validator behavior | OK | low | Validator behavior remains treated as trust-critical; current governance documentation routes validator-impacting changes to manual review. |
| verification package exporter skeleton | Planned | medium | Exporter skeleton paths exist but require additional hardening definition before stronger security claims. |
| public verification API documentation | Needs review | medium | Public verification API documentation exists; security posture sections (authn/authz assumptions, abuse boundaries, response integrity caveats) should be periodically reviewed. |
| federation/signing roadmap risks | Planned | high | Federation and signing roadmap items remain planned/partial; key-distribution, revocation propagation, and cross-node trust semantics remain open risk items. |

## Recommended Next Hardening Actions

1. Add a recurring workflow-permissions review checklist that verifies least-privilege `permissions:` blocks and documents exception rationale.
2. Add a periodic CodeQL coverage review note covering languages scanned, default branch behavior, and severity triage ownership.
3. Publish dependency governance notes for update cadence, pinning strategy, and review ownership for CI/runtime tooling.
4. Add an explicit generated-artifact handling runbook that maps blocked paths, reviewer expectations, and canonical record boundary rationale.
5. Add a focused security appendix to public verification API docs documenting HC:// request/response trust boundaries and non-goals.
6. Define a federation/signing preflight checklist covering key lifecycle, signing scope, revocation flow, and incident rollback expectations.
7. Add a periodic audit review cadence (for example, monthly or release-based) with accountable owners for each checklist area.

## Scope and Non-Goals

- This document is a repository security audit checklist and status snapshot.
- It does not change workflows, validators, schemas, or branch protection.
- It does not claim production-ready security guarantees.
- It does not change canonical record handling semantics.

## Terminology Alignment

This checklist aligns with HC-TRUST-LAYER language and governance boundaries:

- trust kernel
- policy evaluator
- canonical record
- verification infrastructure
- human-supervised validation
- HC://
