---
name: crimson-ui-design-system
description: Shared tokens, components, variants, icon contracts, theme parity, and design-system consistency.
---

# Design System

Use only when the shared system itself is material.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Token Architecture | `aspects/token-architecture/SKILL.md` | Create layered raw, semantic, and component tokens without turning the system into hardcoded aliases. |
| Component Contracts and Variants | `aspects/component-contracts/SKILL.md` | Define component anatomy, variants, slots, states, and composition boundaries consistently. |
| Theme System | `aspects/theme-system/SKILL.md` | Build light/dark/high-contrast or branded themes as semantic remapping instead of duplicated component styling. |
| Icon System | `aspects/icon-system/SKILL.md` | Standardize icon source, sizing, semantics, and accessibility across the product. |
| Governance and Drift Detection | `aspects/governance-drift/SKILL.md` | Detect and prevent token, component, visual, and naming drift across a growing product. |
| Design System Migration | `aspects/migration-strategy/SKILL.md` | Move from legacy styling/components to a new system without requiring a risky all-at-once rewrite. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

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
