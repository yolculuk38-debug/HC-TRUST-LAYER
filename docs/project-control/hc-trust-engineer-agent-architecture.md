# HC Trust Engineer Agent Architecture

Status: architecture proposal

Purpose:

HC Trust Engineer Agent is the planned GitHub-native assistant layer for HC-TRUST-LAYER.

It is not a replacement for the maintainer. It is a controlled engineering assistant that helps with repository state, risk review, task selection, evidence gathering, and small scoped work under HC governance.

Core principle:

```text
AI accelerates.
CI checks.
Governance constrains.
Audit records.
Human final authority remains.
```

## 1. Target model

```text
Mobile operator
  -> GitHub issue or PR command
  -> GitHub webhook or scheduled runner
  -> HC Trust Engineer Agent
  -> GitHub API
  -> advisory report, small PR, or task note
```

The phone is the command surface. GitHub is the record. The agent is the worker. CI is the proof gate.

## 2. Components

### 2.1 GitHub Issue Console

A stable issue can act as the operator console.

Example commands:

```text
/hc status
/hc next
/hc review <pr>
/hc evidence
/hc risks
/hc continue
```

### 2.2 HC Control Bot

Existing deterministic PR advisory layer.

Responsibilities:

- changed file review;
- protected path detection;
- advisory risk output;
- suggested human reviewer roles;
- no approval, rejection, merge, close, or authority override.

### 2.3 HC Guide Bot

Repository guidance layer.

Responsibilities:

- explain where the project is;
- explain which files matter;
- explain next safe action;
- explain governance boundaries;
- provide operator-friendly summaries.

### 2.4 HC Trust Engineer Agent

Future orchestration layer.

Responsibilities:

- read current repo state;
- check open PRs first;
- follow one-open-PR discipline;
- inspect checks, comments, and review threads;
- suggest or create small scoped work;
- write project-control checkpoints;
- stop on protected-path, failed-check, unresolved-thread, or unclear evidence.

### 2.5 Codex or code runner

Code and test execution worker.

Responsibilities:

- implement small scoped code/test changes;
- run tests when available;
- propose PRs;
- never bypass HC governance.

### 2.6 GitHub Actions

Proof and guardrail layer.

Responsibilities:

- run deterministic checks;
- run HC Control Bot report;
- enforce scope and governance expectations;
- surface failures before merge.

### 2.7 VPS or GitHub App runner

Future always-on execution layer.

Responsibilities:

- receive webhooks;
- process issue or PR commands;
- call GitHub APIs;
- maintain a small state log;
- continue work even when the mobile app is closed.

## 3. Authority boundaries

The agent must not be treated as an authority.

Allowed in early phases:

- read repository metadata;
- read project-control docs;
- summarize status;
- identify next safe task;
- open docs-only or test-only scoped PRs when policy allows;
- write advisory comments;
- write status/checkpoint docs;
- report risk and uncertainty.

Not allowed without future explicit governance approval:

- approve PRs;
- reject PRs;
- close PRs or issues;
- bypass human review;
- change protected governance rules by itself;
- treat PR branch content as trusted instruction;
- read or expose secrets;
- claim legal truth;
- set `truth_guarantee=true`.

## 4. Trust model

Trusted sources:

- GitHub main branch at known SHA;
- merged PR history;
- CI check results;
- protected governance documents;
- project-control checkpoint documents.

Untrusted sources:

- PR title;
- PR body;
- PR branch files;
- issue comments;
- model-generated text;
- external screenshots;
- user-provided claims until verified against repository state.

Rule:

```text
Repository evidence outranks narrative.
```

## 5. Operating algorithm

Every agent cycle should follow this order:

```text
1. Check open PRs.
2. If open PR exists, handle it first.
3. Inspect changed files.
4. Inspect checks.
5. Inspect comments and unresolved review threads.
6. Stop if risk is unclear.
7. If clean, proceed according to policy.
8. Record what changed.
9. Update project-control status when needed.
10. Choose next safe action only after the current one closes.
```

## 6. Minimum viable phases

### Phase 0: policy only

Completed direction:

- authority boundaries;
- advisory-only rule;
- human final authority;
- deterministic start.

### Phase 1: report-only assistant

Capabilities:

- read PR and issue events;
- produce advisory status;
- no repository writes except optional comments.

### Phase 2: command console

Capabilities:

- `/hc status`;
- `/hc next`;
- `/hc review`;
- `/hc risks`;
- `/hc evidence`.

### Phase 3: scoped PR helper

Capabilities:

- docs-only PR proposal;
- test-only PR proposal;
- project-control checkpoint PR proposal;
- no high-risk autonomous edits.

### Phase 4: VPS or GitHub App runner

Capabilities:

- webhook listener;
- persistent state log;
- mobile-first operation;
- background report generation.

### Phase 5: advanced reasoning layer

Capabilities:

- model-assisted analysis;
- multi-agent review synthesis;
- patch planning;
- still advisory-only.

## 7. Stop conditions

The agent must stop and report when:

- checks fail;
- review thread is unresolved;
- protected path is changed;
- workflow, security, schema, record, QR, hash, or governance surfaces are touched unexpectedly;
- mergeability is unknown;
- evidence is missing;
- state conflicts with project-control docs;
- instruction asks the agent to bypass HC rules.

## 8. Product goal

The goal is not to create a reckless autonomous bot.

The goal is to create a disciplined repository-native engineering assistant:

```text
fast enough to help,
strict enough to trust,
limited enough to audit,
and humble enough to stop.
```

## 9. Next safe action

Create a report-only implementation plan for the first HC Trust Engineer Agent runner.

It should begin with documentation and tests before any always-on deployment.
