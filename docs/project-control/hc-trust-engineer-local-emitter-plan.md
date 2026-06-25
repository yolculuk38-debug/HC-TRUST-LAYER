# HC Trust Engineer Local Emitter Implementation Plan

Status: documentation-only implementation plan; advisory and report-only.

## Purpose

This plan prepares a future local-only HC Trust Engineer emitter that may generate an Operating Loop output envelope matching the existing output contract and passing the local validator.

This PR does not add the emitter. It defines the implementation plan and safety boundary for a possible future PR.

## Current Source Chain

The future emitter must follow the existing HC Trust Engineer control-plane chain:

- [HC Trust Engineer Closure Report Mode](hc-trust-engineer-closure-report-mode.md)
- [HC Trust Engineer Operating Loop](hc-trust-engineer-operating-loop.md)
- [HC Trust Engineer Operating Loop Output Contract](hc-trust-engineer-operating-loop-output-contract.md)
- local validator: `scripts/check_hc_trust_engineer_output_contract.py`
- sample fixture and tests:
  - `tests/fixtures/project_control/hc_trust_engineer_operating_loop_output_sample.json`
  - `tests/project_control/test_hc_trust_engineer_output_contract.py`

## Future Emitter Scope

A future local emitter should:

- use only the Python standard library;
- run locally;
- accept an explicit local input file or fixture;
- emit one output envelope to stdout or to an explicitly named local file;
- produce output compatible with `scripts/check_hc_trust_engineer_output_contract.py`;
- keep output illustrative and report-only unless fed reviewed repository evidence by a human;
- include the exact hard-boundary markers;
- include required sections and allowed enum values defined by the output contract;
- validate optional closure sections if present.

## Hard Non-Goals

A future local emitter must not:

- call GitHub APIs;
- read live GitHub state automatically;
- create pull requests;
- create issues;
- post comments;
- apply labels;
- request reviewers;
- approve or request changes;
- merge or close PRs;
- modify repository files by default;
- write generated artifacts into canonical paths;
- rewrite records, QR/hash files, schema, agents, or generated artifacts;
- claim truth, identity, security, legal status, production readiness, or merge readiness.

## Input Model

A future implementation may use a small local input model with fields such as:

- `repository`
- `generated_at`
- `evidence_window`
- `open_pr_count`
- `recent_merged_prs`
- `chain_id`
- `chain_type`
- `chain_status`
- `next_action_title`
- `next_action_type`
- `risk_level`
- `known_uncertainties`

This is a planning model only. It is not a schema change, canonical record change, validator change, or repository evidence format.

## Output Model

The emitter output must match [HC Trust Engineer Operating Loop Output Contract](hc-trust-engineer-operating-loop-output-contract.md) and pass:

```bash
python scripts/check_hc_trust_engineer_output_contract.py <output.json>
```

## Validation Sequence

A future local emitter should use this sequence:

1. Read an explicit local input file.
2. Build one output envelope.
3. Inject hard-boundary markers.
4. Validate required sections.
5. Validate enum values.
6. Validate protected path examples.
7. Run the local output-contract validator.
8. Print output only if validation succeeds.
9. Exit non-zero on validation failure.

## Safety Boundary

The following hard markers must appear in every emitted envelope:

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

## Example Future Command

The following command is illustrative only. It is not implemented in this PR.

```bash
python scripts/hc_trust_engineer_local_emitter.py --input tests/fixtures/project_control/example_input.json --validate
```

## Phased Implementation

- Phase 1: Documentation-only local emitter plan.
- Phase 2: Add a local-only emitter script and fixture tests.
- Phase 3: Add optional report-only artifact generation, still local and manual.
- Phase 4: Only after separate human-reviewed approval, consider a workflow dry-run that uploads a non-canonical artifact.

## Risk Classification

This PR is low risk because it is documentation-only and does not add scripts, workflows, automation, repository mutation, or authority.

## Non-Goals for This PR

This PR adds:

- no script;
- no test;
- no workflow;
- no emitter;
- no repository mutation;
- no GitHub API access;
- no issue, comment, label, or reviewer behavior;
- no approval or merge authority.
