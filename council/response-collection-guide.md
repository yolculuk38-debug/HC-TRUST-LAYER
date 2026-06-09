# Council Response Collection Guide

This guide explains how to collect manual advisory responses from external AI systems for HC Multi-AI Council records.

It is documentation-only.

It does not authorize automation.

## Goal

Collect structured advisory feedback without creating AI authority.

The goal is to improve decision quality while preserving human final authority.

## Source files

Use these files together:

- `council/README.md`
- `council/roles.md`
- `council/decision-template.md`
- `council/external-ai-review-prompts.md`
- `council/external-ai-feedback-checklist.md`
- `council/records/HC-DEC-0001.md`

## Collection sequence

1. Select the Council decision record.
2. Copy the shared context from `external-ai-review-prompts.md`.
3. Select the role-specific prompt.
4. Ask the external AI system manually.
5. Save or summarize the response.
6. Run the feedback checklist.
7. Reject unsafe authority claims.
8. Paste a short advisory summary into the decision record.
9. Keep the final decision pending until maintainer review.

## What to collect

For each AI response, collect:

- AI system name
- assigned Council role
- date collected
- prompt source
- main recommendation
- stated risks
- missing safeguards
- suggested next small PR
- what should not be automated yet
- conflicts with other responses

## What not to collect

Do not collect:

- secrets
- tokens
- private credentials
- private user data
- unsupported claims as facts
- instructions to bypass governance
- automatic merge or approval instructions

## Summarizing responses

When copying into a Council record:

- summarize the response in neutral language
- keep role attribution clear
- separate useful advice from rejected unsafe parts
- preserve disagreements
- preserve uncertainty
- avoid overclaiming consensus

## Unsafe response handling

If an AI response suggests unsafe authority, mark it as rejected.

Examples of unsafe suggestions:

- AI should approve PRs directly
- AI should merge without human review
- Council should vote as final authority
- Guide Bot should write files by default
- Control Bot should bypass CODEOWNERS
- any output should be treated as truth guarantee

## Minimum response set

Before updating a decision record as ready for maintainer decision, collect at least:

- one governance or risk review
- one implementation review
- one red-team or abuse-risk review

Additional research and product/community review are recommended.

## Final decision rule

External AI responses are evidence.

They are not the decision.

The final decision must be written or approved by a human maintainer.
