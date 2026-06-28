# Human Final Reviewer PR Checklist Boundary Review

## 1. Purpose

This document defines the HC-native checklist boundary for human final review of pull requests in HC-TRUST-LAYER.

This document is:

- documentation-only
- advisory
- public-safe
- not automation
- not enforcement
- not an approval mechanism
- not a merge mechanism

The checklist helps the human reviewer decide whether a PR is ready for merge review. The document itself does not approve, reject, merge, label, assign, request reviewers, comment, or mutate governance state.

## 2. HC boundary

Boundary flags:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human_review_required=true

AI accelerates work. CI produces evidence. Governance sets boundaries. Audit records what happened. Human maintainer makes the final decision.

A PR being checklist-ready does not mean the content is legally true, identity-final, forensically certain, certified, production-ready, or guaranteed correct.

It only means the repository change passed the agreed HC review process for that PR scope.

## 3. Reviewer role definitions

- **human final reviewer**: The human reviewer who performs final PR review, evaluates evidence, applies judgment, and determines whether the PR may proceed to a human merge decision.
- **maintainer**: The human role responsible for repository stewardship, governance boundaries, merge decisions, and post-merge audit expectations.
- **contributor**: A human participant proposing a scoped repository change.
- **AI-assisted contributor**: A contributor using AI support while retaining responsibility for the proposed change and its evidence.
- **coding agent**: An AI system asked to inspect files, make scoped edits, run checks, and report results under HC boundaries.
- **executor**: The role that performs the requested file changes and records checks within the approved scope.
- **orchestrator**: The role that tracks state, routes work, stores memory, and reports compliance without replacing human final review.
- **HC Control Bot**: A report-only and advisory-only compliance observer. HC Control Bot remains report-only/advisory-only. The existing advisory single-comment path is preserved. No new or expanded comment authority is created by this document.
- **HC Check Digest**: A summarized evidence view of relevant checks, signals, and review status for human evaluation.
- **PR lifecycle**: The path from task intake through implementation, PR opening, checks, comments, fix tasks, review window, human final review, merge decision, and post-merge audit.
- **review comment**: Advisory evidence from a coding agent, bot, or human reviewer that must be evaluated before merge readiness.
- **fix task**: A specific requested change created after a review comment is evaluated and judged to require action.
- **review thread**: A discussion attached to a changed file, line, or PR review context.
- **outdated thread**: A review thread attached to an older diff context that may no longer match the current head diff.
- **resolved thread**: A review thread marked addressed for repository review purposes; it does not prove truth, correctness, or final authority.
- **current head SHA**: The latest commit identifier for the PR head that checks, comments, and diff review must be evaluated against.
- **review window**: The 90-second human review discipline used before merge readiness is considered.
- **merge readiness**: A review state indicating the PR appears ready for a human merge decision within its scope; it is not a truth claim.
- **post-merge audit**: The after-merge evidence review confirming what happened and what follow-up remains.

## 4. Review stages

### 1. PR discovery

- **Reviewer checks**: Find the PR that matches the task scope and confirm it is the PR under review.
- **Evidence used**: PR title, PR number, branch names, task reference, and repository state.
- **Blocks merge**: Ambiguous PR identity, duplicate same-scope PRs, or mismatch between task and PR.
- **Advisory only**: Search results, summaries, and bot reports.
- **Human judgment required**: Decide whether the discovered PR is the correct review target.

### 2. PR identity confirmation

- **Reviewer checks**: Confirm PR number, title, base branch, head branch, open state, draft state, current head SHA, commit count, changed file count, timestamps, and review window status.
- **Evidence used**: PR metadata, current head SHA, commit list, file list, and timestamps.
- **Blocks merge**: Closed PR, draft PR, stale head SHA, stale checks, or unclear review window.
- **Advisory only**: Cached summaries and older review notes.
- **Human judgment required**: Decide whether the metadata is current enough for review.

### 3. Task and PR body review

- **Reviewer checks**: Compare the task, PR body, stated scope, out-of-scope notes, why-now reasoning, related HC documents, and follow-up classification.
- **Evidence used**: Work order, PR body, project-control references, and acceptance criteria.
- **Blocks merge**: Vague body, missing scope, hidden protected-path impact, or contradiction between task and PR body.
- **Advisory only**: AI-generated summaries and comment interpretations.
- **Human judgment required**: Decide whether the PR body accurately frames the change.

### 4. Changed file review

- **Reviewer checks**: Inspect every changed file and confirm the diff matches the stated scope.
- **Evidence used**: Current diff, file list, additions, deletions, and path names.
- **Blocks merge**: Unexpected file type, unrelated edit, unreviewed changed file, or diff that does not match the PR body.
- **Advisory only**: Diff summaries and inventory comments.
- **Human judgment required**: Decide whether each changed file belongs in this PR.

### 5. Whole-system impact review

- **Reviewer checks**: Consider direct and adjacent HC surfaces that could be affected by the change.
- **Evidence used**: Lifecycle standard impact surfaces, nearby docs, affected outputs, check results, and review comments.
- **Blocks merge**: Unexamined impact on public output, validation meaning, audit meaning, records, schema, workflow, bot behavior, or governance risk.
- **Advisory only**: Surface maps, check digests, and bot reports.
- **Human judgment required**: Decide whether the PR has wider HC impact than the edited file suggests.

### 6. Protected path review

- **Reviewer checks**: Confirm protected or authority-adjacent paths are not changed unless explicitly scoped.
- **Evidence used**: Changed file list, protected path table, task allowlist, and PR body.
- **Blocks merge**: Protected path change without explicit scope, records/evidence mutation without scope, generated/canonical artifact change without scope, or unclear authority expansion.
- **Advisory only**: Protected-path warnings and guard reports.
- **Human judgment required**: Decide whether the scoped justification is sufficient.

### 7. Review comments and thread review

- **Reviewer checks**: Inspect review submissions, inline threads, active unresolved non-outdated threads, outdated threads, and resolved threads where relevant.
- **Evidence used**: Review comments, thread state, current diff, and newer commits.
- **Blocks merge**: Active unresolved non-outdated thread, valid comment not addressed, or thread resolved without verification.
- **Advisory only**: Comments by coding agents, bots, and humans until evaluated.
- **Human judgment required**: Decide whether comments identify real issues for this PR scope.

### 8. Fix task review

- **Reviewer checks**: Confirm each valid comment became a specific fix task and that the new diff addresses it.
- **Evidence used**: Comment, fix instruction, new commit, changed diff, checks, and thread state.
- **Blocks merge**: Vague fix task, missing fix, unverified diff, stale checks after fix, or unresolved applicable thread.
- **Advisory only**: Proposed fixes until confirmed in the current diff.
- **Human judgment required**: Decide whether the fix satisfies the review issue without widening scope.

### 9. Current-head checks review

- **Reviewer checks**: Read checks against the current head SHA and distinguish success, failure, missing, cancelled, advisory, report-only, validation, and enforcement signals.
- **Evidence used**: Current head SHA, check list, check logs, HC Check Digest, and guard outputs.
- **Blocks merge**: Required failing check, required missing check, stale checks, or cancelled duplicate run misread as success.
- **Advisory only**: Report-only checks and advisory guard findings.
- **Human judgment required**: Decide whether checks provide enough current evidence for this scope.

### 10. Review window review

- **Reviewer checks**: Confirm the 90-second review window has passed after PR creation or the latest relevant update.
- **Evidence used**: created_at, updated_at, latest commit time, and current review timing.
- **Blocks merge**: Review window has not passed or timing is unclear.
- **Advisory only**: Automated timing notes.
- **Human judgment required**: Decide whether enough time has passed for comments and checks to settle.

### 11. Merge readiness review

- **Reviewer checks**: Confirm all checklist-ready conditions are met on the current head SHA.
- **Evidence used**: PR metadata, current diff, review comments, thread state, checks, protected path assessment, and review window status.
- **Blocks merge**: Any uncertain or unmet merge-readiness item.
- **Advisory only**: Readiness summaries and bot reports.
- **Human judgment required**: Decide whether to hold merge or proceed to a human merge decision.

### 12. Merge execution or human merge decision

- **Reviewer checks**: Confirm the final merge decision remains with a human maintainer.
- **Evidence used**: Maintainer judgment, repository rules, current PR state, and current checks.
- **Blocks merge**: Tool safety block, stale PR state, unresolved issue, or missing human decision.
- **Advisory only**: Checklist-ready state and reports.
- **Human judgment required**: Decide whether and how to merge within repository boundaries.

### 13. Post-merge audit review

- **Reviewer checks**: Confirm the PR closed as merged and record merge evidence where needed.
- **Evidence used**: PR state, merged flag, merge commit SHA, merged_at timestamp, changed file count, additions, deletions, and follow-up classification.
- **Blocks merge**: This stage occurs after merge; missing audit evidence blocks closeout confidence, not the already-completed merge.
- **Advisory only**: Summaries of post-merge state.
- **Human judgment required**: Decide what evidence belongs in project-control updates and what follow-up remains.

### 14. Follow-up classification

- **Reviewer checks**: Classify remaining work as real next work, parked idea, or not applicable.
- **Evidence used**: PR body, review comments, post-merge audit, project-control state, and current roadmap boundaries.
- **Blocks merge**: Follow-up needed before merge if it is required to make the current PR safe within scope.
- **Advisory only**: Suggested follow-ups until accepted by human review.
- **Human judgment required**: Decide whether follow-up belongs in this PR, later work, or parked notes.

## 5. PR identity confirmation checklist

- [ ] Confirm PR number.
- [ ] Confirm PR title.
- [ ] Confirm base branch.
- [ ] Confirm head branch.
- [ ] Confirm PR is open.
- [ ] Confirm PR is not draft.
- [ ] Confirm current head SHA.
- [ ] Confirm commit count.
- [ ] Confirm changed file count.
- [ ] Confirm created_at and updated_at timestamps.
- [ ] Confirm review window status.

The reviewer must not rely on stale PR numbers, stale head SHAs, stale checks, or older review results after a new commit.

## 6. Task and PR body review checklist

- [ ] PR body explains what changed.
- [ ] PR body explains why it changed.
- [ ] PR body identifies the problem solved.
- [ ] Related work order / issue / task is provided or marked N/A.
- [ ] Related HC standard or project-control document is provided or marked N/A.
- [ ] Why-now reasoning is provided or marked N/A.
- [ ] Residual risk if not merged is provided or marked N/A.
- [ ] Primary change type is selected.
- [ ] If multiple primary types apply, split reasoning is explained.
- [ ] Scope is clear.
- [ ] Out-of-scope is clear.
- [ ] Follow-ups are classified as real next work, parked idea, or not applicable.
- [ ] PR body matches the actual diff.

If the PR body is vague, contradicts the diff, or hides a protected-path impact, the PR should not be treated as merge-ready.

## 7. Changed file and protected path review checklist

- [ ] Changed files match the stated scope.
- [ ] No unexpected file type is changed.
- [ ] No protected path changed unless explicitly scoped.
- [ ] No records/evidence file changed unless explicitly scoped.
- [ ] No generated/canonical artifact changed unless explicitly scoped.
- [ ] No workflow / CI / bot behavior changed unless explicitly scoped.
- [ ] No schema/validator/signing/federation/policy surface changed unless explicitly scoped.
- [ ] No package or dependency surface changed unless explicitly scoped.
- [ ] No runtime/API/CLI/public-output behavior changed unless explicitly scoped.
- [ ] No authority expansion is introduced.

| Surface | Example path group | Reviewer concern | Merge-readiness requirement | Human judgment required |
| --- | --- | --- | --- | --- |
| Review automation | `.github/**` | Workflow, template, or bot behavior may change review evidence or governance flow. | Explicit scope, current-head checks, and clear no-authority-expansion review. | Decide whether automation impact is acceptable for the PR scope. |
| Maintenance scripts | `scripts/**` | Check, report, or validation helper behavior may change repository evidence. | Explicit scope and relevant script validation. | Decide whether behavior and evidence meaning remain bounded. |
| Runtime surface | `src/**` | Runtime, API, CLI, public output, or validator-facing behavior may change. | Explicit scope and relevant behavior checks. | Decide whether user-facing or machine-facing meaning changed safely. |
| Test surface | `tests/**` | Test expectations may weaken or reshape evidence. | Explicit scope and test review. | Decide whether tests preserve validation intent. |
| Schema surface | `schema/**` | Record boundary or validation meaning may change. | Explicit scope and schema-impact review. | Decide whether record meaning remains reviewable. |
| Validator surface | `validators/**` | Public validation behavior or error meaning may change. | Explicit scope and validator-impact review. | Decide whether validation evidence remains accurate within scope. |
| Records/evidence | `records/**` | Provenance-bearing artifacts may change audit meaning. | Explicit scope and evidence-preservation review. | Decide whether record continuity is preserved. |
| Generated artifacts | `generated/**` | Generated output may be mistaken for canonical source. | Explicit scope and generation evidence. | Decide whether generated meaning is clear. |
| Canonical artifacts | `canonical/**` | Canonical references may alter review baselines. | Explicit scope and canonical-boundary review. | Decide whether canonical meaning remains intact. |
| Policy surface | `policy/**` | Governance interpretation may change. | Explicit scope and policy-boundary review. | Decide whether policy impact is acceptable. |
| Federation surface | `federation/**` | Federation assumptions or boundaries may change. | Explicit scope and federation-boundary review. | Decide whether federation meaning remains bounded. |
| Signing surface | `signing/**` | Signing expectations may change. | Explicit scope and signing-boundary review. | Decide whether signing meaning remains clear. |
| Signature evidence | `signatures/**` | Signature-related artifacts may affect trust interpretation. | Explicit scope and signature-evidence review. | Decide whether evidence is preserved. |
| Demo fixtures | `docs/demo/fixtures/**` | Fixture changes may alter demo validation examples. | Explicit scope and fixture-boundary review. | Decide whether fixture meaning remains safe. |
| Ownership boundary | `CODEOWNERS` | Review routing expectations may change. | Explicit scope and governance-boundary review. | Decide whether ownership impact is acceptable. |
| Agent instructions | `AGENTS.md` | Agent operating rules may change. | Explicit scope and instruction-boundary review. | Decide whether agent behavior expectations remain aligned. |
| Bootstrap boundary | `HC_BOOTSTRAP.md` | Bootstrap guidance may affect repository entry and governance understanding. | Explicit scope and bootstrap-boundary review. | Decide whether onboarding meaning remains accurate. |
| Package surface | package / dependency files | Dependencies, packaging, or execution environment may change. | Explicit scope and package-impact review. | Decide whether runtime and supply boundaries remain acceptable. |

## 8. Whole-system impact review checklist

- [ ] Direct files affected were reviewed.
- [ ] Adjacent files were checked where relevant.
- [ ] User-facing output was checked where relevant.
- [ ] Public validator output was checked where relevant.
- [ ] API output was checked where relevant.
- [ ] CLI output was checked where relevant.
- [ ] QR output was checked where relevant.
- [ ] Hash meaning was checked where relevant.
- [ ] Witness meaning was checked where relevant.
- [ ] Audit meaning was checked where relevant.
- [ ] Record meaning was checked where relevant.
- [ ] Schema impact was checked where relevant.
- [ ] Validator impact was checked where relevant.
- [ ] Signing impact was checked where relevant.
- [ ] Federation impact was checked where relevant.
- [ ] Policy impact was checked where relevant.
- [ ] Generated/canonical artifact impact was checked where relevant.
- [ ] Workflow / CI / bot behavior was checked where relevant.
- [ ] Tests or evidence were checked where relevant.
- [ ] Documentation and onboarding were checked where relevant.
- [ ] Security risk was checked where relevant.
- [ ] Governance risk was checked where relevant.
- [ ] Rollback or follow-up need was checked where relevant.

A small PR can still have wide HC impact. The reviewer should verify that the contributor or agent did not inspect only the edited file when the surrounding HC surface matters.

## 9. Review comments and thread rules

Review comments from coding agents, bots, and humans are advisory evidence. They are not final authority by themselves. They must still be evaluated.

- [ ] Review comments were inspected.
- [ ] Review submissions were inspected.
- [ ] Inline review threads were inspected.
- [ ] Active unresolved non-outdated threads were identified.
- [ ] Outdated threads were inspected before being ignored or resolved.
- [ ] Lower-priority comments were evaluated if they identify false inventory, wrong boundary language, missing template awareness, misleading claims, or HC authority confusion.
- [ ] No active unresolved non-outdated thread remains before merge readiness.
- [ ] A thread was not resolved merely to make the PR mergeable.

Thread handling:

- **Active unresolved non-outdated thread**: Blocks merge readiness until addressed or explicitly judged not applicable with evidence.
- **Outdated thread**: Can be non-blocking only after the reviewer confirms the new diff truly addressed the issue or made the old comment no longer applicable.
- **Resolved thread**: Means the discussion was addressed for repository review purposes. It does not prove truth, correctness, or final authority.

## 10. Fix task lifecycle

Required lifecycle:

comment found -> evaluate -> fix task -> new commit -> verify diff -> check thread state -> resolve if fixed -> continue review

- **comment found**: The reviewer identifies a coding agent, bot, or human comment that may affect the PR.
- **evaluate**: The reviewer decides whether the comment is valid, applicable, outdated, lower priority, or not relevant to the PR scope.
- **fix task**: If action is needed, the reviewer gives a specific fix task that preserves HC boundaries.
- **new commit**: The contributor or agent makes a scoped commit to address the fix task.
- **verify diff**: The reviewer compares the new diff against the fix task and confirms the issue was addressed.
- **check thread state**: The reviewer checks whether the relevant thread is active, outdated, or resolved.
- **resolve if fixed**: The reviewer resolves the thread only after confirming the fix in the current diff.
- **continue review**: The reviewer continues the full PR review because one fixed thread does not complete final review.

- [ ] Comment was evaluated before a fix task was given.
- [ ] Fix task was specific.
- [ ] Fix task preserved HC boundaries.
- [ ] New commit was checked.
- [ ] Diff was reviewed after the fix.
- [ ] Checks were re-read after the new commit.
- [ ] Thread state was checked after the fix.
- [ ] Thread was resolved only after confirming the fix.
- [ ] If unsure, merge was held.

## 11. Current-head checks review

- [ ] Checks were evaluated against the current head SHA.
- [ ] Old green checks were not reused after a new commit.
- [ ] Required, failing, or missing checks were investigated.
- [ ] Advisory/report-only checks were treated as evidence, not authority.
- [ ] Cancelled duplicate runs were not treated as success by themselves.
- [ ] Cancelled duplicate runs were accepted only if a later run on the same head succeeded.
- [ ] HC Check Digest was reviewed where available.
- [ ] HC Control Bot Report was reviewed where available.
- [ ] PR Scope Guard was reviewed where available.
- [ ] Docs Drift Check was reviewed where available.
- [ ] Terminology Guard was reviewed where available.
- [ ] Canonical Artifact Boundary Guard was reviewed where available.
- [ ] Governance Preflight was reviewed where available.
- [ ] Automation Gate was reviewed where available.

The checklist must not claim every check is an enforcement check. Checks may be advisory, report-only, validation, or enforcement depending on repo configuration.

## 12. Review window rule

The 90-second review window is an HC review practice for PRs before merge readiness is considered.

- [ ] PR created_at was checked.
- [ ] Latest commit time or update time was considered.
- [ ] Review window has passed before merge.
- [ ] If review window has not passed, merge is held.
- [ ] Review window is a human review discipline, not proof of correctness.

The review window helps prevent rushed merges, stale evaluation, and missed comments. It does not replace diff review, checks, thread review, or human judgment.

## 13. Merge readiness decision

Merge readiness is a review state, not truth.

A PR may be treated as merge-ready only when:

- [ ] PR identity is confirmed.
- [ ] Current head SHA is confirmed.
- [ ] PR is open and not draft.
- [ ] Review window has passed.
- [ ] Changed files were inspected.
- [ ] PR body matches the diff.
- [ ] Scope is clear.
- [ ] Out-of-scope is clear.
- [ ] HC impact surfaces were considered.
- [ ] Protected paths are clear.
- [ ] Active unresolved non-outdated threads are addressed.
- [ ] Review comments were evaluated.
- [ ] Fix tasks were verified.
- [ ] Checks are success or properly understood on the current head SHA.
- [ ] Cancelled duplicate runs are properly interpreted.
- [ ] No forbidden authority is added.
- [ ] Human maintainer chooses to merge.

If any item is uncertain, use “hold merge” rather than guessing.

## 14. Merge execution boundary

This document does not grant merge authority to an agent, bot, CI job, checklist, or report. Merge remains a human maintainer decision.

- Squash/merge/rebase method is not defined by this document.
- Commit title/message policy is not defined by this document.
- Tool safety blocks must be reported honestly.
- If a merge tool is blocked, the reviewer should state that clearly.
- After manual merge, the PR must be re-checked and verified.

## 15. Post-merge audit checklist

After merge, verify:

- [ ] PR state is closed.
- [ ] merged=true.
- [ ] merge commit SHA is recorded.
- [ ] merged_at timestamp is recorded when needed.
- [ ] changed file count is recorded when useful.
- [ ] additions/deletions are recorded when useful.
- [ ] open PRs are checked if work is continuing.
- [ ] follow-ups are classified as real next work or parked.
- [ ] project-control updates are made only for phase/milestone/high-risk changes.
- [ ] no state-sync loop is created for every small PR.

Post-merge audit is part of the HC review lifecycle. It confirms what happened; it does not prove external truth.

## 16. Common hold-merge conditions

- PR body does not match diff.
- Changed files exceed scope.
- Protected path changed without explicit scope.
- Active unresolved non-outdated thread remains.
- Review comment is valid but not fixed.
- Fix task was given but diff does not show the fix.
- Thread was resolved without verification.
- Checks are stale.
- Checks are failing.
- Checks are missing.
- Cancelled run is misread as success.
- New commit arrived after review but checks were not re-read.
- Review window has not passed.
- Authority expansion is unclear.
- HC boundary flags are weakened.
- Public output meaning is unclear.
- Generated/canonical artifact meaning is unclear.
- Records/evidence meaning is unclear.
- Reviewer is unsure.

## 17. HC operating principle

Trust the record, not the narrative.

Beyan değil, kayıt esastır.

AI accelerates work. CI produces evidence. Governance sets boundaries. Audit records what happened. Human maintainer makes the final decision.

## 18. Follow-up plan

These follow-ups are not part of this PR.

- **5-2d**: Define HC Control Bot PR lifecycle compliance report behavior.
- **5-2e**: Optionally implement report-only HC Bot PR lifecycle compliance checks after documentation is accepted.
- **5-3**: Protected path contributor guide review.
