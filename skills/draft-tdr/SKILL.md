---
name: draft-tdr
description: Assemble reconciled contributions into a standards-conformant TDR candidate — filling only what the evidence supports, leaving gaps visible, and never raising status beyond proposed. Use this skill after reconcile-record-fragments has produced a candidate assembly, whenever someone says "turn this into a record" or "write it up from these documents", and when a decision found in existing material needs a conformant draft. It refuses to invent a missing owner, date or alternative, and it applies the proportionality rule rather than defaulting to the full template.
---

# Draft TDR

This skill turns a [`CandidateAssembly`](../../shared/candidate-assembly.md) into a conformant markdown
TDR. It is written for humans and usable by AI assistants. Read [`spec.md`](../../spec.md) for field
definitions and [`records/tdr/`](../../records/tdr/) for the roles and admission test.
`challenge-record` and `validate-record` run after it.

Note what this skill is not. `problem-framing-and-decision-capture` drafts a record with a human who
holds the reasoning. This skill drafts from evidence alone, and the difference is that **it may not ask
a question to fill a gap.** Every gap stays a gap.

## The one rule

**Write only what a contribution supports.** A drafted record is a rendering of the evidence, not a
composition informed by it. Where the template has a section and the evidence has nothing, the section
says what is missing — it does not say something plausible.

## Process

### 1. Check admissibility first

Apply [`records/tdr/admission.md`](../../records/tdr/admission.md). An inadmissible candidate is not
drafted; report why. In particular, a candidate whose `context` contributions post-date the decision is
not drafted until the offending contribution is removed.

### 2. Apply the proportionality rule

`spec.md` §3, on the `reversal-cost` contributions: irreversible or costly → full · significant but
revisable → minimal · cheap → bare · cheaper to reverse than to record → **no record, and say so**.

Defaulting to the full template because the evidence is plentiful is a misreading. Volume of material
is not reversal cost.

### 3. Render frontmatter from contributions only

`status: proposed`, always. `supersedes` and `derived_from` take only ids evidenced by
`lineage-*` contributions — never a guess, never an id that does not exist. Where `accountable_owner`
has no contribution, do not emit a value; carry the gap into the draft explicitly.

### 4. Write the body in the present tense of the decision

`spec.md` requires context "as it stood at the moment of decision". Render it from contemporaneous
contributions and nothing else. **If a fact is known only because of what happened afterwards, it does
not belong in the record**, however much it improves the narrative.

### 5. Mark every gap in place

A missing mandatory role appears in the draft where it belongs, named as missing, with what would close
it. A ratifying owner should be able to read the draft and see immediately what the evidence did not
supply.

### 6. Carry provenance

Every rendered value keeps its trace to the contributions and spans behind it. What an adopter does
with that provenance after ratification is their decision — see
[`shared/provenance.md`](../../shared/provenance.md) — but it must exist at the moment of proposal.

## Outputs

A markdown TDR at the routed template tier, with `status: proposed`, gaps marked in place, and
provenance attached. Plus a one-paragraph statement of what the evidence did not supply.

Where the proportionality outcome is **no record**, output that finding with its reasoning instead of a
record. This is a successful result.

## Quality checks

- Does every rendered sentence trace to at least one contribution?
- Is `accountable_owner` either evidenced or visibly absent — never inferred from document authorship?
- Does the context contain anything knowable only in hindsight?
- Are the seven evidence dimensions each either evidenced or marked "not material", with silent omission
  avoided as `spec.md` §5 requires?
- Would the named owner recognise this as their decision, in their words?

## When to refuse

- **The candidate is inadmissible.** Report, do not draft.
- **The evidence supports no decision**, only a plan or a status. Say so.
- **The gaps are so wide the draft would be mostly absences.** Report the finding rather than emitting a
  skeleton that looks like a record.

## Anti-patterns

- **Narrative completion** — writing the alternatives that "must have" been considered.
- **The plausible owner** — the document's author recorded as accountable.
- **Hindsight context** — outcome knowledge presented as what was known.
- **Full-template reflex** — the richest tier chosen because the material was rich.
- **Gap laundering** — a missing field rendered as "not applicable" rather than missing.
- **Status inflation** — anything beyond `proposed`.

## Scope note

This skill drafts from contributions and the record package alone. Whether the resulting file is stored,
registered, indexed or connected to anything is downstream implementation, deliberately outside this
standard (see TDR-0002, TDR-0018).
