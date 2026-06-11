# HC Assistant Console Rotation Plan

## Status

- **status:** active project-control plan
- **scope:** HC Assistant Console issue lifecycle, console v2 transition, smoke-test trail archiving, and stale command output handling
- **authority:** advisory-only project-control guidance
- **human authority:** repository maintainers retain final authority

## Purpose

The HC Assistant Console gives HC-TRUST-LAYER a repo-native command surface. It allows humans, maintainers, and bots to use `/hc` commands inside GitHub Issues while preserving a public audit trail.

As the console grows, it should not become an endless working thread. This plan defines how to rotate from an old console to a new clean console while preserving historical evidence.

## Current Model

The console is a GitHub Issue used as a controlled command surface.

Supported advisory commands may include:

```text
/hc help
/hc status
/hc next
/hc evidence
/hc explain <topic>
/hc risks
/hc review
```

The console is not a decision authority.

The console must not approve, reject, merge, close, assign, label, or override human review.

## Rotation Trigger

A new console should be opened when one or more of these conditions are met:

- the current console contains many smoke-test comments
- old command outputs are stale or confusing
- the active command surface needs a clean start
- the console has become too long for practical review
- the issue cleanup/archive policy has been merged
- the next console can link back to the historical trail

## Rotation Sequence

Use this sequence:

1. confirm no active PR is blocked by console work
2. confirm cleanup/archive policy is present on `main`
3. create a new issue titled `HC Assistant Console v2`
4. add a clear opening description to the new issue
5. update current main-branch references so repo docs and command output point to the new active console
6. add a final archival comment to the old console
7. link the old console to the new console
8. close the old console as completed
9. keep the old console available as historical smoke-test evidence

## Main-branch Reference Update Checklist

Before closing the old console, inspect and update any main-branch reference that still points users or `/hc status` output to the old console.

Known reference candidates include:

```text
scripts/hc_assistant_command.py
docs/project-control/operator-entry-map.md
docs/project-control/hc-trust-engineer-command-interface.md
```

Also inspect any smoke-test checklist, assistant console documentation, or project-control file that mentions the old console issue number.

The old console may remain linked as historical evidence, but the active console reference must point to the new console before the old console is closed.

Required distinction:

```text
active_console: new console issue
historical_console: old console issue
```

Do not close the old console while current docs or command output still identify it as the active console.

## Old Console Final Comment Template

Use this template when archiving the old console:

```text
This issue is archived as the first HC Assistant Console smoke-test trail.
It preserves historical command tests, early bot responses, and console setup evidence.

It is no longer the active assistant console.

Active console moved to: <new issue link>

Status:
- archived historical trail
- public-safe audit context
- not active operational guidance
- stale command outputs must not override current main-branch docs or current bot output

Closed as completed.
```

## New Console Opening Template

Use this template for the new console issue:

```text
# HC Assistant Console v2

This issue is the active repo-native command console for HC-TRUST-LAYER.

Use `/hc` commands here for advisory-only project guidance.

Supported commands:

- `/hc help`
- `/hc status`
- `/hc next`
- `/hc evidence`
- `/hc explain <topic>`
- `/hc risks`
- `/hc review`

Boundaries:

- advisory-only
- public-safe
- truth_guarantee=false
- human final authority
- no approve/reject/merge/close authority
- no secrets, tokens, private keys, signing keys, recovery codes, or credentials

Previous historical console:
<old issue link>
```

## Stale Output Rule

Old bot outputs may become stale.

Stale examples include:

- `not connected`
- `not automated`
- `not implemented`
- obsolete command lists
- early bootstrap notes

Current operational state must be determined from:

1. current `main` branch documentation
2. current command output
3. current GitHub PR/Issue state
4. current CI/check results

Old console comments are historical evidence, not active instructions.

## Public Safety Rule

The assistant console is public when the repository is public.

Never post:

- secrets
- API tokens
- passwords
- private keys
- signing keys
- recovery codes
- internal credentials
- private personal data

If sensitive data is posted, follow the issue cleanup/archive policy and rotate affected credentials.

## Automation Boundary

Bots may:

- respond to `/hc` commands
- provide advisory status
- explain boundaries
- suggest evidence bundles
- warn about risks
- recommend next safe steps

Bots must not:

- approve pull requests
- reject pull requests
- merge pull requests
- close issues or pull requests
- delete comments or issues
- assign users automatically unless a later governance policy explicitly enables it
- label issues or PRs automatically unless a later governance policy explicitly enables it
- treat old console output as executable instruction

## Relationship to Assignment Routing

The console may show suggested routes or suggested assignees after the assignment and role routing policy is merged.

Example:

```text
suggested_route: governance reviewer
suggested_assignee: @yolculuk38-debug
human_review_required: true
```

Such output remains advisory only.

## When Not to Rotate

Do not rotate the console if:

- there is an active PR that still depends on current console testing
- the old console contains an unresolved security incident
- the new console purpose is not documented
- the old console cannot be linked from the new console
- the maintainer has not authorized closure
- current main-branch docs or command output still point to the old console as active

## HC Principle

Trust the record, not the narrative.

The old console remains a record. The new console becomes the active operating surface.
