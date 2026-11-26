# Moved — the record schemas are in the record packages

Every file in this directory is a redirect: a JSON Schema whose only content is a `$ref` to the
schema's new location. The schemas moved into their record packages in the v1.15.0 package
restructure ([TDR-0021](../decisions/TDR-0021-record-package-architecture.md)). The stubs remain so that the previously published paths keep resolving.

| This stub | Now lives at |
|---|---|
| `tdr.schema.json` | [`records/decision/schema/tdr.schema.json`](../records/decision/schema/tdr.schema.json) |
| `decision-assurance.schema.json` | [`records/decision/schema/dac.schema.json`](../records/decision/schema/dac.schema.json) |
| `vr.schema.json` | [`records/value/schema/vr.schema.json`](../records/value/schema/vr.schema.json) |

This directory is not [`schemas/`](../schemas/), which holds the validation-result contract and
the shared interchange schemas.

Do not add content here. A record schema belongs in its record package under
[`records/`](../records/).
