# Corpus

The shared source corpus for interpretation testing: fictional organisational material at fragment
level — multi-document records, contradictory contributions, incomplete records, implicit
propositions, and negative cases where the correct output is nothing.

Populated at v1.17.0 per [TDR-0025](../../decisions/TDR-0025-conformance-architecture.md).
Everything here is fictional and marked as such, per [`CONTRIBUTING.md`](../../CONTRIBUTING.md).

| Case | Category | Proves |
|---|---|---|
| [CORPUS-001](CORPUS-001-decision-across-three-sources.md) | Multi-document | One decision from three sources; the email's date is not the decision date |
| [CORPUS-002](CORPUS-002-contradictory-contributions.md) | Contradiction | Incompatible values recorded as a conflict — never resolved by recency or source dignity |
| [CORPUS-003](CORPUS-003-implicit-decision.md) | Implicit proposition | A workaround that hardened into a commitment is found without decision language |
| [CORPUS-004](CORPUS-004-insufficient-evidence.md) | Incomplete | An admissible candidate with its gaps stated — neither completed nor refused |
| [CORPUS-005](CORPUS-005-nothing-here.md) | Negative | Material full of near-misses yields nothing, confidently |
| [CORPUS-006](CORPUS-006-complaint-challenging-a-decision.md) | Cross-language · standing | A complaint yields a decision reconstruction and a value commitment at once — and proves the standing gap rather than closing it |

Like every fixture in this standard, each case states **expected** and **must-not** results; a run
satisfying only the first has not passed. The single-language fixtures (FIX-001, FIX-003, FIX-004)
live in their packages; FIX-002 and these six are cross-language or record-neutral by design. The
governance fixtures (FIX-018 to FIX-031) are single-language and live in
[`records/decision/fixtures/governance/`](../../records/decision/fixtures/governance/); CORPUS-006 is
their cross-language sibling, and shares their estate.
