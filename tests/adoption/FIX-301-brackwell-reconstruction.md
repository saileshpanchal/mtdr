# FIX-301 — reconstructing the Brackwell framework

**Contract expectation:** accepted

The adoption acceptance case. Six documents of ordinary local-government material
([`brackwell/`](brackwell/)) go in; what should come out is stated here. Its purpose is to prove three
things at once:

1. someone outside this project can apply MTDR **without any knowledge of a private estate**;
2. the framework can be reconstructed from **public MTDR material alone**;
3. [`show-me`](../../skills/shared/show-me/) can trace each resulting claim back through contributions
   and fragments to Brackwell source text — rather than generating an explanation after the fact.

Counts are ranges where span boundaries are a judgement. What is *not* a range is the list below of
things that must not happen.

**Amended 7 November 2026 on the owner's rulings**
([the return](../../decisions/evidence/TDR-0048-0049-owner-return-2026-11-07.md)): D1's authority is
recorded as applicability, not invocation; D1 is one composite candidate with three traceable
resolutions; SRC-06 is persistence, not a decision; and the scheme's own adoption is assessed rather
than passed over. These answers are proposed with
[TDR-0049](../../decisions/TDR-0049-decision-recovery-vocabulary.md) and take effect with it.

## Expected — decisions and findings

**D1 · Depot consolidation approved in principle.** From SRC-02. A consequential decision: the service
footprint across four wards changes, and money follows.

- **`accountable_owner` is missing, and that is the finding.** The sources offer a committee (Cabinet),
  a role (Director of Environment and Place, SRC-01 §3.3) and a mover (Councillor J. Whitfield). None
  of those is a named individual accepting accountability. The gap is reported, with what would close
  it.
- `decision_date` 2026-02-18, explicit.
- **One composite candidate.** Cabinet passed three resolutions on one motion, carried 8–3: one
  authoritative act, so one candidate. Each resolution stays individually traceable — its own span
  and its own `consequence` contribution: approval in principle (res. 1), the Director's authority to
  bring forward schemes within the capital line (res. 2), and a further report on site selection
  before contracts are let (res. 3). D2 later narrows what res. 1 approved and leaves res. 2 and 3
  untouched — which is why they are kept apart.
- **Authority: applicability, not invocation.** SRC-01 §3.2 reserves any commitment altering the
  service footprint in more than one ward to Cabinet, and the minute records that the scheme affects
  four wards: the instrument applies, and the body that acted is the body it names. That is an
  `applicability` finding, reported beside D1. The minute does not cite the scheme, so **no authority
  contribution is recorded**, and nothing says Cabinet relied on it. Neither finding is a judgement
  that the approval was competent.

**D2 · Northgate retained; consolidation narrowed to two depots.** From SRC-05.

- A decision, though the board recorded it as a note. It changes what was committed to.
- **It supersedes part of D1's scope**, and the supersession is stated rather than the earlier record
  edited.
- **An authority question is recorded, not adjudicated**: SRC-01 §3.2 applies — a footprint change
  across more than one ward — and names Cabinet, while the act was the programme board's. The
  `applicability` finding states that mismatch and the evidence for it; the board's notes cite no
  authority, so none is recorded. Whether the board acted within its powers is Brackwell's question,
  not the standard's.

**SRC-06 · Persistence, not a decision to make it permanent.** The two eastern rounds still run from
Northgate on 30 June, past the April–May period the temporary measure was set up for, and no move is
scheduled.

- **A `persistence` finding** — behaviour observed at the note's date — with its **authority for
  continuation flagged `not-evidenced`**. Nothing in the set authorises the arrangement beyond May, and
  nothing records who set up the temporary measure.
- **No decision to make the arrangement permanent is recovered.** Continued operation, stable rounds,
  crew preference and the absence of a scheduled move do not establish one. They travel with the
  finding as the note's account of why nothing moved; crew preference is not authority.
- **The FY28 maintenance inclusion is reported, not recovered.** The note says Northgate *has been
  included* in the depot maintenance schedule through FY28 — an account, after the fact, of a
  commitment of money whose act is not in the set. It evidences that a commitment occurred. Its act,
  date, owner and authority are missing, and a candidate for it needs the record of the commitment.

**SRC-01 · The scheme's own adoption — assessed, not passed over.** The extract states its own adoption
date, 2025-04-01, which is a basis for the time, and it is **not set aside because the only evidence of
the adoption is the instrument itself**. A candidate needs authentication and evidence of effect as
well. In this set nothing authenticates the extract — no adopting resolution, signature, seal or
register entry — and no later act relies on it by citation: Cabinet's reservation and the Section 151
counter-signature are consistent with its terms, and cite nothing. **No candidate**: the adoption is
reported with the condition met (contemporaneity) and the evidence that would establish the other two.

## Expected — value

**V1 · One Operational Value Commitment**, assembled across SRC-01 to SRC-05.

| Role | Value | From |
|---|---|---|
| Beneficiary | The General Fund, and thereby Brackwell council taxpayers | SRC-03 §5 |
| Baseline | £1.42m annual depot running cost, 2025/26, from the FY26 revenue outturn, cost centres 4410–4412 | SRC-03 §4 |
| Target | £0.98m by 2027/28 — a £440,000 annual saving | SRC-03 §4 |
| Recognition | Medium Term Financial Plan from FY28; visible in cost centre 4410 | SRC-03 §4 |
| Falsifying signal | Combined running costs above £1.15m at the end of FY27 | SRC-03 §4 |
| Finance counter-signatory | R. Adeyemi, Section 151 Officer | SRC-03, and required by SRC-01 §5.2 above £100k |
| `committed_by` | Director of Environment and Place — **a role, not a named individual** | SRC-02 res. 2 with SRC-01 §3.3 |
| `reconcile_by` | **Conflicting**: 31 March 2028 and 31 March 2027 | SRC-03 §6 · SRC-04 |

- **`status: candidate`.** Nothing in the material is an act of ratification, and no skill may supply
  one.
- **The £440,000 figure is reported with its currency in question.** SRC-05 states that retaining
  Northgate reduces the expected saving and that the figure *was not revised*. The candidate carries
  £440,000 because that is what the evidence says, together with the finding that the organisation has
  recorded a reason to doubt it and has not acted on it. That finding is more useful than a corrected
  number would be.
- **The 4% improvement is an observation, not an attribution.** SRC-05 records the measurement and the
  caution against drawing attribution from it, and both travel.

## Expected — `show-me`

| Field | State | Because |
|---|---|---|
| `beneficiary` | `supported` | Stated plainly in SRC-03 §5 |
| `finance_countersignatory` | `supported` | Named and dated in SRC-03 |
| baseline | `supported` | Figure, year, method and cost centres all in SRC-03 §4 |
| `committed_by` | `inferred` | SRC-02 authorises the role; SRC-01 §3.3 makes it the committing officer. Two documents, one inference |
| `reconcile_by` | `conflicting` | SRC-03 and SRC-04 disagree, with the recorded conflict named |
| D1 `accountable_owner` | `missing` | Declared absent, not filled |

No field should come back `unsupported`. If one does, something was rendered that the sources do not
carry, and that is the most important thing the exercise could tell you.

## Must not

- **Name an individual as D1's accountable owner.** Not the mover, not the report author, not the
  Director. A committee decided; the gap is the finding, and inventing an owner is the most
  consequential error available here.
- **Resolve the `reconcile_by` conflict.** Not by recency, not by the business case outranking a
  schedule, not by averaging, and not by splitting the commitment in two to make the conflict
  disappear. Neither source cites the other and neither is the approval.
- **Revise the £440,000 saving** to account for Northgate being retained. SRC-05 says the figure was
  not revised; recomputing it would replace an organisational fact with an interpreter's arithmetic.
- **Draw attribution from the 4% figure**, or drop it because attribution is unavailable. It is
  evidence of an observation and travels as one.
- **Recover a decision to make the eastern rounds permanent** from continued operation, crew
  preference or the maintenance schedule. Persistence is observed behaviour; its authority for
  continuation is flagged, not supplied.
- **Report SRC-06 as silent.** It evidences persistence, and that a maintenance commitment was made.
- **Record SRC-01 §3.2 as D1's authority.** The minute does not cite it. Record the applicability,
  beside D1.
- **Split D1's resolutions into three candidates**, or fold them into one undivided statement. One
  vote, one candidate, three traceable resolutions.
- **Set aside the scheme's adoption solely because its only evidence is the scheme**, or draft a
  candidate for it without stating the evidence of authentication and effect.
- **Adjudicate the D2 authority question.** Record the delegation, the act and the tension. Deciding
  whether the board had the power is Brackwell's judgement.
- **Date the maintenance commitment from the note.** 30 June is when the commitment was reported, not
  when it was made.
- **Add local-government semantics to the standard.** No ward, delegation, portfolio-holder or
  Section-151 role may become a field, an enum value or a semantic role. If reconstruction seems to
  need one, the finding is that the *record package* is missing something general — and it goes through
  the language admission test ([TDR-0017](../../decisions/TDR-0017-language-admission-test.md)), not
  into a patch.
- **Require anything private.** Nothing here needs TIM, DTA or any private material. If a step seems
  to, that is a defect in the public distribution rather than a gap in the reader.
