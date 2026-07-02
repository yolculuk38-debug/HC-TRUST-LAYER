# START HERE — HC-TRUST-LAYER Navigation Guide

> **Purpose:** Orient new contributors, reviewers, AI agents, and maintainers to the HC-TRUST-LAYER repository structure, project identity, and protected boundaries without reading 50+ governance files.

---

## Operating Layer quick path

Use this short path when taking over an HC:// operating-layer shift after the HC Assistant Console rotation. It is advisory only, keeps `public_safe: true` and `truth_guarantee: false` boundaries intact, and does not replace human final authority.

1. Confirm current state in [`docs/project-control/project-state.md`](project-control/project-state.md).
2. Choose next safe work from [`docs/project-control/next-actions.md`](project-control/next-actions.md).
3. Check completed and do-not-repeat work in [`docs/project-control/task-ledger.md`](project-control/task-ledger.md).
4. Use [`docs/project-control/active-work-registry.md`](project-control/active-work-registry.md) only for advisory shift coordination.
5. Use [`docs/project-control/operator-entry-map.md`](project-control/operator-entry-map.md) as the navigation map.
6. Route active repository-level `/hc` console work to [#812 active HC Assistant Console v2](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/812). Treat [#763](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/763) as closed and historical only; do not reopen it or treat it as active.

Do not repeat #811, #813, #814, #815, or assistant-console rotation work unless new repository evidence appears. Protected areas remain `schema/**`, `validators/**`, `records/**`, `signatures/**`, `federation/**`, `policy/**`, `canonical/**`, `.github/workflows/**`, generated artifacts, trust-kernel indexes, and governance-enforcement surfaces unless explicitly authorized and human-reviewed.

---

## 1. PROJECT IDENTITY

### Current Official Names

- **Project:** `HC-TRUST-LAYER`
- **Protocol:** `HC://`
- **Repository:** `yolculuk38-debug/HC-TRUST-LAYER`
- **Status:** v0.1.0 (MVP / Early Stage)

### Legacy Names (Archived)

The project was previously known by these names during early experimental phases (May 2026):

- `Humanity Chain` (original project name)
- `Insanlik-Zinciri` (legacy repository name)
- `İnsanlık Zinciri` (Turkish form)

**Important:** Legacy names appear intentionally in:
- Historical records in `records/archived/`
- Witness records in `halkalar/` directory
- Migration documentation in `docs/governance/`
- Test fixtures (to validate QR safety checks)
- Schema backward-compatibility references

**Do not silently rewrite or delete these references.** They preserve evidence of project provenance and audit trail continuity. When encountering old names in active public-facing documentation (e.g., README, user guides, quickstart), they should be updated to `HC-TRUST-LAYER` or `HC://`, but historical/evidence-bearing files must remain unchanged.

### Repository Relationship

- **Old Repository:** `yolculuk38-debug/Insanlik-Zinciri` (legacy origin, now archived/redirected)
- **Current Repository:** `yolculuk38-debug/HC-TRUST-LAYER` (canonical active implementation)
- **New Contributors:** All work should target `HC-TRUST-LAYER`, not the old repository
- **Evidence Preservation:** Migration history is documented in `docs/governance/post-migration-qr-review.md` for audit trail purposes

---

## 2. QUICK START BY ROLE

### Try the Public Validator Demo

Use these HC:// Public Validator demo entry points for a fast, public-safe, advisory-only walkthrough. The demo preserves `public_safe: true` and `truth_guarantee: false`, requires human-supervised review, and does not claim production readiness, certification, legal authority, or autonomous finality.

- Open the static viewer in a browser: [`docs/demo/public-validator-static-viewer.html`](demo/public-validator-static-viewer.html)
- Open a static scenario link: [`banana`](demo/public-validator-static-viewer.html?scenario=banana), [`building`](demo/public-validator-static-viewer.html?scenario=building), [`news`](demo/public-validator-static-viewer.html?scenario=news), or [`qr-spoof`](demo/public-validator-static-viewer.html?scenario=qr-spoof). These are demo-only navigation links and do not prove QR authenticity or signed payload verification.
- Try the viewer Record ID fixture input with supported demo IDs such as `HC-DEMO-PV-FIXTURE-FOOD-0001`; it only maps bundled fixture IDs to bundled scenarios and does not perform canonical record lookup, backend/API calls, production verification, truth verification, QR authenticity checks, or signed payload verification.
- Run the local demo runner from the repository root: [`scripts/run_public_validator_demo.py`](../scripts/run_public_validator_demo.py)
- Read the demo quickstart: [`docs/demo/public-validator-demo-quickstart.md`](demo/public-validator-demo-quickstart.md)
- Try the local `record_id` lookup quickstart: [`docs/demo/public-validator-local-lookup-quickstart.md`](demo/public-validator-local-lookup-quickstart.md). Example: `python scripts/run_public_validator_lookup.py HC-EXAMPLE-2026-0001`. This command is local-only, advisory-only, public-safe, not a production API, not truth verification, not QR authenticity proof, not signed payload verification, and not legal/regulatory/safety certification; human review remains required.
- Read the QR trust-boundary specification: [`docs/security/qr-payload-verification-boundary.md`](security/qr-payload-verification-boundary.md). It defines the future QR payload verification boundary without implementing QR crypto, signing, runtime behavior, validators, schemas, workflows, backend/API behavior, or network calls.
- Try the QR payload parser fixture quickstart: [`docs/demo/fixtures/qr-payload-parser/README.md`](demo/fixtures/qr-payload-parser/README.md). The examples show `valid_payload`, `invalid_payload`, and `malformed_payload` outputs while preserving `advisory_only: true`, `public_safe: true`, `truth_guarantee: false`, and `human_review_required: true`; the parser checks payload shape only and does not prove QR authenticity, verify signatures, fetch `canonical_url`, call a network/backend/API, verify record truth, or replace human review.

### For First-Time Contributors

1. **Start here:** This file (you're reading it)
2. **Then read:** [`README.md`](../README.md) — project overview and demo
3. **Then read:** [`docs/repo-map.md`](repo-map.md) — current repository map and advisory ownership boundaries
4. **Then read:** [`CONTRIBUTING.md`](../CONTRIBUTING.md) — contribution workflow and PR policy
5. **Then read:** [`docs/contributor-start-here.md`](contributor-start-here.md) — detailed beginner guidance
   For a timed contributor path, see [`docs/contributor-start-here.md`](contributor-start-here.md).
6. **Pick work from:** Issues marked `good-first-issue` or make a small documentation improvement
7. **Before opening PR:** Run checks in section 5 below

**Timeline:** 30 minutes reading + 15 minutes local setup = ~45 minutes to first PR-ready change.

### For Maintainers & Release Coordinators

1. **Start here:** This file
2. **Then read:** [`GOVERNANCE.md`](../GOVERNANCE.md) — merge authority and review escalation
3. **Then read:** [`CHANGELOG.md`](../CHANGELOG.md) — version history and release evidence
4. **Then read:** [`HC_CONSTITUTION.md`](../HC_CONSTITUTION.md) — immutable core principles
5. **Reference:** [`docs/governance/`](governance/) — detailed governance, disputes, moderation
6. **Governance surface classification:** [`docs/governance/canonical-vs-advisory-governance-surfaces.md`](governance/canonical-vs-advisory-governance-surfaces.md) — conservative guide to canonical, advisory, project-control, historical/reference, and onboarding surfaces.
7. **For v0.1.0 decisions:** [`docs/governance/v0.1.0-tag-readiness-review.md`](governance/v0.1.0-tag-readiness-review.md) and [`docs/v0.1.0-release-notes.md`](v0.1.0-release-notes.md)
8. **Namespace/refactor readiness:** See [`docs/refactor/namespace-implementation-readiness-plan.md`](refactor/namespace-implementation-readiness-plan.md) before proposing source moves.

**Key roles:**
- Merge approval: repository owner (`@yolculuk38-debug`)
- Review escalation: defined in `GOVERNANCE.md`
- Validator decisions: documented in audit trail

### For AI Agents & Automation

1. **Start here:** This file
2. **Then read:** [`AGENTS.md`](../AGENTS.md) — agent rules, contributor rules, claim boundaries
3. **Then read:** [`HC_BOOTSTRAP.md`](../HC_BOOTSTRAP.md) — startup sequence and check-in/checkout protocol
4. **Then read:** [`docs/project-control/agent-operating-model.md`](project-control/agent-operating-model.md) — roles, authority levels, scope limits
5. **Then read:** [`docs/project-control/task-ledger.md`](project-control/task-ledger.md) — completed work, closed work, do-not-repeat rules
6. **Then read:** [`docs/project-control/project-state.md`](project-control/project-state.md) — current phase and repository-state handoff
7. **Reference:** [`docs/project-control/next-actions.md`](project-control/next-actions.md) — next safe work and do-not-repeat boundaries
8. **Stop and report if:** you encounter protected paths, trust-kernel-adjacent work, or repository evidence gaps

**Mode:** Report-only investigations before any editing. Preserve advisory-only semantics. No autonomous governance finality.

### For Public Validator / Explorer Planners

1. **Start here:** This file
2. **Then read:** [`docs/project-control/public-validator-mvp-specification.md`](project-control/public-validator-mvp-specification.md) — official documentation-only Public Validator MVP Specification added by #820.
3. **Then read:** [`docs/project-control/public-validator-mvp-readiness-review.md`](project-control/public-validator-mvp-readiness-review.md) — supporting report-only readiness review and MVP gap summary.
4. **Then read:** [`docs/project-control/public-validator-mvp-spec.md`](project-control/public-validator-mvp-spec.md) — supporting documentation-only public-safe MVP contract and result shape.
5. **Then read:** [`docs/project-control/public-validator-implementation-plan.md`](project-control/public-validator-implementation-plan.md) — supporting documentation-only implementation planning boundaries.
6. **Cross-check:** [`docs/public-verification-flow.md`](public-verification-flow.md) and [`docs/public-verification-api.md`](public-verification-api.md).

**Boundary:** Public validator / explorer planning does not imply hosted production readiness, backend deployment, truth finality, legal/security certification, or autonomous governance authority.

### For Vision Reviewers

1. **Start here:** This file
2. **Then read:** [`docs/vision/source-and-social-verification.md`](vision/source-and-social-verification.md) — future source, account, media, and social verification direction; vision/planning only.
3. **Then read:** [`docs/vision/identity-layer-concept.md`](vision/identity-layer-concept.md) — future identity-layer concept for account identity, authority scope, and identity evidence; not implemented.
4. **Then cross-check:** [`docs/trust-graph.md`](trust-graph.md), [`docs/validator-identity-architecture.md`](validator-identity-architecture.md), and [`docs/future/signed-validator-identity.md`](future/signed-validator-identity.md).

**Boundary:** Vision documents do not implement runtime behavior, schemas, validators, records, QR behavior, signing, federation, policy, or governance enforcement.

### For Security Reviewers

1. **Start here:** This file
2. **Then read:** [`SECURITY.md`](../SECURITY.md) — vulnerability reporting paths, disclosure guidelines, human oversight requirements
3. **Then read:** [`docs/security/threat-model-master-map.md`](security/threat-model-master-map.md) (if present) — threat model overview
4. **Review:**
   - `.github/workflows/` — CI/CD automation safety
   - `CODEOWNERS` — access control enforcement
   - `schema/` files — canonical record boundaries
   - `src/hc_runtime/` — runtime verification logic (protected)
5. **Escalation:** Sensitive security issues must follow private vulnerability reporting in `SECURITY.md`, not public issues

### For External Reviewers

1. **Start here:** This file
2. **Then read:** [`README.md`](../README.md) — project scope and current status
3. **Then read:** [`docs/limitations-and-risks.md`](limitations-and-risks.md) — boundary language and trust model
4. **Then read:** [`GOVERNANCE.md`](../GOVERNANCE.md) — decision-making process
5. **Reference:** [`HC_CONSTITUTION.md`](../HC_CONSTITUTION.md) — immutable core principles
6. **For questions:** Open a GitHub Discussion or public Issue (for non-sensitive topics only)

---

## 3. PROTECTED AREAS & "DO NOT TOUCH" BOUNDARIES

### What Is the Trust Kernel?

The **trust kernel** is the set of files and paths that affect record identity, provenance continuity, verification semantics, policy interpretation, signing behavior, federation behavior, or governance authority. Changes to trust-kernel-adjacent surfaces require additional review and explicit justification.

### Protected Paths (Do Not Modify Without Explicit Approval)

| Path | Purpose | Why Protected |
|------|---------|---------------|
| `schema/**` | Record schema definitions | Affects all verification and serialization |
| `validators/**` | Verification validation logic | Changes alter verification semantics |
| `policy/**` | Governance and access control policies | Changes affect trust decisions |
| `federation/**` | Federation exchange logic | Changes affect multi-node verification |
| `signing/**` | Cryptographic signing and trust anchors | Changes affect signature verification |
| `records/**` | Verified and archived records | Evidence-bearing; immutable for audit trail |
| `hash/**` | Hash references and integrity artifacts | Changes break canonical linkage |
| `qr/**` | QR verification artifacts | Changes break verification pathways |
| `generated/**` | Auto-generated artifacts (indexes, exports) | Regenerated from canonical sources |
| `.github/workflows/**` | CI/CD automation and branch protection | Changes affect security posture |
| `src/hc_runtime/**` | Runtime verification implementation | Changes alter verification behavior |
| `CODEOWNERS` | Access control enforcement | Changes affect merge authority |
| `trust-kernel-index.json` | Trust kernel advisory index | Carefully curated reference artifact |
| `verification-map.json` | Verification flow metadata | Reference artifact for navigation |
| `protocol-graph.json` | Protocol structure metadata | Reference artifact for understanding |

### What You CAN Edit Without Special Approval

✓ **Documentation-only changes:**
- `docs/**/*.md` (except governance files marked sensitive)
- `README.md`, `CONTRIBUTING.md`, `ROADMAP.md`, `CHANGELOG.md` (within reason)
- Examples and tutorials
- Typo fixes and link repairs

✓ **Safe first contributions:**
- Broken links in documentation
- Typos and grammar
- Clarifying comments in docs
- Small examples that don't change protocol behavior

✓ **With maintainer approval:**
- Any change to protected paths (request review first)
- Changes to verification behavior
- Changes to schema or validators
- Changes to governance or policy

### What You MUST NOT Edit (No Exceptions Without Explicit Task)

✗ **Evidence-bearing files** (preserve exactly for audit trail):
- `records/archived/` — all files
- `GENESIS_BLOCK.md`
- `halkalar/` — all files
- `docs/governance/post-migration-qr-review.md` (migration evidence)

✗ **Canonical artifacts** (do not regenerate without task):
- `schema/record-v1.json`
- `trust-kernel-index.json`
- `verification-map.json`
- `protocol-graph.json`

✗ **Runtime & security** (do not weaken):
- All files in `src/hc_runtime/`
- `.github/workflows/**`
- `policy/**`
- `federation/**`
- `signing/**`

✗ **Release evidence** (do not modify):
- `VERSION` file
- Release tags once created
- Release evidence records in `records/`

---

## 4. PROJECT STATUS: v0.1.0

### Current Version

- **Version:** `0.1.0` (see [`VERSION`](../VERSION) file)
- **Status:** MVP / Early Stage
- **Current phase:** Post-runtime stabilization / operating-layer refinement
- **Release Date:** [See CHANGELOG]
- **Tag Ready:** Yes, with known limitations

For the current handoff state and next safe work, read [`docs/project-control/project-state.md`](project-control/project-state.md) and [`docs/project-control/next-actions.md`](project-control/next-actions.md). Runtime hardening was recently reviewed through #628 (telemetry contract sufficient), #629 (replay / continuity coverage), and #630 (runtime conditionally stabilized). #631 completed the HC Operating Layer review as operating layer conditionally sufficient.

### What v0.1.0 Includes

✓ **Implemented:**
- Core verification workflow
- Record integrity verification baseline
- Public verification CLI/API baseline
- QR verification baseline
- Test infrastructure
- Documentation and examples

⚠ **Experimental (Partial):**
- Witness/signature expansion
- Explorer/index visibility
- Trust scoring foundations

🔮 **Planned (Future):**
- Navigation/index synchronization and public validator / explorer planning
- Federation/sync interoperability
- Ecosystem integrations
- Long-horizon institutional adapters

### Release Evidence

| Item | Location |
|------|----------|
| Version number | [`VERSION`](../VERSION) |
| Changelog | [`CHANGELOG.md`](../CHANGELOG.md) |
| Release notes | [`docs/v0.1.0-release-notes.md`](v0.1.0-release-notes.md) |
| Release decision log | [`docs/governance/v0.1.0-tag-readiness-review.md`](governance/v0.1.0-tag-readiness-review.md) |
| Architecture overview | [`docs/master-architecture.md`](master-architecture.md) |
| Implementation status | [`docs/implementation-map.md`](implementation-map.md) |
| Limitations | [`docs/limitations-and-risks.md`](limitations-and-risks.md) |

### v0.1.0 Known Limitations

- No live federation yet
- No cryptographic signature verification yet (planned)
- No autonomous validator decisions (human-supervised required)
- Advisory-only verification outputs (not definitive truth claims)
- Early governance model (may evolve)

**See [`docs/limitations-and-risks.md`](limitations-and-risks.md) for complete risk model.**

---

## 5. BEFORE OPENING A PULL REQUEST

### Checks to Run

For **documentation-only changes:**

```bash
python scripts/check_terminology.py
python scripts/check_docs_drift.py
python scripts/check_canonical_artifacts.py
git diff --check
```

For **code or runtime changes:**

```bash
pytest -q
python scripts/check_terminology.py
python scripts/check_docs_drift.py
```

If you cannot run checks in your environment, **state that in the PR** and do not imply success.

### PR Checklist

- [ ] Branch name follows pattern: `docs/topic` or `feat/topic` or `fix/topic`
- [ ] One focused change (not multiple unrelated changes)
- [ ] Commit message is clear and references any related issue
- [ ] Required checks pass locally (or noted why they couldn't run)
- [ ] Changed files do not include protected paths (unless task explicitly requests)
- [ ] If touching `src/`, `schema/`, `.github/workflows/`, `policy/`, `federation/`, `signing/`: requested review before opening PR
- [ ] Terminology is consistent: `HC-TRUST-LAYER` and `HC://` in new docs
- [ ] No deletions of evidence-bearing files
- [ ] No modifications to hash, QR, generated, or archived artifacts unless explicitly tasked

### Merge Policy

| PR Type | Merge Requirement |
|---------|------------------|
| Docs-only | Human review and human merge required after checks pass |
| Code, schema, workflows, src/ | Manual review required (labeled `manual-review`) |
| Mixed docs + sensitive | Manual review (escalates to `manual-review` by default) |
| Trust-kernel-adjacent | Explicit justification + human-supervised validation |

**See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for full merge policy.**

---

## 6. KEY REFERENCE DOCUMENTS

### For Understanding the Project

| Document | Purpose |
|----------|---------|
| [`README.md`](../README.md) | Project overview, demo, and quick links |
| [`AGENTS.md`](../AGENTS.md) | Rules for humans, agents, and contributors |
| [`HC_BOOTSTRAP.md`](../HC_BOOTSTRAP.md) | Startup sequence and agent protocol |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | How to submit pull requests and contribute |
| [`SECURITY.md`](../SECURITY.md) | Security and vulnerability reporting |

### For Understanding Trust Boundaries

| Document | Purpose |
|----------|---------|
| [`HC_CONSTITUTION.md`](../HC_CONSTITUTION.md) | Immutable core principles and governance foundation |
| [`GOVERNANCE.md`](../GOVERNANCE.md) | Merge authority, review escalation, dispute handling |
| [`docs/limitations-and-risks.md`](limitations-and-risks.md) | Risk model and boundary language |
| [`docs/trust-kernel-index.md`](trust-kernel-index.md) | Advisory trust kernel routing index |
| [`docs/pr-scope-boundaries.md`](pr-scope-boundaries.md) | PR scope and sensitive-surface guidance |

### For Understanding Verification Architecture

| Document | Purpose |
|----------|---------|
| [`docs/master-architecture.md`](master-architecture.md) | Overall architecture and system design |
| [`docs/implementation-map.md`](implementation-map.md) | Implementation status and component matrix |
| [`docs/verification-map.md`](verification-map.md) | Verification workflow and mapping |
| [`docs/protocol-graph-index.md`](protocol-graph-index.md) | Protocol structure navigation |
| [`docs/capability-status.md`](capability-status.md) | Feature status and maturity |

### For Public Validator Planning

| Document | Purpose |
|----------|---------|
| [`docs/project-control/public-validator-mvp-specification.md`](project-control/public-validator-mvp-specification.md) | Official documentation-only Public Validator MVP Specification added by #820 |
| [`docs/project-control/public-validator-mvp-readiness-review.md`](project-control/public-validator-mvp-readiness-review.md) | Supporting report-only readiness review and MVP gap summary |
| [`docs/project-control/public-validator-mvp-spec.md`](project-control/public-validator-mvp-spec.md) | Supporting documentation-only public validator MVP contract and result shape |
| [`docs/project-control/public-validator-implementation-plan.md`](project-control/public-validator-implementation-plan.md) | Supporting documentation-only public validator implementation planning boundaries |
| [`docs/public-verification-flow.md`](public-verification-flow.md) | Future public verification flow foundation |
| [`docs/public-verification-api.md`](public-verification-api.md) | Future public verification API architecture draft |

### For Future Vision Planning

| Document | Purpose |
|----------|---------|
| [`docs/vision/source-and-social-verification.md`](vision/source-and-social-verification.md) | Future source, account, media, and social verification direction |
| [`docs/vision/identity-layer-concept.md`](vision/identity-layer-concept.md) | Future identity-layer concept for account identity, authority scope, and identity evidence |

### For Release & Governance

| Document | Purpose |
|----------|---------|
| [`CHANGELOG.md`](../CHANGELOG.md) | Version history and release notes |
| [`ROADMAP.md`](../ROADMAP.md) | Long-term direction and strategic sequence |
| [`docs/v0.1.0-release-notes.md`](v0.1.0-release-notes.md) | v0.1.0 release details and evidence |
| [`docs/governance/v0.1.0-tag-readiness-review.md`](governance/v0.1.0-tag-readiness-review.md) | v0.1.0 tag decision and approval process |
| [`docs/governance/`](governance/) | Detailed governance, disputes, moderation, accountability |

### For Historical Context

| Document | Purpose |
|----------|---------|
| [`GENESIS_BLOCK.md`](../GENESIS_BLOCK.md) | Historical origin record and project genesis |
| [`halkalar/`](../halkalar/) | Witness records of early AI interactions |
| [`records/archived/`](../records/archived/) | Verified and archived interaction records |
| [`docs/governance/post-migration-qr-review.md`](governance/post-migration-qr-review.md) | Migration from Insanlik-Zinciri to HC-TRUST-LAYER |

---

## 7. HISTORICAL RECORD FOLDERS (DO NOT EDIT)

These directories contain evidence-bearing records that preserve project provenance and audit trail continuity. **Do not modify, delete, or silently rewrite files in these locations:**

- **`records/archived/`** — Verified interaction records and release evidence
- **`halkalar/`** — Witness records of early AI system interactions (Turkish: "rings/circles")
- **`GENESIS_BLOCK.md`** — Project genesis and historical origin documentation

These files intentionally use legacy project names ("Humanity Chain", "Insanlik-Zinciri") as historical evidence. This is correct and should not be changed. When referencing these files in new documentation, clarify: "See historical record [filename]" or "This is legacy documentation".

---

## 8. COMMON QUESTIONS

### Q: I found "Humanity Chain" in the README. Should I fix it?

**A:** If it's in the main README.md or active public-facing docs (quickstart, user guides), yes—update to `HC-TRUST-LAYER`. If it's in `records/archived/`, `halkalar/`, `GENESIS_BLOCK.md`, or historical docs, **leave it exactly as-is**. It's evidence.

### Q: Can I make changes to the schema files?

**A:** Not without explicit maintainer approval. The schema is a trust-kernel artifact. If you have a schema proposal, open an issue first and request review before implementing.

### Q: What if I find a broken QR link?

**A:** Report it as an issue (public, if not sensitive) or contact the maintainer. QR artifacts are carefully managed for evidence/migration purposes, so updates require review.

### Q: Can I delete old records to clean up?

**A:** **No.** Historical records in `records/archived/` and witness records in `halkalar/` are evidence-bearing. Deleting them breaks the audit trail and violates the immutable core principles in `HC_CONSTITUTION.md`.

### Q: Why do the tests reference "Insanlik-Zinciri"?

**A:** Tests intentionally check that QR URLs pointing to the old repository are flagged as unsafe/high-risk. This validates the security posture. Don't remove these tests.

### Q: Who decides whether my PR merges?

**A:** The repository owner (`@yolculuk38-debug`). Review requirements are:
- Docs-only: Human review and human merge required after checks pass
- Code/schemas/workflows: Manual review required
- Trust-kernel-adjacent: Explicit justification + human-supervised validation

### Q: What does "human-supervised validation" mean?

**A:** It means a human (the maintainer or designated reviewer) must review, understand, and explicitly approve the change before it merges. AI agents and automation can assist, but a human makes the final decision for trust-critical changes.

---

## 9. WHEN TO STOP AND ASK FOR HELP

**Before editing, request review if:**

- [ ] The change touches a protected path (see section 3)
- [ ] The change may alter verification or trust behavior
- [ ] The change affects schemas, validators, policy, signing, federation, or governance
- [ ] You are unsure whether repository evidence supports a claim
- [ ] A required check fails and the fix is non-trivial
- [ ] You are tempted to broaden the PR beyond the original task
- [ ] The change could affect trust kernel boundaries or audit trail continuity

**When in doubt: stop and ask. The maintainer will clarify within 24 hours.**

---

## 10. NEXT STEPS

### For First-Time Contributors

1. ✓ You've read this file
2. → Read [`README.md`](../README.md)
3. → Read [`CONTRIBUTING.md`](../CONTRIBUTING.md)
4. → Pick an issue or make a small docs improvement
5. → Run the checks in section 5
6. → Open a PR and request review

**Expected time to first PR:** ~1 hour

### For Maintainers

1. ✓ You've read this file
2. → Review [`GOVERNANCE.md`](../GOVERNANCE.md)
3. → Check [`docs/governance/v0.1.0-tag-readiness-review.md`](governance/v0.1.0-tag-readiness-review.md)
4. → Decide on v0.1.0 release tag and announcement
5. → Continue merging PRs per merge policy

### For AI Agents

1. ✓ You've read this file
2. → Read [`AGENTS.md`](../AGENTS.md)
3. → Read [`HC_BOOTSTRAP.md`](../HC_BOOTSTRAP.md)
4. → Run agent check-in protocol from HC_BOOTSTRAP.md
5. → Investigate with report-only mode first
6. → Request human-supervised validation for trust-kernel-adjacent work
7. → Prefer navigation/index synchronization or public validator / explorer planning; avoid repeating telemetry, replay, or runtime review unless new evidence appears

---

## Related Documents

- [`README.md`](../README.md) — Start here if you haven't read the main project overview
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — Contribution workflow and PR policy
- [`AGENTS.md`](../AGENTS.md) — Rules for agents and contributors
- [`HC_BOOTSTRAP.md`](../HC_BOOTSTRAP.md) — Startup sequence and project protocol
- [`SECURITY.md`](../SECURITY.md) — Security and vulnerability reporting
- [`HC_CONSTITUTION.md`](../HC_CONSTITUTION.md) — Immutable core principles
- [`GOVERNANCE.md`](../GOVERNANCE.md) — Merge authority and governance framework
- [`docs/contributor-start-here.md`](contributor-start-here.md) — Detailed beginner guidance
- [`docs/project-control/public-validator-mvp-specification.md`](project-control/public-validator-mvp-specification.md) — official documentation-only Public Validator MVP Specification added by #820
- [`docs/project-control/public-validator-mvp-spec.md`](project-control/public-validator-mvp-spec.md) — supporting Public Validator MVP specification reference
- [`docs/project-control/public-validator-implementation-plan.md`](project-control/public-validator-implementation-plan.md) — supporting Public Validator MVP implementation plan
- [`docs/vision/source-and-social-verification.md`](vision/source-and-social-verification.md) — Future source/social verification vision
- [`docs/vision/identity-layer-concept.md`](vision/identity-layer-concept.md) — Future identity-layer concept

---

**Last Updated:** 2026-06-05  
**Status:** Documentation Guide (Advisory; not a canonical record, schema, validator, policy, signing, federation, or runtime artifact)
