# Remote Branch Inventory — 2026-07-22

## Executive summary

This report records a complete, report-only remote branch inventory for HC-TRUST-LAYER at `2026-07-22T11:59:19Z`, before the report branch itself was created.

Snapshot anchor:

- repository: `yolculuk38-debug/HC-TRUST-LAYER`
- default branch: `main`
- `main` SHA: `e7ad2cfb387e5ae4a20779401465353a3761c1a2`
- open pull requests: `0`
- remote branches including `main`: `113`
- non-`main` remote branches: `112`
- protected branches: `1` (`main` only)
- unprotected non-`main` branches: `112`

Classification result:

| Classification | Count | Meaning |
| --- | ---: | --- |
| `KEEP_PROTECTED` | 1 | `main`; never a cleanup target. |
| `DELETE_CANDIDATE_REACHABLE` | 46 | Branch tip is already reachable from the anchored `main` history. |
| `DELETE_CANDIDATE_MERGED_PR_HEAD` | 30 | Branch tip exactly matches the recorded head SHA of a merged pull request; this covers squash-merge cases where the original head commit is not an ancestor of `main`. |
| `HOLD_CLOSED_UNMERGED` | 32 | Branch tip is tied to a closed but unmerged pull request. Preserve until a separate content-equivalence or intentional-abandonment review is completed. |
| `HOLD_UNMAPPED` | 4 | No exact pull-request head mapping was confirmed. Preserve until separately investigated. |

The two candidate classes total `76`; the two hold classes total `36`. Candidate status is evidence for a later human-reviewed deletion decision, not deletion authority. No branch is deleted by this report.

The branch used to publish this report is outside the anchored snapshot. It must remain active while its pull request is open and must be evaluated separately after merge.

Boundary values:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- CI/checks are evidence, not trust authority
- human final authority remains required

## Evidence method

The inventory used independent Git and GitHub evidence:

1. `git fetch --prune origin` refreshed all `refs/heads/*` remote-tracking references.
2. `git for-each-ref refs/remotes/origin` counted every remote branch while excluding the local symbolic `origin/HEAD` alias.
3. Reachability from the anchored `origin/main` classified 46 branch tips as already contained in `main` history.
4. GitHub pull-request head refs mapped the remaining branch tips to candidate PR numbers.
5. Live GitHub PR metadata verified merged state and exact `head_sha` equality for 30 additional branches.
6. Live GitHub PR search verified that no pull request was open at the snapshot time.
7. GitHub's branch API listed all 113 branches and reported only `main` as protected.

The exact-tip requirement matters. A branch is not placed in the merged-PR candidate class merely because its name resembles completed work; its current tip must equal the merged PR's recorded head SHA. A branch with later commits is held.

## `DELETE_CANDIDATE_REACHABLE` — 46

- `chatgpt/audit-snapshot-core` — tip `2257d131ae0b` reachable from `main`.
- `chatgpt/export-import-verification-core` — tip `b69a7c9cb702` reachable from `main`.
- `chatgpt/full-report-triage` — tip `b0e6b1b97cec` reachable from `main`.
- `chatgpt/pr142-adaptive-risk` — tip `3c09e1463219` reachable from `main`.
- `chatgpt/protocol-source-of-truth` — tip `50a48ef8e3ce` reachable from `main`.
- `chatgpt/qr-spoof-negative-input-tests` — tip `da46755cef9f` reachable from `main`.
- `chatgpt/source-social-vision-clean` — tip `9597dcaea303` reachable from `main`.
- `chatgpt/sync-evidence-artifact-review-state` — tip `0305227ee962` reachable from `main`.
- `codex/create-python-package-structure-for-hc-trust-layer` — tip `d7aed88857f4` reachable from `main`.
- `codex/report-governance-index` — tip `f09e490e25c9` reachable from `main`.
- `codex/report-index` — tip `f09e490e25c9` reachable from `main`.
- `codex/report-lifecycle-standard` — tip `f09e490e25c9` reachable from `main`.
- `codex/reports-index` — tip `f09e490e25c9` reachable from `main`.
- `codex/signal-watch-console-issue-model` — tip `6bd6ef7826b4` reachable from `main`.
- `cont221` — tip `41ed03984f81` reachable from `main`.
- `core/package-hash-core-2` — tip `755558370396` reachable from `main`.
- `core/package-hash-core-3` — tip `755558370396` reachable from `main`.
- `core/package-hash-core-4` — tip `755558370396` reachable from `main`.
- `core/package-hash-core-5` — tip `755558370396` reachable from `main`.
- `core/verification-package-hash-core` — tip `755558370396` reachable from `main`.
- `docs-codex-issue-handoff-workflow` — tip `fb5f7d3866a4` reachable from `main`.
- `docs-council-claude-governance-intake` — tip `2ea0ceef5fa9` reachable from `main`.
- `docs-council-gemini-research-standards-summary` — tip `30cfad12fec4` reachable from `main`.
- `docs-council-manual-only-boundary` — tip `37ff7578428a` reachable from `main`.
- `docs-council-workflow-index` — tip `bc04c5121f2b` reachable from `main`.
- `docs-public-validator-mvp-spec` — tip `c74ae9dc3bd8` reachable from `main`.
- `docs-sync-839` — tip `549cd4e974b5` reachable from `main`.
- `docs/record-console-rotation-state` — tip `7955e17f8676` reachable from `main`.
- `docs/source-inventory-output-review` — tip `03668193c73e` reachable from `main`.
- `docs/sync-operating-layer-console-state` — tip `7955e17f8676` reachable from `main`.
- `docs/update-active-console-reference` — tip `f903feb39d8e` reachable from `main`.
- `graph198` — tip `0ea35e7246cf` reachable from `main`.
- `hc-bot-signal-watch-explain` — tip `a40637b5546f` reachable from `main`.
- `inventory-actor-pr-trace-model` — tip `4e45b4fda4d5` reachable from `main`.
- `inventory-anchor` — tip `4b3a5fb5493c` reachable from `main`.
- `ledger-875` — tip `a5b834a4e8c5` reachable from `main`.
- `manifest226` — tip `e4f7c6217289` reachable from `main`.
- `nx1` — tip `72530e4d37ca` reachable from `main`.
- `pc-sync-875` — tip `a5b834a4e8c5` reachable from `main`.
- `policy215` — tip `2d5f8c0ff173` reachable from `main`.
- `pub224` — tip `6170e950bb47` reachable from `main`.
- `recovery207` — tip `8cea3998c98c` reachable from `main`.
- `runtime-pipeline-nested-contract-keys` — tip `9b155297ff41` reachable from `main`.
- `source-inventory-reporter` — tip `57b5f1b23d88` reachable from `main`.
- `sync901` — tip `46d7e03e916e` reachable from `main`.
- `temp-test-noop` — tip `c914e364d3b2` reachable from `main`.

## `DELETE_CANDIDATE_MERGED_PR_HEAD` — 30

- `bot-status-boundary-note` — merged PR #956; tip `3a189afa5684`.
- `chatgpt/add-hc-control-bot-authority-policy` — merged PR #690; tip `59e468f95b91`.
- `chatgpt/issuer-identity-flag` — merged PR #928; tip `320ea2f6bd1a`.
- `chatgpt/link-vision-docs` — merged PR #679; tip `bafc0e9febbc`.
- `chatgpt/source-social-verification-vision` — merged PR #677; tip `3b18ca45adf3`.
- `codex/add-ci-automation-test-documentation` — merged PR #12; tip `84798ff2b5d5`.
- `codex/add-hc-trust-normalize-cli-command` — merged PR #7; tip `f9dd9fad5415`.
- `codex/add-mvp-1-viewer-trust-summary-score-band` — merged PR #344; tip `207197521152`.
- `codex/add-public-validator-mvp-specification` — merged PR #820; tip `916487856e5e`.
- `codex/align-dependency-declarations-for-pytest` — merged PR #587; tip `3a8a50b1aa2f`.
- `codex/clean-and-document-project-dependencies` — merged PR #11; tip `ba2b46f3ac1e`.
- `codex/create-github-pages-link-audit-report` — merged PR #635; tip `b4a217afb424`.
- `codex/create-public-validator-mvp-readiness-pr` — merged PR #637; tip `5b6495a1da42`.
- `codex/document-qr-public-verifier-limitations` — merged PR #593; tip `cd0825c8ce55`.
- `codex/fix-codex-review-findings-in-pr-#888` — merged PR #889; tip `a1f574d4be84`.
- `codex/fix-github-actions-failures-after-hc_trust-merge` — merged PR #4; tip `17854f057159`.
- `codex/fix-qr-generator-canonical-verification-url` — merged PR #592; tip `2f70c3cbb393`.
- `codex/fix-typeerror-in-schema-validation` — merged PR #5; tip `ea429214e4ee`.
- `codex/improve-hc-trust-cli-help-and-experience` — merged PR #8; tip `76de32bd2ae4`.
- `codex/improve-hc-trust-cli-help-and-ux` — merged PR #9; tip `468e7f8c5386`.
- `codex/improve-readme-for-clarity-and-onboarding` — merged PR #6; tip `0d1dbcf60271`.
- `codex/review-and-clean-project-dependencies` — merged PR #10; tip `3d500574589d`.
- `codex/update-active-issue-reference-in-hc-assistant-console` — merged PR #813; tip `b7e0a65adb32`.
- `docs-hc-control-bot-product-surface-awareness` — merged PR #707; tip `ced5302e4126`.
- `docs/hc-assistant-console-rotation-plan` — merged PR #811; tip `499ca7671ae7`.
- `docs/update-smoke-test-console-reference` — merged PR #814; tip `1b54c16f99bc`.
- `fix/cli-summary-escape-values` — merged PR #959; tip `fbdfe147f8e9`.
- `hc-next-command-parser` — merged PR #767; tip `88a7258ca7ea`.
- `raise-python-support-to-3-14` — merged PR #786; tip `1540e73dbbcf`.
- `witness-proof-proposal` — merged PR #866; tip `8d55749d3721`.

## `HOLD_CLOSED_UNMERGED` — 32

- `chatgpt/historical-path-inventory-pass-2026-06-16` — closed-unmerged PR #1028; tip `d29428b2f6b8`.
- `codex/add-combined-qr-bridge-and-local-validator-result` — closed-unmerged PR #671; tip `85e31c0471ab`.
- `codex/add-end-to-end-hc-/-verification-demo-record` — closed-unmerged PR #358; tip `250dd325b366`.
- `codex/add-fastapi-service-foundation-and-routes` — closed-unmerged PR #263; tip `865db4d66054`.
- `codex/add-hc-check-digest-v1-script` — closed-unmerged PR #1065; tip `528cbb61c96d`.
- `codex/add-httpx-as-test-dependency` — closed-unmerged PR #447; tip `49774532c9bc`.
- `codex/add-record-detail-pages-to-explorer` — closed-unmerged PR #529; tip `a35ac1236095`.
- `codex/add-validator-orchestration-architecture-scaffold` — closed-unmerged PR #405; tip `de1983439ccd`.
- `codex/create-docs-only-sync-pr-for-project-control` — closed-unmerged PR #997; tip `18d8bf6b3f69`.
- `codex/create-protocol-hardening-milestone-batch` — closed-unmerged PR #261; tip `5c2e7463abed`.
- `codex/create-repository-health-report` — closed-unmerged PR #14; tip `a4cf81e912ce`.
- `codex/fix-id-field-type-in-schema` — closed-unmerged PR #22; tip `de73734e903c`.
- `codex/fix-json-schema-typeerror-in-validation` — closed-unmerged PR #18; tip `fe5fe6fc48dc`.
- `codex/fix-json-schema-validation-typeerror` — closed-unmerged PR #20; tip `bc1ef0c5d2d7`.
- `codex/fix-missing-qrcode-dependency` — closed-unmerged PR #17; tip `3771636604c7`.
- `codex/fix-qr-legacy-compatibility-bridge` — closed-unmerged PR #1196; tip `e2098b59e21c`.
- `codex/fix-validation-check-not-triggering` — closed-unmerged PR #16; tip `0995b3fb8eb5`.
- `codex/fix-validation-workflow-dependency-installation` — closed-unmerged PR #19; tip `f9a76142ce1a`.
- `codex/harden-codeql-workflow-against-rate-limits` — closed-unmerged PR #1204; tip `4b9bc910408c`.
- `codex/improve-ci-quality-checks` — closed-unmerged PR #538; tip `2e2266c935c5`.
- `codex/include-hc-stale-baseline-scanner-in-report` — closed-unmerged PR #1130; tip `f76d8821aa4a`.
- `codex/optimize-hc-trust-layer-github-actions` — closed-unmerged PR #289; tip `06db246d2b18`.
- `codex/rebase-pr-#513-on-latest-main` — closed-unmerged PR #516; tip `098cfb4f6380`.
- `codex/stabilize-runtime-test-dependencies-in-ci` — closed-unmerged PR #513; tip `b9c31d211595`.
- `codex/sync-governance-preflight-tier-1-protected-paths` — closed-unmerged PR #549; tip `2946b4acb2bb`.
- `codex/update-pr-#1148-to-address-review-comments` — closed-unmerged PR #1149; tip `690488968021`.
- `docs/verified-legacy-bridge` — closed-unmerged PR #1206; tip `95269ce4d4a4`.
- `fix-876-next` — closed-unmerged PR #878; tip `a00f8b192067`.
- `fix/timestamp-proof-subject-binding` — closed-unmerged PR #961; tip `c0087278fef2`.
- `note-875` — closed-unmerged PR #884; tip `3da80028fa68`.
- `state-875` — closed-unmerged PR #883; tip `279b0245e140`.
- `witness-subjects` — closed-unmerged PR #952; tip `a01f527e7d5e`.

## `HOLD_UNMAPPED` — 4

- `chatgpt/code-volume-risk-status` — tip `7c66f3245768`; no exact pull-request head mapping confirmed.
- `fix-next-actions-876` — tip `80c04314a39e`; no exact pull-request head mapping confirmed.
- `pc875a` — tip `6b33cedebbd1`; no exact pull-request head mapping confirmed.
- `state-sync-875` — tip `5435f4235f11`; no exact pull-request head mapping confirmed.

## Deletion gate

Before any later deletion batch, re-run the inventory and require all of the following for every target:

- branch is not `main` and is not protected;
- no open pull request uses the branch;
- branch tip is unchanged from this report or is reclassified against fresh evidence;
- branch remains reachable from current `main`, or its unchanged tip still exactly matches the head SHA of a merged PR;
- branch is not used by current work, automation, deployment, release, or another operator;
- the exact deletion list receives explicit human maintainer approval;
- deletion is performed in a small recorded batch with a post-action branch-count audit.

Any mismatch moves the branch to `HOLD`. Closed-unmerged and unmapped branches must not be deleted from this report alone.

## Next safe action

Treat the complete branch-list triage as evidence-complete and the destructive cleanup step as parked. Review and merge this documentation-only inventory first. A later task may propose an exact small deletion batch from the 76 candidates after a fresh gate check and explicit human approval.

This report does not delete branches, close pull requests, close issues, modify workflows, alter rulesets, change source/runtime behavior, or change any HC:// authority boundary.
