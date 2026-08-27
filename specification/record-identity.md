# Record identity — what a detached record must be able to say about itself

**Version:** 1.0.0 · **Licence:** MIT

A record is frequently read alone: attached to a ticket, pasted into a paper, exported into a
different estate, recovered from a backup years later. In that condition the repository around it is
gone, and with it every convention that made the file interpretable.

> **A detached record must be able to identify its record type and resolve the specification and
> schema that govern it, without repository-private interpretation.**

That is [DAC-0032](../decisions/DAC-0032-typed-multi-object-conformance.md) constraint 2, and this
page is how MTDR meets it ([TDR-0043](../decisions/TDR-0043-version-bound-detached-records.md)).

## The binding

One optional frontmatter field, on every record family:

```yaml
conforms_to: mtdr/decision/tdr@1.15.0
```

```
mtdr / <package> / <record> @ <version>
 │        │          │           └── the specification version the record is presented as conforming to
 │        │          └────────────── the record type: tdr · dac · vr
 │        └───────────────────────── the organisational language the record belongs to
 └────────────────────────────────── the standard
```

## What a reader can do with it, holding nothing else

Given `mtdr/decision/tdr@1.15.0` and no repository:

| Question | Answered by |
|---|---|
| What kind of object is this? | `tdr` — a Transformation Decision Record |
| Which language does it belong to? | `decision` |
| Which document defines its meaning? | The TDR specification at version `1.15.0` |
| Which schema validates it? | `records/decision/schema/tdr.schema.json`, in an MTDR distribution whose decision package declares `specification_version: 1.15.0` |

**The last row is a rule, not a lookup.** The path is derivable from the identifier —
`records/<package>/schema/<record>.schema.json` — so no registry file has to be fetched, hosted or
kept alive for a record to remain resolvable. A registry is a service; a rule is not, and a record
that needed a service to be interpretable would have failed the constraint rather than met it.

## Why the field is optional in the schema

Making it structurally required would invalidate every record authored before it existed, and MTDR
does not invalidate records to add a convenience. The schemas therefore accept its absence, and this
repository requires it of its own governed records, enforced by `tests/verify.py`.

The distinction matters and is deliberate: **`conforms_to` is a property of a record that wants to
travel.** A record that never leaves its register loses nothing by omitting it. A record that does
leave, and omits it, is interpretable only by whoever already knows where it came from — which is the
repository-private interpretation the constraint exists to remove.

This also keeps the change additive under
[TDR-0039](../decisions/TDR-0039-state-relative-requirements.md): the field is valid in every
lifecycle state, so nothing here encodes a transition prerequisite as a representation requirement.

## What it does not do

- **It confers no standing.** A record stating `conforms_to` claims conformance to a specification;
  it says nothing about whether the organisation ratified it ([TDR-0027](../decisions/TDR-0027-human-ratification-confers-standing.md)).
- **It is not a conformance claim about anything but that record.** Under
  [TDR-0032](../decisions/TDR-0032-typed-multi-object-conformance.md) a version-bound record is the
  smallest independent claim, and implies nothing about its package, its register or the participant
  that produced it.
- **It is not provenance.** Where a record came from, and who wrote it, are separate questions
  answered by [provenance](provenance.md) and by the record's own fields.
- **It does not pin the schema by hash.** The identifier resolves to a specification version, and a
  version is a promise about meaning rather than about bytes.
