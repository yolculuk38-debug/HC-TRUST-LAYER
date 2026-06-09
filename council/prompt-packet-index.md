# Council Prompt Packet Index

This index identifies what to copy when asking external AI systems for HC Multi-AI Council advisory feedback.

It is documentation-only.

It does not authorize automation.

## When to use this file

Use this file when manually asking Claude, Gemini, Grok, Copilot, Meta/Product review, or another external reviewer for advisory input.

## Required source files

Before asking an external AI system, use these files as the source packet:

1. `council/workflow-index.md`
2. `council/roles.md`
3. `council/external-ai-review-prompts.md`
4. `council/external-ai-feedback-checklist.md`
5. `council/records/HC-DEC-0001.md`

Optional support files:

- `council/response-collection-guide.md`
- `council/external-ai-response-summary-template.md`
- `council/records/HC-DEC-0001-update-plan.md`
- `council/records/HC-DEC-0001-feedback-intake-log.md`

## Copy order

Copy in this order:

1. Project context from `council/external-ai-review-prompts.md`
2. Decision question from `council/records/HC-DEC-0001.md`
3. Role-specific prompt from `council/external-ai-review-prompts.md`
4. Advisory-only reminder from this file

## Advisory-only reminder

Paste this reminder at the end of each external AI request:

```text
Important boundary:
Your response is advisory only.
Do not approve, reject, merge, release, label, assign, or modify repository files.
Do not claim final authority.
Do not claim truth guarantee.
Human maintainer final authority remains required.
```

## Target reviewers

| Reviewer | Suggested role |
| --- | --- |
| Claude | Governance and Risk Reviewer |
| Gemini | Research and Standards Reviewer |
| Grok | Red-Team Reviewer |
| Copilot | Implementation Reviewer |
| Meta/Product reviewer | Product and Community Reviewer |

## Expected response shape

Ask each reviewer to answer in this shape:

1. Role perspective
2. Main recommendation
3. Risks
4. Missing safeguards
5. Next small PR suggestion
6. What should not be automated yet
7. One-sentence final advice

## After receiving a response

After receiving each response:

1. Screen it with `council/external-ai-feedback-checklist.md`.
2. Summarize it with `council/external-ai-response-summary-template.md`.
3. Track it in `council/records/HC-DEC-0001-feedback-intake-log.md`.
4. Do not update the final decision until maintainer review.

## Final boundary

External AI feedback is evidence.

It is not the decision.

Final decision authority remains human.
