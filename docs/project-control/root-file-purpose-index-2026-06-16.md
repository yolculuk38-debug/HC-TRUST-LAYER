# Root File Purpose Index — 2026-06-16

Status: advisory root-surface index.

This document classifies the repository root surface so HC-TRUST-LAYER can be read like a professional trust-infrastructure project instead of a crowded file list.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This index does not delete, move, rename, archive, disable, rewrite, or reclassify files in Git.
- Future moves or deletions require a separate PR with evidence, risk notes, CI, and post-merge audit.

## Root operating rule

The repository root should contain only high-value entry points, project metadata, protected authority files, machine-readable reference indexes, and top-level directories. Everything else should eventually be classified before any proposed move.

## Root file classes

### Canonical public entry points

These files explain the project to a public reader or contributor.

| Path | Class | Purpose | Cleanup rule |
|---|---|---|---|
| `README.md` | `PUBLIC_ENTRYPOINT` | Public overview, quickest project explanation, and demo path. | Keep at root. Improve clarity only. |
| `CONTRIBUTING.md` | `CONTRIBUTOR_ENTRYPOINT` | Contribution rules and PR workflow. | Keep at root. |
| `SECURITY.md` | `SECURITY_ENTRYPOINT` | Vulnerability reporting and security contact path. | Keep at root; protected review. |
| `CHANGELOG.md` | `RELEASE_HISTORY` | Human-readable release/change history. | Keep at root unless release process changes. |
| `ROADMAP.md` | `PUBLIC_PLANNING_ENTRYPOINT` | Public roadmap and high-level direction. | Keep at root if concise; detailed planning belongs under `docs/`. |
| `LICENSE` | `LEGAL_METADATA` | Repository license. | Keep at root. |
| `VERSION` | `RELEASE_METADATA` | Current version marker. | Keep at root. |

### Authority and agent-operation files

These files define governance, human authority, or agent behavior.

| Path | Class | Purpose | Cleanup rule |
|---|---|---|---|
| `GOVERNANCE.md` | `GOVERNANCE_SECURITY` | Decision authority, review escalation, and merge boundaries. | Keep at root; protected review. |
| `HC_CONSTITUTION.md` | `GOVERNANCE_SECURITY` | Immutable HC principles. | Keep at root; do not weaken. |
| `AGENTS.md` | `OPERATING_LAYER` | AI/agent operating rules. | Keep at root; protected review. |
| `HC_BOOTSTRAP.md` | `OPERATING_LAYER` | Startup/check-in protocol for AI and operators. | Keep at root; protected review. |
| `CODEOWNERS` | `GOVERNANCE_SECURITY` | Ownership/review routing. | Keep at root or `.github/`; protected review. |

### Python/package/tooling metadata

These files define local development, package metadata, or dependency behavior.

| Path | Class | Purpose | Cleanup rule |
|---|---|---|---|
| `pyproject.toml` | `TOOLING` | Python package/build/test tool configuration. | Keep at root; changes require tests. |
| `requirements.txt` | `TOOLING` | Runtime or baseline dependencies. | Keep at root; dependency changes require coordinated review. |
| `requirements-test.txt` | `TOOLING` | Test-only dependencies when present. | Keep at root or consolidate only with dependency review. |
| `.gitignore` | `TOOLING` | Git ignore rules. | Keep at root. |
| `.terminology_allowlist` | `TOOLING` | Terminology guard allowlist. | Keep at root unless tool path changes. |

### Machine-readable reference indexes

These files support repo navigation, protocol structure, or generated/reference evidence.

| Path | Class | Purpose | Cleanup rule |
|---|---|---|---|
| `protocol-graph.json` | `GENERATED_REFERENCE` | Protocol structure/navigation reference. | Do not edit casually; generator/source must be known. |
| `verification-map.json` | `GENERATED_REFERENCE` | Verification flow metadata. | Do not edit casually; preserve source path. |
| `trust-kernel-index.json` | `GENERATED_REFERENCE` | Advisory trust-kernel index. | Protected reference; update only with explicit evidence. |

## Root directory classes

### Active implementation and tests

| Path | Class | Purpose | Cleanup rule |
|---|---|---|---|
| `src/` | `ACTIVE_IMPLEMENTATION` | Runtime, validator, QR, public validator, package verification, redaction, event, policy, and bridge code. | No moves until `src` module purpose index exists. |
| `tests/` | `TEST_EVIDENCE` | Executable regression evidence for trust boundaries. | No moves/deletions until test map and assertion-level review. |
| `scripts/` | `TOOLING` | Local CLIs, repo tooling, report generators, bots, and helper scripts. | No moves until script/tool purpose index exists. |
| `examples/` | `PUBLIC_DEMO` | Example records/packages/payloads for demos or tests. | Preserve until public/demo index exists. |

### Trust-kernel and evidence directories

| Path | Class | Purpose | Cleanup rule |
|---|---|---|---|
| `schema/` | `DO_NOT_TOUCH_PROTECTED` | Canonical schema definitions. | Protected; explicit review only. |
| `validators/` | `DO_NOT_TOUCH_PROTECTED` | Validator logic if present. | Protected; explicit review only. |
| `records/` | `HISTORICAL_EVIDENCE` | Evidence-bearing records and archived records. | Never silently rewrite. |
| `hash/` | `HISTORICAL_EVIDENCE` | Hash references and integrity artifacts. | Protected evidence; no casual cleanup. |
| `qr/` | `PUBLIC_DEMO` | QR artifacts, fixtures, or public verification paths. | Security-adjacent; classify before moving. |
| `generated/` | `GENERATED_REFERENCE` | Generated indexes/snapshots/reference outputs. | Derived; do not treat as canonical record. |
| `policy/` | `GOVERNANCE_SECURITY` | Policy and access-control behavior. | Protected; explicit review only. |
| `federation/` | `DO_NOT_TOUCH_PROTECTED` | Federation behavior and exchange logic. | Protected; explicit review only. |
| `signatures/` | `DO_NOT_TOUCH_PROTECTED` | Signature artifacts/logic if present. | Protected; explicit review only. |
| `canonical/` | `DO_NOT_TOUCH_PROTECTED` | Canonical record or artifact boundary if present. | Protected; explicit review only. |

### Documentation and governance directories

| Path | Class | Purpose | Cleanup rule |
|---|---|---|---|
| `docs/` | `DOCUMENTATION_SURFACE` | Public docs, demo docs, governance docs, security docs, vision docs, project-control docs. | Requires docs directory purpose index before moves. |
| `.github/` | `GOVERNANCE_SECURITY` | Workflows, templates, Dependabot, issue/PR automation. | Protected; workflow changes require separate review. |

### Historical and vision/provenance directories

These may look unusual in a standard software repo, but they may preserve HC provenance.

| Path | Class | Purpose | Cleanup rule |
|---|---|---|---|
| `halkalar/` | `HISTORICAL_EVIDENCE` | Witness/origin/provenance trail from early Humanity Chain / HC evolution. | Preserve; index before any archive proposal. |
| `witness/` | `HISTORICAL_EVIDENCE` | Witness-related references or records. | Preserve; protected review if signing/witness semantics. |
| `timeline/` | `HISTORICAL_EVIDENCE` | Timeline/provenance chronology. | Preserve; index first. |
| `council/` | `VISION_REFERENCE` | Council or multi-reviewer concept records if present. | Classify before moving. |
| `media/` | `VISION_REFERENCE` | Media/provenance examples or concept docs if present. | Classify before moving. |
| `tools/` | `TOOLING` | Developer tools if present. | Classify with script/tool index. |

## Root cleanup rules

### Keep at root

Keep files at root when they are:

- public entry points;
- governance/authority entry points;
- legal/release metadata;
- Python/package metadata;
- machine-readable top-level indexes;
- top-level directories with clear purpose.

### Candidate for later move only after classification

A root item can become a move candidate only if all are true:

1. it is not evidence-bearing;
2. it is not protected;
3. it is not required by tooling/CI;
4. it has a better target folder;
5. an index or redirect note preserves discoverability;
6. CI remains green;
7. human review accepts the move.

### Never move/delete from visual clutter alone

Visual clutter is a signal for mapping, not deletion.

## Immediate next index work

1. `docs/` directory purpose index.
2. `src/` module purpose index.
3. `scripts/` tool purpose index.
4. generated/reference artifact index.
5. historical/evidence index.

## Final rule

Root must become a clean control panel, not a hiding place.

```text
public entry -> governance entry -> implementation folders -> evidence folders -> generated references
```
