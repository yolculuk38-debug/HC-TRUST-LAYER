// Execute the actual viewer script with a minimal DOM recorder. HTML parsing is
// checked independently by the Python test; this recorder does not sanitize it.
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const root = new URL('../../', import.meta.url);
const source = readFileSync(new URL('docs/verification-viewer.html', root), 'utf8');
const scripts = [...source.matchAll(/<script>([\s\S]*?)<\/script>/g)];
if (scripts.length !== 1) throw new Error('Expected the single viewer script');
const nodes = new Map();
class Element {
  constructor(tag = 'div') { this.tag = tag; this.children = []; this.text = ''; this.html = ''; this.disabled = false; this.selectedIndex = 0; }
  set innerHTML(value) { this.html = String(value); this.text = ''; this.children = []; }
  get innerHTML() { return this.html; }
  set textContent(value) { this.text = String(value); this.html = ''; this.children = []; }
  get textContent() { return this.text; }
  appendChild(child) { this.children.push(child); return child; }
  replaceChildren(...children) { this.children = children; this.html = ''; this.text = ''; }
  addEventListener() {}
  setAttribute() {}
  remove() {}
  click() {}
  snapshot() { return { tag: this.tag, html: this.html, text: this.text, children: this.children.map(c => c.snapshot()) }; }
}
const example = JSON.parse(readFileSync(new URL('examples/verification-packages/verified-trace-example.json', root), 'utf8'));
let copied;
const ctx = vm.createContext({
  document: { getElementById(id) { if (!nodes.has(id)) nodes.set(id, new Element()); return nodes.get(id); }, createElement: tag => new Element(tag) },
  window: { location: { hash: '#verified-trace', pathname: '/viewer', search: '' }, addEventListener() {} },
  history: { replaceState() {} },
  navigator: { clipboard: { async writeText(value) { copied = value; } } },
  fetch: async () => ({ ok: true, json: async () => structuredClone(example) }),
  setTimeout: () => 1, clearTimeout() {},
});
vm.runInContext(scripts[0][1], ctx, { filename: 'verification-viewer.html' });
await new Promise(setImmediate); // settle only the stubbed startup fetch
const marker = '<hc-text-probe data-note="a&b">quoted \'text\'</hc-text-probe>';
const pkg = structuredClone(example);
for (const field of ['package_id', 'trust_result', 'trust_confidence', 'content_hash', 'provenance_summary', 'generated_at']) pkg[field] = marker;
pkg.provenance_timeline = [{ stage: marker, actor: marker, timestamp: marker, status: marker }];
pkg.validator_reviews = [{ decision: marker, validator_id: marker, reviewed_at: marker, notes: marker }];
pkg.replay_indicators = [marker, { note: marker }];
pkg.dispute_indicators = [marker, { note: marker }];
pkg.audit_snapshot = { audit_trail_ref: marker, last_event: marker, review_boundary: marker };
const snapshot = () => nodes.get('content').snapshot();
const results = { marker, pkg, examples: [] };
ctx.renderPackage(pkg, marker);
results.package = snapshot();
await ctx.copyCurrentPackageJson();
results.copied = copied;
results.summary = ctx.buildReportSummaryText(pkg, ctx.getPackageWarnings(pkg));
await ctx.loadLocalFile({ name: marker + '.json', text: async () => JSON.stringify(example) });
results.local = snapshot();
ctx.fetch = async () => { throw new Error(marker); };
await ctx.loadSelected();
results.fetchError = snapshot();
results.fetchButtonsDisabled = nodes.get('copyPackageBtn').disabled;
await ctx.loadLocalFile({ name: 'invalid.json', text: async () => { throw new Error(marker); } });
results.fileError = snapshot();
await ctx.loadLocalFile({ name: 'invalid.json', text: async () => marker });
results.parseError = snapshot();
results.parseButtonsDisabled = nodes.get('copyPackageBtn').disabled;
for (const name of ['verified-trace', 'partial-trace', 'replay-warning', 'disputed', 'unverified']) {
  ctx.renderPackage(JSON.parse(readFileSync(new URL(`examples/verification-packages/${name}-example.json`, root), 'utf8')));
  results.examples.push(snapshot());
}
console.log(JSON.stringify(results));
