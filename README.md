# HC-TRUST-LAYER

> **Documentation Status**
> - **status:** PARTIAL
> - **scope:** Repository entrypoint, verification map navigation, and trust kernel orientation.
> - **canonical relevance:** Advisory index into canonical record and schema boundaries; not a canonical record surface.
> - **runtime relevance:** High for operator/reviewer navigation; does not define runtime enforcement logic.

[![Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![MVP Status](https://img.shields.io/badge/Status-MVP%20(Early--Stage)-orange)
![Trust Infrastructure](https://img.shields.io/badge/Category-Trust%20Infrastructure-4c1)
![Verification Workflow](https://img.shields.io/badge/Focus-Verification%20Workflow-6f42c1)
[![HC-TRUST-LAYER Validation](../../actions/workflows/validate.yml/badge.svg)](../../actions/workflows/validate.yml)

> HC:// trust infrastructure for verification workflow transparency, provenance visibility, and human-supervised validation.

HC-TRUST-LAYER is an early-stage verification infrastructure that helps teams evaluate integrity and provenance signals through an auditable verification map and protocol graph. It supports reproducible technical checks and structured review boundaries; it does **not** claim objective-truth finality, forensic certainty, or autonomous finality.

## Quick Navigation

- [MVP Snapshot](#mvp-snapshot)
- [Demo & Verification Viewer](#demo--verification-viewer)
- [Try local verification preview](#try-local-verification-preview-entry-point)
- [Public trial quickstart](docs/public_trial_quickstart.md)
- [Local advisory runtime runbook](docs/local_runtime_runbook.md)
- [Verification Flow Example](#verification-flow-example)
- [Verification Result Types](#verification-result-types)
- [Architecture Overview](#architecture-overview)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [Supervised automation policy](docs/supervised_automation_policy.md)
- [Security & Responsible Use](#security--responsible-use)
- [IP / Brand / Idea Use Notice](#ip--brand--idea-use-notice)
- [Historical Origin](#historical-origin)
- [Long-Term Direction](#long-term-direction)

## MVP Snapshot

Current focus: establish a stable HC:// verification workflow with clear trust-kernel boundaries, reproducible package checks, and auditable reviewer handoff.

- Scope: verification package generation, validation outputs, and viewer-first review flow.
- Positioning: early-stage infrastructure for transparent verification, not production-final trust arbitration.
- Canonical boundaries: schema continuity, provenance continuity, audit trail continuity.

Key docs:

### Implementation Status View

- **Implemented systems:** record integrity verification baseline, public verification CLI/API baseline, QR verification baseline.
- **Experimental systems (partial):** witness/signature expansion, explorer/index visibility, trust scoring foundations.
- **Conceptual future layers (planned/research):** federation/sync interoperability, ecosystem integrations, long-horizon institutional adapters.

Core architecture/status references:

- Master architecture: [`docs/master-architecture.md`](docs/master-architecture.md)
- Implementation map: [`docs/implementation-map.md`](docs/implementation-map.md)
- Capability status matrix: [`docs/capability-status.md`](docs/capability-status.md)
- Foundation completion and transition: [`docs/FOUNDATION_STATUS.md`](docs/FOUNDATION_STATUS.md)

- MVP CLI viewer: [`docs/mvp-1-cli-viewer.md`](docs/mvp-1-cli-viewer.md)
- Static viewer guide: [`docs/static-viewer.md`](docs/static-viewer.md)
- Verification package examples: [`docs/verification-package-examples.md`](docs/verification-package-examples.md)
- Verification package viewer spec: [`docs/mvp-1-verification-package-viewer.md`](docs/mvp-1-verification-package-viewer.md)

## Demo & Verification Viewer

Use the CLI + viewer workflow to inspect verification packages and provenance timeline signals.

### Try local verification preview entry point

For the fastest public HC:// demo path on mobile or desktop, start here:

- **Try local verification preview:** [`docs/self-service-verify.html`](docs/self-service-verify.html)
- **No upload**
- **Browser-side SHA-256**
- **Preview only, not registration**

### Try local verification preview

Open the public self-service verification prototype at [`docs/self-service-verify.html`](docs/self-service-verify.html).

- **No upload**
- **Browser-side SHA-256**
- **Preview only, not registration**

This mobile-readable entry point is designed for quick HC:// self-service verification preview before any human-supervised validation handoff.

```bash
pip install -r requirements.txt
PYTHONPATH=src python -m hc_trust.cli verify records
```

Then continue with:

- Static viewer onboarding: [`docs/static-viewer.md`](docs/static-viewer.md)
- MVP-1 public demo quick links: [`docs/demo-index.md`](docs/demo-index.md)
- Public trust guide: [`docs/public/hc-public-trust-guide.md`](docs/public/hc-public-trust-guide.md)
- MVP-1 package viewer specification: [`docs/mvp-1-verification-package-viewer.md`](docs/mvp-1-verification-package-viewer.md)
- Package examples for replay and review: [`docs/verification-package-examples.md`](docs/verification-package-examples.md)

MVP-1 public demo quick links (bundled samples):

- `docs/verification-viewer.html#verified-trace`
- `docs/verification-viewer.html#partial-trace`
- `docs/verification-viewer.html#replay-warning`
- `docs/verification-viewer.html#disputed`
- `docs/verification-viewer.html#unverified`

Shareable hash links map only to bundled demo packages.
Local uploaded package content is not stored in URL state.
For reviewer handoff, prefer mobile-first checks so trust labels and warnings remain readable on phone-sized viewports.
As with all HC:// trust outcomes, consequential interpretation requires human-supervised validation.

## Verification Flow Example

```text
record input
  -> canonical packaging
  -> integrity + provenance checks
  -> verification package
  -> verification viewer review
  -> validator review layer
  -> trust result classification
```

HC:// outputs verification-oriented results that support human-supervised validation and dispute analysis.

## Verification Result Types

| Result Type | Meaning | Typical Next Step |
|---|---|---|
| PASS | Required checks passed for the evaluated package scope. | Continue with reviewer acknowledgment and archive. |
| REVIEW | Signals are incomplete, ambiguous, or require policy interpretation. | Route to validator review layer for human-supervised validation. |
| FAIL | One or more required checks failed in current scope. | Investigate provenance timeline and rerun after remediation. |
| INCONCLUSIVE | Evidence is insufficient for a stable classification. | Collect additional canonical record evidence and replay. |

## Architecture Overview

```text
User
  ↓
Verification Viewer
  ↓
Verification Package
  ↓
Provenance Timeline
  ↓
Validator Review Layer
  ↓
Replay & Dispute Analysis
  ↓
Trust Result
```

This architecture emphasizes transparent review flow, auditable boundaries, and reproducible verification outcomes.

## Repository Structure

- `src/` — HC:// verification tooling and CLI surfaces.
- `records/` — verification records used in validation workflows.
- `examples/` — verification package and record examples.
- `docs/` — protocol graph, verification map, trust kernel, and MVP guidance.
- `scripts/` — repository guardrails (terminology, docs drift, canonical artifact checks).

## Contributing

Contributions are welcome for documentation quality, onboarding clarity, viewer usability, and verification workflow improvements.

Before opening a PR:

1. Keep terminology aligned with HC:// and HC-TRUST-LAYER.
2. Keep changes scoped, auditable, and reversible.
3. Run repository checks relevant to your change.
4. Avoid production-readiness or certainty claims not validated in-repo.

## Security & Responsible Use

- Treat outputs as verification signals, not definitive truth claims.
- Preserve audit trail continuity when proposing trust-kernel-adjacent updates.
- Escalate non-trivial policy or validator behavior changes for human-supervised validation.
- Review project boundaries and risks in [`docs/limitations-and-risks.md`](docs/limitations-and-risks.md).

## IP / Brand / Idea Use Notice

HC-TRUST-LAYER is released under Apache-2.0 (see [`LICENSE`](LICENSE)).

“HC://” and related project identity elements remain part of the repository’s attribution and provenance context. Reuse should preserve origin references and avoid implying endorsement, production guarantees, or governance finality.

## Historical Origin

This repository is the canonical active home for HC-TRUST-LAYER. Historical/origin references may appear for provenance continuity and canonical record traceability.

## Long-Term Direction

Long-term direction includes stronger verification package interoperability, clearer trust kernel interfaces, and expanded replay/dispute tooling while maintaining human-supervised validation.

Planning references:

- [`HC_CONSTITUTION.md`](HC_CONSTITUTION.md)
- [`docs/core-stabilization-plan.md`](docs/core-stabilization-plan.md)
- [`docs/mvp-priority-roadmap.md`](docs/mvp-priority-roadmap.md)
- [`docs/architecture-consolidation.md`](docs/architecture-consolidation.md)

## Closing Philosophy

HC:// is designed to make verification workflow evidence inspectable, reproducible, and reviewable across time. HC-TRUST-LAYER aims to strengthen trust decisions through transparent process and provenance—not through unverifiable certainty claims.
