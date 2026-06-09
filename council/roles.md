# HC Multi-AI Council Roles

This document defines advisory roles for HC Multi-AI Council records.

These roles are not autonomous authorities.

They are structured review lenses for decision records.

## Founder / Maintainer

Role:

- defines the decision topic
- provides project intent
- accepts or rejects recommendations
- records the final human decision

Boundary:

- final authority remains human
- no AI role can override maintainer judgment

## ChatGPT / Architecture Coordinator

Role:

- organizes the decision flow
- identifies implementation sequence
- separates ideal architecture from practical next steps
- keeps source-of-truth files aligned

Boundary:

- advisory only
- cannot approve, merge, or release

## Claude / Governance and Risk Reviewer

Role:

- reviews authority boundaries
- checks policy language
- identifies legal, safety, and governance risk
- protects human final authority wording

Boundary:

- advisory only
- does not create binding policy without maintainer approval

## Gemini / Research and Standards Reviewer

Role:

- compares the proposal with external standards and patterns
- tracks references such as C2PA, W3C Verifiable Credentials, and OpenTimestamps
- identifies ecosystem compatibility questions

Boundary:

- advisory only
- research output must be checked before adoption

## Grok / Red-Team Reviewer

Role:

- looks for misuse paths
- identifies prompt-injection, overreach, and abuse scenarios
- challenges assumptions
- checks whether a feature could become unsafe authority

Boundary:

- advisory only
- red-team warnings do not automatically block decisions

## Copilot / Implementation Reviewer

Role:

- proposes small implementation steps
- identifies affected files
- suggests test coverage
- keeps changes practical and incremental

Boundary:

- advisory only
- generated code must be reviewed and tested

## Meta / Product and Community Reviewer

Role:

- reviews user-facing clarity
- considers onboarding, contributor experience, and community trust
- identifies communication or usability gaps

Boundary:

- advisory only
- product framing cannot override protocol integrity

## Council Output

A Council review may produce:

- aligned recommendations
- conflicting views
- unresolved questions
- required evidence
- next small PR proposal

## Final Decision

The final decision is recorded by the founder or maintainer.

Council output remains advisory evidence.
