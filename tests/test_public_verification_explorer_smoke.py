from pathlib import Path


EXPLORER_HTML = Path(__file__).resolve().parents[1] / "docs" / "explorer" / "index.html"


def _explorer_html() -> str:
    return EXPLORER_HTML.read_text(encoding="utf-8")


def test_public_verification_explorer_advisory_boundaries() -> None:
    html = _explorer_html()

    assert "Advisory-only notice:" in html
    assert "truth_guarantee=false" in html
    assert "human_final_authority=true" in html
    assert "Generated explorer data is not a canonical record." in html
    assert "Advisory-only / non-canonical detail:" in html


def test_public_verification_explorer_filter_options_are_available() -> None:
    html = _explorer_html()

    for option in ("record_id", "status_trust_state", "source_path", "hash_text"):
        assert f'<option value="{option}">' in html
        assert f'if (type === "{option}")' in html

    assert 'return filterValues(entry, "record_id")' in html
    assert '.concat(filterValues(entry, "status_trust_state"))' in html
    assert '.concat(filterValues(entry, "source_path"))' in html
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
