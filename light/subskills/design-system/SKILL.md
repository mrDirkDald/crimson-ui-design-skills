---
name: crimson-ui-design-system
description: Shared tokens, components, variants, icon contracts, theme parity, and design-system consistency.
---

# Design System

Use only when the shared system itself is material.


## Owner reference

`../../references/design-system.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- shared tokens/components/variants change;
- theme parity/drift is systemic;
- the fix propagates across surfaces;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Read `../../references/design-system.md`.
Do not load app/web references unless a concrete component behavior depends on them.

## Trace before editing
Prove the token/component reaches the target surface via imports, resolved theme usage, props/variants, inheritance, or rendered output.

Naming similarity is not proof.

## Scope
- semantic tokens;
- component states;
- typography/spacing scales;
- color token architecture;
- theme parity;
- SVG icon contract;
- variant/state drift;
- smallest governing fix.

Do not globally promote a local illustration/decorative color into the design system without evidence.
