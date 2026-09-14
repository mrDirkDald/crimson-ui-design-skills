---
name: crimson-ui-visual
description: Visual direction, typography, composition, imagery, identity, and iconography for meaningful redesign work.
---

# Visual Direction

Use for identity work, broad redesign, typography/composition decisions, imagery, or when the current visual system is incoherent.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Composition and Visual Hierarchy | `aspects/composition-hierarchy/SKILL.md` | Control visual mass, grouping, anchors, and action hierarchy across the entire surface. |
| Typography System | `aspects/typography-system/SKILL.md` | Build readable hierarchy, rhythm, density, and identity through type rather than arbitrary font-size jumps. |
| Imagery and Art Direction | `aspects/imagery-art-direction/SKILL.md` | Integrate images, screenshots, illustration, video, and backgrounds into the composition intentionally. |
| Identity and Product Specificity | `aspects/identity-specificity/SKILL.md` | Create a recognizable product language without relying on superficial branding. |
| Motion Language | `aspects/motion-language/SKILL.md` | Define motion as state, continuity, hierarchy, and brand expression rather than decoration. |
| Iconography and SVG | `aspects/iconography-svg/SKILL.md` | Maintain a coherent vector icon language with Lucide as the default fallback system. |

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
- meaningful redesign;
- new visual thesis;
- typography/composition/imagery system work;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Normally read only `../../references/visual-direction.md`.
Do not load color catalogs unless choosing concrete colors.
Do not load expressive-web unless the product explicitly needs an expressive/award-like experience.

## Visual thesis
Before broad styling changes define:
```text
SUBJECT:
AUDIENCE:
PRIMARY JOB:
TONE:
INTENSITY: quiet / balanced / expressive
VISUAL THESIS:
```

One strong governing idea is better than a stack of unrelated effects.

## Systemic harmony
If multiple visual layers conflict, replace the visual system coherently rather than patching component-by-component.

Preserve behavior and product meaning.

## Product specificity
Mentally remove logo, product name and hero image.
If the same layout/style could be relabeled for unrelated products with almost no change, strengthen domain-specific structure and interaction.

## Support competition
Secondary/helper surfaces must not receive the same visual mass as the primary task unless they are equally important.

## Background/media
Treat imagery as composition:
- focal point;
- crop;
- local contrast;
- content placement;
- responsive adaptation.

Do not hide a meaningful image under one uniform dark veil.

## Iconography
UI controls use SVG/vector iconography, not emoji.
Reuse one coherent family and normalize stroke/fill/optical size.

## Deep reference
Read `../../references/visual-direction.md` only when these decisions are material.
