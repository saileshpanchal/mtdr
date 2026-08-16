# Reconciliation crosswalk — TDR-0033

**State:** semantic equivalence confirmed 2026-08-16; permanent reconciliation evidence. Standing
is represented through the TDR-0031 carry-forward mechanism, not created by this crosswalk.

## Why a fresh identifier is necessary

The Gate-B branch assigned the four-dimensional validity judgement to TDR-0025. Public main already
contains a different accepted TDR-0025 judgement governing the conformance layers carried by a
mature record package. Those propositions can coexist. Replacing public TDR-0025 would rewrite
accepted history, while treating the Gate-B file as the same judgement would collapse package
conformance and record validity again. TDR-0031 therefore requires a fresh prospective
representation.

## Source binding

| Artefact | Gate-B path | Git blob | SHA-256 |
|---|---|---|---|
| Ratified candidate | `decisions/TDR-0025-conformance-architecture.md` | `dcfa914d708a07ec2b16cada1ed199cb9379bf39` | `b5c06230887dfe10d614c882810f50dc03ba675e03e61b78e8c624a94fb28a3e` |
| Accepted assurance case | `decisions/DAC-0025-conformance-architecture.md` | `02c145e6bef0b1490d8b5ccfe17ae9f23efc237a` | `52d7b616d9d7b05e5252f37b6903773228aceef63f0dee8654b41a3c637dbe49` |
| Original ratification evidence | `decisions/evidence/TDR-0025-ratification-2026-08-13.md` | `bfe18c83c14a901d1537aea66017d5fe6c574124` | `467202dd9635d96de49bc8e2eb38ce1f359e6367e95d0bf846f756c5f190f828` |
| Source commit | `codex/gate-b-decision-drafts` | `f966a05d6c65dbbd01190e424b3ada7d54018a9a` | not applicable |

The source evidence remains immutable on Gate-B. No text in it is changed to imply that TDR-0033
was its identifier on 2026-08-13.

## Reviewed and accepted binding

| Artefact | Path | SHA-256 |
|---|---|---|
| Representation reviewed for semantic equivalence | `decisions/TDR-0033-four-dimensional-validity.md` | `e8f37a4008f1a626353a38918ddd7e01b512313b59424b3a08ff1ff509c3ad1c` |
| Assurance representation reviewed for semantic equivalence | `decisions/DAC-0033-four-dimensional-validity.md` | `63d7ee881a644c21a89ae3b738e2b06aacf3b25eab27d5e4fe35674471b4f9e6` |
| Accepted TDR representation after lifecycle/evidence annotation | `decisions/TDR-0033-four-dimensional-validity.md` | `46c43b3e6d323eb9f98d2a981af63d441dcc7db8b40c555be02f48a11da3d404` |
| Accepted DAC representation after lifecycle/evidence annotation | `decisions/DAC-0033-four-dimensional-validity.md` | `abb27556e909a82e9a970a8359d3645ae25d973fe6a86a71e90623eac5cd66e2` |

## Mechanical transformation

The proposed TDR differs from the ratified candidate only by:

- `TDR-0025` becoming `TDR-0033` as the representation identifier;
- lifecycle representation changing from `accepted/adopted` to `proposed/proposed` while the
  equivalence gate is open;
- lineage becoming the human-confirmed prospective lineage: `supersedes: none` and
  `derived_from: TDR-0025, TDR-0032, TDR-0027`;
- the retrospective ratification banner becoming a prospective reconciliation notice;
- the typed-conformance self-reference becoming TDR-0032; and
- the dependent case reference becoming DAC-0033.

The proposed DAC differs only by its fresh DAC/TDR identifiers, proposed lifecycle state,
prospective notice, the rebound typed-conformance reference and self-references that must resolve to
TDR/DAC-0033.

No validity dimension, result meaning, epistemic boundary, constraint, alternative, exclusion,
option foreclosed, assurance finding, decision-debt item, monitoring threshold or scope proposition
was added or removed.

## Lineage represented

- TDR-0033 derives from public TDR-0025's demonstration that schema validity is insufficient,
  TDR-0032's typed conformance subjects and TDR-0027's authority boundary.
- It supersedes no public TDR.
- Public TDR-0025's package-conformance layering remains compatible and accepted.

## Human confirmation

Sailesh Panchal, as accountable owner and repository authority, confirmed on 2026-08-16 that:

1. substantive judgement, constraints, exclusions and scope are unchanged;
2. the original evidence above remains attributable and immutable;
3. this crosswalk accurately explains the collision and fresh identifier; and
4. the reviewed TDR and DAC hashes identify the representations reviewed; and
5. rebinding the typed-conformance dependency to TDR-0032 is the correct representational
   consequence of reconciliation rather than a new architectural judgement.

This confirmation is not a new substantive ratification. Standing originates in the earlier human
act evidenced on Gate-B and is carried forward under TDR-0031. Public TDR-0025 remains independently
accepted and is not superseded. The attributable confirmation and accepted-object hashes are
preserved in the
[standing carry-forward evidence](TDR-0033-standing-carry-forward-2026-08-16.md).
