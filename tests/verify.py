#!/usr/bin/env python3
"""The repository's own conformance suite (TDR-0025).

Validates the repository against its own rules — run from the repository root:

    python3 tests/verify.py

Checks: record schema validity · lineage resolution · id/filename agreement · skill frontmatter
discipline · relative-link resolution (stubs included) · package manifests coherent · candidate
packages hold metadata and scope only · package dependency boundary · shared-skill record-neutrality
· consumer-name scan over normative artefacts · VR negative cases still rejected · identifier
allocation register coherent, with next-free proved rather than trusted · the validation-result
contract accepting and rejecting its fixtures as published · no untyped conformance claim on a
normative surface · classified normative closure with no undeclared outward reference · must-not
probes over the reference implementation · a serialisation round-trip through a fresh process ·
the DAC-0032/0033 obligations register accounted for constraint by constraint · every standards-
boundary disposition reasoned and foreclosed.

The run ends with a **repository-subject** assessment (TDR-0032) reporting the four dimensions of
TDR-0033 independently, including eligibility for the DAC-0032/0033 release gate computed from the
obligations register (TDR-0037). Eligibility is reported, never acted on: it is not release authority.
 It is not a general conformance verdict, and there is none: a pass here
implies nothing about any record, package, skill or participant inside the repository. The exit
status is an operational signal about the run — non-zero when something failed — and is not a
normative aggregate result (DAC-0032 constraint 1, DAC-0033 constraint 8).

Requires: pyyaml, jsonschema. `--emit` additionally prints the serialised result.
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

# 3b — stated skill counts match reality. The count drifted silently once; a number in prose that
# nothing checks is a claim, and this repository does not ship unchecked claims about itself.
WORDS = {n: i for i, n in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
    "sixteen seventeen eighteen nineteen twenty twenty-one twenty-two twenty-three twenty-four "
    "twenty-five twenty-six twenty-seven twenty-eight twenty-nine thirty".split())}
# A total is always stated in the plural, which keeps prose like \"exactly one `SKILL.md`\" out.
COUNT = re.compile(r'([\w-]+) (?:`SKILL\.md` files|skills\]\(skills/)')
for f in glob.glob('**/*.md', recursive=True):
    if f.startswith('decisions/') or f == 'CHANGELOG.md':
        continue                       # immutable records and release history state their own moment
    for m in COUNT.finditer(open(f, encoding='utf-8').read()):
        stated = WORDS.get(m.group(1).lower(), m.group(1) if m.group(1).isdigit() else None)
        if stated is None:
            continue                   # not a count — ordinary prose before the marker
        if int(stated) != len(skills):
            fail('skill-count', f"{f}: states {m.group(1)} skills, repository has {len(skills)}")
note('skill-count', f"stated counts agree with the {len(skills)} on disk")

# 4 — every relative link resolves (stubs included). Collected bundle copies are exempt: their links
# are canonical and resolve at the canonical depth, and 12b proves them byte-identical to the
# originals checked here — so nothing goes unverified. Rewriting them to resolve inside a flat bundle
# would modify a canonical artefact, which packaging may never do (see runtime-evidence.md).
checked = 0
for f in glob.glob('**/*.md', recursive=True):
    if f.startswith('skills/packaging/canonical/skills/'):
        continue
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

# 8b — no untyped conformance claim (TDR-0032; DAC-0032 constraint 1). The phrase may be *named* —
# the decisions that prohibit it have to quote it — but never asserted.
UNTYPED = re.compile(r'.?MTDR[- ]conformant', re.I)
for f in glob.glob('records/**/*.md', recursive=True) + glob.glob('specification/*.md') \
       + glob.glob('decisions/*.md') + glob.glob('schemas/**/*.json', recursive=True):
    for m in UNTYPED.finditer(open(f, encoding='utf-8').read()):
        if m.group(0)[0] not in '"\'“`':
            fail('untyped-claim', f"{f}: {m.group(0).strip()} — a conformance claim must name its subject")
note('typed-claims', "no untyped conformance claim on a normative surface")

# 9 — every fixture carries a must-not section (TDR-0025)
fixtures = glob.glob('records/*/fixtures/**/FIX-*.md', recursive=True) \
         + glob.glob('tests/conformance/FIX-*.md') + glob.glob('tests/corpus/CORPUS-*.md') \
         + glob.glob('tests/validation/FIX-*.md') + glob.glob('tests/inspectability/FIX-*.md')
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

# 11 — contract fixtures: each carries a complete document and what the contract must do with it
def run_contract_fixtures(check, schema_path, pattern):
    schema = Validator(json.load(open(schema_path)))
    accepted = rejected = 0
    for f in sorted(glob.glob(pattern)):
        text = open(f, encoding='utf-8').read()
        exp = re.search(r'\*\*Contract expectation:\*\*\s*(accepted|rejected)', text)
        blocks = re.findall(r'```json\n(.*?)```', text, re.S)
        if not exp or len(blocks) != 1:
            fail(check, f"{f}: needs one contract expectation and exactly one json block")
            continue
        errors = list(schema.iter_errors(json.loads(blocks[0])))
        if exp.group(1) == 'accepted':
            accepted += 1
            for e in errors:
                fail(check, f"{f}: expected accepted, contract rejected it — {e.message}")
        else:
            rejected += 1
            if not errors:
                fail(check, f"{f}: expected rejected, the contract accepted it")
    return accepted, rejected

a, r = run_contract_fixtures('result-fixture', 'schemas/validation-result.schema.json',
                             'tests/validation/FIX-*.md')
note('result-contract', f"{a} accepted, {r} rejected as published")

# 11b — the derivation projection contract (TDR-0033's inspectability counterpart)
a, r = run_contract_fixtures('projection-fixture', 'schemas/shared/derivation-projection.schema.json',
                             'tests/inspectability/FIX-*.md')
note('projection-contract', f"{a} accepted, {r} rejected as published")

# 12 — classified normative closure (TDR-0032; DAC-0032 constraint 3). Role metadata, not a trust
# hierarchy — historical material can be authoritative evidence while being non-normative about
# current behaviour. The closure test: no outward reference may go undeclared.
CLASSES = {'normative', 'conformance', 'provenance', 'explanatory', 'navigation', 'historical'}
for f in manifests:
    m = yaml.safe_load(open(f))
    pkg = f.split('/')[1]
    if m.get('status') != 'normative':
        continue
    deps = m.get('dependencies')
    if not deps:
        fail('closure', f"{f}: a normative package must classify its dependencies")
        continue
    declared = []
    for d in deps:
        if set(d) != {'ref', 'class', 'why'}:
            fail('closure', f"{f}: dependency entries carry ref, class and why — got {sorted(d)}")
            continue
        if d['class'] not in CLASSES:
            fail('closure', f"{f}: unknown dependency class {d['class']}")
        if not os.path.exists(d['ref']):
            fail('closure', f"{f}: dependency {d['ref']} does not resolve")
        declared.append(d['ref'])
    for src in glob.glob(f'records/{pkg}/**/*.md', recursive=True):
        base = os.path.dirname(src)
        for link in set(re.findall(r'\]\((?!https?://|mailto:)([^)#\s]+)',
                                   open(src, encoding='utf-8').read())):
            target = os.path.normpath(os.path.join(base, link)).replace(os.sep, '/')
            if target.startswith(f'records/{pkg}/'):
                continue
            if not any(target == r or target.startswith(r.rstrip('/') + '/') for r in declared):
                fail('closure', f"{src} -> {target}: undeclared dependency, not in {f}")
note('closure', f"{sum(len(yaml.safe_load(open(f)).get('dependencies') or []) for f in manifests)} "
                "dependencies classified; no undeclared outward reference")

# 12b — distribution bundles: catalogue equivalence, semantic neutrality, freshness (TDR-0024)
sys.path.insert(0, os.getcwd())
from mtdr_packaging.generate import check as bundle_check  # noqa: E402
from mtdr_packaging.surfaces import SURFACES  # noqa: E402

try:
    drift, bundled = bundle_check()
except SystemExit as e:
    drift, bundled = [str(e)], {}
for d in drift:
    fail('bundle', d)

# every skill on disk is enumerated by a manifest, and vice versa — the generator depends on it
on_disk = {os.path.basename(os.path.dirname(p)) for p in skills}
for orphan in sorted(on_disk - set(bundled)):
    fail('bundle', f"skill {orphan} exists on disk but no package manifest enumerates it")

# capability equivalence: no surface may advertise a different catalogue from any other
counts = {}
for key in SURFACES:
    d = yaml.safe_load(open(f'skills/packaging/{key}/surface.yaml'))
    counts[key] = d.get('skill_count')
    if d.get('class') not in ('direct', 'thin-adapter', 'defer'):
        fail('bundle', f"{key}: unknown surface class {d.get('class')}")
if len(set(counts.values()) | {len(bundled)}) != 1:
    fail('bundle', f"surfaces advertise different catalogues: {counts} against {len(bundled)} collected")
note('bundles', f"{len(SURFACES)} surfaces, one catalogue of {len(bundled)}, canonical files byte-identical")

# 13 — must-not probes against the reference implementation (DAC-0033 constraint 5)
from mtdr_validation import (Dim, ValidationResult, IllegalResult, PASS,  # noqa: E402
                             NOT_APPLICABLE, validate_document)

def _reference_shape():
    r = ValidationResult('repository', 'probe', 'specification/conformance.md', '1.0.0')
    for d in (Dim.STRUCTURAL, Dim.SEMANTIC, Dim.RELATIONAL):
        r.report(d, PASS)
    r.report(Dim.TRANSITION, NOT_APPLICABLE, reasons=[('no-transition-requested', 'none')])
    return r.to_dict()


def refuses(what, thunk):
    try:
        thunk()
    except IllegalResult:
        return
    fail('must-not', f"the reference implementation permitted {what}")

refuses("a collection subject",
        lambda: ValidationResult('collection', 'reg', 'specification/conformance.md', '1.0.0'))
refuses("a participant subject",
        lambda: ValidationResult('participant', 'impl', 'specification/conformance.md', '1.0.0'))
refuses("structural not-applicable",
        lambda: ValidationResult('record', 'TDR-9010', 'x', '1.0.0')
        .report(Dim.STRUCTURAL, NOT_APPLICABLE, reasons=[('skipped', 'not run')]))
refuses("an indeterminate with no reason",
        lambda: ValidationResult('record', 'TDR-9012', 'x', '1.0.0')
        .report(Dim.SEMANTIC, 'indeterminate'))
refuses("a result with a dimension unreported",
        lambda: ValidationResult('record', 'TDR-9009', 'x', '1.0.0')
        .report(Dim.STRUCTURAL, PASS).to_dict())
if hasattr(ValidationResult, '__bool__') or any(
        h in dir(ValidationResult) for h in ('is_valid', 'ok', 'conformant', 'passed', 'exit_code')):
    fail('must-not', "the reference implementation offers an aggregate verdict")

# the assessed object is byte-identical before and after (no repair, no mutation)
probe_src = 'tests/validation/synthetic/TDR-9001-malformed.md'
before = open(probe_src, 'rb').read()
_probe = ValidationResult('record', 'TDR-9001', 'records/decision/specification/tdr.md', '1.14.0',
                          subject_ref=probe_src, assessed_state='proposed')
_probe.report(Dim.STRUCTURAL, 'fail', reasons=[('frontmatter-unparseable', 'did not parse')])
_probe.report(Dim.SEMANTIC, 'indeterminate', reasons=[('no-parsed-object', 'nothing to assess')],
              unevaluated_because='structural')
_probe.report(Dim.RELATIONAL, 'indeterminate', reasons=[('no-parsed-object', 'nothing to resolve')],
              unevaluated_because='structural')
_probe.report(Dim.TRANSITION, NOT_APPLICABLE, reasons=[('no-transition-requested', 'none requested')])
for e in _probe.validate():
    fail('must-not', f"the probe result does not satisfy its own contract: {e}")
if open(probe_src, 'rb').read() != before:
    fail('must-not', f"{probe_src} was mutated by assessment")

# eligibility confers nothing: a result cannot carry a release-performing or authority field
for forbidden in ('released', 'release_authorised', 'authority', 'performed'):
    probe_doc = {**_reference_shape(), forbidden: True}
    if not validate_document(probe_doc):
        fail('must-not', f"the contract accepted a result carrying {forbidden!r} — "
                         "eligibility must confer nothing (TDR-0037)")
note('must-not', "no aggregate verdict, no illegal result, no mutation, no conferred authority")

# 13b — serialisation round-trip. A result reloaded in a fresh process yields the same
# interpretation: nothing in a result may depend on the process that produced it. This is a local
# precursor to the detached-record release gate and claims nothing about external interoperability.
import subprocess, tempfile  # noqa: E402
with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as fh:
    fh.write(_probe.to_json())
    round_trip_path = fh.name
try:
    reader = subprocess.run(
        [sys.executable, '-c',
         "import json,sys;from mtdr_validation import validate_document;"
         "d=json.load(open(sys.argv[1]));e=validate_document(d);"
         "print(json.dumps({'errors':e,'read':[[x['dimension'],x['result']] for x in d['dimensions']]}))",
         round_trip_path],
        capture_output=True, text=True, cwd=os.getcwd())
    if reader.returncode != 0:
        last = reader.stderr.strip().splitlines()[-1] if reader.stderr.strip() else 'no output'
        fail('round-trip', f"a fresh process could not read the serialised result: {last}")
    else:
        got = json.loads(reader.stdout)
        expected = [[d['dimension'], d['result']] for d in _probe.to_dict()['dimensions']]
        if got['errors']:
            fail('round-trip', f"the reloaded result failed the published schema: {got['errors'][0]}")
        if got['read'] != expected:
            fail('round-trip', f"interpretation changed across processes: {got['read']} != {expected}")
finally:
    os.unlink(round_trip_path)
if not [c for c, _ in FAILS if c == 'round-trip']:
    note('round-trip', "serialised, reloaded in a fresh process, same interpretation")

# 13c — DAC-0033 constraint 6: the VR schema contradiction stays explicit until TDR-0019 governs it.
# A constraint to leave something alone is testable, so it is tested rather than promised.
if 'finance_countersignatory' not in json.load(open('records/value/schema/vr.schema.json')).get('required', []):
    fail('vr-frozen', "the VR schema was changed under TDR-0033; that correction belongs to TDR-0019 "
                      "(DAC-0033 constraint 6)")

# 13d — the obligations register: every DAC constraint accounted for, in two independent fields
REG = yaml.safe_load(open('decisions/evidence/DAC-0032-0033-obligations.yaml'))
IMPL = {'pending', 'implemented', 'not-applicable'}
VERIF = {'pending', 'verified', 'release-gated', 'not-applicable'}
expected_ids = []
for dac, path in (('DAC-0032', 'decisions/DAC-0032-typed-multi-object-conformance.md'),
                  ('DAC-0033', 'decisions/DAC-0033-four-dimensional-validity.md')):
    body = open(path, encoding='utf-8').read().split('## Disposition')[-1]
    expected_ids += [f"{dac}#{n}" for n in
                     sorted(int(x) for x in re.findall(r'^(\d+)\. \*\*', body, re.M))]
rows = {r.get('id'): r for r in REG.get('obligations', [])}
for missing in [i for i in expected_ids if i not in rows]:
    fail('obligations', f"{missing} is a constraint of an accepted case and is not registered")
for extra in [i for i in rows if i not in expected_ids]:
    fail('obligations', f"{extra} is registered but is not a constraint of either case")
if len(rows) != len(REG.get('obligations', [])):
    fail('obligations', "duplicate constraint ids in the register")
for rid, r in rows.items():
    if r.get('implementation') not in IMPL:
        fail('obligations', f"{rid}: implementation {r.get('implementation')!r} is not one of {sorted(IMPL)}")
    if r.get('verification') not in VERIF:
        fail('obligations', f"{rid}: verification {r.get('verification')!r} is not one of {sorted(VERIF)}")
    for field in ('constraint', 'owner', 'measure', 'note'):
        if not str(r.get(field) or '').strip():
            fail('obligations', f"{rid}: {field} is empty")
    for ref in r.get('evidence') or []:
        if not os.path.exists(ref):
            fail('obligations', f"{rid}: evidence {ref} does not resolve")
    if r.get('verification') == 'verified' and not (r.get('evidence') or []):
        fail('obligations', f"{rid}: claimed verified with no evidence")
note('obligations', f"{len(rows)} constraints registered; "
     f"{sum(1 for r in rows.values() if r['verification'] == 'verified')} verified, "
     f"{sum(1 for r in rows.values() if r['verification'] == 'release-gated')} release-gated, "
     f"{sum(1 for r in rows.values() if r['verification'] == 'pending')} pending")

# 13e — the standards boundary register (TDR-0035): no row may be a bare verdict
DISPOSITIONS = {'adopt', 'map', 'interoperate', 'defer', 'reject'}
register = open('specification/standards-boundary.md', encoding='utf-8').read()
register_rows = 0
for row in re.findall(r'^\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|\s*$', register.split('## The register')[-1], re.M):
    name, disp, why, foreclosure = (c.strip() for c in row)
    if set(disp) <= set('- ') or disp == 'Disposition':
        continue
    register_rows += 1
    if disp not in DISPOSITIONS:
        fail('standards', f"{name}: disposition {disp!r} is not one of {sorted(DISPOSITIONS)}")
    if len(why) < 40:
        fail('standards', f"{name}: no reasoning — a disposition without one is a bare verdict")
    if len(foreclosure) < 20:
        fail('standards', f"{name}: nothing stated about what the disposition does not mean")
note('standards', f"{register_rows} dispositions, each reasoned and foreclosed")

# 14 — repository assessment. A typed TDR-0032 subject reporting the four TDR-0033 dimensions.
DIMENSION_OF = {
    'record-schema': Dim.STRUCTURAL, 'id-filename': Dim.STRUCTURAL, 'vr-example': Dim.STRUCTURAL,
    'vr-negative': Dim.STRUCTURAL, 'skill-frontmatter': Dim.STRUCTURAL, 'skill-name': Dim.STRUCTURAL,
    'skill-description': Dim.STRUCTURAL, 'skill-count': Dim.SEMANTIC, 'manifest': Dim.STRUCTURAL, 'result-fixture': Dim.STRUCTURAL, 'projection-fixture': Dim.STRUCTURAL,
    'candidate': Dim.SEMANTIC, 'boundary': Dim.SEMANTIC, 'neutrality': Dim.SEMANTIC,
    'consumer-name': Dim.SEMANTIC, 'fixture': Dim.SEMANTIC, 'must-not': Dim.SEMANTIC,
    'untyped-claim': Dim.SEMANTIC, 'vr-frozen': Dim.SEMANTIC, 'obligations': Dim.SEMANTIC,
    'standards': Dim.SEMANTIC,
    'lineage': Dim.RELATIONAL, 'link': Dim.RELATIONAL, 'allocation': Dim.RELATIONAL,
    'closure': Dim.RELATIONAL, 'round-trip': Dim.STRUCTURAL, 'bundle': Dim.SEMANTIC,
}
assessment = ValidationResult(
    'repository', 'mtdr', 'specification/conformance.md', '1.0.0', subject_ref='.',
    assessed_state='pre-release',
    requested_transition={'from': 'pre-release', 'to': 'released'},
    context={'id': 'clean-clone',
             'description': 'The working tree alone — no register, service or network.'},
    validator={'name': 'tests/verify.py', 'version': '1.0.0'})
for dim in (Dim.STRUCTURAL, Dim.SEMANTIC, Dim.RELATIONAL):
    hits = [(c, m) for c, m in FAILS if DIMENSION_OF.get(c) == dim]
    unknown = [(c, m) for c, m in FAILS if c not in DIMENSION_OF]
    if hits:
        assessment.report(dim, 'fail', reasons=[(c, m) for c, m in hits[:8]])
    elif unknown:
        assessment.report(dim, 'indeterminate',
                          reasons=[('unattributed-check', f"{c}: {m}") for c, m in unknown[:8]])
    else:
        assessment.report(dim, PASS)
# Eligibility for the DAC-0032/0033 release gate, derived from the obligations register rather than
# from a curated checklist (specification/obligation-chain.md). Reported, never acted on: a pass would
# mean the evidenced preconditions are satisfied and the request may be placed before whoever is
# authorised to decide it — not that anything may be released.
unmet = [(r['id'].lower().replace('#', '-'), f"{r['id']} — {r['constraint']}: implementation pending")
         for r in rows.values() if r['implementation'] == 'pending']
unproved = [(r['id'].lower().replace('#', '-'), f"{r['id']} — {r['constraint']}: verification {r['verification']}")
            for r in rows.values() if r['verification'] in ('pending', 'release-gated')]
if unmet:
    assessment.report(Dim.TRANSITION, 'fail', reasons=unmet[:8],
                      evidence=[('decisions/evidence/DAC-0032-0033-obligations.yaml',)])
elif unproved:
    assessment.report(Dim.TRANSITION, 'indeterminate', reasons=unproved[:8],
                      evidence=[('decisions/evidence/DAC-0032-0033-obligations.yaml',)])
else:
    assessment.report(Dim.TRANSITION, PASS,
                      evidence=[('decisions/evidence/DAC-0032-0033-obligations.yaml',)])

print()
if FAILS:
    for check, msg in FAILS:
        print(f"FAIL [{check}] {msg}")
    print()
print(assessment.summary())
print("""
The subject of this result is the repository. Under TDR-0032 it implies nothing about the
conformance of any record, package, skill or participant within it, and under TDR-0033 no dimension
above is overridden by any other. There is no aggregate verdict: the process exit status is an
operational signal about this run, not a conformance judgement (DAC-0032 #1, DAC-0033 #8).

Transition eligibility is computed from the obligations register, not from a curated checklist
(specification/obligation-chain.md). It reports whether the release gate's published prerequisites
are met. It is not release authority: it neither performs the release, authorises it, nor gives
anything standing — that remains an authorised human act under TDR-0027.""")
for e in assessment.validate():
    print(f"FAIL [self] the repository result violates its own contract: {e}")
    FAILS.append(('self', e))

if '--emit' in sys.argv:
    print(assessment.to_json(indent=2))
sys.exit(1 if FAILS else 0)
