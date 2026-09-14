from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]

def need(rel):
    if not (ROOT/rel).exists(): errors.append(f"Missing: {rel}")

for rel in [
    'SKILL.md','README.md','agents/openai.yaml','handbook/READING-MAP.md',
    'handbook/stacks/language-toolkit-map.md','handbook/core/iconography-lucide.md',
    'handbook/core/color-system.md','handbook/qa/MASTER-CHECKLIST.md',
    'references/color-pairs.md','references/color-trios.md','references/color-palettes-4plus.md'
]: need(rel)

md=list(ROOT.rglob('*.md'))
word_count=sum(len(p.read_text(encoding='utf-8').split()) for p in md)
if len(md) < 75: errors.append(f'Expected >=75 Markdown files, got {len(md)}')
if word_count < 50000: errors.append(f'Expected >=50000 words, got {word_count}')

root=(ROOT/'SKILL.md').read_text(encoding='utf-8')
for literal in ['Lucide Icons','Programming language / toolkit rule','Runtime verification','Product-specificity test']:
    if literal not in root: errors.append(f'Root missing: {literal}')

matrix=(ROOT/'handbook/stacks/language-toolkit-map.md').read_text(encoding='utf-8')
for language in ['C#','C++','Rust','Kotlin','Swift','Dart','Python','Go','Java','Lua','GDScript','Zig','Delphi','Elm','Haskell']:
    if language not in matrix: errors.append(f'Language map missing {language}')

if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'OK: Crimson UI Design MAX validated: {len(md)} markdown files, {word_count} words.')
