# HC-TRUST-LAYER Repository Map

This current repository map is an advisory classification layer for HC-TRUST-LAYER. HC-TRUST-LAYER is an early-stage, advisory, human-supervised verification infrastructure project for HC:// records, review boundaries, and evidence-preserving workflows.

The repository is not a single simple library. It contains core runtime and CLI surfaces, schemas and verification contracts, records and audit/provenance examples, public verification and demo documentation, governance and contribution policy documentation, GitHub Actions and control-bot automation, project-control planning documents, experimental or future-facing surfaces, and generated or canonical artifacts where applicable.

This map does not finalize all boundaries. If a path's role is unclear, treat it as **needs maintainer confirmation** before using it as canonical, operational, or implementation authority.

## HC boundary

The following boundaries apply to this map and to repository interpretation unless a more specific, human-reviewed document says otherwise:

- `advisory_only=true` where applicable.
- `public_safe=true` where applicable.
- `truth_guarantee=false`.
- `human_review_required=true`.
- CI/checks are evidence, not trust authority.
- Humans remain the final maintainers and review authority.

HC-TRUST-LAYER documentation, checks, demos, records, and automation must not be treated as legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, or guaranteed correctness.

## Current repository map

| Path / area | Role | Status | Ownership expectation | Human review sensitivity |
|---|---|---|---|---|
| `src/` | Core runtime and library surfaces for HC-TRUST-LAYER tooling. | core | Runtime maintainers; needs implementation review. | High: runtime behavior can affect verification semantics. |
| `scripts/` | Checks, report generators, validation helpers, local demo runners, and bounded maintenance utilities. | automation/report-only | Maintainers and contributors may update scoped helpers. | Medium to high: scripts can produce evidence, but are not trust authority. |
| `.github/` | GitHub Actions, control-bot wiring, issue/PR automation, and repository automation configuration. | automation/report-only | Maintainers only unless explicitly authorized. | High: automation may influence review flow, but does not grant approval authority. |
| `schema/` | Record schema definitions and verification contracts. | schema/contract | Schema maintainers; changes need explicit justification. | Very high: canonical/protected surface. |
| `records/` | Evidence-bearing examples, verified records, archived records, pending records, and audit/provenance material. | audit/provenance record | Maintainers must preserve historical evidence and audit continuity. | Very high: historical evidence surface; avoid mutation unless explicitly authorized. |
| `docs/` | Architecture, onboarding, governance references, demos, planning notes, and explanatory material. | documentation/onboarding | Contributors may make small scoped documentation changes. | Varies by subarea; governance, security, and canonical references need extra care. |
| `docs/governance/` | Governance procedures, review expectations, migration notes, and maintainer decision references. | governance | Maintainers and governance reviewers. | High: may affect interpretation of authority boundaries. |
| `docs/project-control/` | Planning, handoff, task ledger, active work registry, and operating-layer coordination. | project-control | Maintainers and operators; report-only unless otherwise stated. | Medium: coordinates work but does not replace human review. |
| `docs/demo/`, `docs/public/`, `docs/explorer/` | Public verification, explorer, and demo guidance. | documentation/onboarding | Documentation and demo maintainers. | Medium: must preserve advisory-only and public-safe language. |
| `docs/future/`, `docs/vision/`, `docs/drafts/` | Future-facing, research, and draft concepts. | experimental/research | Maintainers and researchers; not canonical unless promoted through review. | Medium: avoid treating concepts as implemented guarantees. |
| `docs/runtime/`, `docs/spec/`, `docs/verification/`, `docs/architecture/`, `docs/core/` | Runtime, specification, verification, architecture, and core explanatory references. | schema/contract | Maintainers; needs maintainer confirmation where authority is unclear. | High when used to interpret verification behavior or canonical boundaries. |
| `policy/` | Policy and governance-control material. | governance | Maintainers; protected unless explicitly allowed. | Very high: protected surface. |
| `federation/` | Federation-related references or implementation surfaces. | experimental/research | Maintainers; needs explicit authorization for changes. | High: future federation behavior can affect trust boundaries. |
| `signatures/`, `records/signatures/` | Signature-related evidence or signing references where present. | generated/canonical | Maintainers; protected unless explicitly allowed. | Very high: can affect signing expectations or evidence continuity. |
| `hash/` | Hash references and integrity artifacts. | generated/canonical | Maintainers; protected unless explicitly allowed. | Very high: canonical linkage and integrity evidence. |
| `qr/` | QR-related verification artifacts and references. | generated/canonical | Maintainers; protected unless explicitly allowed. | High: QR paths can affect verification interpretation. |
| `generated/` | Generated indexes, exports, or derived artifacts. | generated/canonical | Maintainers and generation process owners. | Very high: do not hand-edit unless explicitly authorized. |
| `canonical/` | Canonical artifacts where present. | generated/canonical | Maintainers; protected unless explicitly allowed. | Very high: canonical/protected surface. |
| `tests/` | Test suites and fixtures. | core | Runtime and validation maintainers. | Medium to high: tests are evidence of behavior, not trust authority. |
| `examples/` | Example packages, demonstrations, and contributor-facing examples. | documentation/onboarding | Contributors and maintainers. | Medium: examples must not imply production readiness or guaranteed correctness. |
| `exports/` | Exported or derived examples and release-support material. | generated/canonical | Maintainers; needs maintainer confirmation before mutation. | High: may be generated or evidence-adjacent. |
| `tools/` | Developer tooling and documentation helpers. | automation/report-only | Maintainers and contributors for scoped helpers. | Medium: tooling assists review but does not approve changes. |
| `agents/` | Agent-facing operating material. | project-control | Maintainers and agent-ops reviewers. | Medium: advisory instructions must preserve human final authority. |
| `hc_context/` | Context material for HC workflows. | project-control | Maintainers; needs maintainer confirmation where role is unclear. | Medium: context can guide work but is not canonical by default. |
| `council/`, `reviewers/`, `witness/`, `timeline/`, `halkalar/` | Governance, reviewer, witness, timeline, and legacy/historical evidence surfaces. | audit/provenance record | Maintainers; preserve provenance and historical context. | High: historical evidence surfaces; avoid silent rewrites. |
| `media/` | Media assets and public-facing support material. | documentation/onboarding | Documentation maintainers; needs maintainer confirmation where provenance matters. | Low to medium, unless evidence-bearing. |
| Root governance files such as `README.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md`, `CODEOWNERS`, and `AGENTS.md` | Entry points, policy, security, ownership, and contributor/agent rules. | governance | Maintainers and designated reviewers. | High: may affect repository authority and review interpretation. |
| Root canonical references such as `trust-kernel-index.json`, `verification-map.json`, and `protocol-graph.json` where present | Navigation and trust-kernel reference artifacts. | generated/canonical | Maintainers; needs explicit review and justification. | Very high: canonical/protected interpretation surface. |

## Boundary distinctions

- **Canonical / protected surfaces:** schemas, policy, federation, signatures, hash, QR, generated/canonical artifacts, trust-kernel references, and other protected paths require explicit human review and should not be modified opportunistically.
- **Advisory/report-only surfaces:** checks, scripts, control-bot reports, demos, and project-control coordination can provide evidence, but they do not approve changes or establish truth authority.
- **Experimental/research surfaces:** future, vision, draft, explorer, federation-planning, and research documents describe possible directions unless separately implemented and reviewed.
- **Historical evidence surfaces:** records, archived materials, witness/timeline material, legacy names, and provenance examples preserve audit history and should not be silently rewritten.

## How to use this map

- **New contributor:** start with `README.md`, `docs/START_HERE.md`, then this repository map.
- **Maintainer:** use this map to classify PR risk, identify protected or evidence-bearing paths, and decide when additional review is required.
- **AI-assisted reviewer:** use this map to avoid treating experimental docs as canonical, report-only automation as approval authority, or generated/canonical artifacts as safe hand-edit targets.

## Non-goals

This documentation-only classification does not perform or authorize:

- File moves.
- Namespace refactors.
- Package splits.
- Governance authority changes.
- Generated or canonical artifact changes.

## Follow-up work

Deeper refactors may be considered separately after maintainer review. Possible follow-up work includes core namespace split, workflow taxonomy, test taxonomy, governance canonical split, and clearer promotion paths for draft or research material. Those follow-ups are outside this docs-only PR.
