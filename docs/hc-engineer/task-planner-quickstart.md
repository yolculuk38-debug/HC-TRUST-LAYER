# HC Engineer Task Planner Quickstart

This quickstart shows how maintainers and operators can run the deterministic HC Engineer task planner without reading implementation code.

The planner converts a local JSON fixture into a small, ordered, advisory PR plan. It is local-only and does not call a network, call an LLM, write to the repository, open PRs, close PRs, apply labels, assign users, request reviewers, approve, reject, merge, or change merge automation.

## Run the fixture

From the repository root, run:

```bash
python scripts/hc_engineer_task_plan.py examples/hc-engineer/task-plan-fixture.json --pretty
```

The example fixture is a clean docs-only task. Its expected high-level result is:

```text
advisory_only: true
public_safe: true
truth_guarantee: false
planned_pr_count: 1
stop_conditions: []
merge_gate.state: allowed_after_checks
```

## Output fields

| Field | Operator meaning |
| --- | --- |
| `advisory_only` | Always `true`. The planner provides advisory operational evidence only and does not make repository decisions. |
| `public_safe` | Always `true`. The planner output is designed for public repository operations and does not require secrets. |
| `truth_guarantee` | Always `false`. The planner does not certify truth, production readiness, legal conclusions, or forensic certainty. |
| `planned_prs` | Ordered list of proposed small PR slices. The current planner emits one scoped PR plan for the fixture. |
| `planned_pr_count` | Count of planned PR slices. Use it to confirm the task remains small and reviewable. |
| `stop_conditions` | Deterministic blockers that must be resolved before starting, checking, or merging work. |
| `review_order` | Human-readable order of operations for preserving one-open-PR discipline, resolving comments, inspecting checks, and requesting human review where required. |
| `merge_gate` | Advisory merge-readiness summary. `allowed` is false whenever blockers, unresolved comments, pending/failed/skipped checks, protected paths, or scanner-marked human-review signals are present. |
| `post_merge_cleanup` | Follow-up reminders after a PR is merged, including confirming the PR is closed before starting another PR. |

## Required operator examples

Use local fixtures with the same input shape as `examples/hc-engineer/task-plan-fixture.json`. These examples are documentation patterns; keep the fixture data public-safe and evidence-based.

### Clean docs-only task

```json
{
  "task_title": "Document operator flow",
  "changed_files": ["docs/hc-engineer/example.md"],
  "open_prs": [],
  "unresolved_review_comments": [],
  "checks": [
    {"name": "docs", "status": "completed", "conclusion": "success"}
  ]
}
```

Expected operator reading:

```text
stop_conditions: []
merge_gate.state: allowed_after_checks
merge_gate.requires_human_review: false
```

### Open PR blocker

```json
{
  "task_title": "Prepare next docs task",
  "changed_files": ["docs/hc-engineer/example.md"],
  "open_prs": ["889"],
  "unresolved_review_comments": [],
  "checks": [
    {"name": "docs", "status": "completed", "conclusion": "success"}
  ]
}
```

Expected operator reading:

```text
stop_conditions includes: open_pr_exists_stop_before_starting_new_work
merge_gate.state: blocked_or_waiting
```

Do not start another PR until the existing open PR is resolved.

### Unresolved review or Codex comment blocker

```json
{
  "task_title": "Resolve review feedback",
  "changed_files": ["docs/hc-engineer/example.md"],
  "open_prs": [],
  "unresolved_review_comments": ["Codex: clarify skipped-check behavior"],
  "checks": [
    {"name": "docs", "status": "completed", "conclusion": "success"}
  ]
}
```

Expected operator reading:

```text
stop_conditions includes: unresolved_review_comments_resolve_before_checks_or_merge
merge_gate.requires_review_resolution_first: true
merge_gate.state: blocked_or_waiting
```

Resolve Codex and human review comments before relying on checks or considering merge.

### Skipped check requires human review

```json
{
  "task_title": "Review skipped check",
  "changed_files": ["docs/hc-engineer/example.md"],
  "open_prs": [],
  "unresolved_review_comments": [],
  "checks": [
    {"name": "docs", "status": "completed", "conclusion": "skipped"}
  ]
}
```

Expected operator reading:

```text
stop_conditions includes: checks_skipped_require_human_review
merge_gate.requires_human_review: true
merge_gate.state: blocked_or_waiting
```

Skipped checks are manual-review blockers. A human maintainer must inspect why the check was skipped before merge consideration.

### Scanner-marked human-review path without protected path

```json
{
  "task_title": "Update contributor onboarding",
  "changed_files": ["docs/developer-onboarding.md"],
  "open_prs": [],
  "unresolved_review_comments": [],
  "checks": [
    {"name": "docs", "status": "completed", "conclusion": "success"}
  ]
}
```

Expected operator reading:

```text
stop_conditions includes: scanner_human_review_required
merge_gate.requires_human_review: true
merge_gate.state: blocked_or_waiting
```

`docs/developer-onboarding.md` is not a protected path in the path scanner, but it is scanner-marked for version-alignment review. Scanner human-review signals are merge blockers until a human maintainer reviews the route and evidence.

## Boundary

The HC Engineer task planner is an operator aid for HC-TRUST-LAYER review discipline. It preserves `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`; human final authority remains required for repository decisions.
