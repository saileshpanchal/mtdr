# brackwell — decision recovery report

`recover-decision-records`, run 2026-11-07 by `adopter-trial` v1 over the six related Brackwell
District Council documents (`sources/brackwell/SRC-01` … `SRC-06`), as one run. Stages 1–5 run, then
stop. Six historical candidates, all standing `none`. No review event produced.

| Source | sha256 (as read) | Own date (basis) |
|---|---|---|
| SRC-01 Scheme of Delegation v4 (extract) | `b56929a324065cf937b3216006695667cb24a993a115b7194d937e78208f1f1c` | "adopted 2025-04-01" (adoption, not production) |
| SRC-02 Cabinet minute extract | `1406f4a2f165dc411f4834a505696e18fbdd84bb3c57825dadd00ac8ac795c7c` | 18 February 2026 |
| SRC-03 Business Case v2 | `c4420b043b4e5db596fb58d37cca1db128f95999f1892fca9257d84b4c21e0ae` | 4 March 2026; counter-signed 6 March 2026 |
| SRC-04 Capital programme schedule (extract) | `a5eb3348ed39615e17504e7424b2c5133f66e26ba1eade160f3d2ed72e83d6af` | none (undated) |
| SRC-05 Programme board notes | `c3caffaf83d000a10361c56df9cb1434c4114fbaf754cc642cf5e26d68f62214` | 12 May 2026 |
| SRC-06 Operations note | `38d742d99c7cbb6338d33a0c69333cb0d02abcc6843dedd0daf0c7ea118a52c8` | 30 June 2026 |


## Candidates

The candidates follow the event times the material evidences. Across all six, **no named individual is
evidenced as holding any decision.** The material names roles (Director of Environment and Place, Head
of Fleet, Head of Property, Finance Business Partner, Section 151 Officer, Portfolio Holder) and two
individuals: Councillor J. Whitfield, who *moved* the Cabinet recommendation, and R. Adeyemi, who
*counter-signed* the business case. A mover is not an owner, and a counter-signature is a different act
(see Unclassified). The owner is missing throughout, and that is the run's main finding.

### brackwell-1 — adoption of the Scheme of Delegation v4

File `brackwell-1.hdc.json` · `event_time_ref: brackwell-C102` (2025-04-01)

**As evidenced:** "Scheme of Delegation — v4 (extract) / Brackwell District Council · adopted
2025-04-01". Paragraphs 3.1–3.3, 5.2 and 5.4 are the binding content.

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported (epistemic `medium`; see challenge 1) | explicit (C101) |
| context | missing | — |
| decision-date | supported (2025-04-01) | explicit (C102) |
| accountable-owner | missing | — |

Also four `consequence` contributions (C103–C106: §3.1, §3.2, §3.3, §5.2 with §5.4). What the evidence
did not supply: who adopted the scheme, in what act, knowing what.

**Admissibility:** 1 ✓ — We decide: adopt v4; This means: the delegations in Parts 3 and 5 bind · 2 no
context ✓ · 3 ✓ · 4 single instrument ✓ · 5 owner and context reported missing ✓ · 6 undetermined · 7
none ✓. **Admissible, incomplete.**

**Challenge:**
1. Decision or instrument? The extract is the instrument, and states its own adoption. The decision
   test names "a policy adopted" as a decision moment, and both grammar lines can be filled, so it is
   raised. An attester may read it as the instrument only, in which case it is authority material and
   not a candidate. The other reading is recorded in `unresolved`.
2. Evidence kind: `act-record`, as "the signed paper" is. The times of the extract's text are `unknown`;
   the adoption date rests on the instrument's own statement.
3. Authority use elsewhere. No other source cites the scheme. None of its paragraphs is attached as
   authority to brackwell-2 to -6, however well they fit; doing so would be inference on a never-inferred
   class.

**Recommendation: incomplete.**

### brackwell-2 — the Fleet and Depot Modernisation programme approved in principle

File `brackwell-2.hdc.json` · `event_time_ref: brackwell-C202` (2026-02-18)

**As evidenced:** "Resolved: 1. That the Fleet and Depot Modernisation programme be approved in
principle." (SRC-02, Item 7).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C201) |
| context | partial: two act-record contributions, `considered: evidenced`, both **indeterminate** | explicit (C204, C205) |
| decision-date | supported (2026-02-18) | **inferred**: normalised from "18 February 2026" (C202) |
| accountable-owner | missing | — |

Also `authority`: Cabinet, recommendation carried 8–3 (C203). What the evidence did not supply: an owner,
and context that can be presented as contemporaneous.

### brackwell-3 — the Director authorised to bring forward individual schemes

File `brackwell-3.hdc.json` · `event_time_ref: brackwell-C302` (2026-02-18)

**As evidenced:** "2. That the Director of Environment and Place be authorised to bring forward
individual schemes within the approved capital programme line."

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C301) |
| context | partial: C304, C305, `considered: evidenced`, both **indeterminate** | explicit |
| decision-date | supported (2026-02-18) | **inferred** (C302) |
| accountable-owner | missing | — |

Also `authority` Cabinet (C303). The "approved capital programme line" is not identified.

### brackwell-4 — a further site-selection report to Cabinet before contracts are let

File `brackwell-4.hdc.json` · `event_time_ref: brackwell-C402` (2026-02-18)

**As evidenced:** "3. That a further report on the depot site selection be brought to Cabinet before
contracts are let." A deferral of site selection that **commits**: no contracts before the report. So it
is a decision, not `non-decision: deferred`.

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C401) |
| context | partial: C405, C406, `considered: evidenced`, both **indeterminate** | explicit |
| decision-date | supported (2026-02-18) | **inferred** (C402) |
| accountable-owner | missing | — |

Also `option-foreclosed`: letting contracts before that report (C404); `authority` Cabinet (C403).

**Contemporaneity, recomputed, for brackwell-2, -3, -4** (literal reading, `historical-recovery.md`):

| Contribution | Span | Capture | Event | Grade |
|---|---|---|---|---|
| C204 / C304 / C405 | "Cabinet considered the report of the Director …" | 2026-02-18 | 2026-02-18 | **indeterminate** |
| C205 / C305 / C406 | "Members noted the scheme affects collection rounds in four wards." | 2026-02-18 | 2026-02-18 | **indeterminate** |

Read as whole-day intervals, a same-day capture does not "end at or before the event begins". Under an
alternative reading (not the standard's), where a same-day capture ends *at* the event, these would be
`contemporaneous`. I report the literal grade; the defect is friction 3.6. So, per criterion 2, these
are reported in `unresolved` and not presented as contemporaneous context.

**Admissibility (all three):** 1 ✓ — each fills We decide / This means (approve in principle; authorise
the Director; no contracts before a further report) · 2 no `later` context; indeterminate reported ✓ · 3
✓ · 4 `explicit-cross-reference` to Item 7's structure ✓ · 5 owner reported missing ✓ · 6 undetermined
· 7 none ✓. **Admissible, incomplete.**

**Challenge (all three)**, most serious first:
1. **One decision or three?** (decision challenge 9). The three resolutions were carried as one
   recommendation on one vote. Each can be accepted, changed or superseded without changing the others
   (tdr.md §3), and reconcile's rule is one question per candidate, so they are split at reconciliation.
   A single candidate is defensible on the same evidence; this is said in each `unresolved`. The
   programme itself — depots *and* fleet — was approved as one thing and is not split further: that
   would shatter a judgement Cabinet made as one.
2. Owner by default (5). Cabinet is a forum. Councillor J. Whitfield moved the recommendation; the
   Director of Environment and Place wrote the report. Neither is thereby the owner. Missing.
3. Hindsight (1). The Business Case v2 (SRC-03, 4 March 2026) post-dates the decision. It is **not
   attached as context**, not even to be graded `later`. The Director's report to Cabinet is not in the
   material.
4. Authority (6). The minute does not cite the instrument Cabinet acted under. SRC-01 §3.2 reserves to
   Cabinet commitments affecting more than one ward, and the minute notes four wards. The fit is close,
   and it is still not a reference. Not contributed.

**Recommendation: incomplete** (each).

### brackwell-5 — Northgate depot retained for vehicle storage

File `brackwell-5.hdc.json` · `event_time_ref: brackwell-C503` (2026-05-12)

**As evidenced:** "The board agreed that the Northgate depot will be **retained for vehicle storage**
rather than closed, with only Southway and Riverside consolidating onto Calder Road." (SRC-05 item 3).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | supported | explicit (C501) |
| context | partial: C506 (highways works behind) act-record, **indeterminate** (same day); C507 (SRC-03 saving) contemporaneous but `considered: unknown`, circumstance only | explicit |
| decision-date | supported (2026-05-12) | **inferred**: normalised (C503) |
| accountable-owner | missing | — |

Also `alternative-rejected`: closing the Northgate depot (C502, explicit, "rather than closed");
`consequence`: "this reduces the expected annual saving", figure not revised (C505); `authority`: the
Fleet and Depot Programme Board (C504).

**Contemporaneity, recomputed:** C506, capture 2026-05-12 against event 2026-05-12: `indeterminate`
(literal). C507, capture 2026-03-04: `contemporaneous`. But nothing shows the business case was before
the board — the notes say "the expected annual saving" and cite no figure and no document — so it is
`considered: unknown`.

**Admissibility:** 1 ✓ (retain Northgate; only two depots consolidate) · 2 ✓ (indeterminate reported) ·
3 ✓ · 4 `explicit-cross-reference` (item 3) and `entity-match` (Calder Road consolidation saving) ✓ · 5
✓ · 6 undetermined · 7 none ✓. **Admissible, incomplete.**

**Challenge**, most serious first:
1. **Authority** (6). The notes do not say under what authority the board agreed. Whether keeping
   Northgate falls within officer delegation (SRC-01 §3.1, §3.3) or is a commitment reserved to Cabinet
   (§3.2) is not evidenced. Asserting either would be inference. Left in `unresolved`.
2. **Supersession or a different decision?** (10). Cabinet considered consolidating *three* depots onto
   Calder Road; the board now consolidates *two*. The notes do not cite Cabinet, and the authority
   lineage is not shown, so no supersession is recorded. Date order alone establishes none.
3. Owner (5). The Director of Environment and Place chaired; chairing is not ownership, and no
   individual is named. Missing.
4. Grouping attack. C507 joins on subject matter only (assembly confidence `medium`); remove it and no
   mandatory role changes.
5. Later material. SRC-06 (30 June) says two rounds run out of Northgate rather than Calder Road. That is
   not context (it is later), and it is not contributed as `challenge` either, because it never refers
   to this decision. It is recorded as a tension below.

**Recommendation: incomplete.**

### brackwell-6 — the temporary Northgate arrangement that stayed

File `brackwell-6.hdc.json` · `event_time_ref: unknown`

**As evidenced:** "the two eastern rounds have been running out of Northgate rather than Calder Road …
This was set up as a temporary measure for April and May … so we have not scheduled a move. Northgate
has been included in the depot maintenance schedule through FY28 on that basis." (SRC-06).

| Mandatory role | State | Derivation |
|---|---|---|
| decision-statement | **partial**: a choice by default ("we have not scheduled a move") with a binding consequence; epistemic `medium` | explicit (C601) |
| context | partial: three contributions, all **indeterminate** (event time unknown) | explicit (C603–C605) |
| decision-date | missing | — |
| accountable-owner | missing | — |

Also `consequence`: Northgate in the depot maintenance schedule through FY28 (C602). `considered`:
`evidenced` for C603 ("because") and C605 ("so"); `unknown` for C604.

**Admissibility:** 1 ✓, but only just — We decide: rounds stay at Northgate; This means: maintenance
committed through FY28 "on that basis" · 2 all context indeterminate, reported ✓ · 3 ✓ · 4 single note
✓ · 5 date and owner reported missing ✓ · 6 undetermined · 7 none ✓. **Admissible, incomplete.**

**Challenge**, most serious first:
1. **Is it a decision?** `decision-identification` names "an incident workaround that silently became
   the way things work" as a decision moment. tdr.md §3 calls execution events evidence, "unless a
   further judgement was actually exercised". The note states the judgement ("so we have not scheduled a
   move") and a commitment made on it. Raised; an attester may reasonably read it as an execution event
   of brackwell-5.
2. **Evidence kind.** Recorded as `act-record`: the only record of the choice, written by those making
   it. Read as `retrospective`, the matrix would let it support occurrence only, and there would be no
   candidate. Contestable either way.
3. Document date as decision date. 30 June 2026 is when the note was written, not when the arrangement
   stopped being temporary or when the maintenance schedule was changed. Event time `unknown`.
4. Owner. "we" is unnamed; the author (Head of Fleet, a role) is not thereby the owner.

**Recommendation: incomplete.**

### Validation (all six)

SCHEMA: `historical-candidate.schema.json` with `schemas/shared/` as registry: pass ×6. STRUCT:
integrity rules 1–5; `event_time_ref` unknown or a `decision-date` contribution; `considered` on every
context contribution and no other; never-inferred roles (`accountable-owner`, `alternative-rejected`,
`authority`) carry `explicit`; roles from the package or vocabulary; `source_hash` and locator reproduce
every fragment's content; no floats: all pass ×6. Not run: TDR schema, recovered-TDR opening,
rendered-value coverage (no drafts, by instruction); review-event binding (none exist).

### Provenance (fragments, by source)

| Fragment | Lines | Evidence kind | Capture · creation | Used in |
|---|---|---|---|---|
| brackwell-S01-F1 … F6 | 1–3, 7–8, 10–11, 13–14, 18–19, 21 | act-record | unknown · unknown | 1 |
| brackwell-S02-F1 … F8 | 1–3, 5, 7–9, 11, 13–15, 16–17, 18, 20 | act-record | 2026-02-18 · unknown | 2, 3, 4 |
| brackwell-S03-F3 | 10–11 | prior-unlinked | 2026-03-04 · unknown | 5 |
| brackwell-S05-F1, F3, F4, F5 | 1–3, 10, 10–12, 14 | act-record | 2026-05-12 · unknown | 5 |
| brackwell-S06-F2 … F5 | 5–6, 8–9, 9–10, 12 | act-record | 2026-06-30 · 2026-06-30 | 6 |

SRC-03's creation time is `unknown`: the document is dated 4 March 2026 but carries a 6 March 2026
counter-signature, so the artefact as read was finished on or after 6 March, on an unstated date.

## What remains unknown

What an attester would have to find:

- **An accountable owner for every candidate.** Named individuals, evidenced as holding each decision.
  The roles named (Director of Environment and Place; Head of Fleet) are leads, not answers.
- **Who adopted the Scheme of Delegation v4, and in what act** (brackwell-1).
- **The Director's report to Cabinet** (brackwell-2 to -4). Business Case v2 is the only version
  supplied, and it post-dates Cabinet.
- **The "approved capital programme line"** in resolution 2. SRC-04 is undated and is not cited.
- **The further site-selection report Cabinet required, and whether contracts have been let**
  (brackwell-4). Not in the material.
- **The authority for the programme board's Northgate decision** (brackwell-5): delegated (§3.1/§3.3)
  or reserved to Cabinet (§3.2)?
- **When the temporary Northgate arrangement became standing, and when Northgate entered the
  maintenance schedule through FY28** (brackwell-6). And who set up the April–May temporary measure: an
  earlier act whose record is not in the material.
- **Finance's revised position for the July board** — not in the material.

## What remains conflicting

No candidate records a conflict: no two contributions to one role disagree. Three tensions *between*
candidates or sources remain unresolved, with what would settle each:

1. **Northgate's use.** brackwell-5 has Northgate "retained for vehicle storage". SRC-06 has two rounds
   operating out of it. *Settled by:* a record of the decision to keep rounds at Northgate, or the July
   board's position.
2. **Three depots or two.** Cabinet considered consolidating three depots onto Calder Road (brackwell-2
   context); the programme board consolidates two (brackwell-5), citing no authority. *Settled by:* the
   further report to Cabinet that resolution 3 requires, or the instrument under which the board acted.
3. **The reconciliation date of the saving** (value-language, not a decision conflict, not used): SRC-03
   §6 "by **31 March 2028**" against SRC-04 CP-114 "**31 March 2027**", and the Finance note "end of FY27".
   *Settled by:* whoever owns the saving's reconciliation date; a value-record recovery should take it up.

## What is not a decision

Spans classified against `decision-contribution.schema.json` v1.0.0; every classification object
validated against it.

| Fragment / span | Lines · offsets | Verbatim | Classification |
|---|---|---|---|
| brackwell-S05-F5 (SRC-05) | 14 · [487, 589) | "The board noted this reduces the expected annual saving but did not revise the figure at this meeting." | `{"taxonomy_version":"1.0.0","class":"non-decision","non_decision":"deferred"}` — **evidence that no decision was made** on revising the saving figure: put off to July with nothing committed. (The same fragment's first clause is brackwell-5's `consequence`.) |
| SRC-05 | 15 · [590, 644) | "Finance to bring a revised position to the July board." | `{"taxonomy_version":"1.0.0","class":"not-a-decision","reason":"action"}` |
| SRC-05 item 5 | 19–21 · [677, 941) | "Collection round completion times … averaged **4% faster** in April … Head of Fleet cautioned … no attribution should be drawn yet." | `{"taxonomy_version":"1.0.0","class":"not-a-decision","reason":"status-update"}` |
| SRC-04 | 11–12 · [476, 614) | "**Note (Finance, undated):** CP-114 benefits are scheduled for reconciliation at the end of FY27 in line with the capital programme cycle." | `{"taxonomy_version":"1.0.0","class":"not-a-decision","reason":"operational-routine"}` — a schedule fixed by the existing programme cycle. |

**No decision evidenced** (silence, not absence):
- **SRC-04's capital lines** (CP-114 £2.10m/£0.40m, CP-118 £0.65m, CP-121 £1.80m/£1.80m). These are
  allocations with reconcile-by dates, but the schedule is undated and records no act approving them.
- **SRC-03's statements of intent** ("The saving will be recognised in the Medium Term Financial Plan
  from FY28"). A paper recommends; no minute in the material decides on the business case.

## Retrospective material set aside

- No source is retrospective about a candidate in the strict sense. SRC-06 is treated as the act-record
  of brackwell-6 (contestable; see that candidate).
- **Later material kept out of context:** SRC-03 (4 March 2026) is later than the Cabinet decision of
  18 February 2026. It corroborates nothing about Cabinet and was not allowed to explain it. SRC-06 is
  later than brackwell-5 and was not allowed to qualify it.
- SRC-06 sentence 3, "This was set up as a temporary measure for April and May", is the only evidence of
  an earlier act (setting up the temporary measure). As later material about that act, it supports only
  that it occurred, so it seeds no candidate of its own.

## Unclassified, and found and not used

**Unclassified.**
- **SRC-03 line 19 · [813, 902):** "Counter-signed for financial purposes: **R. Adeyemi, Section 151
  Officer**, 6 March 2026." *Recognised:* a named individual's dated personal act, of the kind SRC-01
  §5.2/§5.4 requires before a saving above £100,000 is reported. *Why classification failed:* it is
  not a `decision-moment` (it commits no money or time and forecloses no option on its face); not an
  `owner` (it holds no decision in the material); not `authority` for any decision here (nothing cites
  it); not `evidence` considered at a recorded decision; not `corroboration` of one. It concerns a
  claimed saving, which is value-language material. If this pattern recurs — an assurance act on a
  claim — it may need a class.

**Found and not used** (value-language or authority material with no decision role here):
- SRC-03 §4 lines 7–8 (baseline £1.42m, 2025/26, from the finance ledger), lines 13–14 (MTFP from FY28;
  cost centre 4410), lines 16–17 (the falsifying signal: above £1.15m at end FY27); §5 lines 23–24
  (beneficiaries); §6 line 28 (reconcile by 31 March 2028). Only §4 lines 10–11 are used, as
  brackwell-5 context.
- SRC-01 §§3.1–3.3, 5.2, 5.4 as authority for brackwell-2 to -6: not cited by any source, so not used.
- SRC-02 line 20, "Councillor J. Whitfield (Portfolio Holder, Environment) moved the recommendation":
  used only within Cabinet's authority contribution (the vote); not an owner.
- SRC-05 lines 5–6 ("Present:" roles only) and the item heading (line 8): no owner can be drawn from
  them.
- SRC-06 header "Head of Fleet": the author, not the owner.
- SRC-04 "Dependent on CP-118" and "Enabling scheme". CP-118 is named in SRC-05 item 3, but SRC-04 is
  undated and is not cited as a document; not attached as context.

## Coverage

All six sources examined line by line:

- SRC-01 — every line; fragmented in full into brackwell-1.
- SRC-02 — every line; all of it in brackwell-2 to -4.
- SRC-03 — every line; §4 lines 10–11 used; the counter-signature unclassified; the rest found and not
  used.
- SRC-04 — every line; the Finance note classified; the table found and not used.
- SRC-05 — every line; item 3 in brackwell-5 and the findings; item 5 classified.
- SRC-06 — every line; lines 5–12 in brackwell-6. The header (lines 1–3) was examined and not used: the note's date is not the decision date, and its author is not the owner.
