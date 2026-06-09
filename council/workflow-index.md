# HC Multi-AI Council Workflow Index

This index connects the Council documents into one manual workflow.

It is documentation-only.

It does not introduce live automation.

## Purpose

Use this file when you need to understand the full Council workflow from decision question to final human decision.

## Workflow overview

```text
Decision question
        |
        v
Council roles
        |
        v
External AI review prompts
        |
        v
Feedback checklist
        |
        v
Response collection guide
        |
        v
Response summary template
        |
        v
Feedback intake log
        |
        v
Decision record update plan
        |
        v
Human maintainer final decision
```

## Core files

| File | Purpose |
| --- | --- |
| `council/README.md` | Council overview and boundaries |
| `council/roles.md` | Defined advisory roles |
| `council/decision-template.md` | Template for decision records |
| `council/external-ai-review-prompts.md` | Copy-ready prompts for external AI review |
| `council/external-ai-feedback-checklist.md` | Safety checklist for collected feedback |
| `council/response-collection-guide.md` | Collection procedure |
| `council/external-ai-response-summary-template.md` | Summary template for external AI responses |
| `council/records/HC-DEC-0001.md` | First Council decision record |
| `council/records/HC-DEC-0001-update-plan.md` | Plan for updating the first decision record |
| `council/records/HC-DEC-0001-feedback-intake-log.md` | Intake log for external feedback |

## Manual workflow steps

### 1. Define the decision question

Use `council/decision-template.md` or an existing decision record.

### 2. Select advisory roles

Use `council/roles.md` to select which perspectives are needed.

Minimum recommended roles:

- governance or risk reviewer
- implementation reviewer
- red-team or abuse-risk reviewer

### 3. Ask external AI systems manually

Use `council/external-ai-review-prompts.md`.

Do not ask any AI system to approve, merge, release, label, assign, or modify repository files.

### 4. Screen the responses

Use `council/external-ai-feedback-checklist.md`.

Reject unsafe authority claims.

### 5. Summarize responses

Use `council/external-ai-response-summary-template.md`.

Keep summaries neutral and advisory.

### 6. Track intake status

Use `council/records/HC-DEC-0001-feedback-intake-log.md`.

Record pending, collected, accepted, rejected, and unresolved statuses.

### 7. Update decision record only after review

Use `council/records/HC-DEC-0001-update-plan.md`.

Do not update the final decision based only on AI output.

### 8. Final human decision

The final decision must be written or approved by a human maintainer.

## Authority boundary

Council outputs are advisory evidence.

Council outputs do not approve PRs.

Council outputs do not merge PRs.

Council outputs do not release versions.

Council outputs do not replace maintainers.

## Current status

Current decision record:

- `HC-DEC-0001`

Current collection status:

- external feedback pending

Current automation status:

- manual only

## Next safe action

Collect external feedback manually using `council/external-ai-review-prompts.md`.

Then summarize it using `council/external-ai-response-summary-template.md` and record status in `council/records/HC-DEC-0001-feedback-intake-log.md`.
