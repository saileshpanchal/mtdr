---
id: TDR-0041
title: Separate access, use and disclosure within information scope, each qualified by purpose and context
status: proposed
template: full
decision_date: 2026-08-21
accountable_owner: Sailesh Panchal
confidence: medium
maturity: proposed
supersedes: TDR-0015
derived_from: TDR-0002, TDR-0012, TDR-0032
confirmed_by_outcome: pending — review when an adopter has mapped one material decision across all five questions with each answer owned by the correct layer, or 2027-02-21, whichever is sooner
---

# TDR-0041 — Separate access, use and disclosure within information scope, each qualified by purpose and context

> **Proposed. No standing. A new proposed judgement — not a carry-forward.**
>
> This is the one record on the reconciliation branch that must not be read as representation
> recovery. A candidate on `codex/gate-b-decision-drafts` (`f966a05`) proposed five
> *information-governance* questions. Specification §4.4 has since become five *scope* questions in
> two groups — renaming visibility to access, promoting disclosure, and naming use as a distinction
> outside the record. Reconciling one against the other produced a **different formulation**: six
> questions in two groups, with use promoted to first-class and purpose qualifying all three
> information-scope questions.
>
> **The candidate is the origin of the question. It is not the author of this answer.** That
> candidate was never ratified, its identifier is burnt, and no part of this record inherits
> anything from it beyond the problem it identified. Where the formulations diverge is stated under
> *Decision*, so a reviewer may reject this reconciliation and require the candidate's original form
> instead.
>
> It proposes to supersede [TDR-0015](TDR-0015-visibility-and-effectiveness.md) **narrowly** — only
> its third judgement, the four-scope grouping. The other three are retained and restated below.
> TDR-0015 remains accepted unless and until a named human ratifies this record. The audit is
> [`evidence/gate-b-candidate-disposition-2026-08-21.md`](evidence/gate-b-candidate-disposition-2026-08-21.md).

## Context — what was known at the time

TDR-0015 made four judgements: the record enforces neither access nor disclosure and admits no
classification vocabulary; the `x-` adopter namespace opens with a contract; **spec §4.4 separates
four scopes — applicability, authority, visibility, impact**; and effectiveness fields are deferred
to evidence.

The third of those is no longer what the specification says.

`records/decision/specification/tdr.md` §4.4 is now titled **"Five recurring scope questions"**. It
renames *visibility* to **access**, promotes **disclosure** from a clause to a question of its own,
and adds a paragraph the record never authorised:

> A third, purely **runtime distinction** sits outside the record entirely — *use*: whether
> knowledge, once held, may influence an action. Access does not grant use, and use does not grant
> disclosure.

So the specification already separates access from use from disclosure, already groups the questions
into **operating scope** and **information scope**, and already states the non-implication chain. The
record that governs it still says four scopes, one of them under a name the specification abandoned.

**This is the shape [TDR-0039](TDR-0039-state-relative-requirements.md) found in the VR schema,
reversed.** There the specification was right and the schema encoded something stronger; here the
specification is right and the decision records something older. In both, the correction is small
and the useful part is noticing that the register and the artefact had stopped agreeing without
anyone deciding they should.

What remains genuinely undecided is not whether access, use and disclosure differ — §4.4 says they
do — but whether **use** is a first-class question or a parenthetical, and whether **purpose and
context** qualify one question or all of them. §4.4 currently carries purpose inside the disclosure
row, which reads as though a use permission were context-free once granted. That is the reading this
record exists to close.

The countervailing risk is real and bounded: a standard that enumerates governance questions can be
mistaken for one that answers them. TDR-0015's first judgement exists to prevent exactly that, and it
is retained without amendment.

## Decision

**Scope divides in two, and the second division has three questions, not two.**

| | Question | Asks |
|---|---|---|
| **Operating scope** | Applicability | Where, and to whom, does this decision bind? |
| | Authority | Under what mandate may this be decided, delegated, excepted or attested? |
| | Impact | What does it affect — capabilities, controls, customers, other decisions? |
| **Information scope** | Access | What may this participant know exists, retrieve or read? |
| | Use | May knowledge already held influence this action or decision? |
| | Disclosure | May information be communicated to this audience, through this channel? |

**Each information-scope question is qualified by purpose and context** — for which purpose,
situation, time and conditions the access, use or disclosure is valid. Purpose is not a property of
disclosure alone; a use permission granted for one purpose does not survive into another, and a
record that treats purpose as a disclosure clause cannot express that.

**The non-implication chain is a rule, not an observation:**

> Access does not grant use · use does not grant disclosure · disclosure to one audience for one
> purpose does not license another · **and none of them grants authority.**

The last clause is the load-bearing one. Permission to read a decision, or to invoke a system action,
is not an organisational mandate to decide. A system that can answer *may this participant see it*
and believes it has answered *whose judgement counts* has relocated accountability into software —
the failure [ARCHITECTURE.md](../ARCHITECTURE.md) names when it holds authority orthogonal to every
layer rather than as one of them.

**What this record does not change**, and states so that supersession is read at the right grain:

- **The record still enforces nothing.** It may carry available judgement and evidence about these
  questions. It does not apply their answers, and no classification vocabulary enters the core.
  TDR-0015 judgement 1, retained.
- **The `x-` namespace and its contract stand unchanged.** TDR-0015 judgement 2, retained.
- **Effectiveness fields remain deferred.** TDR-0015 judgement 4, retained.
- **No new core field.** A store governs the material it holds within its administrative domain; a
  downstream consumer evaluates identity, mandate, applicability and purpose for the flows it
  performs; human conduct after legitimate disclosure is guaranteed by no layer at all.

**Where this differs from the Gate-B candidate**, deliberately and reviewably: the candidate proposed
five *information-governance* questions — knowledge and access, authority, permitted use, disclosure,
purpose and context — which would stand beside §4.4's five *scope* questions as a second and
different five. This record instead promotes **use** into the information-scope group the
specification already has, and makes **purpose and context** a qualifier on all three rather than a
sixth question. The candidate's judgement is carried; its shape is reconciled to what shipped.

## Evidence

- **Business** — collapsing these questions produces ambiguous obligations and makes controls appear
  broader than they are. An organisation that cannot say why a participant may act on something it
  may read has no defensible answer when asked.
- **Architecture** — the division keeps identity, storage, access control and authority from
  collapsing into one layer while leaving every enforcement implementation outside MTDR. It is
  consistent with [TDR-0032](TDR-0032-typed-multi-object-conformance.md): the subject of a claim
  determines what the claim means, and *may see* and *may decide* are claims about different
  subjects.
- **Regulatory** — §4.4 is already regulator-neutral in this shape. The promotion of use and the
  qualification by purpose still require applied external review, which this record does not have.
- **Operations** — a participant routinely needs a decision's conclusion to do their work without
  being authorised to see its evidence, act beyond it, or repeat it onward. Three permissions, three
  answers.
- **Customer** — information used or disclosed outside its authorised purpose harms customers even
  when the initial access was entirely legitimate. Purpose-blindness is not a lesser failure than
  over-disclosure; it is the same failure later.
- **Data** — projections and audit evidence must retain purpose, audience, context and time. A
  single context-free access label cannot reconstruct why a flow was permitted.
- **External** — access control, purpose limitation, usage control and information-flow discipline
  are the candidate comparison points. **No durable comparative review is cited here**, and none is
  made a dependency. This gap is carried by DAC-0041 rather than smoothed over, and is the main
  reason confidence is medium.

## Alternatives rejected

1. **Publish the Gate-B five verbatim.** Rejected: it would place a second, differently-composed set
   of five questions beside the specification's own, and a reader would have to work out which five
   governs. Two competing enumerations are worse than the ambiguity they were written to remove.
2. **Amend §4.4 and leave TDR-0015 standing.** Rejected: that is editing the artefact while the
   governing decision says something else — the drift this record was written because it found.
3. **Call it a clarification of TDR-0015.** Rejected: promoting use to a question and qualifying all
   three by purpose changes how responsibility is allocated between layers. That is changed
   judgement, and changed judgement supersedes.
4. **Put access, use, disclosure and purpose into record fields.** Rejected: fields would state
   claims and enforce nothing, and would bind the standard to one governance vocabulary. TDR-0015
   settled this and it is not reopened.
5. **Treat access as authority.** Rejected: permission to read or to invoke is not a mandate to
   decide, and the conflation is how accountability detaches from the people who hold it.
6. **Do nothing.** Rejected: the register currently holds two different answers — a record saying
   four scopes and a specification saying five — and leaving them to disagree teaches every reader
   that the register is not where the answer lives.

## Options foreclosed

- No conforming architecture may claim that access, storage, or a record's status alone confers
  authority.
- No context-free *may use* or *may disclose* conclusion may be inferred from possession.
- Purpose may not be re-narrowed to a property of disclosure without superseding this record.
- MTDR cannot grow a runtime enforcement model for any of these questions without a superseding
  decision. Enumerating a question is not a commitment to answer it.

## Consequences and review

Success is an adopter mapping one material decision across all six questions — three operating,
three information — with each answer owned by the correct layer and no field mistaken for a control.
Failure looks like the enumeration being cited as though it were a control framework, which is what
the assurance case is routed to examine.

If ratified, §4.4 is reconciled to this record in the same change: use promoted into the
information-scope group, purpose stated as a qualifier on all three. **No specification text is
changed while this record is proposed.**

Review on that adopter evidence, or 2027-02-21, whichever is sooner. Assurance must test inference
leakage across compartments, delegated authority, purpose drift, human workarounds, and the harm
created by projections that are too restrictive as well as by those that are too wide.
