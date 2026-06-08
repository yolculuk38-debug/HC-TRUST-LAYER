# START HERE — HC-TRUST-LAYER Navigation Guide

> **Purpose:** Orient new contributors, reviewers, AI agents, and maintainers to the HC-TRUST-LAYER repository structure, project identity, and protected boundaries without reading 50+ governance files.

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
3. **Then read:** [`CONTRIBUTING.md`](../CONTRIBUTING.md) — contribution workflow and PR policy
4. **Then read:** [`docs/contributor-start-here.md`](contributor-start-here.md) — detailed beginner guidance
5. **Pick work from:** Issues marked `good-first-issue` or make a small documentation improvement
6. **Before opening PR:** Run checks in section 5 below

**Timeline:** 30 minutes reading + 15 minutes local setup = ~45 minutes to first PR-ready change.

### For Maintainers & Release Coordinators

1. **Start here:** This file
2. **Then read:** [`GOVERNANCE.md`](../GOVERNANCE.md) — merge authority and review escalation
3. **Then read:** [`CHANGELOG.md`](../CHANGELOG.md) — version history and release evidence
4. **Then read:** [`HC_CONSTITUTION.md`](../HC_CONSTITUTION.md) — immutable core principles
5. **Reference:** [`docs/governance/`](governance/) — detailed governance, disputes, moderation
6. **For v0.1.0 decisions:** [`docs/governance/v0.1.0-tag-readiness-review.md`](governance/v0.1.0-tag-readiness-review.md) and [`docs/v0.1.0-release-notes.md`](v0.1.0-release-notes.md)

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

### For Vision / Future-Layer Reviewers

1. **Start here:** This file
2. **Then read:** [`docs/vision/source-and-social-verification.md`](vision/source-and-social-verification.md) — future source, account, media, and social verification direction; vision/planning only.
3. **Then read:** [`docs/vision/identity-layer-concept.md`](vision/identity-layer-concept.md) — future identity-layer concept for account identity, claimed identity, authority scope, and identity evidence; not implemented.
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

## 5. VALIDATION & CHECKS

Before opening PRs, run:

```bash
python scripts/check_terminology.py
python scripts/check_docs_drift.py
python scripts/check_canonical_artifacts.py
pytest
```

For docs-only changes, at minimum:

```bash
python scripts/check_terminology.py
python scripts/check_docs_drift.py
git diff --check
```

---

## 6. COMMON TASKS

### Add a New Record

1. Create JSON file in `records/pending/`
2. Follow schema in `schema/record-v1.schema.json`
3. Run validator: `python validators/validate_record.py records/pending/your_record.json`
4. Submit PR with evidence trail
5. Wait for human review and merge approval

**Warning:** Do not edit `records/verified/` or `records/archived/` directly without explicit maintainer task.

### Update Documentation

1. Confirm the target file is not evidence-bearing or governance-critical
2. Make the minimal change
3. Preserve terminology: use `HC-TRUST-LAYER` and `HC://` for active references
4. Run documentation checks
5. Open PR with clear scope and testing notes

### Fix a Broken Link

1. Verify the correct target path
2. Update only the broken link
3. Run link check or documentation validation
4. Mention the exact link fixed in PR description

### Review a PR

1. Check changed files against protected paths
2. Verify PR scope matches description
3. Confirm terminology alignment
4. Review validation output
5. Ensure no evidence-bearing files were modified unexpectedly
6. Approve, request changes, or escalate according to `GOVERNANCE.md`

---

## 7. TROUBLESHOOTING

### "Why are old names still in the repo?"

Legacy names are preserved in evidence-bearing contexts for provenance and audit trail continuity. Do not remove them from `records/archived/`, `halkalar/`, or migration docs. Only update active public-facing documentation.

### "Can I trust the validation output?"

Validation output is **advisory-only** and supports human review. HC-TRUST-LAYER does not provide legal certification, absolute truth, production authority, or autonomous finality.

### "Which AI should I trust?"

None automatically. AI outputs are assistive signals only. Human review and repository evidence remain authoritative.

### "Can I modify workflows?"

Not without explicit task and review. `.github/workflows/**` affects CI/CD security posture and is protected.

### "What if I see a conflict between docs?"

Do not silently resolve it. Open an issue or PR describing the conflict and cite both sources. Maintainers will decide.

---

## 8. CONTACT & ESCALATION

- **Repository Owner:** `@yolculuk38-debug`
- **Security Issues:** Follow `SECURITY.md`
- **Governance Questions:** Open public issue unless sensitive
- **Contribution Help:** Use GitHub Discussions or issues

---

## 9. REFERENCES

- [`README.md`](../README.md) — project overview
- [`HC_CONSTITUTION.md`](../HC_CONSTITUTION.md) — immutable principles
- [`GOVERNANCE.md`](../GOVERNANCE.md) — governance model
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — contribution guide
- [`SECURITY.md`](../SECURITY.md) — security policy
- [`docs/limitations-and-risks.md`](limitations-and-risks.md) — risk model
- [`docs/master-architecture.md`](master-architecture.md) — architecture overview
- [`docs/implementation-map.md`](implementation-map.md) — implementation status
- [`docs/project-control/project-state.md`](project-control/project-state.md) — current handoff state
- [`docs/project-control/next-actions.md`](project-control/next-actions.md) — next safe work
- [`docs/vision/source-and-social-verification.md`](vision/source-and-social-verification.md) — future source/social verification vision
- [`docs/vision/identity-layer-concept.md`](vision/identity-layer-concept.md) — future identity-layer concept
