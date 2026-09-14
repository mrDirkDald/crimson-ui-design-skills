from pathlib import Path
import re, sys, json
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def need(rel):
    if not (ROOT/rel).exists(): errors.append(f"Missing: {rel}")
for rel in [
    'SKILL.md','README.md','MANIFEST.json','agents/openai.yaml',
    'handbook/ultra/ULTRA-INDEX.md','handbook/ultra/OPERATING-MANUAL.md',
    'references/web-craft-analysis.md','references/anti-neuroslop-layout.md',
    'references/design-deliberation.md','references/hard-freeze-policy.md',
    'subskills/tooling/SKILL.md'
]: need(rel)
md=list(ROOT.rglob('*.md'))
chars=sum(len(p.read_text(encoding='utf-8',errors='ignore')) for p in md)
words=sum(len(p.read_text(encoding='utf-8',errors='ignore').split()) for p in md)
lines=sum(len(p.read_text(encoding='utf-8',errors='ignore').splitlines()) for p in md)
if len(md) < 430: errors.append(f'Expected >=430 Markdown files, got {len(md)}')
if words < 500000: errors.append(f'Expected >=500000 words, got {words}')
if chars < 3500000: errors.append(f'Expected >=3.5M Markdown chars, got {chars}')
if len(list((ROOT/'handbook'/'ultra').rglob('*.md'))) < 110: errors.append('ULTRA layer is not deep enough')
root=(ROOT/'SKILL.md').read_text(encoding='utf-8')
for literal in ['Crimson UI Design HARD','ULTRA-HARD deep layer','no token economy','Runtime verification','Product-specificity gate']:
    if literal.lower() not in root.lower(): errors.append(f'Root missing: {literal}')
if (ROOT/'scripts'/'check_for_updates.py').exists(): errors.append('Frozen HARD/ULTRA-HARD must not contain self-updater')
secret_re=re.compile(r'(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})')
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.py','.json','.yaml','.yml','.txt'}:
        if secret_re.search(p.read_text(encoding='utf-8',errors='ignore')):
            errors.append(f'Secret-like token pattern in {p.relative_to(ROOT)}')
if errors:
    print('ERRORS:'); [print('-',e) for e in errors]; sys.exit(1)
print(f'OK: ULTRA-HARD validated: {len(md)} markdown files, {lines} lines, {words} words, {chars} markdown chars.')
