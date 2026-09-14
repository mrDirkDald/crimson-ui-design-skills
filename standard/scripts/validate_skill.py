#!/usr/bin/env python3
from pathlib import Path
import re, sys, json, hashlib, subprocess, yaml
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'SKILL.md'
errors=[]; warnings=[]
def txt(p): return p.read_text(encoding='utf-8') if p.exists() else ''
def req(cond,msg):
    if not cond: errors.append(msg)
def warn(cond,msg):
    if not cond: warnings.append(msg)

req(SKILL.exists(),'Missing SKILL.md')
s=txt(SKILL)
req(len(s.splitlines())<=430,f'SKILL.md too long: {len(s.splitlines())} > 430')
m=re.match(r'^---\n(.*?)\n---\n',s,re.S); req(bool(m),'Missing frontmatter')
if m:
    fm=m.group(1)
    name=re.search(r'^name:\s*(.+)$',fm,re.M); desc=re.search(r'^description:\s*(.+)$',fm,re.M)
    req(bool(name),'Missing name'); req(bool(desc),'Missing description')
    if name:
        n=name.group(1).strip().strip('"\''); req(n==ROOT.name,f'Folder {ROOT.name} != name {n}'); req(bool(re.fullmatch(r'[a-z0-9-]{1,64}',n)),'Invalid skill name')
    if desc:
        d=desc.group(1).lower(); req('do not activate' in d,'Frontmatter needs explicit non-trigger guidance'); req('ordinary frontend' in d,'Frontmatter should exclude ordinary frontend work')

# Reachability/orphans
refs=set(re.findall(r'`(references/[A-Za-z0-9._/-]+\.md)`',s))
allrefs={p.relative_to(ROOT).as_posix() for p in (ROOT/'references').glob('*.md')}
graph={}
for rel in ['SKILL.md']+sorted(allrefs): graph[rel]=set(re.findall(r'`(references/[A-Za-z0-9._/-]+\.md)`',txt(ROOT/rel)))
reach=set(); stack=['SKILL.md']
while stack:
    cur=stack.pop()
    if cur in reach: continue
    reach.add(cur); stack.extend(graph.get(cur,[]))
req(not (allrefs-reach),'Orphaned references: '+', '.join(sorted(allrefs-reach)))
for r in refs: req((ROOT/r).exists(),f'Missing reference {r}')

# Routing completeness
for literal in ['references/application.md','references/desktop-app.md','references/mobile-app.md','references/web.md','references/tauri-ui.md','references/tauri-native-security.md','references/electron.md','references/typescript-tailwind.md','references/design-system.md','references/visual-qa.md','references/accessibility-qa.md','references/visual-regression.md','references/evaluation.md','references/expressive-web.md']:
    req(literal in s,f'Missing routing: {literal}')

# Reference content contracts
contracts={
 'application.md':['Native auth / account / session','Sync / offline','Shared background task model'],
 'desktop-app.md':['Window model','Editors / creative tools','File/content managers','Desktop accessibility'],
 'mobile-app.md':['Software keyboard / IME','Permissions','Lifecycle / interruption / restoration','Mobile accessibility'],
 'visual-qa.md':['Evidence protocol','Severity','Runtime packet','State matrix','Overflow / clipping'],
 'accessibility-qa.md':['WCAG 2.2','4.5:1','3:1','24 × 24 CSS px','Screen reader','Native accessibility'],
 'visual-regression.md':['Cross-browser matrix','Desktop runtime matrix','Automated screenshot regression','Visual diff tolerance','Artifact contract'],
 'design-system.md':['Component regression strategy','Component contract tests','Theme coverage matrix','Component accessibility contract matrix','Component release regression gate'],
 'electron.md':['contextBridge API surface','contextIsolation','webSecurity','Session permission handlers','Window-open policy','Security regression tests'],
 'tauri-ui.md':['Versioned DTO evolution','Restart / reconnect recovery','Worker / child-process crash recovery','Task journal / reconciliation pattern'],
 'tauri-native-security.md':['TOCTOU-sensitive filesystem patterns','Capability audit','Security regression tests','Capability diff review'],
 'typescript-tailwind.md':['Framework-level UI state ownership','Server / client / hydration boundaries','Async UI state model','Error boundary / async failure ownership'],
 'visual-direction.md':['Visual reference process','Imagery / illustration direction','Accessibility constraints during direction','Measurable typography and rhythm checks','Optical rhythm review','Color harmony system','Hue relationship','Theme harmony','Color-blind safety'],
 'expressive-web.md':['Award-site bias guard','One-thesis rule','Subject-to-experience mapping','Scroll narrative and pacing','Motion choreography','Immersive 3D / WebGL','Responsive recomposition','Trend saturation penalty','Reference synthesis'],
}
for fn,lits in contracts.items():
    data=txt(ROOT/'references'/fn)
    for lit in lits: req(lit in data,f'{fn} missing content contract: {lit}')


# Color harmony coverage
for fn,lits in {
 'design-system.md':['Color token architecture','Theme color parity','Color drift detection'],
 'visual-qa.md':['Color harmony gate'],
 'web.md':['Data color semantics'],
 'typescript-tailwind.md':['Tailwind color harmony discipline'],
}.items():
    data=txt(ROOT/'references'/fn)
    for lit in lits: req(lit in data,f'{fn} missing color-harmony contract: {lit}')


# Systemic harmony / specificity coverage
for fn,lits in {
 'SKILL.md':['Systemic harmony override'],
 'visual-direction.md':['Duplicate Action Gate','Product-Specificity Gate','Support-Surface Competition Gate','Background Image Integration Gate','Harmony repair strategy'],
 'visual-qa.md':['Systemic visual harmony gate','Duplicate Action QA','Product-Specificity QA','Support-Surface Competition QA','Background Integration QA','Expressive / spectacle QA gate'],
 'web.md':['Expressive web routing'],
}.items():
    data=txt(ROOT/fn) if fn=='SKILL.md' else txt(ROOT/'references'/fn)
    for lit in lits: req(lit in data,f'{fn} missing systemic/expressive contract: {lit}')
req('references/expressive-web.md' in s,'SKILL.md missing conditional expressive-web routing')

# Large refs need TOC
for p in sorted((ROOT/'references').glob('*.md')):
    data=txt(p)
    if len(data.splitlines())>120: warn('## Contents' in data[:1400],f'{p.name}: >120 lines without early Contents')

# Agent config — parse YAML, then validate the supported interface contract.
ay=ROOT/'agents/openai.yaml'; req(ay.exists(),'agents/openai.yaml missing')
if ay.exists():
    try:
        cfg=yaml.safe_load(txt(ay))
        req(isinstance(cfg,dict),'openai.yaml root must be a mapping')
        interface=cfg.get('interface') if isinstance(cfg,dict) else None
        req(isinstance(interface,dict),'openai.yaml interface must be a mapping')
        if isinstance(interface,dict):
            for k in ['display_name','short_description','default_prompt']:
                req(isinstance(interface.get(k),str) and interface.get(k).strip(),f'openai.yaml interface.{k} missing/empty')
            req(len(interface.get('short_description',''))<=120,'openai.yaml short_description too long (>120)')
    except Exception as e:
        errors.append(f'openai.yaml YAML parse failed: {e}')

# Evaluation infrastructure
for rel in ['evaluation/run.schema.json','evaluation/benchmark.schema.json','scripts/aggregate_evaluation.py','scripts/score_benchmark_run.py','scripts/run_fixture_checks.py']:
    req((ROOT/rel).exists(),f'Missing evaluation infrastructure: {rel}')

# Fixture corpus subprocess validation
vf=ROOT/'scripts/validate_fixture_corpus.py'; req(vf.exists(),'validate_fixture_corpus.py missing')
if vf.exists():
    r=subprocess.run([sys.executable,str(vf)],capture_output=True,text=True)
    req(r.returncode==0,'Fixture corpus validation failed: '+r.stdout[:800])

# Benchmark specs 13 and alignment
bdir=ROOT/'evaluation/benchmarks'; specs=sorted(bdir.glob('*.json')) if bdir.exists() else []
req(len(specs)>=13,f'Expected >=13 benchmark specs, found {len(specs)}')
expected={'tiny-refine','desktop-queue','native-editor','mobile-native','web-auth','dashboard-chart','ecommerce','docs-developer','tauri-ipc','tauri-security','electron-security','expressive-media','expressive-web','qa-only'}
ids=set()
for p in specs:
    try: d=json.loads(txt(p)); ids.add(d.get('id'))
    except Exception as e: errors.append(f'{p.name}: invalid JSON {e}'); continue
    for key in ['task','starting_state','acceptance','required_evidence','machine_checks']: req(key in d,f'{p.name} missing {key}')
req(not(expected-ids),'Missing benchmark specs: '+', '.join(sorted(expected-ids-ids)))

# Exact long-sentence duplication heuristic
files=[SKILL]+sorted((ROOT/'references').glob('*.md')); seen={}; dup=0
for f in files:
    chunks=re.split(r'(?<=[.!?])\s+|\n+',txt(f))
    for c in chunks:
        c=re.sub(r'^[#>*\-\d.\s]+','',c).strip().lower(); c=re.sub(r'\s+',' ',c)
        if len(c)<100: continue
        h=hashlib.sha1(c.encode()).hexdigest()
        if h in seen and seen[h]!=f.name: dup+=1
        else: seen[h]=f.name
warn(dup<=8,f'High exact long-sentence duplication: {dup}')


# Anti-neuroslop coverage
req((ROOT/'references'/'anti-neuroslop-layout.md').exists(), 'Missing anti-neuroslop-layout.md')
req('references/anti-neuroslop-layout.md' in s, 'SKILL.md missing anti-neuroslop routing')
for fn, lits in {
    'visual-direction.md': ['Anti-cardification and surface economy', 'Whole-screen silhouette', 'Container necessity'],
    'application.md': ['Application layout archetype before cards', 'Device configurator rule', 'Density by frequency'],
    'desktop-app.md': ['Desktop chrome-to-content ratio'],
    'visual-qa.md': ['Anti-neuroslop / cardification QA gate', 'Surface economy QA', 'Whole-screen silhouette QA'],
    'design-deliberation.md': ['Surface-model comparison'],
}.items():
    data = txt(ROOT/'references'/fn)
    for lit in lits:
        req(lit in data, f'{fn} missing anti-neuroslop rule: {lit}')


# Tooling and update coverage
for rel in [
    'subskills/tooling/SKILL.md',
    'references/tooling-sources.md',
    'references/update-policy.md',
    'scripts/check_for_updates.py',
    'release-manifest.json',
]:
    req((ROOT/rel).exists(), f'Missing tooling/update file: {rel}')

for literal in [
    '## 5A. Canonical update gate',
    'subskills/tooling/SKILL.md',
    'python scripts/check_for_updates.py --stage --json',
    'https://github.com/mrDirkDald/crimson-ui-design-skill',
]:
    req(literal in s, f'SKILL.md missing update/tool routing: {literal}')

tooling_text = txt(ROOT/'subskills'/'tooling'/'SKILL.md')
for literal in ['fchek', 'skill-check', 'npm-safe', 'Tool trust tiers', 'Before installing a new tool']:
    req(literal in tooling_text, f'Tooling subskill missing: {literal}')

update_text = txt(ROOT/'references'/'update-policy.md')
for literal in ['GitHub Releases', 'no GitHub personal access token', 'SHA-256', 'does not execute any downloaded script']:
    req(literal in update_text, f'Update policy missing: {literal}')


# Skills.sh synthesis coverage
req((ROOT/'references'/'skills-sh-patterns.md').exists(), 'Missing skills-sh-patterns.md')
req('references/skills-sh-patterns.md' in s, 'SKILL.md missing skills.sh pattern routing')
for fn, lits in {
    'skills-sh-patterns.md': ['Deterministic process, variable output','Three operating dials','Fresh-guideline audit pattern','Bounded finishing passes','Trigger discrimination for skill quality','Pattern inheritance filter'],
    'visual-direction.md': ['Design operating dials','Characteristic-anchor gate','Pattern inheritance filter'],
    'visual-qa.md': ['Bounded finishing-pass protocol'],
    'design-system.md': ['Component API pressure test'],
    'web.md': ['Fresh external-guideline audit'],
    'evaluation.md': ['Trigger discrimination evaluation','Process determinism evaluation'],
}.items():
    data=txt(ROOT/'references'/fn)
    for lit in lits:
        req(lit in data, f'{fn} missing skills.sh-derived rule: {lit}')
req('skills.sh discovery rule' in tooling_text, 'Tooling subskill missing skills.sh discovery rule')


# Human-crafted web coverage
req((ROOT/'references'/'web-craft-analysis.md').exists(), 'Missing web-craft-analysis.md')
req('references/web-craft-analysis.md' in s, 'SKILL.md missing human-crafted web routing')
for fn, lits in {
    'web-craft-analysis.md': ['Human-crafted strengths','AI-default failure signatures','Human art-direction workflow','Human-vs-AI comparison matrix','Beautiful-site acceptance gates','Reference-study protocol'],
    'web.md': ['Beautiful / distinctive website routing','Whole-page craft','AI-default rejection gate','Responsive art direction'],
    'expressive-web.md': ['Human-craft escalation','Static composition before motion','Scene-based page design','Controlled irregularity','Memorable-moment budget','Typography choreography'],
    'visual-qa.md': ['Human-craft web QA gate','Section shuffle QA','Asset substitution QA','Five-second memory QA','AI-default signature QA'],
    'design-deliberation.md': ['Beautiful-web direction comparison'],
}.items():
    data=txt(ROOT/'references'/fn)
    for lit in lits:
        req(lit in data, f'{fn} missing human-crafted web rule: {lit}')

# Standard extension coverage
for ref in [
    'references/color-pairs.md',
    'references/color-trios.md',
    'references/color-palettes-4plus.md',
    'references/design-deliberation.md',
]:
    req((ROOT/ref).exists(), f'Missing Standard reference: {ref}')

for literal in [
    'references/color-pairs.md',
    'references/color-trios.md',
    'references/color-palettes-4plus.md',
    'references/design-deliberation.md',
    'Lucide Icons',
]:
    req(literal in s, f'SKILL.md missing Standard routing/rule: {literal}')

for fn, lits in {
    'visual-direction.md': [
        'Brief-grounded palette planning',
        'Palette recipe references',
        'Deliberate direction selection',
        'Role-based typography grammar',
        'Recurrent visual grammar',
        'Media normalization and local contrast',
        'Attention budget',
        'Contextual persistent action',
        'Autonomous media contract',
        'Cross-input equivalence',
        'Semantic control gate',
        'Success integrity',
        'Reference extraction discipline',
        'Lucide baseline',
    ],
    'design-system.md': ['Lucide baseline icon system'],
    'typescript-tailwind.md': ['Lucide default implementation'],
    'web.md': ['Semantic controls and success integrity', 'Contextual sticky actions', 'Autonomous carousel / reel behavior'],
    'visual-qa.md': ['Design deliberation QA', 'Attention-budget QA', 'Semantic control QA', 'Success integrity QA', 'Cross-input interaction QA', 'Lucide consistency QA'],
}.items():
    data = txt(ROOT/'references'/fn)
    for lit in lits:
        req(lit in data, f'{fn} missing Standard extension: {lit}')

# Report
print(f'Skill: {ROOT.name}')
if errors:
    print('ERRORS:'); [print('-',e) for e in errors]
if warnings:
    print('WARNINGS:'); [print('-',w) for w in warnings]
if not errors and not warnings:
    print('OK: structural + semantic + fixture checks passed.')
elif not errors:
    print('OK WITH WARNINGS: no blocking errors.')
sys.exit(1 if errors else 0)
