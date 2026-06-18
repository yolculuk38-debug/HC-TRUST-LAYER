#!/usr/bin/env python3
"""Read-only GitHub metadata adapter for HC Check Digest workflow inputs.

This helper is intended for GitHub Actions workflow use. It collects or
normalizes GitHub-style metadata into local JSON files consumed by
``scripts/hc_check_digest.py``. It does not mutate PRs, reviews, labels,
assignees, checks, branches, or repository state.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Iterable
from pathlib import Path
from typing import Any

API_ROOT = "https://api.github.com"


def _items(payload: Any, key: str) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        value = payload.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
        return [payload]
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    return []


def normalize_check_runs(payload: Any) -> list[dict[str, Any]]:
    """Normalize GitHub check-run payloads for the local digest engine."""
    checks: list[dict[str, Any]] = []
    for check in _items(payload, "check_runs"):
        checks.append(
            {
                "name": check.get("name") or check.get("check_suite", {}).get("app", {}).get("name") or "GitHub check run",
                "status": check.get("status") or "unknown",
                "conclusion": check.get("conclusion") or "",
                "workflow": check.get("check_suite", {}).get("app", {}).get("name") or "",
                "url": check.get("html_url") or check.get("url") or "",
            }
        )
    return checks


def normalize_workflow_runs(payload: Any) -> list[dict[str, Any]]:
    """Normalize GitHub workflow-run payloads as additional check signals."""
    checks: list[dict[str, Any]] = []
    for run in _items(payload, "workflow_runs"):
        checks.append(
            {
                "name": run.get("name") or run.get("display_title") or "GitHub workflow run",
                "status": run.get("status") or "unknown",
                "conclusion": run.get("conclusion") or "",
                "workflow": run.get("path") or "",
                "url": run.get("html_url") or "",
            }
        )
    return checks


def normalize_reviews(payload: Any) -> list[dict[str, Any]]:
    """Normalize PR reviews and review comments as non-blocking external review input."""
    reviews: list[dict[str, Any]] = []
    raw_reviews: list[dict[str, Any]] = []
    if isinstance(payload, dict):
        for key in ("reviews", "comments"):
            value = payload.get(key)
            if isinstance(value, list):
                raw_reviews.extend(item for item in value if isinstance(item, dict))
    else:
        raw_reviews = _items(payload, "reviews")
    for review in raw_reviews:
        user = review.get("user") if isinstance(review.get("user"), dict) else {}
        body = review.get("body") or ""
        reviews.append(
            {
                "name": f"PR review by {user.get('login') or 'unknown reviewer'}",
                "author": user.get("login") or "unknown reviewer",
                "status": str(review.get("state") or "commented").lower(),
                "body": body,
                "title": body.splitlines()[0] if body else "PR review",
                "url": review.get("html_url") or "",
            }
        )
    return reviews


def normalize_review_threads(payload: Any) -> list[dict[str, Any]]:
    """Normalize true review-thread payloads when resolved/outdated state exists."""
    if not isinstance(payload, dict) or not isinstance(payload.get("threads"), list):
        return []
    raw_threads = [item for item in payload["threads"] if isinstance(item, dict)]
    threads: list[dict[str, Any]] = []
    for thread in raw_threads:
        user = thread.get("user") if isinstance(thread.get("user"), dict) else {}
        body = thread.get("body") or ""
        resolved = bool(thread.get("isResolved") or thread.get("resolved"))
        outdated = bool(thread.get("isOutdated") or thread.get("outdated"))
        if "position" in thread and thread.get("position") is None:
            outdated = True
        threads.append(
            {
                "name": body.splitlines()[0] if body else f"Review thread by {user.get('login') or 'unknown reviewer'}",
                "author": user.get("login") or "unknown reviewer",
                "status": "resolved" if resolved else "open",
                "resolved": resolved,
                "outdated": outdated,
                "body": body,
                "url": thread.get("html_url") or thread.get("url") or "",
            }
        )
    return threads


def normalize_artifacts(payload: Any) -> list[dict[str, Any]]:
    """Normalize workflow artifacts for digest input."""
    artifacts: list[dict[str, Any]] = []
    for artifact in _items(payload, "artifacts"):
        artifacts.append(
            {
                "name": artifact.get("name") or "GitHub workflow artifact",
                "status": "expired" if artifact.get("expired") else "available",
                "url": artifact.get("archive_download_url") or artifact.get("url") or "",
            }
        )
    return artifacts


def _read_json(path: str | None) -> Any:
    if not path:
        return []
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_inputs(output_dir: Path, checks: list[dict[str, Any]], reviews: list[dict[str, Any]], threads: list[dict[str, Any]], artifacts: list[dict[str, Any]]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, payload in {
        "checks.json": checks,
        "reviews.json": reviews,
        "threads.json": threads,
        "artifacts.json": artifacts,
    }.items():
        (output_dir / filename).write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _merge_page_payloads(payloads: Iterable[Any], key: str) -> dict[str, list[dict[str, Any]]]:
    items: list[dict[str, Any]] = []
    for payload in payloads:
        items.extend(_items(payload, key))
    return {key: items}


def _next_link(headers: Any) -> str | None:
    link_header = headers.get("Link") if headers else None
    if not link_header:
        return None
    for part in link_header.split(","):
        section = part.strip()
        if 'rel="next"' not in section:
            continue
        start = section.find("<")
        end = section.find(">", start + 1)
        if start != -1 and end != -1:
            return section[start + 1 : end]
    return None


def _github_get_pages(path: str, token: str, key: str) -> dict[str, list[dict[str, Any]]]:
    url = f"{API_ROOT}{path}"
    payloads: list[Any] = []
    while url:
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "hc-check-digest-read-only-adapter",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:  # nosec B310: fixed GitHub API root, read-only GET requests.
                payloads.append(json.loads(response.read().decode("utf-8")))
                url = _next_link(response.headers)
        except urllib.error.HTTPError as exc:
            if exc.code in {403, 404}:
                return {key: []}
            raise
    return _merge_page_payloads(payloads, key)


def _github_graphql(query: str, variables: dict[str, Any], token: str) -> Any:
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "hc-check-digest-read-only-adapter",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:  # nosec B310: fixed GitHub GraphQL endpoint, read-only query.
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 404}:
            return {}
        raise


def fetch_review_threads(repo: str, pr_number: str, token: str) -> dict[str, list[dict[str, Any]]]:
    owner, name = repo.split("/", 1)
    query = """
    query($owner: String!, $name: String!, $number: Int!, $after: String) {
      repository(owner: $owner, name: $name) {
        pullRequest(number: $number) {
          reviewThreads(first: 100, after: $after) {
            nodes {
              isResolved
              isOutdated
              comments(first: 1) {
                nodes {
                  body
                  url
                  author { login }
                }
              }
            }
            pageInfo {
              hasNextPage
              endCursor
            }
          }
        }
      }
    }
    """
    threads: list[dict[str, Any]] = []
    after: str | None = None
    while True:
        payload = _github_graphql(
            query,
            {"owner": owner, "name": name, "number": int(pr_number), "after": after},
            token,
        )
        review_threads = (
            payload.get("data", {})
            .get("repository", {})
            .get("pullRequest", {})
            .get("reviewThreads", {})
        )
        for node in review_threads.get("nodes", []) or []:
            comments = node.get("comments", {}).get("nodes", []) or []
            first_comment = comments[0] if comments else {}
            author = first_comment.get("author") if isinstance(first_comment.get("author"), dict) else {}
            threads.append(
                {
                    "body": first_comment.get("body") or "",
                    "url": first_comment.get("url") or "",
                    "user": {"login": author.get("login") or "unknown reviewer"},
                    "isResolved": bool(node.get("isResolved")),
                    "isOutdated": bool(node.get("isOutdated")),
                }
            )
        page_info = review_threads.get("pageInfo", {})
        if not page_info.get("hasNextPage"):
            break
        after = page_info.get("endCursor")
    return {"threads": threads}


def fetch_github_inputs(repo: str, pr_number: str, head_sha: str, token: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    encoded_sha = urllib.parse.quote(head_sha, safe="")
    checks_payload = _github_get_pages(f"/repos/{repo}/commits/{encoded_sha}/check-runs?per_page=100", token, "check_runs")
    runs_payload = _github_get_pages(f"/repos/{repo}/actions/runs?head_sha={encoded_sha}&per_page=100", token, "workflow_runs")
    reviews_payload = _github_get_pages(f"/repos/{repo}/pulls/{pr_number}/reviews?per_page=100", token, "reviews")
    comments_payload = _github_get_pages(f"/repos/{repo}/pulls/{pr_number}/comments?per_page=100", token, "comments")
    threads_payload = fetch_review_threads(repo, pr_number, token)
    artifacts_payload = _github_get_pages(f"/repos/{repo}/actions/artifacts?per_page=100", token, "artifacts")
    return (
        normalize_check_runs(checks_payload) + normalize_workflow_runs(runs_payload),
        normalize_reviews(reviews_payload) + normalize_reviews(comments_payload),
        normalize_review_threads(threads_payload),
        normalize_artifacts(artifacts_payload),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build local HC Check Digest inputs from read-only GitHub metadata.")
    parser.add_argument("--output-dir", default="hc-check-digest-inputs")
    parser.add_argument("--checks-json")
    parser.add_argument("--workflow-runs-json")
    parser.add_argument("--reviews-json")
    parser.add_argument("--threads-json")
    parser.add_argument("--artifacts-json")
    parser.add_argument("--fetch-github", action="store_true")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""))
    parser.add_argument("--pr-number", default=os.environ.get("PR_NUMBER", ""))
    parser.add_argument("--head-sha", default=os.environ.get("PR_HEAD_SHA", ""))
    args = parser.parse_args()

    if args.fetch_github:
        token = os.environ.get("GITHUB_TOKEN", "")
        if not token or not args.repo or not args.pr_number or not args.head_sha:
            raise SystemExit("GITHUB_TOKEN, repo, pr-number, and head-sha are required for --fetch-github")
        checks, reviews, threads, artifacts = fetch_github_inputs(args.repo, args.pr_number, args.head_sha, token)
    else:
        checks = normalize_check_runs(_read_json(args.checks_json)) + normalize_workflow_runs(_read_json(args.workflow_runs_json))
        reviews = normalize_reviews(_read_json(args.reviews_json))
        threads = normalize_review_threads(_read_json(args.threads_json))
        artifacts = normalize_artifacts(_read_json(args.artifacts_json))

    write_inputs(Path(args.output_dir), checks, reviews, threads, artifacts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
