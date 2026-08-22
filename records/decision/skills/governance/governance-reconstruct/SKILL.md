---
name: governance-reconstruct
description: Extract candidate obligations, policies, authorities, decisions, controls, evidence requirements, inventories, review and challenge mechanisms, accountable roles, exceptions, waivers and regulatory or contractual sources from a supplied governance corpus, each carrying provenance and a claim-level epistemic state. Use this skill as the first pass over any governance estate — policy sets, terms of reference, committee packs, minutes, registers, inventories, audit findings — when someone asks "what governance do we actually have here?", "where did this control come from?" or "what does this policy set actually require?". It produces candidate state and projections, never authoritative organisational state, and an origin it cannot locate stays UNKNOWN rather than becoming optional.
---

# Governance Reconstruct

The first pass over a governance corpus. It reads what an organisation already holds and reports what
governance it can find, what it can only infer, and what it cannot establish at all.

Read [`governance-projection.md`](../../../validation/governance-projection.md) and
[`governance-rules.md`](../../../validation/governance-rules.md) first. The mechanics of finding and
classifying spans are the shared
[`identify-record-contributions`](../../../../../skills/shared/identify-record-contributions/)
skill's; this skill adds the governance semantics and holds none of that skill's rules a second time.

## What it looks for

Ten things, asked of the corpus rather than of any one document:

| Looking for | Recognised as |
|---|---|
| Obligation | something the organisation is required to do, by whom, under what source |
| Policy | a stated internal rule, its scope, and its stated basis |
| Authority | who may exercise, challenge, waive or amend — see [`obligation-authority-trace`](../obligation-authority-trace/) |
| Decision | a consequential choice with a binding consequence, routed to the decision language |
| Control | a mechanism said to establish a property |
| Evidence requirement | what must be produced, retained, or shown |
| Inventory | a register of things the estate claims to track |
| Review or challenge mechanism | who examines, and with what standing |
| Accountable role | who answers for it — a named individual, never a committee |
| Exception or waiver | a departure, its condition, its expiry, its authoriser |

**The unit is the governance job, not the document.** One terms-of-reference file may carry six of
these; a single minute line may carry three. Do not classify documents.

## The four rules that make this reconstruction rather than assertion

1. **Every positive claim carries provenance.** A claim with no locatable span behind it is an
   invention, whatever its plausibility (GR-01).
2. **Unknown origin stays `UNKNOWN`.** A policy whose originating authority cannot be found is a
   policy with an unlocated origin. It is not thereby internal, discretionary, or removable, and the
   `UNKNOWN` carries the question asked and the scope searched (GR-05, GR-08).
3. **Repetition does not create authority.** The same requirement restated in four documents is one
   claim copied three times. Four appearances raise no confidence and confer no mandate.
4. **Inferred state stays a projection.** A well-evidenced inference that someone approves things is
   an `INFERRED` claim about practice, never a `RECORDED` claim about entitlement (GR-03).

## The RECORDED / OBSERVED boundary

This is the judgement the skill gets wrong most often, and the one that matters most.

A decision plainly minuted in a pack is **`OBSERVED`** — the pack evidences that it happened. It is
**`RECORDED`** only where the evidence also shows it was admitted as authoritative state at the time.
*That a thing occurred is not evidence that it was authorised.* Collapsing the two is how a
reconstruction launders de-facto practice into governance, and it does so invisibly, because the
output looks better.

## Output

`governance-finding` projections, and candidate records routed to the language that owns them —
decisions to the decision lifecycle, value commitments to the value lifecycle. Nothing here writes a
record; drafting belongs to the drafting skills and ratification to a named human
([`candidacy-and-ratification.md`](../../../../../specification/candidacy-and-ratification.md)).

Report separately: what was found; what was inferred; what remains unknown, with the question and the
scope searched; what is contradictory, with both sides; and what governance-relevant material fitted
no category, as `UNCLASSIFIED` with a note. A recurring unclassified pattern is evidence for extending
the vocabulary by decision, never a reason to near-fit.

## When to refuse

- **Asked to confirm that a control is unnecessary** because the substrate supplies the same property.
  That is GR-05, and it is not this skill's call or any skill's.
- **Asked to fill an unlocated authority** from the most senior name in the material.
- **Asked to go looking for material.** The skill reads what an adopter supplies.

## Anti-patterns

- **Document classification** — "this is a policy, this is a minute" — instead of reconstructing the
  jobs the material evidences.
- **Confidence by repetition** — the same claim in four packs read as four pieces of evidence.
- **The tidy estate** — an output with no unknowns and no contradictions, produced from a real
  corpus. Governance estates accrete; a reconstruction with nothing unresolved has resolved something
  it should have reported.
- **Silent optionality** — an obligation whose source could not be found quietly dropping out of the
  finding set.
