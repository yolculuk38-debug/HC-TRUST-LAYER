# HC Council Command Surface

Status: advisory planning
Mode: docs only

Purpose:

This document defines the safe operator command surface for the HC Multi-AI Council Orchestrator after the local report-only runner.

The command surface is a human-supervised entry point. It is not an autonomous maintainer, approval authority, merge authority, protected-path writer, credential manager, or source of truth.

Core rule:

```text
One mobile/operator command may request a council report.
The command surface must not bypass the HC PR gate.
GitHub evidence remains the durable record.
Human final authority remains.
```

## 1. Operator problem

Manual copy-paste across AI tools does not scale.

The operator needs a mobile-friendly way to say:

```text
/hc council review repo
/hc council review pr 123
/hc council risks
/hc council daily
```

The system should convert that command into a bounded report-only council run, not into uncontrolled automation.

## 2. Supported command surfaces

### 2.1 GitHub issue comment command

Initial recommended surface.

Example:

```text
/hc council review pr 1198
```

Expected behavior:

- parse the command;
- validate the requested scope;
- collect only allowed public repository metadata;
- run the local report-only council runner;
- emit a JSON/Markdown advisory report;
- leave an issue or PR comment only if policy permits;
- never approve, merge, close, label, assign, or mutate protected paths automatically.

Why first:

- GitHub is already the durable audit surface;
- the operator can use it from mobile;
- PR/issue context is explicit;
- existing checks and governance gates can inspect the change.

### 2.2 Google Chat command

Later optional surface.

Example:

```text
@HC-Council /hc council review repo
```

Expected behavior:

- forward the command to the same report-only runner;
- return the report summary to the chat space;
- attach or link the durable GitHub evidence record;
- never treat chat text as canonical truth.

Google Chat is a command input channel. It is not the evidence store.

### 2.3 Calendar or Meet session context

Calendar and Meet can provide session context only.

Allowed context:

- meeting title;
- meeting date/time;
- agenda;
- optional meeting link;
- operator-supplied evidence references.

Not allowed:

- treating Meet attendance as AI execution;
- assuming AI systems joined a meeting automatically;
- using transcripts as canonical truth without normalization, review, and hashing;
- leaking private calendar, email, or meeting content into provider prompts.

## 3. Command grammar

Minimum command grammar:

```text
/hc council status
/hc council review repo
/hc council review pr <number>
/hc council risks
/hc council evidence
/hc council daily
```

Command fields:

| Field | Required | Notes |
| --- | --- | --- |
| prefix | yes | must be `/hc council` |
| action | yes | `status`, `review`, `risks`, `evidence`, or `daily` |
| target | conditional | `repo` or `pr <number>` for review commands |
| evidence refs | optional | must be explicit public references or operator-approved local references |

Invalid commands should fail closed with a public-safe error.

## 4. Output contract

Every accepted command should produce a report compatible with:

```text
schema/hc_council_run.schema.json
```

Minimum output guarantees:

- `mode = report_only`;
- `advisory_only = true`;
- `public_safe = true`;
- `truth_guarantee = false`;
- `operator = human_supervised`;
- self-hash in `verification.output_sha256`;
- role-separated model outputs when available;
- synthesis separated from raw outputs.

## 5. Safe command flow

```text
1. Receive command.
2. Normalize command.
3. Reject unknown or ambiguous command.
4. Check open PR discipline.
5. Check target scope.
6. Load only allowed evidence refs.
7. Run local report-only council runner.
8. Validate output against schema.
9. Compute output hash.
10. Emit report-only advisory output.
```

The command surface must stop before any write that would change repository authority.

## 6. Stop conditions

The command surface must stop if any of these are true:

- command is ambiguous;
- target PR is missing or closed when an open PR is required;
- more than one active PR would be affected;
- unresolved review threads exist for a merge-sensitive command;
- checks are pending or failed for a merge-sensitive command;
- protected paths are requested without explicit human authorization;
- private calendar, email, or meeting content would be sent to a provider;
- provider credentials are missing or policy-disabled;
- output cannot be schema-validated;
- output hash cannot be computed deterministically.

## 7. Security boundary

The command surface must not:

- call external AI providers by default;
- store secrets in repository files;
- print secrets in logs;
- use Gmail or Calendar content as implicit evidence;
- convert user text into authority changes;
- approve, reject, merge, close, label, assign, or request reviewers automatically;
- mutate `schema/**`, `validators/**`, `federation/**`, `signatures/**`, `canonical/**`, `policy/**`, `.github/workflows/**`, or `records/**` without explicit PR review.

## 8. Mobile-first operator flow

Recommended mobile flow:

```text
1. Open GitHub mobile/browser.
2. Open the target issue or PR.
3. Comment: /hc council review pr <number>
4. Wait for report-only output.
5. Review risks and next safe actions.
6. Ask ChatGPT or another reviewer to inspect the report.
7. Merge only through the existing human gate.
```

This keeps the operator in control and preserves the record trail.

## 9. Implementation phases

### Phase 0: docs-only command surface plan

- record command grammar;
- record safety boundary;
- keep all changes documentation-only.

### Phase 1: local command parser

Recommended next implementation files:

```text
scripts/hc_council_command.py
tests/test_hc_council_command.py
examples/hc_council_command.example.json
```

Requirements:

- parse commands locally;
- return deterministic JSON;
- no network calls;
- no GitHub writes;
- no provider calls;
- validate public-safe failure cases.

### Phase 2: GitHub issue-command report-only bridge

Requirements:

- read explicit issue/PR command event;
- convert it into a local fixture;
- run the report-only runner;
- post advisory output only after policy checks;
- stop on ambiguity or gate risk.

### Phase 3: Google Chat bridge

Requirements:

- accept slash-style command input;
- forward to the same local runner path;
- write durable report evidence back to GitHub;
- keep chat output as a convenience summary only.

## 10. Current decision

```text
Allowed now: docs-only command surface planning.
Next gate: local command parser with tests.
Not allowed now: live webhook, Google Chat app, provider API execution, auto-merge, or credential handling.
```
