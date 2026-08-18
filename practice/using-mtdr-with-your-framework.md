# Using MTDR with your framework

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal

You have an architecture, an operating model, a governance framework or a standards project of your
own, spread across documents that were written for other purposes. This is how you apply MTDR to it.

Runtime-neutral. Where a step depends on your reasoning environment, it says so and points at
[`skills/packaging/`](../skills/packaging/).

## The one thing to understand first

**Your framework is source material. It is not something MTDR is configured to match.**

That inverts the usual expectation, and everything else here follows from it. You do not adapt the
record semantics to your terminology, add your document types as fields, or write your governance
model into a prompt. MTDR reads what your material *says* and reconstructs candidate organisational
records from it, preserving provenance, gaps, conflicts and uncertainty on the way.

If your framework genuinely needs record semantics MTDR does not have, that is not a customisation
question — it is a proposal, and it goes through the
[language admission test](../specification/record-admission-test.md). Editing the standard to fit one
adopter is how a portable standard stops being portable.

## What MTDR adds to what you already have

You almost certainly have an agent stack. MTDR does not replace any of it:

| Layer | You probably have this |
|---|---|
| Procedural capability | Skills — MTDR ships twenty-five and uses the same open format |
| Packaging and distribution | Plugins, extensions, however your runtime installs things |
| Interaction | A protocol, a chat surface, an API |
| **Governed semantics and lifecycle** | **This is the gap** |
| **Standing** | **Yours. It always was** |

A skill can express a method. It cannot say that a value commitment lacking a counter-signatory is a
valid *candidate* and an ineligible *ratification*. That distinction — what a record means, which
states it may occupy, what a transition requires — is what MTDR supplies, and the
[standards boundary](../specification/standards-boundary.md) sets it out in full.

## The workflow

> your material → MTDR skills → fragments and contributions → candidate records →
> validation and challenge → **human ratification** → governed records → supersession and
> reconstruction

One pass, in that order.

**1. Point a participant at MTDR and at your material.** Follow the instructions for your runtime in
[`skills/packaging/`](../skills/packaging/). Every runtime verified so far reads the canonical skill
files unmodified, so this is a matter of where files go rather than what they say.

**2. Identify what is there.** `decision-identification` first, then the shared
`identify-record-contributions`. The question is not "which documents are decisions" — documents are
containers, and a decision is often spread across four of them or buried in a note nobody labelled.

**3. Reconcile.** `reconcile-record-fragments` groups contributions that concern one object and refuses
to group ones that merely appear together. **Proximity is never identity.** Expect it to record
conflicts rather than resolve them; that is the point.

**4. Draft.** `draft-tdr`, `value-record`, or the value lifecycle for commitments. What comes back is a
*candidate*: proposed, unratified, with no organisational standing whatever.

**5. Challenge and validate.** `challenge-record` attacks the candidate against its own evidence, and
returns *fit to propose* or *not fit to propose*. `validate-record` reports the four dimensions —
structural, semantic, relational and lifecycle-transition eligibility — independently.

**6. Ask why.** [`show-me`](../skills/shared/show-me/) walks each value back to the span it came from.
Run it before ratifying anything. A field that comes back `unsupported` is a value nothing in your
material accounts for, and it is the most useful thing the exercise will tell you.

**7. Ratify — or don't.** A named individual accepts accountability, or the record stays a candidate.
No skill performs this step, and none can.

## What to expect on real material

The first run is usually uncomfortable, and the discomfort is the product.

- **Decisions with no owner.** Your material will name committees, roles and report authors. MTDR needs
  a named individual and will report the gap rather than choose one. Expect several.
- **Conflicts you did not know you had.** Two documents stating different dates or thresholds for the
  same thing, neither citing the other. Recorded, not resolved.
- **Commitments nobody made.** Figures that appear in a business case and trace to nothing.
- **Decisions nobody wrote down.** A workaround whose review trigger passed years ago and which now has
  budget attached to it.

None of these is a failure of the reconstruction. They are the state of your organisation's memory,
which was previously unmeasured.

## The worked example

[`tests/adoption/brackwell/`](../tests/adoption/brackwell/) is a complete fictional framework — a
council's fleet and depot modernisation, six documents — with the expected reconstruction in
[FIX-301](../tests/adoption/FIX-301-brackwell-reconstruction.md). It contains every failure mode above,
on purpose. It is deliberately not financial services, so that nothing about the reconstruction can
depend on the domain.

Run it before you run your own material. It takes about five minutes and it calibrates what "correct"
looks like — including that a good reconstruction reports more gaps than you expected.

## What this will not do for you

- **It will not decide anything.** MTDR records judgements and reports what evidence supports them.
  Every act of authority remains yours ([TDR-0027](../decisions/TDR-0027-human-ratification-confers-standing.md)).
- **It will not tell you whether a decision was good.** `challenge-record` asks whether the record
  faithfully represents its evidence. A record can pass and describe a terrible decision, accurately.
- **It will not make you compliant with anything.** Regulatory regimes appear in this standard as
  worked examples. Your context is evidence and framing, never a claim the record satisfies a rule.
- **It will not require a platform.** No graph, no register, no policy engine, no service. If something
  seems to require one, that is a defect in the distribution rather than a gap in your setup.

## Contributing back

If your framework surfaced something the standard genuinely cannot express — a record type, a semantic
role, a lifecycle state — that is worth proposing. Open a superseding TDR
([CONTRIBUTING.md](../CONTRIBUTING.md)), state what is now known that was not known before, and bring
the evidence. Discussion happens in the standard's own format, which is the only real test of whether
it works.
