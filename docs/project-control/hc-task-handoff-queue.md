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
