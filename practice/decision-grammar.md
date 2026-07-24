# The Consequential Decision Grammar

*A candidate authoring grammar — v0.1. This is a proposal, offered for use and challenge, not settled
doctrine. It adds nothing to the record format: it is a way of thinking and writing a decision that
compiles straight into the existing [MTDR fields](../spec.md). Nothing here changes a field, a template or
the schema, and every existing record still validates.*

Given–When–Then gave testers a shape for behaviour. User stories gave teams a shape for requirements.
Neither improved the work by adding process; each gave people a form that made the good questions obvious.
Decisions have never had one. This is a candidate.

## The six lines

> **Under.** The authority the choice was made under.
> **Given.** The context, evidence and constraints that shaped it.
> **We decide.** The choice made, and the alternatives rejected.
> **This means.** What now changes: obligations, permissions, scope.
> **Unless.** The exceptions, and where it does not apply.
> **Until.** When it must be revisited, expires, or is superseded.

Read aloud, the six lines are speakable, which is the point — always in this spoken form, never as an
initialism. Underneath the wording sits a durable set of six separations that hold even where the phrasing
does not: **Authority · Basis · Choice · Effect · Boundary · Validity.**

## Clause by clause

### Under — authority

The authority under which the decision was legitimately made. This is not only a delegated forum mandate:
it may be **statutory, regulatory, policy or contractual** authority, or an individual's own accountable
remit. If you cannot name the authority, the decision may not have been anyone's to make — which is itself
a finding worth recording.

### Given — basis

The context as it stood: the facts in hand, the known unknowns, the assumptions being made (as assumptions,
not facts), the constraints, and the decisions this one follows from. Written in the present tense of the
decision, never reconstructed with hindsight.

### We decide — choice

The choice, stated plainly, with the alternatives that were genuinely considered and why they were
rejected. **"We decide" is the iconic line, but the actor is whoever holds the authority:** *I decide*,
*the Board decides*, *the forum decides*, *the accountable executive decides*. Write the named owner, not a
vague "we" — an unnamed "we" is the most common way an ownerless decision hides.

### This means — effect

What now **bindingly** changes: the obligations created, the permissions granted, the prohibitions imposed,
the scope affected. This is the clause people get wrong. *This means* is the **binding consequence**, not
the **hoped-for benefit**. "This means we will delight customers" is an aspiration; "this means teams must
design for credential retention, and reissue now requires justification" is a consequence someone can act
on and be held to. The benefit belongs in a [Value Record](../spec-value-record.md); the consequence
belongs here.

### Unless — boundary

The exceptions and the applicability boundary: where the decision does *not* apply, and the conditions under
which it is set aside. An exception with no stated authority to invoke it is not an exception; it is a
loophole.

### Until — validity

When the decision must be revisited: a review trigger, an expiry, or a superseding condition. **This clause
is about validity, not duration.** Not every decision expires; many are valid **until superseded**, and
that is a complete and honest *Until*. Do not invent an artificial review date to fill the field — a forced
date you do not mean corrupts the one field (`confirmed_by_outcome`) whose whole value is honesty.

## How it compiles into MTDR

The grammar is a lens, not a new format. Each clause maps onto fields the standard already defines:

| Grammar line | Compiles into |
|---|---|
| **Under** | `accountable_owner` (the named individual), and the authority stated in **Context** |
| **Given** | **Context**, **Evidence**, assumptions, `derived_from`, constraints |
| **We decide** | **Decision** + **Alternatives rejected** |
| **This means** | **Options foreclosed** + **Consequences** (the binding change, not the benefit) |
| **Unless** | Exceptions and applicability, stated in **Context / Decision** scope |
| **Until** | `confirmed_by_outcome` (the review trigger) + the supersession lifecycle (`supersedes`) |

Two clauses — *Under*'s authority and *Unless*'s exceptions — live in the record's prose rather than in
dedicated frontmatter fields. That is deliberate: the grammar needs no new field, and a decision written in
the six lines is already most of the way to a complete record.

## A weak decision, rewritten

*Fictional, for illustration.*

**Weak:** "The programme will aim to minimise customer disruption during migration."

That describes an aspiration. Nobody owns it, nothing changes because of it, and it cannot be checked later.
Through the grammar:

> **Under** the migration steering authority.
> **Given** the regulatory duty to treat customers fairly and the programme's customer-outcomes commitment.
> **We decide** that customers keep their existing credentials wherever possible; reissue is the exception,
> not the default.
> **This means** delivery teams must design for credential retention, and any reissue now requires
> documented justification.
> **Unless** retention would create fraud or service risk beyond the agreed tolerance.
> **Until** superseded by the post-migration review.

The rewrite is a decision someone can be accountable for, act on, and check against later. The clause you
cannot fill is the part that was never really decided.

## A second example — a policy clause

*Fictional, for illustration.*

> **Under** the payments product policy and the scheme rules it implements.
> **Given** the scheme's settlement-window obligation and current processing volumes.
> **We decide** that priority payments are submitted no later than 30 minutes before the settlement cut-off.
> **This means** the operations team must monitor submission timing against the cut-off and hold a
> documented exception path.
> **Unless** a scheme incident extends the window, under the incident authority.
> **Until** the scheme rule changes or the decision is superseded.

Notice that the scheme obligation is the **Given**, not the decision. The regulator or scheme made the
obligation; the organisation decided its response. That distinction is what keeps an external requirement
from being mistaken for an internal judgement.

## Anti-patterns

- **Benefit as consequence** — writing a hoped-for outcome in *This means*. If it is a benefit, it is a
  Value Record; *This means* is what bindingly changes.
- **The invented review date** — a date in *Until* that no one means, filled to complete the field. "Until
  superseded" is honest; a fake date is not.
- **The hidden owner** — "we decide" with no named individual behind the "we".
- **Two decisions in one** — if *We decide* needs an "and", there are probably two decisions with two owners.
  Split them.
- **Authority asserted, not sourced** — an *Under* that names no real mandate.

## Is it actually a decision?

The grammar doubles as a test. If you cannot fill **We decide** with a real choice *and* **This means** with
a binding consequence, you are not looking at a consequential decision — you are looking at a status update,
a plan, or an aspiration. That is the same judgement the
[decision-identification skill](../skills/decision-identification/SKILL.md) makes, in six lines.

## Status and how to challenge it

This grammar is a **working candidate (v0.1)**. It reads well against many decision classes, but the real
test is whether all six separations stay conceptually distinct across the full range — strategy, policy,
architecture, risk acceptance, regulatory interpretation, investment, operating model, agent mandate, and
runtime decisions. Where a clause collapses into another for a whole class of decision, that is exactly the
evidence worth bringing.

Challenge it the way you would challenge any decision in this repository: propose a superseding change,
stating what is now known that was not known before. The grammar is here to be used and improved, not
concluded.
