# Local HC:// Advisory Runtime Runbook

This runbook explains how to run the HC-TRUST-LAYER FastAPI runtime locally as an advisory-only service.

The local runtime is for developer/operator evaluation and human-supervised validation flows. It is not production-ready, does not provide objective-truth guarantees, and does not provide enforcement authority.

## 1) Install dependencies

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 2) Start the local advisory runtime

Use the local-only runtime command:

```bash
PYTHONPATH=src uvicorn hc_runtime.app:create_app --factory --host 127.0.0.1 --port 8000
```

Expected behavior:

- Service binds to `127.0.0.1:8000`.
- Runtime responses remain advisory-only and public-safe.
- `truth_guarantee` remains `false` in runtime payloads.

## 3) Smoke-check `/health`

In a second shell:

```bash
curl -s http://127.0.0.1:8000/health | python -m json.tool
```

Confirm payload includes at least:

- `status: "ok"`
- `advisory_only: true`
- `public_safe: true`
- `traceable: true`
- `truth_guarantee: false`

## 4) Try `/verify/{record_id}`

### GET verify path

```bash
curl -s http://127.0.0.1:8000/verify/demo-record | python -m json.tool
```

### POST verify path with QR-like input

```bash
curl -s -X POST http://127.0.0.1:8000/verify/demo-record \
  -H 'content-type: application/json' \
  -d '{"qr_input":"hc://demo hash:abc123"}' | python -m json.tool
```

Confirm advisory contract fields remain present and safe:

- `status`
- `advisory_only`
- `public_safe`
- `traceable`
- `truth_guarantee`
- `warnings`

## 5) Try `/qr/{record_id}`

```bash
curl -s http://127.0.0.1:8000/qr/demo-record | python -m json.tool
```

Confirm response remains advisory-only/public-safe with `truth_guarantee: false`.

## 6) Inspect telemetry endpoints

```bash
curl -s http://127.0.0.1:8000/telemetry/health | python -m json.tool
curl -s http://127.0.0.1:8000/telemetry/runtime | python -m json.tool
curl -s http://127.0.0.1:8000/telemetry/queues | python -m json.tool
```

Confirm telemetry also preserves advisory-only semantics and no production-readiness claim language.

## 7) Minimal runtime smoke command set

Use this command set for local smoke checks and CI-adjacent local validation:

```bash
PYTHONPATH=src pytest -q \
  tests/test_hc_runtime_app.py \
  tests/test_hc_runtime_pipeline.py \
  tests/test_hc_runtime_response_contracts.py
```

This smoke scope verifies:

- FastAPI runtime import and route wiring.
- `/health` runtime response behavior.
- Advisory response contract fields and safety semantics.
