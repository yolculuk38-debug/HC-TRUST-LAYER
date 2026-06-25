# HC Trust Engineer Closure Report Mode

Status: project-control design note; advisory and report-only.

This note defines only closure report mode. It does not define or expand a full HC Trust Engineer operating loop.

## Purpose

Closure report mode is a bounded capability of the existing HC Trust Engineer / report-only advisory line. It reviews project-control report chains and proposes `READY_FOR_CLOSURE_NOTE` only when repository evidence shows that a chain appears complete enough for a human-reviewed closure note.

The mode helps maintainers identify when a project-control report sequence appears ready for a closure-note recommendation. It does not create the closure note, decide repository truth, or mutate repository state.

## Scope

Closure report mode applies only to project-control advisory/report chains, including report lifecycle references, project-control indexes, archived reference reports, finding reports, and direct human maintainer direction for the reviewed chain.

It does not decide:

- truth;
- identity;
- legal status;
- security status;
- production readiness;
- merge readiness;
- approval status.

## Inputs

Closure report mode may review these inputs when they are available in repository evidence:

- recent merged project-control pull requests;
- report lifecycle and index files;
- archive, reference, and finding reports;
- provenance standard wording and related project-control guidance;
- explicit human maintainer direction.

## Output

Closure report mode produces one of two advisory outcomes:

```text
READY_FOR_CLOSURE_NOTE
```

or:

```text
NOT_READY_FOR_CLOSURE
```

When the outcome is `NOT_READY_FOR_CLOSURE`, the report should list the missing evidence, unresolved blocker, or unclear reference that prevents a human-reviewed closure note recommendation.

## Hard boundaries

Closure report mode must preserve these boundaries:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_mutation=false
issue_comment_automation=false
label_reviewer_mutation=false
approval_authority=false
merge_authority=false
```

## What it must not do

Closure report mode must not:

- open pull requests automatically;
- create issues automatically;
- comment automatically;
- label, assign, request reviewers, approve, close, or merge;
- archive, delete, or move files by itself;
- treat advisory report text as command authority;
- present a closure recommendation as final maintainer action.

## Decision rule

Closure report mode may produce `READY_FOR_CLOSURE_NOTE` only when all of the following are true:

1. the report chain has a clear lifecycle or index reference;
2. related project-control pull requests are merged;
3. no active blocker or unresolved reference remains in the reviewed chain;
4. provenance wording is compliant with HC-TRUST-LAYER advisory and evidence-preserving terminology;
5. the proposed closure remains advisory and human-reviewed.

If any condition is missing, unclear, or contradicted by repository evidence, the outcome must be `NOT_READY_FOR_CLOSURE` with the missing evidence stated plainly.

## Human handoff

A closure report mode result is only a recommendation. A human maintainer decides whether to create a pull request, issue, comment, archive action, or another repository-facing follow-up.

Human final authority remains required for closure notes and any repository action. The mode does not create autonomous governance authority for HC Trust Engineer, HC Control Bot, or any other agent.

## Real-world analogy

Closure report mode is similar to release checklist or changelog bots that prepare status for maintainers but do not publish a release by themselves. It can organize evidence for review, but the human maintainer decides whether and how to act.
