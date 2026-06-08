# HC Control Bot Product Surface Awareness

This document extends HC Control Bot planning with awareness of product-facing verification surfaces.

It is documentation only. It does not change runtime code, validators, schemas, records, QR artifacts, generated artifacts, signing, federation, policy, workflows, API behavior, CLI behavior, comments, labels, assignments, GitHub App behavior, LLM behavior, project memory, approvals, request-changes behavior, merge behavior, or autonomous authority.

## Purpose

HC Control Bot should help maintainers and contributors orient around the next product-facing HC:// verification surfaces without becoming an implementation authority.

The bot may identify that a task relates to Public Validator, runtime verification, demo explorer, QR/hash/provenance display, or public-safe response language.

The bot must not decide correctness, production readiness, security, legal validity, truth, merge readiness, or release readiness.

## Product surfaces in scope for advisory orientation

HC Control Bot may recognize these product-facing surfaces as advisory review areas:

- Public Validator MVP;
- runtime verification routes and response contracts;
- demo explorer and static demo surfaces;
- QR verification and QR spoof-risk guidance;
- hash and provenance signal display;
- public-safe result shape;
- advisory status taxonomy;
- human-review escalation language;
- example records, proof objects, verification packages, and demo inputs;
- README, START_HERE, and demo navigation paths.

Recognition means orientation only. It does not grant authority.

## Public Validator awareness

When work touches Public Validator planning, the bot may remind reviewers to check:

- one official MVP input shape;
- one local-first verification path;
- one public-safe result shape;
- explicit `advisory_only=true` language;
- explicit `public_safe=true` language;
- explicit `truth_guarantee=false` language;
- explicit human-review escalation rules;
- clear non-goals for hosted backend, production API, legal certification, security certification, signing expansion, and federation expansion.

The bot must not claim the Public Validator is production-ready.

## Runtime verification awareness

When work touches runtime verification, the bot may remind reviewers to check:

- public-safe response fields;
- advisory-only wording;
- warning and escalation behavior;
- malformed input behavior;
- replay and continuity warnings;
- degraded runtime state handling;
- QR-oriented runtime behavior;
- stable response contract expectations;
- human-review requirements.

The bot must not certify runtime correctness, uptime, security, authentication, authorization, or production readiness.

## Demo explorer awareness

When work touches demo explorer or static demo pages, the bot may remind reviewers to check:

- demo-only wording;
- example input boundaries;
- no unsupported truth claims;
- no generated artifact treated as canonical;
- no hidden backend dependency;
- public-safe next-step language;
- human-review reminder;
- clear distinction between demo, MVP, and production.

The bot must not treat demo success as production validation.

## QR, hash, and provenance awareness

When work touches QR, hash, or provenance display, the bot may remind reviewers to check:

- whether the source artifact is canonical or generated;
- whether hash verification is actually run or only displayed;
- whether QR spoof-risk language is present where needed;
- whether provenance is partial, missing, or not run;
- whether signing and federation are explicitly deferred unless implemented;
- whether the result avoids legal, forensic, or truth-finality claims.

The bot must not certify real-world authenticity.

## Advisory status awareness

When work defines or displays statuses, the bot may remind reviewers to check that statuses remain public-safe.

Acceptable status meanings include:

- `VERIFIED` as local/demo check completion only;
- `NEEDS_REVIEW` for warnings, ambiguity, or missing evidence;
- `REVIEW_REQUIRED` when human interpretation is required;
- `INVALID` for failed local checks;
- `UNKNOWN` when evidence is unavailable;
- `NOT_RUN` when a check was not executed.

`VERIFIED` must not mean objective truth, legal validity, security certification, or production readiness.

## Human-review escalation awareness

The bot may remind reviewers that human review is required when:

- evidence is missing;
- evidence conflicts;
- input is malformed;
- schema or shape checks fail;
- hash or provenance signals are missing or partial;
- replay or continuity risk is present;
- degraded runtime state is present;
- QR spoof risk is present;
- interpretation is consequential;
- legal, security, institutional, or real-world impact is implied;
- a user asks whether the result proves truth.

The bot may surface this as a checklist. It must not decide final sufficiency.

## Safe routing suggestions

If future routing support is enabled through a separate governance-approved PR, the bot may suggest product-surface review areas such as:

- Public Validator review;
- runtime contract review;
- demo explorer review;
- QR/hash/provenance review;
- public-safe language review;
- human-review escalation review;
- example input review.

These suggestions must remain advisory and human-controlled.

## Non-goals

This awareness layer does not authorize:

- hosted public validator backend;
- runtime implementation changes;
- schema changes;
- validator changes;
- signing changes;
- federation changes;
- generated QR/hash artifact changes;
- comment automation;
- label automation;
- assignment automation;
- GitHub App behavior;
- LLM memory behavior;
- production-readiness claims;
- legal certification;
- security certification;
- forensic certification;
- objective truth guarantees;
- autonomous decisions.

## Relationship to completed bot boundary work

This document extends the completed HC Control Bot boundary set by adding product-surface awareness.

It must be read together with:

- `docs/project-control/hc-control-bot-advanced-boundary-completion.md`;
- `docs/project-control/hc-control-bot-report-interpretation-guide.md`;
- `docs/project-control/hc-control-bot-advisory-comment-boundary.md`;
- `docs/project-control/hc-control-bot-evidence-prompt-boundary.md`;
- `docs/project-control/hc-control-bot-issue-routing-boundary.md`;
- `docs/project-control/hc-control-bot-github-app-boundary.md`;
- `docs/project-control/hc-control-bot-llm-memory-boundary.md`.

## Boundary

HC Control Bot may help humans notice product-facing verification concerns.

It must remain advisory-only.

Repository evidence, CI, governance, and human maintainers remain authoritative.

Human final authority remains unchanged.
