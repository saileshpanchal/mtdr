# Tests

The cross-package test surface. Single-language fixtures live inside their package
(`records/<language>/fixtures/`); everything here is deliberately outside every package, because a
package may never depend sideways on another ([TDR-0021](../decisions/TDR-0021-record-package-architecture.md)).
What conformance means, and why schema validation is only its floor, is
[`specification/conformance.md`](../specification/conformance.md) ([TDR-0025](../decisions/TDR-0025-conformance-architecture.md)).

| Directory | Holds |
|---|---|
| [`conformance/`](conformance/) | Cross-language fixtures (FIX-002: one fragment, two objects) and the deployed-agent probes |
| [`corpus/`](corpus/) | The shared source corpus — fragment-level, multi-document, contradictory, incomplete, implicit and negative cases. Populated in the conformance-corpus pass |
| [`interoperability/`](interoperability/) | The horizon: independent implementations over one corpus, compared for semantic equivalence. Empty until there are two |
