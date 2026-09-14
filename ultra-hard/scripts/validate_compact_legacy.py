from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def need(path):
    if not (ROOT/path).exists(): errors.append(f"Missing: {path}")
need("SKILL.md"); need("agents/openai.yaml")
subskills=["review","visual","color","web","application","design-system","implementation","expressive-web","electron","tauri","qa"]
for n in subskills: need(f"subskills/{n}/SKILL.md")
refs=["visual-direction.md","application.md","desktop-app.md","mobile-app.md","web.md","typescript-tailwind.md","design-system.md","expressive-web.md","electron.md","tauri-ui.md","tauri-native-security.md","visual-qa.md","accessibility-qa.md","visual-regression.md","color-pairs.md","color-trios.md","color-palettes-4plus.md"]
for r in refs: need(f"references/{r}")
root_text=(ROOT/"SKILL.md").read_text(encoding="utf-8")
for lit in ["TIER 0","TIER 1","TIER 2","TIER 3","smallest sufficient context that preserves decision quality","## Quality preservation gate","Lucide Icons","SVG icons, not emoji UI.","CRIMSON-UI-DESIGN-TESTS"]:
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
if (ROOT/"evaluation").exists(): errors.append("Runtime skill must not contain evaluation corpus")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("Skill: crimson-ui-design")
print("OK: progressive context tiers + owner-reference escalation + Lucide baseline validated.")
