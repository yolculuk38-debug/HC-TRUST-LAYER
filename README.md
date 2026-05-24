# HC-TRUST-LAYER

[![HC-TRUST-LAYER Validation](../../actions/workflows/validate.yml/badge.svg)](../../actions/workflows/validate.yml) [![CodeQL](../../actions/workflows/codeql.yml/badge.svg)](../../actions/workflows/codeql.yml)

> The visible architecture of digital trust.

## Current Release

[`v0.1.0`](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/releases/tag/v0.1.0) is the first stabilization release for the current verification infrastructure. It includes the visible verification flow and supports integrity and provenance as verification signals. Trust scoring and witness systems remain experimental.

## Visible Verification Flow (v0.1)

For first-time visitors, the shortest path is:

`record → hash → QR → verify → trust explanation`

Run this text-only demo flow:

```bash
PYTHONPATH=src python src/hash.py examples/demo_record.json
PYTHONPATH=src python src/qr.py HC-DEMO-2026-0001 9c169042065246d3b963163cfe8ffe876ffce57fa8759e402281d036f0f9cffc https://github.com/owner/repo/blob/main/examples/demo_record.json
PYTHONPATH=src python -m hc_trust.cli verify records
```

Example output snippets:

```text
SHA256: 9c169042065246d3b963163cfe8ffe876ffce57fa8759e402281d036f0f9cffc
✅ Secure QR oluşturuldu: qr/HC-DEMO-2026-0001.png
Results: 2 passed, 0 failed
```

Detailed walkthrough: [`docs/demo-flow.md`](docs/demo-flow.md).

Verify a Record: [`docs/verify.md`](docs/verify.md).

HC:// verifies integrity and provenance signals, not objective truth.

## Verify a Record

Start with the HC:// verification experience layer here: [`docs/verify.md`](docs/verify.md).

GitHub currently acts as the public archive mirror layer for HC:// records.

## What Is HC-TRUST-LAYER

HC-TRUST-LAYER is an open verification and provenance infrastructure for digital content in the AI era.

It provides open, auditable records so people can check whether content is consistent across time, sources, and distribution channels.

## Why It Exists

Digital content is easier to create, remix, and manipulate at scale. Synthetic media, altered documents, and context loss can make trust decisions harder.

HC-TRUST-LAYER exists to make verification workflows transparent instead of relying on unsupported claims.

## Core Verification Concept

HC-TRUST-LAYER focuses on verifiable records, not narrative authority.

A record can be checked by comparing:

- record identifier
- content hash
- validation status
- witness and provenance context

Verification is reproducible: anyone using the same input and rules should reach the same technical result.

## Verification Example

Sample verification values:

- sample record id: `HC-EXAMPLE-2026-0001`
- sample hash: `9f3a3fb4f7c21ab3a89d4f7db0bf75db6ea9cc57f398a7db53f4a62f5a4d8d57`
- sample validation result: `PASS (schema + hash)`

## Quick Start

```bash
pip install -r requirements.txt
PYTHONPATH=src python src/hash.py examples/demo_record.json
PYTHONPATH=src python src/qr.py HC-DEMO-2026-0001 9c169042065246d3b963163cfe8ffe876ffce57fa8759e402281d036f0f9cffc https://github.com/owner/repo/blob/main/examples/demo_record.json
PYTHONPATH=src python -m hc_trust.cli verify records
```

## Documentation And Examples

- docs: [`docs/`](docs/)
- Demo flow: [`docs/demo-flow.md`](docs/demo-flow.md)
- Verify a Record: [`docs/verify.md`](docs/verify.md)
- Verification result standard (v1): [`docs/verification-result-standard.md`](docs/verification-result-standard.md)
- Verification result badges: [`docs/verification-badges.md`](docs/verification-badges.md)
- Witness layer: [`docs/witness-layer.md`](docs/witness-layer.md)
- Trust graph foundation: [`docs/trust-graph.md`](docs/trust-graph.md)
- Trust decay and risk history foundation: [`docs/trust-decay-risk-history.md`](docs/trust-decay-risk-history.md)
- Federation discovery foundation: [`docs/federation-discovery.md`](docs/federation-discovery.md)
- Institutional governance foundation: [`docs/institutional-governance.md`](docs/institutional-governance.md)
- Evidence retention lifecycle foundation: [`docs/evidence-retention-lifecycle.md`](docs/evidence-retention-lifecycle.md)
- Trust query routing foundation: [`docs/trust-query-routing.md`](docs/trust-query-routing.md)
- Sustainability model foundation: [`docs/sustainability-model.md`](docs/sustainability-model.md)
- Long-term archival integrity foundation: [`docs/long-term-archival-integrity.md`](docs/long-term-archival-integrity.md)
- Offline verification foundation: [`docs/offline-verification.md`](docs/offline-verification.md)
- Verification snapshot foundation: [`docs/verification-snapshots.md`](docs/verification-snapshots.md)
- AI model provenance foundation: [`docs/ai-model-provenance.md`](docs/ai-model-provenance.md)
- Message and content provenance foundation: [`docs/message-content-provenance.md`](docs/message-content-provenance.md)
- Validator identity architecture foundation: [`docs/validator-identity-architecture.md`](docs/validator-identity-architecture.md)
- Replay and duplicate detection foundation: [`docs/replay-duplicate-detection.md`](docs/replay-duplicate-detection.md)
- Verification package v2 architecture foundation: [`docs/verification-package-v2.md`](docs/verification-package-v2.md)
- Verification explorer architecture foundation: [`docs/verification-explorer-architecture.md`](docs/verification-explorer-architecture.md)
- Verification scenario library foundation: [`docs/verification-scenarios.md`](docs/verification-scenarios.md)
- Demo verification flow foundation: [`docs/demo-verification-flow.md`](docs/demo-verification-flow.md)
- Provenance viewer foundation: [`docs/provenance-viewer.md`](docs/provenance-viewer.md)
- Public verification flow foundation: [`docs/public-verification-flow.md`](docs/public-verification-flow.md)
- MVP-1 verification package viewer specification: [`docs/mvp-1-verification-package-viewer.md`](docs/mvp-1-verification-package-viewer.md)
- MVP-1 user flow: [`docs/mvp-1-user-flow.md`](docs/mvp-1-user-flow.md)
- MVP-1 UI principles: [`docs/mvp-1-ui-principles.md`](docs/mvp-1-ui-principles.md)
- MVP-1 boundaries: [`docs/mvp-1-boundaries.md`](docs/mvp-1-boundaries.md)
- Trust workflow model foundation: [`docs/trust-workflow-model.md`](docs/trust-workflow-model.md)
- Trust graph viewer foundation: [`docs/trust-graph-viewer.md`](docs/trust-graph-viewer.md)
- Privacy and redaction model foundation: [`docs/privacy-redaction-model.md`](docs/privacy-redaction-model.md)
- C2PA bridge considerations foundation: [`docs/c2pa-bridge-considerations.md`](docs/c2pa-bridge-considerations.md)
- Signing architecture foundation: [`docs/signing-architecture.md`](docs/signing-architecture.md)
- Dispute resolution and challenge architecture foundation: [`docs/dispute-challenge-architecture.md`](docs/dispute-challenge-architecture.md)
- Verification levels model: [`docs/verification-levels.md`](docs/verification-levels.md)
- Glossary and naming hierarchy: [`docs/glossary.md`](docs/glossary.md)
- Trust scoring: [`docs/trust-scoring.md`](docs/trust-scoring.md)
- Experimental trust engine v1 (draft): [`docs/trust-engine-v1.md`](docs/trust-engine-v1.md)
- Experimental trust score foundation: [`docs/trust-score.md`](docs/trust-score.md)
- Limitations and risks: [`docs/limitations-and-risks.md`](docs/limitations-and-risks.md)
- Record format: [`docs/record-format.md`](docs/record-format.md)
- Architecture roadmap (planned): [`docs/architecture-roadmap.md`](docs/architecture-roadmap.md)
- Master architecture foundation: [`docs/master-architecture.md`](docs/master-architecture.md)
- Implementation map (layer-to-code status): [`docs/implementation-map.md`](docs/implementation-map.md)
- Capability status matrix: [`docs/capability-status.md`](docs/capability-status.md)
- Trust kernel stabilization checkpoint (PR #300): [`docs/trust-kernel-checkpoint-300.md`](docs/trust-kernel-checkpoint-300.md)
- Protocol graph and agent context map foundation: [`docs/protocol-graph-agent-context.md`](docs/protocol-graph-agent-context.md)
- Verification map foundation: [`docs/verification-map.md`](docs/verification-map.md)
- Agent governance foundation: [`docs/agent-governance.md`](docs/agent-governance.md)
- Execution audit trail foundation: [`docs/execution-audit-trail.md`](docs/execution-audit-trail.md)
- Approval checkpoints baseline: [`docs/approval-checkpoints.md`](docs/approval-checkpoints.md)
- AI-assisted review workflow: [`docs/ai-assisted-review.md`](docs/ai-assisted-review.md)
- AI collaboration and contribution workflow: [`docs/ai-collaboration-workflow.md`](docs/ai-collaboration-workflow.md)
- Reviewer registry and independent review pool: [`docs/reviewer-registry.md`](docs/reviewer-registry.md)
- Reviewer selection principles: [`docs/reviewer-selection.md`](docs/reviewer-selection.md)
- Release automation plan: [`docs/release-automation.md`](docs/release-automation.md)
- examples: [`examples/`](examples/)
- AI witness example: [`examples/ai_witness_example.json`](examples/ai_witness_example.json)

## Project Context

HC-TRUST-LAYER is the primary technical brand and repository name.

Humanity Chain may appear as historical/origin project context only.


## Repository Roles

- **HC-TRUST-LAYER** is the canonical repository for active protocol and implementation.
- **Insanlik-Zinciri** is the historical/origin mirror for provenance continuity.
- Trust graph data model foundation: [`docs/trust-graph-data-model.md`](docs/trust-graph-data-model.md)
- Validator capability model foundation: [`docs/validator-capability-model.md`](docs/validator-capability-model.md)
- Evidence continuity foundation: [`docs/evidence-continuity.md`](docs/evidence-continuity.md)
- Verification routing model foundation: [`docs/verification-routing-model.md`](docs/verification-routing-model.md)
