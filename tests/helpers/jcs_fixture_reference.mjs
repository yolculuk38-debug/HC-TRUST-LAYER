// Test-only serializer for the checked-in valid JSON fixtures.
// Uses browser ECMAScript primitives; not an untrusted-input parser.
export function serializeFixture(value) {
  if (value === null || typeof value !== "object") {
    return JSON.stringify(value);
  }
  if (Array.isArray(value)) {
    return `[${value.map(serializeFixture).join(",")}]`;
  }
  // Emit entries directly: rebuilding an object would reorder integer keys.
  return `{${Object.keys(value).sort().map(
    key => `${JSON.stringify(key)}:${serializeFixture(value[key])}`
  ).join(",")}}`;
}

export async function checkFixture(vector) {
  const canonical = serializeFixture(JSON.parse(vector.input_json));
  const bytes = new TextEncoder().encode(canonical);
  const utf8Hex = Array.from(bytes, byte => byte.toString(16).padStart(2, "0")).join("");
  const digest = await globalThis.crypto.subtle.digest("SHA-256", bytes);
  const sha256 = Array.from(new Uint8Array(digest), byte => byte.toString(16).padStart(2, "0")).join("");
  if (canonical !== vector.canonical || utf8Hex !== vector.utf8_hex || sha256 !== vector.sha256) {
    throw new Error(`Canonicalization fixture mismatch: ${vector.id}`);
  }
}
