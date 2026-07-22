# The practice operating model

How a decision record set becomes organisational memory, and how that memory connects to the controls,
evidence and attestations that govern an organisation. This is practice guidance, not normative text — it
draws on boundaries the [specifications](../spec.md) already define, and every layer beyond the record set
is optional (see [ARCHITECTURE.md](../ARCHITECTURE.md)).

## Read the source before you record it

A governing document is dense with different kinds of statement. Classify before you record:

| Source | Is a collection of | Becomes |
|---|---|---|
| **Internal policy** | organisational decisions | records — a clause that sets a limit, a charge, an eligibility rule or an approval threshold is a genuine decision, not merely evidence that a policy was adopted |
| **Regulation / external rule** | obligations and judgement points | cited constraints and evidence; the organisation's interpretation and response are the records |
| **Process / system** | implementation | how decisions are carried out; mapped, not recorded as decisions |
| **Control / management information** | evidence | whether the implementation operated as intended |
| **Contract** | delegated behaviour | third-party obligations, monitored and evidenced |

Only an organisational judgement becomes a record. External requirements keep their own provenance and
become constraints or evidence a record cites. Making a *current* policy's decisions explicit is not the
retro-mining the [identification skill](../skills/decision-identification/SKILL.md) warns against: a policy
in force is the organisation's present position, not an old debate to reconstruct.

## The two loops

**Inner loop — authoring.** A person, an assistant and a named owner: identify, draft, review, challenge,
confirm, save. While a record set is small, link related decisions by hand; once it is connected and tested
(below), searching it before drafting becomes routine.

**Outer loop — stewardship.** Two mechanisms, deliberately kept apart:

- **Deterministic validation — code, not an assistant.** Binary conditions: schema and frontmatter
  validity, duplicate IDs, missing or invalid owners, broken lineage references, invalid status
  transitions, overdue review dates, filename/ID disagreement, references to records that do not exist. An
  LLM adds risk here without adding value. Output: a scheduled health report.
- **Semantic curation — one assistant, propose-never-mutate.** Likely duplicates, contradictions, implied
  supersessions, decisions resting on assumptions that have since changed, and gaps where a material
  decision was never recorded. Output: a proposal queue a human works. It never writes to the record set.

**Immutability and discovered relationships.** Accepted records are never edited. A new decision may point
backwards; a changed judgement becomes a superseding record; a relationship discovered later *between two
existing records* is recorded in a separate, human-confirmed **relationship index**, not written into either
record. Note that a discovered contradiction has nowhere to live *inside* a record in any case: the
lineage fields are [`supersedes`, `derived_from` and `confirmed_by_outcome`](../spec.md#6-lineage) — there is
no `contradicts` field. Contradiction is a review finding and an index entry, never record frontmatter.

## The assurance chain

Records connect outward to how decisions are implemented and evidenced:

> external obligation → decision → implementation → control → operating evidence → (third-party evidence) →
> a named person's attestation

Each link has one meaning: the **record** captures what was decided and why; the **control mapping** shows
how it is meant to be implemented; the **evidence** shows whether it operated as intended; the **named
owner** reaches the conclusion. A contract clause is not evidence a supplier complied with it — that needs
the clause, the accountable owner, the control, the supplier's management information, assurance evidence
and any exceptions.

**The line that protects everyone:** the tooling compiles evidence and surfaces gaps; it never makes the
attestation. Neither a record nor an assurance case proves the organisation is compliant — an
[assurance case](../spec-decision-assurance.md#1-what-a-dac-is-not) demonstrates systematic challenge, not
correctness, safety, approval or compliance. A "conforms" status is a proposed reading a named owner
confirms, never an assurance the tool issues.

## Turn on search by coverage, not by count

Do not wait for an arbitrary number of records. A bounded set of thirty to fifty well-formed decisions that
share a domain, an owner and a source set will retrieve reliably, while hundreds of unrelated records may
not. Turn on corpus review once a coherent set exists **and** known-answer tests (see
[administration and assurance](administration-and-assurance.md)) show the assistant retrieves its decisions
reliably. Measure readiness by coverage of the chosen scope, provenance, owner confirmation, and known-item
retrieval — not by volume.

## Optional: organise related records as a collection

For a policy or domain, a lightweight **collection** — an owned, versioned view that lists the records,
the obligations they cite, the interlocking policies, the controls and the third-party dependencies — gives
an assistant a bounded retrieval context (search the collection first, then its neighbours, then the wider
set). A collection is a *view over records*, never a new record type, and it is an implementation choice
beneath the standard, like the graph.

## Measuring it

Measure decision quality and traceability, not record counts. Baseline what you can actually measure before
you start — time spent reconstructing past intent, decisions without an explicit owner, controls without
clear decision lineage, conflicts found late — and measure the same afterwards. Follow the Value Record's
rule: no baseline, no claim. The leading signs of success are fewer repeated debates, faster governance
papers, clearer traceability from risk and control back to decision, earlier detection of conflicting
assumptions, and confidence that a consequential decision can still be explained years later.

## Govern your own adoption

Adopting this practice is itself a consequential decision. Record it the way the standard prescribes: a
[TDR](../spec.md) for the decision to proceed, a [DAC](../spec-decision-assurance.md) for the consequences
and safeguards, and a [Value Record](../spec-value-record.md) for the expected benefit with a measured
baseline. An organisation that governs its own use of the discipline the way it asks the discipline to
govern everything else has already demonstrated the point.
