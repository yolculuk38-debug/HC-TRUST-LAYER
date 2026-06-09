# External AI Council Review Prompts

This document contains copy-ready prompts for collecting advisory input from external AI systems for HC Multi-AI Council records.

Use these prompts manually.

Do not treat any response as final authority.

Human maintainers remain responsible for all decisions.

## Shared context

Project: HC-TRUST-LAYER

Purpose: Open verification infrastructure for human and AI records using hash, QR, witness, audit, public-safe validation, and advisory governance.

Current Council decision record: HC-DEC-0001

Current question: Should HC-TRUST-LAYER formalize a manual Multi-AI Council decision-record layer and later design a live HC Guide Bot?

Current constraints:

- advisory only
- human final authority
- no autonomous AI authority
- no LLM voting
- no automatic merge, approval, label, reviewer, or release authority
- GitHub audit trail preferred
- small PRs before automation

## Output format requested from each AI

Please answer in this structure:

1. Role perspective
2. Main recommendation
3. Risks
4. Missing safeguards
5. Next small PR suggestion
6. What should not be automated yet
7. One-sentence final advice

## Prompt for Claude / Governance and Risk Reviewer

You are reviewing HC-TRUST-LAYER as a governance and risk reviewer.

Assess the proposed HC Multi-AI Council and future HC Guide Bot direction.

Focus on:

- authority boundaries
- human final authority
- advisory-only wording
- governance risk
- legal or public trust risk
- whether any wording could imply autonomous AI decision power

Use the requested output format.

## Prompt for Gemini / Research and Standards Reviewer

You are reviewing HC-TRUST-LAYER as a research and standards reviewer.

Assess the proposed HC Multi-AI Council and future HC Guide Bot direction.

Focus on:

- alignment with open-source governance patterns
- compatibility with C2PA, W3C Verifiable Credentials, and OpenTimestamps as future references
- public verification architecture
- ecosystem interoperability
- what should remain manual before automation

Use the requested output format.

## Prompt for Grok / Red-Team Reviewer

You are reviewing HC-TRUST-LAYER as a red-team reviewer.

Assess the proposed HC Multi-AI Council and future HC Guide Bot direction.

Focus on:

- misuse scenarios
- prompt injection risks
- AI overreach risks
- false authority claims
- repo governance bypass attempts
- how a malicious contributor might abuse Council records or Guide Bot output

Use the requested output format.

## Prompt for Copilot / Implementation Reviewer

You are reviewing HC-TRUST-LAYER as an implementation reviewer.

Assess the proposed HC Multi-AI Council and future HC Guide Bot direction.

Focus on:

- smallest safe implementation steps
- repo file structure
- test or documentation coverage
- GitHub workflow boundaries
- what should be implemented before any live automation

Use the requested output format.

## Prompt for Meta / Product and Community Reviewer

You are reviewing HC-TRUST-LAYER as a product and community reviewer.

Assess the proposed HC Multi-AI Council and future HC Guide Bot direction.

Focus on:

- contributor onboarding
- public clarity
- trust language
- avoiding overclaiming
- making the project understandable to humans and AI agents
- community safety and expectations

Use the requested output format.

## Collection notes

When responses are collected:

- paste summaries into the relevant HC-DEC-0001 sections
- preserve the original response source when possible
- mark all AI input as advisory
- record conflicts or unresolved questions
- keep final decision human-authored

## Safety boundary

These prompts are for manual advisory review only.

They do not authorize any AI system to merge, approve, release, label, assign, or modify repository files.
