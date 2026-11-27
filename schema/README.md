# Moved — the record schemas are in the record packages

Every file in this directory is a redirect: a JSON Schema that defines nothing of its own, only a
`$ref` to its new location and a `$comment` naming the move, kept so that previously published paths
keep resolving ([TDR-0021](../decisions/TDR-0021-record-package-architecture.md)).

- TDR and DAC schemas: [`records/decision/schema/`](../records/decision/schema/)
- VR schema: [`records/value/schema/`](../records/value/schema/)

This directory is not [`schemas/`](../schemas/), which holds the validation-result contract and the
shared interchange schemas.

Do not add content here.
