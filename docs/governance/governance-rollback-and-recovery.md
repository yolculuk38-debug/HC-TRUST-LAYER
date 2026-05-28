# HC:// Governance Rollback and Recovery Guidance

This document defines governance rollback and recovery guidance for HC-TRUST-LAYER maintainers when governance decisions, merges, automation behavior, or repository stability diverge from expected controls.

Scope boundaries:

- Documentation-only guidance.
- Human-supervised validation remains required.
- No runtime verification behavior changes.
- No canonical schema, validator, signing, or security workflow changes.
- No unrestricted auto-merge behavior.
- No autonomous governance or self-repair authority claims.

## Purpose

Provide a safe, auditable, and reversible recovery flow that preserves provenance, review traceability, and governance accountability during repository-level incidents.

## Rollback scenarios

### Incorrect merge

A pull request is merged with incorrect scope, unintended behavior impact, or missing governance evidence.

### Governance misclassification

A pull request receives an incorrect governance risk label, review route, or trust-impact classification.

### Automation routing mistake

Automation assigns the wrong reviewer path, guard category, or escalation route and requires human correction.

### Dependency instability

A dependency update introduces unstable behavior, broken checks, or drift that undermines governance preflight confidence.

### Protected-path policy violation

A change touches protected boundaries without required routing, review depth, or reviewer confirmation.

## Safe recovery flow

### 1) Pause merges

- Pause non-emergency merges until the incident is triaged.
- Preserve existing branch protection and governance controls while paused.

### 2) Inspect governance logs

- Review governance preflight outputs, label decisions, reviewer routing, and escalation notes.
- Identify where classification, routing, or decision-path divergence occurred.

### 3) Inspect Actions output

- Review GitHub Actions logs and check summaries related to governance, terminology, docs drift, and canonical artifact guards.
- Capture failing or contradictory evidence as part of the recovery record.

### 4) Revert or fix safely

- Prefer minimal, reversible corrective commits.
- Revert incorrect merges when rollback is lower-risk than forward-fix.
- Use forward-fix only when the recovery rationale is explicit, auditable, and reviewer-approved.
- Do not rewrite published history to hide mistakes.

### 5) Rerun governance preflight

- Rerun required governance and documentation guards after corrective changes.
- Confirm the repository returns to expected governance state before unpausing merges.

### 6) Require human confirmation before resuming

- Require explicit human maintainer confirmation that recovery checks pass and audit evidence is complete.
- Resume merges only after human-supervised validation is recorded.

## Auditability requirements

### Preserve traceability

- Keep incident chronology visible through attributable commits, issue links, and review notes.
- Preserve provenance continuity across decision, rollback, and recovery steps.

### Document recovery reason

- Record why rollback or forward-fix was required.
- Record what governance decision or automation path failed and how it was corrected.

### Avoid hidden rewrites

- Avoid force-push history rewrites that remove incident evidence.
- Prefer additive, reviewable corrections that maintain audit trail continuity.

## Forbidden recovery behavior

- Force-bypassing governance checks to accelerate recovery.
- Disabling validators or governance guards without explicit review and documented approval.
- Removing, altering, or obscuring audit evidence tied to governance decisions.

## Recovery checklist (maintainer use)

1. Pause merges and announce recovery state.
2. Collect governance logs and Actions evidence.
3. Classify incident type (merge, misclassification, routing, dependency, policy violation).
4. Choose corrective method (revert or forward-fix) with rationale.
5. Submit minimal corrective PR with explicit recovery context.
6. Rerun governance preflight and required documentation guards.
7. Obtain human-supervised confirmation.
8. Resume merges and publish concise recovery summary.

## Implementation notes

- This guidance is advisory for repository governance operations and does not alter runtime trust-kernel logic.
- Any trust-kernel-impacting follow-up still requires explicit human-supervised validation and reviewer escalation per repository governance policy.
