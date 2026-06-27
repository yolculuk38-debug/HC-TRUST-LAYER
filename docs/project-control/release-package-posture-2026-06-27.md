# Release / Package Posture — 2026-06-27

Status: advisory project-control note

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human_review_required=true
- no production readiness claim
- no security/legal/identity guarantee
- no autonomous finality

This note describes the current HC-TRUST-LAYER release and package posture. It does not change packaging, publication, runtime, validation, workflow, schema, record, policy, federation, signature, canonical, governance, dependency, or CI behavior.

CI/check outputs are evidence for human review. They are not a trust authority and do not provide truth, security, legal, identity, forensic, or production guarantees.

## Current Posture

- Repository has Python package metadata.
- Repository has an `hc-trust` CLI entrypoint.
- Repository has demo/public validator/advisory runtime surfaces.
- Repository is still early-stage verification infrastructure.
- Package metadata does not imply production readiness.
- CLI/demo availability does not imply legal, forensic, identity, security, or truth finality.

HC-TRUST-LAYER remains advisory verification infrastructure. Human review remains required before relying on repository outputs, package metadata, CLI output, demo behavior, validator examples, or release evidence.

## Surface Distinctions

The repository includes several surfaces with different review expectations and authority boundaries:

- Documentation / governance notes: explanatory and advisory materials for contributors and reviewers.
- Demo surfaces: illustrative examples that may help review behavior but do not create production guarantees.
- Advisory runtime / CLI: tooling surfaces that can assist inspection and validation, subject to human review.
- Public validator examples: examples for public-safe validation workflows, not final truth authorities.
- Experimental / future federation and integration surfaces: forward-looking or integration-oriented material that requires separate review before operational reliance.
- Canonical schema / record boundaries: record-shape and provenance boundary material that requires careful human-supervised review.

## Explicit Non-Claims

HC-TRUST-LAYER is:

- Not a production trust authority.
- Not a legal registry.
- Not an identity provider.
- Not a security certification system.
- Not a forensic truth oracle.
- Not an autonomous AI decision system.
- Not a guaranteed PyPI/package distribution contract unless separately released and reviewed.

## Future Release Decision Checklist

Before changing release or package behavior, reviewers should confirm that:

- pyproject metadata reviewed
- Python version support reviewed
- dependency compatibility reviewed
- CLI behavior reviewed
- public validator/demo behavior reviewed
- README/ROADMAP alignment reviewed
- release notes prepared
- tag/signing/version policy reviewed
- no unsupported compatibility or production claim introduced
- human maintainer approval recorded

## Recommendation

- Keep package/runtime posture advisory until compatibility and release evidence are stronger.
- Use small PRs for future release posture changes.
- Do not change packaging or release behavior in this PR.
