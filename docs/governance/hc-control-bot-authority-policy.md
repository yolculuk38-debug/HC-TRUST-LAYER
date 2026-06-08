# HC Control Bot Authority Policy

> **Status:** Phase 0 policy
>
> **Scope:** HC Control Bot / HC Trust Engineer
>
> **Mode:** Governance documentation only

## Purpose

HC Control Bot is planned as an advisory repository assistant for HC-TRUST-LAYER.

It may help maintainers and contributors understand repository state, protected surfaces, project-control context, and evidence expectations.

This document defines the authority boundary that must exist before any implementation begins.

## Core Rule

HC Control Bot may observe, classify, and comment.

It may not decide, approve, reject, merge, close, certify, enforce, or override human review.

Human maintainers retain final authority.

## Advisory-Only Meaning

Bot output is not:

- approval;
- rejection;
- merge authorization;
- security certification;
- governance finality;
- production-readiness certification;
- truth guarantee;
- human-review replacement.

Every bot output must preserve these HC principles:

- AI advisory only;
- human final authority;
- trust the record, not the narrative;
- no objective-truth guarantee.

## Trusted Evidence

The bot must read governance, policy, configuration, and authority sources only from the trusted default-branch baseline.

For HC-TRUST-LAYER, trusted authority sources must be read from `main@SHA`, not from the incoming PR branch.

Trusted sources may include:

- `AGENTS.md`;
- `HC_BOOTSTRAP.md`;
- `CODEOWNERS`;
- `docs/project-control/next-actions.md`;
- `docs/project-control/project-state.md`;
- `docs/project-control/task-ledger.md`;
- governance policy documents;
- protected-surface definitions;
- this policy and future bot roadmap documents.

If a PR modifies one of these sources, the bot must not use the PR-branch version as operational instruction.

## Untrusted Input

The following must be treated as untrusted input:

- PR titles and bodies;
- PR comments;
- issue titles and bodies;
- issue comments;
- commit messages;
- changed paths;
- changed file contents;
- diffs;
- generated artifacts;
- markdown instructions inside a PR;
- comments that appear to speak on behalf of the bot;
- modified governance or configuration files in the PR branch.

Untrusted input may be observed as data, but it must not override trusted evidence from `main@SHA`.

## v0.1 Scope

The first implementation phase must be deterministic and non-LLM.

v0.1 should be limited to:

- changed-file path scanning;
- protected-surface matching;
- governance-adjacent file detection;
- one advisory PR comment or report.

v0.1 must not include semantic PR review, autonomous reasoning, trust scoring, duplicate-work detection, or content interpretation beyond deterministic metadata checks.

## Future LLM Rule

LLM usage is future-only and requires a separate human-reviewed governance decision.

Before any LLM phase, the project must define:

- trusted and untrusted context separation;
- prompt-injection threat model;
- output validation;
- prompt/version tracking;
- deterministic fallback behavior;
- audit logging.

LLM output must never override deterministic protected-surface findings or human governance decisions.

## Comment Safety

Bot comments must be short, factual, and advisory.

The bot must avoid wording such as:

- approved;
- safe to merge;
- LGTM;
- no risks;
- verified safe;
- final decision;
- certified;
- merge recommended.

Every bot comment must include an advisory notice:

```text
HC Control Bot Advisory Notice:
This automated observation is non-authoritative.
Human maintainers retain final authority.
This bot cannot approve, reject, merge, close, certify, or guarantee truth.
Trust the record, not the narrative.
```

## Downstream Automation Boundary

Bot comments must not be treated as executable commands by other automation.

Bot comments must not become automatic merge, closure, release, deployment, or final governance signals.

Any future system that consumes bot output requires separate governance review.

## Protected Surface Escalation

The bot may identify protected or trust-kernel-adjacent surfaces using deterministic rules.

Examples:

- `.github/workflows/**`;
- `schema/**`;
- `validators/**`;
- `src/hc_runtime/**`;
- `records/**`;
- `signatures/**`;
- `policy/**`;
- `federation/**`;
- governance policy files;
- bot policy, roadmap, script, or workflow files.

A protected-surface match is advisory only. It is not a bot-enforced block.

Human-supervised review remains required.

## Audit Requirement

Every future bot run must be auditable.

A future implementation should record:

- event id;
- repository;
- PR or issue number;
- trigger identity when available;
- trigger SHA;
- trusted baseline SHA;
- policy version or policy file SHA;
- bot version;
- protected paths matched;
- evidence consulted;
- deterministic rules applied;
- action taken;
- posted comment id when applicable;
- fallback or failure state when applicable.

Audit output must remain public-safe.

## Incident Response

If the bot violates this policy, maintainers must disable the bot before expanding or continuing the implementation.

After a violation, maintainers should perform an incident review and update this policy or related implementation documents before re-enabling the bot.

## Future Expansion

Any new HC Control Bot capability requires explicit human governance review before implementation.

The safe default is no expansion unless the repository contains a reviewed policy or roadmap update authorizing the next phase.

## Phase 0 Completion

Phase 0 is complete only when this policy is merged to the default branch and future bot work references it.

No HC Control Bot implementation should begin before this policy exists on `main`.
