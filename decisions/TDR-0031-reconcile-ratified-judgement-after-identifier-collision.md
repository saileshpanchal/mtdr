---
id: TDR-0031
conforms_to: mtdr/decision/tdr@1.15.0
title: Reconcile a ratified judgement prospectively when its proposed identifier collides with an accepted record
status: accepted
template: full
decision_date: 2026-08-16
accountable_owner: Sailesh Panchal
confidence: medium
maturity: adopted
supersedes: none
derived_from: TDR-0027
confirmed_by_outcome: pending — review after two independently created identifier collisions have been reconciled without rewriting accepted judgement, or 2027-02-16, whichever is sooner
---

# TDR-0031 — Reconcile a ratified judgement prospectively when its proposed identifier collides with an accepted record

> **Ratified 2026-08-16.** Sailesh Panchal, as accountable owner and repository authority, ratified
> the constitutional rule after reviewing TDR-0031 and DAC-0031, required the semantic-equivalence
> constraints now stated below, and accepted the case as `proceed-with-constraints`. The
> [attributable ratification evidence](evidence/TDR-0031-ratification-2026-08-16.md) binds the
> reviewed candidate, requested refinement and accepted representation. The earlier
> [governance-ruling input](evidence/TDR-0031-governance-ruling-2026-08-16.md) remains preserved as
> pre-candidate evidence rather than being rewritten retrospectively.

## Context — what was known at the time

MTDR's Gate-B review produced valid human rulings for typed multi-object conformance and
four-dimensional validity. Those substantive judgements were preserved on the local
`codex/gate-b-decision-drafts` branch at
`f966a05d6c65dbbd01190e424b3ada7d54018a9a`, with assurance cases and attributable evidence.

The branch was based on PR #11 at `4754e1ae807f80b4bf6d7da8e23504b106c84363`. Public `main` later
advanced independently to `bc29ba009c61b3edb5f021ae392d12ab547265ce`. It contains different
accepted judgements already represented as TDR-0020 and TDR-0025. The Gate-B records reused those
identifiers for materially different judgements. A normal merge would therefore replace the
content of public accepted records while making the history look continuous.

TDR-0027 establishes that authorised human ratification confers standing, while evidence permits
MTDR to represent that standing as `accepted`. It also says ratification binds to the substantive
judgement reviewed rather than necessarily to eternally byte-identical representation. It does not
settle what happens when valid evidence names an identifier that is already occupied by a different
accepted judgement.

The collision creates two unacceptable shortcuts. Treating the public identifier as automatically
decisive would discard a genuine human act. Treating the Gate-B act as permission to replace the
public file would rewrite accepted judgement. The problem concerns identity, evidence and lineage;
Git conflict resolution cannot decide it.

The question is: **how may MTDR represent a ratified substantive judgement when the candidate
identifier associated with its evidence collides with a different accepted record?**

## Decision

**Standing originates in the authorised human act, attaches to the substantive judgement evidenced
by that act, and is represented through repository identity. Repository identity is not the source
of standing. An identifier collision neither invalidates ratification nor authorises replacement of
the accepted record occupying the identifier. MTDR may create a fresh prospective representation
only where human review confirms semantic equivalence to the ratified judgement and an evidence
crosswalk binds the original candidate, ratification act and new representation.**

The rule applies as follows:

1. **Preserve the accepted occupant.** The accepted record already occupying the identifier remains
   immutable. Only lifecycle metadata changes permitted by the governing specification may be made,
   and only when a new standing judgement actually supersedes it.
2. **Test the evidence independently of the identifier.** Review must establish the actor, authority,
   act and intent, time, and the substantive judgement ratified. Evidence that identifies only a
   filename, number, merge or status is insufficient.
3. **Allocate a fresh prospective identifier.** The ratified judgement receives an identifier not
   occupied by any accepted or proposed record in the reconciliation scope. Documented reservations
   are considered to avoid another collision, but reservation confers neither standing nor
   ownership. A number is merely an address until a governed representation exists.
4. **Bind old and new representations through evidence, not false lineage.** A durable crosswalk
   identifies the colliding candidate's commit and content hash, the human ruling, the new
   representation and the semantic-equivalence review. The colliding identifier is retained as
   provenance about the candidate; it is not used as the identity of the new judgement.
5. **Carry standing only across strict semantic equivalence.** A named human must explicitly
   confirm all four conditions before the new representation may carry the earlier standing:
   - the substantive judgement, constraints, exclusions and scope are unchanged;
   - the original ratification evidence remains immutable and attributable;
   - the new representation identifies the collided source representation and why a fresh
     identifier was necessary; and
   - the evidence crosswalk binds the original candidate, ratification act and new representation.

   Necessary identifier, link and provenance substitutions are non-semantic only when they meet
   those conditions. If any substantive proposition changes, the work is no longer reconciliation:
   it is a new decision requiring a new ratification.
6. **Reconstruct lineage against standing public judgements.** `supersedes` and `derived_from`
   describe how the newly represented judgement relates to actual accepted records. They do not
   reproduce the candidate branch's mistaken identifier assignment. Supersession is narrow: a
   prior record is superseded only where the new judgement answers the same question differently.
7. **Re-identify dependent assurance and evidence.** A DAC whose `tdr_id` would otherwise resolve to
   the wrong accepted record receives a fresh identifier and is rebound to the new TDR. Its
   substantive findings and constraints are preserved only after the same equivalence review.
   Ratification evidence retains the original act and adds the reconciliation crosswalk; it is not
   rewritten to pretend the new identifier was used at the time.
8. **Confer no standing by association.** Other records in the same branch, commit, review cohort or
   decomposition retain their own lifecycle state. Reconciliation of one ratified judgement cannot
   promote a neighbouring candidate.

This is a representation repair, not a new source of authority. A merge, renumbering operation,
crosswalk, validator or agent still cannot ratify a judgement.

## Evidence

- **Business** — discarding a valid decision loses accountable organisational judgement; replacing
  the accepted occupant destroys reliable history. Prospective reconciliation preserves both.
- **Architecture** — the exact Git topology proves the case: PR #11 is the common base, while
  Gate-B `f966a05` and public main `bc29ba0` are sibling commits containing materially different
  TDR-0020/TDR-0025 content. The compared refs and their immutable objects remain the primary
  evidence; this record does not depend on an uncommitted review report.
- **Regulatory** — not directly material; the regulator-neutral accountability requirement is that
  the attributable human act and historical judgement both survive review.
- **Operations** — normal merge tools resolve path conflicts, not semantic identity. Without this
  rule, maintainers must either discard standing or silently rewrite history whenever branches
  allocate the same record number.
- **Customer** — indirectly material. False lineage can allow an unreviewed rule to influence
  decisions affecting people, while discarded ratification can remove constraints intended to
  protect them.
- **Data** — Git commit IDs and blob hashes can durably bind candidate content, but a hash proves
  content identity rather than authority or semantic equivalence. The human crosswalk supplies the
  missing judgement.
- **External** — no external standard is required to decide this repository's authority boundary.
  Git's immutable object model supplies useful provenance but does not determine MTDR standing.

## Alternatives rejected

1. **The public identifier wins; discard the colliding ratification.** Rejected because a repository
   address does not nullify an authorised human act whose substantive judgement is established.
2. **The ratified Gate-B file wins; replace the public accepted record.** Rejected because
   ratification of one judgement cannot authorise rewriting a different accepted judgement.
3. **Treat the identifier as constitutive of the decision, so collision invalidates both.** Rejected
   because TDR-0027 attaches authority to the human act and defined judgement, not storage syntax.
4. **Allow two standing records with the same identifier, distinguished by branch or commit.**
   Rejected because references would become context-dependent and a portable lineage could not
   resolve deterministically.
5. **Silently renumber the Gate-B files.** Rejected because later readers would lose the connection
   between the human evidence, the reviewed content and the prospective representation.
6. **Merge the whole Gate-B cohort and repair status afterwards.** Rejected because it would confer
   standing by proximity and make proposed records appear accepted through technical integration.
7. **Do nothing.** Rejected because the ratified judgements would remain unable to enter public
   lineage and every later implementation would build against an ambiguous constitutional state.

## Options foreclosed

- No accepted record may be substantively replaced to resolve an identifier collision.
- No collision may by itself invalidate an otherwise established human ratification.
- No identifier reservation may confer standing, ownership or priority over a future governed
  representation.
- No new identifier may inherit standing without attributable evidence and a semantic-equivalence
  review of the judgement represented.
- No candidate identifier may appear in `supersedes` or `derived_from` as if it named a different
  accepted public judgement.
- No assurance case may retain a `tdr_id` that resolves to the wrong decision after reconciliation.
- No branch, cohort, merge or neighbouring accepted record may confer standing on an unratified
  candidate.
- No crosswalk may rewrite historical evidence to imply that the prospective identifier existed at
  the time of the original act.

## Consequences and review

If accepted, this rule permits the two already-ratified Gate-B judgements to be represented under
fresh identifiers without changing the accepted content of public TDR-0020 or TDR-0025. Their DACs
and evidence will receive explicit crosswalks. The Gate-B candidates TDR-0018, TDR-0019, TDR-0023,
TDR-0028 and TDR-0029 remain proposed and gain no standing from the repair.

Success is two independently created collision cases reconciled so that a reader can start from
either the original evidence or the current identifier, resolve the same substantive judgement,
and verify that no accepted record was rewritten and no unrelated candidate was promoted. Review
at that outcome or on 2027-02-16.
