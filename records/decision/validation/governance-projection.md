# Governance projection — the output contract

**Status:** proposed under [TDR-0034](../../../decisions/TDR-0034-governance-reconstruction-and-forum-evolution.md).
Not accepted, and carrying no standing.

What the governance skills emit, and what each field means. The machine-readable form is
[`governance-projection.schema.json`](../schema/governance-projection.schema.json).

## What a projection is, and is not

A projection carries **interpretation about organisational meaning**, never organisational meaning
itself. It fails question 1 of the [record admission test](../../../specification/record-admission-test.md)
by design, which is that test's own answer to anything proposed for persistence on this basis. So:

- it is **not a record**, and no route exists by which it becomes one;
- it is **not a fourth interchange structure**. `SourceFragment`, `RecordContribution` and
  `CandidateAssembly` are ratified architecture
  ([TDR-0022](../../../decisions/TDR-0022-fragment-contribution-interchange-architecture.md)) and are
  unamended. A projection sits *downstream* of them;
- it **carries no standing**, structurally. `carries_standing` is `const: false`, because a field a
  skill can set to `true` is not a boundary.

`SourceClaim` has no projection shape. It is a
[`RecordContribution`](../../../schemas/shared/record-contribution.schema.json), and a second
representation of it would be the duplication
[TDR-0023](../../../decisions/TDR-0023-portable-skill-architecture.md) names as a defect.

## Epistemic state is assessed per claim

One state for a whole document, source or projection is the failure this contract exists to prevent.
A single forum reconstruction routinely holds all five at once:

```
stated purpose                  RECORDED
actual evidence-assembly job    OBSERVED
de-facto approval authority     INFERRED
waiver authority                UNKNOWN
accountable owner               CONTRADICTORY
```

Reported as one state, that forum is either "mostly recorded" or "contradictory", and both readings
are false. So every assessed claim gets its own entry in `epistemic_assessments[]`, and payload fields
carrying a `claim_ref` resolve to one of them.

Expected cardinality: a **finding** normally carries one; a **forum reconstruction** carries one per
job and one per separated power; a **demonstrability result** carries **one per material answer**.

### The five states, defined for this pack

| State | Means |
|---|---|
| `RECORDED` | Supported by organisational state the supplied evidence shows was **formally admitted or authoritative for the relevant time** |
| `OBSERVED` | Directly evidenced behaviour, artefact or event — **without asserting that it had authoritative standing** |
| `INFERRED` | Reconstructed from evidence, but not directly established |
| `UNKNOWN` | Insufficient evidence to support a claim |
| `CONTRADICTORY` | Materially incompatible evidence remains unresolved |

The `RECORDED`/`OBSERVED` boundary is the one most often drawn wrongly and the most consequential.
A decision plainly minuted in a pack is `OBSERVED` — the pack evidences that it happened. It is
`RECORDED` only where the evidence also shows the decision was admitted as authoritative state at the
time. **That a thing occurred is not evidence that it was authorised**, and collapsing the two is how
a reconstruction quietly launders de-facto practice into governance.

### Orthogonal to the substrate, and not mappable onto it

Three questions, three answers, none derivable from the others:

| Question | Answered by | Lives on |
|---|---|---|
| How was this produced? | `derivation: explicit \| inferred` | `RecordContribution` |
| How strong is it? | extraction / assembly / epistemic confidence | [`uncertainty.md`](../../../specification/uncertainty.md) |
| What standing does the projected claim have? | `epistemic_state` | this contract, and nowhere else yet |

**`RECORDED` is not `explicit`.** An explicit statement in a meeting pack can be an observation about
governance without ever having been admitted organisational state. **An `INFERRED` claim may carry
high `epistemic_confidence` and remain `INFERRED`** — strength of evidence is not standing.

A skill must not compute one from the others, present them as the same axis, or extend the substrate
to carry this. Whether these classes should become record-neutral across every MTDR language is a
constitutional question with its own compatibility analysis, recorded as an irreducibility finding in
TDR-0034 and reserved for its own decision.

### `assessment_as_of` is not `produced_at`

`produced_at` is when the output was generated. `assessment_as_of` is the date **as of which** the
claim was assessed. A demonstrability drill reconstructing February's state in August has one
`produced_at` in August and every `assessment_as_of` in February. Conflating them destroys the
historical boundary the drill exists to hold.

### Provenance is conditional on state

| State | What provenance is required |
|---|---|
| `RECORDED` · `OBSERVED` · `INFERRED` | At least one `basis_refs` entry. A positive claim with nothing behind it is an invention |
| `CONTRADICTORY` | At least two `contradiction_refs` entries — a contradiction needs both sides on the record |
| `UNKNOWN` | **Zero `basis_refs` is legitimate.** `question_asked` and `scope_searched` are required instead |

Requiring provenance unconditionally would force a skill to **manufacture a contribution in order to
report that provenance cannot be found** — turning a rule against fabricated provenance into a
requirement for it. An `UNKNOWN` that cannot say what question it asked and what it searched is an
untested absence rather than a finding, which is why those two fields become mandatory exactly where
`basis_refs` becomes optional.

## Known types are strict; extension stays open

Six known `projection_type` values validate against their own payload and nothing else:
`governance-finding` · `governance-disposition` · `forum-reconstruction` ·
`forum-evolution-projection` · `demonstrability-result` · `accretion-step`.

Anything else takes `extensionPayload`, which requires an `extension_note` saying what the projection
carries and which known type was considered and rejected. **Adding a projection type must never
require a change to the organisational record model** — and a recurring extension note is evidence for
a superseding decision, not a licence for a private convention. This is the `unclassified` discipline
[TDR-0026](../../../decisions/TDR-0026-value-recovery-vocabulary.md) established for value
contribution classes, applied to projection types.

`finding_type` carries the same shape: fourteen classes plus `UNCLASSIFIED`, which requires a note
stating what was recognised and why no class fitted. A near-fit is the failure under test, not the
workaround.

## Separated powers

`forum-reconstruction` reconstructs seven powers separately, each with its own claim and assessment:

```
execution authority
suspension / containment authority
challenge authority
veto / waiver / override authority
amendment authority
escalation route
accountability terminus
```

An unresolved power stays `UNKNOWN`. It never defaults to the adjacent holder, and never to the forum
itself. `accountability_terminus` terminates in an **accountable individual** — the rule
[`semantic-roles.md`](semantic-roles.md) already states for records ("a contribution proposing a
committee is a contribution to `context`, and the owner is reported as missing"), applied to
projections.

`independence_assessment` records seven dimensions — reporting, incentives, authority, evidence
source, cognition or model source, orchestration, and whether the governed owner can suppress or
configure the challenger — before reaching a conclusion. **Multiplicity is not independence**: that a
separate committee exists, under a different name, with its own reporting line, establishes none of it.

## What a reader may not conclude

- That a projection states organisational fact, or that its subject exists as the projection describes.
- That `INFERRED` authority is authority, or that observed exercise of a power proves entitlement to it.
- That an unlocatable source makes a mechanism optional.
- That `RETIRE_CANDIDATE` is a decision, or that any disposition is executable.
- That `required_authority` has been obtained because it has been named.
