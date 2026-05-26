# HC Control Panel — Current Project State

> **Documentation Status**
> - **status:** PARTIAL
> - **scope:** Operator-facing status snapshot for HC-TRUST-LAYER documentation and guardrail posture.
> - **canonical relevance:** Advisory only; references canonical record boundaries but is not a canonical record surface.
> - **runtime relevance:** Medium for operations alignment; does not alter validator or trust-kernel runtime behavior.

## Purpose

This file is the repo-native control panel for HC-TRUST-LAYER.

It is designed to help maintainers, ChatGPT, Codex, and future contributors understand the current state without relying on scattered chat memory or outdated assumptions.

This document is advisory and documentation-only. It does not change schemas, validators, workflows, runtime behavior, or trust-kernel semantics.

## Public demo entry point

For public-facing, low-friction verification onboarding, use:

- **Try local verification preview:** `docs/self-service-verify.html`
- **No upload**
- **Browser-side SHA-256**
- **Preview only, not registration**

This entry point is mobile-friendly, browser-side, and advisory-only before human-supervised validation.


## Public visual verification examples

For standardized, static HC:// visual verification signal examples for public UX, see:

- `docs/visual-verification-signals.md`

## Project Identity

- Canonical repository: `HC-TRUST-LAYER`
- Protocol surface: `HC://`
- Project type: verification and provenance infrastructure
- Core posture: integrity, provenance, audit trail, and human-supervised validation
- Motto: `Trust the record, not the narrative.`
- Turkish motto: `Beyan değil, kayıt esastır.`

## Current Strategy

Development proceeds in this order:

1. Stabilize the working core.
2. Preserve canonical validation boundaries.
3. Harden QR and viewer flows.
4. Expand explorer visibility.
5. Improve immutable audit snapshots.
6. Prepare federation and external verification packages.
7. Move toward public trust-layer interoperability.

The project must not jump into broad ecosystem claims before the core verification pipeline remains stable, reproducible, and reviewable.

## Current PR State Anchor

As of the latest control-panel update:

| PR | State | Meaning |
|---|---|---|
| #359 | Merged | First demo record was aligned with the canonical schema. |
| #360 | Merged | Minimal QR verification landing page was added. |
| #361 | Merged | Immutable audit snapshot foundation was added. |
| #362 | Merged | Lightweight verification explorer index foundation was added. |

Earlier relevant foundations:

| PR | State | Meaning |
|---|---|---|
| #252 | Merged | Generated explorer/index artifacts are skipped by hash validation. |
| #278 | Merged | Canonical artifact guard was added. |
| #300 | Merged | Trust-kernel stabilization checkpoint was documented. |
| #312–#317 | Merged | Agent, protocol graph, verification map, and trust-kernel indexes were added. |
| #324–#357 | Merged | MVP viewer, trust UX, terminology, repair, and guard workflows were expanded. |

## Canonical Record Paths

Only these paths are canonical record locations:

- `records/pending/*.json`
- `records/verified/*.json`
- `records/archived/*.json`

Canonical records are the strict validation surface.

## Generated Artifact Boundary

Generated or derived artifacts must not be treated as canonical records.

Examples of non-canonical artifacts:

- `generated/**`
- `records/explorer_index.json`
- `generated/explorer_index.json`
- `generated/audit_snapshot.json`
- index files
- manifest files
- cache files
- export artifacts
- verification packages outside canonical record paths

These may support visibility, audit, viewer, export, or federation workflows, but they do not replace canonical records.

## Active Guardrail Baseline

The repository currently uses guardrails including:

- schema validation
- SHA-256 record hash verification
- terminology guard
- documentation drift guard
- canonical artifact guard
- advisory PR scope guard
- advisory policy evaluation
- verification package validation helpers
- PR self-audit template
- issue templates
- workflow security hardening

Guardrails must not be weakened to make a PR pass.

## Do Not Break Rules

The following rules are mandatory unless a PR explicitly scopes, documents, and receives human-supervised validation for a change:

- Do not modify canonical schema casually.
- Do not weaken validators.
- Do not weaken guard scripts or guard workflows.
- Do not treat generated artifacts as canonical records.
- Do not add blockchain, token, or economic-token claims.
- Do not add truth-guarantee, objective-certainty, or autonomous-authority claims.
- Do not imply production readiness unless backed by repository evidence.
- Preserve advisory-only verification language.
- Preserve human-supervised validation.
- Keep changes small, auditable, and reversible.

## Current Implemented / Partial Layers

Current repo evidence indicates:

- Record integrity: implemented baseline.
- Public verification: implemented baseline.
- QR verification: implemented baseline with demo landing flow.
- Explorer/index visibility: partial and expanding.
- Immutable audit snapshots: foundation added.
- Witness/signature: partial.
- Federation/sync: planned/partial foundation.
- Governance/dispute: planned/partial foundation.
- External integrations: research/planned foundation.

For detailed status, use:

- `docs/capability-status.md`
- `docs/implementation-map.md`
- `docs/master-architecture.md`
- `docs/federated-oversight-model.md`
- `protocol-graph.json`
- `verification-map.json`
- `trust-kernel-index.json`
- `docs/public-verification-disputes.md`
- `docs/maintainer-accountability-model.md`

## Status Visibility Summary

### Implemented systems
- Record integrity verification baseline.
- Public verification baseline (CLI/API and verification output pathways), including static-site client-side continuity diagnostics for the first public HC:// flow.
- QR verification baseline for demo/operator flow.

### Experimental systems (partial)
- Witness/signature and revocation-related expansion.
- Explorer/index visibility and trust scoring foundations.
- Immutable audit snapshot foundation and related review tooling.

### Conceptual future layers (planned/research)
- Federation and sync interoperability rollout semantics.
- External ecosystem integrations and institutional adapters.
- Long-horizon governance/dispute automation expansion.

## Mobile PR Merge Operations Baseline

HC-TRUST-LAYER merge operations on mobile should follow a clear precedence order:

1. Required checks on latest SHA
2. Mergeable PR state
3. Resolved review conversations
4. Safe Auto Merge job status interpretation

Operational clarification:

- A cancelled Safe Auto Merge job is not automatically a code failure.
- Duplicate/concurrency cancellation can occur while newer valid runs succeed.
- Successful required checks on latest SHA are the primary merge signal.
- Unresolved review conversations remain a hard merge blocker until resolved.
- Manual **Merge pull request** is acceptable when mergeable state and required checks are satisfied and review conversations are resolved.

Reference guide: `docs/mobile-pr-merge-guide.md`.

## Safe Next Direction

After PR #362, the safest next direction is not to add a large new runtime system.

Recommended next steps:

1. Stabilize the control panel and state anchor.
2. Verify generated explorer and audit artifacts remain non-canonical.
3. Add small tests or documentation for explorer/audit artifact expectations if missing.
4. Improve public viewer routing only after the validation pipeline stays green.
5. Continue federation work only through bounded, documented, human-supervised increments.

## New Chat / New Agent Usage

When a new AI conversation or Codex task starts, read this file first together with:

- `AGENTS.md`
- `ROADMAP.md`
- `docs/capability-status.md`
- `docs/implementation-map.md`

This prevents mixing old chat context with current repository state.

## Status Meaning

This file is a control panel, not a marketing page.

It summarizes current repository state and next safe direction. Repository evidence remains authoritative.

For explicit public verification limits and advisory-only boundary language, use `docs/public-verification-boundaries.md` alongside this control panel.

For federation interoperability boundaries and verification package scope, see `docs/federation-readiness-model.md`.

See `docs/qr-verification-security-model.md` for permission-aware HC:// QR entry constraints, spoofing risks, and advisory trust-boundary handling.

For advisory verification badge semantics and visible trust-signal boundaries, see `docs/verification-signal-model.md`.
For standardized self-service public-facing verification result states and advisory signal language, see `docs/verification-result-states.md`.

For anti-spoof visible verification signal stabilization guidance, see `docs/anti-spoof-verification-signals.md`.
For immutable-style state history, tamper trace visibility, and continuity divergence guidance, see `docs/immutable-state-history-model.md`.

For verified AI-assisted analysis disclosure boundaries, validator trace expectations, and anti-spoof AI-claim guidance, see `docs/verified-ai-validator-model.md`.

For authenticated AI validator access boundaries, signed token and challenge expectations, and replay-resistant advisory access states, see `docs/authenticated-ai-validator-access.md`.

For advisory content verification signal design across quotes/text, images, videos, documents, social posts, and archived records, see `docs/content-verification-signal-model.md`.

For the mobile-readable self-service local hashing prototype, use the public entry point **Try local verification preview** at `docs/self-service-verify.html` (**No upload**, **Browser-side SHA-256**, **Preview only, not registration**).

For lightweight public onboarding flow guidance for normal users (QR scan through advisory interpretation with human-supervised validation notice), see `docs/public-onboarding-model.md`.

For first public self-service local hash preview flow guidance (text/file input through advisory preview, with registration/review separated), see `docs/public-self-service-verification-flow.md`.

For a repeatable manual mobile/desktop UX verification checklist for the prototype, see `docs/self-service-smoke-test.md`.

For a start-to-finish normal-user walkthrough of the public self-service prototype flow, see `docs/public-verification-walkthrough.md`.

For the first browser-side self-service verification prototype page (local-only SHA-256 preview and non-canonical HC:// route preview), see `docs/self-service-verify.html`.
## Accountability and defense layer reference

For HC:// trust integrity abuse and anti-manipulation posture guidance, see:

- `docs/accountability-defense-layer.md`
- `docs/public-verification-disputes.md`
- `docs/maintainer-accountability-model.md`

For evidence preservation, continuity gap visibility, and trace reconstruction guidance, see `docs/evidence-preservation-recovery-model.md`.

For multi-layer consensus visibility, disagreement escalation, and conflict preservation guidance, see `docs/multi-layer-consensus-model.md`.

