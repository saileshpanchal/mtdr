#!/usr/bin/env python3
"""The repository's own conformance suite (TDR-0025).

Validates the repository against its own rules — run from the repository root:

    uv run --with pyyaml --with jsonschema python tests/verify.py

That form needs nothing installed first, which is the point: a conformance suite an adopter cannot
run from a clean clone proves less than it claims. Where the dependencies are already present,
`python3 tests/verify.py` is equivalent.

Checks: record schema validity · lineage resolution · id/filename agreement · skill frontmatter
discipline · relative-link resolution (stubs included) · package manifests coherent · candidate
packages hold metadata and scope only · package dependency boundary · shared-skill record-neutrality
· consumer-name scan over normative artefacts · VR negative cases still rejected · identifier
allocation register coherent, with next-free proved rather than trusted · the validation-result
contract accepting and rejecting its fixtures as published · no untyped conformance claim on a
normative surface · classified normative closure with no undeclared outward reference · must-not
probes over the reference implementation · a serialisation round-trip through a fresh process ·
the DAC-0032/0033 obligations register accounted for constraint by constraint · every standards-
boundary disposition reasoned and foreclosed · distribution bundles fresh, equivalent and
byte-identical to the canonical artefacts · the progressive-disclosure budget within its ceilings.

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
    sys.exit("verify.py requires pyyaml and jsonschema — run:\n"
             "    uv run --with pyyaml --with jsonschema python tests/verify.py")

FAILS = []
def fail(check, msg): FAILS.append((check, msg))
def note(check, msg): print(f"  {check}: {msg}")

def frontmatter(path):
    m = re.match(r'^---\n(.*?)\n---\n', open(path, encoding='utf-8').read(), re.S)
    return yaml.safe_load(m.group(1)) if m else None

def as_json(o):
    """YAML dates -> ISO strings, at every depth. Shallow coercion silently passed TDRs (whose dates
    are all top-level) and failed a DAC's nested `assurance` block."""
    if isinstance(o, dict):
        return {k: as_json(v) for k, v in o.items()}
    if isinstance(o, list):
        return [as_json(v) for v in o]
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    return o

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

# 3a — Agent Skills conformance (standards-boundary: `adopt`). `adopt` means MTDR uses it directly,
# as a named dependency — so the claim to prove is not "we have frontmatter" but that MTDR's
# contract is a STRICT PROFILE of the Agent Skills specification: every field MTDR permits is one
# the specification admits, and MTDR permits fewer. The six admitted fields are parsed out of
# `runtime-evidence.md` rather than restated here, so the prose and this check cannot drift apart.
evidence_text = open('skills/packaging/runtime-evidence.md', encoding='utf-8').read()
m = re.search(r'admits six frontmatter fields\s*—\s*((?:[^.]|\n)*?)\.', evidence_text)
AGENT_SKILL_FIELDS = set(re.findall(r'`([a-z-]+)`', m.group(1))) if m else set()
MTDR_SKILL_FIELDS = {'name', 'description'}
if len(AGENT_SKILL_FIELDS) != 6:
    fail('agent-skills', f"runtime-evidence.md states {len(AGENT_SKILL_FIELDS)} admitted fields, not six")
if not MTDR_SKILL_FIELDS <= AGENT_SKILL_FIELDS:
    fail('agent-skills', f"MTDR permits {sorted(MTDR_SKILL_FIELDS - AGENT_SKILL_FIELDS)}, which the "
                         f"Agent Skills specification does not admit — that is a divergence, not an "
                         f"adoption")
if not MTDR_SKILL_FIELDS < AGENT_SKILL_FIELDS:
    fail('agent-skills', "MTDR's contract is not narrower than the specification it profiles")
# a name the specification's loaders can address: lowercase, digits, single hyphens
NAME_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
for f in skills:
    fm = frontmatter(f) or {}
    if not NAME_RE.match(str(fm.get('name', ''))):
        fail('agent-skills', f"{f}: name {fm.get('name')!r} is not a portable skill name")
    if not str(fm.get('description', '')).strip():
        fail('agent-skills', f"{f}: empty description — the field a runtime selects on")
note('agent-skills', f"{len(skills)} skills profile {sorted(MTDR_SKILL_FIELDS)} of the "
                     f"specification's {len(AGENT_SKILL_FIELDS)}")

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
         + glob.glob('tests/validation/FIX-*.md') + glob.glob('tests/inspectability/FIX-*.md') \
         + glob.glob('tests/adoption/FIX-*.md')
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

# 10b — version-bound detached records (DAC-0032 constraint 2, TDR-0043). The obligations register
# warned that the serialisation round-trip "proves nothing about a detached record", so this does the
# thing the constraint actually asks: copy a record OUT, delete every trace of the repository from
# the resolver's reach, and resolve its type, specification and schema from `conforms_to` alone.
import tempfile, shutil                                                       # noqa: E402
BIND_RE = re.compile(r'^mtdr/([a-z][a-z-]*)/(tdr|dac|vr)@([0-9]+\.[0-9]+\.[0-9]+)$')
MANIFEST_VERSION = {}
for mpath in glob.glob('records/*/package.yaml'):
    man = yaml.safe_load(open(mpath, encoding='utf-8'))
    for entry in man.get('records') or []:
        MANIFEST_VERSION[(man['name'], entry['id'].lower())] = entry['specification_version']

governed = (sorted(glob.glob('decisions/TDR-*.md')) + sorted(glob.glob('decisions/DAC-*.md'))
            + sorted(glob.glob('records/*/examples/*.md')))
bound = 0
for f in governed:
    fm = frontmatter(f) or {}
    binding = fm.get('conforms_to')
    if not binding:
        fail('identity', f"{f}: no conforms_to — a governed record must bind its specification")
        continue
    m = BIND_RE.match(str(binding))
    if not m:
        fail('identity', f"{f}: conforms_to {binding!r} is not mtdr/<package>/<record>@<version>")
        continue
    pkg, rec, ver = m.groups()
    # the binding must agree with what this distribution actually ships (DAC-0043 constraint 2)
    shipped = MANIFEST_VERSION.get((pkg, rec))
    if shipped is None:
        fail('identity', f"{f}: claims package/record {pkg}/{rec}, which this distribution does not ship")
    elif shipped != ver:
        fail('identity', f"{f}: claims {rec}@{ver}; the {pkg} manifest ships {shipped}")
    bound += 1

# the detached proof itself, over one record of each family
DETACHED_SAMPLE = ['decisions/TDR-0043-version-bound-detached-records.md',
                   'decisions/DAC-0043-version-bound-detached-records.md']
DETACHED_SAMPLE += sorted(glob.glob('records/value/examples/*.md'))[:1]
for src in DETACHED_SAMPLE:
    with tempfile.TemporaryDirectory() as td:
        detached = os.path.join(td, os.path.basename(src))
        shutil.copyfile(src, detached)
        text = open(detached, encoding='utf-8').read()
        head = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        found = re.search(r'^conforms_to:\s*(\S+)$', head.group(1), re.M) if head else None
        if not found:
            fail('identity', f"detached {src}: carries no binding once separated"); continue
        g = BIND_RE.match(found.group(1))
        if not g:
            fail('identity', f"detached {src}: binding unparseable in isolation"); continue
        pkg, rec, ver = g.groups()
        # resolution BY RULE — the path is derived from the identifier, never looked up
        schema_path = f'records/{pkg}/schema/{rec}.schema.json'
        if not os.path.exists(schema_path):
            fail('identity', f"detached {src}: {rec}@{ver} resolves to {schema_path}, which is absent")
            continue
        obj = as_json(yaml.safe_load(head.group(1)))
        errs = list(Validator(json.load(open(schema_path))).iter_errors(obj))
        if errs:
            fail('identity', f"detached {src}: resolved its own schema and failed it — {errs[0].message}")
note('identity', f"{bound} governed records bound; {len(DETACHED_SAMPLE)} resolved and validated "
                 f"detached, by rule")

# 10c — the extraction trial (DAC-0032 constraint 3). The declaration's COMPLETENESS is proved by the
# closure check below; what that cannot show is whether an extracted package actually stands up
# elsewhere. The register was explicit: "Half proved, and the half matters… What has not been done is
# the extraction trial itself: taking a package out and running its conformance contract elsewhere."
# So: copy a package and exactly its declared dependencies into an empty directory, and run its
# conformance contract there — with nothing else reachable.
def extraction_trial(pkg_dir):
    man = yaml.safe_load(open(f'{pkg_dir}/package.yaml', encoding='utf-8'))
    declared = [d['ref'] for d in (man.get('dependencies') or []) if d.get('class') == 'normative']
    with tempfile.TemporaryDirectory() as td:
        shutil.copytree(pkg_dir, os.path.join(td, pkg_dir))
        for ref in declared:                      # ONLY what the manifest declares
            src = ref.rstrip('/')
            if os.path.isdir(src):
                shutil.copytree(src, os.path.join(td, src), dirs_exist_ok=True)
            elif os.path.isfile(src):
                os.makedirs(os.path.join(td, os.path.dirname(src)), exist_ok=True)
                shutil.copyfile(src, os.path.join(td, src))
            else:
                return [f"declared dependency {ref} does not exist"]
        problems = []
        cwd = os.getcwd()
        try:
            os.chdir(td)                          # nothing outside the extraction is reachable
            by_type = {}
            for entry in man.get('records') or []:
                schema_rel = os.path.join(pkg_dir, entry['schema'])
                if not os.path.exists(schema_rel):
                    problems.append(f"{entry['id']}: schema absent from the extraction"); continue
                by_type[entry['id'].lower()] = Validator(json.load(open(schema_rel)))
            subjects = sorted(glob.glob(f'{pkg_dir}/examples/*.md'))
            if not subjects:
                problems.append('no example to run the contract against')
            for subj in subjects:
                fm2 = frontmatter(subj)
                if fm2 is None:
                    problems.append(f"{subj}: unreadable in the extraction"); continue
                # the extraction resolves a subject's type the way a detached reader must:
                # from its own binding, falling back to its identifier
                b = (fm2 or {}).get('conforms_to')
                g = BIND_RE.match(str(b)) if b else None
                if b and not g:
                    problems.append(f"{subj}: binding unusable in the extraction"); continue
                rec = g.group(2) if g else ('dac' if 'tdr_id' in fm2 else
                                            str(fm2.get('id', '')).split('-')[0].lower())
                v = by_type.get(rec)
                if v is None:
                    problems.append(f"{subj}: resolves to {rec}, which this package does not ship")
                    continue
                for e in v.iter_errors(as_json(fm2)):
                    problems.append(f"{subj}: {e.message}")
            # The constraint permits the wider corpus to "remain durably referenced", so an
            # unresolved link is NOT itself a failure. What must hold is narrower and stricter:
            # every NORMATIVE dependency is present and usable here, and nothing unresolved is
            # undeclared. A reference classified `provenance` or `explanatory` may dangle in an
            # extraction — that is what durable reference means.
            for ref in declared:
                if not os.path.exists(ref.rstrip('/')):
                    problems.append(f"normative dependency {ref} did not survive extraction")
            all_declared = {d['ref'].rstrip('/') for d in (man.get('dependencies') or [])}
            for md in glob.glob(f'{pkg_dir}/**/*.md', recursive=True):
                body = open(md, encoding='utf-8').read()
                for target in re.findall(r'\]\((?!https?:|#)([^)#]+)', body):
                    resolved = os.path.normpath(os.path.join(os.path.dirname(md), target))
                    if os.path.exists(resolved):
                        continue
                    if resolved in all_declared or any(
                            resolved.startswith(d + os.sep) for d in all_declared):
                        continue                  # declared, durably referenced, legitimately absent
                    problems.append(f"{md} -> {target}: unresolved AND undeclared")
        finally:
            os.chdir(cwd)
        return problems

trials = 0
for pkg_dir in sorted(glob.glob('records/*')):
    man_path = f'{pkg_dir}/package.yaml'
    if not os.path.exists(man_path):
        continue
    if (yaml.safe_load(open(man_path, encoding='utf-8')) or {}).get('status') != 'normative':
        continue                                   # a candidate package carries no contract to run
    for problem in extraction_trial(pkg_dir):
        fail('extraction', f"{pkg_dir}: {problem}")
    trials += 1
note('extraction', f"{trials} normative packages extracted with only their declared dependencies, "
                   f"and passed their conformance contract there")

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

# 12c — surface descriptors describe exactly what is generated, and nothing unclaimed is emitted.
# The standards boundary puts Agent plugin packaging at `interoperate`, whose foreclosure column
# says a packaging "may explain how to invoke a skill. It may add no record semantics." Every
# verified runtime turned out to be `direct` — canonical SKILL.md files collected, nothing
# transformed — so NO plugin or extension manifest is produced. That absence is asserted here
# rather than left as a fact about the current tree, because the cheapest way to drift across a
# disposition is to generate an artefact nobody decided to claim.
UNCLAIMED_ARTEFACTS = ('plugin.json', 'gemini-extension.json', 'marketplace.json',
                       '.claude-plugin', 'extension.json', 'manifest.json')
for root, dirs, filenames in os.walk('skills/packaging'):
    for entry in list(dirs) + filenames:
        if entry in UNCLAIMED_ARTEFACTS:
            fail('surfaces', f"{os.path.join(root, entry)}: a packaging artefact no disposition "
                             f"claims — Agent plugin packaging is `interoperate`, not a producer of "
                             f"plugin manifests")

# a generated descriptor must still say what the evidence says: an edit to the generated file is
# drift, and the descriptor is the only place a runtime's verified behaviour is recorded
DESCRIPTOR_FIELDS = ('title', 'class', 'confidence', 'source', 'project_paths', 'personal_paths',
                     'also_accepts', 'invocation', 'progressive_disclosure', 'unverified')
for key, spec in SURFACES.items():
    d = yaml.safe_load(open(f'skills/packaging/{key}/surface.yaml'))
    if d.get('surface') != key:
        fail('surfaces', f"{key}: descriptor names itself {d.get('surface')!r}")
    for field in DESCRIPTOR_FIELDS:
        if d.get(field) != spec.get(field):
            fail('surfaces', f"{key}.{field}: descriptor says {d.get(field)!r}, the verified "
                             f"evidence says {spec.get(field)!r}")
    if d.get('class') == 'direct' and 'byte-identical' not in str(d.get('transformation', '')):
        fail('surfaces', f"{key}: class is `direct` but the descriptor does not state that the "
                         f"canonical files are copied unmodified")
direct = sum(1 for v in SURFACES.values() if v['class'] == 'direct')
note('surfaces', f"{len(SURFACES)} descriptors match their evidence; {direct} direct; "
                 f"no unclaimed packaging artefact")

# 12c — progressive disclosure: selecting and running one skill must not cost the whole corpus
sys.path.insert(0, os.path.join(os.getcwd(), 'tests', 'adoption'))
import disclosure  # noqa: E402

budget_lines, budget_problems = disclosure.report()
for b in budget_problems:
    fail('disclosure', b)
_cat_pct, _run_pct = budget_lines[1].split()[-1], budget_lines[-1].split('bytes')[1].split()[0]
note('disclosure', f"catalogue {_cat_pct} of the corpus; the most demanding skill and its "
                   f"references {_run_pct}")

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

# 13c — state-relative requirements are represented state-relatively (TDR-0039). The VR is the worked
# case: a counter-signatory is required to *become* ratified, never to *exist* as a candidate.
_vr = {"id": "VR-9999", "title": "probe", "status": "candidate", "realisation": "not-started",
       "linked_decisions": "TDR-9999", "beneficiary": "x", "committed_by": "y", "authority": "z",
       "value_kind": "cost", "reconcile_by": "2028-03-31", "procurement_stage": "exploration",
       "supersedes": "none", "derived_from": "none"}
if list(vr_schema.iter_errors(_vr)):
    fail('state-relative', "a candidate VR lacking only a finance counter-signatory is rejected — "
                           "a transition requirement has leaked into the structural one (TDR-0039)")
for _st in ('ratified', 'settled'):
    _probe = {**_vr, 'status': _st, **({'realisation': 'realised'} if _st == 'settled' else {})}
    if not list(vr_schema.iter_errors(_probe)):
        fail('state-relative', f"a {_st} VR with no finance counter-signatory validated — the "
                               "requirement has been loosened past the state that needs it")
note('state-relative', "candidate valid without a counter-signatory; ratified and settled are not")

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

# 13f — the layer summary must agree with the register it summarises (TDR-0035). The check above
# reads only what follows `## The register`; the layer table sits before it and nothing read it, so
# a summary drifted out of agreement with its own source and the suite could not see it. A check
# scoped to one half of a document is a check that guarantees the other half.
DISPOSITION_OF_PHRASE = {'adopted': 'adopt', 'mapped': 'map', 'interoperated with': 'interoperate',
                         'deferred': 'defer', 'rejected': 'reject'}
register_disposition = {}
for row in re.findall(r'^\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|\s*$', register.split('## The register')[-1], re.M):
    name, disp = (c.strip() for c in row[:2])
    if set(disp) <= set('- ') or disp == 'Disposition':
        continue
    register_disposition[name.replace('*', '').strip()] = disp

layer_rows = 0
for row in re.findall(r'^\|(.+?)\|(.+?)\|(.+?)\|\s*$', register.split('## The register')[0], re.M):
    owner = row[2].strip()
    m = re.match(r'^(.*?)\s+—\s+[*_]{1,2}([^*_]+)[*_]{1,2}', owner)
    if not m:
        continue
    name, phrase = m.group(1).replace('*', '').strip(), m.group(2).strip().lower()
    if name not in register_disposition:
        continue                      # MTDR and authorised human acts own themselves
    layer_rows += 1
    stated = DISPOSITION_OF_PHRASE.get(phrase)
    if stated is None:
        fail('standards', f"layer summary: {name!r} states {phrase!r}, which is not a disposition")
    elif stated != register_disposition[name]:
        fail('standards', f"layer summary says {name} is {stated!r}; the register says "
                          f"{register_disposition[name]!r} — the register is the authority")
note('standards', f"{layer_rows} layer rows agree with the register")

# 14 — repository assessment. A typed TDR-0032 subject reporting the four TDR-0033 dimensions.
DIMENSION_OF = {
    'record-schema': Dim.STRUCTURAL, 'id-filename': Dim.STRUCTURAL, 'vr-example': Dim.STRUCTURAL,
    'vr-negative': Dim.STRUCTURAL, 'skill-frontmatter': Dim.STRUCTURAL, 'skill-name': Dim.STRUCTURAL,
    'skill-description': Dim.STRUCTURAL, 'skill-count': Dim.SEMANTIC, 'manifest': Dim.STRUCTURAL, 'result-fixture': Dim.STRUCTURAL, 'projection-fixture': Dim.STRUCTURAL,
    'candidate': Dim.SEMANTIC, 'boundary': Dim.SEMANTIC, 'neutrality': Dim.SEMANTIC,
    'consumer-name': Dim.SEMANTIC, 'fixture': Dim.SEMANTIC, 'must-not': Dim.SEMANTIC,
    'untyped-claim': Dim.SEMANTIC, 'state-relative': Dim.SEMANTIC, 'obligations': Dim.SEMANTIC,
    'standards': Dim.SEMANTIC,
    'lineage': Dim.RELATIONAL, 'link': Dim.RELATIONAL, 'allocation': Dim.RELATIONAL,
    'closure': Dim.RELATIONAL, 'round-trip': Dim.STRUCTURAL, 'bundle': Dim.SEMANTIC,
    'disclosure': Dim.SEMANTIC,
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
