# Explorer Indexing Architecture

## Purpose
Define indexing architecture for public exploration, provenance traversal, and trust/audit lookups.

## Index Surfaces
- Searchable record index (`record_id`, title, tags, status, timestamps).
- Provenance graph index (record-to-record lineage and revision edges).
- Witness relation index (record-to-witness/validator signatures).
- Federation map index (node affiliations and sync state).
- Trust score lookup index (latest and historical scores).
- Audit chain lookup index (event references by record and actor).

## Generation Strategy
`src/generate_explorer_index.py` builds deterministic JSON indexes from repository data.

## Design Constraints
- Append-friendly; historical references are not overwritten.
- Deterministic output ordering for diffability.
- Supports incremental federation ingestion in future phases.
