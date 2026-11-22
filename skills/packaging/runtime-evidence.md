# Runtime evidence register

**Non-normative.** Evidence about external runtimes, gathered on a stated date from stated sources.
It constrains nothing in the standard and is not part of any conformance claim. Its purpose is to make
today's research **re-checkable** rather than leaving it embedded invisibly in an adapter: when a
runtime changes upstream, the change should be detectable by re-running this exercise against the
recorded evidence, not discovered when something breaks.

This directory is the one place in the repository where product names may appear
([TDR-0024](../../decisions/TDR-0024-packaging-independence.md)).

**Verified:** 2026-08-18. Hermes Agent and Claude Chat with Skills **documented** 2026-11-20, not yet run.

**Current standing: four verified direct surfaces, plus one provisionally verified direct surface.**
Stated that way deliberately — the five-surface claim is not weakened, and it is not rounded up either.
Copilot becomes the fifth verified surface when its primary documentation can be reached; until then
the evidence says what it says.

**Five further surfaces are documented and not yet verified** (20 Nov 2026): Hermes Agent, provisionally
direct; Claude Chat with Skills, deferred until a hands-on test; Microsoft 365 Copilot's Cowork plugins and
Agent Builder, which cap skills at 20 and 8 and so take record-type **profiles**
([`profiles/`](profiles/)); and Copilot Studio, whose 100-skill cap the full catalogue fits. Results are recorded per surface and per
capability; one surface's result is never read as another's.

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
| **Claude Code** | `~/.claude/skills/<name>/SKILL.md` (personal), `.claude/skills/<name>/SKILL.md` (project, plus every parent to the repo root), nested `.claude/skills/` below the working directory, and `.claude/skills/` inside any `--add-dir` directory | Yes. Accepts the six Agent Skills spec fields; MTDR uses two of them | Yes — "a skill's body loads only when it's used" | `/<directory-name>`, or loaded automatically when the description matches | A folder package in the canonical layout, reached through a plugin descriptor (`.claude-plugin/plugin.json` naming the skill directories) — a vendor manifest awaiting disposition. Collected flat, or symlinked, the record-package skills' links leave the install (hands-on, 20 Nov 2026: nested skills are not discovered; a symlinked skill reports the link path as its base directory) | **direct** for loading; **thin-adapter** for intact references *(pending the descriptor's disposition)* | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) · **primary** |
| **Codex** | `.agents/skills` scanned "in every directory from your current working directory up to the repository root"; a user directory for personal skills | Yes. "The SKILL.md file must include name and description" | Not stated in the material retrieved | Model-selected from the description | Collection only | **direct** | developers.openai.com/codex/skills · **secondary** — primary blocked by this environment's egress proxy |
| **Gemini CLI** | Four locations in precedence order: built-in, extension, user `~/.gemini/skills/` (alias `~/.agents/skills/`), workspace `.gemini/skills/` (alias `.agents/skills/`) | Yes. "Based on the Agent Skills open standard" | Yes — "Only skill metadata (name and description) is loaded initially. Detailed instructions and resources are only disclosed when the model explicitly activates the skill" | `activate_skill` tool, with a user confirmation prompt before resources enter context | Collection only | **direct** | [gemini-cli/docs/cli/skills.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md) · **primary** |
| **Copilot** | Project locations reported as `.github/skills`, `.claude/skills` and `.agents/skills` | Reported yes, on the same `SKILL.md` standard | Not established | Agent mode, model-selected | Collection only, if the reported paths hold | **direct** *(provisional)* | Microsoft Learn and the GitHub changelog, **both unreachable from this environment** — recorded from secondary summaries. **Re-verify before relying on it.** |
| **ollama-agent** (local) | `~/.ollama-agent/skills/` (global), `./skills/` (project), any `--skills-dir` path; "last wins for same-name skills" | Yes. Stated requirement is "a `SKILL.md` file with YAML frontmatter containing name and description" — and nothing else | Yes — "the agent checks skill descriptions to find relevant ones. Only when a skill matches does the agent read the full instructions" | CLI/REPL, model-selected | **None** — `--skills-dir` can be pointed at a directory directly | **direct** | [github.com/arrase/ollama-agent](https://github.com/arrase/ollama-agent) · **primary** |
| **Hermes Agent** (CLI and desktop app) | `~/.hermes/skills/<category>/<name>/SKILL.md`; a project's `.hermes/skills/` and `.agents/skills/` only once the project is trusted (`hermes skills trust`); further folders under `skills.external_dirs` in `~/.hermes/config.yaml`. The desktop app shares the CLI's configuration and skills | Yes — follows the Agent Skills standard; a missing `name` defaults to the folder name; name and description are truncated beyond 64 and 1,024 characters (MTDR's longest description is 738) | Yes — the listing carries name, description and category; the body loads on view; bundled files open only inside the skill's own folder (`..` is refused) | A slash command per skill, or loaded by the model; *bundles* load several skills under one command with an instruction. One skill directing others in order is not documented | A folder package in the canonical layout at `.agents/skills/mtdr-<record-type>/`, discovered in place because the loader walks the trusted skills directory recursively (`agent/skill_utils.py`, read 2026-11-22): `profiles install --runtime hermes`, then `verify`. The 20 Nov flat collection loaded all 30 skills but broke 66 of their 107 links; the agent found the files by search | **direct** for loading and intact references *(hands-on 22 Nov, `b448432`: the 13 Decision skills discovered in place, every skill link verified before and after the run; the agent, with a local Qwen model, opened none of the linked specifications, and the stage order was not observable)* | hermes-agent.nousresearch.com docs (skills, creating skills, tools, code execution, desktop) and the agent's `skills_tool.py` source, read 2026-11-20; the installed CLI (v0.23.0) · **primary** |
| **Claude Chat with Skills** (claude.ai and the desktop app's chat) | Uploaded one skill at a time as a ZIP holding `<skill-name>/SKILL.md` (Customize › Skills); the folder name must equal `name`; code execution and file creation must be on | Names comply (lowercase, digits, hyphens, ≤ 64, not containing `claude` or `anthropic`). **The description limit is stated inconsistently — 200 characters in one help article, 1,024 elsewhere — and every MTDR description is between 346 and 738** | Bundled files inside the skill's folder are copied into a remote code-execution sandbox; nothing outside the folder is uploaded, so canonical links into the specifications cannot resolve | Model-selected by description, or chosen from the `/` menu | Per-skill ZIPs with the reference knowledge inside each; local evidence folders only through a desktop extension (e.g. the Filesystem extension) whose files the remote sandbox may not reach | **defer** *(until a hands-on upload shows the descriptions are accepted and the references reachable)* | claude.com/docs/skills, support.claude.com help articles and platform.claude.com, read 2026-11-20 · **primary** |
| **Microsoft 365 Copilot — Cowork plugin** | A ZIP with `manifest.json` at its root listing `agentSkills` folders, each `skills/<name>/SKILL.md` | `name` 1–64 characters, kebab-case, equal to the folder; `description` 1–1,024 (MTDR fits). **At most 20 skills per package** and **20 companion files per skill** (5 MB each, 10 MB per skill) | Companion files under `references/` load on demand | Model-selected | A **job** profile: decision and value both fit (13 and 10 skills, at most 12 companions). Emitting `manifest.json` is a packaging artefact no disposition has claimed (the standards boundary) — **not produced** | **thin-adapter** *(provisional — not run; manifest pending a disposition)* | learn.microsoft.com/en-us/copilot/cowork/cowork-plugin-development, read 2026-11-20; the 20-skill cap via the page's summary, the companion limits verbatim · **primary** |
| **Microsoft 365 Copilot — Agent Builder** (declarative agent skills) | A ZIP of skill directories, each with a `SKILL.md`, at most 50 MB | `SKILL.md` instructions under 20,000 characters (MTDR's longest is 8,871). **At most 8 skills per agent**; 350 files across all skills; directory depth 3 | Optional resource files alongside the skill | Model-selected | A **compact** profile only: the entry skill with the other stages and references as its companions (decision 13 and value 10 skills exceed 8). Scripts run in a sandbox with no network and no package install, so the reference validator's dependencies are not available | **thin-adapter** *(provisional — compact equivalence not shown)* | learn.microsoft.com/en-us/plugins/declarative-agent-skills, read 2026-11-20 · **primary** |
| **Microsoft Copilot Studio** | Uploaded per skill (a `SKILL.md`, or a ZIP with resources) — the worked deployment in [`copilot-studio.md`](copilot-studio.md) | Ran unmodified in the field deployment | Not established | Model-selected | **100 skills per agent** (tenant-adjustable): the full catalogue fits | **direct** | learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas, read 2026-11-20 · **primary** |

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
No runtime scans that shape. A bundle therefore **collects** the thirty skill directories into one
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

**7. Hands-on, 20–22 Nov 2026 — points 4 and 5 are corrected.** Point 4's "no runtime scans that
shape" does not hold for Hermes Agent, which discovers every `SKILL.md` below a trusted project skills
directory. Point 5's "that is the right outcome" is withdrawn: collected flat, 66 of the catalogue's
107 skill links leave the install — every Decision and Value lifecycle skill — and an agent left to
search for the files can land on a different checkout. The owner's ruling (22 Nov): **fix the
installer, not the agent's instructions**. A folder package keeps the repository's layout, the
installer places it only where a runtime discovers that layout in place, and `verify` checks digests,
discoverability and every skill link before anything executes. Claude Code discovers one level deep,
so it reaches the layout only through a plugin descriptor — the same class of vendor manifest as the
Copilot Cowork `manifest.json`, routed by the owner to a proposed TDR.

## What is not established

- **Copilot's discovery paths are secondary evidence.** Both primary sources are blocked from this
  environment. The row is provisional and marked as such rather than being quietly promoted.
- **agentskills.io is unreachable here**, so the spec's own text has not been read directly. The
  six-field list above is taken from Claude Code's documentation *of* the spec — a primary source for
  Claude Code, a secondary one for the standard.
- **Codex progressive-disclosure behaviour** is not stated in the material retrieved.
- **Hermes:** whether an orchestrating skill runs the named stages in order (20 Nov: the stage skills
  loaded in order, then one generated script produced the output — not observable); whether the desktop
  app's tools equal the CLI's. Shown on 20 Nov: the agent opens linked files with its file tool, and
  `uv run` works under its default approval in a one-shot session.
- **Claude Chat with Skills:** whether descriptions over 200 characters are accepted at upload; the real
  ZIP size and file-count limits; whether `pyyaml`, `jsonschema` or `uv` are available in its sandbox;
  whether files read through a desktop filesystem extension can reach that sandbox. If supporting it
  would mean shortening a canonical description, it stays **defer** — the falsification criterion above.
- **Execution is barely begun.** One Hermes run over one fictional case (20 Nov), whose raw logs were
  lost with a cleared scratch area; everything else here is documented behaviour. Whether the semantics
  survive execution is the recovery experiment's question, and *"translate packaging and invocation,
  never semantics"* is one of the things it should try to falsify.

## Re-verification

Re-run this exercise when a bundle is regenerated for a new release, and whenever a runtime announces
changes to skill loading. Update the date, the sources and the classifications; if a runtime moves in a
direction that would require altering a canonical artefact, its class becomes **defer** and the reason
is recorded here — the criterion above is not negotiable per runtime.
