# HC Control Bot Advanced Capability Gate

This policy defines the governance gate for any HC Control Bot capability beyond advisory reporting.

## Current approved mode

The approved HC Control Bot mode is advisory reviewer mode.

The bot may produce deterministic advisory metadata from changed file paths:

- protected paths touched
- governance-adjacent paths touched
- generated artifacts observed
- warnings
- evidence prompts
- review routes
- review priority
- suggested labels

The bot may display this metadata in a best-effort advisory comment when comment writing is available.

## Not yet approved

The following capabilities are not approved by default:

- applying labels
- assigning users or teams
- requesting reviews
- submitting approvals
- submitting request-changes reviews
- closing issues or pull requests
- merging pull requests
- editing governance files automatically
- using LLM memory for repository decisions
- using PR branch content as trusted policy input
- acting as a GitHub App with write authority

## Governance requirement for new capability

Any capability beyond advisory reviewer mode requires a separate governance PR.

That governance PR must include:

1. capability name
2. exact allowed action
3. exact denied actions
4. trigger conditions
5. required evidence
6. rollback procedure
7. incident response rule
8. audit/logging rule
9. human approval requirement
10. test plan

## Minimum safety rules

Any advanced capability must preserve these rules:

- AI remains advisory unless explicitly and narrowly authorized by governance
- human maintainers retain final authority
- governance files must be read from trusted base context
- PR branch content is untrusted input
- no hidden write behavior
- no secret, token, private key, or signing key exposure
- generated artifacts are not canonical records by default
- protected and trust-kernel-adjacent paths require human review

## Capability classes

### Class A: advisory-only

Examples:

- advisory comments
- report artifacts
- evidence prompts
- review routes
- suggested labels
- review priority

Status: allowed when deterministic and public-safe.

The advisory comment must remain informational and must not apply labels, assign reviewers, submit review decisions, close pull requests, or merge pull requests.

### Class B: low-risk metadata write

Examples:

- applying a label from a strict allowlist
- writing non-decision repository metadata from an allowlisted rule

Status: requires separate governance PR before activation.

### Class C: routing authority

Examples:

- assigning maintainers
- requesting reviewers
- routing to teams

Status: requires separate governance PR, protected-path review, and rollback plan.

### Class D: decision authority

Examples:

- approving pull requests
- requesting changes
- closing issues or pull requests
- merging pull requests

Status: not approved for HC Control Bot.

Decision authority remains human-controlled.

### Class E: memory or LLM reasoning

Examples:

- persistent repository memory
- LLM-generated review conclusions
- semantic code review
- autonomous task planning

Status: not approved for write authority.

LLM output may only be considered advisory after a separate governance review.

## Incident rule

If HC Control Bot performs an action outside the approved capability class, the bot must be disabled before expansion continues.

Re-enabling requires:

- incident review
- root-cause note
- policy update if needed
- regression test or workflow guard if applicable
- human maintainer approval

## Operating principle

HC Control Bot supports review.

It does not replace maintainers.

Human final authority remains unchanged.
