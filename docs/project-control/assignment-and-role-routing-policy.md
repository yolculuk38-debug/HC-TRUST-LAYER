# Assignment and Role Routing Policy

## Status

- **status:** active project-control policy
- **scope:** issue assignment, PR reviewer routing, bot suggested assignees, and role-based review recommendations
- **authority:** advisory-only routing policy
- **human authority:** repository maintainers retain final authority

## Purpose

HC-TRUST-LAYER should support automation-assisted routing without allowing automation to become a decision maker.

This policy defines how issues and pull requests may be routed to humans or roles while preserving the HC rule:

```text
AI and bots may suggest.
Humans decide.
```

## Core Rule

Assignment is not approval.

Reviewer routing is not a merge decision.

A suggested assignee, reviewer, label, or route only means that a human or role should inspect the work.

## Current Maintainer Model

At the current solo-maintainer stage, the default human maintainer is:

```text
@yolculuk38-debug
```

Until additional maintainers are explicitly added, automated routing must treat this user as the default human review target.

## Role Map

The following role map is advisory. It does not create GitHub teams by itself.

| Area | Suggested role | Examples |
| --- | --- | --- |
| documentation | docs reviewer | README, docs, onboarding, project-control docs |
| governance | governance reviewer | authority policy, cleanup policy, branch protection, decision rules |
| workflow/security | security reviewer | `.github/workflows/**`, CodeQL, Dependabot, permissions |
| runtime/API | runtime reviewer | `src/hc_runtime/**`, API contracts, telemetry, response shape |
| trust kernel | trust-kernel reviewer | schema, validators, records, signatures, policy, federation |
| generated artifacts | generated-artifact reviewer | generated indexes, explorer data, derived artifacts |
| QR/hash/provenance | verification reviewer | QR, hash verification, record provenance, public validator |

## Routing Rules

### Documentation-only Changes

Documentation-only changes may be routed to the docs reviewer.

If the documentation changes governance meaning, authority boundaries, protected areas, or release rules, also route to governance review.

### Governance Changes

Governance changes require human review.

Examples:

- authority policy
- cleanup/archive policy
- protected path rules
- branch protection guidance
- bot permissions
- automation boundaries
- review/merge rules

Suggested route:

```text
governance reviewer
```

### Workflow or Security Changes

Workflow/security changes are trust-critical.

Examples:

- `.github/workflows/**`
- dependency update automation
- CodeQL/security scan settings
- bot workflow permissions
- `pull_request_target` usage
- repo secrets or security guidance

Suggested route:

```text
security reviewer
human_review_required=true
```

Automation must not treat workflow changes as low risk.

### Runtime/API Changes

Runtime/API changes may affect public-safe response contracts.

Suggested route:

```text
runtime reviewer
```

Review should confirm:

- `advisory_only=true` where applicable
- `public_safe=true` where applicable
- `truth_guarantee=false` where applicable
- warnings remain visible
- tests cover response shape changes

### Trust Kernel Changes

Trust-kernel changes require careful human review.

Examples:

- `schema/**`
- `validators/**`
- `records/**`
- `signatures/**`
- `policy/**`
- `federation/**`
- `src/hc_runtime/**`
- QR/hash/provenance logic

Suggested route:

```text
trust-kernel reviewer
human_review_required=true
```

### Generated Artifact Changes

Generated artifacts are not canonical records unless explicitly defined by policy.

Suggested route:

```text
generated-artifact reviewer
```

Review should confirm:

- source artifact is known
- generated output does not imply truth guarantee
- generated output does not override canonical record boundaries

## Bot Suggested Assignment

Bots may suggest routing in comments or reports.

Allowed bot output examples:

```text
suggested_route: governance reviewer
suggested_assignee: @yolculuk38-debug
reason: governance policy file touched
human_review_required: true
```

or:

```text
suggested_route: runtime reviewer
reason: runtime response contract touched
human_review_required: true
```

## Forbidden Automation

Unless a separate governance policy explicitly enables it, bots must not:

- assign users automatically
- request reviewers automatically
- apply labels automatically
- approve pull requests
- request changes
- merge pull requests
- close issues or pull requests
- reopen issues or pull requests
- lock conversations
- delete issues, comments, or branches
- treat their own comments as commands for downstream automation

## Future Auto-assignment Phases

Auto-assignment may be considered only after these phases are complete:

1. role map documented
2. suggested routing implemented as advisory output
3. human review confirms suggestions are useful and low-noise
4. governance approves a limited assignment scope
5. logs and rollback path are documented

Initial auto-assignment, if ever enabled, should be limited to low-risk docs-only work.

High-risk areas must remain human-supervised even if routing is automated.

## Evidence Bundle Requirement

A routing recommendation should include evidence:

```text
changed_files
matched_area
matched_role
risk_reason
human_review_required
source_of_truth
```

The source of truth must be current GitHub state and trusted main-branch policy/docs.

## Public Visibility

Assignments, labels, PR comments, issue comments, and bot reports in a public repository may be visible to others.

Do not include secrets, tokens, credentials, private keys, signing keys, recovery codes, or private personal data in routing comments.

## Human Final Authority

Routing helps humans find the right review surface. It does not decide outcomes.

Only authorized human maintainers or explicitly approved governance workflows may assign final responsibility, request review, close, merge, or reject work.

## HC Principle

Trust the record, not the narrative.

Routing must be based on changed files, explicit policy, current repo state, and human-supervised governance — not on untrusted PR claims.
