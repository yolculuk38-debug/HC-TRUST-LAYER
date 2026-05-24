# HC-TRUST-LAYER HC:// Idea-to-PR Pipeline Model

## Status and Scope

- documentation-only model
- no runtime automation in this phase
- no workflow behavior changes in this phase
- no schema changes in this phase
- no validator changes in this phase

This model defines a controlled path from idea intake to PR review while preserving human-supervised validation, provenance continuity, and audit trail integrity.

## Purpose

The HC-TRUST-LAYER idea-to-PR pipeline helps contributors and AI agents transform ideas into bounded implementation proposals without overwhelming maintainers.

The pipeline emphasizes:

- scoped documentation-first analysis
- policy evaluator-informed triage
- explicit risk classification
- human-supervised approval boundaries
- auditable decision continuity

## Idea Intake Model

Each idea should be captured as a structured intake item with:

1. idea summary
2. stated purpose and expected value
3. affected HC:// layer hints
4. expected change category (docs, workflow, schema, validator, signing, federation, API)
5. trust-kernel sensitivity notes
6. known risks, unknowns, and constraints

Intake records are advisory artifacts and must not be treated as implicit approval to implement.

## Idea Classification

Every intake item is classified into exactly one primary category:

- **core**
- **extension**
- **research**
- **future**
- **rejected**
- **duplicate**

Classification rationale must be recorded to preserve audit trail continuity and reviewer context.

## Core vs Extension Decision

Use the following decision baseline:

- **core** when the idea directly affects canonical HC:// verification surfaces central to HC-TRUST-LAYER.
- **extension** when the idea adds optional capability around existing trust-kernel boundaries without redefining canonical behavior.
- **research** when assumptions are incomplete and additional evidence is required before scoping implementation.
- **future** when the direction is valid but intentionally deferred due to timing, capacity, or dependency sequencing.
- **rejected** when the idea conflicts with policy, architecture boundaries, or repository constraints.
- **duplicate** when an equivalent idea already exists in the repository backlog, roadmap, or accepted plan.

## Feasibility Review

Feasibility review is required before implementation routing. The review should capture:

1. clarity of scope and objective
2. dependency and sequencing needs
3. affected documentation and policy references
4. expected reviewer domains
5. reversibility and rollback posture

If feasibility is uncertain, route to **research** or **future** instead of forcing immediate implementation.

## Risk Scoring

Assign an explicit risk class at intake refinement:

- **low risk**: docs-only or navigation clarification with no trust-kernel behavior impact
- **moderate risk**: workflow/process or routing clarifications requiring governance review
- **high risk**: any potential impact to schema, validator logic, signing/trust anchors, federation behavior, policy interpretation, or canonical record boundaries

High-risk ideas must remain blocked from automatic merge pathways and require human-supervised validation.

## Policy Evaluator Use

Policy evaluator usage in this model is advisory for routing and review preparation.

Expected policy evaluator outputs for idea triage:

1. relevant policy rule references
2. expected decision-path notes
3. disallowed claim detection (for example production-readiness or autonomous-governance claims)
4. reviewer escalation hints

Policy evaluator output does not replace human review decisions.

## Agent Task Routing

After classification and risk scoring, route ideas to scoped tasks:

- **docs-only / low risk** -> documentation and terminology review lane
- **workflow / moderate risk** -> CI/governance review lane
- **high-risk surfaces** -> explicit reviewer escalation lane before any implementation proposal

Routing records should include HC:// layer mapping and trust-kernel boundary notes.

## Codex Implementation Handoff

When an idea is suitable and scoped, the handoff package to Codex should include:

1. goal and purpose
2. in-scope file list
3. out-of-scope boundaries
4. required terminology set
5. risk class and policy notes
6. required checks
7. expected commit message format

Codex output is implementation advisory material subject to repository checks and human-supervised validation.

## PR Creation Flow

The documentation model follows this controlled sequence:

1. Idea submitted.
2. AI summarizes idea.
3. System maps idea to HC:// layer.
4. Policy/risk class assigned.
5. If unsuitable, park in backlog.
6. If suitable, generate scoped task.
7. Codex implements.
8. Checks run.
9. Human reviews/merges.
10. Result enters audit trail.

This sequence is a governance model, not a runtime automation claim.

## Human-Supervised Approval

Human-supervised validation is mandatory for non-trivial and high-risk outcomes.

Approval checkpoints include:

1. policy interpretation review
2. boundary-impact confirmation
3. uncertainty and unresolved risk capture
4. merge, defer, or reject rationale recording

No autonomous governance finality is permitted.

## Audit Trail Preservation

The pipeline must preserve auditable continuity across:

- idea intake entry
- classification and risk scoring updates
- feasibility conclusions
- task routing decisions
- implementation PR references
- check outcomes
- human approval decisions
- merge/deferral/rejection state

All decision transitions should remain attributable and linked to canonical repository records.

## Safeguards

The following safeguards are mandatory in this model:

- no automatic high-risk merge
- schema, validator, signing, and federation changes require human review
- no production claims unless implemented and validated in-repo
- no autonomous governance claims
- no truth guarantee language in idea triage or PR summaries

## Backlog Handling for Unsuitable Ideas

When ideas are unsuitable for immediate implementation:

- classify as **research**, **future**, **rejected**, or **duplicate**
- preserve rationale and provenance notes
- record re-entry conditions when applicable
- avoid silent discard to preserve audit trail continuity

## Related References

- `AGENTS.md`
- `agents/workflow.md`
- `agents/task-template.md`
- `docs/verification-map.md`
- `docs/trust-workflow-model.md`
- `docs/implementation-transition-plan.md`
