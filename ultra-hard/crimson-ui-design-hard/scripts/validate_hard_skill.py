from pathlib import Path
import re, sys, json
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def need(rel):
    if not (ROOT/rel).exists(): errors.append(f"Missing: {rel}")

for rel in [
    'SKILL.md','README.md','MANIFEST.json','agents/openai.yaml','handbook/READING-MAP.md','handbook/HARD-INDEX.md',
    'handbook/stacks/language-toolkit-map.md','handbook/languages/unknown-language-toolkit.md',
    'handbook/core/iconography-lucide.md','handbook/core/color-system.md','handbook/qa/MASTER-CHECKLIST.md',
    'references/color-pairs.md','references/color-trios.md','references/color-palettes-4plus.md',
    'references/web-craft-analysis.md','references/skills-sh-patterns.md','references/anti-neuroslop-layout.md',
    'references/design-deliberation.md','references/hard-freeze-policy.md','subskills/tooling/SKILL.md'
]: need(rel)

md=list(ROOT.rglob('*.md'))
word_count=sum(len(p.read_text(encoding='utf-8',errors='ignore').split()) for p in md)
line_count=sum(len(p.read_text(encoding='utf-8',errors='ignore').splitlines()) for p in md)
if len(md) < 260: errors.append(f'Expected >=260 Markdown files, got {len(md)}')
if word_count < 220000: errors.append(f'Expected >=220000 words, got {word_count}')
if len(list((ROOT/'handbook'/'languages').glob('*.md'))) < 30: errors.append('Language handbook is not exhaustive enough')
if len(list((ROOT/'handbook'/'webcraft').glob('*.md'))) < 18: errors.append('Web-craft handbook is not exhaustive enough')

root=(ROOT/'SKILL.md').read_text(encoding='utf-8')
for literal in ['Crimson UI Design HARD','Programming language / toolkit rule','Runtime verification','Product-specificity gate','Human-crafted web / AI-default guard','Frozen-edition rule']:
    if literal not in root: errors.append(f'Root missing: {literal}')
if 'check_for_updates.py' in root: errors.append('HARD root must not route to self-updater')
if (ROOT/'scripts'/'check_for_updates.py').exists(): errors.append('HARD must not contain self-updater script')

# Secret-like string guard.
secret_re=re.compile(r'(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})')
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.py','.json','.yaml','.yml','.txt'}:
        txt=p.read_text(encoding='utf-8',errors='ignore')
        if secret_re.search(txt): errors.append(f'Secret-like token pattern in {p.relative_to(ROOT)}')

if errors:
    print('ERRORS:')
    for e in errors: print('-',e)
    sys.exit(1)
print(f'OK: Crimson UI Design HARD validated: {len(md)} markdown files, {line_count} lines, {word_count} words.')
