# HC Trust Engineer Report Generator Status

Status: completed local report-only slice

Completed references:

- #872 added the local HC Trust Engineer report generator and tests.
- #873 fixed direct script execution import behavior.

## Current capability

The local report generator converts a local JSON fixture into deterministic advisory JSON.

It reads fixture fields such as:

- repository;
- event type;
- target number;
- base SHA;
- head SHA;
- open PR numbers;
- changed files;
- check state;
- unresolved review threads;
- missing evidence.

It reuses the deterministic HC Control Bot changed-file scanner and returns a structured report with:

- `agent`;
- `mode`;
- `advisory_only`;
- `public_safe`;
- `truth_guarantee`;
- repository and event metadata;
- changed files;
- risk flags;
- check summaries;
- unresolved threads;
- missing evidence;
- stop reasons;
- recommended next action;
- embedded scanner output;
- evidence source.

## Locked boundaries

The report generator is local and report-only.

It does not:

- call a network;
- call an LLM;
- execute PR branch code;
- write to the repository;
- apply labels;
- assign users;
- request reviewers;
- approve pull requests;
- reject pull requests;
- merge pull requests;
- close pull requests or issues;
- claim legal truth;
- set `truth_guarantee=true`.

## Stop behavior

The report recommends `stop` when evidence indicates a review gate, including:

- multiple open PRs;
- pending checks;
- failed checks;
- unresolved review threads;
- missing evidence;
- protected paths touched;
- version-alignment review required.

Otherwise it may recommend `continue` while preserving advisory-only semantics.

## Direct CLI behavior

#873 ensures direct script execution can import the existing HC Control Bot scanner by making the repository root available before the import.

The intended local shape is:

```bash
python scripts/hc_trust_engineer_report.py fixture.json --pretty
```

## Do-not-repeat

Do not repeat #872 or #873 unless new repository evidence shows a defect.

## Next safe action

The next safe action is documentation-only synchronization with project-control state and task ledger, or a narrow fixture/example document showing how to run the local report generator.

Any GitHub Actions integration, issue comment integration, VPS runner, GitHub App runner, label application, assignment, reviewer request, or LLM-assisted layer remains parked until separately authorized by project-control queue and reviewed in its own PR.
