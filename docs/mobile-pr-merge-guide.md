# Mobile PR Merge Guide (HC:// Safe Auto Merge and Manual Fallback)

This guide reduces merge friction for mobile maintainers in HC-TRUST-LAYER.

It explains how to handle cancelled Safe Auto Merge jobs, duplicate/concurrency cancellation, unresolved review conversations, and safe manual merge fallback.

This document is advisory-only and preserves human-supervised validation.

## Why this guide exists

On mobile, pull request status can look blocked even when branch content is correct.

Most common confusion patterns:

- a Safe Auto Merge job is cancelled
- a duplicate automation run is cancelled by concurrency controls
- required checks passed, but unresolved review conversations still block merge

A cancelled auto-merge job is not always a code failure.

## Quick Mobile Decision Flow

1. Confirm PR is mergeable (no conflicts).
2. Confirm required checks are successful.
3. Confirm unresolved review conversations are cleared.
4. If Safe Auto Merge was cancelled due to duplicate/concurrency behavior, use manual **Merge pull request** when the above conditions are satisfied.
5. If any required condition is missing, do not merge.

## Cancelled Safe Auto Merge Jobs

### What cancellation can mean

A cancelled Safe Auto Merge job can indicate:

- newer run superseded older run
- duplicate run cancelled by concurrency rules
- queue state changed while checks/reviews were updating

This often reflects automation state management, not a trust-kernel or content defect.

### What to verify first

Before taking action, verify:

- the latest PR commit SHA
- required checks on that latest SHA are successful
- PR is mergeable
- unresolved review conversations status

If required checks on latest SHA are green, a cancelled duplicate auto-merge run is usually non-blocking by itself.

## Duplicate / Concurrency Cancellation

When multiple automation runs are triggered close together, GitHub can cancel an older run.

Interpretation guidance:

- Cancelled duplicate run alone does **not** equal failed verification.
- The authoritative signal is successful required checks on the latest SHA.
- Ignore stale cancelled runs tied to older SHAs once newer required checks pass.

## Unresolved Review Conversation Blocking

Unresolved review conversations can block merge even when all checks pass.

### When to press Resolve conversation

Press **Resolve conversation** when:

- requested change has been applied, or
- reviewer question was answered and no additional code/docs change is needed, and
- thread participants agree closure is appropriate.

Keep resolution tied to clear audit trail context in the thread.

### When not to resolve yet

Do **not** resolve when:

- reviewer requested changes are still pending
- thread shows open disagreement requiring reviewer follow-up
- PR still needs additional evidence for human-supervised validation

## When to use manual Merge pull request

Manual **Merge pull request** is acceptable when all are true:

- PR is mergeable (no conflicts)
- required checks passed on latest SHA
- unresolved review conversations are resolved
- branch reflects intended, reviewed content

This is a safe fallback when Safe Auto Merge was cancelled for duplicate/concurrency reasons.

## When not to merge

Do not merge if any of the following apply:

- required checks are failing or missing on latest SHA
- unresolved review conversations remain
- branch is not mergeable
- trust-kernel-impacting uncertainty remains without human-supervised validation
- cancellation reason is unknown and status evidence is inconsistent

## Mobile Operator Checklist

- [ ] Open PR on mobile and verify latest commit SHA.
- [ ] Confirm required checks are successful on latest SHA.
- [ ] Confirm any cancelled Safe Auto Merge run is duplicate/concurrency related.
- [ ] Open Conversations tab and clear unresolved threads appropriately.
- [ ] Confirm PR shows mergeable state.
- [ ] If auto-merge remains cancelled but all required conditions are satisfied, use manual **Merge pull request**.
- [ ] Record concise merge rationale in PR comments for audit trail continuity.

## Boundary reminders

- Do not weaken guards to force merge.
- Do not bypass reviewer intent by resolving unresolved conversations prematurely.
- Preserve advisory-only verification language.
- Preserve human-supervised validation for non-trivial trust-kernel-impacting changes.
