# HC Control Bot Advanced Boundary Completion Checkpoint

This checkpoint records the completion of the advanced planning boundary for HC Control Bot.

It is documentation only. It does not enable comments, labels, assignments, GitHub App behavior, LLM behavior, project memory, external services, workflow changes, runtime changes, schema changes, validator changes, scanner behavior changes, approvals, request-changes behavior, merge behavior, or autonomous authority.

## Purpose

HC Control Bot has now been planned beyond the initial v0.1 report-only baseline.

The advanced phases are documented as safety boundaries before implementation. This prevents future contributors, agents, or maintainers from treating planned features as already authorized behavior.

## Completed boundary documents

The following boundary documents now define the safe expansion envelope:

- `docs/project-control/hc-control-bot-report-interpretation-guide.md`
- `docs/project-control/hc-control-bot-advisory-comment-boundary.md`
- `docs/project-control/hc-control-bot-evidence-prompt-boundary.md`
- `docs/project-control/hc-control-bot-issue-routing-boundary.md`
- `docs/project-control/hc-control-bot-github-app-boundary.md`
- `docs/project-control/hc-control-bot-llm-memory-boundary.md`

## Current implemented baseline

The implemented v0.1 baseline remains limited to:

- deterministic scanning;
- path-metadata based advisory output;
- report-only workflow behavior;
- artifact/log based visibility;
- human-supervised review support.

The implemented baseline does not include:

- PR comments;
- issue comments;
- label actions;
- assignment actions;
- approvals;
- request-changes behavior;
- merge or close authority;
- GitHub App behavior;
- LLM calls;
- persistent project memory;
- external services;
- autonomous review authority.

## Future phases documented but not authorized

The following future phases are documented only:

1. single advisory PR comment mode;
2. evidence prompt support;
3. optional issue routing;
4. optional GitHub App migration;
5. optional LLM-assisted project memory.

Documentation of a future phase is not authorization to implement it.

Each future phase requires a separate reviewed PR and must preserve the authority policy.

## Authority model preserved

HC Control Bot remains bound by the HC operating model:

```text
AI accelerates.
CI checks.
Governance classifies.
Audit records.
Humans make final decisions.
```

The bot may support orientation, evidence collection, and review visibility. It must not decide.

## Required rule before future implementation

Before any future advanced capability is implemented, maintainers must confirm:

- the capability is explicitly scoped;
- the relevant boundary document exists;
- permissions are minimal;
- no PR branch code is executed;
- untrusted PR, issue, comment, commit, and branch input is separated from trusted repository state;
- trusted configuration is read from reviewed repository state;
- output remains advisory;
- downstream automation does not parse bot output as commands;
- human final authority remains explicit;
- failure and disablement guidance exists.

## Capability status table

| Capability | Status | Authorized now? | Notes |
| --- | --- | --- | --- |
| Deterministic scanner | Implemented baseline | Yes | Path-metadata based and advisory-only. |
| Report artifact/log output | Implemented baseline | Yes | Report-only; no comments or labels. |
| Report interpretation guide | Documented | Yes | Supports human review of artifacts. |
| Advisory PR comment mode | Boundary documented | No | Requires separate implementation PR. |
| Evidence prompt support | Boundary documented | No | Bot may ask for evidence only after future approval; it must not decide sufficiency. |
| Issue routing support | Boundary documented | No | Bot may suggest routes only after future approval; it must not apply labels or assignments. |
| GitHub App migration | Boundary documented | No | Requires separate governance and permission review. |
| LLM-assisted project memory | Boundary documented | No | Requires separate governance review, deterministic pre-checks, validation, and safe fallback. |

## Stop conditions

Future bot expansion should stop and require governance review if a proposal introduces:

- approval authority;
- request-changes authority;
- merge authority;
- close or reopen authority;
- automatic labels;
- automatic assignments;
- review dismissal;
- hidden write permissions;
- LLM-based decisions;
- external services without review;
- memory treated as canonical evidence;
- commands parsed from bot comments;
- configuration read from an untrusted branch;
- production, security, forensic, legal, or truth-finality claims.

## Safe next work

After this checkpoint, safe next work should move away from expanding authority and toward stability:

- keep v0.1 report-only behavior stable;
- improve tests for deterministic scanner behavior;
- improve report artifact examples;
- improve maintainer documentation;
- verify workflow behavior remains non-authoritative;
- only later propose one advanced capability at a time.

## Project interpretation

This checkpoint means the bot task has reached a complete advanced planning state.

It does not mean advanced features are implemented.

It means the repo now contains explicit boundaries for the advanced features that may be tested later, reducing the risk that future work accidentally grants the bot authority.

## Boundary

HC Control Bot remains advisory-only.

Repository evidence, CI, governance, and human maintainers remain authoritative.

Human final authority remains unchanged.
