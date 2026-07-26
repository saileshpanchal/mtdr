---
id: TDR-0015
title: Keep visibility out of the record, open an adopter namespace, and defer effectiveness fields
status: accepted
template: full
decision_date: 2026-07-24
accountable_owner: Sailesh Panchal
confidence: medium
supersedes: none
derived_from: TDR-0006, TDR-0012
confirmed_by_outcome: pending — review when an adopter register supplies the evidence named under Consequences
---

# TDR-0015 — Keep visibility out of the record, open an adopter namespace, and defer effectiveness fields

## Context — what was known at the time

A review of v1.9.0 found two things absent from the core record and present only as practice guidance or not
at all. First, **visibility**: nothing in the record states who may know a decision exists, read it, read its
reasoning, or reach its evidence, and the practice guides' "scoped, not flat" instruction had no hook in the
format. Second, **effectiveness**: `decision_date` records when a judgement was made, but there is no
effective-from or effective-until, no suspended state, and no jurisdictional applicability — so the standard
cannot honestly claim to compute what is in force.

The review also observed, correctly, that "scope" was carrying four different meanings at once —
applicability, authority, visibility and impact — and that a reader can infer the existence of a record they
cannot read from identifier gaps, lineage references and downstream constraints.

One further fact settled the shape of the answer: `schema/tdr.schema.json` is `additionalProperties: false`.
The schema is closed. An adopter needing a sensitivity label, an effective date or a legal entity on a record
today cannot add one and still validate — they must fork the schema, put the value in prose where nothing can
query it, or fail validation. "Leave it to the adopter" was not actually available.

## Decision

1. **Visibility is not a property of the record, and no classification vocabulary enters the core.** The unit
   of visibility is the register; enforcement belongs to whatever holds the records. Spec §10 states this,
   together with what the format cannot conceal and why compartmentation — not redaction — is the only
   mechanism that conceals existence.
2. **Open an adopter extension namespace.** Frontmatter fields prefixed `x-` validate; core field names stay
   closed so misspellings still fail. The standard defines no meaning for them and no expectation of
   portability (spec §4.3).
3. **Separate the four scopes explicitly** in spec §4.4: applicability, authority, visibility, impact.
4. **Defer effectiveness to evidence.** No `effective_from`, `effective_until`, `suspended` state or
   jurisdiction field enters the core in this release. Spec §11 states plainly what the format therefore does
   not compute. Adopters who need these now carry them under `x-`.

## Evidence

- **Architecture.** ARCHITECTURE.md and TDR-0012 fix the standard's boundary at the decision register and put
  everything below it — graph, reasoning, enforcement — outside the format. Access control is squarely below
  that line; effectiveness computation is the layer above it.
- **Regulatory.** Not material to the choice. The standard is regulator-neutral (TDR-0001, TDR-0002); binding
  a classification vocabulary to any regime would reverse that.
- **External.** Organisations already run incompatible classification schemes — government markings, traffic
  light protocols, four-tier internal ladders. A standard that mints a fifth collides with all of them.
- **Architecture (precedent).** The DAC already carries the repository's only machine-readable temporal state
  (`stale`) and its only temporal fields (`effective_from` and siblings on the risk delta, TDR-0010) — on the
  sibling record, where the need was demonstrated, not in the core. The same discipline applies here.
- **Operations.** The closed schema was blocking adopters silently: the failure mode is a fork, which removes
  them from the standard's evidence pool entirely.
- **Business, Customer, Data.** Not material to this decision.

## Alternatives rejected

- **Add a `visibility:` field (or a classification enum).** Rejected on three counts. It would collide with
  every adopter's existing scheme; it would enforce nothing, since a label in a portable markdown file is a
  claim and not a control; and it would invite the belief that the label *is* the control. A record marked
  restricted, sitting where it can be read, advertises rather than protects. The most security-critical
  property in the review — who may know the decision exists — is precisely the one no field can deliver.
- **Add a full access model (roles, domains, entities, onward-use rules).** Rejected: that is an access-control
  standard, and writing one inside a decision-record standard would serve neither.
- **Open the schema wholesale** (drop `additionalProperties: false`). Rejected: it would silently accept
  misspelled core fields, losing a real validation guarantee. The `x-` namespace keeps that guarantee.
- **Ship `effective_from` and `effective_until` now.** Rejected as premature, not wrong. Their semantics are
  universal and the DAC precedent is good, but no adopter has yet demonstrated the need in a real register.
  Shipping a core field wrongly is close to unremovable; deferring costs one minor version, and the namespace
  means nobody is blocked meanwhile.
- **Say nothing until the question is settled.** Rejected: silence leaves the four scopes conflated and the
  inference-leakage limit undocumented, which is the more dangerous state.

## Options foreclosed

The `x-` prefix is now reserved and cannot later mean anything else. Committing to "the unit of visibility is
the register" means the standard will not grow per-record access semantics without a superseding decision that
overturns this reasoning. And publishing §10 sets an expectation of candour about the format's limits that
later releases must keep.

## Consequences and review

**Success looks like** adopters carrying their own classification and effectiveness data under `x-` without
forking, and the deferred question being settled by evidence rather than argument.

`confirmed_by_outcome` is tested when the evidence arrives. Specifically:

- **Effectiveness.** At least one adopter register where `decision_date` and the date a decision took force
  differ materially and often enough to matter, with the `x-` usage that shows the shape actually needed.
- **Lifecycle.** At least one adopter needing a suspended state, together with an answer to the question this
  release does not settle: whether suspension is a lifecycle fact recorded in place, or a change of judgement
  requiring a superseding record. (The related inconsistency that `rejected` appears in the status enum but in
  no §7 transition rule should be resolved at the same time.)
- **Visibility.** Evidence either way as to whether a record needs to *declare* which register governs it,
  as distinct from being held in one.

Absent that evidence by the review, the deferral stands and this record is superseded only to say so.
