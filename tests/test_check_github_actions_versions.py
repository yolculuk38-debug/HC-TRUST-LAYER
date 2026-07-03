import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_github_actions_versions.py"
SPEC = importlib.util.spec_from_file_location("check_github_actions_versions", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
guard = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = guard
SPEC.loader.exec_module(guard)

CHECKOUT_V4 = "actions/checkout@" + "v4"
UPLOAD_ARTIFACT_V4 = "actions/upload-artifact@" + "v4"
DOWNLOAD_ARTIFACT_V4 = "actions/download-artifact@" + "v4"
SETUP_PYTHON_V5 = "actions/setup-python@" + "v5"
CHECKOUT_V4_PATCH = "actions/checkout@" + "v4.0.0"
UPLOAD_ARTIFACT_V4_PATCH = "actions/upload-artifact@" + "v4.0.0"
SETUP_PYTHON_V4_PATCH = "actions/setup-python@" + "v4.9.1"


def _write_workflow(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def test_detects_exact_deprecated_action_refs(tmp_path: Path) -> None:
    workflows = tmp_path / "workflows"
    _write_workflow(
        workflows / "deprecated.yml",
        """
name: Deprecated
jobs:
  check:
    steps:
      - uses: {CHECKOUT_V4}
      - uses: {UPLOAD_ARTIFACT_V4}
      - uses: {DOWNLOAD_ARTIFACT_V4}
      - uses: {SETUP_PYTHON_V5}
      - uses: actions/attest-build-provenance@v4
      - uses: github/codeql-action/analyze@v3
""".format(
            CHECKOUT_V4=CHECKOUT_V4,
            UPLOAD_ARTIFACT_V4=UPLOAD_ARTIFACT_V4,
            DOWNLOAD_ARTIFACT_V4=DOWNLOAD_ARTIFACT_V4,
            SETUP_PYTHON_V5=SETUP_PYTHON_V5,
        ),
    )

    findings = guard.scan_workflows(workflows)

    assert [finding.reference for finding in findings] == [
        CHECKOUT_V4,
        UPLOAD_ARTIFACT_V4,
        DOWNLOAD_ARTIFACT_V4,
        SETUP_PYTHON_V5,
        "actions/attest-build-provenance@v4",
        "github/codeql-action/analyze@v3",
    ]
    assert guard.main(["--workflows-dir", str(workflows)]) == 1


def test_detects_patch_pinned_deprecated_major_refs(tmp_path: Path) -> None:
    workflows = tmp_path / "workflows"
    _write_workflow(
        workflows / "patch-pinned.yml",
        """
name: Patch pinned
jobs:
  check:
    steps:
      - uses: {CHECKOUT_V4_PATCH}
      - uses: actions/checkout@v6.1.2
      - uses: {UPLOAD_ARTIFACT_V4_PATCH}
      - uses: actions/upload-artifact@v6.2.3
      - uses: actions/download-artifact@v7.0.0
      - uses: {SETUP_PYTHON_V4_PATCH}
      - uses: actions/attest-build-provenance@v4.0.0
      - uses: github/codeql-action/init@v3.28.1
      - uses: github/codeql-action/upload-sarif@v3.28.1
""".format(
            CHECKOUT_V4_PATCH=CHECKOUT_V4_PATCH,
            UPLOAD_ARTIFACT_V4_PATCH=UPLOAD_ARTIFACT_V4_PATCH,
            SETUP_PYTHON_V4_PATCH=SETUP_PYTHON_V4_PATCH,
        ),
    )

    findings = guard.scan_workflows(workflows)

    assert [finding.reference for finding in findings] == [
        CHECKOUT_V4_PATCH,
        "actions/checkout@v6.1.2",
        UPLOAD_ARTIFACT_V4_PATCH,
        "actions/upload-artifact@v6.2.3",
        "actions/download-artifact@v7.0.0",
        SETUP_PYTHON_V4_PATCH,
        "actions/attest-build-provenance@v4.0.0",
        "github/codeql-action/init@v3.28.1",
        "github/codeql-action/upload-sarif@v3.28.1",
    ]
    assert {finding.replacement for finding in findings} == {
        "actions/checkout@v7",
        "actions/upload-artifact@v7",
        "actions/download-artifact@v8",
        "actions/setup-python@v6",
        "actions/attest-build-provenance@v4.1.1",
        "github/codeql-action/init@v4",
        "github/codeql-action/upload-sarif@v4",
    }


def test_allows_upgraded_action_refs(tmp_path: Path) -> None:
    workflows = tmp_path / "workflows"
    _write_workflow(
        workflows / "allowed.yaml",
        """
name: Allowed
jobs:
  check:
    steps:
      - uses: actions/checkout@v7
      - uses: actions/checkout@v7.0.0
      - uses: actions/upload-artifact@v7
      - uses: actions/upload-artifact@v7.2.3
      - uses: actions/download-artifact@v8
      - uses: actions/download-artifact@v8.0.0
      - uses: actions/setup-python@v6
      - uses: actions/setup-python@v6.1.0
      - uses: actions/attest-build-provenance@v4.1.1
      - uses: github/codeql-action/init@v4
      - uses: github/codeql-action/analyze@v4
      - uses: github/codeql-action/upload-sarif@v4
""",
    )

    assert guard.scan_workflows(workflows) == []
    assert guard.main(["--workflows-dir", str(workflows)]) == 0


def test_ignores_unrelated_action_refs_unless_explicitly_denylisted(tmp_path: Path) -> None:
    workflows = tmp_path / "workflows"
    _write_workflow(
        workflows / "unrelated.yml",
        """
name: Unrelated
jobs:
  check:
    steps:
      - uses: ossf/scorecard-action@v2.4.3
      - uses: local/action@v4.1.0
""",
    )

    assert guard.scan_workflows(workflows) == []


def test_guard_is_local_and_network_free() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    for network_marker in ("urllib", "requests", "http.client", "socket", "urlopen"):
        assert network_marker not in source
