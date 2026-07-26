# Transformation Decision Record (TDR) — Specification

**Version:** 1.10.0 · **Licence:** MIT · **Author:** Sailesh Panchal

**TDR** is the standard: the record, its fields, and its accountability semantics.
**MTDR** — Markdown Transformation Decision Record — is the markdown reference format of TDRs described in this repository, as MADR is to ADR.

The TDR has two sibling records: the **Value Record (VR)** — the TDR records the decision; the VR records the value case and its life ([`spec-value-record.md`](spec-value-record.md)) — and the **Decision Assurance Case (DAC)** — a TDR preserves the judgement, it does not prove the consequences are acceptable; the DAC records the reasoning that challenges those consequences ([`spec-decision-assurance.md`](spec-decision-assurance.md)). For what a TDR is *not* — consent receipts, identity claims, runtime logs, model traces — see the [boundary FAQ](FAQ.md).

---

## 1. Purpose

A TDR answers accountability questions, not engineering questions:

> **What was known at the time, by whom, and with what confidence?**

Organisations record the outcomes of decisions. Very few record the judgement — the context, evidence, alternatives, and accountability that produced the outcome. That judgement is lost when people move on, and the organisation pays for it by re-making decided questions at full cost, without the original evidence.

A TDR preserves the judgement, at the moment it is exercised.

## 2. Relationship to existing standards and tools

TDRs work **alongside** existing practice, not instead of it:

- **ADR / MADR.** TDRs extend the Architecture Decision Record lineage (Michael Nygard, 2011) with gratitude. MADR 3.0 already generalised *scope* to any decision; the TDR's contribution is **accountability semantics** — a named accountable owner, stated confidence, evidence completeness, foreclosed options, and decision lineage. A TDR may cite an ADR as its architecture evidence.
- **Enterprise tools.** SAP LeanIX Architecture Decisions, Confluence pages, GRC platforms and PMO records remain where they are. A TDR references them as evidence locations; it does not replace them.

## 3. When to write a TDR — the proportionality rule

Not every decision deserves a record. The test is **reversibility**:

| Decision type | Template |
|---|---|
| Irreversible or costly to reverse (a one-way door) | **Full** |
| Significant, but revisable at tolerable cost | **Minimal** |
| Reversible, conventional, low-stakes | **Bare** — or no record at all |

If reversing the decision would cost less than writing the record, do not write the record. Nobody needs a decision record for choosing the coffee machine — and pretending otherwise turns an accountability instrument into box-ticking.

## 4. Record structure

A TDR is a single markdown file: YAML frontmatter for machine-readable fields, markdown body for human judgement.

### 4.1 Frontmatter fields

| Field | Required | Values / format |
|---|---|---|
| `id` | Yes | `TDR-nnnn`, unique within the owning organisation or repository |
| `title` | Yes | Imperative or declarative statement of the decision |
| `status` | Yes | `proposed` \| `accepted` \| `superseded` \| `rejected` |
| `template` | Yes | `full` \| `minimal` \| `bare` |
| `decision_date` | Yes | ISO 8601 (`YYYY-MM-DD`) |
| `accountable_owner` | Yes | **A named individual.** A committee cannot exercise judgement; it can only endorse it. |
| `confidence` | Full, Minimal | `low` \| `medium` \| `high` — the owner's stated confidence at decision time |
| `maturity` | Optional | `proposed` \| `adopted` \| `validated` |
| `supersedes` | Yes | `TDR-nnnn` (one or more) or `none` |
| `derived_from` | Yes | `TDR-nnnn` (one or more) or `none` |
| `confirmed_by_outcome` | Full, Minimal | `pending — <review trigger>`, or a date plus evidence reference, or `none` |

A JSON Schema for these frontmatter fields is provided at [`schema/tdr.schema.json`](schema/tdr.schema.json) — see [TDR-0006](decisions/TDR-0006-json-schema-for-frontmatter.md). It validates the frontmatter only; the body below is human judgement and is deliberately unconstrained.

An optional authoring lens for these fields — a natural-language grammar that compiles into them — is offered in [`practice/decision-grammar.md`](practice/decision-grammar.md). It is a candidate aid, not part of the normative format.

### 4.2 Body sections

**Full template:**

1. **Context — what was known at the time.** Facts, unknowns, assumptions, constraints, and time pressure as they stood at the decision. Written in the present tense of the decision, never reconstructed.
2. **Decision.** What was decided, stated plainly.
3. **Evidence.** Assessed across the seven dimensions (§5).
4. **Alternatives rejected.** Each with the reason for rejection. "Do nothing" counts as an alternative.
5. **Options foreclosed.** The futures this decision closes off, stated honestly — including foreclosures accepted deliberately.
6. **Consequences and review.** What success looks like, and when `confirmed_by_outcome` will be tested.

**Minimal template:** Context, Decision, Alternatives rejected, Options foreclosed, Review.

**Bare template:** Decision, Why, Reversible (how, and at what cost).

### 4.3 Adopter extensions — the `x-` namespace

Organisations carry data the standard deliberately does not define: a sensitivity classification in their own
scheme, a legal entity, an effective date, a local register key. Frontmatter fields prefixed `x-` are
permitted and ignored by the standard — `x-acme-classification`, `x-acme-effective-from`. The
standard defines no vocabulary and no meaning for them, and no adopter should expect them to be portable to
another organisation.

Two rules keep the namespace honest. Core field names remain closed, so a misspelling (`desicion_date`) still
fails validation rather than passing as an extension. And an extension that proves broadly useful should be
proposed for the core by a superseding TDR, with the adopter evidence that justifies it — the namespace is an
evidence pipeline, not a permanent annexe. See [TDR-0015](decisions/TDR-0015-visibility-and-effectiveness.md).

**The extension contract.** Name extensions `x-<owner>-<field>` — `x-acme-classification`, not
`x-classification` — so two organisations' extensions cannot collide in a shared or merged register. A tool
that round-trips records should preserve `x-` fields it does not recognise rather than dropping them, and a
reader that meets an unknown extension should ignore it, never reject the record. One caution deserves
stating plainly: **schema validity implies nothing about security.** A record can validate perfectly while
carrying a classification that nothing in its environment enforces.

### 4.4 Four kinds of scope

"Scope" carries four distinct meanings in a decision record, and conflating them is a common and consequential
error:

| Scope | Asks | Where it lives |
|---|---|---|
| **Applicability** | Where, and to whom, does this decision bind? | The Decision and Context prose — the grammar's *Unless* clause |
| **Authority** | Under what authority was it made — and who may exercise, delegate or except it? | The authority named in Context — the grammar's *Under* clause. `accountable_owner` names who owns the **judgement**; it does not by itself say who may exercise, delegate, suspend or grant an exception to the decision. |
| **Visibility** | Who may know this decision exists, read it, read its reasoning, or reach its evidence? | **Not a property of the record** — see §10 |
| **Impact** | What does this decision affect — capabilities, controls, customers, other decisions? | Options foreclosed, lineage, and the assurance case |

An exception ("*unless* the incident authority extends the window") is an applicability boundary, not a
visibility rule. A restricted decision is not a narrowly-applicable one. Keeping the four apart is what lets a
reader answer "does this bind me?" separately from "may I see it?".

## 5. The seven evidence dimensions

Evidence in a full TDR is assessed across seven dimensions. For each, the record states what evidence was considered and where it lives — or declares the dimension **not material to this decision**, with a one-line justification. An honest "not material" is worth more than padded prose; a silent omission is worth less than either.

| Dimension | Asks |
|---|---|
| **Business** | What commercial or strategic evidence supported this? |
| **Architecture** | What system, structural or technical evidence applied? |
| **Regulatory** | What obligations, guidance or supervisory expectations were in scope? |
| **Operations** | What did running the organisation day-to-day contribute? |
| **Customer** | What did we know about the effect on customers or members? |
| **Data** | What data supported or constrained the decision, and how good was it? |
| **External** | What market, supplier, peer or research evidence was used? |

## 6. Lineage

Three fields make flat markdown graph-ready without requiring any graph tooling:

- `supersedes` — this record replaces a prior decision. The prior record's `status` becomes `superseded`; its content is never edited.
- `derived_from` — this decision follows from, or was made possible by, a prior one.
- `confirmed_by_outcome` — the honesty field. At the stated review point, the record is updated with evidence that the decision worked, or an honest account that it did not.

Any tool can later assemble records into a connected decision history. No tool is required to.

## 7. Status and lifecycle

- Records are **never edited or deleted once accepted**. They are **superseded**.
- **Status transitions** (`proposed → accepted`, `proposed → rejected`, `accepted → superseded`) and `confirmed_by_outcome` updates are made in place — they are lifecycle facts, not changes of judgement. A record `rejected` at proposal was never accepted, so nothing is superseded; it stays as evidence that the question was asked and answered.
- **Changes to decision content require a superseding TDR** stating what is now known that was not known at the time.

This is what makes a body of TDRs organisational memory rather than documentation: the reasoning trail survives its own corrections.

## 8. Regulatory framing — worked examples, not dependencies

The TDR is regulator-neutral. Two UK financial services regimes illustrate the test it is built to answer:

- **SM&CR "reasonable steps".** Accountability attaches to a *named* Senior Manager. When asked to demonstrate reasonable steps, that individual needs evidence of judgement exercised at the time — not a policy document, and not fragments reconstructed from a shared drive. A full TDR is that evidence.
- **Consumer Duty.** Firms must evidence that customer outcomes were considered in significant decisions. The customer evidence dimension makes that consideration explicit — or its absence visible — at decision time.

Organisations outside financial services, and outside the UK, will recognise the shape of the same test from their own boards, auditors and supervisors.

## 9. Versioning

This specification follows semantic versioning. Additive field changes are minor versions. Removal or weakening of the accountability core (named owner, time-of-decision context, confidence, evidence, foreclosure, lineage) would constitute a different standard, not a new version — see [TDR-0002](decisions/TDR-0002-differentiate-on-accountability-semantics.md).

## 10. What this format does not conceal

This standard specifies how decisions are **captured**. What is subsequently done with a body of records — who may see which of them, how a view is assembled and authorised, how any of it is enforced when people and machines use it — belongs to the systems an adopter builds above the register. This section states only what the format itself does and does not do.

**A record does not enforce its own visibility.** Enforcement belongs to whatever stores, queries and projects the records; markdown carries no access semantics and cannot acquire any. A classification label is *metadata for an enforcement layer to act on* — legitimate and often useful, but a claim rather than a control. A record marked restricted, sitting where it can be read, advertises rather than protects.

A lineage-connected register discloses more than its readable contents:

- **Sequential identifiers disclose gaps.** A reader who sees TDR-0041 and TDR-0043 knows TDR-0042 exists.
- **Lineage fields disclose existence and subject.** `supersedes: TDR-0042` reveals that a record exists, that it concerned the same subject, and that it was replaced.
- **Downstream records disclose substance.** A readable decision that cites a restricted one for its authority or its constraint leaks the substance of what was restricted.
- **Indexes are disclosure surfaces by construction** — anything that lists records to make them navigable also makes them enumerable.

It follows that **redaction within a connected set is not concealment**. Where existence itself must be concealed, the record has to be separated from the readable set — physically, in a distinct register, or logically, by a store that discloses it in no index, identifier sequence, relationship or derived output. Separation is necessary but not sufficient: caches, exports, logs and any projection built from the records must respect the same boundary, or the disclosure simply moves. And separation costs something real — a concealed decision is absent from the organisation's connected memory, and the lineage that would have explained it is broken by design. Choosing that is itself a decision worth recording.

One consequence falls inside this standard's scope, because it happens at capture: an assistant reading broadly can carry protected content into a less-protected record. See [`practice/administration-and-assurance.md`](practice/administration-and-assurance.md). Everything else — authorised views, entitlement resolution, runtime enforcement — sits above the register and is out of scope here.

## 11. What this format does not yet compute

The lineage fields (§6) establish what was decided, by whom, and how each record relates to those before and after it. They do not establish what is **in force at a given moment**: the core record carries `decision_date` (when the judgement was made) but no effective-from or effective-until, no suspended state, and no jurisdictional or legal-entity applicability. A decision agreed in March and effective from April is indistinguishable from one effective immediately.

So a body of TDRs supports the current position; it does not compute it. Establishing what is in force is the work of whatever layer an adopter builds above the register, from the records and their lineage — and, until the standard settles the question, from whatever effectiveness data the adopter carries in the `x-` namespace (§4.3). Whether any of it belongs in the core is deliberately open: see [TDR-0015](decisions/TDR-0015-visibility-and-effectiveness.md).

A related caution: the governed position is not the realised position. What was decided, what was implemented, what is controlled and what actually happens are four different things, joined by evidence and closed by a named person's attestation — never by the record alone.

---

*This standard documents its own design decisions as TDRs in [`/decisions`](decisions/). Disagree with any of them? Propose a superseding TDR — see [CONTRIBUTING](CONTRIBUTING.md).*
