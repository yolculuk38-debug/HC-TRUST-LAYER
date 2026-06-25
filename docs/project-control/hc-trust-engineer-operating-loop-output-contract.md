# HC Trust Engineer Operating Loop Output Contract

Status: project-control output contract; advisory and report-only.

## Purpose

This contract standardizes advisory outputs of the HC Trust Engineer Operating Loop so maintainers can compare reports consistently across pull request chains, project-control chains, and future report-only runs.

The contract defines the required report envelope, advisory output sections, mandatory fields, safety markers, example shape, and human handoff boundaries. It does not add script behavior or repository mutation.

## Source of Truth Rule

GitHub state is the source of truth for pull request state, merge state, comments, review status, issue state, and check status.

Generated summaries are advisory aids only. Local or generated summaries must not override GitHub evidence.

## Required Output Envelope

Every generated operating-loop report must use a top-level envelope with these fields:

- `report_type`
- `generated_at`
- `repository`
- `source_of_truth`
- `evidence_window`
- `advisory_only`
- `public_safe`
- `truth_guarantee`
- `human_review_required`
- `repository_mutation`
- `issue_comment_automation`
- `label_reviewer_mutation`
- `approval_authority`
- `merge_authority`
- `outputs`

The envelope must make the evidence window explicit so reviewers can see which repository state was inspected and where uncertainty may remain.

## Hard Boundary Markers

These exact markers must appear in every generated output envelope:

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

## Required Advisory Output Sections

The `outputs` field may contain the sections below. When a section appears, it must include all required fields listed for that section.

### A. `STATE_SUMMARY`

Required fields:

- `summary`
- `evidence_reviewed`
- `open_pr_count`
- `recent_merged_prs`
- `known_uncertainties`

### B. `CHAIN_STATUS`

Required fields:

- `chain_id`
- `chain_type`
- `related_prs`
- `status`
- `evidence`
- `uncertainty`

Allowed `status` values:

- `complete`
- `partially_complete`
- `blocked`
- `duplicated`
- `stale`
- `unknown`

### C. `READY_FOR_CLOSURE_NOTE`

Required fields:

- `chain_id`
- `reason`
- `evidence`
- `human_action_required`
- `must_follow_closure_report_mode_rules`

### D. `NOT_READY_FOR_CLOSURE`

Required fields:

- `chain_id`
- `missing_evidence`
- `blocker`
- `uncertainty`
- `recommended_follow_up`

### E. `NEXT_ACTION_CANDIDATE`

Required fields:

- `action_type`
- `title`
- `reason`
- `allowed_scope`
- `forbidden_scope`
- `expected_risk`
- `human_decision_required`

Allowed `action_type` values:

- `immediate_safe_action`
- `follow_up_planning_action`
- `parked_action`
- `blocked_action`

### F. `RISK_BOUNDARY_CLASSIFICATION`

Required fields:

- `risk_level`
- `reason`
- `protected_paths_touched`
- `automation_authority_change`
- `runtime_or_validator_impact`

Allowed `risk_level` values:

- `low`
- `medium`
- `high`

### G. `HUMAN_HANDOFF_NOTE`

Required fields:

- `recommendation`
- `decision_needed`
- `safe_next_step`
- `do_not_do`
- `final_authority`

## Illustrative Example

The following example is illustrative only. It is not canonical repository evidence and must not be treated as GitHub state.

```yaml
report_type: hc_trust_engineer_operating_loop
generated_at: "2026-06-25T00:00:00Z"
repository: HC-TRUST-LAYER
source_of_truth: GitHub state for PRs, merges, comments, reviews, issues, and checks
evidence_window: "Example only; no repository state asserted"
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
repository_mutation: false
issue_comment_automation: false
label_reviewer_mutation: false
approval_authority: false
merge_authority: false
outputs:
  - section: STATE_SUMMARY
    summary: "Example report shape for a reviewed project-control chain."
    evidence_reviewed:
      - "Example pull request list"
      - "Example project-control documents"
    open_pr_count: 1
    recent_merged_prs:
      - "#123"
    known_uncertainties:
      - "Example data is illustrative and not repository evidence."
  - section: CHAIN_STATUS
    chain_id: project-control-example-chain
    chain_type: project_control
    related_prs:
      - "#123"
    status: partially_complete
    evidence:
      - "Example project-control report reference"
    uncertainty:
      - "Maintainer review still required."
  - section: NEXT_ACTION_CANDIDATE
    action_type: follow_up_planning_action
    title: "Prepare a small docs-only follow-up plan"
    reason: "Example chain has a possible documentation gap."
    allowed_scope:
      - "docs/project-control/**"
    forbidden_scope:
      - "records/**"
      - "schemas/**"
      - "scripts/**"
    expected_risk: low
    human_decision_required: true
  - section: RISK_BOUNDARY_CLASSIFICATION
    risk_level: low
    reason: "Example candidate is documentation-only and does not change authority."
    protected_paths_touched: false
    automation_authority_change: false
    runtime_or_validator_impact: false
  - section: HUMAN_HANDOFF_NOTE
    recommendation: "Human maintainer may review whether a docs-only planning PR is useful."
    decision_needed: "Approve, defer, or reject the suggested follow-up."
    safe_next_step: "Review GitHub evidence before opening any PR."
    do_not_do: "Do not comment, label, approve, merge, or mutate repository state automatically."
    final_authority: "Human maintainer"
```

## Closure Note Relationship

`READY_FOR_CLOSURE_NOTE` and `NOT_READY_FOR_CLOSURE` must follow [HC Trust Engineer Closure Report Mode](hc-trust-engineer-closure-report-mode.md).

This operating loop output contract does not expand closure authority. A closure recommendation remains advisory and human-reviewed.

## Non-Goals

This contract does not add or perform:

- scripts;
- workflows;
- issue or comment automation;
- label or reviewer changes;
- approvals or merges;
- canonical record rewrites;
- QR/hash file rewrites;
- schema rewrites;
- agent rewrites;
- generated artifact rewrites;
- truth, legal, security, identity, or production-readiness guarantees.

## Future Implementation Note

Future report-only scripts may emit this contract, but any implementation must remain report-only unless a later human-reviewed pull request explicitly changes the boundary.
