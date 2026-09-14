---
name: crimson-ui-implementation
description: Focused TypeScript/Tailwind design implementation, component styling, responsive utilities, tokens, and SVG integration.
---

# TypeScript / Tailwind Implementation

Use when design decisions are already clear and implementation details matter.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| CSS and Styling Architecture | `aspects/css-architecture/SKILL.md` | Translate design decisions into maintainable styles without arbitrary-value drift. |
| React / TypeScript / Tailwind | `aspects/react-typescript-tailwind/SKILL.md` | Implement design systems and interaction states cleanly in component-driven TS/Tailwind applications. |
| Responsive Implementation | `aspects/responsive-implementation/SKILL.md` | Encode adaptive behavior with content-driven rules instead of breakpoint patch stacks. |
| Stateful Component Implementation | `aspects/stateful-components/SKILL.md` | Implement loading, error, selection, focus, validation, disabled, optimistic, and transient states explicitly. |
| SVG and Lucide Implementation | `aspects/svg-lucide/SKILL.md` | Implement consistent accessible icons across web and app renderers. |
| Design-to-Code Verification | `aspects/design-to-code-verification/SKILL.md` | Compare implementation against the intended design system and actual runtime constraints. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

## Owner reference

`../../references/typescript-tailwind.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- implementation spans multiple components;
- token architecture or responsive utilities change;
- Tailwind/TS choices affect maintainability;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Read only `../../references/typescript-tailwind.md`.

## Rules
- reuse existing components/tokens first;
- avoid arbitrary-value accumulation;
- use semantic tokens over per-component raw colors;
- preserve behavior/API/state;
- avoid unrelated refactors;
- SVG icons instead of emoji controls;
- keep responsive behavior intentional;
- run build/type/lint/tests relevant to the change.

Do not reopen broad visual references unless implementation exposes a real design conflict.
