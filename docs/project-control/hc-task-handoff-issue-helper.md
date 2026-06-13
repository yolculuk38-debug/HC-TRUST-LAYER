# HC Task Handoff Issue Helper

Status: advisory helper note.

`scripts/hc_task_handoff_issue.py` converts a local GitHub issue-form body into a local task handoff fixture or full handoff package.

It does not call a network, an LLM, GitHub API, workflow API, or repository write API.

## Usage

Save an HC Task Handoff issue body to a local file, then run:

```bash
python scripts/hc_task_handoff_issue.py issue.md --pretty
```

To print only the generated fixture:

```bash
python scripts/hc_task_handoff_issue.py issue.md --fixture-only --pretty
```

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- no external-agent invocation
- no pull request creation
- no approval, close, label, assignment, or merge authority
- human review remains required
