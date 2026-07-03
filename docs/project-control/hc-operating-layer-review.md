# HC Operating Layer Review

> **PR:** #631  
> **Mode:** REPORT ONLY  
> **Scope:** Repository usability, onboarding, and AI/human agent guidance after runtime stabilization.  
> **Decision:** OPERATING LAYER CONDITIONALLY SUFFICIENT

## Executive Summary

The HC-TRUST-LAYER operating layer is conditionally sufficient for a new human contributor, external reviewer, maintainer, security reviewer, release reviewer, or AI-assisted agent to enter the repository and understand the project purpose, advisory-only posture, human-supervised authority model, and protected trust-kernel boundaries.

The repository has strong onboarding anchors:

- `README.md` explains HC-TRUST-LAYER as early-stage HC:// verification infrastructure and avoids production, forensic-certainty, truth-finality, and autonomous-finality claims.
- `docs/START_HERE.md` provides the clearest role-based entry path and explicitly lists protected areas, evidence-bearing material, current v0.1.0 status, checks, and safe contribution types.
- `AGENTS.md` establishes repository-wide agent and contributor rules.
- `HC_BOOTSTRAP.md` provides an operational startup sequence, shift-ledger model, check-in / checkout expectations, and source-of-truth discipline.
- `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`, governance docs, runtime review docs, and project-control docs provide enough supporting context for scoped work.

The main weakness is navigation consistency. The repository contains many valid but overlapping documentation surfaces. Some operating-layer files point contributors toward the right concepts, but the current phase and next-task state are not fully synchronized with the most recent runtime stabilization sequence noted for this review: #628 telemetry contract review, #629 replay / continuity edge-case coverage, and #630 runtime stabilization review. A new contributor can still orient safely, but may need to reconcile `README.md`, `docs/START_HERE.md`, `HC_BOOTSTRAP.md`, `docs/project-control/project-state.md`, `docs/project-control/next-actions.md`, runtime reports, governance reports, and historical evidence files manually.

No runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy files were modified for this review.

## Current Operating Layer Inventory

### Primary entry points

| Surface | Role in onboarding | Assessment |
| --- | --- | --- |
| `README.md` | Public repository overview, project purpose, MVP snapshot, demo links, architecture and contribution navigation. | Strong high-level entry point. It clearly frames the project as early-stage advisory verification infrastructure and provides many navigation links. |
| `docs/START_HERE.md` | Role-based onboarding guide for contributors, maintainers, AI agents, security reviewers, and external reviewers. | Strongest single entry point. It answers most first-hour onboarding questions. |
| `AGENTS.md` | Repository-wide agent and contributor rules. | Effective and concise. It preserves HC:// terminology, evidence preservation, protected-path awareness, and advisory-only agent behavior. |
| `HC_BOOTSTRAP.md` | Operational startup sequence and shift-ledger handoff protocol. | Effective for agents and maintainers, especially for check-in / checkout discipline and source-of-truth ordering. |
| `CONTRIBUTING.md` | Contribution workflow, validation expectations, protected paths, and PR discipline. | Useful contributor path; should remain paired with `docs/START_HERE.md`. |
| `SECURITY.md` | Public/private security reporting boundaries and human oversight requirements. | Clear security reviewer entry point and preserves sensitive disclosure boundaries. |
| `CODEOWNERS` | Protected ownership baseline. | Strong discoverability for protected protocol/runtime/security boundaries. |
| `.github/pull_request_template.md` | PR self-audit and validation checklist. | Strong guardrail against terminology drift, truth-guarantee claims, AI-authority claims, and schema/validator/generated-artifact drift. |

### Supporting operating-layer documents

| Surface | Role in onboarding | Assessment |
| --- | --- | --- |
| `docs/project-control/project-state.md` | Current project phase and shift handoff summary. | Useful but appears stale relative to the recent #628-#630 runtime stabilization context. |
| `docs/project-control/next-actions.md` | Safe next work queue. | Useful but appears stale relative to the requested #631 operating-layer review. |
| `docs/project-control/agent-operating-model.md` | AI/human role boundaries, scope categories, validation boundaries. | Strong for AI-assisted work. |
| `docs/project-control/authority-model.md` | Authority boundaries and human final decision model. | Strong support for preserving human final authority. |
| `docs/project-control/trust-kernel-boundary.md` | Trust-kernel and trust-kernel-adjacent classification. | Strong protected-surface explanation, especially for AI agents. |
| `docs/governance/` | Governance decisions, historical migration handling, release evidence, preflight, rollback, and review process. | Comprehensive but dense; needs stronger index/routing for new readers. |
| `docs/runtime/` | Runtime stabilization, telemetry, contract, configuration, persistence, and production-risk notes. | Valuable post-stabilization evidence, but readers need a short route from onboarding files to the latest runtime status sequence. |
| `docs/index.md` | Documentation index. | Useful, but the repository would benefit from stronger prominence and role-based grouping across top-level onboarding files. |

## Human Contributor Onboarding Review

Human contributor onboarding is conditionally sufficient.

A first-time contributor can determine:

- what HC-TRUST-LAYER is: early-stage HC:// verification infrastructure for provenance visibility, audit consistency, and human-supervised validation;
- where to start: `docs/START_HERE.md`, `README.md`, `CONTRIBUTING.md`, and `docs/contributor-start-here.md`;
- safe first tasks: documentation fixes, broken links, typo corrections, clarifying examples, and small non-protected documentation improvements;
- what must not be touched without explicit approval: trust-kernel, protected runtime/security/governance, record, hash, QR, generated, signing, federation, policy, schema, validator, and workflow paths;
- how to validate documentation-only changes: terminology, docs drift, canonical artifact checks, and `git diff --check`.

Strengths:

- The first-time contributor path in `docs/START_HERE.md` is concrete and time-bounded.
- Protected and evidence-bearing files are named directly.
- The language repeatedly discourages truth-finality, production-readiness, and autonomous-authority claims.
- The PR template reinforces contribution discipline at the point of review.

Conditional gap:

- Contributors may encounter duplicate entry points (`README.md`, `docs/START_HERE.md`, `docs/contributor-start-here.md`, `CONTRIBUTING.md`, `docs/CONTRIBUTING.md`, `docs/developer-onboarding.md`) without a single canonical routing table explaining which one to use first for each role.

## AI Agent Onboarding Review

AI-agent onboarding is conditionally sufficient and generally strong.

AI agents are told to:

- inspect existing files first;
- preserve evidence and auditability;
- avoid speculative implementation;
- prefer report-only investigations before major or trust-kernel-adjacent changes;
- avoid production, forensic-certainty, truth-finality, live-federation, and autonomous-governance claims;
- treat agent output as advisory until validated by repository-defined checks and reviewer oversight;
- stop and report when protected paths, evidence gaps, or scope conflicts appear.

`HC_BOOTSTRAP.md` is especially useful because it requires a startup sequence, repository-state discipline, check-in, checkout, and evidence cross-checking. `docs/project-control/agent-operating-model.md` and `docs/project-control/trust-kernel-boundary.md` provide deeper classification guidance for protected, trust-kernel-sensitive, and trust-kernel-adjacent work.

Conditional gap:

- The AI-agent path depends on several separate documents. The guidance is safe, but fragmented. A small index/navigation PR could reduce the chance that an agent reads only one entry point and misses `HC_BOOTSTRAP.md`, `project-state.md`, `task-ledger.md`, or `next-actions.md`.

Risk:

- The risk of AI agents modifying wrong files is moderate without task-specific constraints, but current repository instructions, `docs/START_HERE.md`, `AGENTS.md`, `HC_BOOTSTRAP.md`, `CODEOWNERS`, and PR template checklists significantly reduce this risk when followed.

## Maintainer Review Path

Maintainer onboarding is conditionally sufficient.

Maintainers can find:

- merge authority and escalation context through governance files;
- daily operational support through `docs/governance/maintainer-daily-checklist.md`;
- project phase context through `docs/project-control/project-state.md`;
- release review material through `CHANGELOG.md`, `docs/v0.1.0-release-notes.md`, and `docs/governance/v0.1.0-*` readiness/signoff reviews;
- protected ownership routing through `CODEOWNERS`;
- review self-audit through `.github/pull_request_template.md`.

Strengths:

- The governance directory contains detailed review, release, rollback, migration, archive, hash, QR, generated-artifact, and release-evidence material.
- The project-control directory contains explicit authority and validation models.
- CODEOWNERS maps protected areas to the repository owner.

Conditional gap:

- Maintainer guidance is comprehensive but distributed. A maintainer can find the right files, but a new maintainer may need a shorter maintainer-specific index that distinguishes daily triage, release review, trust-kernel review, security review, and historical evidence review.

## Security / Trust-Kernel Discoverability

Security and trust-kernel discoverability is sufficient with minor navigation conditions.

Strong signals:

- `docs/START_HERE.md` defines the trust kernel and lists protected paths.
- `AGENTS.md` describes protected areas affecting record identity, provenance continuity, policy interpretation, signing expectations, federation behavior, validation semantics, and governance controls.
- `CODEOWNERS` identifies protected protocol/runtime/security boundaries, including schemas, validators, signatures, policy, federation, records, workflows, runtime, protocol graph, verification map, and trust-kernel index.
- `SECURITY.md` separates public integrity reports from private vulnerability reports and requires human-supervised validation for sensitive archive, trust-kernel, policy, signing, record-reference, and provenance decisions.
- `docs/project-control/trust-kernel-boundary.md` gives a deeper classification model for trust-kernel-sensitive and trust-kernel-adjacent changes.

Security reviewer path clarity:

- Sufficient for reporting boundaries and sensitive disclosure handling.
- Sufficient for identifying protected areas.
- Conditional for rapid navigation because the security reviewer may need to jump among `SECURITY.md`, `docs/security/**`, `CODEOWNERS`, `docs/project-control/trust-kernel-boundary.md`, governance docs, and runtime docs.

No production-readiness claim should be inferred from any checklist or runtime stabilization note. Runtime stabilization remains advisory and conditional within repository-defined scope.

## Historical Evidence Discoverability

Historical evidence discoverability is conditionally sufficient.

Strong signals:

- `docs/START_HERE.md` explicitly explains legacy names and states that historical/evidence-bearing files must not be silently rewritten or deleted.
- Historical and migration references are present in `records/`, `records/archive/`, `records/archived/`, `witness-archive/`, and `docs/governance/`.
- Governance reports cover archive migration, historical record classification, hash handling, QR handling, generated artifact handling, and release evidence handling.
- `AGENTS.md` and `HC_BOOTSTRAP.md` both reinforce evidence preservation and source-of-truth discipline.

Conditional gap:

- Historical/evidence-bearing files are discoverable after reading `docs/START_HERE.md`, but the repository has many evidence-related documents. A short evidence index could help distinguish canonical records, archived records, migration evidence, generated artifacts, QR artifacts, hash references, signatures, release evidence, and historical-origin docs.

## Current Phase / Next Task Discoverability

Current phase and next-task discoverability is the main conditional weakness.

What is discoverable:

- `README.md` describes MVP / early-stage status and the broad current focus on stable HC:// verification workflow.
- `docs/START_HERE.md` states v0.1.0 MVP / early-stage status, current version, release evidence, implemented/experimental/future areas, limitations, and safe PR checks.
- `HC_BOOTSTRAP.md` directs agents to `docs/project-control/project-state.md`, `docs/project-control/task-ledger.md`, and `docs/project-control/next-actions.md`.
- Runtime review documents record recent stabilization evidence, including telemetry contract review and runtime stabilization review.

Gap:

- `docs/project-control/project-state.md` and `docs/project-control/next-actions.md` appear to describe an earlier Phase 2 trust-kernel enforcement sequence and references around #545-#551, while the present review context says recent completed work is #628, #629, and #630 and the focus has shifted to repository usability, onboarding, and AI/human agent guidance.

Impact:

- New contributors and agents can still stay safe because protected-path boundaries are clear, but they may be unsure whether the next safe task is still the older Tier-1 governance review queue or the newer operating-layer/navigation review path.
- This is a navigation/state-synchronization gap, not a runtime, validator, schema, workflow, governance-rule, record, hash, QR, signing, federation, or policy defect.

## Gaps

1. **Current-state drift in project-control files.** `project-state.md` and `next-actions.md` appear stale relative to the #628-#630 runtime stabilization sequence and the #631 operating-layer review request.
2. **Navigation fragmentation.** Multiple onboarding files are individually useful, but contributors may not know which entry point is primary for their role unless they find `docs/START_HERE.md` first.
3. **Maintainer route density.** Governance and release docs are comprehensive but dense; a new maintainer may need a shorter route by task type.
4. **Security route density.** Security reviewers can find the right material, but a security/trust-kernel index could reduce navigation time.
5. **Historical evidence route density.** Historical evidence is protected and explained, but an evidence index would reduce confusion between canonical records, archives, generated artifacts, QR artifacts, hash references, signatures, and release evidence.
6. **Runtime status handoff.** The recent runtime reports are valuable but should be easier to find from onboarding and project-control surfaces after stabilization.
7. **Duplicate or overlapping guidance.** `README.md`, `docs/START_HERE.md`, `CONTRIBUTING.md`, `docs/CONTRIBUTING.md`, `docs/contributor-start-here.md`, `docs/developer-onboarding.md`, `AGENTS.md`, and `HC_BOOTSTRAP.md` overlap. The overlap is not unsafe, but it increases cognitive load.

## Risk Assessment

| Risk | Level | Rationale | Mitigation already present | Residual need |
| --- | --- | --- | --- | --- |
| New contributor gets lost | Medium | Many docs exist and several entry points overlap. | `docs/START_HERE.md`, README quick navigation, contributor docs. | Small navigation/index PR. |
| AI agent modifies wrong files | Medium | Agents may follow stale or incomplete context if they do not read all operating docs. | `AGENTS.md`, `HC_BOOTSTRAP.md`, protected-path lists, CODEOWNERS, PR template, project-control docs. | Stronger prominent agent route and current-state refresh. |
| Protected paths are misunderstood | Low to Medium | Protected paths are listed in several places, but not always identically grouped. | `docs/START_HERE.md`, AGENTS, CODEOWNERS, trust-kernel boundary docs. | Optional protected-path navigation consolidation. |
| Historical evidence is altered accidentally | Low to Medium | Evidence preservation is emphasized, but evidence surfaces are spread across directories and governance docs. | `docs/START_HERE.md`, AGENTS, governance migration docs, records directories. | Optional evidence index. |
| Runtime stabilization status is missed | Medium | Runtime reports exist but are not the default path for non-runtime contributors. | Runtime docs directory and README runtime links. | Link latest stabilization review sequence from project-control/START_HERE. |
| Human final authority is weakened | Low | Current language repeatedly preserves human-supervised validation and advisory-only agent output. | AGENTS, HC_BOOTSTRAP, SECURITY, PR template, governance docs. | Continue preserving claim boundaries. |
| Production-readiness overclaim | Low | README and security docs avoid production-final claims. | Explicit early-stage and advisory-only language. | Continue avoiding production, forensic, and truth-finality claims. |

## Final Recommendation

Decision: **OPERATING LAYER CONDITIONALLY SUFFICIENT**.

The operating layer is safe enough for continued human-supervised repository work. It explains what HC-TRUST-LAYER is, where to start, what files are primary, what must not be touched, how AI-assisted work should behave, and how human final authority is preserved.

The condition is navigation and current-state synchronization. The main improvement should be a small documentation-only PR that updates onboarding/project-control navigation after runtime stabilization, without changing runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy.

This review does not recommend modifying protected paths or implementation behavior.

## Recommended Next PR

Recommended next PR: **small documentation navigation refresh after runtime stabilization**.

Suggested scope:

1. Update the primary onboarding route so `README.md`, `docs/START_HERE.md`, `AGENTS.md`, and `HC_BOOTSTRAP.md` clearly point to one role-based onboarding path.
2. Refresh `docs/project-control/project-state.md` and `docs/project-control/next-actions.md` to reflect the post-#628, #629, and #630 focus on operating-layer usability and safe documentation navigation work.
3. Add or improve links from onboarding/project-control docs to:
   - `docs/runtime/telemetry-contract-coverage-review.md`
   - `docs/runtime/runtime-stabilization-review.md`
   - `docs/project-control/trust-kernel-boundary.md`
   - `docs/project-control/authority-model.md`
   - governance historical evidence docs
4. Keep the PR documentation-only, scoped, reversible, and advisory.
5. Do not change runtime, tests, validators, schemas, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy.

If no other major gap is identified, this should be treated as a navigation/index-linking PR only.
