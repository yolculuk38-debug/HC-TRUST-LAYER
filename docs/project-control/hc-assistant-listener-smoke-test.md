# HC Assistant Listener Smoke Test Checklist

Status: manual smoke test checklist.

This document defines the first safe manual verification pass for the `/hc` issue-comment listener.

It does not change workflow behavior, command behavior, labels, assignments, approvals, merges, closes, runtime behavior, schemas, validators, records, generated artifacts, federation, policy, or LLM usage.

## Scope

Workflow under test:

```text
.github/workflows/hc-assistant-command.yml
```

Parser under test:

```text
scripts/hc_assistant_command.py
```

Active console issue:

```text
#812 HC Assistant Console v2
```

Historical console trail:

```text
#763 first HC Assistant Console smoke-test trail
```

## Required Safety Boundary

Every smoke-test observation must preserve:

```text
advisory_only = true
public_safe = true
truth_guarantee = false
```

The listener must not claim:

- approval;
- rejection;
- merge readiness;
- objective truth;
- production readiness;
- legal validity;
- forensic certainty.

The listener must not perform:

- label application;
- assignment;
- approval;
- rejection;
- request-changes decisions;
- merge;
- close;
- reopen;
- repository file writes;
- LLM calls.

## Manual Test Inputs

Run these as separate comments in the active assistant console issue or a safe test issue.

```text
/hc help
/hc status
/hc next
/hc evidence
/hc explain advisory-only
/hc explain trust-kernel
/hc explain protected-paths
/hc explain commands
/hc risks
/hc review
/hc unknown-command
```

## Expected Behavior

For every command response:

- a comment response is posted under the same issue or pull request;
- the response includes the HC assistant response heading;
- the response includes machine-readable boundary fields;
- `advisory_only` is rendered as true;
- `public_safe` is rendered as true;
- `truth_guarantee` is rendered as false;
- human final authority is stated;
- unsupported commands are ignored safely;
- no label is applied;
- no assignee is changed;
- no review is submitted;
- no pull request or issue is closed;
- no merge action is performed.

## Artifact Check

For each triggered workflow run, verify that the artifact exists:

```text
hc-assistant-command-response-<comment_id>
```

The artifact should include:

```text
hc-assistant-command-result.json
hc-assistant-command-response.md
```

## Negative Input Check

For comments that do not start with `/hc`, expected behavior:

```text
No listener response.
```

Examples:

```text
hello
please review this
hc help
```

## PR Comment Check

On a safe test pull request, run:

```text
/hc review
/hc risks
/hc evidence
```

Expected behavior:

- the parser returns static advisory guidance;
- it does not inspect the PR diff;
- it does not decide PR outcome;
- it does not apply labels or assignments;
- it does not approve, reject, request changes, merge, close, or reopen.

## Pass Criteria

The smoke test passes only if:

- all supported commands respond safely;
- unsupported commands are ignored safely;
- non-`/hc` comments do not produce listener output;
- artifacts are generated;
- all outputs remain advisory-only;
- no authority action occurs.

## Failure Handling

If any command output violates the safety boundary:

1. Disable or revert the listener workflow.
2. Record the failing command and response.
3. Open a governance-reviewed fix PR.
4. Do not expand command behavior until the failure is resolved.

## Final Boundary

This checklist verifies the listener surface only.

It is not a production-readiness certificate.

It is not a truth guarantee.

Human maintainers retain final authority.

Trust the record, not the narrative.
