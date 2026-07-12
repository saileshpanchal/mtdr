# Transformation Decision Record (TDR) — Specification

**Version:** 1.3.0 · **Licence:** MIT · **Author:** Sailesh Panchal

**TDR** is the standard: the record, its fields, and its accountability semantics.
**MTDR** — Markdown Transformation Decision Record — is the markdown reference format of TDRs described in this repository, as MADR is to ADR.

The TDR has a sibling record: the **Value Record (VR)** — the TDR records the decision; the VR records the value case and its life. See [`spec-value-record.md`](spec-value-record.md). For what a TDR is *not* — consent receipts, identity claims, runtime logs, model traces — see the [boundary FAQ](FAQ.md).

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
- **Status transitions** (`proposed → accepted`, `accepted → superseded`) and `confirmed_by_outcome` updates are made in place — they are lifecycle facts, not changes of judgement.
- **Changes to decision content require a superseding TDR** stating what is now known that was not known at the time.

This is what makes a body of TDRs organisational memory rather than documentation: the reasoning trail survives its own corrections.

## 8. Regulatory framing — worked examples, not dependencies

The TDR is regulator-neutral. Two UK financial services regimes illustrate the test it is built to answer:

- **SM&CR "reasonable steps".** Accountability attaches to a *named* Senior Manager. When asked to demonstrate reasonable steps, that individual needs evidence of judgement exercised at the time — not a policy document, and not fragments reconstructed from a shared drive. A full TDR is that evidence.
- **Consumer Duty.** Firms must evidence that customer outcomes were considered in significant decisions. The customer evidence dimension makes that consideration explicit — or its absence visible — at decision time.

Organisations outside financial services, and outside the UK, will recognise the shape of the same test from their own boards, auditors and supervisors.

## 9. Versioning

This specification follows semantic versioning. Additive field changes are minor versions. Removal or weakening of the accountability core (named owner, time-of-decision context, confidence, evidence, foreclosure, lineage) would constitute a different standard, not a new version — see [TDR-0002](decisions/TDR-0002-differentiate-on-accountability-semantics.md).

---

*This standard documents its own design decisions as TDRs in [`/decisions`](decisions/). Disagree with any of them? Propose a superseding TDR — see [CONTRIBUTING](CONTRIBUTING.md).*
