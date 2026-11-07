# Historical candidate

**Version:** 1.0.0 · **Licence:** MIT · **Author:** Sailesh Panchal
**Status:** **Proposed under [TDR-0048](../decisions/TDR-0048-historical-recovery-doctrine.md) — no
standing until ratified.** Normative for skill interchange once accepted. Not a record specification.

The structure a [historical recovery](historical-recovery.md) hands on: a retrospective candidate for
an organisational object, carrying everything its claims rest on. It is a **profile over the existing
interchange structures** — [`SourceFragment`](source-fragment.md),
[`RecordContribution`](record-contribution.md) and [`CandidateAssembly`](candidate-assembly.md),
unchanged — with the retrospective facts they cannot carry added beside them, keyed by identifier.

## What it is not

The [contribution model](contribution-model.md)'s refusals apply in full.

- **It is not a record**, not a fourth record type, and not a peer of the record schemas.
- **It need not be kept.** This specification says what a historical candidate must preserve **if** an
  adopter keeps one. How it is produced, stored, indexed or reviewed is outside this standard.
- **Keeping one is processing personal data.** A candidate holds names recovered from historical
  material. Whether to keep it, and for how long, is the adopter's decision under the adopter's own
  obligations.
- **It describes no pipeline.** Ingestion, chunking, models, prompts, queues and review tools are
  implementation, and an implementation conforms by producing this structure, not by resembling
  anyone's process.

## The one rule

**A historical candidate never acquires standing because someone, or something, reconstructed it.**
Its standing is `none`, its status is `candidate`, and both are constants. Nothing that happens to it
afterwards changes the candidate itself.

## Fields

| Field | Required | Meaning |
|---|---|---|
| `contract_version` | Yes | The version of this contract, `1.0.0` — independent of any record specification |
| `candidate_id` | Yes | Stable identifier |
| `retrospective` | Yes | Always `true`: this was assembled after the event, from what survived it |
| `standing` | Yes | Always `none` |
| `status` | Yes | Always `candidate` |
| `event_time_ref` | Yes | The `contribution_id` of the contribution to the package's event role, or `unknown`. A pointer, never a copy, so the event time cannot disagree with its evidence |
| `fragments` | Yes | The `SourceFragment`s every claim rests on. At least one |
| `contributions` | Yes | The `RecordContribution`s. At least one |
| `assembly` | Yes | The `CandidateAssembly` grouping them — its `missing_semantics`, `conflicts`, `supersessions` and `unresolved` are where the candidate's uncertainty lives |
| `fragment_annotations` | Yes | One per fragment: `fragment_ref`, `capture_time`, `creation_time`, `evidence_kind`, and `restates` where the fragment repeats another source |
| `contribution_annotations` | Yes | One per contribution to a context role: `contribution_ref` and `considered` — `{state, fragment_refs}` |

Times are `YYYY`, `YYYY-MM`, `YYYY-MM-DD` or `unknown`, at the precision the evidence gives. The four
times, the contemporaneity grade, `considered` and the evidence kinds are defined in
[`historical-recovery.md`](historical-recovery.md).

**Contemporaneity is not a field.** It is computed from `capture_time`, `creation_time` and the event
time, so it cannot be authored, and a reader recomputes it rather than trusting a stored grade.

## What it never holds

Closed by schema, so each is refused rather than discouraged:

- **No disposition and no forward link to a record.** What happened to the candidate is recorded
  beside it, in review events, never written into it.
- **No rationale, explanation, summary or notes** — the same refusal the
  [derivation projection](derivation-projection.md) makes, for the same reason.
- **No score**, aggregate confidence or completeness percentage.
- **No workflow state.** `candidate` is the only status there is.
- **No reflective observation** — what might have been decided better is interpretation of the past,
  and belongs to whatever reads candidates, not to the candidate.

## Integrity

A schema checks shape. These are checked by validators, and are part of the contract:

1. Every `fragment_refs` value in a contribution names a fragment in `fragments`.
2. Every `contribution_refs` value in the assembly names a contribution in `contributions`.
3. `fragment_annotations` names each fragment exactly once; `contribution_annotations` names only
   contributions that exist, each at most once.
4. `event_time_ref` is `unknown` or names a contribution in the assembly.
5. `considered.state: evidenced` carries at least one fragment showing the link; `unlinked` and
   `unknown` carry none.
6. Where the object's record package declares its recovery roles, they hold: `event_time_ref` names a
   contribution to the event role; `considered` is on every contribution to a context role and on no
   other; no never-inferred role is filled with `derivation: inferred`; no contribution carries a class
   the package reports as a **finding**, since findings travel by fragment and are never grouped; no
   **invocation** role rests on a fragment of kind `unlinked` or `retrospective` — or a restatement of
   one — since authority is what the act invokes; and the event contribution's value is a time in the
   form above, so the grade can be recomputed. The decision language declares them in its
   [recovery vocabulary](../records/decision/specification/decision-contribution.md).
7. `restates` names the `fragment_id` of the fragment it repeats where the candidate carries it,
   otherwise the `source_ref` of what it repeats — and never the fragment itself.

## The digest

A candidate's **digest** is `sha256:` followed by the lowercase hexadecimal SHA-256 of its JSON
serialisation canonicalised under **RFC 8785 (JSON Canonicalization Scheme)**. Implementers use a JCS
library. A candidate carries no digest of itself: it is computed by whoever needs to bind to it, and a
candidate altered after review no longer matches the digest its review recorded.

## Review is appended, never applied

What a named individual does with a candidate is recorded as a **review event** beside it
([`schemas/shared/candidate-review-event.schema.json`](../schemas/shared/candidate-review-event.schema.json)).
The candidate is never changed.

| Field | Required | Meaning |
|---|---|---|
| `contract_version` | Yes | `1.0.0` |
| `event_id` | Yes | Stable identifier |
| `candidate_id` | Yes | The candidate acted on |
| `candidate_digest` | Yes | The digest of the candidate as it stood when the act was performed |
| `act` | Yes | `attest-account` · `split` · `merge` · `reject` · `retain` · `supersede` |
| `result_refs` | For four acts | `attest-account`: the record made, exactly one · `split`: two or more candidates · `merge`: the candidate merged into · `supersede`: the superseding candidate. None for `reject` or `retain` |
| `reviewer` | Yes | The named individual who performed the act |
| `authority` | Yes | The basis on which they acted |
| `date` | Yes | `YYYY-MM-DD` |
| `scope` | Yes | What the act covers, in words |
| `evidence_ref` | Yes | Where the evidence of the act is kept |
| `governs` | Yes | Always `false`. No review act — attestation included — establishes that the object governs now; that takes a separate, prospective record |

**The pipeline that produces candidates produces no review events.** A recommendation from a challenge
stage — split, merge, reject — is that stage's output, and becomes an event only when a named
individual acts on it.

**A candidate's disposition is a view.** It is `unreviewed` where no event exists, and otherwise the
acts recorded against it, in date order. Nothing in it can be authored.

### What an event does not prove

A review event **identifies** an act and binds it to the exact candidate it concerned. It does not
capture, authorise or evidence the act — how ratification is captured is outside this standard
([`candidacy-and-ratification.md`](candidacy-and-ratification.md)) — and the existence of a
well-formed event, or of a reference to evidence, **is never proof that a valid human act occurred**
([TDR-0027](../decisions/TDR-0027-human-ratification-confers-standing.md)). An event models no
routing, approval step or workflow; it records one act.

## Schemas

[`historical-candidate.schema.json`](../schemas/shared/historical-candidate.schema.json) and
[`candidate-review-event.schema.json`](../schemas/shared/candidate-review-event.schema.json). The
candidate schema refers to its sibling schemas by `$id`: load [`schemas/shared/`](../schemas/shared/)
as a registry before validating with it.

## Anti-patterns

- **The disposition field** — writing `ratified` into the candidate, so that the candidate claims what
  only an act can confer.
- **The stored grade** — a contemporaneity grade carried as data, where it can be authored wrong.
- **The copied event time** — the decision date restated in the envelope, free to disagree with the
  contribution that evidences it.
- **The pipeline standard** — reading this profile as a description of how mining should run.
- **The self-certifying event** — treating a well-formed review event as evidence that the review
  happened.
