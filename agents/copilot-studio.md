# Worked deployment — Microsoft Copilot Studio

A worked example, not a dependency (any runtime that loads the open skill format works —
see [`README.md`](README.md)). Copilot Studio's new experience supports agent skills
directly (in preview at the time of writing), and this pack's first field deployment ran
there: the agent, on a reasoning model, identified the decisions in a live
steering-committee pack, produced candidate envelopes distinguishing commitments from
requests and plans, drafted two full-template TDRs — and held both at `proposed` with the
named-owner gap called out, unprompted. The skill files ran unmodified.

## Steps

1. **Create the agent** and paste the instruction block from
   [`README.md`](README.md#the-agent-instructions) into its Instructions field. Select a
   reasoning model if available — the routing and contradiction-hunt steps benefit most.
2. **Load the skills**: agent → **Build** tab → **Skills** → **Add skill → Upload a
   skill**. Upload each of the thirteen `skills/*/SKILL.md` files as-is (an upload is a
   standalone `SKILL.md`, or a `.zip` bundling one with resources). The frontmatter
   `name:` identifies each skill after upload; filenames don't matter.
3. **Add the reference knowledge** (8 files): `spec.md`, `spec-value-record.md`,
   `spec-decision-assurance.md`, and the five templates in `templates/`. Optionally
   `FAQ.md` and the `examples/` — the agent imitates the worked examples' register and
   depth. Use v1.5.0 of the repository or later (the DAC routing rule is normative in one
   place from that release).
4. **Seed memory** (if enabled) per the guidance in [`README.md`](README.md#memory-if-the-runtime-offers-it):
   register conventions, named owners by area, regimes in scope — plus the two guardrails,
   written into memory itself.
5. **Run the six probes** in [`conformance.md`](conformance.md) before giving anyone
   access.

## Notes

- Alternative packaging: zip each capture-path skill with its templates as bundled
  resources (problem-framing + the three TDR templates; value-record + `vr.md`; the
  assurance path + `dac.md`) so the skeleton travels with the skill. Start with the
  simple split; move to zips only if template retrieval from knowledge proves unreliable.
- Skills in Copilot Studio are preview: if an upload validates but misbehaves, uploading
  the same `SKILL.md` files as plain knowledge documents preserves the whole design — the
  instructions already direct the agent through the skills by name.
- Connected agents: see the multi-agent rule in [`README.md`](README.md#multiple-agents-if-the-runtime-connects-them).
  Specialist outputs are advisory evidence, never verdicts; synthesis and the one
  disposition stay with the main agent and a named human owner.
