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
dependencies = ["fastapi==0.138.1", "jsonschema==4.26.0", "qrcode[pil]==8.2"]
[project.optional-dependencies]
test = ["pytest==9.1.1; python_version >= '3.10'"]
''',
    )
    write(tmp_path / "requirements.txt", "jsonschema==4.26.0\nqrcode[pil]==8.2\nfastapi==0.138.1\npytest==9.1.1\n")
    write(tmp_path / ".github/workflows/validate.yml", "python-version: '3.14'\njava-version: '21'\nnode-version: '20'\ngo-version: '1.22'\n")
    return tmp_path


def test_python_current_baseline_parsing_from_pyproject_and_requirements(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)

    python = scanner.detect_python(repo, scanner.workflow_files(repo))

    assert python.current_observed["requires_python"] == ">=3.14"
    assert python.current_observed["pyproject_dependency_pins"] == {
        "fastapi": "0.138.1",
        "jsonschema": "4.26.0",
        "pytest": "9.1.1",
        "qrcode[pil]": "8.2",
    }
    assert python.current_observed["requirements_dependency_pins"] == {
        "fastapi": "0.138.1",
        "jsonschema": "4.26.0",
        "pytest": "9.1.1",
        "qrcode[pil]": "8.2",
    }


def test_workflow_version_parsing_from_sample_workflow_text(tmp_path: Path) -> None:
    repo = tmp_path
    write(repo / ".github/workflows/validate.yml", "python-version: '3.14'\npython-version: 3.x\npython-version: \"3.14\"\n")

    assert scanner.workflow_versions(scanner.workflow_files(repo), repo, "python-version") == {
        ".github/workflows/validate.yml": ["3.14", "3.x"]
    }


def test_python_quoted_declaration_forms_from_feedback(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(
        repo / "docs/python.md",
        "\n".join(
            [
                'python-version: "3.11"',
                "python-version: '3.11'",
                "python-version: 3.11",
                'python-version: "3.9"',
                "python-version: '3.9'",
                "python-version: 3.9",
                'requires-python = ">=3.11"',
                "requires-python = '>=3.11'",
                'requires-python = ">=3.9"',
                "requires-python = '>=3.9'",
            ]
        ),
    )

    report = scanner.build_report(repo)
    matches = report["missing_boundary_matches"]["python"]

    assert [match["matched_text"] for match in matches] == [
        'python-version: "3.11"',
        "python-version: '3.11'",
        "python-version: 3.11",
        'python-version: "3.9"',
        "python-version: '3.9'",
        "python-version: 3.9",
        'requires-python = ">=3.11"',
        "requires-python = '>=3.11'",
        'requires-python = ">=3.9"',
        "requires-python = '>=3.9'",
    ]


def test_python_historical_safe_classification_when_boundary_exists(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "docs/historical.md", "Historical/report-only boundary. Old value: Python 3.9.\n")

    report = scanner.build_report(repo)

    assert report["historical_safe_matches"]["python"][0]["classification"] == "historical_safe"
    assert report["missing_boundary_matches"] == {}


def test_python_missing_boundary_classification_when_boundary_absent(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "docs/missing.md", "Old value: pytest==9.0.3.\n")

    report = scanner.build_report(repo)

    assert report["missing_boundary_matches"]["python"][0]["classification"] == "missing_boundary"
    assert report["historical_safe_matches"] == {}


def test_java_baseline_and_stale_doc_detection(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / ".java-version", "21\n")
    write(repo / "pom.xml", "<project><properties><java.version>21</java.version></properties></project>\n")
    write(repo / "docs/java.md", 'java-version: "17"\nJava 17\n')

    report = scanner.build_report(repo)

    assert report["current_baseline"]["java"]["current_observed"]["java_version_file"] == "21"
    assert report["current_baseline"]["java"]["current_observed"]["pom_java_versions"] == ["21"]
    assert report["current_baseline"]["java"]["current_observed"]["workflow_java_versions"] == {
        ".github/workflows/validate.yml": ["21"]
    }
    assert [match["matched_text"] for match in report["missing_boundary_matches"]["java"]] == ['java-version: "17"', "Java 17"]


def test_node_baseline_and_stale_doc_detection(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / ".nvmrc", "20\n")
    write(repo / "package.json", '{"engines": {"node": ">=20"}}\n')
    write(repo / "docs/node.md", 'node-version: "18"\nNode 18\n')

    report = scanner.build_report(repo)

    assert report["current_baseline"]["node"]["current_observed"]["nvmrc"] == "20"
    assert report["current_baseline"]["node"]["current_observed"]["package_json_engines_node"] == ">=20"
    assert report["current_baseline"]["node"]["current_observed"]["workflow_node_versions"] == {
        ".github/workflows/validate.yml": ["20"]
    }
    assert [match["matched_text"] for match in report["missing_boundary_matches"]["node"]] == ['node-version: "18"', "Node 18"]


def test_go_baseline_and_stale_doc_detection(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "go.mod", "module example.test/hc\n\ngo 1.22\n")
    write(repo / "docs/go.md", "Go 1.21\n")

    report = scanner.build_report(repo)

    assert report["current_baseline"]["go"]["current_observed"]["go_mod_version"] == "1.22"
    assert report["missing_boundary_matches"]["go"][0]["matched_text"] == "Go 1.21"


def test_rust_baseline_and_stale_doc_detection(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "rust-toolchain.toml", 'channel = "1.76"\n')
    write(repo / "docs/rust.md", "Rust 1.75\n")

    report = scanner.build_report(repo)

    assert report["current_baseline"]["rust"]["current_observed"]["rust_toolchain_toml_channel"] == "1.76"
    assert report["missing_boundary_matches"]["rust"][0]["matched_text"] == "Rust 1.75"


def test_json_report_is_grouped_by_ecosystem(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)
    write(repo / "docs/missing.md", "Old value: Python 3.9.\n")

    report = scanner.build_report(repo)

    assert set(report["current_baseline"]) == {"python", "java", "node", "go", "rust"}
    assert report["baseline_model"] == "repository_declared_ecosystem_baselines"
    assert report["upstream_latest_version_check"] is False
    assert report["missing_boundary_matches"]["python"][0]["ecosystem"] == "python"


def test_markdown_output_shows_ecosystem_sections(tmp_path: Path) -> None:
    repo = make_repo(tmp_path)

    report = scanner.build_report(repo)
    markdown = scanner.markdown_report(report)

    assert "### python" in markdown
    assert "### java" in markdown
    assert "### node" in markdown
    assert "### go" in markdown
    assert "### rust" in markdown
    assert "does not fetch latest upstream versions" in markdown


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

    forbidden_tokens = ["requests", "urllib", "http.client", "socket", "subprocess", "write_text(", "open("]
    assert not any(token in source for token in forbidden_tokens)
