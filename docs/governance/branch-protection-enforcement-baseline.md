# Branch Protection Enforcement Baseline

This document records the protected-branch enforcement model identified during governance review for HC-TRUST-LAYER and HC://. It is documentation only and does not change workflows, repository settings, schemas, validators, runtime behavior, policy interpretation, signing semantics, federation behavior, canonical records, or trust-kernel enforcement logic.

## 1. Current enforcement gap

The Trust Kernel Enforcement Gap Review identified that current protected-path coverage is narrower than the full trust-kernel review surface.

Current protected paths cover:

- `schema/**`
- `validators/**`
- `signatures/**`
- `policy/**`
- `federation/**`
- `.github/workflows/**`
- `src/hc_runtime/**`

Trust-critical surfaces also include:

- `records/**`
- `src/hc_trust/**`
- `src/validator.py`
- `src/verify_hashes.py`
- `scripts/check_pr_governance.py`
- `scripts/check_canonical_artifacts.py`
- `scripts/check_verification_package_schema.py`
- `scripts/evaluate_policy.py`
- `CODEOWNERS`
- `protocol-graph.json`
- `verification-map.json`
- `trust-kernel-index.json`
- `docs/canonical-record-boundary.md`
- `docs/trust-kernel-index.md`
- `docs/protocol-graph-index.md`
- `docs/verification-map-index.md`

This gap is a routing and review-boundary issue. It does not by itself establish new enforcement behavior.

## 2. Expanded protected-path recommendation

Expanded trust-kernel paths should be documented and reviewed in tiers before any enforcement change.

### Tier 1: canonical / hard protected

Tier 1 paths should be treated as canonical or hard protected because they can affect canonical record boundaries, schemas, validators, signing, policy evaluation, federation, CI guardrails, or machine-readable trust-kernel routing:

- `schema/**`
- `validators/**`
- `signatures/**`
- `policy/**`
- `federation/**`
- `.github/workflows/**`
- `records/**`
- `CODEOWNERS`
- `protocol-graph.json`
- `verification-map.json`
- `trust-kernel-index.json`

### Tier 2: trust-kernel documentation protected

Tier 2 paths should require protected documentation review because they define or index trust-kernel boundaries, verification map routing, protocol graph routing, or canonical record boundary expectations:

- `docs/canonical-record-boundary.md`
- `docs/trust-kernel-index.md`
- `docs/protocol-graph-index.md`
- `docs/verification-map-index.md`

### Tier 3: implementation pattern review

Tier 3 paths should require implementation-pattern review because they can influence verification behavior, hash checking, governance preflight, canonical artifact checks, verification package schema checks, policy evaluation, or trust-kernel runtime assumptions:

- `src/hc_runtime/**`
- `src/hc_trust/**`
- `src/validator.py`
- `src/verify_hashes.py`
- `scripts/check_pr_governance.py`
- `scripts/check_canonical_artifacts.py`
- `scripts/check_verification_package_schema.py`
- `scripts/evaluate_policy.py`

## 3. Auto-merge restriction

Expanded trust-kernel paths should not be eligible for unattended auto-merge. Automation labels, status checks, and advisory risk signals may support review, but they must not replace maintainer judgment for changes that touch expanded trust-kernel paths.

## 4. Human review routing

Changes touching expanded trust-kernel paths should require human-supervised validation before merge. Review should confirm the affected tier, expected trust-kernel impact, required checks, and whether reviewer escalation is needed for canonical record, verification map, protocol graph, policy, federation, signing, schema, validator, or runtime boundaries.

## 5. Future implementation note

This PR is documentation-only and does not enforce the expanded protected-path model. Enforcement changes to `CODEOWNERS`, `scripts/check_pr_governance.py`, PR risk labeler behavior, or workflows must be proposed in separate PRs with explicit human-supervised validation.
