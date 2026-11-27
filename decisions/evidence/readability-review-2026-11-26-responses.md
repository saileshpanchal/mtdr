# Responses to the readability review — 26 November 2026

How each finding of the [independent readability review](readability-review-2026-11-26.md) of the
public documentation at `1a2d0e54761db08bc0b2c3aaa4a68cff609534a6` was dealt with. The fixes are in the
documentation commit that adds this file. Nothing here changes a specification, schema, template,
worked example or canonical skill. The review was the one review asked for, and these fixes have not
been reviewed again.

**Fixed** means changed in this commit. **Deferred** means recorded and not changed, with the reason.
**Kept** means the text is deliberate.

| | Severity | Disposition |
|---|---|---|
| **RD1** No way to validate an authored TDR | Blocker | **Fixed in the documentation; the command is for the owner.** The README and the quick start now say plainly that no command checks a TDR you have written, give the manual route (the `validate-record` checklist, and the TDR schema for any JSON Schema validator), and warn that `mtdr_validation` on a folder of TDRs reports `0 artefact(s) assessed`, which is not a pass. It is listed as a known limitation. A command to validate an authored TDR would be new tooling, so whether to add one before release is put to the owner |
| RD2 | Fix | **Deferred.** Moving the route and status material out of *Write your first TDR* restructures the README; the first line of that section already sends the reader to the quick start |
| RD3 | Fix | **Fixed.** MADR and ADR are expanded |
| RD4 | Fix | **Fixed** for OIR, OAR and OER. *Operational Value Commitment* is already defined after its colon; the DAC's description is kept |
| RD5 | Fix | **Fixed.** The README says what the package is built for, recovering decisions from existing documents, and names Hermes Agent |
| RD6 | Note | **Kept.** Flat claims in the author's register; *Using MTDR with your framework* supports the last one |
| RD7 | Fix | **Fixed.** The README and the quick start tell the reader to point an assistant at `problem-framing-and-decision-capture` in the repository |
| RD8 | Note | **Fixed** for the two ragged wraps in the README sections this commit touches. The long line elsewhere is left |
| RD9 | Note | **Deferred.** The 13 failures are explained as a known limitation. The installer's `@ unknown` output is code, not documentation |
| RD10 | Fix | **Fixed.** Step 1 now works from material for the decision being made now, and sends a reader holding only what survives a past decision to the interpretation path |
| RD11 | Fix | **Fixed.** Step 6 says that confirming changes `status` from `proposed` to `accepted`, how to choose the identifier, and that it must match the file name |
| RD12 | Fix | **Fixed.** Step 3 names the full template's seven evidence headings |
| RD13 | Fix | **Fixed.** The paragraph is split: what a skill is, then the installed package's limitation |
| RD14 | Note | **Kept.** The author's register |
| RD15 | Fix | **Fixed.** The decision package README names the quick start's path unambiguously and links the package's templates and examples. It cannot link the quick start, because the package closure check forbids undeclared links out of a package |
| RD16 | Fix | **Deferred.** The package README's opening describes the package for an implementer; rewriting it is beyond this pass |
| RD17 | Fix | **Deferred, in part addressed.** The README now calls the interpretation path "recovering decisions from existing documents". Settling one name for *recovery*, *interpretation* and *reconstruction* is a terminology decision for the owner |
| RD18 | Note | **Fixed.** "Spec §3" links the TDR specification |
| RD19 | Fix | **Fixed.** The README and the profiles page say to run from the root of a clone, with uv, and that uv creates a `.venv` there |
| RD20 | Fix | **Fixed.** Both install paths are stated: `.mtdr/plugins/` for Claude Code, `.agents/skills/` for Hermes. Whether `claude --plugin-dir` can be made permanent is deferred |
| RD21 | Fix | **Fixed** for "(owner, 23 Nov 2026)", now a ruling of the maintainer with its date. The generator notice is kept: the page is generated |
| RD22 | Fix | **Deferred.** The flat-copy statistics come from the generator template; recasting them is a template change beyond this pass |
| RD23 | Fix | **Deferred.** Moving the agent-instruction block below the install guidance restructures the page. Its count now says five skills are proposed |
| RD24 | Note | **Deferred.** The claim is sourced in `runtime-evidence.md`, which the page links |
| RD25 | Fix | **Deferred.** Saying what an agent probe is and when it is needed is for the packaging page's next pass |
| RD26 | Note | **Deferred.** The installer's output is code |
| RD27 | Fix | **Fixed.** The README says which fields to change when starting from an example, to set `status: proposed`, and to keep `conforms_to` |
| RD28 | Fix | **Deferred.** The worked examples are normative and byte-identical to v1.30.0; the passed review date belongs to the example's own timeline |
| RD29 | Note | **Kept.** Two documents define the header's fields, and the sentence says which |
| RD30 | Fix | **Deferred** with RD1: a validation result for an authored TDR waits for the owner's decision on a command |

**Counts:** 16 fixed (RD1 only in the documentation, pending the owner), 11 deferred, 3 kept.
