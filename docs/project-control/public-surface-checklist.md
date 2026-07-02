# HC Public Surface Checklist

## Purpose

This project-control checklist is used to review public-facing entry points before or after changes to GitHub Pages, README material, demos, public previews, and onboarding documents.

It is advisory project-control documentation. It does not create production readiness, guarantee correctness, or replace human review. Public-facing changes remain subject to human final authority before they are treated as accepted repository guidance.

## Covered public surfaces

Use this checklist for public-facing surfaces that exist in the repository:

- [ ] GitHub repository home
- [ ] README: `README.md`
- [ ] GitHub Pages landing page: `docs/index.md`
- [ ] Start-here onboarding: `START_HERE.md`
- [ ] Public-safe demo: `docs/demo/mini-public-validator-demo.md`
- [ ] Browser-side self-service preview: `docs/self-service-verify.html`
- [ ] Project status page: `docs/project-control/project-state.md`
- [ ] GitHub Issues / contribution path
- [ ] Public trust / public onboarding docs, if present

## Checklist

### A. Status clarity

- [ ] No public-facing `ARCHIVED` label appears unless the page is truly an archive.
- [ ] Current status is visible where needed.
- [ ] Wording such as "active public preview," "partial implementation," and "advisory-only" is acceptable when accurate.
- [ ] Old legacy names are not presented as the active project identity.

### B. Visitor orientation

- [ ] The page explains what HC-TRUST-LAYER is.
- [ ] The page explains what a visitor can do next.
- [ ] Start here, README, demo, preview, repository, project status, and issues or contribution paths are reachable where appropriate.

### C. Link health

- [ ] Public links resolve.
- [ ] The page does not link to planned-but-missing docs.
- [ ] External GitHub links point to the active repository.
- [ ] Internal relative links work from the GitHub Pages context.

### D. Boundary language

Public pages must not claim:

- [ ] Production readiness
- [ ] Guaranteed truth
- [ ] Legal or institutional finality
- [ ] Identity finality
- [ ] Forensic certainty
- [ ] Certification authority
- [ ] Autonomous system authority
- [ ] Guaranteed correctness

Public pages should preserve:

- [ ] Advisory-only boundaries
- [ ] Public-safe framing
- [ ] Human review requirements
- [ ] Human final authority

### E. Mobile / translation friendliness

- [ ] Headings are simple.
- [ ] Sentences are short.
- [ ] Link text is clear.
- [ ] Jargon-heavy headings are avoided unless necessary.
- [ ] Google Translate and mobile readers should be able to follow the basic flow.

### F. Contribution path

- [ ] Issues or another contribution path is visible.
- [ ] Feedback language does not imply official certification or legal authority.
- [ ] Contributors can understand where to report broken links or public-facing confusion.

## Current baseline note

After the landing-page cleanup, the current public-surface baseline is:

- The public landing page is active.
- The visible status is active public preview / partial implementation / advisory-only.
- Action links are present.
- Advisory boundaries are visible.
- This checklist should be reused for future public-surface changes.

## Future polish, not required for current baseline

The following items may improve the public surface later, but they are optional polish items and are not blockers for the current baseline:

- Visual hierarchy review.
- Contrast and accessibility review.
- Button-like presentation if the GitHub Pages theme supports it safely.
