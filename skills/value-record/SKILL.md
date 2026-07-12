---
name: value-record
description: Raise, draft and reconcile a Value Record (VR) — the sibling record to the TDR that holds a quantified benefit claim and its reconciliation as one record. Use this skill whenever a quantified benefit claim enters a decision ("this saves", "this unlocks", "this reduces the risk of"), whenever someone asks "did that value ever arrive" or "who owns this benefit", and at every reconcile-by date. It refuses to mark a VR agreed without a measured baseline, a named finance counter-signatory and a reconcile-by date.
---

# Value Record

This skill raises and runs Value Records. It is written for humans and usable by AI assistants. Read `spec-value-record.md` for field definitions; the decision-identification skill sits in front of it and finds the decisions the claims are attached to.

## The one rule

**No baseline, no claim.** A benefit measured against nothing can never be reconciled against anything, and an unreconcilable claim is decoration, not a value case. Everything else in this skill exists to keep claims reconcilable.

## Process

### 1. Recognise the claim

Raise a VR whenever a quantified benefit claim enters a decision — a number doing persuasive work in a TDR's context, evidence or business case references. Listen for "this saves", "this pays for itself", "this releases", "this de-risks". One claim per record; a business case with three benefit lines is three VRs, each with its own baseline and falsifying signal.

If the claim is too small to be worth reconciling, the answer is to take it out of the decision, not to record it unreconciled — proportionality applies to value claims exactly as it applies to decisions.

### 2. Baseline first

Before drafting anything else, establish the measured starting point: the value, its date, its source. If no baseline exists, the first action is to measure one — not to draft around its absence. A baseline reconstructed after the change lands is not a baseline; it is the same hindsight the TDR's context section forbids.

### 3. Counter-signatory before agreement

Identify the **named individual in finance** who will co-sign the claim — before the VR moves to `agreed`, not after. Not a committee, not a role, not "finance to confirm". The counter-signatory co-signs the claim, every material state change, and any write-off. A claim nobody in finance will put their name to is not a claim the organisation believes, and the record should say so by staying `proposed`.

### 4. Draft the record

Using [`templates/vr.md`](../../templates/vr.md):

- **Value thesis** — what value, of which kind, and the **falsifying signal** that would show it is not arriving. If the drafter cannot name what failure would look like, the thesis is not yet a claim.
- **Expected value and recognition route** — where the value shows up (cost line, revenue line, risk reduction, capacity) and how it is recognised. "Recognised" means the counter-signatory can point at it.
- **Optimism adjustment** — the declared correction and its rationale. An adjustment of zero is permitted; an undeclared one is not.
- **Stage** — place the spend or change on the ladder: exploration, pilot, procurement, build, production, retired.
- **Reconcile-by** — the date the claim faces reality. Mandatory. "Ongoing" is not a date.

### 5. Run the reconciliation loop

While the VR is `realising`:

- Append **realised entries** — dated observations against the baseline — as they occur. Entries are lifecycle facts, added in place; the thesis and baseline are never edited.
- Watch for the **falsifying signal**. Its appearance is not an emergency; it is the record working. Bring it to the counter-signatory when it appears, not at the deadline.
- At each **stage promotion**, raise a superseding VR stating what is now known that was not known at the previous stage — including a corrected expected value if the optimism adjustment proved too kind.
- At `reconcile_by`, close the loop: **reconciled** (claim tested against baseline, outcome recorded, whatever it was) or **written-off**. Passing the date in silence is the one outcome this skill exists to prevent.

### 6. The write-off discipline

`written-off` is a **signed state**: value that did not arrive is declared, not forgotten. A write-off requires the counter-signatory's signature and a statement of what was learned — about the thesis, the baseline, or the organisation's optimism. Treat a clean write-off as the record succeeding: the organisation paid full price for that knowledge and now gets to keep it. A record set with no write-offs in it is not evidence of good forecasting; it is evidence of unreconciled claims.

## When to refuse

This skill refuses to mark a VR `agreed` when any of the following holds, and says which:

- **No measured baseline** — there is nothing to reconcile against.
- **No named finance counter-signatory** — a committee, a role, or a blank is not a name.
- **No reconcile-by date** — a claim with no date never has to be true.

The refusal is not a rejection of the underlying decision. The linked TDR can proceed on its own merits; what it cannot do is carry an unreconcilable number as if the number were evidence.

## Quality checks

- Does the falsifying signal describe something observable, on a stated route, before `reconcile_by`?
- Could a stranger reproduce the baseline from its stated source and date?
- Would the counter-signatory recognise the recognition route as theirs?
- Is the optimism adjustment reasoned, or a ritual percentage?
- Does every `supersedes` / `derived_from` reference resolve to a real VR?

## Anti-patterns

- **Benefit laundering** — re-claiming the same value against successive decisions; one baseline cannot be spent twice.
- **The migrating reconcile-by** — pushing the date back each time it approaches; a moved date is a material state change and needs the counter-signature and the reason.
- **Retro-fitted baselines** — measuring the starting point after the change has landed.
- **Write-off by silence** — letting a claim quietly expire instead of signing its write-off; the unsigned version teaches the organisation nothing.
- **Committee counter-signature** — "approved by the benefits board" defeats the field's purpose exactly as a committee owner defeats the TDR's.

## Scope note

This skill runs the value case using nothing beyond the record set itself. Implementations that wire VRs to finance systems, benefit registers or dashboards are downstream implementation, deliberately outside this standard (see TDR-0002, TDR-0008).
