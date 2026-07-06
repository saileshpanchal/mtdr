---
name: decision-identification
description: Recognise when a conversation, document, meeting, incident or piece of work contains a decision that should become a Transformation Decision Record (TDR) — and route it to the right template tier or to no record at all. Use this skill when reviewing meeting notes, project plans, RFCs, incident retrospectives, strategy papers or chat threads, when someone asks "do we need a decision record for this?", or when work is starting and nobody is sure whether a decision has actually been made. It sits in front of the other three skills: it finds the decision; they capture and review it.
---

# Decision Identification

This skill finds decisions that deserve a record. It is written for humans and usable by AI assistants. Read `spec.md` for field definitions; the capture, evidence and governance skills in this directory take over once a decision is identified.

## The one rule

**Most things are not decisions, and most decisions do not need a record.** The skill exists as much to say "no record needed — here is why" as to say "this is a TDR". A record set diluted with status updates is as useless as no record set at all.

## Process

### 1. Scan for decision moments

A decision moment is a commitment that changes what the organisation will do: money committed, an architecture or supplier chosen, a policy adopted or dropped, a channel opened or closed, an option deliberately given up. Listen for the language of commitment — "we'll go with", "we've agreed", "approved", "from now on", "we're not doing" — and for its quieter forms: a default that hardened because nobody objected, an incident workaround that silently became the way things work.

### 2. Split compound decisions

One question per record. "Adopt platform X and migrate the customer data and restructure the team" is three decisions with three owners and three reversibility profiles. Escalate the split to whoever owns the work — never flatten a compound decision into one record to save effort.

### 3. Check the existing record set

Before proposing a new record, look for what it touches: does it revisit, contradict or build on a decision already recorded? Search whatever store of TDRs the organisation keeps — flat files in a repository, a wiki space, or a connected decision history assembled from the lineage fields (spec §6). Propose `supersedes` and `derived_from` candidates by id. If the new decision contradicts an accepted record, the outcome is a **superseding** TDR, never an edit (spec §7).

### 4. Apply the proportionality test

The same test as capture (spec §3): *what would it cost to reverse this in twelve months?*

- Irreversible or costly to reverse → **full template**
- Significant but revisable at tolerable cost → **minimal template**
- Cheap to reverse → **bare template**, or no record
- Reversing costs less than writing the record → **no record**, say so

### 5. Produce the candidate envelope

Summarise the identification as a **TDR Candidate Envelope** — a plain, tool-neutral summary the next skill (or any downstream implementation) can pick up without re-reading the source material:

```
outcome: tdr_candidate | split_required | not_a_tdr | update_existing | supersedes_existing
decision_moment: <the commitment, in one sentence>
compound_decisions: <list, if split_required>
lineage_candidates: <supersedes / derived_from ids, or none>
proportionality: <full | minimal | bare | no_record, with the reversal-cost reasoning>
recommended_next_skill: <problem-framing-and-decision-capture | evidence-review | governance-review | none>
reasoning_summary: <two or three sentences a stranger could follow>
```

The envelope is vocabulary, not schema — it adds no fields to the TDR format and needs no tooling to produce.

### 6. Hand off

- A candidate worth recording → **Problem Framing & Decision Capture**, ideally while the decision is still being made.
- A drafted record with thin evidence → **Evidence Review**.
- A record heading for acceptance → **Governance Review**.

## What is not a TDR

Name these explicitly so "no record needed" is a confident answer, not a shrug:

- **Status updates** — reporting that work happened is not deciding anything.
- **Actions** — "Priya to send the contract" is a task, not a judgement.
- **Preferences** — opinions not yet attached to a commitment of money, time or foreclosed options.
- **Restatements** — repeating an already-recorded decision in a new meeting does not create a new decision.
- **Operational routine** — choices fully determined by an existing policy or runbook; the judgement was exercised when the policy was decided.

## Quality checks

- Would the accountable owner recognise the decision moment as theirs?
- Is every `supersedes` / `derived_from` candidate a real id in the record set, not a guess?
- Does the proportionality reasoning name the actual reversal cost, not a feeling?
- If the outcome is `not_a_tdr`, does the reason cite one of the categories above?

## Anti-patterns

- **Record hunger** — turning every agenda item into a candidate; the proportionality test exists to stop this.
- **Retro-mining** — trawling old minutes to mass-produce records after outcomes are known; identification serves capture at the moment of decision, not archaeology.
- **Guessed lineage** — inventing supersedes links to records that do not exist.
- **Silent splitting** — quietly recording one slice of a compound decision and losing the rest.

## Scope note

This skill identifies decisions and their lineage hints using nothing beyond the record set itself. Implementations that hold decisions in a connected store may resolve lineage, policy links or impact automatically — that resolution is downstream implementation, deliberately outside this standard (see TDR-0002, TDR-0007).
