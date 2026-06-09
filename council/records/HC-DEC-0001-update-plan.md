# HC-DEC-0001 Update Plan

This document explains how to update `council/records/HC-DEC-0001.md` after external AI advisory feedback is collected.

It is a planning document.

It does not update the decision record by itself.

## Source decision record

Decision record:

- `council/records/HC-DEC-0001.md`

Related Council support files:

- `council/external-ai-review-prompts.md`
- `council/external-ai-feedback-checklist.md`
- `council/response-collection-guide.md`
- `council/external-ai-response-summary-template.md`

## Update trigger

Update `HC-DEC-0001.md` only after at least the minimum response set is collected:

- one governance or risk review
- one implementation review
- one red-team or abuse-risk review

Research and product/community reviews are recommended before finalizing the decision.

## Sections to update

### Claude / Governance and Risk Reviewer input

Update this section when governance/risk feedback is collected.

Include:

- advisory summary
- recommendation
- authority-boundary warnings
- rejected unsafe suggestions, if any

### Gemini / Research and Standards Reviewer input

Update this section when research/standards feedback is collected.

Include:

- external standards alignment
- C2PA, W3C Verifiable Credentials, or OpenTimestamps relevance
- interoperability concerns
- manual-before-automation recommendations

### Grok / Red-Team Reviewer input

Update this section when red-team feedback is collected.

Include:

- misuse scenarios
- prompt-injection risks
- false-authority risks
- governance bypass concerns
- rejected unsafe suggestions, if any

### Copilot / Implementation Reviewer input

Update this section when implementation feedback is collected.

Include:

- smallest safe implementation step
- affected files
- test or documentation coverage
- automation boundaries

### Meta / Product and Community Reviewer input

Update this section when product/community feedback is collected.

Include:

- contributor clarity
- onboarding impact
- public trust language
- overclaiming risks
- usability recommendations

## Alignment section update

After all collected summaries are added, update:

- agreed points
- conflicting points
- unresolved questions

Do not hide disagreement.

Disagreement is useful audit evidence.

## Evidence requirements update

Update evidence requirements with:

- required docs
- required tests, if any
- required maintainer review
- audit notes
- future hash or witness requirements

## Decision section update

Only a human maintainer may update the final decision.

Allowed final decision statuses:

- approved
- rejected
- deferred
- needs more evidence

Do not mark the decision as approved based only on AI feedback.

## Follow-up update

Update follow-up with the next small PR after maintainer review.

Possible follow-up PRs:

- HC Guide Bot source priority rules
- Council response summary records
- Council hash or audit note preparation
- START_HERE navigation link for operating-layer start guide

## Integrity notes

Preserve these values unless a separate approved governance change modifies the protocol:

- Advisory only: true
- Human final authority: true
- Truth guarantee: false

## Safety boundary

AI feedback can change recommendations.

AI feedback must not become final authority.

The final decision must remain human-authored or human-approved.
