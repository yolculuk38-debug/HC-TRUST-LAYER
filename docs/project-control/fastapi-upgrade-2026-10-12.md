# FastAPI 0.142.2 upgrade boundary

## Scope before compatibility implementation

Dependabot #1249 changes only the FastAPI pins from 0.141.1 to 0.142.2.
Upstream 0.142.0 introduced native OpenTelemetry with tracing, metrics, logs,
operation spans and environment exporter configuration enabled by default.
Upstream documentation says global providers can be reused and exception logs
can contain exception messages and stack traces. The existing HC app does not
configure this newly introduced behavior.

Preserve the reference runtime's local advisory boundary during this upgrade:
explicitly disable FastAPI native tracing, metrics, logs, operation spans and
automatic exporter configuration in `hc_runtime.app.create_app`. This does not
change HC's existing local `/telemetry/*` response contract or control telemetry
explicitly installed by an embedding application, server or external agent.

Validation must exercise app startup and successful, invalid and failing
requests while provider/exporter probes are installed. A control app with
FastAPI defaults must activate those probes, making the negative result
meaningful. Run the complete suite with the actual updated pinned dependency,
then current-head CI, installed wheel smoke and matching Codex review.

Primary evidence: FastAPI upstream PR 16403, its OpenTelemetry documentation
and installed 0.142.2 source. Release 0.142.1 fixes repeated router wrapping;
0.142.2 allows startup when automatic telemetry configuration fails. No claim
of broader operational security or production readiness follows from this fix.

## Local validation

On the actual #1248 merge `31035c5c9a8996d2ecbf1ea48e6aaaebe3b137eb`, a fresh
CPython 3.14.7 environment installed FastAPI 0.142.2 and the repository's pinned
dependencies. Both telemetry control cases passed, followed by all 1342 tests;
one upstream Starlette TestClient warning remains. The probes observe global
provider lookup and environment endpoint discovery without network export.
Startup, successful requests, validation errors and unhandled errors are covered.
The existing `tests/runtime` CI invocation includes this regression automatically.
