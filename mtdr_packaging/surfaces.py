"""Verified surface descriptors — NON-NORMATIVE.

Every field here is evidence recorded in `skills/packaging/runtime-evidence.md`, on the date stated
there. Nothing is inferred, and a runtime whose loader could not be verified from a primary source
says so in `confidence` rather than being quietly promoted.

Adapters translate packaging and invocation, never semantics. If supporting a runtime ever required
altering a canonical MTDR artefact, the runtime would be classified `defer` here instead.
"""

#: Where the collected canonical skills are placed for each runtime, and how they are then invoked.
#: `class` is one of: direct (reads canonical SKILL.md unmodified), thin-adapter, defer.
SURFACES = {
    "claude-code": {
        "title": "Claude Code",
        "class": "direct",
        "confidence": "primary",
        "source": "https://code.claude.com/docs/en/skills",
        "project_paths": [".claude/skills/"],
        "personal_paths": ["~/.claude/skills/"],
        "also_accepts": ["any .claude/skills/ inside a directory passed to --add-dir"],
        "invocation": "Type /<skill-name>, or let Claude load a skill when its description matches.",
        "progressive_disclosure": "Yes — a skill's body loads only when it is used.",
        "unverified": [],
    },
    "codex": {
        "title": "Codex",
        "class": "direct",
        "confidence": "secondary",
        "source": "developers.openai.com/codex/skills (primary unreachable from the verifying environment)",
        "project_paths": [".agents/skills/"],
        "personal_paths": ["the Codex user skills directory"],
        "also_accepts": [".agents/skills is scanned in every directory from the working directory up to the repository root"],
        "invocation": "Model-selected from the skill description.",
        "progressive_disclosure": "Not stated in the material retrieved.",
        "unverified": ["the exact personal/global skills path", "progressive-disclosure behaviour"],
    },
    "gemini-cli": {
        "title": "Gemini CLI",
        "class": "direct",
        "confidence": "primary",
        "source": "https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md",
        "project_paths": [".gemini/skills/", ".agents/skills/"],
        "personal_paths": ["~/.gemini/skills/", "~/.agents/skills/"],
        "also_accepts": ["built-in and extension skills take precedence over both"],
        "invocation": "The activate_skill tool, with a confirmation prompt before resources enter context.",
        "progressive_disclosure": "Yes — only name and description load initially; instructions are disclosed on activation.",
        "unverified": [],
    },
    "copilot": {
        "title": "Copilot",
        "class": "direct",
        "confidence": "secondary — provisional, re-verify before relying on it",
        "source": "Microsoft Learn and the GitHub changelog, both unreachable from the verifying environment",
        "project_paths": [".github/skills/", ".claude/skills/", ".agents/skills/"],
        "personal_paths": [],
        "also_accepts": [],
        "invocation": "Agent mode, model-selected from the skill description.",
        "progressive_disclosure": "Not established.",
        "unverified": ["every discovery path in this row", "personal skill locations", "progressive-disclosure behaviour"],
    },
    "ollama-agent": {
        "title": "ollama-agent (local)",
        "class": "direct",
        "confidence": "primary",
        "source": "https://github.com/arrase/ollama-agent",
        "project_paths": ["./skills/"],
        "personal_paths": ["~/.ollama-agent/skills/"],
        "also_accepts": ["any directory passed to --skills-dir; last wins for same-name skills"],
        "invocation": "CLI or REPL, model-selected from the skill description.",
        "progressive_disclosure": "Yes — descriptions are checked first; full instructions load only on a match.",
        "unverified": [],
    },
}
