# HC-TRUST-LAYER Explorer Index Specification

## Status and Scope

This document defines a stable, modular architecture for explorer indexing and provenance lookup in HC-TRUST-LAYER.

It is designed to:
- preserve backward compatibility with current repository layouts,
- keep canonical verification records separate from generated artifacts,
- support scalable public lookup and provenance traversal,
- maintain consistent project terminology.

This specification is architecture guidance for explorer and indexing behavior. It does not change canonical record formats.

---

## 1) Canonical index structure

Explorer indexes are generated lookup artifacts that reference canonical records. They are not canonical records themselves.

### 1.1 Index package layout (conceptual)

```text
explorer/
  index/
    records.json            # primary record lookup index
    witnesses.json          # witness-centric lookup index
    provenance.json         # provenance graph adjacency index
    revisions.json          # revision chain index
    federation.json         # federation source and propagation index
    manifest.json           # version + generation metadata for index package
```

Implementations may place generated index files in repository-specific paths, but must preserve the same logical separation.

### 1.2 Primary record index shape

Each entry should map a `record_id` to normalized metadata and lookup pointers.

Example shape:

```json
{
  "version": "1",
  "generated_at": "2026-05-23T00:00:00Z",
  "records": {
    "HC-CHATGPT-2026-0001": {
      "record_id": "HC-CHATGPT-2026-0001",
      "canonical_path": "records/verified/HC-CHATGPT-2026-0001.md",
      "content_hash": "sha256:...",
      "verification_status": "verified",
      "witness_count": 3,
      "trust_score": 0.94,
      "revision_state": "current",
      "federation_state": "local",
      "created_at": "2026-01-02T11:22:33Z",
      "updated_at": "2026-01-08T09:10:11Z",
      "pointers": {
        "witness_index_key": "HC-CHATGPT-2026-0001",
        "provenance_index_key": "HC-CHATGPT-2026-0001",
        "revision_index_key": "HC-CHATGPT-2026-0001"
      }
    }
  }
}
```

---

## 2) Searchable metadata model

Explorer indexes should normalize and expose the following metadata fields:

- `record_id`: stable canonical record identifier.
- `content_hash`: immutable hash of canonical content at indexed revision.
- `verification_status`: verification lifecycle status (for example `pending`, `verified`, `archived`).
- `witness_count`: number of associated witness entries.
- `trust_score`: numeric trust aggregate produced by project-defined policy.
- `revision_state`: state in revision chain (for example `current`, `superseded`, `forked`).
- `federation_state`: federation publication/ingestion state (for example `local`, `exported`, `imported`, `mirrored`).
- `created_at`: canonical creation timestamp.
- `updated_at`: canonical last-updated timestamp.

Compatibility rule:
- New metadata fields may be added as optional fields.
- Existing fields should remain stable once published.

---

## 3) Witness lookup structure

Witness lookup indexes enable fast retrieval by witness identity and by record.

Recommended shape:

```json
{
  "by_record": {
    "HC-CHATGPT-2026-0001": ["wit_001", "wit_002", "wit_003"]
  },
  "by_witness": {
    "wit_001": {
      "witness_id": "wit_001",
      "records": ["HC-CHATGPT-2026-0001"],
      "type": "human",
      "status": "active"
    }
  }
}
```

Guidance:
- `by_record` supports record-centric explorer pages.
- `by_witness` supports witness explorer and reverse lookup.
- Witness objects in indexes should avoid storing sensitive raw payloads; store pointers and summary metadata.

---

## 4) Provenance lookup structure

Provenance lookup indexes represent graph relationships needed for public verification explanation.

Recommended graph-oriented shape:

```json
{
  "nodes": {
    "rec:HC-CHATGPT-2026-0001": {"kind": "record", "record_id": "HC-CHATGPT-2026-0001"},
    "wit:wit_001": {"kind": "witness", "witness_id": "wit_001"}
  },
  "edges": [
    {"from": "wit:wit_001", "to": "rec:HC-CHATGPT-2026-0001", "relation": "attests"},
    {"from": "rec:HC-CHATGPT-2026-0001", "to": "rec:HC-CHATGPT-2026-0002", "relation": "revises"}
  ]
}
```

Edge relation set should remain explicit and versioned (for example `attests`, `revises`, `derived_from`, `federated_from`, `federated_to`).

---

## 5) Revision lookup structure

Revision indexes provide stable traversal across record history.

Recommended shape:

```json
{
  "chains": {
    "HC-CHATGPT-2026-0001": {
      "head": "HC-CHATGPT-2026-0003",
      "members": [
        "HC-CHATGPT-2026-0001",
        "HC-CHATGPT-2026-0002",
        "HC-CHATGPT-2026-0003"
      ]
    }
  },
  "reverse": {
    "HC-CHATGPT-2026-0002": {"previous": "HC-CHATGPT-2026-0001", "next": "HC-CHATGPT-2026-0003"}
  }
}
```

Rules:
- Revision membership must reference canonical record IDs only.
- Multiple branch heads may be represented for forked histories.

---

## 6) Federation source mapping

Federation mapping tracks origin and propagation without redefining canonical content.

Recommended shape:

```json
{
  "sources": {
    "HC-CHATGPT-2026-0001": {
      "origin": "local-node-a",
      "seen_on": ["local-node-a", "partner-node-b"],
      "imported_from": null,
      "exported_to": ["partner-node-b"],
      "last_sync_at": "2026-05-23T00:00:00Z"
    }
  }
}
```

Guidance:
- Federation metadata is operational and generated.
- Canonical record validity must not depend on federation sync state.

---

## 7) Explorer artifact separation and validation boundaries

### 7.1 Artifact classes

1. **Canonical records**
   - Authoritative verification data and signed or validated record payloads.

2. **Generated indexes**
   - Lookup-oriented artifacts derived from canonical records.

3. **Manifests**
   - Generation metadata describing index version, schema version, and source snapshot.

4. **Cache/export artifacts**
   - Derived artifacts intended for distribution, caching, or transport.

### 7.2 Validation rules

- Validation applies to canonical records.
- Explorer indexes are not canonical records.
- Generated artifacts must not fail canonical validation gates.
- Validation tools should explicitly skip generated index/cache/export paths.

### 7.3 File treatment matrix

| Artifact type | Must be validated | Must be skipped by canonical validation | Generated only |
|---|---:|---:|---:|
| Canonical records (`records/verified`, `records/pending`, signed payloads) | Yes | No | No |
| Generated indexes (for example explorer index files) | No | Yes | Yes |
| Index manifests | No (canonical) / Yes (schema, optional) | Yes | Yes |
| Cache/export artifacts | No | Yes | Yes |

Backward compatibility rule:
- Existing layouts (for example `records/explorer_index.json`) remain valid as generated index locations.

---

## 8) Provenance graph architecture notes

### 8.1 Witness relationships

- Witness nodes attach attestations to record nodes.
- Multiple witnesses may attest the same record.
- Witness disagreement is represented as parallel attestations with independent status metadata.

### 8.2 Revision chains

- Revision edges connect prior and successor canonical records.
- Chains support linear or branched history.
- Explorer views should expose current head and full lineage.

### 8.3 Verification lineage

- Verification lineage combines witness attestations, revision edges, and verification status transitions.
- Lineage traversal should be deterministic from index snapshots.

### 8.4 Federation propagation

- Federation edges represent record movement across nodes.
- Propagation metadata should not override canonical provenance relations.

### 8.5 Audit graph behavior

- Audit traversal should permit:
  - forward exploration (origin to latest state),
  - reverse exploration (current state to origin),
  - relationship filtering by edge type.
- Graph snapshots should be reproducible from the same canonical source set.

---

## 9) Scalable indexing preparation

Architecture should support multiple storage and query backends while preserving logical model parity.

Planned backends:
- SQLite indexes for local transactional lookup.
- JSON indexes for static export and repository-native workflows.
- Graph relations for provenance traversal and lineage queries.
- Search backends for text and metadata lookup at scale.

Design constraints:
- Shared canonical schema contract across backends.
- Stable identifier strategy (`record_id`, node IDs, witness IDs).
- Deterministic index build pipeline.
- Incremental update capability for high-volume growth.

---

## 10) Public explorer UX notes (forward-looking)

Future explorer features may include:
- public verify lookup by `record_id` and hash,
- trust explanation panels (witness counts, trust factors, status inputs),
- revision history timelines,
- provenance chain visualization,
- witness explorer views,
- federation explorer views.

UX principle:
- The explorer presents generated lookup results and explanations.
- Canonical verification decisions are grounded in canonical records and verification rules.

---

## 11) Terminology consistency

Standard terms for this project scope:

- **Explorer**: user-facing lookup and navigation layer.
- **Index**: generated data structure optimized for lookup/traversal.
- **Manifest**: metadata about generation version, schema, and source snapshot.
- **Canonical record**: authoritative verification record subject to canonical validation.
- **Generated artifact**: non-canonical derived output (indexes, exports, caches).
- **Provenance graph**: relationship model connecting witnesses, records, revisions, and federation movement.
- **Verification package**: bundle containing canonical record material and associated verification context for transport or processing.

Use these terms consistently across docs, tooling, and explorer implementations.
