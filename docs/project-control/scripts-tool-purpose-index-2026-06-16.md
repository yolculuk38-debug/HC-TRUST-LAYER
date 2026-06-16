# Scripts Tool Purpose Index — 2026-06-16

Status: advisory tooling-surface index.

This document classifies the `scripts/` tooling surface so HC-TRUST-LAYER helper scripts can be reviewed by operating boundary instead of by filename guesswork.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This index is documentation only.
- This index does not modify scripts, workflows, source behavior, tests, schemas, records, QR data, hash data, generated artifacts, or repository settings.
- No tool is moved, renamed, deleted, disabled, or consolidated by this document.

## Tooling operating rule

`scripts/` should contain local tools, CI helpers, report generators, validators, and deterministic assistant helpers. Tooling must be reviewed by capability and permission boundary:

```text
read-only check -> local report -> generated advisory artifact -> workflow integration -> write-capable automation
```

The safer default is read-only, local, deterministic, and report-only.

## Main tooling classes

| Class | Purpose | Review posture |
|---|---|---|
| `DETERMINISTIC_GUARD` | Fails or reports when repository text, docs, or changed files violate a fixed rule. | Rule changes require focused review. |
| `ADVISORY_REPORTER` | Produces public-safe advisory JSON, markdown, or logs. | Must not become decision authority. |
| `LOCAL_VERIFIER` | Runs local verification, hash checks, or package checks. | Must preserve local/advisory boundary. |
| `INVENTORY_TOOL` | Lists files, sources, generated artifacts, or coverage surfaces. | Output is reference evidence, not canonical record. |
| `HANDOFF_TOOL` | Converts issues, fixtures, or task descriptions into structured work packages. | Must not trigger external execution by itself. |
| `RELEASE_AUDIT_TOOL` | Checks release or audit readiness. | Must not replace human release review. |
| `GENERATOR` | Produces derived files, examples, summaries, or indexes. | Generator/source path must remain clear. |
| `WRITE_CAPABLE_TOOL` | Modifies files or repository state when invoked. | High review. Keep separate from read-only tools. |

## Verified tool anchors

These tool anchors were checked from current repository content during this indexing pass:

| Path | Class | Purpose |
|---|---|---|
| `scripts/hc_control_bot.py` | `ADVISORY_REPORTER` | Deterministic HC Control Bot scanner for changed file paths and protected-surface routing. It intentionally avoids network calls, model calls, labels, assignments, and repository writes. |
| `scripts/check_terminology.py` | `DETERMINISTIC_GUARD` | Documentation terminology guard with forbidden and warning phrase lists. |

This is not a complete script inventory. It is the first tool-purpose map. A later PR may add a complete script inventory if a file-listing pass is needed.

## Capability boundaries

Scripts should clearly state whether they are:

- read-only;
- local-only;
- report-only;
- generator-only;
- workflow helper;
- write-capable;
- security-adjacent;
- release/audit-adjacent.

If a script writes files, emits artifacts, opens network connections, invokes external tools, or changes repository state, it should be reviewed as higher risk.

## Review rules for script changes

A script change should identify:

1. exact script paths changed;
2. whether behavior is read-only or write-capable;
3. whether it can run in GitHub Actions;
4. whether it reads untrusted PR content;
5. whether it touches generated output;
6. whether it affects release, audit, governance, runtime, validator, QR, hash, record, or security behavior;
7. targeted tests or checks.

## Do not combine

Do not combine script changes with unrelated:

- workflow permission changes;
- runtime behavior changes;
- dependency upgrades;
- schema changes;
- record/hash/QR edits;
- governance authority changes;
- generated artifact rewrites.

## Immediate next index work

1. generated/reference artifact index.
2. historical/evidence index.
3. public/demo docs index.
4. optional complete script inventory.

## Final rule

Scripts must be easy to classify before they are easy to run.

```text
clear capability
clear inputs
clear outputs
clear risk
no hidden authority
```
