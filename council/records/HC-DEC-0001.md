# HC-DEC-0001: Establish HC Multi-AI Council and Guide Bot Direction

## Decision metadata

Decision ID: HC-DEC-0001

Date: 2026-06-09

Status: proposed

Related PRs: #732, #733, #734

Related issues: none

Decision owner: Founder / Maintainer

## Topic

Short title: Establish HC Multi-AI Council and Guide Bot direction

Decision question: Should HC-TRUST-LAYER formalize a manual Multi-AI Council decision-record layer and later design a live HC Guide Bot?

Why this matters: The project needs a structured way to preserve founder intent, AI review input, human final authority, and audit-ready decision history before adding more automation.

## Context

Current state:

- HC Control Bot exists as a background advisory GitHub check layer.
- The Council overview has been introduced.
- Advisory Council role definitions have been introduced.
- A manual decision template has been introduced.

Relevant files:

- council/README.md
- council/roles.md
- council/decision-template.md
- docs/project-control/
- docs/governance/
- scripts/hc_control_bot.py

Relevant checks:

- HC Control Bot Report
- Governance Preflight
- PR Scope Guard
- Docs Drift Check
- Advisory Policy Evaluation

Known constraints:

- No autonomous AI authority.
- No LLM voting.
- No automatic merge, approval, label, reviewer, or release authority.
- Human final authority remains required.

## Inputs

### Founder / Maintainer input

Summary: The founder wants a repo-native system that remembers the project direction, coordinates human and AI guidance, and later supports a live guide bot similar to a Copilot-style assistant for HC-TRUST-LAYER.

Recommendation: Build the Council as a manual, auditable decision-record layer first. Add live guide behavior later after governance boundaries are clear.

Risks: Moving too quickly into live automation could create unsafe authority or confusion about whether AI is making final project decisions.

### ChatGPT / Architecture Coordinator input

Summary: The correct architecture is layered: HC Control Bot for background PR checks, HC Guide Bot for live guidance later, and HC Multi-AI Council for structured decision records.

Recommendation: Start with documentation and manual records, then add templates, prompts, hashes, and only later automation.

Risks: Combining all bot functions too early could make the system hard to audit and harder to trust.

### Claude / Governance and Risk Reviewer input

Summary: Pending external input.

Recommendation: Pending external input.

Risks: Pending external input.

### Gemini / Research and Standards Reviewer input

Summary: Pending external input.

Recommendation: Pending external input.

Risks: Pending external input.

### Grok / Red-Team Reviewer input

Summary: Pending external input.

Recommendation: Pending external input.

Risks: Pending external input.

### Copilot / Implementation Reviewer input

Summary: Pending external input.

Recommendation: Pending external input.

Risks: Pending external input.

### Meta / Product and Community Reviewer input

Summary: Pending external input.

Recommendation: Pending external input.

Risks: Pending external input.

## Alignment

Agreed points:

- Council records must remain advisory-only.
- Human final authority must remain explicit.
- Live AI automation should not be added before governance boundaries are clear.
- HC Control Bot and HC Guide Bot should remain separate concepts.

Conflicting points:

- None recorded yet.

Unresolved questions:

- Which external AI responses should be collected first?
- Should decision records be hashed immediately or after the first manual cycle?
- Should Guide Bot begin as documentation, a Custom GPT, or a GitHub App design?

## Evidence requirements

Required tests:

- Not applicable for this documentation-only decision record.

Required docs:

- Council overview
- Council roles
- Council decision template
- First Council decision record

Required audit notes:

- Record that the Council is manual and advisory-only.
- Record that live automation is deferred.

Required human review:

- Founder / maintainer review before merge.

## Decision

Final human decision: pending

Approved scope:

- Manual Council record layer.
- Future prompt packet for external AI review.
- Future HC Guide Bot design document.

Rejected scope:

- Live AI automation in this step.
- LLM voting in this step.
- Any autonomous merge, approval, label, reviewer, or release authority.

Reason: The project should preserve the 7-party advisory idea while keeping implementation safe, auditable, and human-controlled.

## Follow-up

Next small PR: Add prompt packet for external AI Council review.

Owner: Founder / Maintainer

Rollback plan: Revert this documentation record if the Council direction is rejected.

Review date: After external AI feedback is collected.

## Integrity notes

Advisory only: true

Human final authority: true

Truth guarantee: false

Hash or audit reference: pending
