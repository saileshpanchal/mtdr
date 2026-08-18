# `mtdr_packaging` — bundle generator

**Non-normative.** This assembles distributions from the canonical artefacts. It defines nothing,
constrains nothing, and is not part of any conformance claim — the files it copies are the standard,
and this module only decides where they are put.

```bash
python3 -m mtdr_packaging.generate           # write the bundles
python3 -m mtdr_packaging.generate --check   # report drift without writing
```

`tests/verify.py` runs `--check` on every run, so a bundle cannot silently fall behind the manifests.

## The rule it exists to keep

> **Adapters translate packaging and invocation, never semantics.** If supporting a runtime required
> changing the meaning of a canonical MTDR artefact, that runtime would be unsupported — it would not
> be a reason to change MTDR.

The generator performs exactly one transformation, and it is not semantic: **collection**. MTDR stores
skills two levels deep because they live with the record semantics they serve
([TDR-0023](../decisions/TDR-0023-portable-skill-architecture.md)), and no runtime scans that shape.
Every `SKILL.md` is copied byte-identical, and the suite compares them byte for byte.

## What it produces

```
skills/packaging/
  canonical/skills/<name>/SKILL.md   the 25 canonical skills, collected, unmodified
  canonical/catalogue.yaml           enumerated from each package.yaml, with per-file digests
  canonical/provenance.yaml          standard version, commit, source manifests, reference knowledge
  <surface>/surface.yaml             verified discovery paths, invocation, and what is unverified
  <surface>/README.md                how to install and invoke, for that runtime
```

**One catalogue, not one per surface.** Every runtime verified so far reads canonical `SKILL.md` files
directly, so five copies of the same skills would prove only that copying works. A single collection
that every surface points at makes a divergent catalogue *impossible* rather than merely detectable —
and the suite still checks that no surface advertises a different count.

The surface descriptors are the only per-runtime content, and every field in them is evidence recorded
in [`skills/packaging/runtime-evidence.md`](../skills/packaging/runtime-evidence.md) with its source
and date. Nothing is inferred; a path that could not be verified from a primary source says so.

## What it will not do

It will not edit a skill, reword a specification, relax a schema, or add record semantics to a
surface descriptor. A packaging layer that did any of those would have made the standard depend on a
runtime, which is the whole thing [TDR-0024](../decisions/TDR-0024-packaging-independence.md) exists
to prevent.

It also will not claim anything about behaviour. A bundle delivers conforming skill *files*; whether
a participant executes them conformingly is a separate claim under
[TDR-0032](../decisions/TDR-0032-typed-multi-object-conformance.md), tested against fixtures, corpus
and probes.

## Requirements

`pyyaml`. Nothing else.
