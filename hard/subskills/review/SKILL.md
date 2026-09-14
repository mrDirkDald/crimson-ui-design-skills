---
name: crimson-ui-review
description: Focused UI/UX diagnosis, preservation, refine-vs-redesign decisions, and scope control.
---

# Review / Refine

Use this as the default primary subskill for UI review or improvement requests.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Evidence Audit | `aspects/evidence-audit/SKILL.md` | Prove what actually governs the target UI before making design claims. |
| Preservation Contract | `aspects/preservation-contract/SKILL.md` | Define what must survive a redesign so visual improvement does not break product behavior. |
| Refine vs Redesign | `aspects/refine-vs-redesign/SKILL.md` | Choose the smallest design phase that can solve the real problem without patch accumulation. |
| Severity and Prioritization | `aspects/severity-prioritization/SKILL.md` | Rank issues by user impact rather than by visual annoyance. |
| Product-Specificity Review | `aspects/product-specificity-review/SKILL.md` | Detect generic AI-template design and reconnect structure to the product's real domain. |
| Before / After Verification | `aspects/before-after-verification/SKILL.md` | Verify that the redesign actually improved the same product state rather than only producing a prettier screenshot. |

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
