# HC Control Center v0.1

Single-entry operator orientation for HC-TRUST-LAYER. Use this page to understand the current HC:// repository status in under one minute before opening a contributor, reviewer, Codex, Copilot, ChatGPT, or future HC Guide Bot session.

## Purpose

Provide a concise advisory starting point for repository orientation, safe task scoping, and evidence collection. This page points operators to authoritative repository evidence; it does not replace that evidence.

## Authority Boundary

- Repository evidence remains authoritative.
- HC Control Center is not approval authority.
- HC Control Center is not merge authority.
- HC Control Center is not governance enforcement.
- HC Control Center is not security validation.
- Human-supervised validation and repository-defined checks remain required for non-trivial trust-kernel-impacting work.

## Current Phase

Repository cleanup phase 1 mapping is completed. Phase 2 cleanup must stay small, reversible, evidence-backed, and human-reviewed. HC-TRUST-LAYER remains advisory-only, early-stage trust infrastructure.

## Active Focus

- Use `docs/project-control/project-state.md` for current phase and focus.
- Use `docs/project-control/next-actions.md` for the active safe next-work queue.
- Use `docs/project-control/repository-index-chain-2026-06-16.md` before proposing repository structure work.
- Use `docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md` to confirm phase 1 completion and phase 2 limits.
- Keep protected-path, workflow, runtime, schema, validator, record, policy, federation, signing, canonical, QR/hash, and authority-changing work parked unless explicitly authorized and validated.

## Next Safe Action

Read `docs/project-control/next-actions.md`, `docs/project-control/repository-index-chain-2026-06-16.md`, and `docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md`. Start only with small documentation-first, evidence-backed, human-reviewed follow-up unless an authorized reviewer explicitly changes the mode.

## Protected Path Reminder

Do not modify runtime code, schemas, validators, records, policy, federation, signing, trust-kernel indexes, workflows, or other protected paths unless explicitly requested and validated through the repository review process.

## Do-Not-Repeat Reminder

Treat completed phase 1 cleanup mapping, inventory passes, project-state sync, operator-entry-map sync, task-ledger sync, shift-checklist sync, and active-work-registry sync as completed references. Cross-check `docs/project-control/task-ledger.md` and GitHub PR history before related work.

## Evidence Bundle Minimum

Before claiming a task is complete, collect and report at least:

- changed files;
- commit hash or PR number when available;
- checks run and their outcomes;
- relevant repository evidence or review notes;
- any stale-context or advisory-source mismatch.

## Read Order

1. `AGENTS.md`
2. `HC_BOOTSTRAP.md`
3. `docs/project-control/project-state.md`
4. `docs/project-control/agent-operating-model.md`
5. `docs/project-control/task-ledger.md`
6. `docs/project-control/next-actions.md`
7. `docs/project-control/repository-index-chain-2026-06-16.md`
8. `docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md`
9. `docs/project-control/active-work-registry.md`
10. `docs/project-control/shift-change-checklist.md`
11. `hc_context` files only after markdown project-control docs, and only as advisory agent context.

## Relationship Map

- `AGENTS.md`: repository-wide contributor and agent rules, terminology baseline, safe task boundaries, and protected-path expectations.
- `HC_BOOTSTRAP.md`: first operational bootstrap checklist for repository-native handoff and evidence expectations.
- `docs/project-control/project-state.md`: current phase, active focus, parked work, protected-path reminder, and source-of-truth priority.
- `docs/project-control/task-ledger.md`: task history, completed or closed PR references, task barcodes, and do-not-repeat notes.
- `docs/project-control/next-actions.md`: priority-ordered safe next work; current entries remain advisory unless explicitly authorized otherwise.
- `docs/project-control/repository-index-chain-2026-06-16.md`: cleanup purpose-index and inventory-pass navigation chain.
- `docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md`: cleanup phase 1 completion checkpoint and phase 2 limits.
- `docs/project-control/active-work-registry.md`: advisory shift-level coordination snapshot; it does not replace Project State, Task Ledger, or Next Actions.
- `hc_context`: advisory machine-readable agent context that may lag behind markdown docs, merged files, checks, PR records, or human review decisions.
- HC Guide Bot: future advisory orientation assistant that should summarize repository evidence, surface gaps, and avoid approval, merge, governance-enforcement, security-validation, or truth-finality claims.

## Non-Goals

- No runtime behavior changes.
- No schema, validator, record, policy, federation, signing, workflow, or trust-kernel index changes.
- No production-readiness, truth guarantee, forensic certainty, autonomous governance, or security-validation claims.
- No replacement for repository evidence, checks, reviewer oversight, or human-supervised validation.
