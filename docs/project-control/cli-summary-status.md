# CLI Summary Status

Status: completed local operator-output slice

Completed reference:

- #851 added optional summary output for the verification package CLI.

Current command:

```bash
hc-trust verify-package <package_path> --summary
```

Current behavior:

- default JSON output is unchanged;
- `--summary` prints a short operator-readable summary;
- summary includes status, verification state, package id, record id, checked file count, issuer proof status, human review flag, and advisory boundaries.

Do-not-repeat:

- do not repeat #851 unless new repository evidence appears.

Next safe action:

- update the quickstart so users can see both JSON output and summary output usage.
