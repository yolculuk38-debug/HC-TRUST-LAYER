from __future__ import annotations

import io
from contextlib import redirect_stdout
from pathlib import Path

import scripts.hc_stale_baseline_report as scanner


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_repo(tmp_path: Path) -> Path:
    write(
        tmp_path / "pyproject.toml",
        '''[project]
requires-python = ">=3.14"
dependencies = [
  "fastapi==0.138.1",
  "jsonschema==4.26.0",
  "qrcode[pil]==8.2",
]
[project.optional-dependencies]
test = ["pytest==9.1.1; python_version >= '3.10'"]
''',
    )
    write(tmp_path / "requirements.txt", "jsonschema==4.26.0\nqrcode[pil]==8.2\nfastapi==0.138.1\npytest==9.1.1\n")
    write(
        tmp_path / ".github/workflows/validate.yml",
        "jobs:\n  test:\n    steps:\n      - uses: actions/setup-python@v6\n        with:\n          python-version: '3.14'\n",
    )
    return tmp_path


def test_current_baseline_parsing_from_pyproject() -> None:
    text = 'requires-python = ">=3.14"\ndependencies = ["fastapi==0.138.1", "pytest==9.1.1; python_version >= \'3.10\'"]\n'

    assert scanner.parse_requires_python(text) == ">=3.14"
    assert scanner.parse_dependency_pins(text) == {"fastapi": "0.138.1", "pytest": "9.1.1"}


def test_requirements_parsing_from_sample_requirements() -> None:
    text = "jsonschema==4.26.0\nqrcode[pil]==8.2\nfastapi==0.138.1\n"

    assert scanner.parse_dependency_pins(text) == {
        "fastapi": "0.138.1",
        "jsonschema": "4.26.0",
        "qrcode[pil]": "8.2",
    }


def test_workflow_python_version_parsing_from_sample_workflow_text() -> None:
    text = "python-version: '3.14'\npython-version: 3.x\npython-version: \"3.14\"\n"

    assert scanner.parse_workflow_python_versions(text) == ["3.14", "3.x"]


def test_stale_reference_detection(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    doc = repo / "docs/example.md"
    write(doc, "This mentions Python 3.9 and pytest==9.0.3.\n")

    matches = scanner.find_stale_matches(doc, doc.read_text(encoding="utf-8"), repo)

    assert {match["match"] for match in matches} == {"Python 3.9", "pytest==9.0.3"}


def test_historical_safe_detection_when_boundary_exists(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "docs/historical.md", "Historical/report-only boundary. Old value: Python 3.9.\n")

    report = scanner.build_report(repo)

    assert [item["file"] for item in report["historical_safe_matches"]] == ["docs/historical.md"]
    assert report["missing_boundary_matches"] == []


def test_missing_boundary_detection_when_boundary_absent(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "docs/missing.md", "Old value: requires-python = \">=3.9\".\n")

    report = scanner.build_report(repo)

    assert report["historical_safe_matches"] == []
    assert [item["file"] for item in report["missing_boundary_matches"]] == ["docs/missing.md"]


def test_default_report_only_exit_behavior(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "docs/missing.md", "Old value: uvicorn==0.35.0.\n")

    stdout = io.StringIO()
    with redirect_stdout(stdout):
        exit_code = scanner.main(["--repo-root", str(repo)])

    assert exit_code == 0
    assert '"advisory_only": true' in stdout.getvalue()
    assert '"truth_guarantee": false' in stdout.getvalue()


def test_optional_fail_on_missing_boundary_behavior(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "docs/missing.md", "Old value: fastapi==0.115.14.\n")

    stdout = io.StringIO()
    with redirect_stdout(stdout):
        exit_code = scanner.main(["--repo-root", str(repo), "--fail-on-missing-boundary"])

    assert exit_code == 1


def test_no_network_or_write_behavior_by_construction() -> None:
    source = Path(scanner.__file__).read_text(encoding="utf-8")

    forbidden_tokens = ["requests", "urllib", "http.client", "socket", "subprocess", "write_text(", "open(", "GitHub"]
    assert not any(token in source for token in forbidden_tokens)
