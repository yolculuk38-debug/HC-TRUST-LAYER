# Shift-Change Checklist

This checklist gives HC-TRUST-LAYER operators a compact handoff path for shift changes. It is documentation-only guidance and does not modify workflow behavior, runtime behavior, schemas, validators, records, policy, federation, signing, trust-kernel indexes, or governance enforcement.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Phase 2 — Trust Kernel Enforcement |
| Active focus | Use `docs/project-control/project-state.md` for the current focus list. |
| Next up | Use `docs/project-control/next-actions.md` and preserve REPORT ONLY mode unless explicitly changed by the Founder or an authorized reviewer. |
| Blocked / parked work | Protected-path and trust-kernel-impacting work remains parked unless explicitly authorized and routed through human-supervised validation. |
| Do-not-repeat references | Check `docs/project-control/task-ledger.md` before repeating or reviving closed, merged, superseded, or abandoned work. |
| Protected-path reminder | Treat `schema/**`, `validators/**`, `federation/**`, `signatures/**`, `canonical/**`, `policy/**`, `.github/workflows/**`, `records/**`, and trust-kernel indexes as protected. |
| Source-of-truth priority | Markdown project-control docs, repository evidence, checks, PR records, and human review decisions outrank `hc_context` and chat memory. |

## Read order

Read these files before proposing or continuing work:

1. `AGENTS.md`
2. `HC_BOOTSTRAP.md`
3. `docs/project-control/project-state.md`
4. `docs/project-control/agent-operating-model.md`
5. `docs/project-control/task-ledger.md`
6. `docs/project-control/next-actions.md`
7. `docs/project-control/active-work-registry.md`
8. `docs/project-control/shift-change-checklist.md`

After the markdown control files, optional advisory context may include `hc_context/project_state.json`, `hc_context/agent_rules.json`, `hc_context/protected_surfaces.json`, `hc_context/next_tasks.json`, and `hc_context/evidence_rules.json`.

## State reconciliation steps

At shift start:

1. Compare the current branch, changed files, and recent commits or PR references against the project-state, active-work registry, and task-ledger notes.
2. Confirm whether the requested mode is REPORT ONLY, docs-only, tests-only, implementation, or protected-path work.
3. Identify protected-path adjacency before making changes.
4. Check whether any task appears merged, closed, superseded, abandoned, or already parked.
5. Record uncertainty as an evidence gap; do not fill gaps with chat memory or stale machine-readable context.

## Check-in requirements

A shift check-in should state:

- operator or agent role;
- task scope and intended files;
- requested mode and protected-path assessment;
- current phase and active focus being served;
- source files read for orientation;
- checks expected for the touched scope;
- known blockers, parked work, active-work registry updates, or stale-context mismatches.

## Checkout requirements

A shift checkout should state:

- changed files, or confirmation that no files changed;
- commit hash and PR reference when available;
- checks run and whether each passed, failed, or could not run;
- remaining gaps, risks, or reviewer decisions needed;
- next safe action, active-work registry status, and any do-not-repeat notes;
- confirmation that protected paths were not modified, unless explicitly authorized.

## Evidence bundle reminders

Include enough evidence for another operator to continue without relying on chat memory:

- task or issue reference;
- changed files;
- commit hash and PR reference when available;
- commands and checks run;
- review or human-supervised validation notes when available;
- source documents used for state claims;
- stale-context mismatch notes when `hc_context`, chat memory, or external summaries differ from repository evidence.

## Stale-context guidance

Markdown project-control docs are authoritative for handoff state, active focus, priority order, and protected-path reminders. The `hc_context` directory is advisory agent context and may be useful for cross-checking, but it must not override markdown docs, merged repository files, checks, PR records, protected indexes, or human review decisions. If a mismatch appears, report the mismatch in the evidence bundle and continue from repository evidence; do not automatically rewrite either source during handoff.
