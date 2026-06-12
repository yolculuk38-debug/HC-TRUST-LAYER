# Quickstart Summary Status

Status: completed documentation slice

Completed reference:

- #853 documented `--summary` usage in the verification package CLI quickstart.

Current documented command:

```bash
hc-trust verify-package examples/verification-package/valid --summary
```

Current documented summary fields:

- package status;
- verification state;
- checked file count;
- issuer proof status;
- advisory-only boundary;
- public-safe boundary;
- truth guarantee boundary.

Do-not-repeat:

- do not repeat #851, #852, or #853 unless new repository evidence appears.

Next safe action:

- add or strengthen tests around summary output failure states before adding a new trust layer.
