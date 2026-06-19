#!/usr/bin/env python3
"""Render the advisory HC Check Digest job-summary wrapper for local snapshots."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hc_check_digest import render_markdown

SUMMARY_PREAMBLE = (
    "# HC Check Digest v2\n"
    "\n"
    "HC Check Digest is advisory-only.\n"
    "It does not approve, reject, label, assign, comment, or merge.\n"
    "Humans retain final authority.\n"
    "\n"
)


def render_job_summary(digest: dict) -> str:
    """Render the same advisory wrapper the workflow appends to GITHUB_STEP_SUMMARY."""
    return SUMMARY_PREAMBLE + render_markdown(digest)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a local HC Check Digest job-summary snapshot.")
    parser.add_argument("digest_json", help="Path to hc-check-digest JSON output.")
    args = parser.parse_args()

    with Path(args.digest_json).open("r", encoding="utf-8") as handle:
        digest = json.load(handle)
    print(render_job_summary(digest), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
