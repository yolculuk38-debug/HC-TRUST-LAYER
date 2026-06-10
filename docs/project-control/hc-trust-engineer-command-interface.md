# HC Trust Engineer Command Interface

Status: local deterministic command interface implemented for the current core command set.

This document defines a safe command interface for using HC Trust Engineer inside the GitHub repository without requiring a separate website or chat UI.

## Current implementation snapshot

Implemented in `scripts/hc_assistant_command.py`:

- `/hc help`
- `/hc status`
- `/hc next`
- `/hc evidence`
- `/hc explain`
- `/hc risks`
- `/hc review`

Covered by `tests/test_hc_assistant_command.py`.

Current implementation mode:

- local deterministic parser;
- machine-readable JSON output;
- static response maps and checklists only;
- no workflow connection;
- no issue-comment listener;
- no live pull request inspection;
- no file reading from command execution;
- no network calls;
- no LLM calls;
- no repository writes;
- no labels, assignments, approvals, rejections, merges, or closes.

## Purpose

GitHub repositories do not provide a native always-on chat panel. For the first safe implementation, HC Trust Engineer can behave like a repository assistant through explicit commands and auditable GitHub comments.

The goal is to make the repository feel guided while keeping all interactions advisory-only and reviewable.

## Operating model

```text
User writes a command in an issue or pull request comment.
↓
HC Trust Engineer parses the command.
↓
The assistant returns an advisory-only response.
↓
Human maintainers decide what to do next.
```

Current limitation: the parser exists locally, but GitHub issue/PR comment automation is not connected yet.

## Recommended console issue

A repository may keep one pinned or clearly named issue as the assistant console:

```text
HC Assistant Console
```

Current console issue:

```text
#763 HC Assistant Console
```

This issue can be used for project-level questions such as status, next task, onboarding, and explanation commands.

Pull-request-specific questions should still be asked on the relevant PR.

## Command prefix

All commands should use the `/hc` prefix.

This keeps the interface explicit and avoids accidental bot responses.

## Core commands

### `/hc help`

Implementation status: implemented in the local deterministic parser.

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
```

Boundary: advisory only. Human maintainers retain final authority.

### `/hc status`

Implementation status: implemented as static local parser output.

Summarizes current command-surface status.

Current parser boundaries:

- returns static command-surface status;
- does not perform live GitHub state lookup;
- warns that a separate GitHub-verified control pass is required for current PR state;
- does not expose secrets, credentials, tokens, or private keys.

Future implementation may add live GitHub state only through a separately reviewed integration.

### `/hc next`

Implementation status: implemented as static local parser output.

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

Implementation status: implemented as static local parser output.

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

Implementation status: implemented as static local parser output.

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

Implementation status: implemented as static local parser output.

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

Implementation status: implemented as static local parser output.

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

They should be added only after the core commands are stable and after separate governance-reviewed PRs.

## Where commands should work

### Assistant console issue

Use for:

- `/hc help`;
- `/hc status`;
- `/hc next`;
- `/hc explain`;
- `/hc evidence`;
- `/hc risks`;
- `/hc review`.

Current limitation: the issue exists, but automatic issue-comment listening is not connected yet.

### Pull request comments

Use for:

- `/hc review`;
- `/hc risks`;
- `/hc evidence`.

Current limitation: PR comment automation is not connected yet.

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
