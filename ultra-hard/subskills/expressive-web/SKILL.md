---
name: crimson-ui-expressive-web
description: Expressive, editorial, studio, cultural, campaign, festival, luxury, experimental, or explicitly award-level web experiences.
---

# Expressive Web

Use only when spectacle/expressiveness is actually part of the product brief.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Experience Thesis | `aspects/experience-thesis/SKILL.md` | Reduce an expressive site to one memorable governing idea instead of an effect stack. |
| Scroll and Motion Choreography | `aspects/scroll-motion/SKILL.md` | Use scroll as spatial/narrative structure without hijacking basic navigation. |
| WebGL / 3D | `aspects/webgl-3d/SKILL.md` | Use 3D only when it materially strengthens product identity, explanation, or interaction. |
| Editorial Typography | `aspects/editorial-typography/SKILL.md` | Use expressive typography as structure and identity without sacrificing reading flow. |
| Media Art Direction | `aspects/media-art-direction/SKILL.md` | Use image, video, texture, collage, and masks as active compositional material. |
| Progressive Enhancement and Performance | `aspects/progressive-enhancement/SKILL.md` | Keep expressive sites usable when motion, JS, WebGL, audio, or high-end rendering is unavailable. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

## Owner reference

`../../references/expressive-web.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- motion/3D/scroll narrative is material;
- award-like interaction is explicitly requested;
- fallback/performance strategy matters;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Read `../../references/expressive-web.md`.
Also read `../../references/web-craft-analysis.md` for human-crafted page-level art direction and AI-default failure detection.
Do not load it for ordinary SaaS/admin/dashboard/utilities.

## One-thesis rule
Define:
```text
EXPERIENCE THESIS:
DOMINANT MOVE:
SUPPORTING MOTION:
WHAT STAYS QUIET:
```

The site should not become a pile of WebGL, custom cursors, pinned scroll, page wipes and giant type with no product reason.

## Product mapping
Turn subject matter into interaction/structure where useful.
Do not copy award-site effects literally.

## Progressive enhancement
Content and primary actions must remain understandable without advanced motion/WebGL.
Provide reduced-motion and lower-capability fallbacks.

## Mobile
Recompose the idea rather than merely shrinking it.


## HARD web-craft routing
Use the complete human-vs-AI craft gates in `references/web-craft-analysis.md` and the detailed chapters in `handbook/webcraft/`.
