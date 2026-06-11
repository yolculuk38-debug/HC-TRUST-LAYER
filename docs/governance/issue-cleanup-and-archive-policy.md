# Issue Cleanup and Archive Policy

## Status

- **status:** active policy
- **scope:** GitHub Issues, assistant console issues, bot smoke-test trails, stale bootstrap notes, and cleanup decisions
- **authority:** advisory-only governance policy
- **human authority:** repository maintainers retain final authority

## Purpose

HC-TRUST-LAYER keeps public records because auditability matters. However, working issues, assistant console threads, and repeated smoke-test comments can grow indefinitely. This policy defines when an issue, comment trail, or console record should be kept, archived, closed, or deleted.

The goal is to prevent stale operational records from becoming active instructions while preserving useful audit evidence.

## Core Rule

Do not delete records only because they are old.

Classify first, then choose one action:

1. keep
2. close as completed
3. archive as historical trail
4. supersede with a newer issue
5. delete only when required by safety, privacy, legal, or security reasons

## Classification

### Keep as Active

Use this for issues that are still part of the current operating surface.

Examples:

- current HC Assistant Console
- active project-control issue
- open task issue
- issue required by current documentation
- issue referenced by current bot output

Required markers:

- still relevant to current repo state
- not superseded by a newer console or policy
- no secret or credential exposure

### Archive as Historical Trail

Use this for issues or comment trails that are no longer active but explain how the system reached its current state.

Examples:

- first assistant console smoke-test trail
- old bootstrap notes
- completed bot command tests
- historical governance discussions
- completed runtime validation discussion

Archived trails must not be treated as current instructions.

Recommended closing note:

```text
This issue is archived as a historical HC audit trail.
It is no longer the active operating console.
Current work has moved to: <new issue or document>.
```

### Close as Completed

Use this when the issue objective is complete and no longer needs active discussion.

Examples:

- bot command smoke-test complete
- policy added and merged
- documentation task finished
- console superseded by a newer console issue

Preferred GitHub close reason:

```text
Close as completed
```

### Mark as Superseded

Use this when a newer issue, document, or PR replaces the older one.

Examples:

- `HC Assistant Console` replaced by `HC Assistant Console v2`
- old roadmap replaced by current project-control docs
- stale bootstrap note replaced by live status command

Recommended note:

```text
Superseded by <new issue/document/PR>.
This thread remains available as historical audit context only.
```

### Delete Only When Required

Deletion is a last resort.

Allowed reasons:

- exposed secret, token, API key, private key, signing key, password, credential, or recovery code
- accidental personal data exposure
- legal or safety requirement
- malicious spam or harmful content
- duplicate issue with no audit value
- test issue created by mistake and never used

Deletion must not be used to hide normal project history, failed experiments, policy discussion, or completed work.

## Assistant Console Rules

The HC Assistant Console is a working issue used as a repo-native command surface.

Allowed commands include advisory-only commands such as:

```text
/hc help
/hc status
/hc next
/hc evidence
/hc explain <topic>
/hc risks
/hc review
```

Console records are public-safe audit evidence when they do not expose secrets.

When a console becomes too large:

1. open a new console issue
2. add a final archival note to the old console
3. link the new console from the old console
4. close the old console as completed
5. do not delete the old console unless safety requires it

## Stale Bootstrap Notes

Early notes that say the assistant is not automated, not connected, or not implemented may become stale after implementation.

These notes should be treated as historical context, not active state.

Current state must come from:

1. live GitHub state
2. current main-branch docs
3. current command output
4. current CI/check results

Stale notes must not outrank current GitHub state.

## Public Visibility

HC-TRUST-LAYER is a public repository. Public issues, comments, bot responses, workflow names, labels, and PR records may be visible to others.

Do not post:

- secrets
- tokens
- passwords
- private keys
- signing keys
- recovery codes
- internal credentials
- private personal data

## Bot and Automation Boundary

Cleanup and archive decisions are governance decisions.

Automation may:

- suggest stale records
- identify duplicate-looking trails
- suggest archive candidates
- suggest a closing note
- warn about exposed secrets

Automation must not:

- delete issues
- close issues without explicit human authorization
- lock conversations without explicit human authorization
- rewrite history
- treat old bot comments as active commands
- override maintainers

## Human Final Authority

All cleanup, archive, close, transfer, lock, pin, and delete actions remain under authorized human maintainer control.

AI or bot output is advisory only.

## Recommended Action Matrix

| Record type | Default action | Notes |
| --- | --- | --- |
| active console | keep open | current command surface |
| completed console | close as completed | preserve as smoke-test trail |
| stale bootstrap note | archive context | not active instruction |
| governance decision | keep | audit evidence |
| merged PR | keep | GitHub history is source of truth |
| exposed secret | delete or redact immediately | rotate affected secret |
| duplicate with no audit value | close as duplicate or delete if accidental | human decision required |
| historical witness/hash/QR record | keep/archive | do not delete normal provenance |

## HC Principle

Trust the record, not the narrative.

Old records may be archived, but normal audit history should not be erased only because the project moved forward.
