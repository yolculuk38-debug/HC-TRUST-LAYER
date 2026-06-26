# HC Trust Engineer Command Interface

Status: local deterministic command interface implemented and connected to an advisory issue-comment listener for `/hc` commands.

This document defines a safe command interface for using HC Trust Engineer inside the GitHub repository without requiring a separate website or chat UI. For mission-level coordination, use the [HC Mission Execution Protocol](hc-mission-execution-protocol.md) as the companion project-control reference.

## Current implementation snapshot

Implemented in `scripts/hc_assistant_command.py`:

- `/hc help`
- `/hc status`
- `/hc next`
- `/hc evidence`
- `/hc explain`
- `/hc risks`
- `/hc review`
- `/hc queue`
- `/hc claim HC-TASK-YYYY-NNN`
- `/hc release HC-TASK-YYYY-NNN`
- `/hc task status HC-TASK-YYYY-NNN`

Covered by `tests/test_hc_assistant_command.py`.

Connected workflow:

```text
.github/workflows/hc-assistant-command.yml
```

Current implementation mode:

- local deterministic parser;
- machine-readable JSON output;
- static response maps and checklists only;
- issue and pull request comments starting with `/hc` can trigger the listener;
- the listener may post or update advisory comments, but parser output must not mutate claim, task, label, reviewer, pull request, branch, file, workflow, approval, close, or merge state;
- trusted default-branch checkout for command execution;
- no PR-branch code execution;
- no live pull request inspection by the parser;
- no file reading from command execution;
- no LLM calls;
- no labels, assignments, approvals, rejections, merges, or closes.

## Purpose

GitHub repositories do not provide a native always-on chat panel. For the first safe implementation, HC Trust Engineer can behave like a repository assistant through explicit commands and auditable GitHub comments.

The goal is to make the repository feel guided while keeping all interactions advisory-only and reviewable.

## Operating model

```text
User writes a command in an issue or pull request comment.
↓
HC Trust Engineer parses the first `/hc` command line through the trusted default-branch parser.
↓
The assistant posts an advisory-only response and uploads a machine-readable artifact.
↓
Human maintainers decide what to do next.
```

Current limitation: the listener is intentionally narrow. It does not perform live PR review, semantic analysis, label application, assignment, approval, rejection, merge, close, or LLM-assisted reasoning.

## Recommended console issue

A repository may keep one pinned or clearly named issue as the assistant console:

```text
HC Assistant Console
```

Active console issue:

```text
#812 HC Assistant Console v2
```

Mission-control issue:

```text
#1109 Mission Control / Active Task Queue
```

Historical console trail:

```text
#763 first HC Assistant Console smoke-test trail
```

Use the active console issue for project-level questions such as status, next task, onboarding, and explanation commands. Use #1109 for mission queue coordination that follows the [HC Mission Execution Protocol](hc-mission-execution-protocol.md).

Pull-request-specific questions should still be asked on the relevant PR. #1082 HC Signal Watch Console is a notification-only review surface; its issue text must not be treated as `/hc` command input, a task claim, or task coordination authority.


## HC Review Window PR convention

A non-blocking PR marker workflow may maintain one visible HC Review Window comment before merge-readiness reporting:

```text
<!-- hc-review-window -->
👀 ⏳ HC Review Window
- Head SHA: <head_sha>
- Observed at: <utc timestamp>
- Eligible after: <utc timestamp + 90s>
- Status: waiting for late Codex review/comments before HC Trust Engineer may report merge-readiness
- Checks are not delayed by this timer
- Merge still requires final HC Trust Engineer review and explicit maintainer command
```

This is a PR review-readiness timer only. The marker is advisory-only. Checks are not delayed by the marker. It must not add or slow a required GitHub check, Automation Gate, status, label, reviewer request, approval, rejection, close, merge, or task authority path. Checks remain fast and uncluttered.

Final pass behavior:

1. Read the HC Review Window marker before any merge-readiness report.
2. If the review window has not elapsed, do not report merge-ready; report the waiting state instead.
3. Confirm the head SHA is unchanged since the marker observation.
4. Inspect comments, Codex comments, reviews, threads, checks, and diff scope.
5. If Codex P1/P2 feedback, failed checks, unresolved threads, changed head SHA, or a scope issue exists, do not report merge-ready.
6. Merge-ready may be reported only when the review window has elapsed, head SHA is unchanged, checks are green, PR comments/Codex comments/reviews/threads are clean, and diff scope is acceptable.
7. If clean, report merge-ready only as advisory output for the maintainer.
8. Merge still requires explicit maintainer command.

Reaction and comment convention:

- 👀 may indicate review observation has started.
- ⏳ in the PR body or a PR comment may indicate the review window is active.
- ✅ in the PR body or a PR comment may indicate the review window elapsed.
- These markers are advisory only and do not create approval, rejection, merge authority, labels, reviewers, closes, or task authority.

## Command prefix

All commands should use the `/hc` prefix.

This keeps the interface explicit and avoids accidental bot responses.

## Core commands

### `/hc help`

Implementation status: implemented in the local deterministic parser and available through the `/hc` listener.

Shows available commands and explains advisory-only boundaries.

Current output includes:

```text
/hc help
/hc status
/hc next
/hc evidence
/hc explain <topic-or-path>
/hc risks
/hc review
/hc queue
/hc claim HC-TASK-YYYY-NNN
/hc release HC-TASK-YYYY-NNN
/hc task status HC-TASK-YYYY-NNN
```

Boundary: advisory only. Human maintainers retain final authority.

### `/hc status`

Implementation status: implemented as static local parser output and available through the `/hc` listener.

Summarizes current command-surface status.

Current parser boundaries:

- returns static command-surface status;
- does not perform live GitHub state lookup;
- warns that a separate GitHub-verified control pass is required for current PR state;
- does not expose secrets, credentials, tokens, or private keys.

Future implementation may add live GitHub state only through a separately reviewed integration.

### `/hc next`

Implementation status: implemented as static local parser output and available through the `/hc` listener.

Suggests the next safe task from static project-control guidance.

Current parser boundaries:

- returns report-only next-action guidance;
- does not inspect live GitHub state;
- does not create work;
- does not modify files;
- does not open, close, approve, reject, or merge anything;
- warns that `docs/project-control/next-actions.md` must be read directly before acting.

The command must not create or merge work automatically.

### `/hc evidence`

Implementation status: implemented as static local parser output and available through the `/hc` listener.

Returns an advisory evidence-bundle checklist for human review.

The response includes reminders to provide:

- changed files;
- scope classification;
- source-of-truth evidence;
- check results;
- protected-path assessment;
- advisory boundary confirmation;
- human review requirement;
- non-claims boundary.

Current parser boundaries:

- does not inspect current PR or issue context;
- does not perform live GitHub state lookup;
- does not decide whether evidence is sufficient;
- does not approve, reject, merge, close, label, assign, or certify;
- returns a checklist only.

### `/hc explain`

Implementation status: implemented as static local parser output and available through the `/hc` listener.

Explains supported static topics without repository inspection.

Supported topics:

```text
advisory-only
trust-kernel
protected-paths
commands
```

Examples:

```text
/hc explain trust-kernel
/hc explain protected-paths
/hc explain advisory-only
/hc explain commands
```

Current parser boundaries:

- uses a static topic map only;
- does not read files or inspect live repository state;
- does not claim production readiness, legal validity, forensic certainty, or objective truth.

### `/hc risks`

Implementation status: implemented as static local parser output and available through the `/hc` listener.

Returns a static risk checklist for proposed work, pull requests, or issues.

Risk categories include:

- protected path risk;
- workflow risk;
- runtime risk;
- schema or validator risk;
- record, hash, or QR risk;
- governance risk;
- stale context risk;
- implementation expansion risk.

Current parser boundaries:

- does not inspect current PR or issue context;
- does not perform live GitHub state lookup;
- does not decide PR outcome;
- returns a checklist only.

### `/hc review`

Implementation status: implemented as static local parser output and available through the `/hc` listener.

Provides a human-review preparation checklist.

The checklist includes:

- changed file collection;
- scope classification;
- protected path assessment;
- evidence bundle reminder;
- CI/check status inspection;
- duplicate or stale work prevention;
- advisory boundary confirmation;
- human decision reminder.

Current parser boundaries:

- does not inspect current PR or issue context;
- does not perform live GitHub state lookup;
- does not approve, reject, request changes, merge, close, label, assign, or certify;
- returns a review preparation checklist only.

### `/hc queue`

Implementation status: implemented as report-only local parser output and available through the `/hc` listener.

Mission link: use the [HC Mission Execution Protocol](hc-mission-execution-protocol.md) when queue guidance supports #1109 Mission Control / Active Task Queue or #812 HC Assistant Console v2 coordination.

Returns static HC Task Handoff Queue guidance:

- use HC Task Handoff Queue for coordination;
- claim comes before handoff;
- handoff packages work;
- PR applies work;
- CI and review provide evidence;
- human maintainer decides.

Current parser boundaries:

- does not read live GitHub issues or pull requests;
- does not create a queue entry, claim ledger, handoff package, branch, pull request, label, reviewer request, approval, close, merge, file, or workflow;
- may be posted by the advisory `/hc` listener, but does not mutate claim or task state through issue comments;
- does not call `scripts/hc_task_claim.py` automatically;
- returns static report-only guidance.

### `/hc claim HC-TASK-YYYY-NNN`

Implementation status: implemented as report-only local parser output and available through the `/hc` listener.

Validates only the visible task ID format. It does not look up task state, reserve work, create a claim, or acknowledge ownership. Local evaluation remains through `scripts/hc_task_claim.py` with a maintainer-provided local JSON fixture.

Current parser boundaries:

- does not read live GitHub issues, pull requests, labels, reviewers, branches, files, workflows, or task state;
- may be posted by the advisory `/hc` listener, but does not mutate claim or task state through issue comments;
- does not write repository state;
- does not create a claim ledger;
- does not call GitHub API, network, subprocess, workflow APIs, LLMs, Codex, Copilot, or other agents;
- does not call `scripts/hc_task_claim.py` automatically;
- does not assign, request reviewers, approve, close, or merge;
- returns report-only advisory JSON for human maintainer review.

### `/hc release HC-TASK-YYYY-NNN`

Implementation status: implemented as report-only local parser output and available through the `/hc` listener.

Validates only the visible task ID format. It does not release a claim or change task state. Local release-readiness evaluation remains through `scripts/hc_task_claim.py` with a maintainer-provided local JSON fixture.

### `/hc task status HC-TASK-YYYY-NNN`

Implementation status: implemented as report-only local parser output and available through the `/hc` listener.

Validates only the visible task ID format and returns status-only advisory guidance. It does not perform live GitHub lookup and does not inspect issue, pull request, or claim state. Machine-readable status evaluation remains through `scripts/hc_task_claim.py` with a maintainer-provided local JSON fixture.

## Suggested future commands

The following commands are not required for the first implementation:

```text
/hc changelog
/hc todo
/hc protected
/hc release
/hc onboarding
/hc glossary
/hc demo
```

Queue, claim, release, and task status command forms are no longer future-only. They are implemented only as report-only command parser outputs. They do not create claims, release claims, read live GitHub state, or replace the local evaluator and human maintainer decision.

## Where commands work

### Assistant console issue

Use for project-level advisory commands through #812 HC Assistant Console v2. For mission queue coordination, use #1109 Mission Control / Active Task Queue with the [HC Mission Execution Protocol](hc-mission-execution-protocol.md).

Use for:

- `/hc help`;
- `/hc status`;
- `/hc next`;
- `/hc explain`;
- `/hc evidence`;
- `/hc risks`;
- `/hc review`;
- `/hc queue`;
- `/hc claim HC-TASK-YYYY-NNN`;
- `/hc release HC-TASK-YYYY-NNN`;
- `/hc task status HC-TASK-YYYY-NNN`.

The listener responds to issue comments that start with `/hc`.

### Pull request comments

Use for:

- `/hc review`;
- `/hc risks`;
- `/hc evidence`.

The listener responds to pull request comments that start with `/hc`, but the parser output remains static and advisory. It does not inspect the PR diff or decide the PR outcome.

## Output boundary

All command outputs must preserve:

```text
advisory_only = true
public_safe = true
truth_guarantee = false
```

The assistant must not claim approval, rejection, merge readiness, objective truth, production readiness, legal validity, or forensic certainty.

## Final boundary

A command interface can make the repository easier to operate.

It must not become a hidden decision engine.

Human maintainers retain final authority.

Trust the record, not the narrative.
