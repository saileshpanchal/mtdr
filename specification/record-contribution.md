# RecordContribution

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** Normative for skill interchange. Not a record specification.

An interpretation: *this evidence may contribute this semantic value to this organisational object.*
The first structure in which a skill commits to a reading, and therefore the first that can be wrong.

## The one rule

**Every contribution references at least one SourceFragment, and its interpreted value must be
supported by the referenced spans.** A contribution with no fragment behind it is an invention. This
is the rule that makes interpretation falsifiable: a reader can go to the span and disagree.

## Contribution is many-to-many

One fragment may contribute to several objects. Take:

> "The Committee approved the investment subject to maintaining complaints below 4%."

That single span yields contributions to:

- a **consequential decision** — the approval itself, and the constraint as a condition on it
- an **OVC** — a commitment whose review boundary is the 4% complaints threshold
- a **constraint relation** between the two

Equally, one object draws contributions from many fragments — the ordinary case for a value
commitment, whose proposition, beneficiary, baseline, measure, owner and revised target routinely sit
in different documents written months apart.

Neither direction is one-to-one. A `record_type_hint` carried on the fragment would have forced it to
be, and would have lost the second and third readings of the sentence above.

## Fields

| Field | Required | Meaning |
|---|---|---|
| `contribution_id` | Yes | Stable identifier |
| `fragment_refs` | Yes | One or more `fragment_id` values. At least one |
| `target_object` | Yes | The organisational object being reconstructed — `consequential-decision`, `ovc`, or an object supplied by a later record package |
| `target_record_type` | Yes | The record type that would preserve that object — `TDR`, `VR` |
| `semantic_role` | Yes | The role within the object. **Defined by the record package**, not here |
| `interpreted_value` | Yes | What the skill reads the evidence as saying for that role |
| `interpreter` | Yes | Name and version of whatever produced this reading |
| `interpreted_at` | Yes | When the reading was made |
| `extraction_confidence` | Yes | Did I read these words correctly? |
| `epistemic_confidence` | Yes | How strong is the underlying evidence for the claim? |
| `derivation` | No | `explicit` — read directly from the referenced span(s) — or `inferred` — derived across spans or from context. Optional and additive ([TDR-0026](../decisions/TDR-0026-value-recovery-vocabulary.md)); reported alongside completeness, never folded into it |

The two confidences are different facts and must never be merged — see
[`uncertainty.md`](uncertainty.md).

`target_object` and `target_record_type` are both required, and both carried, because the object is
what is being reconstructed while the record is how it would be preserved. Recording only the record
type would make the structure unable to express a contribution to an object whose record status is
still unsettled.

## What it never holds

- **No authority.** A contribution proposes a reading. It cannot make one true.
- **No ratified status.** See [`candidacy-and-ratification.md`](candidacy-and-ratification.md).
- **No assembly membership.** Whether this contribution belongs with others is
  [`CandidateAssembly`](candidate-assembly.md)'s judgement, and it is a separate act with its own
  confidence.

## Quality checks

- **The span supports the value.** Read the fragment content alone: does it sustain the interpreted
  value without the surrounding document? If it needs the rest of the document, reference more
  fragments.
- **The semantic role exists** in the target record package. A role invented at interpretation time
  cannot be validated later.
- **Absence is not a contribution.** "No beneficiary stated" is not a contribution with an empty
  value; it is a missing semantic, reported by the assembly.
- **The two confidences move independently.** If they are always equal, one of them is not being
  assessed.

## When to refuse

Emit no contribution where the source does not sustain one. A skill that returns nothing from a
document containing nothing has succeeded. **The pressure to find something is the main way
interpretation goes wrong**, and it produces exactly the plausible, unfalsifiable content that a
governed record must never carry.

## Anti-patterns

- **The confident invention** — a value with high extraction confidence and no fragment that says it.
- **The merged confidence** — one score standing for both "I read this correctly" and "this claim is
  well-evidenced", which are routinely opposite.
- **The role invented to fit** — creating a semantic role because the evidence did not match any
  existing one, rather than reporting that the evidence contributes nothing.
- **The pre-assembled contribution** — a single contribution carrying six roles at once, which
  smuggles the grouping judgement in before it can be examined.
