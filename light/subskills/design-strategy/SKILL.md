---
name: crimson-ui-design-strategy
description: Compare plausible design directions, explain why one fits the product best, and avoid committing to the first visually attractive idea.
---

# Design Strategy

Use for meaningful redesigns, ambiguous visual direction, or whenever the user asks what design should be used and why.

## Owner reference

`../../references/design-deliberation.md`

Load it for TIER 1+ design-direction work.

### Escalation triggers
- several plausible layout/identity directions exist;
- the current design is systemically weak;
- the user asks for the best design rather than a predetermined design;
- a major hero/navigation/workspace/composition decision is being made;
- expressive identity or product-specificity is material.

For a trivial local fix, do not generate artificial alternatives.

## Required reasoning pattern

For meaningful REDESIGN:
1. understand product, audience, primary job and must-preserve behavior;
2. identify the governing problems;
3. generate 2–4 materially different directions;
4. compare them against product-specific criteria;
5. select one;
6. explain **why this one**, **why not the strongest alternative**, and the accepted tradeoff;
7. only then implement.

Do not present several weak variants just to satisfy a number.

## Candidate quality

Candidates must differ structurally or strategically, not merely by color/theme.

Consider differences in:
- IA/layout;
- workspace density;
- action hierarchy;
- typography/image relationship;
- interaction model;
- motion/media role;
- platform convention vs custom identity.

## Selection output

```text
SELECTED DIRECTION:
WHY IT FITS:
WHY IT BEATS ALTERNATIVE B:
TRADEOFF:
IDENTITY SOURCE:
RUNTIME PROOF NEEDED:
```

## Specialist routing

After choosing the direction:
- visual execution → `../visual/SKILL.md`
- color → `../color/SKILL.md`
- web mechanics → `../web/SKILL.md`
- application workflow → `../application/SKILL.md`
- implementation architecture → `../implementation/SKILL.md`
- final audit → `../qa/SKILL.md`
