"""Exercise the real viewer JavaScript and independently parse its HTML output."""
import json
from html.parser import HTMLParser
from pathlib import Path
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]


class RenderedHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)

    def handle_data(self, data):
        self.text.append(data)


def parsed(node):
    parser = RenderedHTML()
    parser.feed(node['html'])
    texts = parser.text + [node['text']]
    tags = parser.tags
    for child in node['children']:
        child_tags, child_text = parsed(child)
        tags.extend([child['tag'], *child_tags])
        texts.append(child_text)
    return tags, ''.join(texts)


@pytest.fixture(scope='module')
def results():
    run = subprocess.run(['node', 'tests/helpers/verification_viewer_harness.mjs'],
                         cwd=ROOT, capture_output=True, text=True, check=True)
    return json.loads(run.stdout)


@pytest.mark.parametrize('surface', ['package', 'local', 'fetchError', 'fileError', 'parseError'])
def test_external_text_never_becomes_markup(results, surface):
    tags, text = parsed(results[surface])
    assert 'hc-text-probe' not in tags
    # Preserve readable data, including quotes and ampersands, without decoding
    # it into elements. JSON parser diagnostics may truncate to a short prefix.
    if surface != 'parseError':
        assert results['marker'] in text
    else:
        assert '<hc-text' in text
    if surface == 'package':
        assert results['marker'].upper() in text  # normalized result label too
        assert json.dumps(results['pkg'], ensure_ascii=False, indent=2) in text


def test_copy_and_plain_text_report_preserve_original_values(results):
    assert json.loads(results['copied']) == results['pkg']
    assert results['marker'] in results['summary']
    assert '&lt;hc-text' not in results['summary']


def test_errors_disable_package_actions(results):
    assert results['fetchButtonsDisabled'] is True
    assert results['parseButtonsDisabled'] is True
    assert 'Invalid Package' in parsed(results['parseError'])[1]


def test_all_five_bundled_examples_keep_report_sections(results):
    assert len(results['examples']) == 5
    for example in results['examples']:
        tags, text = parsed(example)
        assert 'article' in tags
        for label in ['Trust Result Card', 'Content Hash', 'Provenance Timeline', 'Raw Package Fields']:
            assert label in text
