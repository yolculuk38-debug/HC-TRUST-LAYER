# Verification API v1 Specification

## Overview
Read-only API for verification state, trust context, and historical evidence.

## Endpoint: `GET /verify/{record_id}`
Returns current verification result for a record.

Example response:
```json
{
  "record_id": "HC-TEST-2026-0001",
  "status": "verified",
  "verification": {
    "state": "verified",
    "validators": 3,
    "witnesses": 4,
    "last_updated": "2026-05-23T10:20:30Z"
  }
}
```

## Endpoint: `GET /history/{record_id}`
Returns append-only state and decision history.

Example response:
```json
{
  "record_id": "HC-TEST-2026-0001",
  "history": [
    {"state": "ingested", "timestamp": "2026-05-20T12:00:00Z"},
    {"state": "in_review", "timestamp": "2026-05-21T08:00:00Z"},
    {"state": "verified", "timestamp": "2026-05-22T15:30:00Z"}
  ]
}
```

## Endpoint: `GET /trust/{record_id}`
Returns trust score and component signals.

Example response:
```json
{
  "record_id": "HC-TEST-2026-0001",
  "trust": {
    "score": 0.91,
    "level": "high",
    "components": {
      "validator_quality": 0.94,
      "witness_consistency": 0.89,
      "risk_penalty": -0.05
    }
  }
}
```

## Endpoint: `GET /validator/{id}`
Returns validator profile and activity summary.

## Endpoint: `GET /witness/{id}`
Returns witness profile and attestation summary.

## Response States
- `unverified`
- `in_review`
- `verified`
- `disputed`
- `revoked`
- `quarantined`

## Verification Status Structure
```json
{
  "state": "verified",
  "reason": "consensus_threshold_met",
  "last_updated": "ISO-8601 timestamp",
  "evidence_refs": ["audit:event:..."],
  "revision": {"version": "1.2.0", "previous_hash": "..."}
}
```

## Trust Score Structure
```json
{
  "score": 0.0,
  "level": "low|medium|high",
  "components": {
    "validator_quality": 0.0,
    "witness_consistency": 0.0,
    "risk_penalty": 0.0
  },
  "computed_at": "ISO-8601 timestamp"
}
```
