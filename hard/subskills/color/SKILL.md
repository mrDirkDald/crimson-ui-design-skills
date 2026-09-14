---
name: crimson-ui-color
description: Focused color harmony, semantic palette roles, theme adaptation, and palette selection without loading unrelated design references.
---

# Color Harmony

Use for palette creation, palette repair, accent hierarchy, theme harmony, or color QA.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Color Harmony Theory | `aspects/harmony-theory/SKILL.md` | Choose hue relationships intentionally instead of assembling attractive swatches independently. |
| Semantic Color Tokens | `aspects/semantic-color-tokens/SKILL.md` | Map colors to stable interface meaning so components do not invent local palettes. |
| Light / Dark Theme Adaptation | `aspects/theme-adaptation/SKILL.md` | Preserve product identity and hierarchy across themes without mechanical inversion. |
| Color Accessibility | `aspects/color-accessibility/SKILL.md` | Ensure color remains readable and non-exclusive as a carrier of meaning. |
| Data Visualization Color | `aspects/data-color/SKILL.md` | Use categorical, sequential, diverging, and highlight palettes according to data semantics. |
| Palette Generation and Selection | `aspects/palette-generation/SKILL.md` | Generate concrete palettes from the brief while avoiding AI-default color clichés. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

## Owner reference

`../../references/visual-direction.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- palette roles are unclear;
- theme parity is involved;
- color affects hierarchy beyond swatch selection;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Do **not** load `visual-direction.md` for a color-only task.
Choose exactly one catalog only when concrete palette candidates are needed:
- 2 principal chromatic colors → `../../references/color-pairs.md`
- 3 → `../../references/color-trios.md`
- 4+ → `../../references/color-palettes-4plus.md`

Never load all three by default.

## Semantic roles
Define only roles that exist:
```text
CANVAS
SURFACE
SURFACE-ELEVATED
TEXT-PRIMARY
TEXT-SECONDARY
BORDER
ACCENT-PRIMARY
ACCENT-SECONDARY (optional)
SUCCESS
WARNING
DANGER
INFO
FOCUS
```

## Harmony
- choose hue relationships intentionally;
- keep one dominant action accent;
- separate brand colors from semantic status colors;
- use lightness hierarchy, not hue alone;
- avoid equal saturation everywhere;
- adapt light/dark themes as the same product, not mechanical inversions.

## Brief grounding
Derive color from subject, audience, product vernacular, materials, and workflow.

Challenge:
**Would this exact palette fit five unrelated products equally well?**
If yes, revise unless genericity is intentional.

## Accessibility
Harmony and contrast are separate gates.
Do not rely on red vs green or hue-only distinction for critical states.

## Stop
Once semantic roles, dominance, contrast, and theme behavior are coherent, stop adding colors.
