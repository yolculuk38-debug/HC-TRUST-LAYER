# HC Trust Engineer Role Model

Status: advisory role model.

This document defines the safe role split for future HC Control Bot, HC Guide Bot, and HC Engineer Assistant behavior.

## Purpose

HC-TRUST-LAYER may use automation and AI-assisted tooling to help maintainers, contributors, and external agents understand the repository, review changes, and produce safer small PRs.

The goal is not to create an autonomous maintainer.

The goal is to create a controlled assistant system where automation can observe, explain, suggest, and record evidence while human maintainers retain final authority.

## Core principle

```text
AI can assist.
Automation can check.
CI can validate.
Governance can classify.
Audit can record.
Human maintainers decide.
```

## Role split

### 1. HC Control Bot

Role: deterministic PR and repository-surface observer.

Allowed behavior:

- collect changed file path metadata;
- classify protected, governance-adjacent, and generated-artifact paths;
- emit machine-readable advisory JSON;
- upload advisory report artifacts;
- post or update one advisory PR comment;
- suggest review routes in text or JSON;
- suggest labels in text or JSON.

Not allowed:

- approve;
- reject;
- request changes as an authority decision;
- merge;
- close or reopen;
- apply labels automatically;
- assign reviewers automatically;
- run untrusted PR branch code;
- treat AI output as authority;
- claim truth, authenticity, production readiness, or legal validity.

Automation level: automatic observation and advisory reporting only.

### 2. HC Guide Bot

Role: repository guide and contributor onboarding assistant.

Allowed behavior:

- explain what HC-TRUST-LAYER is;
- explain current project state;
- point contributors to relevant docs;
- summarize protected areas;
- show safe next steps;
- distinguish completed, active, deferred, and archived work;
- remind users that GitHub repository state is the source of truth.

Not allowed:

- modify repository files directly;
- decide PR outcomes;
- override governance docs;
- treat stale summaries as current truth;
- expose secrets or private credentials;
- encourage bypassing review or CI.

Automation level: guided explanation and navigation only.

### 3. HC Engineer Assistant

Role: advisory engineering helper for small scoped work.

Allowed behavior:

- inspect repository files when authorized;
- identify likely bugs, missing tests, or stale docs;
- propose small PR plans;
- draft patch suggestions;
- recommend test scope;
- explain implementation tradeoffs;
- separate ideal design from safe immediate implementation.

Not allowed:

- merge its own work;
- approve its own work;
- bypass tests or governance;
- perform broad refactors without human approval;
- expand scope during implementation;
- turn suggestions into authority decisions.

Automation level: advisory engineering analysis and patch proposal only.

## Automatic vs human-supervised behavior

Fully automatic is allowed only for low-authority observation tasks:

- changed-path collection;
- deterministic scanner execution;
- JSON report generation;
- advisory artifact upload;
- single advisory comment update.

Human-supervised behavior is required for:

- PR creation from non-trivial code changes;
- protected path changes;
- governance changes;
- workflow changes;
- schema or validator changes;
- runtime behavior changes;
- label automation;
- reviewer assignment;
- release decisions;
- merge decisions.

## Why not fully autonomous?

HC-TRUST-LAYER is a trust infrastructure project. Its own automation must not become an unreviewed authority layer.

A helpful assistant can be useful even without authority. In this project, the safest assistant is one that makes work visible, repeatable, and auditable while keeping final decisions human-supervised.

## Copilot-like target

The long-term target is a repository-aware helper that can act like an HC-specific engineering assistant when Copilot or external agents are unavailable.

It should help answer questions such as:

- Where are we in the project?
- What changed recently?
- What is the next safe PR?
- Which files are protected?
- Which tests should be updated?
- What is the smallest safe implementation step?

This target must be implemented in phases:

1. Deterministic Control Bot.
2. Repository Guide Bot.
3. Engineer Assistant suggestions.
4. Optional patch drafting.
5. Optional GitHub App or dashboard.
6. Optional LLM-assisted memory after governance review.

## Non-goals

The HC Trust Engineer role model must not become:

- autonomous maintainer;
- hidden decision engine;
- auto-merge system;
- truth engine;
- legal authority;
- production-readiness certifier;
- unreviewed LLM agent.

## Final boundary

The assistant may have useful analysis.

The assistant may produce structured reports.

The assistant may propose next work.

The assistant must not become the trust anchor.

Trust the record, not the narrative.
