# Threat Model

This threat model documents security considerations for HC-TRUST-LAYER documentation, CI quality controls, and GitHub Actions governance. It is advisory and does not change HC:// protocol behavior, canonical record schemas, validators, signing logic, federation logic, or policy evaluator behavior.

## Scope

The scope covers repository contribution paths, CI/CD workflows, verification package handling, generated trust artifacts, documentation surfaces, and human-supervised validation boundaries. Runtime protocol guarantees must come from implemented and validated repository evidence, not from this document.

## Threat Actors

- **Malicious contributors** who attempt to introduce unsafe documentation, workflow, policy, validator, or canonical record changes through Pull Requests.
- **Supply-chain attackers** who target package dependencies, transitive dependencies, build tooling, or third-party GitHub Actions.
- **Compromised CI runners** that may expose workspace state, alter generated artifacts, or produce misleading check results.
- **Unauthorized validators** that attempt to influence verification outputs without repository-defined authority or review.
- **Dependency maintainers** whose packages or release processes may be compromised or may introduce unexpected behavior.

## Protected Assets

- **Canonical records** and related provenance continuity.
- **Verification packages** and their expected structure, hashes, signatures, and metadata.
- **Security policies** and policy interpretation boundaries.
- **Workflow secrets** and GitHub token permissions.
- **Generated trust artifacts**, including audit snapshots, explorer indexes, hashes, and verification reports.

## Attack Surfaces

- **GitHub Pull Requests** that modify source, documentation, workflows, dependencies, or governance controls.
- **Dependencies** installed by local contributors or CI jobs.
- **GitHub Actions** definitions, referenced third-party actions, token permissions, runners, and artifacts.
- **Validation pipeline** steps that normalize records, verify hashes, validate schemas, generate audit snapshots, or publish artifacts.
- **Static documentation site** content that may misstate trust kernel boundaries or imply unsupported guarantees.

## CI/CD Risks

### Third-Party Action Compromise

Actions referenced by tags can move if a maintainer changes the tag. Prefer pinning third-party actions to reviewed commit SHAs and updating them through human-reviewed dependency maintenance.

### Excessive Token Permissions

Workflow tokens should use least privilege. Most validation jobs only need:

```yaml
permissions:
  contents: read
```

Write permissions should be limited to workflows that intentionally write comments, labels, generated files, or merge state. Those workflows require additional review because they can affect repository state or Pull Request outcomes.

### Workflow Manipulation

Workflow changes can alter guardrails, checks, or release behavior. Treat `.github/workflows/**` changes as security-sensitive and require reviewer attention before merge.

### Artifact Poisoning

Generated artifacts can be misleading if they are produced from tampered inputs, a compromised runner, or an unsafe dependency. Artifacts should be scoped, named clearly, and treated as derived evidence until reviewed against canonical record and verification map expectations.

## Verification Package Manipulation

### Hash Modification

An attacker may attempt to update a hash without updating the reviewed source artifact, or modify both together to hide unauthorized changes. Hash verification must be paired with review of provenance, canonical record continuity, and relevant guard checks.

### Signature Bypass

An attacker may attempt to route around signature checks, weaken signing expectations, or present unsigned content as validated. Signing semantics are trust-kernel-sensitive and require explicit human-supervised validation before merge.

### Record Tampering

An attacker may alter record identity, timestamps, provenance fields, or canonical serialization assumptions. These changes affect canonical record boundaries and should be reviewed with the canonical artifact guard and relevant schema validation.

### Dependency Injection

An attacker may introduce new dependencies or loosen dependency constraints to run unexpected code in local or CI contexts. Dependency changes should be reviewed for necessity, source, maintenance posture, and CI impact.

## Human Review Limits

Human oversight is necessary but not sufficient by itself. Reviewers can miss subtle workflow permission changes, dependency behavior, generated artifact drift, or trust-kernel boundary impacts.

### Oversight Boundaries

- Automated checks provide advisory evidence, not autonomous governance finality.
- Reviewers should verify that claims are backed by repository evidence.
- Security-sensitive path changes require focused review even when tests pass.

### Escalation Paths

Escalate Pull Requests that touch or indirectly affect:

- canonical records or deterministic serialization assumptions;
- schema contracts;
- validator behavior;
- signing and trust anchor semantics;
- federation behavior;
- policy evaluator behavior;
- GitHub Actions permissions, workflow triggers, or release automation.

### Manual Review Requirements

Manual review should confirm that changed files match the stated Pull Request scope, required guard checks were run or explicitly deferred with a reason, and any trust kernel impact is documented for human-supervised validation.
