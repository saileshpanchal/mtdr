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

## Expected — decisions

**D1 · Depot consolidation approved in principle.** From SRC-02. A consequential decision: the service
footprint across four wards changes, and money follows.

- **`accountable_owner` is missing, and that is the finding.** The sources offer a committee (Cabinet),
  a role (Director of Environment and Place, SRC-01 §3.3) and a mover (Councillor J. Whitfield). None
  of those is a named individual accepting accountability. The gap is reported, with what would close
  it.
- `decision_date` 2026-02-18, explicit.
- Authority traces to SRC-01 §3.2 — above-threshold and multi-ward, therefore reserved to Cabinet — so
  the approval is competent. That is a *relational* finding about authority, not a judgement about the
  decision's merits.

**D2 · Northgate retained; consolidation narrowed to two depots.** From SRC-05.

- A decision, though the board recorded it as a note. It changes what was committed to.
- **It supersedes part of D1's scope**, and the supersession is stated rather than the earlier record
  edited.
- **An authority question is recorded, not adjudicated**: SRC-01 §3.2 reserves footprint changes across
  more than one ward to Cabinet, and this was taken at a programme board. MTDR records the tension and
  the evidence for it; whether the board acted within its powers is Brackwell's question, not the
  standard's.

**D3 · Eastern rounds run permanently from Northgate.** From SRC-06. A decision nobody wrote down as
one: a temporary arrangement whose stated trigger passed, which the organisation has since committed
maintenance budget to through FY28.

- `decision_date` is **unknown and bounded** — after the September slip was known, before the FY28
  maintenance schedule was set. The fuzziness is the honest value.
- Crew preference is context, not authority.

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
- **Report SRC-06 as "no decision present".** The organisation has committed maintenance budget through
  FY28; that is a decision whatever the document calls itself.
- **Adjudicate the D2 authority question.** Record the delegation, the act and the tension. Deciding
  whether the board had the power is Brackwell's judgement.
- **Invent a decision date for D3** from any single document's date.
- **Add local-government semantics to the standard.** No ward, delegation, portfolio-holder or
  Section-151 role may become a field, an enum value or a semantic role. If reconstruction seems to
  need one, the finding is that the *record package* is missing something general — and it goes through
  the language admission test ([TDR-0017](../../decisions/TDR-0017-language-admission-test.md)), not
  into a patch.
- **Require anything private.** Nothing here needs TIM, DTA or any private material. If a step seems
  to, that is a defect in the public distribution rather than a gap in the reader.
