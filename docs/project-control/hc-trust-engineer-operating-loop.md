# HC Trust Engineer Operating Loop

Status: project-control design note; advisory and report-only.

## Purpose

The HC Trust Engineer Operating Loop is an advisory control-plane process for helping maintainers understand repository state without creating autonomous repository authority.

It helps maintainers understand:

- what changed;
- what was completed;
- what risk remains;
- whether a report chain is ready for closure;
- what the next safe action candidate is.

The loop prepares evidence and recommendations for human review. It does not decide repository truth, approve work, merge work, mutate repository state, or replace maintainer judgment.

## Operating Loop Stages

### A. Repository State Read

Read current repository evidence before proposing action. Inputs may include:

- recent merged pull requests;
- open pull requests;
- project-control documentation;
- check status and CI results.

GitHub is the source of truth for pull request state, merge state, comments, review status, issue state, and check status. Local or generated summaries are advisory aids only and must not override GitHub evidence.

### B. Work Grouping

Group related work into reviewable chains so maintainers can see which items belong together. Example chains include:

- dependency updates;
- project-control report chains;
- bot/control-plane work;
- validator/runtime work;
- documentation governance;
- audit/provenance work.

Grouping is descriptive only. It does not create labels, assignments, project fields, or repository actions.

### C. Completion Assessment

Assess whether each chain appears:

- complete;
- partially complete;
- blocked;
- duplicated;
- stale.

The assessment should state the evidence used and any uncertainty. A completion assessment is not merge authority, approval authority, release authority, or a truth guarantee.

### D. Closure Candidate Detection

Closure candidate detection uses the existing [HC Trust Engineer Closure Report Mode](hc-trust-engineer-closure-report-mode.md) as the narrow stage for report-chain closure review.

The operating loop may propose `READY_FOR_CLOSURE_NOTE` only through closure report mode rules. If closure report mode rules are not satisfied, the loop must output `NOT_READY_FOR_CLOSURE` and state the missing evidence, blocker, or uncertainty.

### E. Next Action Candidate Generation

When the next safe step is clear, the loop may produce a `NEXT_ACTION_CANDIDATE`. The candidate must distinguish one of these action types:

- immediate safe action: a small, reversible step that is ready for human-maintainer consideration now;
- follow-up planning action: a planning or scoping step needed before implementation;
- parked action: a possible future step that should wait for new repository evidence or maintainer direction;
- blocked action: a step that cannot proceed until a stated blocker is resolved.

A next action candidate is advisory only. It is not permission to open a pull request, create an issue, comment, label, assign, request reviewers, approve, close, merge, or mutate repository state.

### F. Risk Boundary Classification

Each candidate must include `RISK_BOUNDARY_CLASSIFICATION` as low, medium, or high risk.

- Low risk: documentation-only, no protected paths, no automation authority.
- Medium risk: scripts, tests, or report-only behavior.
- High risk: workflows, protected paths, issue/comment automation, labels/reviewers, security-sensitive behavior, runtime behavior, or validator behavior.

High-risk candidates require especially explicit human review before any repository-facing work begins.

### G. Human Handoff

The loop ends with a clear `HUMAN_HANDOFF_NOTE` that summarizes the recommendation, uncertainty, risk boundary, and possible maintainer decision points.

The human maintainer decides whether to create a task, pull request, issue, comment, archive action, merge, or do nothing. The operating loop does not create autonomous governance authority for HC Trust Engineer, HC Control Bot, or any other agent.

## Required Outputs

The operating loop may produce these advisory outputs:

```text
STATE_SUMMARY
CHAIN_STATUS
READY_FOR_CLOSURE_NOTE
NOT_READY_FOR_CLOSURE
NEXT_ACTION_CANDIDATE
RISK_BOUNDARY_CLASSIFICATION
HUMAN_HANDOFF_NOTE
```

Output meanings:

- `STATE_SUMMARY`: concise statement of recent repository state and evidence reviewed.
- `CHAIN_STATUS`: grouped status for related work chains.
- `READY_FOR_CLOSURE_NOTE`: closure report mode outcome indicating a report chain appears ready for a human-reviewed closure note.
- `NOT_READY_FOR_CLOSURE`: closure report mode outcome indicating closure evidence is missing, blocked, or unclear.
- `NEXT_ACTION_CANDIDATE`: advisory next step for human-maintainer consideration.
- `RISK_BOUNDARY_CLASSIFICATION`: low, medium, or high risk classification for the candidate.
- `HUMAN_HANDOFF_NOTE`: final maintainer-facing recommendation and decision boundary.

## Hard Boundaries

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

## What It Must Not Do

The operating loop must not:

- open pull requests automatically;
- create issues automatically;
- comment automatically;
- label, assign, or request reviewers automatically;
- approve, close, or merge;
- treat advisory output as command authority;
- rewrite canonical records, QR/hash files, schemas, agents, or generated artifacts;
- bypass human maintainer approval.

## Difference From Closure Report Mode

Closure report mode is one narrow stage inside the broader operating loop.

Closure report mode asks: “Is this report chain ready for a closure note?”

The operating loop asks: “What changed, what is complete, what risk remains, and what should be considered next?”

The broader loop may read state, group work, assess completion, classify risk, and hand a recommendation back to the human maintainer. Only the closure report mode stage may produce `READY_FOR_CLOSURE_NOTE`, and only under its existing rules.

## Real-World Analogy

The operating loop is similar to release management, change advisory boards, CI dashboards, or banking risk review. The system prepares evidence, groups related work, identifies risk, and recommends a next review point. Humans retain authority for decisions and repository actions.

## Example Flow

A project-control report chain has pull requests A, B, and C merged. The operating loop groups them as one chain and checks the relevant project-control documentation and GitHub state. Closure report mode finds no active blocker.

Output:

```text
READY_FOR_CLOSURE_NOTE
HUMAN_HANDOFF_NOTE
```

The human maintainer then decides whether to open a closure-note pull request, defer the action, request more evidence, or do nothing.

## Non-Goals

The operating loop does not provide:

- autonomous governance;
- autonomous release;
- security, truth, legal, or identity guarantee;
- automatic repository mutation;
- full AI agent autonomy.
