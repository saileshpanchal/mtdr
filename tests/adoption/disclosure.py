#!/usr/bin/env python3
"""Progressive-disclosure budget — NON-NORMATIVE measurement.

    python3 tests/adoption/disclosure.py

"Works in five runtimes" must not secretly mean "load the entire MTDR repository into context". Every
runtime verified in `skills/packaging/runtime-evidence.md` selects a skill from its *metadata* and
reads the body only on a match. This measures what that actually costs, in three stages:

    1. catalogue      every skill's name and description, and nothing else
    2. + one skill    the selected skill's body
    3. + references   the documents that skill's body links to, resolved one level

Stage 3 is the honest cost of selecting and running one skill. It is compared against the corpus — what
a participant would carry if it loaded the repository instead.
"""
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#: The catalogue must stay a small fraction of the corpus, or selection is not cheap and progressive
#: disclosure has no purchase. Not a tuned figure — a ceiling well above the measured value, so it
#: catches a structural change rather than ordinary drift.
CATALOGUE_CEILING = 0.05
#: Running the most demanding single skill, with everything it names, against loading everything.
WORST_SKILL_CEILING = 0.35


def frontmatter(path):
    m = re.match(r"^---\n(.*?)\n---\n", open(path, encoding="utf-8").read(), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def size(path):
    return os.path.getsize(path)


def corpus_bytes():
    """What "just load the repository" costs: every markdown and schema a participant might read."""
    total = 0
    for pattern in ("**/*.md", "**/*.json", "**/*.yaml"):
        for f in glob.glob(os.path.join(ROOT, pattern), recursive=True):
            if "/.git/" in f or "/skills/packaging/canonical/" in f:
                continue          # the bundle is a copy; counting it would double the corpus
            total += size(f)
    return total


def measure():
    skills = sorted(glob.glob(os.path.join(ROOT, "records", "*", "skills", "**", "SKILL.md"),
                              recursive=True)) + \
             sorted(glob.glob(os.path.join(ROOT, "skills", "shared", "*", "SKILL.md")))

    catalogue = 0
    for f in skills:
        fm = frontmatter(f)
        catalogue += len(str(fm.get("name", "")).encode()) + len(str(fm.get("description", "")).encode())

    per_skill = {}
    for f in skills:
        base = os.path.dirname(f)
        refs = set()
        for link in re.findall(r"\]\((?!https?://|mailto:)([^)#\s]+)", open(f, encoding="utf-8").read()):
            target = os.path.normpath(os.path.join(base, link))
            if os.path.isfile(target):
                refs.add(target)
        per_skill[os.path.basename(base)] = {
            "body": size(f),
            "references": sum(size(r) for r in refs),
            "reference_count": len(refs),
        }
    return catalogue, per_skill, corpus_bytes()


def report():
    catalogue, per_skill, corpus = measure()
    worst = max(per_skill.items(), key=lambda kv: kv[1]["body"] + kv[1]["references"])
    name, w = worst
    stage3 = catalogue + w["body"] + w["references"]

    lines = [
        f"corpus (load everything)      {corpus:>8,} bytes",
        f"1. catalogue only             {catalogue:>8,} bytes   {catalogue / corpus:6.1%}",
        f"2. + {name[:22]:<22}  {catalogue + w['body']:>8,} bytes   {(catalogue + w['body']) / corpus:6.1%}",
        f"3. + its {w['reference_count']:>2} references     {stage3:>8,} bytes   {stage3 / corpus:6.1%}"
        "   ← the honest cost of running one skill",
    ]
    problems = []
    if catalogue / corpus > CATALOGUE_CEILING:
        problems.append(f"catalogue is {catalogue / corpus:.1%} of the corpus, above the "
                        f"{CATALOGUE_CEILING:.0%} ceiling — selection is no longer cheap")
    if stage3 / corpus > WORST_SKILL_CEILING:
        problems.append(f"the most demanding skill costs {stage3 / corpus:.1%} of the corpus, above the "
                        f"{WORST_SKILL_CEILING:.0%} ceiling — disclosure is no longer progressive")
    return lines, problems


if __name__ == "__main__":
    lines, problems = report()
    print("\n".join(lines))
    for p in problems:
        print(f"OVER BUDGET {p}")
    sys.exit(1 if problems else 0)
