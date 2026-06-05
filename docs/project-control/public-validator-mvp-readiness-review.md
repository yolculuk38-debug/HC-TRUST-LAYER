# Public Validator MVP Readiness Review

> **Mode:** REPORT ONLY  
> **Scope:** Public Validator MVP readiness, current record-to-result user path, runtime/API/CLI verification surfaces, schema/hash/advisory response capability, public-safe boundaries, and human-review requirements.  
> **Decision:** PUBLIC VALIDATOR MVP CONDITIONALLY READY

## Executive Summary

A new user can reach a verification result today, but the shortest path is not yet a single polished Public Validator MVP journey. The repository already contains the main ingredients for a narrow, public-safe, advisory validator path: README orientation, START_HERE onboarding, the Mini Public Validator Demo, runtime `GET /verify/{record_id}` and `POST /verify/{record_id}` routes, CLI package verification helpers, public validator proof helpers, public validator API payload helpers, schema references, example records/packages, hash helpers, and runtime response tests that preserve runtime advisory/public-safe response flags. The helper/API response surfaces still need explicit MVP contract alignment before they can be treated as sufficient public validator result shapes.

The shortest current path is:

```text
README.md
→ docs/demo/mini-public-validator-demo.md
→ choose a demo/example record or package
→ run an existing CLI/API/runtime helper locally
→ read an advisory public-safe result
→ escalate ambiguous or consequential interpretation to human review
```

That path is usable for reviewers and contributors, but it is still fragmented for a new public user. The repository has multiple verifier-related surfaces (`src/hc_runtime`, `src/hc_trust`, root-level public validator helpers, static demo docs, and examples) without one documentation-only MVP specification that says which input shape, command, endpoint, output fields, warnings, and human-review language form the official smallest public validator flow.

Final decision: **PUBLIC VALIDATOR MVP CONDITIONALLY READY**.

The condition is documentation and product-boundary clarity, not a request to modify runtime, validators, schemas, hashes, records, signing, federation, policy, workflows, QR artifacts, or generated artifacts in this PR. The next step should be #638, a documentation-only Public Validator MVP specification that reuses existing local-only pieces and either requires the MVP result shape to include `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and `human_review_required=true`, or documents that existing helper/API responses are not yet sufficient for the full public MVP contract. Human final authority must remain preserved.

## Existing Verification Capabilities

### Current validation flow

The current validation flow is advisory and evidence-oriented:

1. A user or test provides a record identifier, QR input, verification package, proof object, or evidence object.
2. Existing helpers inspect shape, schema-like requirements, content hash markers, canonical lookup status, replay/continuity warnings, risk indicators, or trust/passport fields depending on the surface used.
3. Output is formatted as a verification response, public validator decision, public runtime response, or CLI result.
4. The output must remain a review aid and must not be interpreted as production readiness, truth finality, legal certification, security certification, or autonomous authority.
5. Human review remains required for interpretation, escalation, and any consequential decision.

### Schema validation capability

Existing schema material includes record schemas, verification-result schemas, verification-package schemas, and signature schema references under `schema/`. These files define canonical record and package boundaries, but this review did not modify them. Current schema validation capability is reusable for an MVP only through existing documented or implemented checks; a Public Validator MVP should not invent new schema semantics or mutate protected schema files.

Root-level CLI support also calls package-shape and schema-hardening helpers for verification packages. That is useful for a local-only MVP path, but it needs clearer documentation before it becomes the first-click public path.

### Hash validation capability

Existing hash capability appears in several forms:

- record and package examples include hash or content-hash fields;
- schema references define hash-shaped fields;
- `src/hc_trust/hashing.py` provides SHA-256 helper behavior;
- the runtime QR flow can surface `hash_verified` when the QR input contains a hash marker or structured payload evidence;
- public validator proof checks can mark `invalid_content_hash` when supplied proof metadata says the content hash is invalid.

This is enough for a narrow MVP to explain and display hash-related signals, especially for local demo input. It is not enough to claim that every public record has a complete cryptographic chain, signed provenance, durable custody, or real-world truth validation.

### Advisory response capability

Advisory response capability is already present and test-covered for the runtime response contracts. Current runtime response expectations preserve:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `warnings` as a list
- visible `human_review_required` behavior when warnings or escalation conditions apply
- prototype/advisory runtime stage language

This is a strong foundation for a Public Validator MVP because the MVP can reuse runtime response semantics instead of creating a new authority model. This claim is limited to runtime response contracts; it does not yet apply to every public validator helper/API response shape.

### Public-safe response capability

The runtime public response contract explicitly distinguishes public-safe advisory output from production API guarantees. It documents current `GET /verify/{record_id}` and `POST /verify/{record_id}` differences and states that response fields are protected by tests but do not imply authentication, authorization, rate limiting, durable persistence, generic exception handling, or stable machine-readable warning codes.

A Public Validator MVP should keep this boundary visible on every user-facing result page or example output.

Public Validator helper/API gap: `src/public_verification_response.py::build_public_verification_response` and `src/public_validator_api.py::build_validator_api_response` can emit `VERIFIED` or `trusted` response shapes without also emitting `advisory_only`, `public_safe`, `truth_guarantee`, or `human_review_required`. Their current tests focus on status/trusted/portable behavior rather than the full runtime advisory/public-safe posture. Therefore those helper/API responses should be treated as reusable adjacent surfaces, not as sufficient full public MVP contract outputs until #638 resolves the result-shape boundary.

### Human-review capability

Human review is already a repository-wide governance boundary. Runtime responses, demo docs, project-control docs, and governance docs preserve human-supervised validation and human final authority. The Public Validator MVP should make the human-review checkpoint explicit in the user journey rather than hiding it behind a simple `VERIFIED` status.

## Existing Runtime Capabilities

### Runtime entry points

The current FastAPI runtime scaffold provides a minimal advisory runtime app with health and verification routes. The app description states that it is advisory-only, not production-ready, and not a truth guarantee.

Relevant runtime entry points are:

- `GET /health` for advisory runtime status;
- `GET /verify/{record_id}` for a lightweight advisory placeholder response;
- `POST /verify/{record_id}` for a QR-oriented advisory verification path;
- `GET /qr/{record_id}` for a QR-style public-safe response path;
- `GET /verify/{record_id}/history` for public-safe scoped event history;
- telemetry/queue surfaces used by tests and runtime review docs.

These are enough for an MVP demo or local preview, but they should not be presented as a stable hosted Public Validator API without a separate specification and review.

### API verification flow

There are two related API-like surfaces:

1. `src/hc_runtime` runtime routes return public-safe advisory runtime responses.
2. `src/hc_trust` API helpers build experimental verification responses from evidence and witness input.

The runtime contract notes that these response surfaces are related but not identical. A Public Validator MVP specification should choose one public-facing flow for the first MVP and describe other helpers as reusable internals or adjacent surfaces.

### Replay, continuity, degraded state, and abuse warnings

Recent runtime work already covered telemetry contract sufficiency, replay/continuity edge-case coverage, and conditional runtime stabilization. Current tests exercise replay warnings, degraded runtime state, continuity warnings, malformed input responses, QR spoof-risk signals, advisory rate-limit recommendations, and stable public-safe key order.

This supports an MVP that can show `NEEDS_REVIEW` / `REVIEW_REQUIRED` style states when signals are missing, stale, malformed, replay-like, degraded, or ambiguous. It does not support autonomous blocking, hidden enforcement, or production abuse-control claims.

## Existing Public Surfaces

### README and START_HERE

`README.md` is the healthiest current public entry point. It points new visitors to the Mini Public Validator Demo first and then to START_HERE for repository navigation. It also states what works today and what is not claimed.

`docs/START_HERE.md` provides role-based onboarding and current project identity. It helps a new reviewer find the active repository path, governance model, and project-control docs, but it is not a compact validator product flow.

### Mini Public Validator Demo

`docs/demo/mini-public-validator-demo.md` is the closest existing public explanation of the desired user journey. It presents:

```text
HC record
→ validation
→ hash/provenance checks where applicable
→ advisory result
→ human review reminder
```

It also includes the correct public-safe fields: `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true`. This should be reused as the narrative base for the MVP.

### Examples

The `examples/` directory includes demo records, verification result examples, API response examples, gateway response examples, and verification-package examples. These are useful as public-safe sample inputs and outputs, but they mix illustrative, experimental, and non-canonical examples. A Public Validator MVP should select one or two explicit demo-safe examples and label them as explanatory, not canonical proof.

### Existing verifier-related surfaces

Verifier-related surfaces already exist in multiple areas:

- `src/hc_runtime` for the reference runtime scaffold and route responses;
- `src/hc_trust` for CLI/API/trust helper logic;
- root-level `src/public_validator.py` and `src/public_validator_api.py` for public proof/API helper shapes;
- `src/verification_cli.py` for local package verification and provenance scan commands;
- `src/public_verification_response.py` for stable public response shaping, with the current limitation that it does not emit the full advisory/public-safe posture fields;
- tests under `tests/` and `tests/runtime/` that exercise these surfaces.

The MVP should reuse these surfaces in a narrow path instead of adding a new backend or broad architecture.

## Current User Journey

### Shortest path from a record to a verification result today

For a new user arriving today, the shortest public-safe path is documentation-led and local-first:

1. Open `README.md`.
2. Follow `What Works Today` to `docs/demo/mini-public-validator-demo.md`.
3. Read the quick flow and demo result shape.
4. Use a demo/example record or package from `examples/`.
5. Run an existing local helper or runtime route in a development environment.
6. Interpret the output as advisory-only, public-safe, and not a truth guarantee.
7. Escalate any missing, ambiguous, disputed, high-impact, replay, degraded, or malformed result to human review.

### What a user can verify today

A user can currently verify or inspect:

- whether a demo or package-shaped input has expected required fields through existing helper checks;
- whether a proof object reports a valid or invalid content-hash signal through the public validator helper;
- whether QR-like runtime input produces advisory `schema_valid`, `hash_verified`, replay, continuity, degraded, QR-risk, and human-review signals;
- whether an API-like response shape matches expected experimental fields;
- whether runtime response flags preserve advisory-only and public-safe semantics;
- whether examples and docs describe a record-to-result pathway.

### What a user cannot verify today

A user cannot currently verify, through a single polished public MVP path:

- objective truth of record contents;
- legal certification or institutional finality;
- security certification;
- production readiness;
- signed-chain custody across all examples;
- live federation state;
- durable backend persistence;
- authenticated or authorized user workflows;
- complete public explorer search/index behavior;
- canonical hash provenance for every public input;
- autonomous tool authority or autonomous governance finality.

The MVP should state these non-goals prominently.

## Smallest Viable Public Validator

The smallest viable Public Validator should be a **documentation-defined, local-only, public-safe record-to-result path** that reuses existing components and avoids backend expansion.

### MVP decision

The smallest viable MVP is conditionally ready if it is scoped as:

```text
Public-safe demo/example input
→ local schema/shape check using existing helpers
→ local hash/provenance signal display where available
→ public-safe advisory response
→ human-review checkpoint
```

### MVP user journey

1. User opens the Public Validator MVP page.
2. User chooses one of two safe paths:
   - paste or load a demo-safe HC:// record/proof/package locally; or
   - use a bundled example from `examples/`.
3. The page or command shows which checks are run and which checks are not run.
4. The result displays:
   - record identifier;
   - schema/shape status;
   - hash/provenance status where available;
   - advisory status such as `VERIFIED`, `NEEDS_REVIEW`, `REVIEW_REQUIRED`, `INVALID`, `UNKNOWN`, or `NOT_RUN`;
   - warnings;
   - `advisory_only=true`;
   - `public_safe=true`;
   - `truth_guarantee=false`;
   - `human_review_required` when appropriate;
   - plain-language next steps.
5. User is reminded that human final authority controls interpretation.

### Required components

The MVP specification should require:

- one canonical MVP documentation page;
- one explicit demo input shape;
- one explicit local verification command or runtime path;
- one result shape;
- public-safe warning language;
- clear status definitions;
- human-review escalation rules;
- local-only processing guidance where possible;
- explicit non-goals and deferred components;
- compatibility notes for existing runtime/API/CLI response surfaces.

### Optional components

Optional components that can be included only if they reuse existing files and stay documentation-only:

- a compact mobile-readable flow diagram;
- a table mapping existing helper modules to MVP responsibilities;
- links to examples that are safe for public explanation;
- a manual checklist for reviewers;
- a future HC:// Control Panel alignment note.

### Components that should be deferred

Defer all of the following:

- hosted public backend;
- authentication or accounts;
- authorization model;
- durable database persistence;
- Redis, queue, or rate-limit enforcement;
- CAPTCHA or web application firewall behavior;
- new schema versions;
- signing or federation expansion;
- policy changes;
- canonical record changes;
- generated QR or hash artifact changes;
- autonomous tool judgement;
- trust scoring product claims;
- legal/security certification language;
- production-readiness claims;
- broad explorer/index architecture.

## What Already Exists

The following can be reused:

- README `What Works Today` orientation.
- START_HERE onboarding.
- Mini Public Validator Demo narrative and result shape.
- Runtime public response contract.
- Runtime advisory `GET /verify/{record_id}` and QR-oriented `POST /verify/{record_id}` surfaces.
- Runtime history and telemetry visibility for review contexts.
- Runtime public-safe response builders and response-contract tests.
- Public validator proof helper, as an adjacent reusable surface that still needs MVP result-shape alignment.
- Public validator API payload helper, as an adjacent reusable surface that still needs MVP result-shape alignment.
- CLI package verification and provenance scan helper.
- Schema references for records, verification results, verification packages, and signatures.
- Example records/packages/API responses for public-safe explanation.
- Runtime tests and response-contract tests that preserve advisory/public-safe boundaries.
- Governance and ethics docs preserving human-supervised validation.

## What Is Missing

The repository is missing:

- a single Public Validator MVP specification;
- one official MVP input type and example;
- one official first-click local command or endpoint path;
- a public-safe status taxonomy aligned across demo/runtime/helper surfaces;
- a single result shape that maps demo fields to runtime/helper output fields;
- explicit handling of the Public Validator helper/API response gap where helper outputs can be `VERIFIED` or `trusted` without `advisory_only`, `public_safe`, `truth_guarantee`, or `human_review_required`;
- explicit guidance on when `human_review_required` must be true;
- a new-user walkthrough that starts at a record and ends at a result in one page;
- a boundary table explaining which checks are real, partial, unknown, or not run;
- clear reuse guidance for `src/hc_runtime`, `src/hc_trust`, and root-level public validator helpers;
- explicit non-goals for backend, signing, federation, policy, security, legal, and production claims.

These gaps can be closed in a documentation-only #638 PR before any runtime or validator implementation change is considered.

## What Must Be Deferred

The Public Validator MVP should not build or change:

- runtime code;
- validators;
- tests;
- schemas;
- canonical records;
- hashes;
- QR artifacts;
- generated artifacts;
- signing logic;
- federation logic;
- policy files;
- workflows;
- governance rules;
- security gates;
- trust-kernel boundaries.

It should also avoid product language that implies production readiness, truth finality, autonomous tool authority, legal certification, security certification, live federation guarantees, or forensic certainty.

## Risk Assessment

### Runtime risks

Risk level: **Medium if the MVP is presented as a live public service; Low if it remains documentation-defined and local-only.**

Current runtime output is prototype/advisory and public-safe, but it does not guarantee authentication, authorization, durable persistence, rate limiting, generic exception contracts, or hosted availability. A hosted Public Validator would require separate architecture, threat-model, abuse-control, privacy, persistence, deployment, and operations review. The MVP should therefore remain local-first and documentation-defined.

### Security risks

Risk level: **Medium.**

Public validator UX can invite arbitrary inputs, malformed payloads, repeated probing, QR spoof attempts, and over-trust in simplified status labels. Existing runtime docs and tests already preserve public-safe warning behavior and advisory rate-limit language, but they do not implement infrastructure enforcement. The MVP must avoid accepting secrets, echoing private payloads, or implying autonomous blocking/security certification.

### Backward compatibility risks

Risk level: **Medium for response-shape confusion; Low for this report-only PR.**

There are multiple response surfaces: runtime route responses, `hc_trust` API helpers, public validator proof responses, public validator API payloads, CLI results, and static demo result shapes. Runtime response contracts preserve the full advisory/public-safe posture fields, but current Public Validator helper/API responses do not necessarily emit those fields. A future MVP spec must choose and document one public-facing result shape without silently redefining existing contracts. Any future field changes should be separately reviewed and tested.

### Governance and trust-kernel risks

Risk level: **Low for documentation-only planning; High if implementation changes touch protected paths without review.**

Schema, signing, federation, policy, records, generated artifacts, hashes, workflows, governance rules, and validator logic are trust-kernel-adjacent or protected. The MVP should reuse existing capabilities and preserve human-supervised validation rather than changing protected semantics.

## Final Recommendation

Decision: **PUBLIC VALIDATOR MVP CONDITIONALLY READY**.

HC-TRUST-LAYER is ready to move from documentation/runtime hardening into a visible Public Validator MVP planning phase, provided the next step is documentation-only and tightly scoped. The repository already has enough advisory runtime, helper, schema, hash-signal, example, and public-safe response material to define the smallest possible user journey. However, the full advisory/public-safe posture is currently preserved by runtime response contracts, not by every reusable Public Validator helper/API response. It is not ready for a hosted production validator, new backend, schema mutation, signing/federation expansion, or authoritative trust product claims.

The acceptable MVP posture is:

- advisory_only preserved;
- public_safe preserved;
- truth_guarantee=false preserved;
- human_review_required visible where appropriate;
- human final authority preserved;
- local-only processing preferred;
- no backend unless explicitly reviewed later;
- no production, legal, security, forensic, federation, or autonomous authority claims.

## Recommended Next PR

Open **#638 Public Validator MVP specification (documentation-only)**.

Recommended scope for #638:

1. Add a documentation-only Public Validator MVP specification.
2. Define the smallest record-to-result user path.
3. Select one demo-safe input example.
4. Define one public-safe result shape.
5. Map existing reusable components to MVP responsibilities.
6. Define `VERIFIED`, `NEEDS_REVIEW` / `REVIEW_REQUIRED`, `INVALID`, `UNKNOWN`, and `NOT_RUN` language carefully.
7. Either require the MVP public validator result shape to include `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and `human_review_required=true`, or document that existing helper/API responses are not yet sufficient for the full public MVP contract.
8. Preserve human final authority.
9. Defer backend, schema, validator, runtime, tests, signing, federation, policy, workflow, record, hash, QR, generated-artifact, and governance-rule changes.

Do not implement the MVP in #638. Keep it small, scoped, mobile-readable, local-first, and reversible.
