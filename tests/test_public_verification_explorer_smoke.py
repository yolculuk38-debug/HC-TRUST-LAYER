from pathlib import Path


EXPLORER_HTML = Path(__file__).resolve().parents[1] / "docs" / "explorer" / "index.html"


def _explorer_html() -> str:
    return EXPLORER_HTML.read_text(encoding="utf-8")


def test_public_verification_explorer_advisory_boundaries() -> None:
    html = _explorer_html()

    assert "Advisory-only notice:" in html
    assert "truth_guarantee=false" in html
    assert "human_final_authority=true" in html
    assert "read_only=true" in html
    assert "Generated explorer data is not a canonical record." in html
    assert "Advisory-only / non-canonical detail:" in html


def test_public_verification_explorer_filter_options_are_available() -> None:
    html = _explorer_html()

    for option in ("record_id", "hash_text"):
        assert f'<option value="{option}">' in html
        assert f'if (type === "{option}")' in html

    assert '<option value="all">record_id or content hash</option>' in html
    assert 'return filterValues(entry, "record_id")' in html
    assert '.concat(filterValues(entry, "hash_text"))' in html


def test_public_verification_explorer_exposes_verification_status_badge_logic() -> None:
    html = _explorer_html()

    assert 'function createStateBadges(entry)' in html
    assert 'addBadge(badges, "verification_status", entry.verification_status);' in html
    assert 'appendField(list, "verification_status", entry.verification_status);' in html
    assert 'badges.setAttribute("aria-label", "result state badges");' in html


def test_public_verification_explorer_keeps_generated_indexes_non_canonical() -> None:
    html = _explorer_html()

    assert '"../../generated/explorer_index.json"' in html
    assert '"../generated/explorer_index.json"' in html
    assert '"./explorer_index.json"' in html
    assert '"../../records/explorer_index.json"' in html
    assert 'addBadge(badges, "index", "non-canonical generated", { warning: true });' in html
    assert "Raw generated index entry preview" in html
    assert "generated explorer index entry" in html
    assert "non-canonical generated index details" in html


def test_public_verification_explorer_mvp_detail_sections_are_available() -> None:
    html = _explorer_html()

    for section in ("Record metadata", "Full record metadata", "Verification history", "Witness information", "Archive status"):
        assert section in html

    for field in ("timestamp", "content_hash", "witness_count", "source_path", "archive_status"):
        assert f'appendField(list, "{field}"' in html or f'["{field}"' in html


def test_public_verification_explorer_detail_renders_zero_witness_count() -> None:
    html = _explorer_html()

    assert 'function hasFieldValue(value)' in html
    assert 'return value !== "" && value !== null && value !== undefined;' in html
    assert 'displayLabel + ": " + valueText' in html
    assert '["witness_count", entry.witness_count]' in html
