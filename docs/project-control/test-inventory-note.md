# Test Inventory Note

Status: advisory checkpoint.

The reported `test_integration.py` filename does exist at the repository root.

Current reading shows it is a legacy integration script entry point that discovers repository record candidates, skips non-canonical JSON artifacts, validates applicable records against `schema/record-v1.schema.json`, checks hash formats, checks record status/type values, and includes an import-safety pytest guard.

This does not prove current coverage is complete. It only means the outside finding must be evaluated against the current root-level script and the broader `tests/` tree, not against the filename alone.

Confirmed search anchors also exist for verification package tests, runtime tests, telemetry tests, QR security tests, and bot/operator support tests.

Next safe action: inventory current `tests/` files and root-level integration scripts before changing test behavior.

Do not rewrite tests from an incomplete filename search alone.
