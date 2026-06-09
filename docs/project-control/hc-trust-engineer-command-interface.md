# HC Trust Engineer Command Interface

Status: design proposal.

This document defines a safe command interface for using HC Trust Engineer inside the GitHub repository without requiring a separate website or chat UI.

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

## Recommended console issue

A repository may keep one pinned or clearly named issue as the assistant console:

```text
HC Assistant Console
```

This issue can be used for project-level questions such as status, next task, onboarding, and explanation commands.

Pull-request-specific questions should still be asked on the relevant PR.

## Command prefix

All commands should use the `/hc` prefix.

This keeps the interface explicit and avoids accidental bot responses.

## Core commands

### `/hc help`

Shows available commands and explains advisory-only boundaries.

Expected response:

```text
HC Trust Engineer commands:
- /hc help
- /hc status
- /hc next
- /hc explain
- /hc review
- /hc risks
- /hc evidence

Boundary: advisory only. Human maintainers retain final authority.
```

### `/hc status`

Summarizes current repository state.

Allowed sources:

- current open PR list;
- latest merged PR metadata;
- project-control documents;
- governance documents;
- known roadmap/checkpoint documents.

Required boundaries:

- separate GitHub-verified state from stale summaries;
- do not claim full repository audit unless actually performed;
- do not expose secrets, credentials, tokens, or private keys.

### `/hc next`

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

### Pull request comments

Use for:

- `/hc review`;
- `/hc risks`;
- `/hc evidence`.

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

## First implementation recommendation

The first implementation should be documentation-only or report-only.

Recommended sequence:

1. define command interface;
2. create an Assistant Console issue template or guide;
3. add a non-LLM command parser;
4. support `/hc help` and `/hc status`;
5. support `/hc next` using trusted project-control docs;
6. support PR-scoped `/hc review` using changed-file metadata;
7. consider GitHub App migration only after the command model is stable.

## Final boundary

HC Trust Engineer should feel helpful like a repository assistant.

It must remain advisory like a controlled trust-layer component.

The assistant can guide the work.

It cannot become the authority.
