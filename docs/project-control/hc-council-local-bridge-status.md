# HC Council Local Bridge Status

## Status

The HC Council local command bridge is implemented as a report-only fixture bridge.

Merged baseline:

- PR #1200 added the deterministic local command parser.
- PR #1201 added the local issue-comment fixture bridge, example fixture, and tests.

## Current boundary

The current HC Council bridge implementation is local-only and report-only.

It does not add or modify any live GitHub webhook, GitHub App, issue-comment automation, or workflow wiring.

Important repository distinction:

- The repository already has a generic HC Assistant Command Listener workflow for real comments that start with `/hc`.
- That existing listener is separate from the HC Council local bridge described here.
- Operators must not treat `/hc council ...` production comments as inert test input; a real GitHub issue or PR comment beginning with `/hc` can still trigger the existing generic listener.
- The HC Council bridge is not wired into that listener in this baseline.

This bridge does not perform:

- network calls
- provider API calls
- repository writes
- workflow changes
- schema changes
- credential access
- approval, merge, close, label, assignment, or reviewer authority

Invalid, ambiguous, unsupported, or unauthorized local fixtures fail closed.

## Intended use

The bridge turns explicit local issue-comment fixtures such as:

```text
/hc council review pr 1201
```

into public-safe report-only JSON that can later feed a controlled HC Council report flow.

This supports the project rule:

```text
GitHub is source of truth.
AI is advisory only.
Human final authority remains required.
```

## Council bridge not yet active

The following HC Council-specific capabilities are intentionally not active yet:

- live HC Council issue-comment trigger
- automatic HC Council PR review posting
- automatic labels or reviewer requests
- automatic approve, reject, close, merge, or assignment actions
- provider-backed Council synthesis

Any future HC Council automation must be introduced in a separate PR with the normal gate:

1. single-open-PR discipline
2. protected-path review when applicable
3. checks green before merge
4. comments and review threads resolved
5. scope and duplicate-risk review
6. human-authorized merge

## Next safe slice

The next safe slice is a documentation-only command usage note that explains how an operator would prepare and run local fixtures manually without posting production issue or PR comments.

A later implementation slice may add a report-only workflow only after the local behavior, security boundary, existing listener interaction, and operator instructions are stable.
