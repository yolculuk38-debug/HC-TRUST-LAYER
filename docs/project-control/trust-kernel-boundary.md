# Trust Kernel Boundary

Documentation-only boundary reference for HC-TRUST-LAYER and HC:// trust-kernel review routing.

## 1. Purpose

This document consolidates existing repository evidence about the trust kernel, Trust-Kernel-Adjacent surfaces, governance-only surfaces, constitutional-only surfaces, operational-only surfaces, protected surfaces, source-of-truth order, human-supervised validation expectations, sensitive change criteria, adjacent change criteria, and known boundary gaps.

This document is advisory and documentation-only. It does not change runtime behavior, workflow behavior, schemas, validators, records, policy, federation, signing, automation, or governance enforcement. Repository evidence remains authoritative.

## 2. Authority Boundary

This document supports orientation and review routing only.

It does not:

- approve changes;
- merge changes;
- validate security posture;
- establish production readiness;
- create governance enforcement;
- create automation;
- replace repository-defined checks;
- replace reviewer oversight;
- replace human-supervised validation.

Human-supervised validation remains required for sensitive trust-kernel-impacting work.

## 3. Trust Kernel Definition

The trust kernel is the set of HC-TRUST-LAYER repository surfaces that define or materially affect HC:// verification integrity, provenance continuity, canonical record handling, validation outcomes, policy interpretation, signing or trust-anchor semantics, federation routing, public verification, dispute or replay handling, hash behavior, and audit trail continuity.

The trust kernel is not a single file or implementation layer. Repository evidence currently distributes the definition across `AGENTS.md`, `CODEOWNERS`, the verification map, the protocol graph, the trust kernel index, project-control guidance, protected-path rules, and related documentation.

## 4. Trust Kernel Scope

The trust kernel scope includes repository surfaces where a change can directly or indirectly affect:

- schema contracts;
- canonical record identity, structure, serialization, or provenance continuity;
- validator behavior or validation result normalization;
- policy evaluator interpretation or routing;
- signing, signature envelopes, trust anchors, or key-handling assumptions;
- federation discovery, sync, or routing boundaries;
- runtime HC:// verification behavior;
- public verification behavior;
- dispute, replay, challenge, or supersession semantics;
- hash-linked artifacts or deterministic serialization assumptions;
- audit trail continuity;
- machine-readable trust-kernel, protocol graph, or verification map indexes;
- owner and review-routing controls for protected protocol, runtime, and security boundaries.

## 5. Trust Kernel Non-Goals

This boundary document does not expand the trust kernel by itself.

It does not:

- change runtime behavior;
- change workflow behavior;
- change schemas;
- change validators;
- change records;
- change policy;
- change federation;
- change signing;
- create automation;
- create governance enforcement;
- claim production readiness;
- claim live federation guarantees;
- claim complete dispute automation;
- claim autonomous governance finality;
- claim cryptographic or policy guarantees not backed by tests and repository documentation.

## 6. Trust Kernel Boundary Map

Use these review categories as advisory routing labels:

| Category | Meaning | Review posture |
| --- | --- | --- |
| Trust Kernel Core | Surfaces that define or materially affect HC:// verification integrity, provenance, canonical records, validators, policy, signing, federation, runtime verification, public verification, dispute or replay handling, hashes, audit continuity, or protected index metadata. | Treat as high sensitivity. Require explicit review and human-supervised validation when non-trivial impact is possible. |
| Trust-Kernel-Adjacent | Surfaces that guide, describe, route, guard, or contextualize trust-kernel work without directly changing core behavior. | Treat as sensitive documentation or operations context. Escalate if language changes boundary interpretation or reviewer expectations. |
| Governance-Only | Advisory governance process, decision, review, and evidence-handling surfaces. | Review for authority, source-of-truth, protected-surface, and human-supervised validation implications. |
| Constitutional-Only | Durable principles and value boundaries for HC:// governance and repository stewardship. | Review for stability, authority limits, and non-enforcement claims. |
| Operational-Only | Shift handoff, task planning, control-center, operator orientation, and working-state surfaces. | Review for staleness, source-of-truth priority, and no approval or enforcement claims. |
| Protected Surface | Paths or files that require heightened review because repository evidence identifies them as protocol, runtime, security, workflow, canonical, or trust-kernel sensitive. | Do not modify unless explicitly requested and validated through the repository review process. |

## 7. Trust Kernel Core Surfaces

Trust Kernel Core surfaces include:

- `schema/**`;
- `records/**`;
- `validators/**`;
- `policy/**`;
- `signatures/**`;
- `federation/**`;
- `src/hc_runtime/**`;
- runtime modules under `src/**` that affect validation, policy, signing, federation, provenance, public verification, dispute or replay behavior, hash behavior, or audit continuity;
- `CODEOWNERS`;
- `verification-map.json`;
- `protocol-graph.json`;
- `trust-kernel-index.json`.

These surfaces should be treated as trust-kernel-sensitive even when a specific file, directory, or module is reserved, absent, generated, or currently documentation-backed rather than fully implemented.

## 8. Trust-Kernel-Adjacent Surfaces

Trust-Kernel-Adjacent surfaces include:

- `AGENTS.md`;
- `HC_BOOTSTRAP.md`;
- `docs/verification-map.md`;
- `docs/protocol-graph-agent-context.md`;
- `docs/trust-kernel-index.md`;
- `docs/project-control/**`;
- `hc_context/**`;
- `agents/**`;
- guard scripts;
- `.github/workflows/**`.

These surfaces may not directly change runtime verification behavior, but they can change orientation, review routing, protected-surface interpretation, source-of-truth expectations, or guardrail visibility. Treat changes as adjacent when they only clarify or route trust-kernel work and do not modify core behavior, schemas, validators, records, policy, federation, signing, runtime behavior, or index metadata.

## 9. Governance-Only Surfaces

Governance-only surfaces describe advisory decision processes, review expectations, evidence models, escalation rules, and change lifecycles.

Examples include project-control governance documents, decision records, audit-layer guidance, reviewer-facing process notes, governance change protocols, and related documentation that does not alter core trust-kernel behavior or protected machine-readable indexes.

Governance-only changes remain advisory unless repository evidence explicitly implements enforcement elsewhere. They must not imply approval authority, merge authority, autonomous governance, security validation, or truth-finality validation.

## 10. Constitutional-Only Surfaces

Constitutional-only surfaces describe durable HC:// principles, stewardship values, authority limits, and long-lived review expectations.

They may inform governance and operational interpretation, but they do not directly enforce repository behavior. They must preserve the advisory documentation boundary unless a separately authorized and validated implementation changes repository controls.

## 11. Operational-Only Surfaces

Operational-only surfaces provide shift-level orientation, current-state summaries, next-action guidance, task ledgers, control-center notes, bot-readiness notes, or operator checklists.

They can guide safe work sequencing, but they do not override merged repository files, protected repository evidence, repository-defined checks, PR records, review notes, human review decisions, trust-kernel boundaries, canonical record boundaries, or governance controls documented in-repo.

## 12. Protected Surface Model

Protected surfaces are paths, files, or concepts that require heightened review because they can affect HC:// verification integrity, security posture, provenance, audit trail continuity, canonical record handling, policy interpretation, workflow governance, signing, federation, or runtime behavior.

Protected surfaces include the Trust Kernel Core surfaces listed above and any additional protected paths identified by repository instructions, CODEOWNERS, project-control guidance, reviewer direction, or task-specific instructions.

A protected-surface assessment should identify:

- whether protected paths are modified;
- whether protected concepts are reinterpreted;
- whether a documentation change could alter reviewer expectations for protected paths;
- whether human-supervised validation is required, pending, limited, or not applicable;
- whether the change is reversible and auditable.

## 13. Source-of-Truth Model

When trust-kernel boundary guidance conflicts with other evidence, use this advisory priority order:

1. Merged repository files and protected repository evidence.
2. Repository-defined checks and validation outputs.
3. PR records, commits, review notes, and human review decisions.
4. Protected-path rules, trust-kernel boundaries, canonical record boundaries, and governance controls documented in-repo.
5. Machine-readable indexes: `verification-map.json`, `protocol-graph.json`, and `trust-kernel-index.json`.
6. Human-readable companion documentation, including the verification map, protocol graph, trust kernel index, and project-control documents.
7. Advisory agent context, `hc_context`, bot summaries, chat memory, and external summaries.

Repository evidence remains authoritative. Weaker advisory context must not override stronger repository evidence.

## 14. Human-Supervised Validation Expectations

Human-supervised validation remains required for sensitive trust-kernel-impacting work.

Require or escalate for human-supervised validation when a change may affect:

- runtime verification behavior;
- schema contracts;
- validator logic;
- record identity, canonical record handling, or provenance continuity;
- policy interpretation or routing;
- signing or trust-anchor semantics;
- federation behavior;
- protected workflow behavior;
- deterministic serialization, hash behavior, replay handling, dispute handling, public verification, or audit continuity;
- CODEOWNERS or protected index metadata;
- governance interpretation of any Trust Kernel Core surface.

Documentation-only clarification may still require human review when it changes boundary interpretation, expected validation paths, or reviewer routing.

## 15. Trust-Kernel-Sensitive Change Criteria

Classify a change as trust-kernel-sensitive when it:

- modifies a Trust Kernel Core surface;
- changes runtime behavior that affects validation, policy, signing, federation, provenance, public verification, dispute or replay handling, hash behavior, or audit continuity;
- changes schema contracts, canonical record assumptions, deterministic serialization, or hash-linked artifacts;
- changes validators, validation output semantics, result normalization, or verification package validation;
- changes policy rules, policy evaluator behavior, or decision-path interpretation;
- changes signing envelopes, trust-anchor assumptions, key-handling semantics, or signature verification behavior;
- changes federation discovery, sync, routing, or consensus-oriented trust boundaries;
- changes CODEOWNERS or protected machine-readable indexes;
- changes documentation in a way that redefines a Trust Kernel Core boundary or implies a new guarantee.

Trust-kernel-sensitive changes should identify affected surfaces, expected decision-path differences where applicable, validation requirements, reviewer routing, and audit trail continuity expectations.

## 16. Trust-Kernel-Adjacent Change Criteria

Classify a change as Trust-Kernel-Adjacent when it:

- modifies advisory documentation that describes trust-kernel boundaries without changing core behavior;
- updates project-control, agent context, `hc_context`, guard documentation, or workflow documentation without changing the underlying guard or workflow behavior;
- clarifies source-of-truth order, human-supervised validation expectations, or protected-surface routing;
- adds navigation aids or links for the verification map, protocol graph, or trust kernel index;
- documents a known gap without modifying schemas, validators, records, policy, federation, signing, runtime behavior, workflows, guard scripts, or machine-readable trust-kernel indexes.

Trust-Kernel-Adjacent changes should remain documentation-first, scoped, reversible, and explicit about advisory limits.

## 17. Verification Map Relationship

The verification map is a documentation-first orientation layer for HC-TRUST-LAYER and HC:// trust-kernel domains. It connects canonical records, validators, policy evaluation, verification packages, trust graph and protocol graph context, signing, dispute and challenge pathways, provenance, federation, and public verification surfaces.

`verification-map.json` is a protected Trust Kernel Core machine-readable index. `docs/verification-map.md` is a Trust-Kernel-Adjacent human-readable companion. Both remain advisory in this phase unless repository evidence implements behavior elsewhere.

## 18. Protocol Graph Relationship

The protocol graph maps HC:// trust-kernel components, relationships, dependencies, and likely change-impact areas for review routing.

`protocol-graph.json` is a protected Trust Kernel Core machine-readable index. `docs/protocol-graph-agent-context.md` and `docs/protocol-graph-index.md` are Trust-Kernel-Adjacent companion documentation that support agent context, provenance, audit trail continuity, and human-supervised validation awareness.

## 19. Trust Kernel Index Relationship

`trust-kernel-index.json` is a protected Trust Kernel Core machine-readable index that links the protocol graph and verification map into one trust-kernel navigation layer.

`docs/trust-kernel-index.md` is a Trust-Kernel-Adjacent human-readable companion. It explains advisory use, source-of-truth relationships, human review expectations, and limits. It does not replace repository evidence, runtime enforcement, schemas, validators, workflow gates, or human-supervised validation.

## 20. HC Context Relationship

`hc_context/**` is advisory agent context. It may help agents orient around current project state, task scope, and review routing, but it can lag behind merged files, repository-defined checks, PR records, review notes, human review decisions, protected-path rules, and project-control documents.

Use `hc_context/**` only after stronger source-of-truth layers. It must not override repository evidence or create approval, merge, governance-enforcement, security-validation, production-readiness, or truth-finality claims.

## 21. Known Boundary Gaps

Known boundary gaps include:

- Trust Kernel definition is distributed across multiple repository files.
- Some guard definitions appear narrower than CODEOWNERS or protected-surface metadata.
- `validators/**` and `signatures/**` may be protected or reserved even if absent.
- `records/**` includes both canonical record locations and non-canonical or generated artifacts.
- Human-readable index companion docs are not always protected the same way as JSON index files.
- `src/**` contains Trust-Kernel-sensitive modules outside `src/hc_runtime/**`.

These gaps should be surfaced in review summaries when relevant. They do not authorize broad changes or bypass human-supervised validation.

## 22. Risks and Guardrails

Key risks:

- boundary drift caused by advisory docs being treated as stronger than repository evidence;
- accidental protected-path impact from documentation wording;
- overclaiming runtime, policy, federation, signing, cryptographic, dispute, or governance guarantees;
- missing trust-kernel-sensitive modules outside obvious paths;
- stale `hc_context`, bot summaries, or chat memory overriding merged repository files;
- guard definitions being interpreted as complete when CODEOWNERS or protected metadata are broader.

Guardrails:

- keep changes small, scoped, reversible, and auditable;
- preserve HC-TRUST-LAYER and HC:// terminology;
- run terminology, docs drift, canonical artifact, and diff checks for documentation changes;
- do not modify workflows, runtime, schemas, validators, records, policy, federation, signing, trust-kernel indexes, `hc_context`, agents, or guard scripts unless explicitly requested;
- do not weaken repository checks, policy, guardrails, or validation logic;
- document protected-path confirmation and docs-only confirmation in review summaries;
- escalate uncertainty instead of inferring unsupported production guarantees.

## 23. Related Documents

- `AGENTS.md`
- `HC_BOOTSTRAP.md`
- `CODEOWNERS`
- `docs/verification-map.md`
- `verification-map.json`
- `docs/verification-map-index.md`
- `docs/protocol-graph-agent-context.md`
- `protocol-graph.json`
- `docs/protocol-graph-index.md`
- `docs/trust-kernel-index.md`
- `trust-kernel-index.json`
- `docs/protocol-graph-integrity.md`
- `docs/anti-spoofing-foundations.md`
- `docs/trusted-relationship-model.md`
- `docs/trust-workflow-model.md`
- `docs/idea-to-pr-pipeline.md`
- `docs/project-control/hc-control-center.md`
- `docs/project-control/hc-constitutional-layer.md`
- `docs/project-control/governance-change-protocol.md`
- `docs/project-control/hc-audit-layer.md`
- `docs/project-control/project-state.md`
- `docs/project-control/task-ledger.md`
- `docs/project-control/next-actions.md`
