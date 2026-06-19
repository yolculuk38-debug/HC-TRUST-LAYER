import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_github_actions_versions.py"
SPEC = importlib.util.spec_from_file_location("check_github_actions_versions", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
guard = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = guard
SPEC.loader.exec_module(guard)


def _write_workflow(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def test_detects_deprecated_action_refs(tmp_path: Path) -> None:
    workflows = tmp_path / "workflows"
    _write_workflow(
        workflows / "deprecated.yml",
        """
name: Deprecated
jobs:
  check:
    steps:
      - uses: actions/checkout@v4
      - uses: actions/upload-artifact@v4
""",
    )

    findings = guard.scan_workflows(workflows)

    assert [finding.reference for finding in findings] == [
        "actions/checkout@v4",
        "actions/upload-artifact@v4",
    ]
    assert guard.main(["--workflows-dir", str(workflows)]) == 1


def test_allows_upgraded_action_refs(tmp_path: Path) -> None:
    workflows = tmp_path / "workflows"
    _write_workflow(
        workflows / "allowed.yaml",
        """
name: Allowed
jobs:
  check:
    steps:
      - uses: actions/checkout@v6
      - uses: actions/upload-artifact@v7
""",
    )

    assert guard.scan_workflows(workflows) == []
    assert guard.main(["--workflows-dir", str(workflows)]) == 0


def test_guard_is_local_and_network_free() -> None:
    source = SCRIPT.read_text(encoding="utf-8")

    for network_marker in ("urllib", "requests", "http.client", "socket", "urlopen"):
        assert network_marker not in source
