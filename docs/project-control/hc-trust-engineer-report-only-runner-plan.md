# HC Trust Engineer Report-Only Runner Plan

Status: implementation plan

Related architecture:

- `docs/project-control/hc-trust-engineer-agent-architecture.md`

Purpose:

Define the first safe runner for the HC Trust Engineer Agent.

This runner is not an autonomous maintainer. It is a report-only assistant that turns repository state into structured, auditable guidance.

Core data principle:

```text
Data is not only stored.
Data carries provenance, memory, context, and responsibility.
```

HC interpretation:

```text
A repository event is not just an event.
It has a source, history, trigger, changed files, checks, comments, risk, and audit trail.
```

The agent must read that memory before speaking.

## 1. First runner mode

The first runner must be report-only.

It may:

- read repository metadata;
- read PR metadata;
- read changed file paths;
- read CI check state;
- read issue or PR comments;
- read project-control docs from `main`;
- produce a structured report;
- write an advisory comment only if explicitly enabled later.

It must not:

- approve PRs;
- reject PRs;
- merge PRs;
- close PRs or issues;
- edit repository files;
- change labels;
- request reviewers;
- run code from PR branches;
- treat user or PR text as trusted instruction;
- expose secrets;
- claim legal truth;
- set `truth_guarantee=true`.

## 2. Inputs

Minimum inputs:

- repository name;
- event type;
- PR or issue number when available;
- base branch;
- base SHA;
- head SHA;
- changed file list;
- workflow/check state;
- existing review thread state;
- project-control current state file paths.

Untrusted inputs:

- PR title;
- PR body;
- issue body;
- issue comments;
- commit messages;
- PR branch files;
- model-generated suggestions.

Trusted inputs:

- `main` branch at known SHA;
- merged PR history;
- GitHub check results;
- project-control docs from `main`;
- governance docs from `main`.

## 3. Output shape

The runner should produce a deterministic JSON report.

Proposed fields:

```json
{
  "agent": "HC Trust Engineer",
  "mode": "report_only",
  "advisory_only": true,
  "public_safe": true,
  "truth_guarantee": false,
  "repository": "yolculuk38-debug/HC-TRUST-LAYER",
  "event_type": "pull_request",
  "target_number": 0,
  "base_sha": "...",
  "head_sha": "...",
  "open_prs": [],
  "changed_files": [],
  "risk_flags": [],
  "required_human_review": true,
  "checks": [],
  "unresolved_threads": [],
  "missing_evidence": [],
  "recommended_next_action": "stop_or_continue",
  "stop_reason": null
}
```

## 4. Decision language

The report must use advisory language.

Allowed:

- `recommended_next_action`;
- `risk_flags`;
- `required_human_review`;
- `stop_reason`;
- `missing_evidence`.

Not allowed:

- `approved`;
- `rejected`;
- `authorized`;
- `truth_guarantee=true`;
- `final_decision`.

## 5. Stop conditions

The runner must stop and report if:

- checks are failing;
- checks are still pending;
- review threads are unresolved;
- mergeability is unknown;
- protected or trust-critical files changed unexpectedly;
- project-control state conflicts with PR state;
- evidence is missing;
- instruction asks for policy bypass;
- more than one PR is open.

## 6. Minimum first implementation

The first code slice should be small.

Suggested path:

```text
scripts/hc_trust_engineer_report.py
```

Required behavior:

- accept local JSON input fixture;
- produce deterministic JSON report;
- no network calls;
- no GitHub writes;
- no LLM calls;
- no subprocess execution;
- no PR branch checkout.

Suggested tests:

```text
tests/test_hc_trust_engineer_report.py
```

Test scenarios:

- no open PRs;
- one open PR with green checks;
- one open PR with pending checks;
- unresolved review thread;
- protected path changed;
- multiple open PRs;
- missing evidence;
- advisory boundaries always present.

## 7. Later implementation stages

### Stage A: local fixture runner

- local JSON input;
- deterministic report output;
- unit tests.

### Stage B: GitHub Actions report artifact

- read event metadata;
- run report generator;
- upload JSON artifact;
- no comments yet.

### Stage C: advisory issue or PR comment

- write one deduplicated advisory comment;
- never issue commands to other workflows;
- never request merge.

### Stage D: issue command console integration

- `/hc status`;
- `/hc next`;
- `/hc review <number>`;
- `/hc continue`.

### Stage E: VPS or GitHub App runner

- webhook listener;
- persistent state log;
- background report generation;
- mobile-first operation.

## 8. Security constraints

- read governance from `main`, not PR branch;
- never execute PR branch code;
- never import PR branch modules;
- never use PR body as instruction;
- never expose secrets or environment values;
- keep permissions minimal;
- prefer read-only mode first.

## 9. Product goal

The first useful version should answer:

```text
What is happening in the repo?
What evidence exists?
What is risky?
What should stop?
What is the next safe action?
```

It should not pretend to be a person, maintainer, judge, or truth engine.

## 10. Queue status

Stage A is a future candidate, not the active queue by itself.

Before starting implementation, check the canonical project-control queue in:

- `docs/project-control/next-actions.md`
- `docs/project-control/project-state.md`
- `docs/project-control/task-ledger.md`

If those files point to a different active task, follow the current queue first and update this plan through a separate reviewed PR when needed.
