# Archived / superseded notice

This report is preserved as historical project-control audit evidence.

It is no longer treated as an active navigation source or current public-entrypoint decision record.

Later report-control records found no active blocker requiring this file to remain active. The recommended safest handling is to keep it in place with this notice rather than delete, move, or rewrite it.

Current handling is governed by:

- `docs/project-control/report-lifecycle-index.md`
- `docs/project-control/archiveable-report-reference-findings-2026-06-23.md`
- `docs/project-control/public-navigation-audit-final-reference-search-2026-06-24.md`
- `docs/project-control/public-navigation-audit-archive-stub-plan-2026-06-24.md`

Deletion is not authorized.
Path movement is not authorized.
This file remains audit evidence.

---

# Public Navigation Audit

> **Mode:** REPORT ONLY  
> **Scope:** GitHub Pages, public documentation navigation, README entry points, START_HERE navigation, and Mini Public Validator Demo links.  
> **Decision:** PUBLIC NAVIGATION BROKEN

## Executive Summary

The external review claim is verified in part. The repository's active README and START_HERE navigation are generally healthy after the recent navigation updates, and the Mini Public Validator Demo resolves to existing repository paths. However, the GitHub Pages-style documentation landing surface at `docs/index.md` still presents an archived page as a public entry point and contains broken internal links for `Protocol` and `Witness Records`.

The most important issue is not broad repository-wide link failure. It is a public-surface mismatch: `docs/index.md` is marked `ARCHIVED`, but it still reads like a public landing page and links to missing lower-case files (`protocol.md`, `witnesses.md`). The current active protocol document exists as `docs/PROTOCOL.md`, and witness-related material exists under other names/locations, but the public landing page does not route users there.

Final decision: **PUBLIC NAVIGATION BROKEN** until the public GitHub Pages/index surface either routes to current active entry points or is clearly demoted away from public canonical navigation.

## Public Entry Point Inventory

Reviewed public or likely public-facing entry points:

- `README.md`
  - Current repository front door.
  - Contains the new `What Works Today` section.
  - Links to the Mini Public Validator Demo and START_HERE.
- `docs/START_HERE.md`
  - Current role-based onboarding guide.
  - Identifies current official names and archived legacy names.
- `docs/demo/mini-public-validator-demo.md`
  - Current shortest public-safe walkthrough added by PR #633.
  - Links to README, START_HERE, runtime docs, project-control docs, and governance docs.
- `docs/index.md`
  - Likely GitHub Pages documentation landing/index file if Pages is configured to publish from `docs/`.
  - Marked `ARCHIVED`, but still exposes public sections.
- `docs/demo-index.md`
  - GitHub Pages-oriented MVP-1 demo index.
  - Links to static viewer and self-service preview pages.
- `docs/self-service-verify.html`
  - Public local-only self-service SHA-256 preview prototype.
- `docs/verify.html`
  - First-flow/demo static QR verification page.
- `docs/explorer/index.html`
  - Static explorer-oriented page.
- `docs/project-control/project-state.md`
  - Current phase and source-of-truth handoff.
- `docs/project-control/next-actions.md`
  - Safe next-work queue and report-only boundaries.
- `.github/workflows/`
  - No Pages deployment workflow named `pages*` was found in the checked-out repository.

## Link Audit Findings

Repository-local link scanning found a small number of broken internal documentation links across `README.md`, `docs/**/*.md`, and `docs/**/*.html`. The public navigation-critical findings are:

- `docs/index.md` links `Protocol` to `protocol.md`, but `docs/protocol.md` is not present.
- `docs/index.md` links `Witness Records` to `witnesses.md`, but `docs/witnesses.md` is not present.
- `docs/index.md` links `Timeline` to `timeline.md`, and that target exists.
- `README.md`, `docs/START_HERE.md`, and `docs/demo/mini-public-validator-demo.md` did not show broken repository-local documentation targets in the local scan, except that the README workflow badge uses a GitHub web-relative path that is not a local filesystem path.

Additional broken internal links exist outside the primary public landing files. They appear mostly in older, draft, or secondary documentation surfaces and should be handled in a later cleanup PR rather than fixed here.

## GitHub Pages Findings

No `.github/workflows/pages*` workflow was present in the checked-out repository. The repository does contain GitHub Pages-oriented docs and static HTML surfaces, including:

- `docs/index.md`
- `docs/demo-index.md`
- `docs/self-service-verify.html`
- `docs/verify.html`
- `docs/verification-viewer.html`
- `docs/explorer/index.html`

The likely Pages risk is `docs/index.md`. If GitHub Pages publishes from `docs/`, this file is positioned as the landing index for public documentation. It is marked as archived, but it still exposes top-level public section links and therefore can appear like a current public navigation surface.

Live GitHub Pages HTTP verification could not be completed from this environment because outbound access to `https://yolculuk38-debug.github.io/HC-TRUST-LAYER/` failed with a proxy tunnel `403 Forbidden`. This audit therefore relies on repository-local source inspection and local link resolution, not live hosted response validation.

## README / START_HERE Findings

`README.md` is currently a healthier public entry point than `docs/index.md`:

- It starts with advisory/non-canonical status language.
- It contains a `What Works Today` section.
- It sends users to the Mini Public Validator Demo first.
- It sends users to `docs/START_HERE.md` for repository navigation.
- Its core internal navigation targets resolve locally.

`docs/START_HERE.md` is also generally healthy:

- It clearly identifies current official names: `HC-TRUST-LAYER`, `HC://`, and `yolculuk38-debug/HC-TRUST-LAYER`.
- It distinguishes legacy names from active project identity.
- It routes roles to README, governance, security, project-control, and contribution documents.
- Its checked internal targets resolve locally.

Remaining README / START_HERE concern:

- These files do not appear to be the GitHub Pages landing file. A visitor entering through Pages may encounter `docs/index.md` first instead of the current README / START_HERE path.

## Demo Navigation Findings

`docs/demo/mini-public-validator-demo.md` is healthy as a current public-safe walkthrough:

- Its reviewed internal links resolve locally.
- It preserves advisory-only semantics.
- It does not claim objective-truth finality, production readiness, forensic certainty, live federation, or autonomous governance finality.
- It correctly points users back to README and START_HERE.

Adjacent demo surfaces are mostly usable but fragmented:

- `docs/demo-index.md` is GitHub Pages-oriented and points to self-service and viewer HTML files.
- `docs/self-service-verify.html` links to existing result-state and visual-signal docs.
- `docs/verify.html` links to existing demo/generated continuity artifacts.

The missing piece is not the demo page itself. The missing piece is a clear route from the likely Pages landing page to the current Mini Public Validator Demo and `What Works Today` entry point.

## Archived vs Active Surface Findings

The archived-vs-active boundary is confusing:

- `docs/index.md` is explicitly marked `ARCHIVED`.
- The same file still presents a public-facing `HC-TRUST-LAYER` overview and `Public Sections` list.
- Two of those `Public Sections` links are broken.
- The archived page does not point users to the active README `What Works Today` section, START_HERE, Mini Public Validator Demo, or current project-control state.

This creates a public navigation risk: a user can reasonably treat `docs/index.md` as the project’s current public documentation landing page even though the file itself says it is archived.

## Broken Links

Public navigation-critical broken links:

| Source | Link text | Target | Finding |
| --- | --- | --- | --- |
| `docs/index.md` | `Protocol` | `protocol.md` | Broken; no `docs/protocol.md` file exists. |
| `docs/index.md` | `Witness Records` | `witnesses.md` | Broken; no `docs/witnesses.md` file exists. |

Other local broken links found during the broader docs scan:

| Source | Target |
| --- | --- |
| `docs/append-only-review-chain.md` | `./architecture-roadmap.md` |
| `docs/public_trial_quickstart.md` | `protocol-graph.md` |
| `docs/public_trial_quickstart.md` | `trust-kernel.md` |
| `docs/ai-assisted-review.md` | `./architecture-roadmap.md` |
| `docs/witness-layer.md` | `./signed-witness-format.md` |
| `docs/trust-layer.md` | `architecture-roadmap.md` |
| `docs/signed-witness-model.md` | `./architecture-roadmap.md` |
| `docs/signed-witness-model.md` | `./signed-witness-format.md` |
| `docs/maintainer-triage.md` | `protocol-graph.md` |
| `docs/verification-result-standard.md` | `./trust-engine-v1.md` |
| `docs/verification-result-standard.md` | `./architecture-roadmap.md` |
| `docs/drafts/architecture-roadmap.md` | several sibling links that likely should point outside `docs/drafts/` |
| `docs/drafts/trust-engine-v1.md` | `../examples/trust_score_example.json` and several sibling links that likely should point outside `docs/drafts/` |

These secondary links should not be fixed in this report-only PR.

## Confusing Links

Confusing or potentially misleading navigation surfaces:

- `docs/index.md` uses archived status language but still acts as a public landing page.
- `docs/index.md` uses lower-case `protocol.md`, while the active protocol file is `docs/PROTOCOL.md`.
- `docs/index.md` links to `witnesses.md`, while current witness-related documentation appears elsewhere, including `docs/PROVENANCE.md`, `docs/witness-layer.md`, `witness/README.md`, and `halkalar/` legacy witness records.
- The current Mini Public Validator Demo is not linked from `docs/index.md`.
- README `What Works Today` is not linked from `docs/index.md`.
- `docs/demo-index.md`, `docs/self-service-verify.html`, `docs/verify.html`, `docs/verification-viewer.html`, and `docs/demo/mini-public-validator-demo.md` provide multiple public/demo entry points without a single Pages-facing hierarchy that clearly says which one is the current first-click route.

## Risk Assessment

Risk level: **Medium for public documentation clarity; low for runtime/protocol integrity in this PR.**

Rationale:

- The issue affects public navigation and reviewer/user orientation.
- It does not modify schemas, validators, records, signing, federation, policy, workflows, hashes, QR artifacts, generated artifacts, runtime code, or governance rules.
- Broken public navigation can cause external reviewers to believe active surfaces are missing or stale.
- An archived page that appears canonical can weaken trust in HC:// verification documentation even when the current README and demo are healthier.
- The risk is bounded and suitable for a small docs-only follow-up PR.

## Final Recommendation

Decision: **PUBLIC NAVIGATION BROKEN**.

The claim that public Pages may contain broken links such as `Protocol` and `Witness Records` is supported by repository-local inspection of `docs/index.md`. The broader active navigation surface is not broadly broken: README, START_HERE, and the Mini Public Validator Demo are mostly healthy. The failure is concentrated in the likely GitHub Pages/index landing surface and in archived-vs-active clarity.

No fixes were made in this PR by design.

## Recommended Next PR

Open a small docs-only follow-up PR to repair public navigation without changing runtime, records, schemas, validators, workflows, policy, signing, federation, hashes, QR artifacts, generated artifacts, or governance rules.

Recommended minimal fix plan:

1. Update `docs/index.md` so it cannot be mistaken for the current canonical public entry point.
2. Add a clear active-entry notice near the top of `docs/index.md` pointing to:
   - `../README.md` or the repository README `What Works Today` section,
   - `START_HERE.md`,
   - `demo/mini-public-validator-demo.md`,
   - `project-control/project-state.md`.
3. Replace or remove broken `docs/index.md` links:
   - `protocol.md` should route to the current active protocol reference or be explicitly labeled archived if retained.
   - `witnesses.md` should route to the current witness/provenance reference or be explicitly labeled archived if retained.
4. Add a short archived-surface banner explaining that `docs/index.md` is retained for provenance continuity and is not the active public navigation root.
5. Optionally add a small docs link-check report or script in a later PR, but do not mix automation changes into the minimal navigation fix PR.
