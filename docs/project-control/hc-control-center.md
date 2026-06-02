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

Phase 2 — Trust Kernel Enforcement. HC-TRUST-LAYER remains advisory-only, early-stage trust infrastructure.

## Active Focus

- PR risk labeler Tier-1 review.
- Safe auto-merge Tier-1 review.
- HC Guide Bot design.
- GitHub Project Board and label taxonomy.
- `hc_context` machine-readable state proposal.

## Next Safe Action

Read `docs/project-control/next-actions.md` and start with the first REPORT ONLY item unless an authorized reviewer explicitly changes the mode.

## Protected Path Reminder

Do not modify runtime code, schemas, validators, records, policy, federation, signing, trust-kernel indexes, workflows, or other protected paths unless explicitly requested and validated through the repository review process.

## Do-Not-Repeat Reminder

Treat #545, #546, #547, #548, #550, and #551 as completed references. Do not reuse #549 because it is closed and conflicted. Cross-check `docs/project-control/task-ledger.md` before related work.

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
7. `docs/project-control/shift-change-checklist.md`
8. `hc_context` files only after markdown project-control docs, and only as advisory agent context.

## Relationship Map

- `AGENTS.md`: repository-wide contributor and agent rules, terminology baseline, safe task boundaries, and protected-path expectations.
- `HC_BOOTSTRAP.md`: first operational bootstrap checklist for repository-native handoff and evidence expectations.
- `docs/project-control/project-state.md`: current phase, active focus, parked work, protected-path reminder, and source-of-truth priority.
- `docs/project-control/task-ledger.md`: task history, completed or closed PR references, task barcodes, and do-not-repeat notes.
- `docs/project-control/next-actions.md`: priority-ordered safe next work; current entries remain REPORT ONLY unless explicitly authorized otherwise.
- `hc_context`: advisory machine-readable agent context that may lag behind markdown docs, merged files, checks, PR records, or human review decisions.
- HC Guide Bot: future advisory orientation assistant that should summarize repository evidence, surface gaps, and avoid approval, merge, governance-enforcement, security-validation, or truth-finality claims.

## Non-Goals

- No runtime behavior changes.
- No schema, validator, record, policy, federation, signing, workflow, or trust-kernel index changes.
- No production-readiness, truth guarantee, forensic certainty, autonomous governance, or security-validation claims.
- No replacement for repository evidence, checks, reviewer oversight, or human-supervised validation.
