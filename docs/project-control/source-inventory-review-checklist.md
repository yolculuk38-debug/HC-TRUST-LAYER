# Source Inventory Review Checklist

Status: advisory checklist.

Use this checklist after running the non-mutating source inventory reporter:

```bash
python scripts/hc_source_inventory.py .
```

The reporter is inventory-only. It does not write, delete, move, call the network, call an LLM, change workflows, or change authority.

## Review order

1. Keep active anchors first.
2. Mark source files with direct tests as active or reviewable, not cleanup by default.
3. Mark files without tests as review-needed, not deletion candidates.
4. Mark experimental or archive-classified files for manual review.
5. Do not touch protected paths.
6. Do not delete, move, or archive anything from file name alone.

## Evidence to collect before cleanup

For each source file, collect:

- inventory category;
- import or reference evidence;
- matching test evidence;
- docs or quickstart references;
- whether it touches protected-path or trust-kernel-adjacent behavior;
- last known PR or status note if available.

## Cleanup gate

A cleanup PR may be proposed only after the file has all of the following:

- no active import/reference evidence;
- no direct test anchor;
- no current documentation anchor;
- no protected-path relationship;
- a human-reviewed reason for removal, move, or archive.

Until those conditions are met, keep the file and record the review status.
