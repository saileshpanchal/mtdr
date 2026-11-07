---
id: DAC-0048
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0048
title: Assure the historical recovery doctrine
status: proposed
disposition: proceed-with-constraints
assessed_at: 2026-11-07
accountable_owner: Sailesh Panchal
review_date: 2027-05-07
confidence: medium
supersedes: none
---

# DAC-0048 — Assure the historical recovery doctrine

> **Proposed. No standing.** Must be accepted before [TDR-0048](TDR-0048-historical-recovery-doctrine.md)
> is. Routed in full because TDR-0048 decides who and what may confer standing on a past decision that
> nobody recorded — authority and delegation are its subject, not its side-effect. Its constraints bind.
>
> **Returned on 7 November 2026 and amended** ([the return](evidence/TDR-0048-0049-owner-return-2026-11-07.md)): the same-day correction carried into
> constraint 3; the trial preserved as evidence ([the trial evidence](evidence/DAC-0048-adopter-trial-2026-11-07/)) and its count reconciled; a further
> independent confirmation recorded as debt. It stays proposed.

## Routing

All seven lenses ran; [assurance synthesis](../records/decision/skills/assurance/assurance-synthesis/)
closes.

| Lens | Why material |
|---|---|
| Systems thinking, counterfactual and evidence, accumulated and resultant risk | always run |
| Fraud and adversarial thinking | the decision governs what an attestation may confer — a manufactured authority is the exploit |
| Customer outcomes | controls are proposed, and people named in historical material are affected by being named |
| Systems dynamics | recovery runs over estates, not documents; behaviour at a thousand candidates is not behaviour at ten |
| Adaptive capacity | the decision deliberately constrains a future change to the record format |

## Uncertainty

**Known:** the substrate already carries everything recovery needs, unchanged; most recovered
candidates will be incomplete (the adopter's corpus assessment, July 2026); the TDR format cannot carry
recovery metadata without a version, and the identity check that would have blocked one is repaired.

**Tested once, and what it showed** ([the trial evidence](evidence/DAC-0048-adopter-trial-2026-11-07/)). An AI agent ran the published recovery
instructions over twelve fictional cases and a six-document corpus on 7 November 2026, without sight of
any expected answer, from the standard at `665aa6e` — and `7b2fb20`, which changed two specification
files it read, landed two minutes into the run. It produced **seventeen** candidates: eleven from the
cases and six from the corpus. Its report opened with *sixteen*, but its own file list and per-run
counts total seventeen; there was one run and one set of files, and the sixteen is a slip in a
sentence. All seventeen meet the suite's own contract at the pin, rechecked independently of the
agent — but in several places only by conventions the standard did not supply. Its friction log found
rules the suite enforced and the specifications did not state, fixtures that broke the doctrine they
illustrate, and a hindsight loophole through the `evidence-*` roles; those were corrected. Four of its
calls diverged from the accepted Brackwell answers, and the owner ruled on them; one correction made in
answer to it — same-day material as contemporaneous — the owner replaced. **Contract conformance is not
historical correctness**, and it was one run, by an agent, over material this repository's author
wrote: it is not the evidence TDR-0049's confirmation asks for, and a further independent confirmation
is required.

**Unknown:** whether reviewers grade the six evidence kinds consistently; whether the four times are
the right granularity for material beyond minutes, papers and transcripts — times carry days, so
material dated the decision's own day is ordered only by evidence that it was before whoever acted; whether any implementation
will consume the contract as published rather than copy and reshape it.

**Assumptions, stated as assumptions:** that an act-record can usually be told from a later-recording
by its content; that implementations keep annotations honest when nothing but challenge checks them;
that a reader of a recovered record reads its banner.

**The finding the case rests on: contemporaneity is computed, but the times it is computed from are
interpretations.** Computing the grade removes an authored grade. It does not remove an authored time,
and a capture time set a month early turns later material into context. Constraint 3 exists for this.

## Systems thinking

**Boundary.** The decision says it changes recovery semantics. The system it touches is wider: the
tools that produce candidates, the people who review them, every later reader of a recovered record,
the graphs and agents that consume candidates above the artefact boundary, and the people named in old
minutes — who are inside the system and absent from the decision's words.

**Where the pressure goes.** The conservative path keeps recovered records rare. That protects
authority inside the standard and **moves the pressure outside it**: a consumer that wants usable
history will be tempted to treat candidates themselves as fact. The standard cannot govern consumers.
What it can do is make the limit travel with the artefact — `standing: none`, `retrospective: true`
and `status: candidate` are constants in every candidate, readable detached.

**Loops.** Reinforcing: more candidates → more requests to attest → attestation as routine → less
scrutiny per attestation. Balancing: the admission test, unchanged, and the refusal to relax it.

**Second-order hypotheses.** (1) Recovered records will be cited as `derived_from` in new decisions
as though they were contemporaneous authority. (2) Personal names recovered as historical owners will
persist in adopters' stores long after the decision has lost relevance. (3) Most context will grade
`indeterminate`, and reviewers will read that as weakness to be fixed rather than as a finding.

## Counterfactual and evidence

**Strongest alternative.** *Define nothing; keep the standard prospective, and let adopters govern
their own recovery.* It keeps the standard small and refuses to lend MTDR's credibility to weaker
material. It fails on the adopter evidence: implementations recover anyway, one has already named the
missing rule as the gate on its own work, and rules invented per implementation are where laundering
happens unobserved — a candidate file moved into a register is the cheapest path, and nothing would
name it a fault.

**Doing nothing.** Candidates stay stranded, and the hindsight rule stays a release note and three
paragraphs in skills, none of it normative and none of it testable.

**Evidence quality.** The adopter's gate predates this decision and was written to govern its own
work — produced to inform. The owner's review of this approach was produced to inform it. The
analysis that prompted the work was produced to argue for change, and is weighed as advocacy. No
external comparative review of recovery practice exists, and none is claimed.

**Falsifiers.** Two reviewers grading the same fragments' evidence kinds disagree on more than one in
five; an implementation consuming the contract finds a recovery case none of the six kinds fits; a
recovered record is cited as current authority within a year. Any of these reopens TDR-0048.

## Accumulated and resultant risk

| | Delta |
|---|---|
| **Increases** | a new surface — recovered TDRs that can be cited as authority — opening only as attestations accumulate, slowly under the conservative path |
| **Decreases** | laundering through ad hoc recovery rules; hindsight entering context unobserved; the stranding of every candidate an adopter produces |
| **Transfers** | interpretation risk to the implementations that produce candidates, and to the reviewers who attest them |
| **Unknown** | reviewer consistency; consumer behaviour above the boundary |

**Declared interactions.**
- **[TDR-0027](TDR-0027-human-ratification-confers-standing.md)** — an attestation is a ratification
  of an account, and inherits its evidence requirement. Review events are checked structurally only.
- **[TDR-0046](TDR-0046-oir-experiment-preregistration.md)** — the Operational Inheritance Record
  experiment's corpus is hash-frozen, and its independent-source control makes any reconstruction
  that populates other records from it inadmissible. Decision recovery run over that corpus would
  contaminate the experiment. Constraint 7.
- **[TDR-0043](TDR-0043-version-bound-detached-records.md)** — the repaired identity check is what
  keeps a future recovered-record provision possible. Nothing here relies on using it.

**Resultant position:** stabilising, provided constraints 3 and 6 hold. Deteriorating if recovered
records begin to be cited as authority.

## Adversarial projection

- **Retrospective cover.** An organisation recovers a decision to legitimise an action already taken —
  *we always decided this* — and uses the attestation as the paper trail. Mitigated: an attestation is
  scoped to the account, `governs` is always false, the record carries its recovery in its opening,
  and every claim traces to a contemporaneous span. Residual: an attested account cited in a dispute
  as if it had been recorded at the time. Owned by the record's attester.
- **Backdating.** A capture time set early makes later material contemporaneous. The computation is
  faithful to whatever time it is given. Mitigated only by constraint 3. Its quietest form — material
  written after the meeting but dated its day — is closed by the same-day correction: a shared date
  orders nothing.
- **Self-attestation.** The person who assembled a candidate attests it. Nothing in an event records
  whether the reviewer produced the candidate. Not mitigated; a learning obligation.
- **Re-emission.** A candidate re-issued under the same identifier with different content. Mitigated:
  review binds to the digest, so the new content is unreviewed.
- **Corroboration by copying.** Three restatements of one paper presented as three sources. Mitigated:
  restatements name what they restate, and independence counts once.
- **The consuming agent.** An agent reading candidates as organisational fact, and acting on an
  authority nobody held. Outside the standard's reach; mitigated only by the constants travelling.

## Customer-outcome projection

Indirect for customers: a recovered decision acted on as current authority affects whoever that
decision governs, without an accountable owner who chose to apply it now. The three-way separation is
the control.

**Direct for the people named.** Recovering an evidenced historical owner records an individual as
accountable for a decision years after the fact, often after they have left, and without their
participation. The rule that the attester is never the owner protects the attester from false
accountability; it does nothing for the owner. A named historical owner must be able to contest the
account, and a contested account is superseded, not argued in the margin. Constraint 6. A kept
candidate also holds those names; the profile says that keeping one is the adopter's processing, under
the adopter's obligations.

## Control side-effects

- **Rarity drives work around the standard.** Conservative admission makes recovered records rare;
  adopters wanting usable history may stop at candidates and treat them as records in their own tools.
  Watched by the monitoring contract, not preventable here.
- **Indeterminacy reads as weakness.** Partial dates make most context `indeterminate`, and a reviewer
  under pressure may "fix" a date to clear it. That is the backdating attack, made by someone well
  intentioned. Constraint 3 again.
- **Annotation burden.** Every fragment and context contribution carries annotations. Implementations
  will default them. A defaulted `considered: evidenced` is caught by schema; a defaulted
  `evidence_kind` is not.

## Systems dynamics

**At scale.** An estate yields thousands of candidates and a handful of reviewers. Review saturates
first, and the balancing loop — careful attestation — is the one that vanishes under load.

**Tipping point.** Attestation becomes signature: events per reviewer per day rising while time spent
per candidate falls. Beyond it, attestations confer an account nobody read.

**Equilibrium.** Most candidates unreviewed indefinitely. The doctrine accepts that as a legitimate
terminal state; the risk is consumers using them anyway.

**Velocity.** A wrongly attested account propagates into graphs and agents in hours; supersession takes
a named individual and a record. Detection is slower than propagation, and the constraints are
therefore preventive, not detective.

## Adaptive capacity

Reversible at low cost: every change is additive, the record format is unchanged, and the
specifications are proposed and travel with this case. The mind-changing evidence is named under
*Counterfactual*. Dissent is retained: TDR-0048's alternatives include defining nothing, and its third
alternative keeps a recovered-record provision open.

**Execution capability.** One maintainer; no independent human reviewer of recovery practice; one
agent trial over self-authored fixtures; no
implementation yet consuming the contract. The case is proportionate to a doctrine that has not yet met
an adopter, and its review date is set for that reason.

## Contradictions, and how each is handled

1. **Conservative admission protects authority inside the standard and pushes it outside.** Constrained:
   the limit is a constant in the artefact, and consumer behaviour is monitored.
2. **A computed grade, from authored times.** Constrained: constraint 3.
3. **Accountability for the named owner against fairness to someone who cannot reply.** Constrained:
   constraint 6.
4. **Structural checks on review events against TDR-0027's refusal to let technical state confer
   standing.** Resolved: the checks say what they are, and never claim an act occurred.

## Decision debt

| Item | Owner | By |
|---|---|---|
| The decision package's instance of the evidence matrix and its never-inferred roles | Sailesh Panchal | with TDR-0049, before this case is accepted |
| Fixtures testing constraint 3 — a capture time not evidenced by its fragment or source is `unknown` | Sailesh Panchal | with TDR-0049 |
| A two-reviewer grading of evidence kinds over a sample, to test consistency | Sailesh Panchal | before TDR-0048 is confirmed |
| An independent reviewer of the doctrine, who is not its author | Sailesh Panchal | before confirmation |
| A further independent confirmation of decision recovery, by an adopter who is not the drafter, over material the drafter did not write | Sailesh Panchal | before TDR-0049's confirmation gate is met |
| Order within a day: times carry no time of day, so same-day material is ordered only by evidence of consideration — kept deliberately, not broadened in this increment | Sailesh Panchal | revisit on a demonstrated need |

## Monitoring contract

| Hypothesis | Observable | Threshold |
|---|---|---|
| Recovered records cited as current authority | recovered TDRs named in a later record's `derived_from` with no confirming prospective record | any one reopens this case |
| Inference supplying owners or authority | validation failures on never-inferred roles in published candidates | any |
| The contract copied, not consumed | an implementation pinning an MTDR commit and validating against the published schemas | none within a year is a failure of TDR-0048 |
| Reviewers disagreeing on evidence kinds | agreement between two reviewers on a sample | below four in five |
| Attestation fatigue | attestations per reviewer per day, and time from candidate to attestation | review if attestations outpace any plausible reading time |

## Learning obligations

Whether reviewers produce the candidates they attest, and whether that matters. Whether the six
evidence kinds survive their first non-minute corpus. Whether naming historical owners provokes
contest, and how contests are resolved.

## Constraints

Proceed only with these.

1. **TDR-0048 is not accepted before this case is.**
2. **Nothing reaches `main` while TDR-0048 is proposed.** Its specification text travels with it.
3. **A time is the fragment's own statement or its source's recorded metadata, or it is `unknown`.**
   Any other basis — a folder, a filename, a neighbouring document, a reviewer's knowledge — makes it
   `unknown`. Challenge tests every time against its fragment. **A shared date is not an order:**
   material dated the decision's own day is contemporaneous only where it is shown to have been before
   whoever acted.
4. **No skill writes a review event or a disposition.** Enforced: the candidate is closed against
   both, and the pipeline specification emits none.
5. **No attestation establishes current authority.** Enforced: `governs` is always false. Stated: a
   governing decision takes its own prospective record.
6. **A recovered record opens with its recovery, names its historical owner as evidenced, and is open
   to contest.** A contest by a named historical owner is answered by supersession.
7. **Recovery never runs over the OIR experiment's frozen corpus**, and no trial of recovery in this
   repository runs over real client material.
8. **At review, count the attestations, and look for recovered records cited as authority.** Any such
   citation without a confirming prospective record reopens this case.

## Review

On the monitoring contract's evidence, or 2027-05-07. The trigger that reopens it earlier is the first
recovered record cited as current authority.
