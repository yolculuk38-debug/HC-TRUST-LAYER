# HC Task Handoff Queue

Status: advisory workflow guide.

This document defines the safe queue format for tasks that may be handed to a coding assistant after human review.

## Purpose

The queue turns a human request into a small, reviewable task package.

It does not run an external assistant, create a pull request, approve a pull request, merge, close, label, assign, or change repository state by itself.

## Supported flow

1. The maintainer states the task.
2. HC Trust Engineer splits the task into the smallest safe scope.
3. `scripts/hc_task_handoff.py` can build a local handoff package from a task fixture.
4. The maintainer may paste the handoff package into a coding assistant.
5. Any generated pull request is reviewed by the normal GitHub flow.
6. Comments, review threads, protected-path status, and checks are inspected before merge consideration.

## Required task fields

- task title
- goal
- expected files or allowed path scope
- blocked paths, if any
- evidence required
- validation expected
- human review requirement
- handoff package, if available

## Boundaries

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human final authority remains required
- no automatic external-agent invocation
- no automatic pull request creation
- no automatic approval, close, label, assignment, or merge


## Claim and queue extension

The existing handoff queue prepares safe task packages for human-reviewed work. A claim is an advisory reservation that a human, ChatGPT, Codex, or future HC Trust Engineer automation is working on a task. Claim comes before handoff. Handoff packages what to do. A pull request applies the work. CI and review provide the evidence/check layer. A human maintainer remains the final authority for merge, wait, or close decisions.

This is not a new bot, automation system, or authority path. It extends the existing HC Assistant, HC Trust Engineer, and HC Task Handoff model with coordination language only.

Coordination model:

```text
Issue = discussion / queue / task preparation area
Claim = advisory reservation
Handoff = package for Codex or another coding assistant
PR = applied change
CI = evidence/check layer
Human maintainer = final authority
```

Boundary markers:

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

### Claim states

- `proposed`: a task idea exists, but scope and safety boundaries are not ready.
- `ready`: a maintainer has marked the task as small enough and safe enough to claim.
- `claimed`: a human or coding assistant has an acknowledged advisory reservation.
- `in_progress`: work has started, but no pull request is open yet.
- `pr_open`: a pull request exists for the task.
- `completed`: the task was resolved through review and repository process.
- `released`: the completed work is included in a release or release evidence trail, if applicable.
- `blocked`: the task cannot proceed until a blocker is resolved.
- `stale`: the claim or task appears inactive and needs maintainer review.

### Task ID format

Task IDs should use this format:

```text
HC-TASK-YYYY-NNN
```

Example:

```text
HC-TASK-2026-001
```

Task IDs are coordination aids only. They are not canonical records, proof of truth, approval, or merge authority.

### Manual v0.1 workflow

1. Maintainer or assistant proposes a small task.
2. Task receives a task ID.
3. Task is written into the HC Task Handoff Queue or an HC task handoff issue.
4. Maintainer marks it ready.
5. A human or coding assistant requests claim.
6. Claim is acknowledged manually.
7. Handoff package is generated or written.
8. Codex or another assistant creates a pull request.
9. Pull request follows normal review:
   - changed files;
   - comments;
   - review threads;
   - checks;
   - protected path assessment.
10. Human maintainer decides merge, wait, or close.

### Claim safety rules

- A claim is not approval.
- A claim is not assignment authority.
- A claim is not a reviewer request.
- A claim is not merge readiness.
- A claim is not ownership of the repository.
- A claim can expire or be released.
- A stale claim can be reviewed by a maintainer.
- A task with an open pull request should not be claimed again unless explicitly split.
- Duplicate task work should stop and report instead of opening a second pull request.

### Local claim evaluator

`scripts/hc_task_claim.py` evaluates local task-claim fixtures and prints a machine-readable advisory report.

It evaluates local fixtures only. It does not create claims, write ledgers, call GitHub, automate issue comments, invoke agents, assign labels or reviewers, approve, close, merge, or change repository state.

### Security model

- Issue comments are untrusted input.
- Only explicit `/hc` commands may be parsed in a future implementation.
- Future implementation must bind claim owner to the authenticated GitHub actor, not text inside the comment.
- Governance/config must be read from `main@SHA`.
- Pull request branch code must not be checked out or executed by claim workflows.
- Bot comments must not become downstream automation commands.
- No `pull_request_target` workflow may checkout, import, source, execute, or evaluate pull request branch code.
- No hidden auto-merge path is allowed.

## Example local handoff fixture

```json
{
  "task_title": "Add documentation note",
  "changed_files": ["docs/project-control/example.md"],
  "checks": [
    {"name": "ci", "status": "completed", "conclusion": "success"}
  ]
}
```

Run locally:

```bash
python scripts/hc_task_handoff.py task.json --pretty
```

Use the output as a reviewable task package, not as authority.
