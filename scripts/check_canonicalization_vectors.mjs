// Independent ECMAScript/Web Crypto execution of the shared golden corpus.
import {readFile} from "node:fs/promises";
import {checkFixture} from "../tests/helpers/jcs_fixture_reference.mjs";

const corpus = JSON.parse(await readFile(
  new URL("../tests/fixtures/canonicalization/golden-v1.json", import.meta.url), "utf8"
));
if (corpus.profile !== "rfc8785-jcs-v1" || corpus.vectors.length === 0) {
  throw new Error("Missing or unsupported canonicalization corpus");
}
for (const vector of corpus.vectors) await checkFixture(vector);
console.log(`ECMAScript/Web Crypto: ${corpus.vectors.length} canonical byte and SHA-256 vectors passed`);
