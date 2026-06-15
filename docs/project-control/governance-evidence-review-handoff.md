# Governance Evidence Review Handoff

Status: advisory evidence-review handoff.

This handoff completes the project-control documentation path after #981 and #982. It should be read with `docs/project-control/governance-evidence-review-checklist.md` before any cleanup, source rewrite, branch cleanup, workflow change, ruleset change, release action, or authority-changing automation.

Boundary:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- human final authority remains required
- generated artifacts are advisory evidence, not canonical records
- CI green is evidence, not trust authority

## Do-not-repeat references

Do not repeat the following completed work unless new repository evidence appears:

- #967 repository inventory ledger
- #968 test-anchor detection
- #970 category Markdown inventory views
- #973 actor and PR trace evidence
- #974 HC Large-Repo Operating Model
- #975 large-repo governance automation baseline
- #976 governance automation review findings follow-up
- #977 `.github/CODEOWNERS` protected metadata classification
- #978 AI Agent Supply-Chain Threat Model
- #979 late-review fix for #978
- #980 project-control security hardening sync
- #981 Governance Evidence Review Checklist
- #982 Governance Evidence Checklist State note

## Evidence sources to review next

Review these evidence sources directly before proposing any change that affects files, branches, workflows, rulesets, releases, or governance authority.

| Evidence source | Review target | Handoff instruction | Current checkout gap |
| --- | --- | --- | --- |
| Repository inventory artifacts | JSON and Markdown outputs from the repository inventory workflow, including category views and actor/PR trace fields from #967/#970/#973. | Confirm branch, commit, workflow run, artifact name, generated time, changed-file category, protected-path classification, and whether each finding still matches repository files. Treat review-needed entries as prompts, not deletion-ready facts. | Generated workflow artifacts are not present in this repository checkout. Human reviewers must inspect the matching GitHub Actions artifacts before relying on the inventory output. |
| Test inventory evidence | Inventory test-anchor fields, test category Markdown views, and any root-level integration-script evidence. | Confirm exact, prefix-style, and reference-based anchors from #968 against current repository files before changing tests or source. Missing anchors should become review questions, not rewrite authority. | Generated test inventory artifacts are not present in this repository checkout. Human reviewers must inspect GitHub Actions artifacts and current repository files before proposing test cleanup or source rewrites. |
| Branch-count evidence | Branch-count finding status, reliable branch listing, and GitHub UI branch views. | Confirm branch counts from GitHub source-of-truth before any branch cleanup, archival, deletion, or naming proposal. Connector or generated summaries alone are insufficient. | Live branch listings and generated branch reports are not available from this checkout. Human reviewers must inspect GitHub branch views or trusted platform output. |
| Ruleset readiness reports | Local or workflow-produced ruleset readiness report outputs. | Verify target branch, commit, required checks, protected paths, and human-review preservation before any branch protection, workflow, or ruleset proposal. Do not convert readiness output into bot authority. | Generated ruleset readiness artifacts are not present in this checkout. Human reviewers must inspect GitHub Actions artifacts and repository settings evidence. |
| Scorecard advisory signals | OpenSSF Scorecard JSON artifact evidence, if generated. | Record run date, repository target, branch, commit, signal mapping, and limitations. Use signals as review prompts only; do not imply certification, production readiness, or guaranteed correctness. | Scorecard artifacts are not present in this checkout. Human reviewers must inspect GitHub Actions artifacts before citing signal values. |
| Release audit reports | Deterministic release audit report output, PR references, changed files, and changelog/task-ledger evidence. | Confirm report target, branch, commit, command, missing evidence, and `human_review_required=true` before any release, tag, changelog, or readiness proposal. Do not publish releases or tags from generated reports alone. | Generated release audit artifacts are not present in this checkout. Human reviewers must inspect GitHub Actions artifacts and release-related repository evidence. |

## Next-safe-action boundary

The next safe action is evidence review only. Do not perform cleanup, source rewrite, branch cleanup, workflow change, ruleset change, release action, protected-path change, or authority-changing automation until human reviewers inspect the relevant generated artifacts and repository/platform evidence.

If artifacts cannot be inspected, record the gap as a blocker or follow-up. Do not invent artifact contents, hashes, signatures, approvals, check conclusions, branch counts, Scorecard values, release readiness, or governance authority.
