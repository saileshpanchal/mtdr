---
name: problem-framing-and-decision-capture
description: Frame a significant organisational decision and capture it as a Transformation Decision Record (TDR) at the moment it is made. Use this skill whenever a decision is being taken, discussed, or prepared — a supplier selection, an architecture choice, a policy change, a channel closure, a migration, an investment — and especially whenever someone says "let's decide", "we've agreed", "the steering group approved", or asks to write up a decision. Use it during the meeting, not after it — the value of the record collapses when it is reconstructed.
---

# Problem Framing & Decision Capture

This skill produces a TDR at the moment of decision. It is written for humans and usable by AI assistants. Read `spec.md` for field definitions; templates are in `/templates`.

## The one rule

**The record is drafted before the decision meeting ends.** A TDR written a week later is a reconstruction, and reconstructions inherit exactly the gaps this format exists to prevent.

## The grammar — six lines first

Before working the process below, draft the decision as six spoken lines — it makes the missing pieces obvious, and it compiles straight into the fields:

> **Under** (the authority) · **Given** (the context and evidence) · **We decide** (the choice and the rejected alternatives) · **This means** (what bindingly changes) · **Unless** (the exceptions) · **Until** (the review trigger, expiry, or "until superseded").

The clause you cannot fill is the part that was not really decided. Full guidance, the field mapping and worked examples are in [`practice/decision-grammar.md`](../../practice/decision-grammar.md). The steps below are the same discipline in long form: *Under* is step 4 (the named owner), *Given* is step 3, *We decide* is steps 1 and 5, *This means* is step 6, *Until* is step 8.

## Process

### 1. Frame the actual question

State, in a single sentence, what is being decided. If it takes three sentences, there are probably three decisions — split them.

Check the altitude: is this being decided by the person who should own it? A core platform choice decided by a technology lead without a board mandate, or a brand refresh governed like a core migration, are both altitude errors. Note a mismatch in the Context section; do not silently fix it.

### 2. Apply the proportionality test

Is this a one-way door? Ask: *what would it cost to reverse this in twelve months?*

- Irreversible or costly to reverse → **full template**
- Significant but revisable → **minimal template**
- Cheap to reverse → **bare template**, or no record at all

If reversing would cost less than writing the record, stop here.

### 3. Capture what is known at the time

In the present tense of the decision, record: the facts in hand, the known unknowns, the assumptions being made, the constraints (budget, regulatory, time), and any time pressure forcing the decision now. This section is the record's core value — it is what nobody can reconstruct later.

### 4. Name the accountable owner

A named individual. If the room offers a committee name, ask: *if a regulator, auditor or board asked who exercised judgement here, whose name would be given?* That is the owner. A committee can endorse judgement; it cannot exercise it.

### 5. Enumerate alternatives — including "do nothing"

Every option genuinely considered, each with its reason for rejection. If no alternatives were considered, record that honestly: it is itself important evidence about how the decision was made.

### 6. Surface options foreclosed

Ask the room: *what does this decision make impossible, or prohibitively expensive, later?* Record foreclosures accepted deliberately as well as those merely tolerated. This question routinely changes the decision itself — ask it before the decision is final, not after.

### 7. State confidence honestly

`low`, `medium` or `high` — the owner's actual confidence, not the meeting's social confidence. A recorded `low` with good evidence is a defensible position; an inflated `high` is a liability.

### 8. Set the review trigger

`confirmed_by_outcome: pending — <date or event>`. A record that is never tested against its outcome is a diary entry, not memory.

## Quality checks before saving

- Could a stranger reconstruct the judgement from this record without interviewing anyone?
- Is the owner a named individual?
- Is "do nothing" among the alternatives, or its absence explained?
- Is the Context written at decision time, not hindsight?
- Does the template tier match the reversibility test?

## Anti-patterns

- **Retro-fitting** — writing the record after outcomes are known, then presenting it as time-of-decision context.
- **Committee-as-owner** — accountability laundering through a group name.
- **Confidence theatre** — recording `high` because the meeting felt confident.
- **Everything-is-full** — full records for reversible decisions; box-ticking that erodes the instrument.
