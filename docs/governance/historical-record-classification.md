# Historical Record Classification

## Purpose

This note classifies existing verified test, demo, and workflow records without moving, deleting, rewriting, or reissuing the records. It is documentation/classification metadata only and does not change canonical record contents, hashes, QR references, generated audit snapshots, schemas, validators, source code, workflows, policy, federation, signing, or trust-kernel artifacts.

Historical verified records remain provenance-bearing HC:// artifacts. They must not be deleted. They are not current v0.1.0 release evidence and should not be used as active v0.1.0 public QR targets.

## Classification Summary

| Record | Current path | Classification | Recommended lifecycle state | Active release evidence | Public QR target | Known risks / notes |
| --- | --- | --- | --- | --- | --- | --- |
| `HC-TEST-2026-0001` | `records/verified/HC-TEST-2026-0001.md` | `historical_test_record` | `archived` / historical reference after maintainer-approved migration | No | No | Historical test record retained for provenance and compatibility with existing examples, hashes, and references. It should not be presented as current release evidence. |
| `HC-CHATGPT-2026-0001` | `records/verified/HC-CHATGPT-2026-0001.md` | `historical_workflow_test_record` | `archived` / historical reference after maintainer-approved migration | No | No | Historical workflow test record retained for audit continuity. Existing QR and hash references may depend on the current path, so it should not be treated as an active v0.1.0 public verification target. |
| `HC-CHATGPT-2026-0002` | `records/verified/HC-CHATGPT-2026-0002.md` | `historical_demo_or_protocol_context_record` | `archived` / historical reference after maintainer-approved migration | No | No | Historical demo or protocol-context record retained for review context. It should not be used to imply current release evidence, production readiness, forensic certainty, or live public verifier availability. |

## Operational Guidance

- These records must not be deleted.
- These records are not current release evidence.
- QR targets should not use these records as active v0.1.0 public targets.
- Archive migration requires a later maintainer-approved PR.
- Moving these records requires updating hash manifests, QR references, release evidence references, generated audit snapshots, and documentation examples.

## Review Boundary

This classification does not move records out of `records/verified/`, does not update hash material, and does not change verification semantics. It only documents how maintainers should interpret these existing verified records during v0.1.0 stabilization and future archive planning.
