# HC Trust Engineer Local Emitter Quickstart

Status: documentation-only quickstart; local-only, advisory, and report-only.

## Purpose

This quickstart shows how to run the local-only HC Trust Engineer emitter against an explicit local JSON input fixture and validate the resulting Operating Loop output envelope.

The quickstart is for maintainer inspection of local advisory output. It does not create canonical repository evidence, change repository state, or replace human review.

## What This Tool Does

The local emitter:

- reads an explicit local JSON input file;
- builds one advisory Operating Loop output envelope;
- injects hard-boundary markers;
- derives risk boundary flags from candidate scope;
- validates output with the local output-contract validator;
- prints JSON only after validation succeeds.

## What This Tool Does Not Do

The local emitter does not:

- read live GitHub state;
- call GitHub APIs;
- call network services;
- run subprocesses;
- create issues;
- create pull requests;
- post comments;
- apply labels;
- request reviewers;
- approve or request changes;
- merge or close PRs;
- mutate repository files;
- write canonical records;
- prove truth, identity, security posture, legal status, production readiness, or merge readiness.

## Basic Command

Run the emitter with the checked-in local sample fixture:

```bash
python scripts/hc_trust_engineer_local_emitter.py --input tests/fixtures/project_control/hc_trust_engineer_local_emitter_input_sample.json
```

The command prints one JSON Operating Loop output envelope to stdout only after local validation succeeds.

## Validate Emitted Output

Use this safe manual validation sequence when you want to inspect a saved local copy:

```bash
python scripts/hc_trust_engineer_local_emitter.py --input tests/fixtures/project_control/hc_trust_engineer_local_emitter_input_sample.json > /tmp/hc-trust-engineer-output.json
python scripts/check_hc_trust_engineer_output_contract.py /tmp/hc-trust-engineer-output.json
```

The `/tmp/hc-trust-engineer-output.json` file is non-canonical local scratch output. It must not be treated as a repository record, canonical artifact, approval, or source of truth.

## Expected Output Sections

The emitted envelope includes these advisory sections:

- `STATE_SUMMARY`
- `CHAIN_STATUS`
- `NEXT_ACTION_CANDIDATE`
- `RISK_BOUNDARY_CLASSIFICATION`
- `HUMAN_HANDOFF_NOTE`

The output is advisory. Human review remains required before any repository action, pull request decision, closure decision, or follow-up work.

## Hard Safety Markers

Every emitted envelope must preserve these exact hard safety markers:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_mutation=false
issue_comment_automation=false
label_reviewer_mutation=false
approval_authority=false
merge_authority=false
```

## Risk-Boundary Behavior

The emitter derives risk flags from candidate scope:

- protected or canonical paths can upgrade risk to `high`;
- workflow scope can set `automation_authority_change=true`;
- runtime, validator, check, governance, or emitter scripts can set `runtime_or_validator_impact=true`;
- `forbidden_scope` alone is a boundary and should not falsely imply the candidate touched that path;
- risk may be upgraded but should not be downgraded.

Risk classification is an advisory aid for human reviewers. It is not approval authority and does not prove safety, correctness, merge readiness, or production readiness.

## Failure Behavior

Failure is intentionally conservative:

- invalid input exits non-zero;
- validator failure exits non-zero;
- partial JSON should not be printed to stdout on failure.

Treat any failure as a reason to inspect the local input, emitted envelope assumptions, and validator output before re-running. Do not bypass validation to create or preserve output.

## Human Handoff

A maintainer should use the output as an advisory handoff aid:

1. inspect the envelope;
2. verify the evidence window;
3. check the risk boundary classification;
4. decide manually whether the next action is useful;
5. never treat the output as approval or merge readiness.

Human maintainers retain final authority for repository action, review, approval, merge, closure, and governance decisions.

## Relationship to Future Work

Future Phase 3 may add optional manual non-canonical artifact output. This quickstart does not add artifact generation, workflow behavior, repository mutation, live repository-state reading, GitHub API access, issue/comment automation, label/reviewer behavior, approval authority, or merge authority.

## Risk Classification

This PR is low risk because it is documentation-only.
