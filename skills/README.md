# Skills

Portable skills — each a directory holding exactly one `SKILL.md` with two frontmatter fields
(`name`, `description`), loadable unmodified by any runtime that supports the open skill format, and
readable by a human with no runtime at all. The architecture is decided in
[TDR-0023](../decisions/TDR-0023-portable-skill-architecture.md).

## Where skills live

**Skills live with the record semantics they carry.** Each language package holds its own —
[`records/decision/skills/`](../records/decision/skills/) (authoring + assurance),
[`records/value/skills/`](../records/value/skills/) — because a package must extract complete, and
because record semantics stranded in a "neutral" skill quietly specialise it.

**[`shared/`](shared/) holds only skills that are demonstrably record-neutral** — the demonstration
being the skill's own text, which may reference no package's roles, admission test or specification
except by parameter:

| Skill | Does |
|---|---|
| [`identify-record-contributions`](shared/identify-record-contributions/) | Finds contributions in supplied material, for any package |
| [`reconcile-record-fragments`](shared/reconcile-record-fragments/) | Groups contributions into candidates — proximity is never identity |
| [`challenge-record`](shared/challenge-record/) | Attacks a candidate against its own evidence |
| [`validate-record`](shared/validate-record/) | Checks conformance against the record's own specification version |

Where a shared skill and a package skill both apply, the package skill carries the record semantics
and the shared skill the neutral mechanics; duplicated semantics between them is a defect, resolved
in the package's favour.

## The lifecycle

Every package's skills compose along one vocabulary — a package may omit a stage it does not need,
but may not rename one:

```
identify → classify contributions → reconcile → draft → challenge → validate → ratify
```

**Ratify is always human, never a skill** ([`specification/candidacy-and-ratification.md`](../specification/candidacy-and-ratification.md)).
Inputs and outputs between stages are the interchange structures of the
[contribution model](../specification/contribution-model.md).

## Distribution

[`packaging/`](packaging/) holds the distribution adapters — how these same files ship through
specific runtimes. Adapters are assembled *from* the normative artefacts and never constrain them
([TDR-0024](../decisions/TDR-0024-packaging-independence.md)); it is the one place in the repository
where product names may appear.
