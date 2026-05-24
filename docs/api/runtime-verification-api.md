# Runtime Verification API (Experimental)

The HC-TRUST-LAYER runtime verification API is an experimental public API scaffold.
It is intended for local development and architecture validation, not production trust enforcement.

## Experimental Status

- This service is explicitly experimental.
- Verification responses are placeholder-normalized for protocol consistency.
- Federation integration is not yet active.

## Non-Production Limitations

- Trust scores are placeholder values.
- Witness and revision analytics are not yet connected to a consensus runtime.
- Federation source verification is planned but currently returns empty sources.

## Endpoint Behavior

- `GET /health`: service liveness check.
- `GET /version`: runtime API version metadata.
- `GET /experimental-status`: explicit experimental service banner.
- `GET /verify/{record_id}`: safe record lookup plus normalized provenance payload.
- `GET /trust/{record_id}`: trust payload scaffold with provenance fields.
- `GET /history/{record_id}`: revision history scaffold with normalized state.
- `GET /witness/{witness_id}`: witness summary scaffold.
- `GET /federation/{record_id}`: federation source scaffold.

## Trust Limitations

Current responses are not sufficient for high-assurance verification decisions. They preserve the HC-TRUST-LAYER response shape while the verification runtime is under active implementation.

## Security Protections (Current)

- Safe path handling is enforced in the record loader by record ID validation and resolved-path checks.
- Replay-safe lookup behavior uses canonical directory order: `pending`, `verified`, then `archived`.
- Malformed request protection rejects invalid record IDs and malformed JSON files.
- Non-canonical artifact rejection excludes generated or unsupported artifacts (e.g., `.sha256`, signatures, and unknown file types).

## Future Federation Plans

Planned milestones include federated source ingestion, signed remote attestations, and consensus-weighted cross-node trust evidence.

## Local Development

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Local API

```bash
uvicorn src.api.main:app --reload
```

### Example Requests

```bash
curl -s http://127.0.0.1:8000/health
curl -s http://127.0.0.1:8000/version
curl -s http://127.0.0.1:8000/experimental-status
curl -s http://127.0.0.1:8000/verify/HC-EXAMPLE-2026-0001
curl -s http://127.0.0.1:8000/trust/HC-EXAMPLE-2026-0001
curl -s http://127.0.0.1:8000/history/HC-EXAMPLE-2026-0001
curl -s http://127.0.0.1:8000/witness/HC-WITNESS-2026-0001
curl -s http://127.0.0.1:8000/federation/HC-EXAMPLE-2026-0001
```
