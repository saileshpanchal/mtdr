"""Job profiles — one distribution package per record type — NON-NORMATIVE.

    uv run python -m mtdr_packaging.profiles list
    uv run python -m mtdr_packaging.profiles build <profile> [--mode job|compact|full] [--target T] [--out DIR] [--zip]
    uv run python -m mtdr_packaging.profiles install <profile> --runtime R --project DIR
    uv run python -m mtdr_packaging.profiles verify <installed package folder> [--json REPORT]

A profile is what one recovery job needs, and nothing else: the package's own recovery skills — the
closure of its orchestration entry over skill-to-skill links — the shared primitives the package
declares as normative dependencies, and the package's normative layer. One profile per record type;
never a combined bundle to fill a runtime's allowance, and never a skill from another record package
(owner, 20 Nov 2026). Candidate and experimental packages have no profile (TDR-0021, TDR-0047).

Every SKILL.md and reference file is copied byte-identical. The only things generated are navigation
(an index of where each linked file sits in the package) and a manifest of what the package holds.
**Packaging fails rather than drops**: a closure that leaves its package, a target limit exceeded, or a
description longer than a target accepts stops the build — a skill is never trimmed, merged or left
out to fit (TDR-0024).
"""
import argparse
import glob
import hashlib
import json
import os
import re
import shutil
import sys
import zipfile

import yaml

from .generate import ROOT, canonical_skills, repo_commit

LINK = re.compile(r'\]\((?!https?:|mailto:)([^)#\s]+)')
LAYERS = ('specification', 'schema', 'templates', 'validation')
SUBSTRATE = ('specification/', 'schemas/')

#: Target runtimes and the limits their own documentation states. Evidence and dates:
#: skills/packaging/runtime-evidence.md. A limit not established is absent, never guessed.
TARGETS = {
    'folder': {
        'title': 'any runtime that loads skills from a folder — Claude Code, Hermes Agent, Codex, Gemini CLI, Copilot in VS Code',
        'delivery': 'folder', 'limits': {},
        'source': 'skills/packaging/runtime-evidence.md'},
    'm365-cowork-plugin': {
        'title': 'Microsoft 365 Copilot — Cowork plugin package', 'delivery': 'upload',
        'limits': {'skills': 20, 'companions_per_skill': 20, 'description': 1024, 'name': 64},
        'source': 'learn.microsoft.com/en-us/copilot/cowork/cowork-plugin-development, read 2026-11-20 '
                  '(the skill cap from the page summary; the companion cap verbatim)'},
    'm365-agent-builder': {
        'title': 'Microsoft 365 Copilot — Agent Builder (declarative agent skills)', 'delivery': 'upload',
        'limits': {'skills': 8, 'total_files': 350, 'depth': 3, 'skill_chars': 20000},
        'source': 'learn.microsoft.com/en-us/plugins/declarative-agent-skills, read 2026-11-20'},
    'copilot-studio': {
        'title': 'Microsoft Copilot Studio', 'delivery': 'upload', 'limits': {'skills': 100},
        'source': 'learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas, read 2026-11-20'},
    'claude-chat': {
        'title': 'Claude — Chat with Skills', 'delivery': 'upload', 'limits': {'name': 64},
        'source': 'claude.com/docs/skills and support.claude.com, read 2026-11-20 — the description limit is stated as '
                  '200 in one article and 1,024 in others, and is not applied until a hands-on upload settles it'},
}

MODES = ('job', 'compact', 'full')

#: Runtimes the installer places a folder package into. A runtime is offered only where it is shown to
#: discover the canonical layout in place, so that every skill's relative links resolve from where the
#: runtime finds it. A runtime that scans one level deep would need a flat collection — which takes the
#: record-package skills' links out of the install — or a vendor descriptor no disposition has yet
#: claimed: it is refused, never installed broken (owner, 22 Nov 2026: fix the installer, not the
#: agent's instructions).
RUNTIMES = {
    'hermes': {
        'title': 'Hermes Agent', 'root': '.agents/skills', 'installable': True,
        'discovery': 'recursive — every SKILL.md below a trusted project skills directory '
                     '(agent/skill_utils.py, iter_skill_index_files: os.walk, following links; v0.23.0, '
                     'read 2026-11-22)'},
    'claude-code': {
        'title': 'Claude Code', 'root': '.claude/skills', 'installable': False,
        'discovery': 'one level — .claude/skills/<name>/SKILL.md or a symlink there; a skill nested deeper '
                     'is not discovered, and a symlinked skill reports the link path as its base directory '
                     '(2.1.316, probed 2026-11-20)',
        'refusal': 'the canonical layout is discoverable only through a plugin descriptor '
                   '(.claude-plugin/plugin.json naming the skill directories), a vendor manifest awaiting '
                   "disposition; a flat or symlinked install would take the record-package skills' links "
                   'out of the install'},
}


PROFILES_README = """# Profiles — one distribution package per record type

*Generated by `mtdr_packaging.profiles`. Do not edit; regenerate.*

A profile is what one recovery job needs and nothing else: a record package's own recovery skills (the
closure of its orchestration entry over skill-to-skill links), the shared primitives that package
declares, and its normative layer. One profile per record type — never a combined bundle, and never a
skill from another record package. Connecting records across types is not MTDR's job.

Each `<package>.yaml` lists the members, what is omitted, what is linked but not packaged (with the
class the package's manifest gives it), and whether a package fits each target in each mode.

| Mode | What a target receives |
|---|---|
| `job` | every skill in the profile, discoverable and unmodified |
| `compact` | the entry skill only; the other stages and the reference files travel as its companion files, with an index — behavioural equivalence **not yet shown** |
| `full` | the whole catalogue (profile `all`), for unrestricted runtimes |

Build on demand — packages are not committed:

```
uv run python -m mtdr_packaging.profiles list
uv run python -m mtdr_packaging.profiles build decision --mode job --target folder
uv run python -m mtdr_packaging.profiles build value --mode compact --target m365-agent-builder --zip
```

## Install, then verify before every execution

A folder package keeps the repository's layout, so each skill's relative links resolve inside it. Install
it where the runtime discovers skills **without moving any file relative to another**, and verify it
where it sits:

```
uv run python -m mtdr_packaging.profiles install decision --runtime hermes --project <your project>
uv run python -m mtdr_packaging.profiles verify <your project>/.agents/skills/mtdr-decision
```

`verify` exits non-zero unless every file matches the manifest's digest, nothing else is present, exactly
the package's skills are discoverable at their canonical paths, and every link in every skill resolves
inside the package or is one the manifest declares under `not_packaged`. **A flat collection is not an
install**: the record-package skills sit one or two levels deeper than a flat directory, so collected
flat, their links leave the install.

`install` offers a runtime only where it is shown to discover that layout in place — Hermes Agent walks
its trusted project skills directory recursively. Claude Code discovers one level deep, so the layout
reaches it only through a plugin descriptor, a vendor manifest awaiting disposition; until then `install`
refuses it rather than install it broken. Runtimes not yet tested are not offered.

A package that exceeds a target's limit is **not built** — nothing is trimmed, merged or dropped to fit.
Every built package carries `mtdr-package.json`: version, commit, skills and references with digests,
counts, the limits checked, required capabilities, omitted skills and unpackaged links. Nothing in a
package confers standing on anything it produces.
"""


class PackagingError(Exception):
    """The package cannot be built without changing or dropping something it needs."""


def _rel(path):
    return os.path.relpath(path, ROOT)


def _sha(path):
    return hashlib.sha256(open(os.path.join(ROOT, path), 'rb').read()).hexdigest()


def _links(path):
    base = os.path.dirname(path)
    return [os.path.normpath(os.path.join(base, l)) for l in LINK.findall(open(os.path.join(ROOT, path), encoding='utf-8').read())]


def _files_under(path):
    full = os.path.join(ROOT, path)
    if os.path.isfile(full):
        return [path]
    return sorted(_rel(p) for p in glob.glob(os.path.join(full, '**', '*'), recursive=True) if os.path.isfile(p))


def _description(path):
    return yaml.safe_load(open(os.path.join(ROOT, path), encoding='utf-8').read().split('---')[1])['description']


def profiles():
    """One profile per normative package with a recovery orchestration entry, and the reason the others
    have none."""
    out, none = {}, {}
    for m in sorted(glob.glob(os.path.join(ROOT, 'records', '*', 'package.yaml'))):
        man = yaml.safe_load(open(m, encoding='utf-8'))
        pkg = man['name']
        if man.get('status') != 'normative':
            none[pkg] = f"status {man.get('status')}: no distribution profile until admitted"
            continue
        entries = (man.get('skills') or {}).get('orchestration') or []
        if not entries:
            none[pkg] = 'no recovery orchestration entry'
            continue
        out[pkg] = {'manifest': man, 'entries': entries}
    return out, none


def resolve(pkg, manifest=None):
    """The members of one record type's profile, or a PackagingError naming why it cannot be built.
    `manifest` substitutes the package's manifest — the suite uses it to prove the boundary holds."""
    found, _ = profiles()
    if pkg not in found:
        raise PackagingError(f'no profile for {pkg!r}')
    man = manifest or found[pkg]['manifest']
    entries = (man.get('skills') or {}).get('orchestration') or found[pkg]['entries']
    skills = canonical_skills()
    path = {n: _rel(i['path']) for n, i in skills.items()}
    by_dir = {os.path.dirname(p): n for n, p in path.items()}
    deps = {d['ref']: d['class'] for d in man.get('dependencies') or []}
    shared_ok = {os.path.basename(r) for r, c in deps.items() if c == 'normative' and r.startswith('skills/shared/')}

    members, stack, problems = set(entries), list(entries), []
    while stack:
        for target in _links(path[stack.pop()]):
            t = target.rstrip('/')
            n = by_dir.get(os.path.dirname(t) if t.endswith('SKILL.md') else t)
            if n and n not in members:
                own = skills[n]['package'] == pkg
                if not (own or (skills[n]['package'] == 'shared' and n in shared_ok)):
                    problems.append(f'{n} ({skills[n]["package"]}) is reached by link but is neither a {pkg} skill nor a '
                                    f'shared primitive the {pkg} package declares')
                members.add(n)
                stack.append(n)
    if problems:
        raise PackagingError('; '.join(sorted(problems)))

    refs = set()
    for layer in LAYERS:
        refs.update(_files_under(f'records/{pkg}/{layer}') if os.path.isdir(os.path.join(ROOT, 'records', pkg, layer)) else [])
    for ref, cls in deps.items():
        if cls == 'normative' and not ref.startswith('skills/'):
            refs.update(_files_under(ref))
    def packaged(t):
        full = os.path.join(ROOT, t)
        return t in refs or (os.path.isdir(full) and bool(_files_under(t)) and set(_files_under(t)) <= refs)

    not_packaged = []
    for n in sorted(members):
        for target in _links(path[n]):
            t = target.rstrip('/')
            if by_dir.get(os.path.dirname(t) if t.endswith('SKILL.md') else t) or packaged(t):
                continue
            if skills[n]['package'] == 'shared' and t.startswith(SUBSTRATE) and os.path.exists(os.path.join(ROOT, t)):
                refs.update(_files_under(t))      # a shared primitive's own substrate references travel with it
                continue
            cls = next((c for r, c in deps.items() if t == r.rstrip('/') or t.startswith(r.rstrip('/') + '/')), None)
            if cls is None and t.startswith(f'records/{pkg}/'):
                cls = 'own package, outside its normative layer'
            elif cls is None and skills[n]['package'] == 'shared':
                cls = 'shared-skill reference'
            not_packaged.append({'from': n, 'link': target, 'class': cls or 'undeclared'})
    undeclared = [x for x in not_packaged if x['class'] in ('normative', 'undeclared')]
    if undeclared:
        raise PackagingError('; '.join(f"{x['from']} links {x['link']} ({x['class']}), which the profile would drop"
                                       for x in undeclared))
    omitted = sorted(n for n, i in skills.items() if i['package'] == pkg and n not in members)
    return {'package': pkg, 'record_type': man.get('primary_record'), 'entries': list(entries),
            'skills': {n: path[n] for n in sorted(members)}, 'references': sorted(refs),
            'not_packaged': sorted(not_packaged, key=lambda x: (x['from'], x['link'])), 'omitted_skills': omitted}


def full_catalogue():
    skills = canonical_skills()
    refs = set()
    for p in ('specification', 'schemas/shared'):
        refs.update(_files_under(p))
    found, _ = profiles()
    for pkg in found:
        for layer in LAYERS:
            if os.path.isdir(os.path.join(ROOT, 'records', pkg, layer)):
                refs.update(_files_under(f'records/{pkg}/{layer}'))
    return {'package': 'all', 'record_type': None, 'entries': sorted(skills),
            'skills': {n: _rel(i['path']) for n, i in skills.items()}, 'references': sorted(refs),
            'not_packaged': [], 'omitted_skills': []}


def _flat(path):
    return path.replace('/', '__')


def layout(members, mode, target):
    """{packaged path: source path} for every file, plus the generated navigation and per-skill counts."""
    delivery = TARGETS[target]['delivery']
    files, generated, discoverable, companions = {}, {}, [], {}
    if delivery == 'folder':
        for n, src in members['skills'].items():
            files[src] = src          # canonical layout: links resolve in the package, but for `not_packaged`
        for r in members['references']:
            files[r] = r
        discoverable = sorted(members['skills']) if mode != 'compact' else list(members['entries'])
        return files, generated, discoverable, companions
    entry_set = set(members['entries']) if mode == 'compact' else set(members['skills'])
    for n in sorted(entry_set):
        files[f'skills/{n}/SKILL.md'] = members['skills'][n]
    discoverable = sorted(entry_set)
    for n in discoverable:
        own = []
        if mode == 'compact':
            own += [(f'skill__{m}.md', members['skills'][m]) for m in sorted(members['skills']) if m not in entry_set]
            own += [(_flat(r), r) for r in members['references']]
        else:
            refs, linked = set(members['references']), set()
            for t in (x.rstrip('/') for x in _links(members['skills'][n])):
                under = _files_under(t) if os.path.exists(os.path.join(ROOT, t)) else []
                if t in refs:
                    linked.add(t)
                elif under and set(under) <= refs:  # a directory link travels only if the whole directory does
                    linked.update(under)
            own += [(_flat(r), r) for r in sorted(linked)]
        for name, src in own:
            files[f'skills/{n}/references/{name}'] = src
        index = [f'# Where this skill\'s links point, in this package', '',
                 f'`{n}` is a canonical MTDR skill, unmodified. Its links are written against the MTDR repository '
                 f'layout; in this package each linked file is a companion of this skill, named below. This file is '
                 f'navigation only and adds no rule.', '',
                 f'In the repository this skill sits at `{os.path.dirname(members["skills"][n])}/`: resolve its relative '
                 f'links from there to the paths in the first column.', '', '| Linked file | Read |', '|---|---|']
        index += [f'| `{src}` | `references/{name}` |' for name, src in own]
        generated[f'skills/{n}/references/INDEX.md'] = '\n'.join(index) + '\n'
        companions[n] = len(own) + 1
    return files, generated, discoverable, companions


def check_limits(members, mode, target, files, generated, discoverable, companions):
    lim = TARGETS[target]['limits']
    every = list(files) + list(generated)
    actual = {'skills': len(discoverable), 'total_files': len(every) + 1,
              'depth': max(p.count('/') for p in every) if every else 0,
              'companions_per_skill': max(companions.values()) if companions else 0,
              'description': max(len(_description(members['skills'][n])) for n in discoverable),
              'name': max(len(n) for n in discoverable),
              'skill_chars': max(len(open(os.path.join(ROOT, members['skills'][n]), encoding='utf-8').read()) for n in discoverable)}
    report = {k: {'limit': v, 'actual': actual[k], 'within': actual[k] <= v} for k, v in lim.items()}
    return report, [f'{k}: {r["actual"]} exceeds {r["limit"]}' for k, r in report.items() if not r['within']]


def plan(profile, mode='job', target='folder'):
    if mode not in MODES or target not in TARGETS:
        raise PackagingError(f'unknown mode {mode!r} or target {target!r}')
    members = full_catalogue() if profile == 'all' or mode == 'full' else resolve(profile)
    if mode == 'full' and profile != 'all':
        raise PackagingError("full mode is the whole catalogue: use the profile 'all'")
    files, generated, discoverable, companions = layout(members, mode, target)
    limits, exceeded = check_limits(members, mode, target, files, generated, discoverable, companions)
    return members, files, generated, discoverable, companions, limits, exceeded


def standard_version():
    text = open(os.path.join(ROOT, 'CHANGELOG.md'), encoding='utf-8').read()
    release = re.search(r'^## \[([0-9]+\.[0-9]+\.[0-9]+)\]', text, re.M)
    unreleased = re.search(r'^## Unreleased', text, re.M)
    v = release.group(1) if release else '0.0.0'
    return v + ('+unreleased' if unreleased and (not release or unreleased.start() < release.start()) else '')


def manifest(profile, mode, target, members, files, generated, discoverable, companions, limits):
    capabilities = ['read the files in this package', 'read a folder of evidence the user selects',
                    'write an output folder',
                    'optional — run Python with jsonschema, referencing and pyyaml, to execute the reference '
                    'validator from an MTDR checkout; without it, validation is the validate skill applied by the agent']
    return {
        'generated_by': 'mtdr_packaging.profiles — non-normative; canonical files copied byte-identical',
        'mtdr_version': standard_version(), 'commit': repo_commit(),
        'profile': profile, 'record_type': members['record_type'], 'mode': mode,
        'target': target, 'target_title': TARGETS[target]['title'], 'target_source': TARGETS[target]['source'],
        'entry_skills': members['entries'] if mode != 'job' else sorted(members['skills']),
        'skills': [{'name': n, 'source': src, 'sha256': _sha(src), 'discoverable': n in discoverable,
                    'companions': companions.get(n, 0)} for n, src in members['skills'].items()],
        'references': [{'source': r, 'sha256': _sha(r)} for r in members['references']],
        'counts': {'discoverable_skills': len(discoverable), 'skills': len(members['skills']),
                   'references': len(members['references']), 'files': len(files) + len(generated) + 1},
        'limits_checked': limits,
        'required_capabilities': capabilities,
        'omitted_skills': members['omitted_skills'],
        'not_packaged': members['not_packaged'],
        'equivalence': ('compact: the stages are companions of the entry skill, not discoverable skills — behavioural '
                        'equivalence to the canonical pipeline is NOT yet shown' if mode == 'compact' else
                        'every skill is discoverable and unmodified'),
        'standing': 'Nothing in this package confers standing on anything it produces. Candidates stay candidates.',
    }


def build(profile, mode='job', target='folder', out=None, make_zip=False):
    members, files, generated, discoverable, companions, limits, exceeded = plan(profile, mode, target)
    if exceeded:
        raise PackagingError(f'{profile} ({mode}) does not fit {target}: ' + '; '.join(exceeded) +
                             ' — nothing is dropped or trimmed to fit')
    out = out or os.path.join(ROOT, 'dist', 'profiles')
    dest = os.path.join(out, f'mtdr-{profile}-{mode}-{target}')
    shutil.rmtree(dest, ignore_errors=True)
    for packaged, src in files.items():
        os.makedirs(os.path.dirname(os.path.join(dest, packaged)), exist_ok=True)
        shutil.copyfile(os.path.join(ROOT, src), os.path.join(dest, packaged))
    for packaged, text in generated.items():
        os.makedirs(os.path.dirname(os.path.join(dest, packaged)), exist_ok=True)
        open(os.path.join(dest, packaged), 'w', encoding='utf-8').write(text)
    m = manifest(profile, mode, target, members, files, generated, discoverable, companions, limits)
    with open(os.path.join(dest, 'mtdr-package.json'), 'w', encoding='utf-8') as fh:
        json.dump(m, fh, indent=2, ensure_ascii=False)
        fh.write('\n')
    if make_zip:
        archive = shutil.make_archive(dest, 'zip', dest)
        return dest, archive, m
    return dest, None, m


def _tree_sha(root, paths):
    """One digest over the package: the sha256 of `<sha256>  <path>` lines, sorted by path."""
    lines = ''.join(f'{hashlib.sha256(open(os.path.join(root, p), "rb").read()).hexdigest()}  {p}\n'
                    for p in sorted(paths))
    return hashlib.sha256(lines.encode('utf-8')).hexdigest()


def verify(root):
    """Check an installed folder package where it sits, before anything executes from it:

    - every file the manifest lists is present with the manifest's digest, and nothing else is there;
    - the SKILL.md files discoverable below the root are exactly the package's skills, at their
      canonical paths;
    - every relative link in every skill, resolved lexically from where the skill sits, lands inside the
      root — or is one the manifest declares under `not_packaged`, with its class.

    Links in the reference files are counted and reported, not failed: the skills are the instructions.
    Returns a report whose `failures` is empty only when the package is intact."""
    failures = []
    try:
        man = json.load(open(os.path.join(root, 'mtdr-package.json'), encoding='utf-8'))
    except (OSError, ValueError) as e:
        return {'root': root, 'failures': [f'no readable mtdr-package.json: {e}']}
    if (man.get('mode'), man.get('target')) != ('job', 'folder'):
        failures.append(f"verify checks folder job packages; this one is {man.get('mode')} for {man.get('target')}")
    expected = {s['source']: s['sha256'] for s in man['skills']}
    expected.update({r['source']: r['sha256'] for r in man['references']})
    for path, sha in sorted(expected.items()):
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            failures.append(f'{path}: missing')
        elif hashlib.sha256(open(full, 'rb').read()).hexdigest() != sha:
            failures.append(f'{path}: digest differs from the manifest')
    present = {os.path.relpath(os.path.join(d, f), root) for d, _, fs in os.walk(root) for f in fs}
    for extra in sorted(present - set(expected) - {'mtdr-package.json'}):
        failures.append(f'{extra}: present but not in the manifest')

    found = {}
    for p in sorted(x for x in present if os.path.basename(x) == 'SKILL.md'):
        try:
            name = yaml.safe_load(open(os.path.join(root, p), encoding='utf-8').read().split('---')[1])['name']
        except Exception:                                  # noqa: BLE001 — any unreadable skill is a failure
            failures.append(f'{p}: a SKILL.md whose name cannot be read')
            continue
        found[name] = os.path.dirname(p)
    want = {s['name']: os.path.dirname(s['source']) for s in man['skills']}
    for name in sorted(set(found) | set(want)):
        if name not in want:
            failures.append(f'{name}: discoverable at {found[name]} but not in the package')
        elif name not in found:
            failures.append(f'{name}: in the package but not discoverable')
        elif found[name] != want[name]:
            failures.append(f'{name}: discoverable at {found[name]}, not at its canonical path {want[name]}')

    declared = {(x['from'], x['link']) for x in man['not_packaged']}
    links = {'resolved': 0, 'declared_not_packaged': [], 'broken': []}
    for name, base in sorted(found.items()):
        for link in LINK.findall(open(os.path.join(root, base, 'SKILL.md'), encoding='utf-8').read()):
            target = os.path.normpath(os.path.join(base, link))
            inside = not (target == '..' or target.startswith('../') or os.path.isabs(target))
            if inside and os.path.exists(os.path.join(root, target)):
                links['resolved'] += 1
            elif (name, target) in declared:
                links['declared_not_packaged'].append({'from': name, 'link': target})
            else:
                links['broken'].append({'from': name, 'link': link, 'resolves_to': target})
                failures.append(f'{name}: link {link} resolves to {target}, outside the package and undeclared')

    reference_links = {'resolved': 0, 'outside': {}}
    for path in sorted(r['source'] for r in man['references'] if r['source'].endswith('.md')):
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            continue
        for link in LINK.findall(open(full, encoding='utf-8').read()):
            target = os.path.normpath(os.path.join(os.path.dirname(path), link))
            if not target.startswith('..') and os.path.exists(os.path.join(root, target)):
                reference_links['resolved'] += 1
            else:
                top = target.split('/')[0] if not target.startswith('..') else '(outside the root)'
                reference_links['outside'][top] = reference_links['outside'].get(top, 0) + 1

    listed = list(expected) + (['mtdr-package.json'] if 'mtdr-package.json' in present else [])
    return {'root': os.path.abspath(root), 'profile': man.get('profile'), 'commit': man.get('commit'),
            'mtdr_version': man.get('mtdr_version'),
            'tree_sha256': _tree_sha(root, [p for p in listed if os.path.isfile(os.path.join(root, p))]),
            'files': len(expected) + 1, 'skills_discoverable': sorted(found),
            'skill_links': {'resolved': links['resolved'],
                            'declared_not_packaged': len(links['declared_not_packaged']),
                            'broken': len(links['broken'])},
            'declared_not_packaged': links['declared_not_packaged'], 'broken': links['broken'],
            'reference_links': reference_links, 'failures': failures}


def install(profile, runtime, project):
    """Build `profile` as a folder job package, place it where `runtime` discovers skills with every file
    in its canonical position relative to every other, and verify it there. Refuses a runtime not shown
    to discover that layout, and an occupied destination; never repairs a skill to make it resolve."""
    rt = RUNTIMES.get(runtime)
    if rt is None:
        raise PackagingError(f'unknown runtime {runtime!r}; known: {", ".join(sorted(RUNTIMES))}')
    if not rt['installable']:
        raise PackagingError(f"{rt['title']}: not installed — {rt['refusal']}")
    dest = os.path.join(project, rt['root'], f'mtdr-{profile}')
    if os.path.exists(dest):
        raise PackagingError(f'{dest} already exists — install into a clean location')
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        built, _, _ = build(profile, 'job', 'folder', out=tmp)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copytree(built, dest)
    report = verify(dest)
    if report['failures']:
        raise PackagingError(f'installed at {dest} but verification failed: ' + '; '.join(report['failures'][:5]))
    return dest, report


def descriptor_yaml(pkg):
    """The committed profile descriptor: members and, per target and mode, whether the package fits."""
    members = resolve(pkg)
    lines = ['# Generated by mtdr_packaging.profiles — do not edit. One profile per record type.',
             f'profile: {pkg}', f'record_type: {members["record_type"]}',
             f'entry: [{", ".join(members["entries"])}]', f'skill_count: {len(members["skills"])}', 'skills:']
    lines += [f'  - {n}  # {hashlib.sha256(open(os.path.join(ROOT, p), "rb").read()).hexdigest()[:16]}'
              for n, p in members['skills'].items()]
    lines += [f'reference_count: {len(members["references"])}', 'references:']
    lines += [f'  - {r}' for r in members['references']]
    lines += ['omitted_skills:'] + ([f'  - {n}' for n in members['omitted_skills']] or ['  []'])
    lines += ['not_packaged:'] + ([f'  - {x["link"]}  # {x["class"]}, from {x["from"]}' for x in members['not_packaged']] or ['  []'])
    lines.append('fit:')
    for target in TARGETS:
        for mode in ('job', 'compact'):
            _, _, _, _, _, _, exceeded = plan(pkg, mode, target)
            lines.append(f'  {target}.{mode}: ' + ('fits' if not exceeded else 'does not fit — ' + '; '.join(exceeded)))
    return '\n'.join(lines) + '\n'


def descriptors():
    found, none = profiles()
    files = {f'profiles/{pkg}.yaml': descriptor_yaml(pkg) for pkg in found}
    files['profiles/README.md'] = PROFILES_README
    files['profiles/unavailable.yaml'] = ('# Generated by mtdr_packaging.profiles — do not edit.\n'
                                          '# Record types with no distribution profile, and why.\n'
                                          + ''.join(f'{pkg}: {why}\n' for pkg, why in sorted(none.items())))
    return files


def main(argv=None):
    p = argparse.ArgumentParser(prog='python -m mtdr_packaging.profiles')
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('list')
    b = sub.add_parser('build')
    b.add_argument('profile', help="a record type's package name, or 'all' with --mode full")
    b.add_argument('--mode', default='job', choices=MODES)
    b.add_argument('--target', default='folder', choices=sorted(TARGETS))
    b.add_argument('--out')
    b.add_argument('--zip', action='store_true')
    i = sub.add_parser('install', help='place a folder package where a runtime discovers it, then verify it')
    i.add_argument('profile')
    i.add_argument('--runtime', required=True, choices=sorted(RUNTIMES))
    i.add_argument('--project', required=True, help='the project the runtime runs in')
    v = sub.add_parser('verify', help='check an installed folder package before executing from it')
    v.add_argument('root', help='the installed package folder (the one holding mtdr-package.json)')
    v.add_argument('--json', help='also write the full report here')
    args = p.parse_args(argv)
    if args.cmd in ('install', 'verify'):
        try:
            if args.cmd == 'install':
                dest, report = install(args.profile, args.runtime, args.project)
                print(f'installed {dest}')
            else:
                report = verify(args.root)
        except PackagingError as e:
            print(f'not installed: {e}', file=sys.stderr)
            return 1
        if getattr(args, 'json', None):
            with open(args.json, 'w', encoding='utf-8') as fh:
                json.dump(report, fh, indent=2, ensure_ascii=False)
                fh.write('\n')
        for f in report['failures']:
            print(f'FAIL {f}')
        if 'skill_links' in report:
            l = report['skill_links']
            print(f"{report['profile']} @ {report['commit']}: {report['files']} files, tree {report['tree_sha256'][:16]}; "
                  f"{len(report['skills_discoverable'])} skills discoverable; skill links: {l['resolved']} resolve, "
                  f"{l['declared_not_packaged']} declared not packaged, {l['broken']} broken")
        print('verified' if not report['failures'] else f"{len(report['failures'])} failure(s)")
        return 0 if not report['failures'] else 1
    if args.cmd == 'list':
        found, none = profiles()
        for pkg in found:
            m = resolve(pkg)
            print(f'{pkg}: {len(m["skills"])} skills, {len(m["references"])} references')
        for pkg, why in sorted(none.items()):
            print(f'{pkg}: none — {why}')
        return 0
    try:
        dest, archive, m = build(args.profile, args.mode, args.target, args.out, args.zip)
    except PackagingError as e:
        print(f'not built: {e}', file=sys.stderr)
        return 1
    print(f'built {dest}' + (f' and {archive}' if archive else '') +
          f' — {m["counts"]["discoverable_skills"]} discoverable skill(s), {m["counts"]["files"]} files')
    return 0


if __name__ == '__main__':
    sys.exit(main())
