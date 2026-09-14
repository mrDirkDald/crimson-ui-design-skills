---
name: crimson-ui-implementation
description: Focused TypeScript/Tailwind design implementation, component styling, responsive utilities, tokens, and SVG integration.
---

# TypeScript / Tailwind Implementation

Use when design decisions are already clear and implementation details matter.


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
