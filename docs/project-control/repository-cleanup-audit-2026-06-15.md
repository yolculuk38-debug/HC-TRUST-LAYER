# Repository Cleanup Audit — 2026-06-15

This docs-only audit is advisory evidence for HC-TRUST-LAYER cleanup planning. It does not delete files, move files, edit workflows, edit tests, close issues, delete branches, or add authority-changing automation. The project boundary remains `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, with human final authority required.

## 1. Executive summary

- **Codex/local environment limitation:** Codex could not independently verify remote GitHub state from this container. The local checkout has no configured Git remote, `gh` is unavailable, and direct shell access to the GitHub API returned a network 403.
- **Maintainer/operator verification note:** Live maintainer/operator review identified current open PR #993 during this audit review and current open issue #812, `HC Assistant Console v2`. Issue #812 must remain ACTIVE_KEEP unless explicitly superseded by human review.
- **Whether cleanup is safe now:** Cleanup implementation is **not safe now**. Only this audit report is safe because it is docs-only and changes no protected behavior. Do not close issues, delete branches, or change workflows, tests, source, generated artifacts, or protected files as part of this audit.
- **What must remain active:** Governance, security, release audit, branch protection, code scanning/advisory security, validation, terminology, canonical-artifact, policy, PR guard, inventory, and active assistant/control workflows must remain active pending human review.
- **What is parked:** Branch deletion, issue closure, workflow disable/delete actions, test deletion, orphan-file deletion, generated artifact cleanup, and notification cleanup are PARKED until current GitHub state is reviewed by a human maintainer.
- **What needs human review:** Any cleanup touching protected paths, workflow authority, test coverage, active PRs, active issues, branches not proven merged into `main`, provenance records, generated evidence, or repository-facing operator state.

## 2. Workflow cleanup review

Repository evidence: `.github/workflows` contains 23 workflow files. The audit inspected file names, triggers, permissions, and visible intent from workflow definitions. Cancelled runs caused by concurrency must not be treated as failures when later runs succeeded; current run history was not accessible from this container.

| Classification | Path | Purpose | Trigger type | Mutates repo state | Authority-changing behavior | Latest evidence available | Recommendation | Risk |
|---|---|---|---|---|---|---|---|---|
| KEEP | `.github/workflows/archive.yml` | Archive automation for records, src, docs, qr path changes | `push` path-filtered | No; `contents: read` | No | Local workflow file only | Keep; archive evidence is high-value | Medium |
| PARKED_HIGH_RISK | `.github/workflows/auto-hash.yml` | Auto-generate hash files for verified records | `push` on `records/verified/**.md` | Yes; `contents: write` | Potentially affects provenance artifacts | Local workflow file only | Do not delete; human review required before any disable/change | High |
| KEEP | `.github/workflows/automation-gate.yml` | PR automation boundary check | `pull_request` | No | Advisory gate | Local workflow file only | Keep | Medium |
| KEEP | `.github/workflows/canonical-artifacts.yml` | Canonical artifact boundary guard | `pull_request`, `push` to `main` | No | Guards canonical boundaries | Local workflow file only | Keep | High |
| KEEP | `.github/workflows/docs-auto-merge.yml` | Docs review policy check | `pull_request` | No; read permissions | Advisory auto-merge policy evidence | Local workflow file only | Keep; do not remove auto-merge-related checks without human review | Medium |
| KEEP | `.github/workflows/docs-drift.yml` | Documentation drift check | `pull_request`, `push` to `main` | No | No | Local workflow file only | Keep | Medium |
| PARKED_HIGH_RISK | `.github/workflows/enable-auto-merge.yml` | Evaluates whether PR auto-merge may be enabled | PR lifecycle events | No; read permissions visible | Auto-merge-related policy surface | Local workflow file only | Park; any disable/delete requires human review and proof of inactive/duplicated behavior | High |
| KEEP | `.github/workflows/governance-preflight.yml` | Governance preflight check | `pull_request` | No | Governance evidence | Local workflow file only | Keep | High |
| PARKED_HIGH_RISK | `.github/workflows/hc-assistant-command.yml` | HC Assistant issue-comment command listener | `issue_comment` | Yes; `issues: write` | Comments/assistant command surface | Local workflow file only | Park; verify active console state before changes | High |
| PARKED_HIGH_RISK | `.github/workflows/hc-control-bot-advisory-comment.yml` | HC Control Bot advisory PR comment | `pull_request_target` | Yes; `issues: write` | Uses elevated event context; advisory output | Local workflow file only | Park; requires security/governance review before change | High |
| KEEP | `.github/workflows/hc-control-bot-report.yml` | HC Control Bot report generation | `pull_request` | No | Advisory reporting | Local workflow file only | Keep | Medium |
| KEEP | `.github/workflows/hc-repo-inventory.yml` | Repository inventory evidence | `pull_request`, `workflow_dispatch`, `push` to `main` | Attestation permissions present; no local behavior change made | Evidence artifact surface | Local workflow file only | Keep | High |
| KEEP | `.github/workflows/policy-evaluation.yml` | Advisory policy evaluation | `pull_request` | No | Advisory policy evidence | Local workflow file only | Keep | High |
| CANDIDATE_FOR_REVIEW | `.github/workflows/pr-risk-labeler.yml` | PR risk labeling | `pull_request` | Yes; `pull-requests: write`, `issues: write` | Applies labels, not final authority | Local workflow file only | Review for label allowlist and current usefulness; do not remove blindly | High |
| KEEP | `.github/workflows/pr-scope-guard.yml` | PR scope guard | `pull_request` | No | Advisory scope guard | Local workflow file only | Keep | High |
| KEEP | `.github/workflows/release-audit.yml` | Release audit evidence | `pull_request`, `workflow_dispatch` | No | Release evidence | Local workflow file only | Keep | High |
| PARKED_HIGH_RISK | `.github/workflows/safe-auto-merge.yml` | Safe auto-merge evaluation | `pull_request`, `workflow_run` after Automation Gate | No; read permissions visible | Auto-merge-related policy surface | Local workflow file only | Park; human review required before any change | High |
| KEEP | `.github/workflows/scorecard.yml` | OpenSSF Scorecard advisory | schedule, manual dispatch | No | Security posture evidence | Local workflow file only | Keep | High |
| CANDIDATE_FOR_REVIEW | `.github/workflows/terminology-autofix-suggest.yml` | Advisory terminology fix suggestions | `pull_request` | No | Advisory only | Local workflow file only | Review for overlap with terminology guard; do not delete without run evidence | Medium |
| KEEP | `.github/workflows/terminology.yml` | Terminology guard | `pull_request`, `push` to `main` | No | Boundary language guard | Local workflow file only | Keep | High |
| KEEP | `.github/workflows/validate.yml` | Runtime/schema/test validation | `push` and `pull_request` path-filtered | No | Validation evidence | Local workflow file only | Keep | High |
| KEEP | `.github/workflows/verification-package-schema.yml` | Verification package schema check | `pull_request`, `push` to `main` | No | Schema/evidence boundary | Local workflow file only | Keep | High |
| KEEP | `.github/workflows/verify-archive.yml` | Verify archive on `main` | `push` to `main` | No | Archive evidence | Local workflow file only | Keep | High |

## 3. Test cleanup review

Repository evidence: `tests/` contains broad coverage across runtime behavior, public validator flows, QR guard flows, policy, federation, signing, packages, inventory, assistant/control tooling, and trust graph modules. Because `tests/**` is protected by task scope, no test deletion is safe in this PR.

| Classification | Path | Tested module / behavior | Reason it may be stale or duplicate | Evidence | Safe cleanup recommendation |
|---|---|---|---|---|---|
| KEEP_ACTIVE | `tests/runtime/*` | Runtime hardening, response contracts, telemetry, recovery, redaction | Runtime coverage is safety-adjacent | Files are in dedicated runtime test subtree | Keep active |
| KEEP_ACTIVE | `tests/test_hc_repo_inventory.py` | `scripts/hc_repo_inventory.py` inventory output | Required validation command exists | Script and workflow both exist | Keep active |
| KEEP_ACTIVE | `tests/test_hc_assistant_command.py` | Assistant command listener script | Active workflow exists | `hc-assistant-command.yml` and script exist | Keep active; issue #812 state requires human check |
| KEEP_ACTIVE | `tests/test_hc_control_bot.py`, `tests/test_hc_bot_status.py` | Control bot/status scripts | Active control workflows exist | Matching scripts and workflows exist | Keep active |
| CONSOLIDATE_CANDIDATE | `tests/test_manipulation_detection.py`, `tests/test_manipulation_detection_additional.py`, `tests/test_manipulation_engine.py` | Manipulation signal behavior | Naming suggests overlapping behavior | Similar test names; no import-level duplicate proof gathered | Park; compare assertions before any consolidation |
| CONSOLIDATE_CANDIDATE | `tests/test_qr_guard.py`, `tests/test_qr_hardening.py`, `tests/test_qr_orchestrator_integration.py`, `tests/test_qr_payload_parser.py`, `tests/test_qr_public_validator.py`, `tests/test_qr_record_bridge.py`, `tests/test_qr_security_domain_allowlist.py` | QR parsing, guard, domain allowlist, integration | Dense QR suite may have overlap | Multiple QR-focused files and matching scripts | Keep now; produce a separate test inventory before consolidation |
| CONSOLIDATE_CANDIDATE | `tests/test_public_validator*.py`, `tests/test_public_verification_*.py` | Public validator and verification explorer behavior | Broad public validator/explorer suite may contain navigation duplication | Multiple similarly named public-validator tests | Keep now; documentation navigation fixes before test changes |
| NEEDS_HUMAN_REVIEW | `tests/test_federation_*`, `tests/test_signed_*`, `tests/test_policy_engine.py` | Federation, signing, policy behavior | Protected/high-risk domains | Protected domain coverage | Do not delete or consolidate without protocol/security review |
| STALE_REFERENCE | none proven | Not applicable | No stale test reference was proven by repository search in this pass | Local audit only | Do not delete tests |

## 4. Branch cleanup review

- **Merged branches safe to delete:** None proven. Local checkout only shows current branch state, and remote branches were not available because no Git remote is configured.
- **Stale Codex branches:** Cannot be determined from local evidence.
- **Branches with open PRs:** Cannot be determined from local evidence.
- **Branches that must not be touched:** `main` must never be deleted; any branch with an open PR must not be deleted; any branch not proven merged into `main` must not be deleted.
- **Branches needing human review:** All remote branches until GitHub branch and PR state are reviewed.

Manual GitHub UI steps after human review:
1. Open GitHub repository → **Pull requests** → confirm no open PR uses the branch.
2. Open **Branches** → filter stale Codex branches.
3. For each candidate, confirm it is merged into `main` or explicitly human-approved as abandoned.
4. Delete only the selected branch using GitHub UI branch delete controls.
5. Never delete `main` or protected/release branches.

## 5. Issue cleanup review

Codex/local container could not independently inspect all open issues. Live operator review identified #812 as the active HC Assistant Console v2; it must remain ACTIVE_KEEP. Any other issue cleanup requires separate human-reviewed issue audit. Do not close issues from this PR.

| Classification | Issue | Title | Reason | Evidence | Proposed closing comment | State reason |
|---|---|---|---|---|---|---|
| ACTIVE_KEEP | #812 | HC Assistant Console v2, if still active | User explicitly marked this as active | User instruction; remote issue state unavailable | Not applicable | Not applicable |
| NEEDS_HUMAN_REVIEW | all open issues | Unknown | Remote issue list unavailable | No GitHub CLI, no remote, shell API blocked | Not applicable | Not applicable |

Human issue cleanup process:
1. Export open issues from GitHub.
2. Keep active console, roadmap, governance, release, security, and protected-domain issues.
3. For each completed candidate, verify merged PR evidence.
4. Comment before closure with linked PR evidence.
5. Use `completed`, `duplicate`, or `not_planned` only when evidence supports that state reason.

## 6. GitHub/Codex messages and notification cleanup

Repository PRs cannot clean GitHub inbox state, ChatGPT Codex task lists, or notification messages.

| Classification | Evidence | Cleanup path |
|---|---|---|
| cannot-clean-from-repo | Notifications and Codex task lists are user/account state, not repository files | Manual cleanup only |
| merged PR task record | Recent local git history shows merged PR references through #992 | Mark related GitHub notifications done/read after confirming merge |
| active task record | Current audit task | Keep visible until this audit PR is reviewed |
| duplicate task record | Not proven | Do not archive unless the associated PR is merged or superseded |
| stale Codex task record | Not proven from repo files | Park pending human inbox review |

Manual cleanup instructions:
- Mark merged PR notifications as done/read after confirming the PR is merged.
- Do not create duplicate PRs from completed Codex task outputs.
- Keep only current open PR and active issue tasks visible.
- Ignore or archive old GitHub Mention tasks only after confirming their PR is merged or intentionally superseded.

## 7. Unused / orphan file review

No deletion is recommended in this audit. The repository has many project-control and planning documents that preserve operating history; provenance-preserving records should be parked rather than deleted.

| Classification | Path | Why it looks unused/stale | References found | Risk level | Safe next action |
|---|---|---|---|---|---|
| CANDIDATE_FOR_DOC_NAV_UPDATE | `docs/project-control/*status*.md` | Many narrow status/checkpoint files may be hard to navigate | Directory inventory shows numerous status files | Medium | Add navigation/index guidance before considering archive |
| CANDIDATE_FOR_DOC_NAV_UPDATE | `docs/project-control/hc-control-bot-*.md` | Large cluster of bot boundary/status documents | Directory inventory shows many related files | Medium | Create/refresh an index; do not delete |
| CANDIDATE_FOR_DOC_NAV_UPDATE | `docs/demo/public-validator-*.md` | Multiple demo and quickstart files may overlap | Directory inventory shows several public validator demo files | Low | Review navigation and consolidate references only |
| NEEDS_HUMAN_REVIEW | `generated/**` | Generated evidence may look removable but can preserve audit context | Protected by user instructions | High | Do not delete; follow generated artifact policy |
| NEEDS_HUMAN_REVIEW | `records/**`, `canonical/**`, `schema/**`, `validators/**`, `policy/**`, `federation/**`, `signatures/**` | Protected/provenance domains | Protected by repository and user instructions | High | Do not delete or modify without explicit human-approved scope |
| KEEP | release, audit, provenance, dependency, and security documents | Preserve project evidence and governance continuity | Repository map and governance boundaries | High | Keep |

## 8. Recommended cleanup PR sequence

| PR | Title | Scope | Allowed files | Forbidden files | Validation commands | Risk | Human review requirement |
|---|---|---|---|---|---|---|---|
| A | `docs(project-control): clarify cleanup navigation` | Docs-only navigation/stale-reference cleanup after this audit | `docs/project-control/**` navigation files only | Protected paths, workflows, tests, records, generated evidence | `git diff --check`; `python scripts/check_terminology.py`; `python scripts/check_docs_drift.py`; `python scripts/check_canonical_artifacts.py` | Low | Standard docs review |
| B | `test: inventory duplicate cleanup candidates` | Report-only test duplicate inventory | New docs report or test inventory note only | Test deletion/editing until proven safe | Same docs checks; optional targeted `pytest` after later code/test PR | Medium | Required before any test consolidation |
| C | `docs(governance): document workflow cleanup recommendation` | Human-reviewed workflow disable/delete proposal only | Docs proposal | `.github/workflows/**` unless explicitly approved | Docs checks plus workflow review checklist | High | Required |
| D | `chore(project): close completed issues with evidence` | Issue comments and closures after human approval | GitHub issue UI/API only | Repository files unless a docs ledger is requested | Manual issue audit | Medium | Required |
| E | `chore(project): delete merged stale branches` | Branch deletion after open PR and merge checks | GitHub branch UI/API only | `main`, open-PR branches, unmerged branches | Manual branch audit | High | Required |

## 9. Stop conditions

STOP and request human review if any of the following are true:

- Any protected path deletion is considered.
- Any workflow deletion or disablement is considered.
- Any test deletion lacks full import, coverage, and CI evidence.
- Any open PR exists.
- Any branch is not proven merged into `main`.
- Any issue is still active, including active console, roadmap, governance, release, or security issues.
- Any cleanup would affect source/runtime/security/governance authority.
- Current open PR, issue, or branch state cannot be inspected.

## Validation performed for this audit

Planned validation commands for this PR:

- `git diff --check`
- `python scripts/check_terminology.py`
- `python scripts/check_docs_drift.py`
- `python scripts/check_canonical_artifacts.py`
- `python scripts/hc_repo_inventory.py`

This report itself is advisory only and does not change repository authority.
