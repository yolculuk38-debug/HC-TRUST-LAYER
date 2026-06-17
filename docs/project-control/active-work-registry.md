# Active Work Registry

This advisory registry helps HC-TRUST-LAYER operators and agents track active, next, blocked, parked, and recently completed work during a shift. It is a lightweight coordination aid for HC:// repository operations and does not change workflow behavior, runtime behavior, schemas, validators, records, policy, federation, signing, trust-kernel indexes, or governance enforcement.

## Authority Boundary

- Advisory only.
- Not approval authority.
- Not merge authority.
- Not governance enforcement.
- Not security validation.
- Not a substitute for repository-defined checks, reviewer oversight, or human-supervised validation.
- Does not establish production readiness, truth guarantees, forensic certainty, autonomous governance finality, or cryptographic or policy guarantees.

## Source-of-Truth Priority

Use this priority order when registry notes conflict with other evidence:

1. Merged repository files and protected repository evidence.
2. Repository-defined checks and validation outputs.
3. PR records, commits, review notes, and human review decisions.
4. `docs/project-control/project-state.md` for current phase and current focus.
5. `docs/project-control/task-ledger.md` for task history, completed references, closed references, and do-not-repeat notes.
6. `docs/project-control/next-actions.md` for the priority queue of safe next work.
7. This Active Work Registry for advisory shift-level coordination only.
8. `hc_context` files, chat memory, and external summaries as advisory context that may be stale.

Do not use this registry to override Project State, Task Ledger, Next Actions, repository evidence, or human-supervised validation.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Repository cleanup phase 1 mapping completed; phase 2 must stay small, reversible, evidence-backed, and human-reviewed. |
| Current focus | Use `docs/project-control/project-state.md`. |
| Current active work | Record short advisory entries under Current Work during check-in. |
| Next work | Use `docs/project-control/next-actions.md`, `docs/project-control/repository-index-chain-2026-06-16.md`, and `docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md` before proposing phase 2 cleanup. |
| Blocked work | Record shift-visible blockers under Blocked Work; do not treat this as approval routing. |
| Parked work | Record parked items under Parked Work and cross-check Project State. |
| Completed references | Use `docs/project-control/task-ledger.md` as the history and do-not-repeat source. |
| Repository signal review | Use `docs/project-control/github-signal-watch-policy.md` before claiming the repository is clean, dependency updates are current, or platform signals have no HC impact. |
| Protected-path reminder | Do not modify workflows, runtime code, schemas, validators, records, policy, federation, signing, trust-kernel indexes, `hc_context`, or agents unless explicitly authorized. |
| Evidence expectation | Every entry should point to repository evidence or name the evidence gap. |

## Current Work

Use this section for work actively being handled during the current shift.

Recommended entry format:

- Task: `<short task name>`
  - Mode: `REPORT ONLY`, `DOCS ONLY`, `tests-only`, or explicitly authorized implementation mode.
  - Operator / agent: `<name or role>`
  - Intended files: `<paths>`
  - Protected-path assessment: `<none / adjacency / authorized protected-path work>`
  - Evidence: `<issue, PR, commit, check output, or source file reference>`
  - Status: `<started / in review / waiting on evidence / ready for checkout>`

Current entries:

- No standing current-work entry is asserted by this registry. Use Project State, Next Actions, the repository index chain, and the cleanup phase 1 checkpoint for current phase, current focus, and priority queue.

## Next Work

Next Work mirrors only the advisory handoff need for a shift. It does not replace `docs/project-control/next-actions.md`, which remains the priority queue source.

Recommended entry format:

- Task: `<short task name>`
  - Priority source: `docs/project-control/next-actions.md`
  - Mode: `<mode from request or Next Actions>`
  - Evidence needed before start: `<files, PRs, checks, or reviewer notes>`

Current entries:

- Use `docs/project-control/next-actions.md`, `docs/project-control/repository-index-chain-2026-06-16.md`, and `docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md` before starting the next item.

## Blocked Work

Use this section for active tasks that cannot proceed because evidence, authorization, checks, or reviewer decisions are missing.

Recommended entry format:

- Task: `<short task name>`
  - Blocker: `<missing evidence / explicit authorization needed / check failure / reviewer decision>`
  - Last evidence: `<source file, commit, PR, or command output>`
  - Safe next step: `<report gap / request review outside this file / park item>`

Current entries:

- No standing blocked-work entry is asserted by this registry.

## Parked Work

Use this section for work intentionally not being advanced during the current shift.

Parked work commonly includes workflow, runtime, schema, validator, record, policy, federation, signing, trust-kernel index, `hc_context`, agent, and governance-enforcement changes unless explicitly authorized and routed through human-supervised validation.

Recommended entry format:

- Task: `<short task name>`
  - Reason parked: `<protected path / trust-kernel impact / out of scope / stale evidence>`
  - Source: `<Project State, Task Ledger, Next Actions, PR, or reviewer note>`
  - Reopen condition: `<explicit authorization / new evidence / reviewer request>`

Current entries:

- Protected-path and trust-kernel-impacting work remains parked unless explicitly authorized and validated.

## Completed Work References

This registry may point to completed work, but it is not the completed-work history source. Use `docs/project-control/task-ledger.md` for task history, PR references, closed references, and do-not-repeat notes.

Recommended entry format:

- Reference: `<task, PR, or commit>`
  - Summary: `<short description>`
  - Evidence: `<Task Ledger, PR record, commit, checks, or review notes>`
  - Follow-up: `<none / do not repeat / inspect before related work>`

Current entries:

- Cross-check `docs/project-control/task-ledger.md` before treating any task as completed.

## Do-Not-Repeat Work

This registry may surface do-not-repeat reminders during a shift, but it does not replace the Task Ledger.

Before repeating, reviving, or renaming related work:

1. Read `docs/project-control/task-ledger.md`.
2. Check PR records, commits, review notes, and checks when available.
3. Report stale or conflicting evidence instead of assuming the registry is current.
4. Do not reuse closed, conflicted, superseded, abandoned, or merged work as a new active task without explicit reviewer direction.

## Evidence Requirements

Every registry update should include enough evidence for another operator to continue without chat memory:

- task or issue reference when available;
- changed files or intended files;
- mode and protected-path assessment;
- source files read for orientation;
- commit hash or PR reference when available;
- checks run and outcomes when available;
- review or human-supervised validation notes when available;
- stale-state or advisory-source mismatch notes.

If an evidence layer is missing, mark it as an evidence gap and avoid completion, approval, merge, governance-enforcement, or security-validation claims.

## Check-In Use

At shift check-in, use this registry to record only the active coordination snapshot:

1. Confirm the current phase and current focus from `docs/project-control/project-state.md`.
2. Confirm the priority queue from `docs/project-control/next-actions.md`.
3. Cross-check completed or do-not-repeat work in `docs/project-control/task-ledger.md`.
4. Confirm repository-wide pull requests, dependency updates, check annotations, and platform signals using `docs/project-control/github-signal-watch-policy.md`.
5. Add or update a Current Work entry with role, scope, mode, intended files, protected-path assessment, expected checks, and evidence gaps.
6. Keep claims advisory and reversible.

## Checkout Use

At shift checkout, use this registry to hand off the active coordination snapshot:

1. Move finished shift items to Completed Work References only when evidence is available.
2. Move unfinished items to Current Work, Blocked Work, or Parked Work as appropriate.
3. Include changed files, commit hash or PR reference when available, checks run, unresolved gaps, and next safe action.
4. Keep `docs/project-control/task-ledger.md` as the history and do-not-repeat source.
5. Do not imply approval, merge readiness, governance enforcement, or security validation.

## Stale-State Handling

This registry may lag behind repository evidence. When it conflicts with Project State, Task Ledger, Next Actions, merged files, checks, PR records, protected indexes, or human review decisions:

1. Treat the registry as stale.
2. Report the mismatch in the evidence bundle.
3. Cite the stronger repository evidence.
4. Do not rewrite Project State, Task Ledger, Next Actions, `hc_context`, protected paths, or reviewer decisions automatically.
5. Update this registry only when the requested scope allows documentation updates and the change is small, auditable, and advisory.

## Related Files

- `AGENTS.md` — repository-wide contributor and agent rules.
- `HC_BOOTSTRAP.md` — first operational bootstrap checklist.
- `docs/project-control/hc-control-center.md` — single-entry operator orientation.
- `docs/project-control/project-state.md` — current phase and current focus source.
- `docs/project-control/agent-operating-model.md` — agent operating guidance.
- `docs/project-control/task-ledger.md` — task history and do-not-repeat source.
- `docs/project-control/next-actions.md` — safe next-work priority queue.
- `docs/project-control/github-signal-watch-policy.md` — repository-wide PR, dependency, platform, code scanning, workflow warning, and community visibility signal triage policy.
- `docs/project-control/repository-index-chain-2026-06-16.md` — cleanup purpose-index and inventory-pass chain.
- `docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md` — cleanup phase 1 completion checkpoint.
- `docs/project-control/shift-change-checklist.md` — check-in and checkout handoff checklist.
