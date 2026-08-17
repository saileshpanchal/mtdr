#!/usr/bin/env python3
"""The repository's own conformance suite (TDR-0025).

Validates the repository against its own rules — run from the repository root:

    python3 tests/verify.py

Checks: record schema validity · lineage resolution · id/filename agreement · skill frontmatter
discipline · relative-link resolution (stubs included) · package manifests coherent · candidate
packages hold metadata and scope only · package dependency boundary · shared-skill record-neutrality
· consumer-name scan over normative artefacts · VR negative cases still rejected · identifier
allocation register coherent, with next-free proved rather than trusted.

Requires: pyyaml, jsonschema. Exit code 0 = conforming.
"""
import sys, os, re, glob, json, datetime

try:
    import yaml
    from jsonschema import Draft202012Validator as Validator
except ImportError:
    sys.exit("verify.py requires pyyaml and jsonschema: pip install pyyaml jsonschema")

FAILS = []
def fail(check, msg): FAILS.append((check, msg))
def note(check, msg): print(f"  {check}: {msg}")

def frontmatter(path):
    m = re.match(r'^---\n(.*?)\n---\n', open(path, encoding='utf-8').read(), re.S)
    return yaml.safe_load(m.group(1)) if m else None

def as_json(o):
    return {k: (v.isoformat() if isinstance(v, (datetime.date, datetime.datetime)) else v)
            for k, v in o.items()}

# 1 — decision records validate; ids match filenames; lineage resolves
tdr_schema = Validator(json.load(open('records/decision/schema/tdr.schema.json')))
records = sorted(glob.glob('decisions/TDR-*.md'))
ids = set()
for f in records:
    fm = as_json(frontmatter(f))
    ids.add(fm['id'])
    for e in tdr_schema.iter_errors(fm):
        fail('record-schema', f"{f}: {e.message}")
    if fm['id'] != os.path.basename(f)[:8]:
        fail('id-filename', f)
for f in records:
    fm = frontmatter(f)
    for field in ('supersedes', 'derived_from'):
        val = str(fm.get(field, 'none'))
        if val != 'none':
            for ref in (x.strip() for x in val.split(',')):
                if ref not in ids:
                    fail('lineage', f"{f}: {field} -> {ref} does not resolve")
note('records', f"{len(records)} validated")

# 2 — VR example validates; the two negative cases are still rejected
vr_schema = Validator(json.load(open('records/value/schema/vr.schema.json')))
vr_example = as_json(frontmatter('records/value/examples/example-value-record-practice-skills.md'))
for e in vr_schema.iter_errors(vr_example):
    fail('vr-example', e.message)
v1_shaped = {"id": "VR-0002", "title": "x", "status": "agreed", "linked_decisions": "TDR-0003",
             "value_kind": "cost", "finance_countersignatory": "A B", "reconcile_by": "2026-10-05",
             "procurement_stage": "pilot", "supersedes": "none", "derived_from": "none"}
if not list(vr_schema.iter_errors(v1_shaped)):
    fail('vr-negative', "a v1-shaped record validated against the v2 schema")
if not list(vr_schema.iter_errors({**vr_example, "status": "candidate", "realisation": "realised"})):
    fail('vr-negative', "candidate + realised validated — the state axes are not being enforced")
note('value', "example valid; both negative cases rejected")

# 3 — skills: strict YAML, exactly name+description, name = leaf directory, single-line description
skills = sorted(glob.glob('records/*/skills/**/SKILL.md', recursive=True)) \
       + sorted(glob.glob('skills/shared/*/SKILL.md'))
for f in skills:
    fm = frontmatter(f)
    if fm is None or set(fm) != {'name', 'description'}:
        fail('skill-frontmatter', f); continue
    if fm['name'] != os.path.basename(os.path.dirname(f)):
        fail('skill-name', f"{f}: name != leaf directory")
    if '\n' in str(fm['description']):
        fail('skill-description', f"{f}: multi-line description")
note('skills', f"{len(skills)} strict-parsed")

# 4 — every relative link resolves (stubs included)
checked = 0
for f in glob.glob('**/*.md', recursive=True):
    base = os.path.dirname(f)
    for link in set(re.findall(r'\]\((?!https?://|mailto:)([^)#\s]+)', open(f, encoding='utf-8').read())):
        checked += 1
        if not os.path.exists(os.path.normpath(os.path.join(base, link))):
            fail('link', f"{f} -> {link}")
note('links', f"{checked} checked")

# 5 — package manifests coherent; candidates hold metadata and scope only
manifests = sorted(glob.glob('records/*/package.yaml'))
for f in manifests:
    m = yaml.safe_load(open(f))
    pkg = f.split('/')[1]
    if m.get('name') != pkg or m.get('language') != pkg:
        fail('manifest', f"{f}: name/language mismatch")
    if m.get('status') == 'candidate':
        if m.get('conformance_layers') != {} or m.get('admission') != 'not-passed':
            fail('candidate', f"{f}: candidate manifest must be empty-layered, admission not-passed")
        files = sorted(os.path.basename(p) for p in glob.glob(f'records/{pkg}/**', recursive=True)
                       if os.path.isfile(p))
        if files != ['README.md', 'package.yaml']:
            fail('candidate', f"records/{pkg}: candidate packages hold metadata and scope only, found {files}")
    elif m.get('status') == 'normative':
        for r in m.get('records', []):
            for key in ('specification', 'schema'):
                if r.get(key) and not os.path.exists(f'records/{pkg}/{r[key]}'):
                    fail('manifest', f"{f}: {key} path {r[key]} missing")
            for t in r.get('templates', []):
                if not os.path.exists(f'records/{pkg}/{t}'):
                    fail('manifest', f"{f}: template {t} missing")
    else:
        fail('manifest', f"{f}: unknown status {m.get('status')}")
note('manifests', f"{len(manifests)} coherent")

# 6 — dependency boundary: packages reach sideways only into a sibling's specification/ or README
for f in glob.glob('records/*/**/*.md', recursive=True):
    pkg = f.split('/')[1]
    base = os.path.dirname(f)
    for link in set(re.findall(r'\]\((?!https?://|mailto:)([^)#\s]+)', open(f, encoding='utf-8').read())):
        target = os.path.normpath(os.path.join(base, link)).replace(os.sep, '/')
        parts = target.split('/')
        if target.startswith('records/') and len(parts) > 1 and parts[1] != pkg \
           and target != 'records/README.md':
            if not (len(parts) > 2 and (parts[2] == 'specification' or (len(parts) == 3 and parts[2] == 'README.md'))):
                fail('boundary', f"{f} -> {target} (sideways dependency)")

# 7 — shared skills are record-neutral: no link into any records/<language>/ path
for f in glob.glob('skills/shared/*/SKILL.md'):
    base = os.path.dirname(f)
    for link in set(re.findall(r'\]\((?!https?://|mailto:)([^)#\s]+)', open(f, encoding='utf-8').read())):
        target = os.path.normpath(os.path.join(base, link)).replace(os.sep, '/')
        if target.startswith('records/') and target not in ('records', 'records/README.md'):
            fail('neutrality', f"{f} -> {target}")
note('boundary+neutrality', "scanned")

# 8 — no consumer names in normative artefacts (TDR-0020); packaging adapters are exempt
CONSUMERS = re.compile(r'\b(Copilot|SharePoint|LangChain|Kuzu|Netlify|TIM-Miner)\b', re.I)
for f in glob.glob('records/**/*.md', recursive=True) + glob.glob('specification/*.md') \
       + glob.glob('schemas/**/*.json', recursive=True):
    for m in CONSUMERS.finditer(open(f, encoding='utf-8').read()):
        fail('consumer-name', f"{f}: {m.group(0)}")
note('consumer-names', "normative artefacts clean")

# 9 — every fixture carries a must-not section (TDR-0025)
fixtures = glob.glob('records/*/fixtures/**/FIX-*.md', recursive=True) \
         + glob.glob('tests/conformance/FIX-*.md') + glob.glob('tests/corpus/CORPUS-*.md')
for f in fixtures:
    if '## Must not' not in open(f, encoding='utf-8').read():
        fail('fixture', f"{f}: no must-not section — a fixture without one is non-conforming")
note('fixtures', f"{len(fixtures)} carry must-not sections")

# 10 — identifier allocation register (TDR-0034): state-defined, next-free derived not trusted
alloc_text = open('decisions/ALLOCATION.md', encoding='utf-8').read()
ALLOCATED, BURNT, NEXT_FREE = set(), set(), set()
STATES = {'allocated': ALLOCATED, 'burnt': BURNT, 'next free': NEXT_FREE}
for row in re.findall(r'^\|(.+?)\|(.+?)\|', alloc_text, re.M):
    cell, state = (c.replace('*', '').strip() for c in row)
    nums = [int(n) for n in re.findall(r'TDR-(\d{4})', cell)]
    if not nums or state not in STATES:
        continue
    STATES[state].update(range(nums[0], nums[-1] + 1))

# duplicate ids across records, and the id set the register must account for
seen = {}
for f in records:
    rid = frontmatter(f)['id']
    if rid in seen:
        fail('allocation', f"duplicate id {rid}: {seen[rid]} and {f}")
    seen[rid] = f
represented = {int(rid.split('-')[1]) for rid in seen}

for n in sorted(ALLOCATED - represented):
    fail('allocation', f"TDR-{n:04d} allocated but no governed representation exists")
for n in sorted(represented - ALLOCATED):
    fail('allocation', f"TDR-{n:04d} has a governed representation but no allocated register entry")
for n in sorted(BURNT & represented):
    fail('allocation', f"TDR-{n:04d} is burnt — no governed representation may use it")
if overlap := ALLOCATED & BURNT:
    fail('allocation', f"identifiers both allocated and burnt: {sorted(overlap)}")
if len(NEXT_FREE) != 1:
    fail('allocation', f"the register must state exactly one next-free identifier, found {len(NEXT_FREE)}")
else:
    stated = next(iter(NEXT_FREE))
    if stated in represented:
        fail('allocation', f"TDR-{stated:04d} is stated next free but a representation exists")
    derived = max(ALLOCATED | BURNT) + 1
    if stated != derived:
        fail('allocation', f"stated next free TDR-{stated:04d} != max(allocated ∪ burnt) + 1 = TDR-{derived:04d}")
note('allocation', f"{len(ALLOCATED)} allocated, {len(BURNT)} burnt, next free derived")

print()
if FAILS:
    for check, msg in FAILS:
        print(f"FAIL [{check}] {msg}")
    print(f"\n{len(FAILS)} failure(s)")
    sys.exit(1)
print("conforming — all checks passed")
