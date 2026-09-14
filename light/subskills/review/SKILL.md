---
name: crimson-ui-review
description: Focused UI/UX diagnosis, preservation, refine-vs-redesign decisions, and scope control.
---

# Review / Refine

Use this as the default primary subskill for UI review or improvement requests.


## Owner reference

`../../references/visual-direction.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- systemic redesign;
- identity/composition materially changes;
- visual harmony is a root cause;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
- Do not recursively inspect every skill/reference file.
- Start from the target surface and actual rendered state/code path.
- Load **at most one** specialist reference unless a concrete issue requires another.
- Stop reading once the top evidence-backed problems and direction are clear.

## Contract
Capture only what matters:
```text
OUTCOME:
MUST PRESERVE:
ALLOWED TO CHANGE:
ACCEPTANCE:
BLOCKED:
```

## Diagnose
Default to the top 3 problems:
```text
PROBLEM:
EVIDENCE:
USER IMPACT:
DIRECTION:
RISK:
```

## Phase
- `REVIEW`: report only.
- `REFINE`: keep accepted structure and fix local issues.
- `REDESIGN`: use only when systemic evidence shows local fixes would become patches.
- `IMPLEMENT`: build the selected direction.

## Preserve
Keep working workflows, state, routes, integrations, shortcuts, accessibility, responsive behavior, and useful identity.

## Composition
Check:
1. first visual anchor;
2. primary action;
3. primary work/content;
4. current state;
5. secondary controls;
6. tertiary metadata.

Visual mass should follow task importance.

## Escalation
Move to REDESIGN when several shared causes conflict across color, typography, spacing, surfaces, action hierarchy, composition, imagery, or product identity.

Do not rewrite business logic because the visual layer is weak.

## Specialist routing
- color-only problem → `../color/SKILL.md`
- broad visual identity → `../visual/SKILL.md`
- web behavior → `../web/SKILL.md`
- native app behavior → `../application/SKILL.md`
- system/components → `../design-system/SKILL.md`
- final runtime audit → `../qa/SKILL.md`


## Direction deliberation

When REVIEW concludes that REDESIGN is justified and the new direction is not already specified, route to `../design-strategy/SKILL.md` before implementation.

Do not let diagnosis silently become the first design idea.
