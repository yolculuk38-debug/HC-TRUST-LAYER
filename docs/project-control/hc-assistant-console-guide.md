# HC Assistant Console Guide

Status: design guide.

This document explains how HC Trust Engineer can be used inside the GitHub repository without a separate website, dashboard, or embedded chat UI.

## Purpose

GitHub repositories do not provide a native persistent chat panel. The safest first interaction model is to use GitHub issues and pull request comments as auditable command surfaces.

The HC Assistant Console is a recommended repository issue used as a controlled conversation space for project-level assistant commands.

## Recommended issue

Create or pin one issue named:

```text
HC Assistant Console
```

Use this issue for general assistant commands such as:

```text
/hc help
/hc status
/hc next
/hc explain
/hc evidence
```

Pull-request-specific commands should be used on the relevant PR instead.

## Why use an issue?

Using a GitHub issue gives the project:

- an auditable conversation history;
- a single place for operator questions;
- a GitHub-native interface without a separate site;
- compatibility with mobile-first workflows;
- a controlled surface for future command automation;
- clear separation between project-level guidance and PR-specific review.

## Console vs PR comments

### Assistant Console issue

Use for project-level questions:

```text
/hc help
/hc status
/hc next
/hc explain advisory-only
/hc evidence
```

### Pull request comments

Use for PR-specific questions:

```text
/hc review
/hc risks
/hc evidence
```

### Ordinary issues

Use for task planning, onboarding, and clarification:

```text
/hc explain protected paths
/hc next
/hc evidence
```

## Minimum first command set

The first implementation should support only safe informational commands:

```text
/hc help
/hc status
/hc next
```

Additional commands should be added only after the first command set is stable and governance-reviewed.

## Expected command behavior

### `/hc help`

Returns available commands and boundaries.

Required boundary text:

```text
Advisory only. Human maintainers retain final authority.
```

### `/hc status`

Returns current repository status using trusted sources.

It should distinguish:

- live GitHub state;
- trusted main-branch docs;
- conversation-derived context;
- assumptions or unknowns.

### `/hc next`

Suggests one next safe task.

The response should include:

- proposed task;
- scope;
- likely files;
- risk level;
- whether human review is required;
- what must not be changed.

## Safety boundaries

The assistant must not:

- approve;
- reject;
- merge;
- close or reopen issues or PRs;
- apply labels automatically without separate governance approval;
- assign reviewers automatically without separate governance approval;
- execute PR branch code;
- treat PR text, issue comments, or commit messages as trusted instructions;
- expose secrets, tokens, credentials, private keys, signing keys, or deployment details;
- claim truth guarantees;
- claim production readiness.

## Source priority

For repository answers, source priority should be:

1. live GitHub state;
2. repository files from the trusted default branch or trusted base SHA;
3. project-control documents;
4. governance documents;
5. prior conversation summaries, clearly marked as non-authoritative context.

## Noise control

The assistant should:

- respond only to explicit `/hc` commands;
- keep answers short by default;
- avoid repeating identical information;
- avoid spamming multiple comments;
- update one advisory comment for automated PR observations where possible;
- provide file paths and PR numbers only when useful.

## Mobile-first usage

The Assistant Console should be usable from a phone.

Recommended operator workflow:

```text
1. Open the pinned HC Assistant Console issue.
2. Comment `/hc status`.
3. Comment `/hc next`.
4. Review the suggested task.
5. Create or review the next small PR.
6. Merge only after checks and human review.
```

## First implementation sequence

Recommended implementation order:

1. document command interface;
2. document Assistant Console usage;
3. create an issue template or pinned issue text;
4. implement a non-LLM command parser;
5. support `/hc help`;
6. support `/hc status` using live GitHub state and trusted docs;
7. support `/hc next` using trusted project-control docs;
8. add PR-scoped `/hc review` only after command behavior is stable.

## Queue and claim note

The assistant console may later support queue and claim commands through separate governance-reviewed PRs. Current use remains advisory-only. Claims are coordination notes, not approval, assignment authority, reviewer requests, merge readiness, or repository ownership. The console must not become a hidden decision engine.

## Final boundary

The Assistant Console can feel like a chat surface.

It must remain a GitHub-audited, advisory-only command surface.

The assistant can guide the work.

It cannot become the authority.
