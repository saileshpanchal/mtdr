---
id: DAC-0031
conforms_to: mtdr/decision/dac@1.12.0
tdr_id: TDR-0031
title: Assure prospective reconciliation of ratified judgement after identifier collision
status: accepted
disposition: proceed-with-constraints
assessed_at: 2026-08-16
accountable_owner: Sailesh Panchal
review_date: 2026-09-16
confidence: medium
supersedes: none
---

# DAC-0031 — Assure prospective reconciliation of ratified judgement after identifier collision

> **Accepted 2026-08-16.** Sailesh Panchal accepted this case as `proceed-with-constraints` while
> ratifying [TDR-0031](TDR-0031-reconcile-ratified-judgement-after-identifier-collision.md). The
> ruling confirmed human-reviewed semantic equivalence as the only carry-forward mechanism and
> authorised TDR/DAC-0032 and TDR/DAC-0033 drafting only. This case does not itself transfer their
> standing or authorise reconciliation merge.

## Uncertainty

Known: public accepted records and independently ratified Gate-B judgements use the same
identifiers for materially different content; the original human rulings and candidate Git objects
remain available; TDR-0027 makes authority and accepted representation separate. Unknown: whether
semantic equivalence can be assessed consistently when prose, identifiers and lineage references
change together, and how the rule should operate across repositories with different identifier
domains. Assumption: within one repository, exact source hashes plus human review of a bounded
judgement crosswalk are sufficient to preserve the act without pretending the identifier was part
of it. Confidence is medium because the present collision is well evidenced but the rule has not
yet survived an independent second case.

## Adversarial projection

Fully routed for internal-integrity and authority abuse. A maintainer or agent could label a
substantively expanded record “renumbered”, replay genuine ratification evidence against different
content, allocate a fresh ID to launder an edit, or use a cohort merge to promote unratified
neighbours. A malicious contributor could also reserve identifiers indefinitely to obstruct work.
Controls are immutable accepted occupants, exact candidate commit/blob binding, a human-reviewed
semantic crosswalk covering judgement, constraints, exclusions and scope, unique prospective
allocation, newly bound DACs and explicit exclusion of cohort standing. Identifier reservation
confers neither ownership nor standing. Residual exposure belongs to Sailesh Panchal as repository
authority until a portable reconciliation protocol and adversarial fixtures exist.

## Customer-outcome projection

Routed lightly because the decision has no direct customer journey. Indirect harm is material where
false lineage gives an unreviewed rule apparent authority over later records affecting customers,
or where a valid protective constraint is discarded because its candidate number collided. The
control is reviewable lineage rather than a customer-facing process.

## Control side-effects

Fresh identifiers can make one human act look like two decisions, create apparent gaps in numbering
and burden readers with crosswalks. Treating documented reservations as collision inputs can also
encourage identifier hoarding. The crosswalk must therefore state that the old candidate
representation has provenance value but no second standing identity, and reservations avoid
collisions without conferring ownership or standing.

## Execution capability

Git can preserve source commits and blobs, and the repository can validate unique public TDR/DAC
identifiers and resolvable lineage. It does not yet validate cross-branch reservations, semantic
equivalence, evidence-to-content binding or DAC rebinding. The first reconciliation must therefore
remain human-reviewed and must add deterministic must-not checks before any general automation is
claimed.

## Risk delta and declared interactions

The rule decreases the risk of lost ratification, rewritten accepted history and context-dependent
identifiers. It increases crosswalk complexity and creates a new place where a semantic edit could
be misclassified as representational. It interacts directly with TDR-0027's standing/evidence
boundary, the TDR lifecycle specification, public TDR-0020/TDR-0025, the Gate-B evidence bundle and
the future Packaging & Inspectability work. The resultant position remains constrained until the
first two crosswalks are reviewed and the repository rejects collision laundering.

## Risk vector

| Axis | Assessment and basis |
|---|---|
| severity | high — a false carry-forward can manufacture standing or erase accepted history |
| likelihood | medium — parallel branches have already produced two real collisions |
| exposure volume | high — the rule can apply to every governed record family |
| velocity | high — a merge or automated renumber can propagate the defect in one operation |
| concentration | high — repository authority and one reconciliation rule are shared trust anchors |
| detectability | medium — hashes expose content change, but semantic drift still requires judgement |
| reversibility | medium before public reliance; low after downstream records cite the wrong identity |
| control confidence | medium — preservation rules are clear; equivalence protocol and fixtures are new |
| customer-cohort distribution | indirect; harm concentrates where later consequential decisions rely on false standing |
| time horizon | permanent lineage, with acute exposure during every parallel governance merge |
| trend | stabilising under manual review and no-merge constraints |

## Decision debt

- Define a reusable reconciliation crosswalk containing source commit, source blob hash, original
  ruling, prospective identifier, target content hash, semantic-difference classification and human
  reviewer — owner Sailesh Panchal, due before TDR-0032 or TDR-0033 can represent `accepted`.
- Add repository checks for duplicate identifiers across the merge inputs, evidence bound to the
  wrong TDR subject, DAC `tdr_id` rebinding and unrelated candidate promotion — owner Sailesh
  Panchal, due before reconciliation merge.
- Define the identifier collision domain for extracted packages and independently governed forks —
  owner Sailesh Panchal, due 2026-10-16.
- Test evidence replay, semantic expansion hidden as renumbering, reservation abuse, stale
  crosswalks and one-to-many mappings — owner Sailesh Panchal, due 2026-09-16.
- Run the rule against a second independently created collision before raising confidence — owner
  Sailesh Panchal, due 2027-02-16.

## Monitoring contract

- Hypothesis: every reconciled representation resolves to one attributable human act and one
  materially equivalent judgement, while the colliding accepted occupant remains unchanged and no
  unrelated candidate changes lifecycle state. Counter-hypothesis: evidence is reused for changed
  substance, an accepted occupant changes content, one act creates two standing identities, or a
  cohort neighbour is promoted. Test: compare source/target blobs and judgement crosswalks, traverse
  lineage from both representations, and diff lifecycle state across the complete cohort. Metric is
  unreviewed semantic differences, changed accepted-content lines, ambiguous standing identities or
  unrelated promotions; threshold is one; owner Sailesh Panchal; trigger is stop reconciliation,
  restore the last public state and reopen TDR-0031.

## Learning obligations

Retain the original colliding objects, their branch topology, every proposed semantic-equivalence
crosswalk and the human review outcome. Record disagreements about whether a change is semantic,
especially where lineage wording changes meaning. The second proving case must be independently
created rather than manufactured from this one.

## Disposition

**Proceed with constraints.** The constitutional rule is supportable, but no automatic carry-forward
or reconciliation merge is authorised. The constraints are:

1. **Accepted occupant immutable.** Owner: Sailesh Panchal. Measure: byte comparison shows no
   substantive change to public TDR-0020 or TDR-0025; only separately justified lifecycle metadata
   may change.
2. **Exact evidence binding.** Owner: Sailesh Panchal. Measure: each carried judgement identifies
   the original Gate-B commit and blob, the human ruling and the new representation hash.
3. **Human semantic-equivalence review.** Owner: Sailesh Panchal. Measure: a named human approves a
   field-by-field crosswalk confirming unchanged substantive judgement, constraints, exclusions and
   scope; immutable attributable original evidence; an explicit collision explanation; and binding
   between original candidate, ratification act and new representation. Any changed substantive
   proposition is separately ratified.
4. **Fresh, unambiguous identities.** Owner: Sailesh Panchal. Measure: new TDR/DAC identifiers are
   unique across public records, Gate-B candidates and documented active reservations; reservation
   is recorded as operational coordination and confers neither ownership nor standing.
5. **Lineage describes judgement, not file history.** Owner: Sailesh Panchal. Measure:
   `supersedes`/`derived_from` refer only to the standing decisions actually related; branch
   provenance remains in evidence.
6. **No standing by association.** Owner: Sailesh Panchal. Measure: TDR-0018, TDR-0019, TDR-0023,
   TDR-0028 and TDR-0029 remain proposed unless independently ratified.
7. **Dependent cases rebound.** Owner: Sailesh Panchal. Measure: every carried DAC resolves to the
   fresh TDR it actually assures and preserves its constraints without implying retrospective IDs.
8. **No merge before proof.** Owner: Sailesh Panchal. Measure: full repository conformance,
   collision must-not tests and human crosswalk review pass before commit integration or release.

Skills run: systems-thinking, counterfactual-and-evidence, accumulated-and-resultant-risk,
fraud-and-adversarial-thinking, customer-outcomes (light), systems-dynamics, adaptive-capacity and
assurance-synthesis.
