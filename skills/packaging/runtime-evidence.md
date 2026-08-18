# Runtime evidence register

**Non-normative.** Evidence about external runtimes, gathered on a stated date from stated sources.
It constrains nothing in the standard and is not part of any conformance claim. Its purpose is to make
today's research **re-checkable** rather than leaving it embedded invisibly in an adapter: when a
runtime changes upstream, the change should be detectable by re-running this exercise against the
recorded evidence, not discovered when something breaks.

This directory is the one place in the repository where product names may appear
([TDR-0024](../../decisions/TDR-0024-packaging-independence.md)).

**Verified:** 2026-08-18.

**Current standing: four verified direct surfaces, plus one provisionally verified direct surface.**
Stated that way deliberately — the five-surface claim is not weakened, and it is not rounded up either.
Copilot becomes the fifth verified surface when its primary documentation can be reached; until then
the evidence says what it says.

## The falsification criterion

> **If supporting a runtime requires changing the meaning of a canonical MTDR artefact, that runtime
> is unsupported — it is not a reason to change MTDR.**

Adapters translate **packaging and invocation, never semantics.** A surface that needs a skill's
instructions altered, a specification reworded, or a schema relaxed does not get an adapter; it gets a
row here recording why it cannot be supported.

## Classification

| | Meaning |
|---|---|
| **direct** | The runtime reads canonical `SKILL.md` files unmodified. Only their *location* is arranged. |
| **thin-adapter** | Canonical files unmodified, but the runtime needs a descriptor or manifest alongside them. |
| **defer** | The loader mechanism is not verified, or supporting it would require altering canonical artefacts. |

## The register

| Runtime | Discovery | Canonical-skill compatibility | Progressive disclosure | Invocation | Transformation required | Class | Source · confidence |
|---|---|---|---|---|---|---|---|
| **Claude Code** | `~/.claude/skills/<name>/SKILL.md` (personal), `.claude/skills/<name>/SKILL.md` (project, plus every parent to the repo root), nested `.claude/skills/` below the working directory, and `.claude/skills/` inside any `--add-dir` directory | Yes. Accepts the six Agent Skills spec fields; MTDR uses two of them | Yes — "a skill's body loads only when it's used" | `/<directory-name>`, or loaded automatically when the description matches | Collection only — flatten the two-level MTDR layout into one directory | **direct** | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) · **primary** |
| **Codex** | `.agents/skills` scanned "in every directory from your current working directory up to the repository root"; a user directory for personal skills | Yes. "The SKILL.md file must include name and description" | Not stated in the material retrieved | Model-selected from the description | Collection only | **direct** | developers.openai.com/codex/skills · **secondary** — primary blocked by this environment's egress proxy |
| **Gemini CLI** | Four locations in precedence order: built-in, extension, user `~/.gemini/skills/` (alias `~/.agents/skills/`), workspace `.gemini/skills/` (alias `.agents/skills/`) | Yes. "Based on the Agent Skills open standard" | Yes — "Only skill metadata (name and description) is loaded initially. Detailed instructions and resources are only disclosed when the model explicitly activates the skill" | `activate_skill` tool, with a user confirmation prompt before resources enter context | Collection only | **direct** | [gemini-cli/docs/cli/skills.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md) · **primary** |
| **Copilot** | Project locations reported as `.github/skills`, `.claude/skills` and `.agents/skills` | Reported yes, on the same `SKILL.md` standard | Not established | Agent mode, model-selected | Collection only, if the reported paths hold | **direct** *(provisional)* | Microsoft Learn and the GitHub changelog, **both unreachable from this environment** — recorded from secondary summaries. **Re-verify before relying on it.** |
| **ollama-agent** (local) | `~/.ollama-agent/skills/` (global), `./skills/` (project), any `--skills-dir` path; "last wins for same-name skills" | Yes. Stated requirement is "a `SKILL.md` file with YAML frontmatter containing name and description" — and nothing else | Yes — "the agent checks skill descriptions to find relevant ones. Only when a skill matches does the agent read the full instructions" | CLI/REPL, model-selected | **None** — `--skills-dir` can be pointed at a directory directly | **direct** | [github.com/arrase/ollama-agent](https://github.com/arrase/ollama-agent) · **primary** |

## What the evidence establishes

**1. `SKILL.md` is a named open standard, and MTDR uses a strict subset of it.** The Agent Skills spec
admits six frontmatter fields — `name`, `description`, `license`, `compatibility`, `metadata`,
`allowed-tools`. MTDR's skill contract permits exactly two, `name` and `description`, and
`tests/verify.py` has enforced that on every skill since before any of this was checked.

That is not caution rewarded by luck; it is why the answer below is what it is. Claude Code's
documentation notes that a field outside the spec makes packaging or upload *fail with a hard error* —
so the narrower the frontmatter, the wider the portability. MTDR is at the narrowest point available.

**2. Distribution equivalence is strongest when runtimes consume the same canonical artefact, not
generated semantic replicas of it.** This is the architectural finding of the exercise, and it inverts
the assumption it started from. Five per-surface bundles would have made divergence *possible in order
to then detect it*; one collection every surface points at makes divergence impossible. The five-runtime
problem collapsed into one standards problem: MTDR needs **one portable capability plus verified
discovery instructions**, not five semantic packaging implementations.

**3. Every runtime checked is `direct`.** Not one requires a transformed skill file. The strongest
available evidence for [TDR-0024](../../decisions/TDR-0024-packaging-independence.md) turns out to be
that there is almost nothing for a packaging adapter to do — packaging independence demonstrated by
the near-absence of packaging.

**4. There is exactly one transformation, and it is not semantic.** MTDR stores skills two levels deep
— `records/<language>/skills/<name>/SKILL.md` and `skills/shared/<name>/SKILL.md` — because skills live
with the record semantics they serve ([TDR-0023](../../decisions/TDR-0023-portable-skill-architecture.md)).
No runtime scans that shape. A bundle therefore **collects** the twenty-five skill directories into one
flat directory, byte-identical, and places it where the runtime looks. Collection is packaging; nothing
is rewritten, and the falsification criterion is not engaged.

**5. Collection breaks the skills' relative links, and that is the right outcome.** MTDR skills link
back into the semantics they serve — `../../../specification/candidacy-and-ratification.md` and the
like — which resolve at the canonical depth and not inside a flat bundle directory.

Rewriting those links to resolve in the bundle would modify a canonical artefact, which the criterion
above forbids outright. So they are preserved exactly, and the bundle documents that the
**reference-knowledge layer must be deployed alongside the skills** — which is what every runtime's
own documentation already assumes, and what `provenance.yaml` enumerates.

The finding underneath is worth stating: for MTDR, the natural distribution unit is a *subset of the
repository* rather than a flat directory of skill files, because [TDR-0023](../../decisions/TDR-0023-portable-skill-architecture.md)
deliberately puts skills next to the record semantics they serve. Runtimes want the flat shape; the
standard is not going to acquire a flat shape to suit them. The bundle resolves the tension by shipping
both and rewriting neither.

**6. `.agents/skills/` is a converging neutral path.** Codex scans it, Gemini aliases both its user and
workspace paths to it, and Copilot is reported to read it. A single `.agents/skills/` directory
plausibly serves three of the five without per-surface work — which, if it holds, means the "five
bundles" are largely one bundle in several places.

## What is not established

- **Copilot's discovery paths are secondary evidence.** Both primary sources are blocked from this
  environment. The row is provisional and marked as such rather than being quietly promoted.
- **agentskills.io is unreachable here**, so the spec's own text has not been read directly. The
  six-field list above is taken from Claude Code's documentation *of* the spec — a primary source for
  Claude Code, a secondary one for the standard.
- **Codex progressive-disclosure behaviour** is not stated in the material retrieved.
- **No runtime has been executed.** Everything here is documented behaviour. Whether the semantics
  survive execution is the recovery experiment's question, and *"translate packaging and invocation,
  never semantics"* is one of the things it should try to falsify.

## Re-verification

Re-run this exercise when a bundle is regenerated for a new release, and whenever a runtime announces
changes to skill loading. Update the date, the sources and the classifications; if a runtime moves in a
direction that would require altering a canonical artefact, its class becomes **defer** and the reason
is recorded here — the criterion above is not negotiable per runtime.
