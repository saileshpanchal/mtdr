# Moved — the interchange schemas are in `schemas/shared/`

Every file in this directory is a redirect: a JSON Schema whose only content is a `$ref` to the
schema's new location. The interchange schemas moved to [`schemas/shared/`](../../schemas/shared/)
in the v1.15.0 package restructure ([TDR-0021](../../decisions/TDR-0021-record-package-architecture.md)). The stubs remain so that the previously published
paths keep resolving.

| This stub | Now lives at |
|---|---|
| `source-fragment.schema.json` | [`schemas/shared/source-fragment.schema.json`](../../schemas/shared/source-fragment.schema.json) |
| `record-contribution.schema.json` | [`schemas/shared/record-contribution.schema.json`](../../schemas/shared/record-contribution.schema.json) |
| `candidate-assembly.schema.json` | [`schemas/shared/candidate-assembly.schema.json`](../../schemas/shared/candidate-assembly.schema.json) |

Do not add content here.
