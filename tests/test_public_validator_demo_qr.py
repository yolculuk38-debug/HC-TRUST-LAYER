from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import subprocess
import sys
from urllib.parse import parse_qs, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_public_validator_demo_qr.py"
QR_ASSET = ROOT / "docs" / "demo" / "public-validator-demo-qr.svg"
QR_ENTRY_DOC = ROOT / "docs" / "demo" / "public-validator-demo-qr-entry.md"
VIEWER = ROOT / "docs" / "demo" / "public-validator-static-viewer.html"
README = ROOT / "README.md"
START_HERE = ROOT / "docs" / "START_HERE.md"

spec = spec_from_file_location("generate_public_validator_demo_qr", GENERATOR)
assert spec is not None and spec.loader is not None
generator = module_from_spec(spec)
spec.loader.exec_module(generator)


def _svg_root() -> ET.Element:
    return ET.fromstring(QR_ASSET.read_text(encoding="utf-8"))


def _local_name(name: str) -> str:
    return name.rsplit("}", 1)[-1]


def test_committed_qr_matches_deterministic_generator() -> None:
    assert QR_ASSET.read_text(encoding="utf-8") == generator.generate_svg()

    completed = subprocess.run(
        [sys.executable, str(GENERATOR), "--check"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    assert "is current" in completed.stdout


def test_qr_target_is_the_official_record_id_result_route() -> None:
    root = _svg_root()
    target = root.attrib["data-target-url"]
    parsed = urlsplit(target)

    assert parsed.scheme == "https"
    assert parsed.netloc == "yolculuk38-debug.github.io"
    assert parsed.path == (
        "/HC-TRUST-LAYER/demo/public-validator-static-viewer.html"
    )
    assert parse_qs(parsed.query, strict_parsing=True) == {
        "record_id": ["HC-DEMO-PV-FIXTURE-FOOD-0001"]
    }
    assert parsed.fragment == "result-heading"
    assert root.attrib["data-record-id"] == "HC-DEMO-PV-FIXTURE-FOOD-0001"
    assert 'id="result-heading"' in VIEWER.read_text(encoding="utf-8")


def test_qr_svg_is_text_only_and_has_no_active_or_external_content() -> None:
    root = _svg_root()
    allowed_elements = {"svg", "title", "desc", "rect", "path"}

    for element in root.iter():
        assert _local_name(element.tag) in allowed_elements
        for attribute in element.attrib:
            local_attribute = _local_name(attribute).lower()
            assert not local_attribute.startswith("on")
            assert local_attribute not in {"href", "src"}

    assert root.attrib["data-advisory-only"] == "true"
    assert root.attrib["data-public-safe"] == "true"
    assert root.attrib["data-truth-guarantee"] == "false"
    assert root.attrib["data-human-review-required"] == "true"


def test_qr_entry_document_exposes_target_and_safety_boundary() -> None:
    document = QR_ENTRY_DOC.read_text(encoding="utf-8")

    assert generator.DEMO_TARGET_URL in document
    assert "public-validator-demo-qr.svg" in document
    assert "`advisory_only: true`" in document
    assert "`public_safe: true`" in document
    assert "`truth_guarantee: false`" in document
    assert "`human_review_required: true`" in document
    assert "does not prove QR authenticity" in document


def test_primary_navigation_exposes_the_current_qr_and_live_result() -> None:
    readme = README.read_text(encoding="utf-8")
    start_here = START_HERE.read_text(encoding="utf-8")

    assert "(docs/demo/public-validator-demo-qr-entry.md)" in readme
    assert "(demo/public-validator-demo-qr-entry.md)" in start_here
    assert generator.DEMO_TARGET_URL in readme
    assert generator.DEMO_TARGET_URL in start_here

    assert readme.index("docs/demo/public-validator-demo-qr-entry.md") < readme.index(
        "docs/demo/public-validator-static-viewer.html"
    )
    assert start_here.index("demo/public-validator-demo-qr-entry.md") < start_here.index(
        "demo/public-validator-static-viewer.html"
    )
