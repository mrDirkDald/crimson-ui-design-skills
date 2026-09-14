from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def need(path):
    if not (ROOT/path).exists(): errors.append(f"Missing: {path}")
need("SKILL.md"); need("agents/openai.yaml")
subskills=["review","design-strategy","visual","color","web","application","design-system","implementation","expressive-web","electron","tauri","qa","tooling"]
for n in subskills: need(f"subskills/{n}/SKILL.md")
refs=["tooling-sources.md","update-policy.md","design-deliberation.md","visual-direction.md","application.md","desktop-app.md","mobile-app.md","web.md","typescript-tailwind.md","design-system.md","expressive-web.md","electron.md","tauri-ui.md","tauri-native-security.md","visual-qa.md","accessibility-qa.md","visual-regression.md","color-pairs.md","color-trios.md","color-palettes-4plus.md","web-reference-corpus.md"]
for r in refs: need(f"references/{r}")

for extra in ["scripts/check_for_updates.py","release-manifest.json"]: need(extra)
root_text=(ROOT/"SKILL.md").read_text(encoding="utf-8")
for lit in ["## Design deliberation gate","subskills/design-strategy/SKILL.md","TIER 0","TIER 1","TIER 2","TIER 3","smallest sufficient context that preserves decision quality","## Quality preservation gate","Lucide Icons","SVG icons, not emoji UI.","CRIMSON-UI-DESIGN-TESTS","## Update check gate","subskills/tooling/SKILL.md","python scripts/check_for_updates.py --stage --json"]:
    if lit not in root_text: errors.append(f"Router missing: {lit}")
for n in subskills:
    p=ROOT/f"subskills/{n}/SKILL.md"
    if p.exists():
        t=p.read_text(encoding="utf-8")
        if "## Owner reference" not in t: errors.append(f"Subskill missing owner reference: {n}")
        if "### Escalation triggers" not in t: errors.append(f"Subskill missing escalation triggers: {n}")
for rel,lit in [("references/visual-direction.md","### Lucide baseline"),("references/design-system.md","### Lucide as default library"),("references/typescript-tailwind.md","### Lucide default for web UI"),("references/visual-qa.md","### Lucide consistency check")]:
    p=ROOT/rel
    if p.exists() and lit not in p.read_text(encoding="utf-8"): errors.append(f"Missing {lit} in {rel}")

for rel, lit in [
    ("references/design-deliberation.md","SELECTED DIRECTION:"),
    ("references/design-deliberation.md","Autonomous media contract"),
    ("references/web.md","## Contextual persistent actions"),
    ("references/web.md","## Semantic interactive controls"),
    ("references/expressive-web.md","## Attention and continuous-motion budget"),
    ("references/visual-qa.md","## Design choice QA gate"),
]:
    p=ROOT/rel
    if p.exists() and lit not in p.read_text(encoding="utf-8"):
        errors.append(f"Missing {lit} in {rel}")


for rel, lit in [
    ("references/web-reference-corpus.md","## Four-role triangulation"),
    ("references/web-reference-corpus.md","## Reference collage failure"),
    ("references/web.md","## Reference-led web redesign"),
    ("references/expressive-web.md","## Cross-source reference gate"),
    ("references/visual-qa.md","## Reference-integrity web QA"),
]:
    p=ROOT/rel
    if p.exists() and lit not in p.read_text(encoding="utf-8"):
        errors.append(f"Missing {lit} in {rel}")

if (ROOT/"evaluation").exists(): errors.append("Runtime skill must not contain evaluation corpus")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("Skill: crimson-ui-design")
print("OK: progressive context tiers + owner-reference escalation + Lucide baseline validated.")
