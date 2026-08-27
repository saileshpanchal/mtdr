# Ratification evidence — TDR-0043

This note preserves the attributable human act permitting TDR-0043 to represent its standing as
`accepted`, and DAC-0043 as `proceed-with-constraints`. **It authorises no release.**

## Attributable act

| Element | Evidence |
|---|---|
| Actor | Sailesh Panchal |
| Authority | Accountable owner of TDR-0043 and repository authority for MTDR's design decisions |
| Date | 2026-08-27 |
| Act | Ratified TDR-0043 and accepted DAC-0043 as `proceed-with-constraints` |
| Subject | A record binds itself to the specification that governs it |
| Consequence | DAC-0032 constraints 2 and 3 discharged; the release gate moves from `fail` to `indeterminate` |

## Decision-bearing ruling preserved

The reviewer accepted that:

1. A detached record must be able to identify its type and resolve its governing specification
   without repository-private interpretation, and `conforms_to` supplies that.
2. The field is **optional in the schema and required of this repository's governed records**.
   Structurally required would invalidate every record authored before it existed and force major
   versions on all three specifications; the measure asks for a capability, not a mandate.
3. Resolution is **by rule**, never by registry, network call or service.
4. The specifications take additive minor versions — TDR 1.15.0, DAC 1.12.0, VR 2.1.0 — and every
   prior record still validates.
5. The stated limits stand and are not to be softened: the detached test is executed by the author,
   so it proves the rule works rather than that the scheme is legible to a first-time reader; and
   the extraction trial verifies the declaration is sufficient, not that each classification is
   correct.
6. DAC-0032 constraints **4 and 5 remain outstanding**. Nothing in this act discharges them, and
   `indeterminate` does not permit inferring the missing fact.

## Reviewed and accepted content

| Artefact | SHA-256 |
|---|---|
| Reviewed TDR-0043 as proposed | `0e02c84dd33a396911e4de0d38afb9aa6952f025569801214c2e92f986c6c12c 877810a40a7a3003348222f28ba0ad27b998bbeca54655334623d3d6f5d28896 c13ca4adb94408ca5c2b0066a67f61e8ffe8b0f4a0b8841d0c9f8e840817a94e a52631cec66c60dad0b163a5eca425ab22136e18ae86f89b39f5ab73c3cc4876` |
| Accepted TDR-0043 representation | `` |
| Reviewed DAC-0043 as proposed | `` |
| Accepted DAC-0043 representation | `` |

The hashes differ only by the lifecycle transition and its banner. No substantive proposition changed
between review and acceptance.

## Source integrity

The ruling was supplied as a human instruction in the Claude Code session after the implementation,
its falsification results and its stated limits were presented. The source instruction remains the
authoritative evidence of the act; this note preserves its decision-bearing content.
