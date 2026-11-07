# Tests

The cross-package test surface. Single-language fixtures live inside their package
(`records/<language>/fixtures/`); everything here is deliberately outside every package, because a
package may never depend sideways on another ([TDR-0021](../decisions/TDR-0021-record-package-architecture.md)).
What conformance means, and why schema validation is only its floor, is
[`specification/conformance.md`](../specification/conformance.md) ([TDR-0025](../decisions/TDR-0025-conformance-architecture.md)).

Run the repository's suite from the root of a clean clone. `uv` is the only prerequisite; it resolves
exactly what `uv.lock` pins:

```bash
uv run tests/verify.py
```

The same command runs on Linux and macOS on every push. That proves the suite is reproducible, not
that anyone outside this repository has validated anything.

| Directory | Holds |
|---|---|
| [`conformance/`](conformance/) | Cross-language fixtures (FIX-002: one fragment, two objects) and the deployed-agent probes |
| [`corpus/`](corpus/) | The shared source corpus — fragment-level, multi-document, contradictory, incomplete, implicit and negative cases. Populated in the conformance-corpus pass |
| [`validation/`](validation/) | Known-answer fixtures for the [validation-result contract](../specification/validation-result.md) — what a result may say, and the must-not probes for what it may never say |
| [`inspectability/`](inspectability/) | Known-answer fixtures for the [derivation projection](../specification/derivation-projection.md) — the five field states, and the must-not probes for rationale, scores, repair and conferred standing |
| [`recovery/`](recovery/) | Known-answer fixtures for the [historical candidate](../specification/historical-candidate.md) and its review events — what a retrospective candidate may claim, the digest that binds review to it, and the must-not probes for standing, dispositions and rationale. *Proposed under TDR-0048* |
| [`adoption/`](adoption/) | The acceptance case for applying MTDR to somebody else's framework — a fictional local authority, the expected reconstruction, and the progressive-disclosure budget |
| [`interoperability/`](interoperability/) | The horizon: independent implementations over one corpus, compared for semantic equivalence. Empty until there are two |
