---
name: crimson-ui-color
description: Focused color harmony, semantic palette roles, theme adaptation, and palette selection without loading unrelated design references.
---

# Color Harmony

Use for palette creation, palette repair, accent hierarchy, theme harmony, or color QA.


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
