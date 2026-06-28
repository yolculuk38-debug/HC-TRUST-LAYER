# HC Agent Task and PR Lifecycle Standard

## 1. Purpose

This document defines a shared HC standard for:

- writing tasks for coding agents
- receiving tasks from humans
- analyzing direct and indirect impact before implementation
- opening PRs
- handling agent, bot, and human review comments
- verifying checks on the current head SHA
- respecting review windows
- resolving threads only after confirming fixes
- merging only after human final review
- producing post-merge audit evidence

This document is advisory and documentation-only. It does not create automation authority. It does not approve, reject, merge, label, assign, request reviewers, or create new or expanded comment authority.

## 2. HC boundary

Boundary flags:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human_review_required=true

AI accelerates work. CI produces evidence. Governance sets boundaries. Audit records what happened. Human maintainer makes the final decision.

Agents must not claim:

- legal truth
- identity finality
- forensic certainty
- certification
- production readiness
- guaranteed correctness
- autonomous governance authority

## 3. Terminology

- **work order**: A bounded HC request that identifies the intended change, review boundary, required evidence, and expected follow-up handling.
- **agent task contract**: The standard task format used to give coding agents enough context, scope, boundary flags, checks, and acceptance criteria to complete work without narrowing the task incorrectly.
- **impact analysis**: A direct and indirect review of HC surfaces that could be affected by a change before implementation begins.
- **PR lifecycle**: The path from task intake through implementation, PR opening, checks, review comments, fix tasks, review window, human final review, merge verification, and post-merge audit.
- **human contributor**: A person preparing, reviewing, validating, or maintaining HC-TRUST-LAYER material.
- **AI-assisted contributor**: A human contributor using AI support while retaining responsibility for the proposed change.
- **coding agent**: An AI system asked to inspect files, edit scoped files, run checks, and report results under HC boundaries.
- **executor**: The role that writes code, documentation, or tests and runs checks within the approved scope.
- **orchestrator**: The role that tracks state, routes work, stores memory, and reports compliance without replacing human final review.
- **HC Control Bot**: A report-only compliance observer that may use the existing advisory single-comment path, without new or expanded comment authority unless a later governed PR explicitly changes that boundary.
- **HC Check Digest**: A summarized evidence view of relevant checks, signals, and review status for human evaluation.
- **maintainer / human final reviewer**: The human role that performs final review and decides whether a PR may merge.
- **report-only**: A mode that observes and reports findings without approving, rejecting, merging, labeling, assigning, requesting reviewers, mutating governance state, or creating new or expanded comment authority.
- **advisory-only**: A boundary that makes output useful for review but not authoritative by itself.
- **compliance signal**: Evidence that a task, PR body, diff, check, thread, or audit step appears aligned or misaligned with HC expectations.
- **protected path**: A path that affects record identity, provenance continuity, policy interpretation, signing expectations, federation behavior, validation semantics, governance controls, or other trust-kernel surfaces.
- **public output**: Any HC-facing output that could shape user, reviewer, maintainer, bot, record, validator, API, CLI, QR, audit, or governance interpretation.
- **generated/canonical artifact**: A generated or canonical file whose meaning, provenance, or review boundary must be preserved.
- **records/evidence**: HC artifacts that preserve what happened, what was checked, what changed, and what remains uncertain.

The executor writes code, documentation, or tests and runs checks. The orchestrator tracks state, routes work, stores memory, and reports compliance. HC Control Bot remains a report-only compliance observer and retains only the existing advisory single-comment path unless a later governed PR explicitly changes that boundary.

## 4. Whole-system impact analysis rule

A task can be implemented in a small PR, but the agent must first analyze the full surrounding HC system.

Every task must consider:

- direct files affected
- adjacent files affected
- user-facing output affected
- public validator output affected
- API output affected
- CLI output affected
- QR output affected
- hash meaning affected
- witness meaning affected
- audit meaning affected
- record meaning affected
- schema affected
- validator affected
- signing affected
- federation affected
- policy affected
- generated/canonical artifact affected
- workflow / CI / bot behavior affected
- tests or evidence affected
- documentation and onboarding affected
- security risk
- governance risk
- rollback or follow-up needs

The agent must not only inspect the requested file. The agent must inspect the surrounding HC surfaces that could be affected by the change.

## 5. HC Agent Task Contract

Future agent tasks should use this standard format:

1. **Title**
   Short PR-style title.

2. **Goal**
   One clear outcome.

3. **Why this exists**
   What problem it solves, why now, and what risk remains if not done.

4. **Context**
   Relevant HC docs, prior PRs, boundary reviews, work order, or project-control files.

5. **Impact analysis**
   Direct and indirect HC surfaces. The agent must think beyond the immediate file.

6. **Scope**
   What this PR must do.

7. **Out of scope**
   What this PR must not do.

8. **Allowed files**
   Explicit file/path allowlist.

9. **Forbidden files**
   Explicit protected or unrelated paths.

10. **Required content or implementation details**
    What must be added or changed.

11. **HC boundaries**
    advisory_only, public_safe, truth_guarantee, human_review_required, and no authority expansion.

12. **Acceptance criteria**
    Concrete pass/fail criteria.

13. **Checks**
    Commands or CI checks expected.

14. **PR body requirements**
    What the PR body must confirm.

15. **Failure rules**
    If uncertain, do not invent. Use “not observed,” “needs confirmation,” or “out of scope.” Ask for clarification or create a follow-up.

16. **Follow-up handling**
    Separate real follow-up items from parked ideas.

## 6. Token-efficient task writing

Future tasks should be concise but complete.

Small docs-only task:

- short context
- clear allowed/forbidden files
- required headings
- checks
- PR body confirmations

Medium task:

- include impact matrix
- include acceptance criteria
- include related docs/tests
- include review risk

Critical HC trust-boundary task:

- include detailed impact analysis
- include protected path reasoning
- include rollback/follow-up
- include public-output and audit implications
- include stronger review requirements

Do not paste the whole project philosophy into every task. Do include the relevant HC boundaries every time. The task should be short enough for the agent to execute, but complete enough that it cannot narrowly misread the work.

## 7. Work order before PR

Ideal flow:

1. Human or system identifies work.
2. Assistant or agent performs whole-system impact analysis.
3. Task is written using HC Agent Task Contract.
4. Agent implements only within scope.
5. Agent opens PR using the current repo PR process.
6. CI and HC checks produce evidence.
7. Review comments are evaluated.
8. Fix tasks are given when needed.
9. Review threads are resolved only after the diff truly addresses them.
10. Review window is respected.
11. Maintainer performs final review.
12. Merge commit is verified.
13. Follow-up status is recorded.

## 8. PR opening standard

Every PR body should make visible:

- what changed
- why it changed
- what problem it solves
- what HC surfaces were considered
- what files changed
- whether it is docs-only, test-only, code/runtime, workflow/CI, schema/validator, records/evidence, generated/canonical, demo/example, public output, governance, or dependency/package work
- what is intentionally out of scope
- what checks ran
- what checks did not run and why
- whether AI assistance was used
- whether the contributor understands and accepts responsibility for the change
- whether any public trust wording changed
- whether any authority changed
- whether follow-up is required

The actual `.github/pull_request_template.md` will be updated in a later PR after this standard is accepted.

## 9. Review comment and fix-task lifecycle

Required process:

- Inspect coding-agent, bot, and human reviewer comments.
- Treat comments as advisory evidence, not final authority.
- Do not dismiss comments because they are automated.
- Lower-priority comments can still be important if they identify false inventory, wrong boundary language, missing template awareness, or misleading claims.
- If a comment is valid, give a clear fix task.
- After the fix, re-check the diff.
- Confirm the comment is outdated or resolved for the right reason.
- Resolve only after confirming the new diff actually fixes the issue.
- Do not resolve a thread merely to make the PR mergeable.
- If unsure, hold merge.

Explicit lifecycle:

comment found -> evaluate -> fix task -> new commit -> verify diff -> check thread state -> resolve if fixed -> continue review

## 10. Review window and merge readiness

The HC review practice includes a 90-second review window.

A PR should not be merged until:

- PR number is confirmed
- current head SHA is confirmed
- PR is open and not draft
- review window has passed
- changed files are inspected
- PR body matches actual diff
- active unresolved non-outdated threads are addressed
- coding-agent, bot, and human comments are evaluated
- checks are verified on current head SHA
- cancelled duplicate runs are interpreted correctly
- forbidden paths are not changed unless explicitly scoped
- no authority expansion is introduced
- human maintainer chooses to merge

Merge-ready does not mean truth-ready. Merge-ready only means the repository change passed the agreed review process.

## 11. Checks and current-head verification

Checks must be evaluated against the current head SHA. Old green checks are not enough after a new commit. Cancelled duplicate automation runs may be acceptable only when a later run on the same head succeeds.

Advisory/report-only checks support review but do not approve or merge. Required, failing, or missing checks require investigation.

HC examples include:

- Docs Drift Check
- Terminology Guard
- Canonical Artifact Boundary Guard
- PR Scope Guard
- HC Control Bot Report
- HC Check Digest
- Governance Preflight
- Automation Gate
- other current repo checks when visible

These examples are evidence or advisory signals unless the repo itself says otherwise. This document does not classify all checks as enforcement checks.

## 12. Post-merge audit

After merge, check:

- PR state is closed
- merged=true
- merge commit SHA recorded
- changed file count recorded when useful
- open PRs checked if continuing work
- follow-up items classified as real next work or parked
- project-control updated only for phase/milestone/high-risk changes
- no state-sync loop for every small PR

## 13. HC Control Bot compliance signals

Future report-only signals HC Control Bot may produce include:

- missing impact analysis
- PR body does not match diff
- allowed/forbidden file scope missing
- docs-only claim but protected path changed
- public-output impact not declared
- generated/canonical impact not declared
- review comment unresolved
- fix task referenced but not reflected in diff
- thread resolved without confirming fix
- review window not respected
- checks not verified on current head SHA
- cancelled run misread as success
- merge commit not verified after merge
- follow-up unclear
- agent added authority it should not have

Initial HC Control Bot behavior remains report-only and advisory-only. The existing advisory single-comment path is preserved. HC Control Bot must not merge, approve, reject, label, request reviewers, close issues, mutate governance state, or add new or expanded comment authority unless a future governed PR explicitly adds such behavior.

## 14. Ideal vs practical path

Ideal:

- shared memory across tasks and agents
- standard task contract
- PR template aligned to task contract
- agent instructions aligned to task contract
- HC Control Bot compliance report
- checks mapped to meaning
- protected paths require stronger review
- human maintainer always final

Practical now:

- write this standard first
- then update the PR template in a later PR
- then add maintainer checklist
- then add HC Control Bot report-only compliance documentation
- only later consider implementation
- do not jump directly to enforcement

## 15. HC operating principle

Trust the record, not the narrative.

Beyan değil, kayıt esastır.

AI accelerates work. CI produces evidence. Governance sets boundaries. Audit records what happened. Human maintainer makes the final decision.

## 16. Follow-up plan

These follow-ups are not part of this PR.

5-2b: Align the existing `.github/pull_request_template.md` with this HC Agent Task and PR Lifecycle Standard.

5-2c: Add a maintainer PR review checklist boundary review.

5-2d: Define HC Control Bot PR lifecycle compliance report behavior.

5-2e: Optionally implement report-only HC Bot PR lifecycle compliance checks after documentation is accepted.

5-3: Protected path contributor guide review.
