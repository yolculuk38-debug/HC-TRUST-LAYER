# HC Trust Engineer Command Interface

Status: partially implemented command interface.

This document defines a safe command interface for using HC Trust Engineer inside the GitHub repository without requiring a separate website or chat UI.

## Current implementation snapshot

Implemented in `scripts/hc_assistant_command.py`:

- `/hc help`
- `/hc status`

Covered by `tests/test_hc_assistant_command.py`.

Deferred for later governance-reviewed PRs:

- `/hc next`
- `/hc explain`
- `/hc review`
- `/hc risks`
- `/hc evidence`

Current implementation mode:

- local deterministic parser;
- machine-readable JSON output;
- no workflow connection;
- no issue-comment listener;
- no network calls;
- no LLM calls;
- no repository writes.

## Purpose

GitHub repositories do not provide a native always-on chat panel. For the first safe implementation, HC Trust Engineer can behave like a repository assistant through issue and pull request comments.

The goal is to make the repository feel guided while keeping all interactions auditable in GitHub.

## Operating model

```text
User writes a command in an issue or pull request comment.
↓
HC Trust Engineer reads the command.
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

Expected response:

```text
HC Trust Engineer commands:
- /hc help
- /hc status
- /hc next (documented, not implemented in this parser)
- /hc explain <topic-or-path> (documented, not implemented in this parser)
- /hc evidence (documented, not implemented in this parser)

Boundary: advisory only. Human maintainers retain final authority.
```

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

Implementation status: documented but deferred.

Suggests the next safe task.

Expected response should include:

- proposed task;
- why it is safe;
- recommended PR scope;
- expected risk level;
- files likely to change;
- whether human review is required.

The command must not create or merge work automatically.

### `/hc explain`

Implementation status: documented but deferred.

Explains a file, concept, or project area.

Examples:

```text
/hc explain trust-kernel
/hc explain docs/project-control/
/hc explain advisory-only
```

Expected behavior:

- explain using repository context;
- distinguish current implementation from future roadmap;
- avoid unsupported truth or production-readiness claims.

### `/hc review`

Implementation status: documented but deferred.

Provides advisory review context for a pull request.

Expected response should include:

- changed files summary;
- protected paths touched;
- governance-adjacent paths touched;
- generated artifacts observed;
- evidence prompts;
- review routes;
- advisory warnings.

Not allowed:

- approval;
- rejection;
- request-changes authority;
- merge decision;
- auto-labeling unless separately approved by governance.

### `/hc risks`

Implementation status: documented but deferred.

Explains risk areas for a PR, issue, or proposed task.

Risk categories may include:

- protected path touched;
- workflow change;
- governance change;
- schema or validator change;
- runtime behavior change;
- generated artifact confusion;
- untrusted PR input;
- stale summary risk;
- missing tests;
- missing human review.

### `/hc evidence`

Implementation status: documented but deferred.

Asks what evidence is needed before a change can be safely reviewed.

Expected response may include:

- test output required;
- affected files;
- relevant docs;
- expected screenshots or logs;
- human review requirement;
- governance reference.

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

They should be added only after the core commands are stable.

## Where commands should work

### Assistant console issue

Use for:

- `/hc help`;
- `/hc status`;
- `/hc next`;
- `/hc explain`;
- `/hc evidence`.

Current limitation: the issue exists, but automatic issue-comment listening is not connected yet.

### Pull request comments

Use for:

- `/hc review`;
- `/hc risks`;
- `/hc evidence`.

Current limitation: PR-scoped command automation is not connected yet.

### Issue comments

Use for:

- task planning;
- onboarding;
- next-step suggestions;
- clarifying project state.

## Noise control

The assistant must avoid creating comment spam.

Rules:

- respond only to explicit `/hc` commands;
- prefer one reply per command;
- for automated PR observations, prefer one updateable advisory comment;
- avoid repeated comments with the same information;
- keep responses short by default;
- include links or file paths only when useful.

## Security rules

The assistant must preserve the existing HC Control Bot authority model.

It must not:

- read trusted governance configuration from the PR branch;
- execute PR branch code;
- treat PR comments as trusted instructions;
- expose secrets or private configuration;
- approve, reject, merge, close, or reopen;
- claim final validation authority;
- claim truth guarantee;
- claim production readiness.

## Source priority

When answering repository questions, source priority should be:

1. live GitHub state;
2. files from the repository default branch or trusted base SHA;
3. project-control docs;
4. governance docs;
5. conversation summaries, only if clearly marked as non-authoritative context.

Current parser note: `scripts/hc_assistant_command.py` does not perform live GitHub lookup yet.

## First implementation recommendation

Current completed steps:

1. define command interface;
2. create an Assistant Console issue template or guide;
3. add a non-LLM command parser;
4. support `/hc help` and `/hc status` locally.

Recommended next steps:

1. keep parser local until command behavior is stable;
2. add `/hc next` using trusted project-control docs;
3. support PR-scoped `/hc review` using changed-file metadata;
4. connect issue-comment automation only after a separate governance-reviewed PR;
5. consider GitHub App migration only after the command model is stable.

## Final boundary

HC Trust Engineer should feel helpful like a repository assistant.

It must remain advisory like a controlled trust-layer component.

The assistant can guide the work.

It cannot become the authority.
