# Reconciliation crosswalk — TDR-0032

**State:** semantic equivalence confirmed 2026-08-16; permanent reconciliation evidence. Standing
is represented through the TDR-0031 carry-forward mechanism, not created by this crosswalk.

## Why a fresh identifier is necessary

The Gate-B branch assigned the typed multi-object conformance judgement to TDR-0020. Public main
already contains a different accepted TDR-0020 judgement defining the repository's open,
consumer-neutral boundary. Replacing that file would rewrite accepted history; retaining both under
TDR-0020 would make identity context-dependent. TDR-0031 therefore requires a fresh prospective
representation.

## Source binding

| Artefact | Gate-B path | Git blob | SHA-256 |
|---|---|---|---|
| Ratified candidate | `decisions/TDR-0020-open-organisational-record-repository-boundary.md` | `05f46f22585ba03503426b8d0fd47a011cd61f18` | `687aab58e9ee2af26e10a3779b50c8e4de0dd013e063743aeb01513544271604` |
| Accepted assurance case | `decisions/DAC-0020-conformance-boundary.md` | `de359154b7e52041900d78d6fb8b4787609567ab` | `e02549d5d16b5ec1247a7f21fb40566db37d2ce5c107dc99b14b4a763b73474a` |
| Original ratification evidence | `decisions/evidence/TDR-0020-ratification-2026-08-13.md` | `c7fb68d3ba0080a67b542127bc4892d6e5e82b77` | `b35fe87267d8b127868f93948d07023d4de0ef620ce7b4cfd85548938bf690b2` |
| Source commit | `codex/gate-b-decision-drafts` | `f966a05d6c65dbbd01190e424b3ada7d54018a9a` | not applicable |

The source evidence remains immutable on Gate-B. No text in it is changed to imply that TDR-0032
was its identifier on 2026-08-13.

## Reviewed and accepted binding

| Artefact | Path | SHA-256 |
|---|---|---|
| Representation reviewed for semantic equivalence | `decisions/TDR-0032-typed-multi-object-conformance.md` | `624ce1dddd3b08c53cf4f431f2a5db4a0c8237b54c0bba4bd7787dd5ca8b454d` |
| Assurance representation reviewed for semantic equivalence | `decisions/DAC-0032-typed-multi-object-conformance.md` | `fe3c6aa3dbcd27d3c040482fa5a2222b52be5d6370049cb775302efefeb57ce1` |
| Accepted TDR representation after lifecycle/evidence annotation | `decisions/TDR-0032-typed-multi-object-conformance.md` | `775a6ae66b29b62c9014958cab05b24f83f33a962a618313a41a5c74b80f9f2b` |
| Accepted DAC representation after lifecycle/evidence annotation | `decisions/DAC-0032-typed-multi-object-conformance.md` | `6bc852e3e2fc01a84829840c0c10ed159b1ce3859582fd0043972abe3c58ab46` |

## Mechanical transformation

The proposed TDR differs from the ratified candidate only by:

- `TDR-0020` becoming `TDR-0032` as the representation identifier;
- lifecycle representation changing from `accepted/adopted` to `proposed/proposed` while the
  equivalence gate is open;
- lineage becoming the human-confirmed prospective lineage: `supersedes: TDR-0012` and
  `derived_from: TDR-0020, TDR-0027`;
- the retrospective ratification banner becoming a prospective reconciliation notice; and
- the dependent case reference becoming DAC-0032.

The proposed DAC differs only by its fresh DAC/TDR identifiers, proposed lifecycle state,
prospective notice and self-references that must resolve to TDR/DAC-0032.

No decision paragraph, constraint, alternative, exclusion, option foreclosed, assurance finding,
decision-debt item, monitoring threshold or scope proposition was added or removed.

## Lineage represented

- TDR-0032 derives from public TDR-0020's open repository boundary and TDR-0027's standing rule.
- It supersedes only TDR-0012's proposition that the register is the universal minimum of a
  complete conforming implementation.
- It retains TDR-0012's runtime neutrality, optional consumers and register-as-valid-pattern
  judgements.
- It does not supersede public TDR-0020.

## Human confirmation

Sailesh Panchal, as accountable owner and repository authority, confirmed on 2026-08-16 that:

1. substantive judgement, constraints, exclusions and scope are unchanged;
2. the original evidence above remains attributable and immutable;
3. this crosswalk accurately explains the collision and fresh identifier; and
4. the reviewed TDR and DAC hashes identify the representations reviewed; and
5. rebinding the collided identity and lineage is representational only.

This confirmation is not a new substantive ratification. Standing originates in the earlier human
act evidenced on Gate-B and is carried forward under TDR-0031. The attributable confirmation and
the accepted-object hashes are preserved in the
[standing carry-forward evidence](TDR-0032-standing-carry-forward-2026-08-16.md).
