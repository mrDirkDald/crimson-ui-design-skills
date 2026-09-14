from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

parents = ["application", "color", "design-system", "electron", "expressive-web", "implementation", "qa", "review", "tauri", "visual", "web"]
expected_aspects = {
  "review": [
    "before-after-verification",
    "evidence-audit",
    "preservation-contract",
    "product-specificity-review",
    "refine-vs-redesign",
    "severity-prioritization"
  ],
  "visual": [
    "composition-hierarchy",
    "iconography-svg",
    "identity-specificity",
    "imagery-art-direction",
    "motion-language",
    "typography-system"
  ],
  "color": [
    "color-accessibility",
    "data-color",
    "harmony-theory",
    "palette-generation",
    "semantic-color-tokens",
    "theme-adaptation"
  ],
  "web": [
    "data-dense-web",
    "forms-validation",
    "navigation-routing",
    "responsive-layout",
    "web-performance-design",
    "web-state-feedback"
  ],
  "application": [
    "commands-shortcuts",
    "density-inspectors",
    "desktop-mobile-adaptation",
    "persistence-recovery",
    "selection-focus",
    "workflow-architecture"
  ],
  "design-system": [
    "component-contracts",
    "governance-drift",
    "icon-system",
    "migration-strategy",
    "theme-system",
    "token-architecture"
  ],
  "implementation": [
    "css-architecture",
    "design-to-code-verification",
    "react-typescript-tailwind",
    "responsive-implementation",
    "stateful-components",
    "svg-lucide"
  ],
  "expressive-web": [
    "editorial-typography",
    "experience-thesis",
    "media-art-direction",
    "progressive-enhancement",
    "scroll-motion",
    "webgl-3d"
  ],
  "electron": [
    "electron-security",
    "native-dialogs-menus",
    "preload-ipc",
    "renderer-ux",
    "updater-tray-deeplink",
    "window-shell"
  ],
  "tauri": [
    "capabilities-security",
    "commands-ipc",
    "filesystem-process-shell",
    "renderer-integration",
    "updater-tray-deeplink",
    "windows-state"
  ],
  "qa": [
    "accessibility-audit",
    "evidence-reporting",
    "interaction-state-audit",
    "responsive-cross-platform",
    "visual-hierarchy-audit",
    "visual-regression"
  ]
}

for path in ["SKILL.md", "README.md", "agents/openai.yaml"]:
    if not (ROOT/path).exists():
        errors.append(f"Missing {path}")

for parent in parents:
    parent_skill = ROOT/"subskills"/parent/"SKILL.md"
    if not parent_skill.exists():
        errors.append(f"Missing parent skill: {parent}")
        continue
    text = parent_skill.read_text(encoding="utf-8")
    if "## Deep aspect subskills" not in text:
        errors.append(f"Parent missing deep-aspect routing: {parent}")
    for aspect in expected_aspects[parent]:
        ap = ROOT/"subskills"/parent/"aspects"/aspect/"SKILL.md"
        if not ap.exists():
            errors.append(f"Missing aspect skill: {parent}/{aspect}")
        else:
            at = ap.read_text(encoding="utf-8")
            for required in ["## Purpose","## Evidence to collect","## Detailed rules","## Verification checklist","## Deliverable format"]:
                if required not in at:
                    errors.append(f"{parent}/{aspect} missing section {required}")

md = list(ROOT.rglob("*.md"))
aspect_files = list(ROOT.glob("subskills/*/aspects/*/SKILL.md"))

if len(aspect_files) != 66:
    errors.append(f"Expected 66 aspect skills, found {len(aspect_files)}")

root_text = (ROOT/"SKILL.md").read_text(encoding="utf-8")
if "## Nested subskill architecture" not in root_text:
    errors.append("Root missing nested subskill architecture")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"OK: Crimson UI Design MAX validated: {len(md)} markdown files, {len(aspect_files)} nested aspect skills.")
